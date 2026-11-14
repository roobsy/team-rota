"""Scheduling's persistence (ADU-05, layer 3): the week, shift and assignment rows of the data model.

Every function works in the session the service passes, which is always db.current_session() (D-14): nothing
here opens, commits or closes a session, reads the clock or checks a rule. Members are identity's rows and are
never read here; scheduling asks MemberDirectory (IR-06, IR-12).
"""

from __future__ import annotations

from collections.abc import Iterable
from datetime import date, time

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models import Assignment, Shift, Week

DRAFT = "draft"


# ---- weeks
def get_week(session: Session, start_date: date) -> Week | None:
    return session.get(Week, start_date)


def all_weeks(session: Session) -> list[Week]:
    """Every week, newest first by start_date (the key: no tie)."""
    return list(session.scalars(select(Week).order_by(Week.start_date.desc())))


def add_week(session: Session, start_date: date) -> Week:
    """A new week in state draft; flushed."""
    week = Week(start_date=start_date, state=DRAFT)
    session.add(week)
    session.flush()
    return week


# ---- shifts
def get_shift(session: Session, shift_id: int) -> Shift | None:
    return session.get(Shift, shift_id)


def shifts_of_week(session: Session, start_date: date) -> list[Shift]:
    """The week's shifts in board order: date, start, then id (R-scheduling-05)."""
    query = select(Shift).where(Shift.week_start == start_date).order_by(Shift.date, Shift.start, Shift.id)
    return list(session.scalars(query))


def add_shift(session: Session, *, week_start: date, day: date, start: time, end: time, slots: int) -> Shift:
    """A new shift; flushed, so the store has assigned its id."""
    shift = Shift(week_start=week_start, date=day, start=start, end=end, slots=slots)
    session.add(shift)
    session.flush()
    return shift


def shifts_held_on(session: Session, member_id: int, day: date) -> list[Shift]:
    """The shifts on `day` on which the member holds a slot."""
    query = (
        select(Shift)
        .join(Assignment, Assignment.shift_id == Shift.id)
        .where(Assignment.member_id == member_id, Shift.date == day)
    )
    return list(session.scalars(query))


def shifts_held_by(session: Session, member_id: int) -> list[Shift]:
    """Every shift, in any week, on which the member holds a slot."""
    query = (
        select(Shift)
        .join(Assignment, Assignment.shift_id == Shift.id)
        .where(Assignment.member_id == member_id)
    )
    return list(session.scalars(query))


# ---- assignments
def get_assignment(session: Session, assignment_id: int) -> Assignment | None:
    return session.get(Assignment, assignment_id)


def assignments_of_shifts(session: Session, shift_ids: Iterable[int]) -> list[Assignment]:
    """The assignments of the given shifts, by assignment id ascending."""
    ids = list(shift_ids)
    if not ids:
        return []
    query = select(Assignment).where(Assignment.shift_id.in_(ids)).order_by(Assignment.id)
    return list(session.scalars(query))


def add_assignment(session: Session, *, shift_id: int, member_id: int) -> Assignment:
    """A new assignment; flushed, so the store has assigned its id."""
    assignment = Assignment(shift_id=shift_id, member_id=member_id)
    session.add(assignment)
    session.flush()
    return assignment


def delete_assignment(session: Session, assignment: Assignment) -> None:
    session.delete(assignment)
    session.flush()
