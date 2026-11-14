"""Notifications' persistence (ADU-09, layer 3): the notification rows of the data model
(models.Notification).

Every function works in the session the service passes, which is always db.current_session() (D-14): nothing
here opens, commits or closes a session, reads the clock or checks a rule.
"""

from __future__ import annotations

from datetime import datetime

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models import Notification


def add(session: Session, *, recipient_id: int, event: str, text: str, created_at: datetime) -> Notification:
    """A new unread notification; flushed, so the store has assigned its id and checked its recipient."""
    notification = Notification(
        recipient_id=recipient_id, event=event, text=text, created_at=created_at, read=False
    )
    session.add(notification)
    session.flush()
    return notification


def get(session: Session, notification_id: int) -> Notification | None:
    return session.get(Notification, notification_id)


def of_recipient(session: Session, recipient_id: int) -> list[Notification]:
    """The recipient's own notifications, newest first by created_at, then id descending
    (R-notifications-04)."""
    query = (
        select(Notification)
        .where(Notification.recipient_id == recipient_id)
        .order_by(Notification.created_at.desc(), Notification.id.desc())
    )
    return list(session.scalars(query))
