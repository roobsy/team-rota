"""The five in-process protocols of design/INTERFACES.md (layer 2). Imports nothing of the product.

A domain reaches another only through these; the composition root binds the Null implementations until each
provider lands (class replaced, shape kept). Values are frozen dataclasses; events are self-contained
payloads.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date, datetime, time
from typing import Iterable, Protocol, runtime_checkable

Role = str
EVENT_CODES = (
    "week_published",
    "swap_requested",
    "swap_accepted",
    "swap_declined",
    "swap_approved",
    "swap_refused",
    "member_added",
    "role_changed",
    "member_deactivated",
)


class MemberNotFound(LookupError):
    pass


class AssignmentNotFound(LookupError):
    pass


class TransferRefused(Exception):
    """reason is one of counterpart_overlap, counterpart_inactive and nothing else (IR-02)."""

    def __init__(self, reason: str) -> None:
        super().__init__(reason)
        self.reason = reason


class Refused(Exception):
    """The one domain refusal (D-13; design/INTERFACES.md, Refused): reason is a code of PRODUCT-DESIGN's
    Reason codes table, detail the refusal's plain sentence, extra the fields a story names. It carries no
    HTTP status (the API layer maps the reason to its bucket's status, D-07); a refusal changes nothing."""

    def __init__(self, reason: str, detail: str = "", **extra: object) -> None:
        super().__init__(reason)
        self.reason, self.detail, self.extra = reason, detail, extra


@dataclass(frozen=True)
class Caller:
    member_id: int
    name: str
    role: Role
    active: bool


@dataclass(frozen=True)
class AssignmentInfo:  # IR-01
    assignment_id: int
    holder_id: int
    shift_id: int
    shift_date: date
    start: time
    end: time
    start_at: datetime
    week_start: date
    week_state: str
    holder_ids: tuple[int, ...]


@dataclass(frozen=True)
class AssignmentView:  # IR-07
    pending: str | None
    requestable: bool


# ---- the nine events of R-notifications-01, each self-contained; recipients are named by the emitter
@dataclass(frozen=True)
class WeekPublished:
    code = "week_published"
    start_date: date
    recipient_ids: tuple[int, ...]


@dataclass(frozen=True)
class SwapRequested:
    code = "swap_requested"
    request_id: int
    shift_date: date
    shift_start: time
    requester_name: str
    reason: str
    recipient_id: int


@dataclass(frozen=True)
class SwapAccepted:
    code = "swap_accepted"
    request_id: int
    shift_date: date
    shift_start: time
    counterpart_name: str
    recipient_ids: tuple[int, ...]


@dataclass(frozen=True)
class SwapDeclined:
    code = "swap_declined"
    request_id: int
    shift_date: date
    shift_start: time
    counterpart_name: str
    reason: str
    recipient_id: int


@dataclass(frozen=True)
class SwapApproved:
    code = "swap_approved"
    request_id: int
    shift_date: date
    shift_start: time
    new_holder_name: str
    recipient_ids: tuple[int, ...]


@dataclass(frozen=True)
class SwapRefused:
    code = "swap_refused"
    request_id: int
    shift_date: date
    shift_start: time
    reason: str
    recipient_ids: tuple[int, ...]


@dataclass(frozen=True)
class MemberAdded:
    code = "member_added"
    member_id: int
    role: Role


@dataclass(frozen=True)
class RoleChanged:
    code = "role_changed"
    member_id: int
    role: Role


@dataclass(frozen=True)
class MemberDeactivated:
    code = "member_deactivated"
    member_id: int


Event = (
    WeekPublished
    | SwapRequested
    | SwapAccepted
    | SwapDeclined
    | SwapApproved
    | SwapRefused
    | MemberAdded
    | RoleChanged
    | MemberDeactivated
)


@runtime_checkable
class Clock(Protocol):
    def now(self) -> datetime: ...  # naive local time of the team


class SystemClock:
    """The product's clock; tests use FixedClock from tests/support/doubles.py."""

    def now(self) -> datetime:
        return datetime.now().replace(microsecond=0)


@runtime_checkable
class MemberDirectory(Protocol):
    def caller_for_token(self, token: str) -> Caller | None: ...  # IR-11; None for unknown or inactive
    def is_active(self, member_id: int) -> bool | None: ...  # None for an id that names no member
    def role_of(self, member_id: int) -> Role: ...  # raises MemberNotFound
    def name_of(self, member_id: int) -> str: ...
    def active_member_ids(self) -> list[int]: ...  # IR-12
    def decider_ids(self) -> list[int]: ...  # active admins and planners


@runtime_checkable
class SchedulingPort(Protocol):
    def assignment(self, assignment_id: int) -> AssignmentInfo: ...  # raises AssignmentNotFound
    def holds_intersecting_shift(self, member_id: int, shift_id: int) -> bool: ...
    def transfer(
        self, assignment_id: int, to_member_id: int
    ) -> None: ...  # raises TransferRefused; commits nothing
    def has_assignment_after(self, member_id: int, now: datetime) -> bool: ...  # IR-05, any week


@runtime_checkable
class SwapsPort(Protocol):
    def view(
        self, caller_id: int, week_published: bool, assignments: Iterable[tuple[int, int, datetime]]
    ) -> dict[int, AssignmentView]: ...  # (assignment_id, holder_id, start_at) → per assignment


@runtime_checkable
class Notifier(Protocol):
    def notify(self, event: Event) -> None: ...  # one notification per recipient, in the caller's session
