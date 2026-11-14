"""Identity's persistence (ADU-03, layer 3): the member rows of the data model (models.Member).

Every function works in the session the service passes, which is always db.current_session() (D-14): nothing
here opens, commits or closes a session, reads the clock or checks a rule. Emails and names are compared
case-insensitively with str.lower, the data model's lower(email) (models.py, R-identity-02) applied in Python
so that a non-ASCII letter folds too.
"""

from __future__ import annotations

from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.models import Member

ADMIN = "admin"


def get(session: Session, member_id: int) -> Member | None:
    return session.get(Member, member_id)


def all_members(session: Session) -> list[Member]:
    """Every member, active and inactive, by id."""
    return list(session.scalars(select(Member).order_by(Member.id)))


def count(session: Session) -> int:
    return session.scalar(select(func.count()).select_from(Member)) or 0


def by_email(session: Session, email: str) -> Member | None:
    """The member whose email equals `email` compared case-insensitively (R-identity-02), active or not."""
    wanted = email.lower()
    return next((m for m in all_members(session) if m.email.lower() == wanted), None)


def by_token(session: Session, token: str) -> Member | None:
    """The member holding `token` as their one token, compared exactly."""
    return session.scalars(select(Member).where(Member.token == token)).first()


def active_admin_count(session: Session) -> int:
    query = select(func.count()).select_from(Member).where(Member.active.is_(True), Member.role == ADMIN)
    return session.scalar(query) or 0


def add(session: Session, *, name: str, email: str, role: str, passcode_hash: str) -> Member:
    """A new active member; flushed, so the store has assigned its id."""
    member = Member(name=name, email=email, role=role, active=True, passcode_hash=passcode_hash, token=None)
    session.add(member)
    session.flush()
    return member
