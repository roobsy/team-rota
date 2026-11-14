"""The notifications service (ADU-09, layer 3): the Notifier that identity, scheduling and swaps call, and
the two reads of the notifications API (design/INTERFACES.md, Notifier; contracts/openapi.yaml,
notifications.list and notifications.mark_read).

- Sessions (D-14). Every method reads and writes in db.current_session() and never opens, commits or closes
  one. Each method takes that session before anything else, so with none current db.NoCurrentSession
  propagates, even from a notify that has nobody to write to.
- Bindings (D-15). The clock and the member directory are the composition root's bindings, read at call
  time; main.Ports satisfies Bindings, so notifications never imports main or identity.
- Recipients (R-notifications-01, -03; IR-04). One notification per recipient the payload names, each once.
  A recipient identity does not answer active for is skipped, except for MemberDeactivated, whose recipient
  is the member just deactivated. The directory is asked nothing else.
- Text (R-notifications-02). Composed from the payload alone. It names the state as it is (the past
  participle of the event's code) and the reason when there is one. The date is ISO and the start HH:MM, as
  the contract's examples render them. Ids are carried, never shown.
- Values (D-17's reading). Both reads answer NotificationValue, the contract's Notification, as a frozen
  value defined here.
"""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
from datetime import date, datetime, time
from typing import Protocol

from app import db, models
from app.notifications import repo
from app.ports import (
    Caller,
    Clock,
    Event,
    MemberAdded,
    MemberDeactivated,
    MemberDirectory,
    Refused,
    RoleChanged,
    SwapAccepted,
    SwapApproved,
    SwapDeclined,
    SwapRefused,
    SwapRequested,
    WeekPublished,
)


class Bindings(Protocol):
    """The composition root's bindings the service reads (D-15); main.Ports satisfies it."""

    clock: Clock
    member_directory: MemberDirectory


@dataclass(frozen=True)
class NotificationValue:
    """The contract's Notification (contracts/openapi.yaml, Notification); created_at is naive local time."""

    id: int
    recipient_id: int
    event: str
    text: str
    created_at: datetime
    read: bool


def _value(notification: models.Notification) -> NotificationValue:
    return NotificationValue(
        id=notification.id,
        recipient_id=notification.recipient_id,
        event=notification.event,
        text=notification.text,
        created_at=notification.created_at,
        read=notification.read,
    )


def recipients_of(event: Event) -> tuple[int, ...]:
    """The member ids the emitter named in the payload, in its order (R-notifications-01)."""
    match event:
        case WeekPublished() | SwapAccepted() | SwapApproved() | SwapRefused():
            return tuple(event.recipient_ids)
        case SwapRequested() | SwapDeclined():
            return (event.recipient_id,)
        case MemberAdded() | RoleChanged() | MemberDeactivated():
            return (event.member_id,)
    raise TypeError(f"not one of the nine events of R-notifications-01: {event!r}")


def _shift(shift_date: date, shift_start: time) -> str:
    return f"{shift_date.isoformat()} {shift_start.strftime('%H:%M')}"


def text_of(event: Event) -> str:
    """The notification's text, from the payload alone (R-notifications-02)."""
    match event:
        case WeekPublished():
            return f"The week of {event.start_date.isoformat()} is published."
        case SwapRequested():
            shift = _shift(event.shift_date, event.shift_start)
            return (
                f"{event.requester_name} requested that you take {shift} ({event.reason}); "
                "it awaits your answer."
            )
        case SwapAccepted():
            shift = _shift(event.shift_date, event.shift_start)
            return f"{event.counterpart_name} accepted the swap of {shift}; it awaits a decision."
        case SwapDeclined():
            shift = _shift(event.shift_date, event.shift_start)
            return f"{event.counterpart_name} declined the swap of {shift} ({event.reason})."
        case SwapApproved():
            shift = _shift(event.shift_date, event.shift_start)
            return f"The swap of {shift} is approved; {event.new_holder_name} now holds the shift."
        case SwapRefused():
            shift = _shift(event.shift_date, event.shift_start)
            return f"The swap of {shift} is refused ({event.reason})."
        case MemberAdded():
            return f"You were added to the team as {event.role}."
        case RoleChanged():
            return f"Your role was changed to {event.role}."
        case MemberDeactivated():
            return "Your membership was deactivated; you can no longer sign in."
    raise TypeError(f"not one of the nine events of R-notifications-01: {event!r}")


class NotificationsService:
    """Implements ports.Notifier and the notifications reads; the composition root binds it as
    Ports.notifier (ADU-09 arm 1)."""

    def __init__(self, bound: Callable[[], Bindings]) -> None:
        self._bound = bound

    # ---- Notifier (IR-03, IR-08, IR-10; the one lookup is IR-04)
    def notify(self, event: Event) -> None:
        """One unread notification per recipient the payload names, each once, written in the caller's
        session; an inactive recipient gets none, except for MemberDeactivated (R-notifications-01, -03)."""
        session = db.current_session()
        bound = self._bound()
        text = text_of(event)
        created_at = bound.clock.now()
        reaches_the_inactive = isinstance(event, MemberDeactivated)
        for recipient_id in dict.fromkeys(recipients_of(event)):
            if not reaches_the_inactive and not bound.member_directory.is_active(recipient_id):
                continue
            repo.add(session, recipient_id=recipient_id, event=event.code, text=text, created_at=created_at)

    # ---- operations (contracts/openapi.yaml, notifications.list and notifications.mark_read)
    def list(self, caller: Caller) -> list[NotificationValue]:
        """The caller's own notifications, newest first by created_at, then id descending; nobody else's
        (R-notifications-04)."""
        return [_value(n) for n in repo.of_recipient(db.current_session(), caller.member_id)]

    def mark_read(self, caller: Caller, notification_id: int) -> NotificationValue:
        """Sets read on one of the caller's notifications and answers it; marking again changes nothing and
        succeeds (R-notifications-04). An id that names nothing is not_found; another member's is
        not_recipient, which needs the row to tell."""
        session = db.current_session()
        notification = repo.get(session, notification_id)
        if notification is None:
            raise Refused("not_found", f"No notification has the id {notification_id}.")
        if notification.recipient_id != caller.member_id:
            raise Refused("not_recipient", "This notification is not yours.")
        if not notification.read:
            notification.read = True
        return _value(notification)
