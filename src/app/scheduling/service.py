"""The scheduling service (ADU-05, layer 3): weeks, shifts and assignments, the week board and the weeks list,
and the SchedulingPort that swaps (IR-01, IR-02) and identity (IR-05) read (design/INTERFACES.md,
SchedulingPort; the values and signatures are Q-18's ruling, OPEN-QUESTIONS.md).

- Sessions (D-14). Every method takes db.current_session() before anything else and never opens, commits or
  closes one, so with none current db.NoCurrentSession propagates. The transfer writes in the caller's
  session.
- Refusals. Every refusal is ports.Refused; the transfer's is ports.TransferRefused (IR-02), never Refused.
  Checks run per operation in the order Q-18 accepted (forbidden → not_found → state → validation, and within
  a bucket the arms' order; R-scheduling-07 for assign), and every check comes before the first write.
- Bindings (D-15). The clock, the member directory, the swaps port and the notifier are the composition root's
  bindings, read at call time.
- Identity. Whether a member is active, a holder's name and the active members come from MemberDirectory
  (IR-06, IR-12), never from identity's rows; forbidden is judged on the Caller's role.
- Cases no arm names (built, not pinned by a test): transfer to an id that names no member answers
  counterpart_inactive, and overlap is checked before inactive (Q-19 (a)); holds_intersecting_shift for an
  unknown shift answers False (Q-19 (a)); transfer of an unknown assignment raises AssignmentNotFound
  (Q-20 (a)).
"""

from __future__ import annotations

from collections import Counter
from collections.abc import Callable
from dataclasses import dataclass
from datetime import date, datetime, time
from typing import Protocol

from sqlalchemy.orm import Session

from app import db, models
from app.ports import (
    AssignmentInfo,
    AssignmentNotFound,
    Caller,
    Clock,
    MemberDirectory,
    Notifier,
    Refused,
    SwapsPort,
    TransferRefused,
    WeekPublished,
)
from app.scheduling import repo, rules

PLANNING_ROLES = ("admin", "planner")  # create, assign, unassign, publish; see draft weeks (Permissions)
DRAFT, PUBLISHED = "draft", "published"


class Bindings(Protocol):
    """The composition root's bindings the service reads (D-15); main.Ports satisfies it, so scheduling never
    imports main."""

    clock: Clock
    member_directory: MemberDirectory
    swaps: SwapsPort
    notifier: Notifier


@dataclass(frozen=True)
class HolderValue:
    """One holder-row of a shift (R-scheduling-05; the contract's Holder)."""

    assignment_id: int
    member_id: int
    name: str
    pending: str | None
    requestable: bool


@dataclass(frozen=True)
class ShiftRow:
    """A shift with its holder-rows, as the board shows it; create_shift answers it with holders=() (Q-18)."""

    id: int
    week_start: date
    date: date
    start: time
    end: time
    slots: int
    holders: tuple[HolderValue, ...]


@dataclass(frozen=True)
class BoardValue:
    """The board {start_date, state, shifts} (R-scheduling-05; Q-18 (a))."""

    start_date: date
    state: str
    shifts: tuple[ShiftRow, ...]


@dataclass(frozen=True)
class AssignmentValue:
    """The contract's Assignment, assign's answer (Q-18)."""

    id: int
    shift_id: int
    member_id: int


@dataclass(frozen=True)
class WeekValue:
    """The contract's Week, publish's answer and a row of the weeks list (Q-18)."""

    start_date: date
    state: str


@dataclass(frozen=True)
class WeeksValue:
    """The weeks list {weeks, current} (R-scheduling-06; the contract's Weeks)."""

    weeks: tuple[WeekValue, ...]
    current: date | None


@dataclass(frozen=True)
class UnfilledShift:
    """One row of publish's unfilled_slots refusal (R-scheduling-03; the contract's UnfilledShift)."""

    shift_id: int
    date: date
    start: time
    unfilled: int


def _hhmm(t: time) -> str:
    return t.isoformat("minutes")


