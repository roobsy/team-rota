"""The stored entities of PRODUCT-DESIGN §Entities (design v1.7, D-02). Layer 1: imports nothing of the
product.

Timestamps are naive local datetimes (the team's one timezone); dates are dates; shift times are times of day.
Ids are integers assigned by the store in creation order; Week is keyed by its start_date; Role is an
enumeration carried in Member.role, not a row. Nothing here reads the clock: every timestamp is given by the
caller.
"""

from __future__ import annotations

import hashlib
from datetime import date, datetime, time

from sqlalchemy import (
    Boolean,
    CheckConstraint,
    Date,
    DateTime,
    ForeignKey,
    Index,
    Integer,
    String,
    Time,
    UniqueConstraint,
    func,
)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

ROLES = ("admin", "planner", "member")
WEEK_STATES = ("draft", "published")
REQUEST_STATES = ("requested", "accepted", "declined", "approved", "refused")
DECISION_OUTCOMES = ("approved", "refused")
EVENTS = (
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


def _in(column: str, values: tuple[str, ...], name: str) -> CheckConstraint:
    quoted = ", ".join(f"'{v}'" for v in values)
    return CheckConstraint(f"{column} IN ({quoted})", name=name)


def hash_passcode(passcode: str, salt: str) -> str:
    """A salted SHA-256 from the standard library (D-04): a passcode is represented by its hash."""
    return salt + "$" + hashlib.sha256((salt + passcode).encode("utf-8")).hexdigest()


class Base(DeclarativeBase):
    pass


class Member(Base):
    __tablename__ = "members"
    __table_args__ = (_in("role", ROLES, "ck_member_role"),)
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=False)
    role: Mapped[str] = mapped_column(String, nullable=False)
    active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
    passcode_hash: Mapped[str] = mapped_column(String, nullable=False)
    token: Mapped[str | None] = mapped_column(String, nullable=True, unique=True)


# email unique compared case-insensitively (R-identity-02): a unique index on lower(email)
Index("ix_members_email_lower", func.lower(Member.email), unique=True)


class Week(Base):
    __tablename__ = "weeks"
    __table_args__ = (_in("state", WEEK_STATES, "ck_week_state"),)
    start_date: Mapped[date] = mapped_column(Date, primary_key=True)
    state: Mapped[str] = mapped_column(String, nullable=False, default="draft")


class Shift(Base):
    __tablename__ = "shifts"
    __table_args__ = (
        CheckConstraint("slots >= 1", name="ck_shift_slots"),
        CheckConstraint('"end" > "start"', name="ck_shift_interval"),
    )
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    week_start: Mapped[date] = mapped_column(Date, ForeignKey("weeks.start_date"), nullable=False)
    date: Mapped[date] = mapped_column(Date, nullable=False)
    start: Mapped[time] = mapped_column(Time, nullable=False)
    end: Mapped[time] = mapped_column(Time, nullable=False)
    slots: Mapped[int] = mapped_column(Integer, nullable=False)


class Assignment(Base):
    __tablename__ = "assignments"
    __table_args__ = (UniqueConstraint("shift_id", "member_id", name="uq_assignment_shift_member"),)
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    shift_id: Mapped[int] = mapped_column(Integer, ForeignKey("shifts.id"), nullable=False)
    member_id: Mapped[int] = mapped_column(Integer, ForeignKey("members.id"), nullable=False)


class SwapRequest(Base):
    """One open request per assignment is the swaps service's rule (R-swaps-02), not a database constraint:
    'open' depends on the clock (R-swaps-06), which the store never reads."""

    __tablename__ = "swap_requests"
    __table_args__ = (_in("state", REQUEST_STATES, "ck_request_state"),)
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    assignment_id: Mapped[int] = mapped_column(Integer, ForeignKey("assignments.id"), nullable=False)
    requester_id: Mapped[int] = mapped_column(Integer, ForeignKey("members.id"), nullable=False)
    counterpart_id: Mapped[int] = mapped_column(Integer, ForeignKey("members.id"), nullable=False)
    reason: Mapped[str] = mapped_column(String, nullable=False)
    state: Mapped[str] = mapped_column(String, nullable=False, default="requested")
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=False), nullable=False)
    answered_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=False), nullable=True)
    answer_reason: Mapped[str | None] = mapped_column(String, nullable=True)


class Decision(Base):
    __tablename__ = "decisions"
    __table_args__ = (_in("outcome", DECISION_OUTCOMES, "ck_decision_outcome"),)
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    request_id: Mapped[int] = mapped_column(Integer, ForeignKey("swap_requests.id"), nullable=False)
    decider_id: Mapped[int] = mapped_column(Integer, ForeignKey("members.id"), nullable=False)
    outcome: Mapped[str] = mapped_column(String, nullable=False)
    reason: Mapped[str | None] = mapped_column(String, nullable=True)
    decided_at: Mapped[datetime] = mapped_column(DateTime(timezone=False), nullable=False)


class Notification(Base):
    __tablename__ = "notifications"
    __table_args__ = (_in("event", EVENTS, "ck_notification_event"),)
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    recipient_id: Mapped[int] = mapped_column(Integer, ForeignKey("members.id"), nullable=False)
    event: Mapped[str] = mapped_column(String, nullable=False)
    text: Mapped[str] = mapped_column(String, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=False), nullable=False)
    read: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