def _shift_row(shift: models.Shift, holders: tuple[HolderValue, ...]) -> ShiftRow:
    return ShiftRow(
        id=shift.id,
        week_start=shift.week_start,
        date=shift.date,
        start=shift.start,
        end=shift.end,
        slots=shift.slots,
        holders=holders,
    )


def _holds_intersecting(session: Session, member_id: int, shift: models.Shift) -> bool:
    """Whether the member holds a slot on `shift` itself or on a shift of its date whose [start, end)
    intersects it (R-scheduling-02: a slot on the same shift counts)."""
    return any(
        held.id == shift.id or rules.intersects(shift.start, shift.end, held.start, held.end)
        for held in repo.shifts_held_on(session, member_id, shift.date)
    )


def _interval_detail(start: str | None, end: str | None, start_t: time | None, end_t: time | None) -> str:
    if start_t is None or end_t is None:
        return "Start and end must be times of day (HH:MM), at most 23:59."
    return f"End {end} is not after start {start}."


class SchedulingService:
    """Implements ports.SchedulingPort and the scheduling operations; the composition root binds it as
    Ports.scheduling (ADU-05 arm 1)."""

    def __init__(self, bound: Callable[[], Bindings]) -> None:
        self._bound = bound

    # ---- SchedulingPort (IR-01, IR-02, IR-05)
    def assignment(self, assignment_id: int) -> AssignmentInfo:
        """The assignment, its shift's times and start instant, its week's state and the shift's current
        holder ids (IR-01); raises AssignmentNotFound."""
        session = db.current_session()
        assignment = repo.get_assignment(session, assignment_id)
        if assignment is None:
            raise AssignmentNotFound(assignment_id)
        shift = repo.get_shift(session, assignment.shift_id)
        week = repo.get_week(session, shift.week_start)
        holders = repo.assignments_of_shifts(session, [shift.id])
        return AssignmentInfo(
            assignment_id=assignment.id,
            holder_id=assignment.member_id,
            shift_id=shift.id,
            shift_date=shift.date,
            start=shift.start,
            end=shift.end,
            start_at=rules.start_instant(shift.date, shift.start),
            week_start=shift.week_start,
            week_state=week.state,
            holder_ids=tuple(a.member_id for a in holders),
        )

    def holds_intersecting_shift(self, member_id: int, shift_id: int) -> bool:
        """IR-01. A shift id that names no shift answers False (Q-19 (a))."""
        session = db.current_session()
        shift = repo.get_shift(session, shift_id)
        return shift is not None and _holds_intersecting(session, member_id, shift)

    def transfer(self, assignment_id: int, to_member_id: int) -> None:
        """IR-02, R-scheduling-08: the counterpart becomes the assignment's holder, written in the caller's
        session and committed by the caller. Refused with TransferRefused counterpart_overlap, then
        counterpart_inactive (Q-19 (a)), the assignment unchanged."""
        session = db.current_session()
        assignment = repo.get_assignment(session, assignment_id)
        if assignment is None:
            raise AssignmentNotFound(assignment_id)  # Q-20 (a)
        shift = repo.get_shift(session, assignment.shift_id)
        if _holds_intersecting(session, to_member_id, shift):
            raise TransferRefused("counterpart_overlap")
        if not self._bound().member_directory.is_active(to_member_id):  # None, an unknown id, is not active
            raise TransferRefused("counterpart_inactive")
        assignment.member_id = to_member_id
        session.flush()

    def has_assignment_after(self, member_id: int, now: datetime) -> bool:
        """IR-05: any week, draft or published, with a shift start instant strictly after `now`."""
        session = db.current_session()
        return any(
            rules.start_instant(shift.date, shift.start) > now
            for shift in repo.shifts_held_by(session, member_id)
        )

    # ---- operations (the contract's operationIds scheduling.<action>)
    def create_shift(
        self,
        caller: Caller,
        start_date: date,
        date: date,
        start: str | None,
        end: str | None,
        slots: int | None,
    ) -> ShiftRow:
        """R-scheduling-01: the week comes into being in state draft with its first shift. Answers the shift
        with no holder-rows (Q-18)."""
        session = db.current_session()
        self._require_planner(caller, "create a shift")
        week = repo.get_week(session, start_date)
        if week is not None and week.state == PUBLISHED:
            raise Refused("week_published", f"The week of {start_date.isoformat()} is published.")
        if not rules.is_week_start(start_date):
            raise Refused("not_week_start", f"{start_date.isoformat()} is not a Monday.")
        if not rules.within_week(start_date, date):
            raise Refused(
                "outside_week", f"{date.isoformat()} is not within the week of {start_date.isoformat()}."
            )
        start_t, end_t = rules.time_of_day(start), rules.time_of_day(end)
        if not rules.valid_interval(start_t, end_t):
            raise Refused("invalid_interval", _interval_detail(start, end, start_t, end_t))
        if not rules.valid_slots(slots):
            raise Refused("invalid_slots", "Slots must be at least 1.")
        if week is None:
            week = repo.add_week(session, start_date)
        shift = repo.add_shift(
            session, week_start=week.start_date, day=date, start=start_t, end=end_t, slots=slots
        )
        return _shift_row(shift, ())

    def assign(self, caller: Caller, shift_id: int, member_id: int) -> AssignmentValue:
        """R-scheduling-02, -07: an active member takes a free slot. The state checks run week_published,
        already_assigned, overlapping_shift, shift_full, member_inactive."""
        session = db.current_session()
        self._require_planner(caller, "assign a member")
        shift = repo.get_shift(session, shift_id)
        if shift is None:
            raise Refused("not_found", f"No shift has the id {shift_id}.")
        directory = self._bound().member_directory
        active = directory.is_active(member_id)
        if active is None:
            raise Refused("not_found", f"No member has the id {member_id}.")
        week = repo.get_week(session, shift.week_start)
        if week.state == PUBLISHED:
            raise Refused("week_published", f"The week of {week.start_date.isoformat()} is published.")
        name = directory.name_of(member_id)
        held = repo.shifts_held_on(session, member_id, shift.date)
        if any(other.id == shift.id for other in held):
            raise Refused("already_assigned", f"{name} already holds this shift.")
        overlaps = (o for o in held if rules.intersects(shift.start, shift.end, o.start, o.end))
        overlap = next(overlaps, None)
        if overlap is not None:
            span = f"{overlap.date.isoformat()} {_hhmm(overlap.start)}–{_hhmm(overlap.end)}"
            raise Refused("overlapping_shift", f"{name} holds {span}, which overlaps.")
        if len(repo.assignments_of_shifts(session, [shift.id])) >= shift.slots:
            raise Refused("shift_full", f"All {shift.slots} slots are held.")
        if not active:
            raise Refused("member_inactive", f"{name} is inactive.")
        assignment = repo.add_assignment(session, shift_id=shift.id, member_id=member_id)
        return AssignmentValue(id=assignment.id, shift_id=assignment.shift_id, member_id=assignment.member_id)

    def unassign(self, caller: Caller, assignment_id: int) -> None:
        """R-scheduling-04: an assignment of a draft week may be removed, and its slot is free. Answers
        nothing."""
        session = db.current_session()
        self._require_planner(caller, "remove an assignment")
        assignment = repo.get_assignment(session, assignment_id)
        if assignment is None:
            raise Refused("not_found", f"No assignment has the id {assignment_id}.")
        shift = repo.get_shift(session, assignment.shift_id)
        week = repo.get_week(session, shift.week_start)
        if week.state == PUBLISHED:
            raise Refused("week_published", f"The week of {week.start_date.isoformat()} is published.")
        repo.delete_assignment(session, assignment)

    def publish(self, caller: Caller, start_date: date) -> WeekValue:
        """R-scheduling-03, -04: a draft week whose every slot is filled becomes published, and every active
        member is notified once (WeekPublished, IR-08, IR-12). Answers the week."""
        session = db.current_session()
        self._require_planner(caller, "publish a week")
        week = repo.get_week(session, start_date)
        if week is None:
            raise Refused("not_found", f"No week starts on {start_date.isoformat()}.")
        if week.state == PUBLISHED:
            raise Refused(
                "week_published", f"The week of {start_date.isoformat()} is already published.", unfilled=()
            )
        shifts = repo.shifts_of_week(session, start_date)
        held = Counter(a.shift_id for a in repo.assignments_of_shifts(session, [s.id for s in shifts]))
        unfilled = tuple(
            UnfilledShift(shift_id=s.id, date=s.date, start=s.start, unfilled=s.slots - held[s.id])
            for s in shifts
            if held[s.id] < s.slots
        )
        if unfilled:
            count = "1 shift has" if len(unfilled) == 1 else f"{len(unfilled)} shifts have"
            raise Refused("unfilled_slots", f"{count} unfilled slots.", unfilled=unfilled)
        week.state = PUBLISHED
        session.flush()
        bound = self._bound()
        recipients = tuple(dict.fromkeys(bound.member_directory.active_member_ids()))
        bound.notifier.notify(WeekPublished(start_date=week.start_date, recipient_ids=recipients))
        return WeekValue(start_date=week.start_date, state=week.state)

    def board(self, caller: Caller, start_date: date, mine: bool = False) -> BoardValue:
        """R-scheduling-05, -06: every shift by date, start, then id, and holder-rows by assignment id, with
        pending and requestable answered by swaps (IR-07). With mine, only the caller's shifts, each with all
        its holder-rows. A draft week is shown to planners and admins only."""
        session = db.current_session()
        week = repo.get_week(session, start_date)
        if week is None:
            raise Refused("not_found", f"No week starts on {start_date.isoformat()}.")
        if week.state == DRAFT and caller.role not in PLANNING_ROLES:
            raise Refused("week_draft", f"The week of {start_date.isoformat()} is a draft.")
        shifts = repo.shifts_of_week(session, start_date)
        by_shift: dict[int, list[models.Assignment]] = {s.id: [] for s in shifts}
        for assignment in repo.assignments_of_shifts(session, by_shift):
            by_shift[assignment.shift_id].append(assignment)
        if mine:
            shifts = [s for s in shifts if any(a.member_id == caller.member_id for a in by_shift[s.id])]
        bound = self._bound()
        facts = [
            (a.id, a.member_id, rules.start_instant(s.date, s.start)) for s in shifts for a in by_shift[s.id]
        ]
        views = bound.swaps.view(caller.member_id, week.state == PUBLISHED, facts)
        names: dict[int, str] = {}
        for _id, member_id, _at in facts:
            if member_id not in names:
                names[member_id] = bound.member_directory.name_of(member_id)
        rows = tuple(
            _shift_row(
                s,
                tuple(
                    HolderValue(
                        assignment_id=a.id,
                        member_id=a.member_id,
                        name=names[a.member_id],
                        pending=views[a.id].pending,
                        requestable=views[a.id].requestable,
                    )
                    for a in by_shift[s.id]
                ),
            )
            for s in shifts
        )
        return BoardValue(start_date=week.start_date, state=week.state, shifts=rows)

    def list_weeks(self, caller: Caller) -> WeeksValue:
        """R-scheduling-06: newest first; members see published weeks only; the current week is the latest
        published one whose start_date is on or before today by the clock, or None."""
        session = db.current_session()
        weeks = repo.all_weeks(session)
        today = self._bound().clock.now().date()
        current = rules.current_week([w.start_date for w in weeks if w.state == PUBLISHED], today)
        if caller.role not in PLANNING_ROLES:
            weeks = [w for w in weeks if w.state == PUBLISHED]
        listed = tuple(WeekValue(start_date=w.start_date, state=w.state) for w in weeks)
        return WeeksValue(weeks=listed, current=current)

    # ---- helpers
    @staticmethod
    def _require_planner(caller: Caller, action: str) -> None:
        if caller.role not in PLANNING_ROLES:
            raise Refused("forbidden", f"Only a planner or an admin may {action}.")
