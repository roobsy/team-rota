"""ADU-07 - Swaps service: arms 1, 2, 3, 7, 8 and 9 of ADU-PLAN.md (ADU-07), written tests first.

Every member, name, e-mail, date, time and id in this module is SYNTHETIC: invented for the test by the
literals below (TEAM, CATALOGUE, the Req arrangements MINE, PENDING, VIEW_REQUESTS and the cases). They are
the same on every run, and none is real data.

The interface under test is derived from the contract's swaps operations, Q-21 (a), Q-22 (a), D-14 and D-15.
SwapsService(bound) reads bound().clock, .scheduling, .member_directory and .notifier at call time (D-15) and
works in db.current_session() (D-14). It answers RequestRow, the contract's SwapRequest as a frozen dataclass
(state stored, display_state derived, decision None until there is one, Q-21 (a)). A refusal is
ports.Refused, asserted by .reason only.

"Through the ports alone." Foreign keys are ON, so every request needs real members, weeks, shifts and
assignments rows. Those rows disagree with the doubles on purpose:
- every members row's name differs from identity's (FakeMemberDirectory.name_of);
- SAM's row is inactive while identity says active, and XIN's row is active while identity says inactive;
- ZED is a members row identity does not know (is_active answers None);
- the rows' roles are not identity's: MO's row says admin and LEE's says planner, every other row says member;
- LEE's Caller is a planner while identity says member; MAY's Caller is a member while identity says planner;
- every shift row lies in December at 14:30-18:30, while scheduling's AssignmentInfo answers November dates
  and other times;
- the week rows' states are the opposite of AssignmentInfo.week_state;
- every assignment row's member differs from AssignmentInfo.holder_id.
So a service fails here if it reads identity's or scheduling's tables, or judges forbidden on anything but
the Caller it was given (PRODUCT-DESIGN, The caller).

What a rollback hides. A refusal is asserted the way design/INTERFACES.md (Domain services, "A test")
prescribes: pytest.raises around the unit of work, which rolls back. A read-back in a second unit of work
after a refusal therefore only catches a service that commits by itself or writes through a session of its
own. To close that gap, _refusal also reads the swaps tables through the caller's session at the moment the
refusal propagates, before the rollback (autoflush is on, so an unflushed write is flushed and seen). That
probe covers swap_requests and decisions only: a write to any other table in the caller's session before a
refusal is still hidden by the rollback. "Emits nothing" is a full check, because the SpyNotifier is not
transactional; so is FakeSchedulingPort.transfers.

Arm 1 - retires MK-03 (the binding, the Null deleted, nothing imports a Null):
    test_arm1_create_app_binds_the_swaps_service_as_the_swaps_port
    test_arm1_the_bound_service_reads_the_apps_own_bindings
    test_arm1_the_bound_service_reads_the_bindings_at_call_time                    (D-15)
    test_arm1_the_null_swaps_port_and_the_nulls_test_no_longer_exist
    test_arm1_no_module_under_src_or_tests_imports_a_null
    test_arm1_the_import_scan_finds_every_import_form_of_each_null_and_nothing_else (the scan's twin)
  The arm's clauses on the contract unit's tests and on the scheduling tests are the gate's at this unit's
  close; by the arm's own words, no test of this file repeats them. The retirement tests are red until the
  developer's retirement step (the amends of ADU-07).
Arm 2 - request:
    test_arm2_the_request_row_carries_exactly_the_contracts_swap_request_fields   (Q-21 (a); frozen)
    test_arm2_request_records_state_requested_and_answers_the_request_row
    test_arm2_request_notifies_the_counterpart_once
    test_arm2_each_request_reason_code_is_accepted
    test_arm2_a_counterpart_of_any_role_is_eligible                                (implied by R-swaps-08)
    test_arm2_a_request_one_minute_before_the_deadline_is_recorded
    test_arm2_a_closed_request_on_the_assignment_does_not_block_a_new_one
    test_arm2_an_open_request_on_another_assignment_does_not_block
    test_arm2_an_expired_request_is_not_open_so_the_answer_is_past_deadline
    test_arm2_request_refuses_each_invalid_request                                 (single faults)
    test_arm2_request_answers_the_first_failing_check                              (adjacent double faults)
Arm 3 - answer:
    test_arm3_accept_moves_the_request_to_accepted_with_answered_at_from_the_clock
    test_arm3_accept_notifies_the_requester_and_every_eligible_decider_once
    test_arm3_decline_moves_the_request_to_declined_with_the_reason_and_tells_the_requester
    test_arm3_an_answer_one_minute_before_the_deadline_is_recorded
    test_arm3_answer_refuses_each_invalid_answer                                   (single faults)
    test_arm3_answer_answers_the_first_failing_check                               (adjacent double faults)
Arm 7 - mine:
    test_arm7_mine_lists_every_request_the_caller_is_party_to_newest_first
    test_arm7_mine_answers_each_as_the_request_row_with_display_state_awaiting_and_decision
    test_arm7_expired_is_derived_on_read_nothing_stored_nobody_notified
    test_arm7_an_inactive_other_party_is_still_listed_with_their_name
    test_arm7_requests_the_caller_is_not_party_to_are_absent
Arm 8 - pending:
    test_arm8_pending_is_forbidden_for_a_member
    test_arm8_pending_lists_open_accepted_requests_oldest_first_by_answered_at_then_id
    test_arm8_every_decider_gets_the_same_list_with_party_per_viewer
    test_arm8_pending_answers_request_rows_and_a_request_whose_party_is_inactive_is_listed
Arm 9 - SwapsPort.view:
    test_arm9_view_answers_pending_and_requestable_per_assignment_without_reading_scheduling
    test_arm9_view_judges_open_and_the_deadline_by_the_start_instant_it_is_given
    test_arm9_nothing_is_requestable_on_a_week_that_is_not_published
    test_arm9_requestable_is_judged_for_the_caller_id_given
    test_arm9_an_empty_input_answers_an_empty_mapping
No session (D-14):
    test_d14_with_no_session_current_every_method_raises_no_current_session
    test_d14_a_write_commits_nothing_itself                                         (R-swaps-04's atomicity)
    test_d14_the_no_session_cases_cover_exactly_the_six_methods                    (self-test)

Not pinned here, because the documents leave them open: Q-19 and Q-20; an outcome outside accept/decline (the
API's invalid_request); an empty-string reason; an inactive requester on accept or decline; a member name
identity does not know; Q-02 (a counterpart deactivated while a request is open); Q-03 (an accept where every
decider is a party: every case here leaves at least one eligible decider); notification texts (ADU-09's); the
order of recipient_ids.
"""

from __future__ import annotations

import ast
import json
from collections.abc import Callable
from dataclasses import FrozenInstanceError, dataclass, fields, replace
from datetime import date, datetime, time, timedelta
from pathlib import Path
from types import SimpleNamespace
from typing import NamedTuple

import pytest
from sqlalchemy import Engine, select
from sqlalchemy.orm import Session
from support.doubles import FakeMemberDirectory, FakeSchedulingPort, FixedClock, SpyNotifier

from app import db, models, ports
from app.main import create_app
from app.ports import AssignmentInfo, AssignmentView, Refused
from app.swaps import service as swaps_service

# the package import keeps ruff's import order stable before and after service.py exists (scheduling's)
SwapsService = swaps_service.SwapsService
RequestRow = swaps_service.RequestRow
DecisionValue = swaps_service.DecisionValue

ROOT = Path(__file__).resolve().parents[2]
SCHEMAS = json.loads((ROOT / "contracts" / "openapi.json").read_text(encoding="utf-8"))["components"][
    "schemas"
]
NULL_MODULES = (
    "app.identity.null_directory",
    "app.notifications.null_notifier",
    "app.scheduling.null_port",
    "app.swaps.null_port",
)

NOW = datetime(2026, 11, 12, 10, 0)  # SYNTHETIC: the FixedClock's instant, a Thursday
DAY24 = timedelta(hours=24)  # the deadline is 24 hours before the shift's start instant (R-swaps-01)
MINUTE = timedelta(minutes=1)
UNKNOWN = 9_999  # names no member, assignment or request in any arrangement of this module


def T(day: int, hour: int, minute: int = 0) -> datetime:
    """A SYNTHETIC instant of November 2026."""
    return datetime(2026, 11, day, hour, minute)


# ------------------------------------------------------------------------------------------------ the team
@dataclass(frozen=True)
class Seat:
    """One SYNTHETIC member. The members row, identity's entry and the Caller disagree on purpose."""

    member_id: int
    row_name: str  # what a service reading the members table would see
    name: str  # identity's name (FakeMemberDirectory.name_of), and the Caller's
    caller_role: str  # the Caller's role: forbidden is judged on it
    directory_role: str  # identity's role: decider_ids is computed from it
    row_role: str
    row_active: bool
    directory_active: bool | None  # None: identity does not know the id (is_active answers None)


AVI, PAT, RAE, MO, SAM, NED, OLA, XIN, ZED, LEE, MAY = range(601, 612)
TEAM = (
    Seat(AVI, "Quinn", "Avi", "admin", "admin", "member", True, True),
    Seat(PAT, "Ravi", "Pat", "planner", "planner", "member", True, True),
    Seat(RAE, "Hana", "Rae", "planner", "planner", "member", True, True),
    Seat(MO, "Tess", "Mo", "member", "member", "admin", True, True),
    Seat(SAM, "Uma", "Sam", "member", "member", "member", False, True),  # the row says inactive
    Seat(NED, "Kofi", "Ned", "member", "member", "member", True, True),
    Seat(OLA, "Lior", "Ola", "member", "member", "member", True, True),
    Seat(XIN, "Noor", "Xin", "member", "member", "member", True, False),  # identity says inactive
    Seat(ZED, "Jude", "Zed", "member", "member", "member", True, None),  # identity does not know ZED
    Seat(LEE, "Bram", "Lee", "planner", "member", "planner", True, True),  # a planner by the Caller only
    Seat(MAY, "Ines", "May", "member", "planner", "member", True, True),  # a decider by identity only
)
SEAT = {s.member_id: s for s in TEAM}
NAME = {s.member_id: s.name for s in TEAM}
C = {
    s.member_id: ports.Caller(member_id=s.member_id, name=s.name, role=s.caller_role, active=True)
    for s in TEAM
}
DECIDERS = {AVI, PAT, RAE, MAY}  # identity's active admins and planners: FakeMemberDirectory.decider_ids()


# ------------------------------------------------------------------------- scheduling's answers (the fake)
class Slot(NamedTuple):
    """One assignment as SchedulingPort.assignment answers it (IR-01)."""

    assignment_id: int
    holder_id: int
    shift_id: int
    day: date
    start: str
    end: str
    week_state: str
    holder_ids: tuple[int, ...]


D13, D19, D20, D21, D22, D26 = (date(2026, 11, d) for d in (13, 19, 20, 21, 22, 26))
A1, A2, A3, A4, A5, A6, A7, A8, A9 = range(701, 710)
SOON, EDGE, NEAR = 711, 712, 713
CATALOGUE = (
    Slot(A1, MO, 801, D19, "08:00", "12:00", "published", (MO, NED)),
    Slot(A2, MO, 802, D26, "08:00", "12:00", "draft", (MO,)),
    Slot(A3, MO, 803, D20, "08:00", "12:00", "published", (MO, OLA)),
    Slot(A4, PAT, 804, D19, "16:00", "20:00", "published", (PAT,)),
    Slot(A5, XIN, 805, D20, "12:00", "16:00", "published", (XIN,)),
    Slot(A6, SAM, 806, D21, "08:00", "12:00", "published", (SAM,)),
    Slot(A7, NED, 807, D21, "12:00", "16:00", "published", (NED,)),
    Slot(A8, OLA, 808, D22, "08:00", "12:00", "published", (OLA,)),
    Slot(A9, AVI, 809, D22, "12:00", "16:00", "published", (AVI,)),
    Slot(SOON, MO, 811, D13, "08:00", "10:00", "published", (MO,)),  # deadline 2026-11-12 08:00, before NOW
    Slot(EDGE, MO, 812, D13, "10:00", "12:00", "published", (MO,)),  # deadline 2026-11-12 10:00 == NOW
    Slot(NEAR, SAM, 813, D13, "10:01", "12:00", "published", (SAM,)),  # deadline NOW + 1 minute
)
SLOT = {s.assignment_id: s for s in CATALOGUE}


def _info(slot: Slot) -> AssignmentInfo:
    start = time.fromisoformat(slot.start)
    return AssignmentInfo(
        assignment_id=slot.assignment_id,
        holder_id=slot.holder_id,
        shift_id=slot.shift_id,
        shift_date=slot.day,
        start=start,
        end=time.fromisoformat(slot.end),
        start_at=datetime.combine(slot.day, start),
        week_start=slot.day - timedelta(days=slot.day.weekday()),
        week_state=slot.week_state,
        holder_ids=slot.holder_ids,
    )


def _deadline(assignment_id: int) -> datetime:
    return _info(SLOT[assignment_id]).start_at - DAY24


def _directory() -> FakeMemberDirectory:
    directory = FakeMemberDirectory()
    for s in TEAM:
        if s.directory_active is not None:
            directory.add(s.member_id, s.name, s.directory_role, active=s.directory_active)
    return directory


def _scheduling() -> FakeSchedulingPort:
    scheduling = FakeSchedulingPort()
    for slot in CATALOGUE:
        scheduling.set_assignment(_info(slot))
    return scheduling


# -------------------------------------------------------------- the stored rows (foreign keys are ON)
DB_DRAFT, DB_PUBLISHED = date(2026, 12, 7), date(2026, 12, 14)  # SYNTHETIC Mondays, rows only


def _seat(engine: Engine) -> None:
    """Members, weeks, shifts and assignments rows that disagree with identity and scheduling (see above)."""
    with db.unit_of_work(engine) as session:
        session.add_all(
            [
                models.Member(
                    id=s.member_id,
                    name=s.row_name,
                    email=f"{s.row_name.lower()}@example.test",
                    role=s.row_role,
                    active=s.row_active,
                    passcode_hash="SYNTHETIC-not-a-passcode-hash",
                )
                for s in TEAM
            ]
        )
        session.add_all(
            [
                models.Week(start_date=DB_DRAFT, state="draft"),
                models.Week(start_date=DB_PUBLISHED, state="published"),
            ]
        )
        session.flush()
        shifts = []
        for n, slot in enumerate(CATALOGUE):
            week = DB_PUBLISHED if slot.week_state == "draft" else DB_DRAFT  # the opposite state
            shifts.append(
                models.Shift(
                    id=slot.shift_id,
                    week_start=week,
                    date=week + timedelta(days=n % 7),
                    start=time(14, 30),
                    end=time(18, 30),
                    slots=2,
                )
            )
        session.add_all(shifts)
        session.flush()
        session.add_all(
            [
                models.Assignment(
                    id=slot.assignment_id,
                    shift_id=slot.shift_id,
                    member_id=OLA if slot.holder_id != OLA else NED,  # never scheduling's holder
                )
                for slot in CATALOGUE
            ]
        )


class Dec(NamedTuple):
    id: int
    decider_id: int
    outcome: str
    reason: str | None
    decided_at: datetime


class Req(NamedTuple):
    """A stored swap request (and its decision), arranged directly: a SYNTHETIC row."""

    id: int
    assignment_id: int
    requester_id: int
    counterpart_id: int
    state: str
    created_at: datetime
    answered_at: datetime | None = None
    answer_reason: str | None = None
    reason: str = "other"
    decision: Dec | None = None


def _put(engine: Engine, *requests: Req) -> None:
    with db.unit_of_work(engine) as session:
        session.add_all(
            [
                models.SwapRequest(
                    id=r.id,
                    assignment_id=r.assignment_id,
                    requester_id=r.requester_id,
                    counterpart_id=r.counterpart_id,
                    reason=r.reason,
                    state=r.state,
                    created_at=r.created_at,
                    answered_at=r.answered_at,
                    answer_reason=r.answer_reason,
                )
                for r in requests
            ]
        )
        session.flush()
        session.add_all(
            [
                models.Decision(
                    id=r.decision.id,
                    request_id=r.id,
                    decider_id=r.decision.decider_id,
                    outcome=r.decision.outcome,
                    reason=r.decision.reason,
                    decided_at=r.decision.decided_at,
                )
                for r in requests
                if r.decision
            ]
        )


class Stored(NamedTuple):
    # id -> (assignment_id, requester_id, counterpart_id, reason, state, created_at, answered_at,
    #        answer_reason)
    requests: dict[int, tuple]
    decisions: list[tuple]  # (id, request_id, decider_id, outcome, reason, decided_at)


REQUEST_COLUMNS = (
    models.SwapRequest.id,
    models.SwapRequest.assignment_id,
    models.SwapRequest.requester_id,
    models.SwapRequest.counterpart_id,
    models.SwapRequest.reason,
    models.SwapRequest.state,
    models.SwapRequest.created_at,
    models.SwapRequest.answered_at,
    models.SwapRequest.answer_reason,
)
DECISION_COLUMNS = (
    models.Decision.id,
    models.Decision.request_id,
    models.Decision.decider_id,
    models.Decision.outcome,
    models.Decision.reason,
    models.Decision.decided_at,
)


def _read(session: Session) -> Stored:
    """The swaps tables as plain tuples. Columns, not entities: a read through the caller's session puts
    nothing into its identity map, while autoflush still sends any pending write first."""
    requests = {
        row[0]: tuple(row[1:])
        for row in session.execute(select(*REQUEST_COLUMNS).order_by(models.SwapRequest.id))
    }
    decisions = [
        tuple(row) for row in session.execute(select(*DECISION_COLUMNS).order_by(models.Decision.id))
    ]
    return Stored(requests, decisions)


def _stored(engine: Engine) -> Stored:
    """The swaps tables, read back in a unit of work of their own."""
    with db.unit_of_work(engine) as session:
        return _read(session)


# ---------------------------------------------------------------------------------------------- the world
class World(NamedTuple):
    engine: Engine
    clock: FixedClock
    directory: FakeMemberDirectory
    scheduling: FakeSchedulingPort
    spy: SpyNotifier
    service: SwapsService


@pytest.fixture
def world(tmp_path: Path) -> World:
    engine = db.engine_for(tmp_path)
    _seat(engine)
    clock, directory, scheduling, spy = FixedClock(NOW), _directory(), _scheduling(), SpyNotifier()
    service = SwapsService(
        lambda: SimpleNamespace(clock=clock, scheduling=scheduling, member_directory=directory, notifier=spy)
    )
    return World(engine, clock, directory, scheduling, spy, service)


Call = Callable[[SwapsService], object]
Arrange = Callable[[World], None]


def _do(world: World, call: Call) -> object:
    with db.unit_of_work(world.engine):
        return call(world.service)


def _refusal(world: World, call: Call) -> Refused:
    """The refusal, with pytest.raises around the unit of work (design/INTERFACES.md, "A test"). It also
    asserts that the refusal changed nothing: the swaps tables seen through the caller's session as the
    refusal propagates, and again in a unit of work of their own, equal the arrangement; nothing was emitted;
    nothing was transferred."""
    before, sent = _stored(world.engine), list(world.spy.sent)
    inside: list[Stored] = []
    with pytest.raises(Refused) as refused:
        with db.unit_of_work(world.engine) as session:
            try:
                call(world.service)
            except Refused:
                inside.append(_read(session))
                raise
    assert inside == [before], "a write was made in the caller's session before the refusal"
    assert _stored(world.engine) == before
    assert world.spy.sent == sent
    assert world.scheduling.transfers == []
    return refused.value


def _set_clock(clock: FixedClock, at: datetime) -> None:
    clock.advance(seconds=int((at - clock.now()).total_seconds()))


def _row(req: Req, *, display_state: str, awaiting: str, party: bool, **changes: object) -> RequestRow:
    """The expected row of a stored request. The copied fields come from the arrangement (the Req, identity's
    names, scheduling's slot); display_state, awaiting and party are the test's oracle and always explicit."""
    slot = SLOT[req.assignment_id]
    decision = None
    if req.decision:
        decision = DecisionValue(
            id=req.decision.id,
            request_id=req.id,
            decider_id=req.decision.decider_id,
            outcome=req.decision.outcome,
            reason=req.decision.reason,
            decided_at=req.decision.decided_at,
        )
    values: dict[str, object] = dict(
        id=req.id,
        assignment_id=req.assignment_id,
        shift_date=slot.day,
        shift_start=time.fromisoformat(slot.start),
        requester_id=req.requester_id,
        requester_name=NAME[req.requester_id],
        counterpart_id=req.counterpart_id,
        counterpart_name=NAME[req.counterpart_id],
        reason=req.reason,
        state=req.state,
        display_state=display_state,
        awaiting=awaiting,
        created_at=req.created_at,
        answered_at=req.answered_at,
        answer_reason=req.answer_reason,
        decision=decision,
        party=party,
    )
    values.update(changes)
    return RequestRow(**values)


# ------------------------------------------------------------------------------- arrangement building blocks
def _nothing(world: World) -> None:
    """No arrangement beyond the world's."""


def _requests(*requests: Req) -> Arrange:
    def arrange(world: World) -> None:
        _put(world.engine, *requests)

    return arrange


def _at(instant: datetime) -> Arrange:
    def arrange(world: World) -> None:
        _set_clock(world.clock, instant)

    return arrange


def _intersecting(member_id: int, shift_id: int) -> Arrange:
    def arrange(world: World) -> None:
        world.scheduling.set_intersecting(member_id, shift_id)

    return arrange


def _inactive_by_identity(member_id: int) -> Arrange:
    def arrange(world: World) -> None:
        world.directory.add(member_id, NAME[member_id], SEAT[member_id].directory_role, active=False)

    return arrange


def _holder_ids(assignment_id: int, holder_ids: tuple[int, ...]) -> Arrange:
    def arrange(world: World) -> None:
        world.scheduling.set_assignment(replace(_info(SLOT[assignment_id]), holder_ids=holder_ids))

    return arrange


def _all(*arrangements: Arrange) -> Arrange:
    def arrange(world: World) -> None:
        for each in arrangements:
            each(world)

    return arrange


class Case(NamedTuple):
    arrange: Arrange
    call: Call
    reason: str


# ===================================================================================================== arm 1
def test_arm1_create_app_binds_the_swaps_service_as_the_swaps_port(tmp_path: Path) -> None:
    swaps = create_app(workspace=tmp_path).state.ports.swaps
    assert isinstance(swaps, SwapsService)  # the class: the Null also passes the protocol
    assert isinstance(swaps, ports.SwapsPort)


def test_arm1_the_bound_service_reads_the_apps_own_bindings(tmp_path: Path) -> None:
    """An app built with injected doubles. A request through app.state.ports.swaps reads the app's clock
    (created_at; the system clock reads another instant), the app's scheduling (the shift's date and start;
    the real scheduling would read the December rows), the app's directory (the names; the real identity would
    read the rows' names) and reaches the app's notifier."""
    directory, scheduling, spy = _directory(), _scheduling(), SpyNotifier()
    app = create_app(
        workspace=tmp_path,
        clock=FixedClock(NOW),
        member_directory=directory,
        scheduling=scheduling,
        notifier=spy,
    )
    engine = db.engine_for(tmp_path)
    _seat(engine)
    with db.unit_of_work(engine):
        row = app.state.ports.swaps.request(C[MO], A1, SAM, "sick")
    assert (row.created_at, row.shift_date, row.shift_start) == (NOW, D19, time(8, 0))
    assert (row.requester_name, row.counterpart_name) == ("Mo", "Sam")
    assert [(type(e), e.request_id, e.recipient_id) for e in spy.sent] == [(ports.SwapRequested, row.id, SAM)]


def test_arm1_the_bound_service_reads_the_bindings_at_call_time(tmp_path: Path) -> None:
    """D-15: the service reads the composition root's bindings when it is called, not when it is built. A
    notifier bound after create_app receives the event, and the one bound before receives nothing."""
    first, later = SpyNotifier(), SpyNotifier()
    app = create_app(
        workspace=tmp_path,
        clock=FixedClock(NOW),
        member_directory=_directory(),
        scheduling=_scheduling(),
        notifier=first,
    )
    engine = db.engine_for(tmp_path)
    _seat(engine)
    app.state.ports.notifier = later
    with db.unit_of_work(engine):
        row = app.state.ports.swaps.request(C[MO], A1, SAM, "sick")
    assert first.sent == []
    assert [(type(e), e.request_id) for e in later.sent] == [(ports.SwapRequested, row.id)]


def test_arm1_the_null_swaps_port_and_the_nulls_test_no_longer_exist() -> None:
    assert not (ROOT / "src" / "app" / "swaps" / "null_port.py").exists()
    assert not (ROOT / "tests" / "test_nulls.py").exists()


def _imported_names(source: str, module: tuple[str, ...]) -> set[str]:
    """Every dotted name an Import or ImportFrom node of `source` can bind. A relative import is resolved
    against `module`, the importing module's dotted parts. A string literal is never an import node, so it
    cannot match."""
    names: set[str] = set()
    for node in ast.walk(ast.parse(source)):
        if isinstance(node, ast.Import):
            names.update(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            base = list(module[: len(module) - node.level]) if node.level else []
            full = ".".join([*base, *(node.module.split(".") if node.module else [])])
            names.add(full)
            names.update(f"{full}.{alias.name}" for alias in node.names)
    return names


def _nulls_imported(source: str, module: tuple[str, ...]) -> set[str]:
    names = _imported_names(source, module)
    return {m for m in NULL_MODULES if any(n == m or n.startswith(m + ".") for n in names)}


def _module_parts(path: Path) -> tuple[str, ...]:
    for top in (ROOT / "src", ROOT / "tests"):
        if path.is_relative_to(top):
            return path.relative_to(top).with_suffix("").parts
    raise AssertionError(f"{path} is under neither src/ nor tests/")


def test_arm1_no_module_under_src_or_tests_imports_a_null() -> None:
    files = sorted(p for top in ("src", "tests") for p in (ROOT / top).rglob("*.py"))
    assert Path(__file__).resolve() in files, "the scan must cover tests/swaps"
    offenders = {
        p.relative_to(ROOT).as_posix(): sorted(found)
        for p in files
        if (found := _nulls_imported(p.read_text(encoding="utf-8"), _module_parts(p)))
    }
    assert offenders == {}


def _forms(null: str) -> list:
    """Each import form of one Null module (found), and the near misses (not found)."""
    package, leaf = null.rsplit(".", 1)
    domain = package.split(".")[-1]
    sibling_module = (*package.split("."), "service")
    return [
        pytest.param(f"from {null} import Null\n", ("app", "main"), {null}, id=f"{leaf}@{domain}-from"),
        pytest.param(f"import {null}\n", ("app", "main"), {null}, id=f"{leaf}@{domain}-import"),
        pytest.param(f"import {null} as n\n", ("app", "main"), {null}, id=f"{leaf}@{domain}-import-as"),
        pytest.param(
            f"from {package} import {leaf}\n", ("test_x",), {null}, id=f"{leaf}@{domain}-from-package"
        ),
        pytest.param(f"from . import {leaf}\n", sibling_module, {null}, id=f"{leaf}@{domain}-relative"),
        pytest.param(
            f"from .{leaf} import Null\n", sibling_module, {null}, id=f"{leaf}@{domain}-relative-from"
        ),
        pytest.param(
            f"from ..{domain}.{leaf} import Null\n", ("app", "api", "x"), {null}, id=f"{leaf}@{domain}-up-two"
        ),
        pytest.param(
            f"TEXT = 'from {null} import Null'\n", ("app", "main"), set(), id=f"{leaf}@{domain}-string"
        ),
        pytest.param(
            f"from {package}.service import X\n", ("app", "main"), set(), id=f"{leaf}@{domain}-sibling"
        ),
        pytest.param(f"import {package}\n", ("app", "main"), set(), id=f"{leaf}@{domain}-the-package-alone"),
    ]


@pytest.mark.parametrize("source, module, found", [form for null in NULL_MODULES for form in _forms(null)])
def test_arm1_the_import_scan_finds_every_import_form_of_each_null_and_nothing_else(
    source: str, module: tuple[str, ...], found: set[str]
) -> None:
    """The falsification twin of the scan above. The same helper reports each import form of each retired
    module, and none of a string literal (completed test files hold such lines as literals), a sibling module
    or the bare package. So an empty offender map carries information."""
    assert _nulls_imported(source, module) == found


# ===================================================================================================== arm 2
def test_arm2_the_request_row_carries_exactly_the_contracts_swap_request_fields() -> None:
    """Q-21 (a): the row is the contract's SwapRequest, its 17 required names, as a frozen dataclass."""
    required = SCHEMAS["SwapRequest"]["required"]
    assert len(required) == 17
    assert {f.name for f in fields(RequestRow)} == set(required)
    value = RequestRow(**{name: n for n, name in enumerate(required)})  # by keyword: kw_only passes too
    with pytest.raises(FrozenInstanceError):
        setattr(value, "state", "approved")


def _request(caller_id: int, assignment_id: int = A1, counterpart_id: int = SAM, reason: str | None = "sick"):
    return lambda s: s.request(C[caller_id], assignment_id, counterpart_id, reason)


def test_arm2_request_records_state_requested_and_answers_the_request_row(world: World) -> None:
    row = _do(world, _request(MO))
    stored = _stored(world.engine)
    assert stored.decisions == []
    ((new_id, values),) = stored.requests.items()
    assert values == (A1, MO, SAM, "sick", "requested", NOW, None, None)
    assert row == RequestRow(
        id=new_id,
        assignment_id=A1,
        shift_date=D19,  # scheduling's answer, not the December shift row
        shift_start=time(8, 0),
        requester_id=MO,
        requester_name="Mo",  # identity's answer, not the row's "Tess"
        counterpart_id=SAM,
        counterpart_name="Sam",
        reason="sick",
        state="requested",
        display_state="requested",
        awaiting="counterpart",
        created_at=NOW,
        answered_at=None,
        answer_reason=None,
        decision=None,
        party=True,
    )


def test_arm2_request_notifies_the_counterpart_once(world: World) -> None:
    row = _do(world, _request(MO))
    assert world.spy.sent == [
        ports.SwapRequested(
            request_id=row.id,
            shift_date=D19,
            shift_start=time(8, 0),
            requester_name="Mo",
            reason="sick",
            recipient_id=SAM,
        )
    ]


@pytest.mark.parametrize("reason", ["sick", "family", "travel", "other"])
def test_arm2_each_request_reason_code_is_accepted(world: World, reason: str) -> None:
    row = _do(world, _request(MO, reason=reason))
    assert row.reason == reason
    assert [values[3] for values in _stored(world.engine).requests.values()] == [reason]
    assert [e.reason for e in world.spy.sent] == [reason]


@pytest.mark.parametrize("counterpart_id", [AVI, RAE, OLA], ids=["an-admin", "a-planner", "a-member"])
def test_arm2_a_counterpart_of_any_role_is_eligible(world: World, counterpart_id: int) -> None:
    """R-swaps-08 asks for a member other than the requester, active, free on that shift and that date; it
    names no role (R-notifications-01's 'every eligible decider' assumes a decider may be a party)."""
    row = _do(world, _request(MO, counterpart_id=counterpart_id))
    assert (row.counterpart_id, row.counterpart_name, row.state) == (
        counterpart_id,
        NAME[counterpart_id],
        "requested",
    )


def test_arm2_a_request_one_minute_before_the_deadline_is_recorded(world: World) -> None:
    """The deadline is half-open (PRODUCT-DESIGN, The clock): allowed while now < start - 24 h. The deadline
    comes from scheduling's start instant; the December shift row would put it weeks later."""
    _set_clock(world.clock, _deadline(A1) - MINUTE)
    row = _do(world, _request(MO))
    assert (row.created_at, row.display_state, row.awaiting) == (
        _deadline(A1) - MINUTE,
        "requested",
        "counterpart",
    )


CLOSED_ON_A1 = {
    "declined": Req(951, A1, MO, OLA, "declined", T(9, 9), T(9, 10), "unavailable"),
    "approved": Req(
        951, A1, MO, OLA, "approved", T(9, 9), T(9, 10), decision=Dec(961, AVI, "approved", None, T(9, 11))
    ),
    "refused": Req(
        951, A1, MO, OLA, "refused", T(9, 9), T(9, 10), decision=Dec(961, PAT, "refused", "policy", T(9, 11))
    ),
}


@pytest.mark.parametrize("closed", list(CLOSED_ON_A1.values()), ids=list(CLOSED_ON_A1))
def test_arm2_a_closed_request_on_the_assignment_does_not_block_a_new_one(world: World, closed: Req) -> None:
    _put(world.engine, closed)
    row = _do(world, _request(MO))
    assert row.state == "requested"
    assert sorted(_stored(world.engine).requests) == sorted([closed.id, row.id])


def test_arm2_an_open_request_on_another_assignment_does_not_block(world: World) -> None:
    """R-swaps-02: one open request per assignment, not per requester."""
    _put(world.engine, Req(951, A3, MO, SAM, "requested", T(11, 9)))
    row = _do(world, _request(MO))
    assert (row.assignment_id, row.state) == (A1, "requested")


@pytest.mark.parametrize("state", ["requested", "accepted"])
def test_arm2_an_expired_request_is_not_open_so_the_answer_is_past_deadline(world: World, state: str) -> None:
    """R-swaps-06: open means stored requested or accepted AND now < the deadline. SOON's deadline passed, so
    its stored request is expired, not open: past_deadline answers, not request_open."""
    answered = T(9, 10) if state == "accepted" else None
    _put(world.engine, Req(951, SOON, MO, SAM, state, T(9, 9), answered))
    assert _refusal(world, _request(MO, SOON, OLA)).reason == "past_deadline"


OPEN_ON_A1 = Req(951, A1, MO, OLA, "requested", T(11, 9))
REQUEST_SINGLE_FAULTS = {
    "not_found-the-assignment": Case(_nothing, _request(MO, UNKNOWN), "not_found"),
    "not_found-a-counterpart-identity-does-not-know": Case(
        _nothing, _request(MO, counterpart_id=ZED), "not_found"
    ),
    "not_found-a-counterpart-id-naming-nobody": Case(
        _nothing, _request(MO, counterpart_id=UNKNOWN), "not_found"
    ),
    "not_holder-a-member": Case(_nothing, _request(OLA), "not_holder"),  # OLA is the assignment row's member
    "not_holder-an-admin": Case(_nothing, _request(AVI), "not_holder"),
    "week_draft": Case(_nothing, _request(MO, A2), "week_draft"),  # the week row of A2 says published
    "request_open-requested": Case(_requests(OPEN_ON_A1), _request(MO), "request_open"),
    "request_open-accepted": Case(
        _requests(OPEN_ON_A1._replace(state="accepted", answered_at=T(11, 10))), _request(MO), "request_open"
    ),
    "counterpart_self": Case(_nothing, _request(MO, counterpart_id=MO), "counterpart_self"),
    "counterpart_inactive": Case(_nothing, _request(MO, counterpart_id=XIN), "counterpart_inactive"),
    "counterpart_on_shift": Case(_nothing, _request(MO, counterpart_id=NED), "counterpart_on_shift"),
    "counterpart_overlap": Case(_intersecting(SAM, 801), _request(MO), "counterpart_overlap"),
    "past_deadline": Case(_at(_deadline(A1)), _request(MO), "past_deadline"),
    "reason_required": Case(_nothing, _request(MO, reason=None), "reason_required"),
    "invalid_reason-a-decline-code": Case(_nothing, _request(MO, reason="unavailable"), "invalid_reason"),
    "invalid_reason-a-refusal-code": Case(_nothing, _request(MO, reason="fairness"), "invalid_reason"),
    "invalid_reason-a-system-code": Case(
        _nothing, _request(MO, reason="counterpart_overlap"), "invalid_reason"
    ),
    "invalid_reason-no-code": Case(_nothing, _request(MO, reason="holiday"), "invalid_reason"),
}


@pytest.mark.parametrize("case", list(REQUEST_SINGLE_FAULTS.values()), ids=list(REQUEST_SINGLE_FAULTS))
def test_arm2_request_refuses_each_invalid_request(world: World, case: Case) -> None:
    """One fault each; every other argument is the valid request of MO's A1 to SAM for sick. The refusal
    changes nothing and emits nothing (_refusal)."""
    case.arrange(world)
    assert _refusal(world, case.call).reason == case.reason


# Each pair is two adjacent checks of the arm's order, both failing; the earlier one answers. Two pairs cannot
# be built: the assignment's not_found and the counterpart's answer the same code, and reason_required and
# invalid_reason exclude each other. not_found (the assignment) before not_holder cannot be built either: an
# unknown assignment has no holder.
REQUEST_DOUBLE_FAULTS = {
    "not_found-counterpart-before-not_holder": Case(_nothing, _request(OLA, counterpart_id=ZED), "not_found"),
    "not_holder-before-week_draft": Case(_nothing, _request(OLA, A2), "not_holder"),
    "week_draft-before-request_open": Case(
        _requests(Req(952, A2, MO, OLA, "requested", T(11, 9))), _request(MO, A2), "week_draft"
    ),
    "request_open-before-counterpart_self": Case(
        _requests(OPEN_ON_A1), _request(MO, counterpart_id=MO), "request_open"
    ),
    # identity calls MO inactive while MO's Caller is active: only the counterpart's activeness is asked
    "counterpart_self-before-counterpart_inactive": Case(
        _inactive_by_identity(MO), _request(MO, counterpart_id=MO), "counterpart_self"
    ),
    "counterpart_inactive-before-counterpart_on_shift": Case(
        _holder_ids(A1, (MO, NED, XIN)), _request(MO, counterpart_id=XIN), "counterpart_inactive"
    ),
    "counterpart_on_shift-before-counterpart_overlap": Case(
        _intersecting(NED, 801), _request(MO, counterpart_id=NED), "counterpart_on_shift"
    ),
    "counterpart_overlap-before-past_deadline": Case(
        _all(_intersecting(SAM, 801), _at(_deadline(A1))), _request(MO), "counterpart_overlap"
    ),
    "past_deadline-before-reason_required": Case(
        _at(_deadline(A1)), _request(MO, reason=None), "past_deadline"
    ),
    "past_deadline-before-invalid_reason": Case(
        _at(_deadline(A1)), _request(MO, reason="holiday"), "past_deadline"
    ),
}


@pytest.mark.parametrize("case", list(REQUEST_DOUBLE_FAULTS.values()), ids=list(REQUEST_DOUBLE_FAULTS))
def test_arm2_request_answers_the_first_failing_check(world: World, case: Case) -> None:
    """The arm's order: not_found (assignment, counterpart) -> not_holder -> week_draft -> request_open ->
    counterpart_self -> counterpart_inactive -> counterpart_on_shift -> counterpart_overlap ->
    past_deadline -> reason_required -> invalid_reason."""
    case.arrange(world)
    assert _refusal(world, case.call).reason == case.reason


# ===================================================================================================== arm 3
ASKED = Req(901, A1, MO, SAM, "requested", T(11, 9), reason="sick")


def _answer(caller_id: int, request_id: int = 901, answer: str = "accept", reason: str | None = None):
    return lambda s: s.answer(C[caller_id], request_id, answer, reason)


def test_arm3_accept_moves_the_request_to_accepted_with_answered_at_from_the_clock(world: World) -> None:
    _put(world.engine, ASKED)
    row = _do(world, _answer(SAM))
    assert _stored(world.engine) == Stored({901: (A1, MO, SAM, "sick", "accepted", T(11, 9), NOW, None)}, [])
    assert row == _row(
        ASKED._replace(state="accepted", answered_at=NOW),
        display_state="accepted",
        awaiting="decider",
        party=True,
    )


ACCEPTS = {
    "a-member-requester": (ASKED, {MO} | DECIDERS),
    "a-planner-requester-named-once": (Req(902, A4, PAT, SAM, "requested", T(11, 9)), {PAT, AVI, RAE, MAY}),
    "a-decider-counterpart-left-out": (Req(903, A1, MO, RAE, "requested", T(11, 9)), {MO, AVI, PAT, MAY}),
    "both-parties-deciders": (Req(904, A4, PAT, RAE, "requested", T(11, 9)), {PAT, AVI, MAY}),
}


@pytest.mark.parametrize("asked, recipients", list(ACCEPTS.values()), ids=list(ACCEPTS))
def test_arm3_accept_notifies_the_requester_and_every_eligible_decider_once(
    world: World, asked: Req, recipients: set[int]
) -> None:
    """SwapAccepted goes to the requester and every decider_ids() entry who is not a party (R-swaps-05,
    R-notifications-01), each exactly once. Deciders are identity's: MAY is one and LEE is not, whatever
    their Callers or rows say. The order of recipient_ids is not pinned."""
    _put(world.engine, asked)
    _do(world, _answer(asked.counterpart_id, asked.id))
    (event,) = world.spy.sent
    slot = SLOT[asked.assignment_id]
    assert type(event) is ports.SwapAccepted
    assert (event.request_id, event.shift_date, event.shift_start, event.counterpart_name) == (
        asked.id,
        slot.day,
        time.fromisoformat(slot.start),
        NAME[asked.counterpart_id],
    )
    assert set(event.recipient_ids) == recipients
    assert len(event.recipient_ids) == len(recipients), "a recipient is named twice"


@pytest.mark.parametrize("reason", ["unavailable", "other"])
def test_arm3_decline_moves_the_request_to_declined_with_the_reason_and_tells_the_requester(
    world: World, reason: str
) -> None:
    _put(world.engine, ASKED)
    row = _do(world, _answer(SAM, answer="decline", reason=reason))
    assert _stored(world.engine) == Stored(
        {901: (A1, MO, SAM, "sick", "declined", T(11, 9), NOW, reason)}, []
    )
    assert row == _row(
        ASKED._replace(state="declined", answered_at=NOW, answer_reason=reason),
        display_state="declined",
        awaiting="none",
        party=True,
    )
    assert world.spy.sent == [
        ports.SwapDeclined(
            request_id=901,
            shift_date=D19,
            shift_start=time(8, 0),
            counterpart_name="Sam",
            reason=reason,
            recipient_id=MO,
        )
    ]


def test_arm3_an_answer_one_minute_before_the_deadline_is_recorded(world: World) -> None:
    _put(world.engine, ASKED)
    _set_clock(world.clock, _deadline(A1) - MINUTE)
    row = _do(world, _answer(SAM))
    assert (row.state, row.display_state, row.awaiting, row.answered_at) == (
        "accepted",
        "accepted",
        "decider",
        _deadline(A1) - MINUTE,
    )


def _asked_in(state: str) -> Req:
    """ASKED, stored in another state (with its decision when one exists)."""
    if state == "accepted":
        return ASKED._replace(state=state, answered_at=T(11, 10))
    if state == "declined":
        return ASKED._replace(state=state, answered_at=T(11, 10), answer_reason="other")
    outcome_reason = None if state == "approved" else "coverage"
    return ASKED._replace(
        state=state, answered_at=T(11, 10), decision=Dec(961, AVI, state, outcome_reason, T(11, 11))
    )


ANSWER_SINGLE_FAULTS = {
    "not_found": Case(_requests(ASKED), _answer(SAM, UNKNOWN), "not_found"),
    "not_counterpart-the-requester": Case(_requests(ASKED), _answer(MO), "not_counterpart"),
    "not_counterpart-a-third-member": Case(_requests(ASKED), _answer(NED), "not_counterpart"),
    "not_counterpart-an-admin": Case(_requests(ASKED), _answer(AVI), "not_counterpart"),
    **{
        f"wrong_state-{state}": Case(_requests(_asked_in(state)), _answer(SAM), "wrong_state")
        for state in ("accepted", "declined", "approved", "refused")
    },
    # an expired request's stored state is still requested: it answers past_deadline, not wrong_state
    "past_deadline": Case(_all(_requests(ASKED), _at(_deadline(A1))), _answer(SAM), "past_deadline"),
    "reason_required-a-decline-without-a-reason": Case(
        _requests(ASKED), _answer(SAM, answer="decline"), "reason_required"
    ),
    **{
        f"invalid_reason-decline-{reason}": Case(
            _requests(ASKED), _answer(SAM, answer="decline", reason=reason), "invalid_reason"
        )
        for reason in ("sick", "fairness", "counterpart_inactive", "holiday")
    },
    **{
        f"invalid_reason-accept-with-{reason}": Case(
            _requests(ASKED), _answer(SAM, answer="accept", reason=reason), "invalid_reason"
        )
        for reason in ("unavailable", "other")
    },
}


@pytest.mark.parametrize("case", list(ANSWER_SINGLE_FAULTS.values()), ids=list(ANSWER_SINGLE_FAULTS))
def test_arm3_answer_refuses_each_invalid_answer(world: World, case: Case) -> None:
    case.arrange(world)
    assert _refusal(world, case.call).reason == case.reason


# not_found before not_counterpart cannot be built (an unknown request has no counterpart), and
# reason_required and invalid_reason exclude each other.
ANSWER_DOUBLE_FAULTS = {
    "not_counterpart-before-wrong_state": Case(
        _requests(_asked_in("accepted")), _answer(MO), "not_counterpart"
    ),
    "wrong_state-before-past_deadline": Case(
        _all(_requests(_asked_in("accepted")), _at(_deadline(A1))), _answer(SAM), "wrong_state"
    ),
    "wrong_state-before-reason_required": Case(
        _requests(_asked_in("declined")), _answer(SAM, answer="decline"), "wrong_state"
    ),
    "past_deadline-before-reason_required": Case(
        _all(_requests(ASKED), _at(_deadline(A1))), _answer(SAM, answer="decline"), "past_deadline"
    ),
    "past_deadline-before-invalid_reason": Case(
        _all(_requests(ASKED), _at(_deadline(A1))), _answer(SAM, reason="other"), "past_deadline"
    ),
}


@pytest.mark.parametrize("case", list(ANSWER_DOUBLE_FAULTS.values()), ids=list(ANSWER_DOUBLE_FAULTS))
def test_arm3_answer_answers_the_first_failing_check(world: World, case: Case) -> None:
    """The order: not_found -> not_counterpart -> wrong_state (stored) -> past_deadline -> reason_required /
    invalid_reason."""
    case.arrange(world)
    assert _refusal(world, case.call).reason == case.reason


# ===================================================================================================== arm 7
# MO is party to 921-928; 929 and 930 are other members' requests. created_at does not follow the ids, and
# 923 and 924 tie on it. 922 is a closed request on SOON, whose deadline has passed: it still shows declined.
MINE = (
    Req(921, A3, MO, SAM, "accepted", T(10, 9), T(10, 10), reason="travel"),
    Req(922, SOON, MO, OLA, "declined", T(8, 9), T(8, 12), "unavailable", reason="sick"),
    Req(
        923, A6, SAM, MO, "approved", T(11, 9), T(11, 10), decision=Dec(961, AVI, "approved", None, T(11, 15))
    ),
    Req(
        924,
        A7,
        NED,
        MO,
        "refused",
        T(11, 9),
        T(11, 11),
        decision=Dec(962, PAT, "refused", "coverage", T(11, 16)),
    ),
    Req(925, SOON, MO, SAM, "requested", T(9, 9), reason="family"),  # SOON's deadline has passed: expired
    Req(926, EDGE, MO, OLA, "accepted", T(10, 12), T(10, 13)),  # EDGE's deadline is NOW: expired
    Req(927, A5, XIN, MO, "accepted", T(10, 8), T(10, 9)),  # XIN is inactive by identity
    Req(928, NEAR, SAM, MO, "requested", T(9, 8)),  # NEAR's deadline is NOW + 1 minute: open
    Req(929, A8, OLA, NED, "requested", T(11, 20)),
    Req(930, A4, PAT, SAM, "accepted", T(12, 9), T(12, 9, 30)),
)
MINE_BY_ID = {r.id: r for r in MINE}


@pytest.mark.parametrize(
    "viewer, ids",
    [
        (MO, [924, 923, 926, 921, 927, 925, 928, 922]),
        (NED, [929, 924]),
        (OLA, [929, 926, 922]),
        (LEE, []),
    ],
    ids=["MO", "NED", "OLA", "LEE-party-to-nothing"],
)
def test_arm7_mine_lists_every_request_the_caller_is_party_to_newest_first(
    world: World, viewer: int, ids: list[int]
) -> None:
    """Every state, requester or counterpart, newest first by created_at, then id descending (924 before
    923)."""
    _put(world.engine, *MINE)
    with db.unit_of_work(world.engine):
        rows = world.service.mine(C[viewer])
    assert [r.id for r in rows] == ids
    assert all(r.party is True for r in rows)


def test_arm7_mine_answers_each_as_the_request_row_with_display_state_awaiting_and_decision(
    world: World,
) -> None:
    """R-swaps-09 with Q-21 (a): awaiting is counterpart while open in requested, decider while open in
    accepted, none otherwise; state stays the stored one while display_state shows expired."""
    _put(world.engine, *MINE)
    with db.unit_of_work(world.engine):
        rows = world.service.mine(C[MO])
    expected = {
        924: ("refused", "none"),
        923: ("approved", "none"),
        926: ("expired", "none"),
        921: ("accepted", "decider"),
        927: ("accepted", "decider"),
        925: ("expired", "none"),
        928: ("requested", "counterpart"),
        922: ("declined", "none"),
    }
    assert rows == [
        _row(MINE_BY_ID[i], display_state=shown, awaiting=awaiting, party=True)
        for i, (shown, awaiting) in expected.items()
    ]


def test_arm7_expired_is_derived_on_read_nothing_stored_nobody_notified(world: World) -> None:
    _put(world.engine, *MINE)
    before = _stored(world.engine)
    with db.unit_of_work(world.engine):
        rows = {r.id: r for r in world.service.mine(C[MO])}
    assert [(rows[i].state, rows[i].display_state, rows[i].awaiting) for i in (925, 926)] == [
        ("requested", "expired", "none"),
        ("accepted", "expired", "none"),
    ]
    assert _stored(world.engine) == before
    assert world.spy.sent == []


def test_arm7_an_inactive_other_party_is_still_listed_with_their_name(world: World) -> None:
    _put(world.engine, *MINE)
    with db.unit_of_work(world.engine):
        rows = {r.id: r for r in world.service.mine(C[MO])}
    assert (rows[927].requester_id, rows[927].requester_name) == (XIN, "Xin")


def test_arm7_requests_the_caller_is_not_party_to_are_absent(world: World) -> None:
    _put(world.engine, *MINE)
    with db.unit_of_work(world.engine):
        ids = {r.id for r in world.service.mine(C[MO])}
    assert ids.isdisjoint({929, 930})


# ===================================================================================================== arm 8
# Open accepted: 931, 932, 933, 934 and 940; answered_at follows neither the ids nor created_at, and 931, 933
# and 940 tie on it. Absent: 935 (accepted, EDGE's deadline is NOW), and the requested, declined, approved and
# refused ones.
PENDING = (
    Req(931, A1, MO, SAM, "accepted", T(9, 8), T(11, 9), reason="sick"),
    Req(932, A3, MO, RAE, "accepted", T(9, 10), T(10, 9)),  # RAE, a planner, is the counterpart
    Req(933, A4, PAT, SAM, "accepted", T(8, 9), T(11, 9)),
    Req(934, A5, XIN, MO, "accepted", T(9, 9), T(10, 12), reason="family"),  # XIN is inactive by identity
    Req(935, EDGE, MO, OLA, "accepted", T(9, 7), T(9, 8)),
    Req(936, A6, SAM, NED, "requested", T(11, 8)),
    Req(937, A7, NED, OLA, "declined", T(8, 8), T(8, 9), "other"),
    Req(938, A8, OLA, SAM, "approved", T(8, 7), T(8, 8), decision=Dec(971, AVI, "approved", None, T(8, 10))),
    Req(
        939,
        SOON,
        MO,
        SAM,
        "refused",
        T(8, 6),
        T(8, 7),
        decision=Dec(972, PAT, "refused", "fairness", T(8, 11)),
    ),
    Req(940, NEAR, SAM, MO, "accepted", T(9, 6), T(11, 9)),  # open by one minute
)
PENDING_BY_ID = {r.id: r for r in PENDING}
PENDING_ORDER = [932, 934, 931, 933, 940]


@pytest.mark.parametrize("viewer", [MO, MAY], ids=["a-member", "a-member-whom-identity-calls-a-planner"])
def test_arm8_pending_is_forbidden_for_a_member(world: World, viewer: int) -> None:
    """forbidden is judged on the Caller's role (PRODUCT-DESIGN, The caller), not identity's or the row's."""
    _put(world.engine, *PENDING)
    assert _refusal(world, lambda s: s.pending(C[viewer])).reason == "forbidden"


def test_arm8_pending_lists_open_accepted_requests_oldest_first_by_answered_at_then_id(world: World) -> None:
    _put(world.engine, *PENDING)
    with db.unit_of_work(world.engine):
        rows = world.service.pending(C[AVI])
    assert [r.id for r in rows] == PENDING_ORDER
    assert {(r.state, r.display_state, r.awaiting) for r in rows} == {("accepted", "accepted", "decider")}


@pytest.mark.parametrize(
    "viewer, party_on",
    [(AVI, set()), (PAT, {933}), (RAE, {932}), (LEE, set())],
    ids=["an-admin", "the-requester-of-933", "the-counterpart-of-932", "a-planner-by-the-caller"],
)
def test_arm8_every_decider_gets_the_same_list_with_party_per_viewer(
    world: World, viewer: int, party_on: set[int]
) -> None:
    _put(world.engine, *PENDING)
    with db.unit_of_work(world.engine):
        rows = world.service.pending(C[viewer])
    assert [r.id for r in rows] == PENDING_ORDER
    assert {r.id for r in rows if r.party} == party_on


def test_arm8_pending_answers_request_rows_and_a_request_whose_party_is_inactive_is_listed(
    world: World,
) -> None:
    _put(world.engine, *PENDING)
    with db.unit_of_work(world.engine):
        rows = world.service.pending(C[PAT])
    assert rows == [
        _row(PENDING_BY_ID[i], display_state="accepted", awaiting="decider", party=(i == 933))
        for i in PENDING_ORDER
    ]
    assert (rows[1].id, rows[1].requester_name) == (934, "Xin")


# ===================================================================================================== arm 9
class _NoScheduling:
    """Bound as scheduling for view: any attribute read fails the test and is recorded."""

    def __init__(self, touched: list[str]) -> None:
        self._touched = touched

    def __getattr__(self, name: str) -> object:
        self._touched.append(name)
        pytest.fail(f"view read scheduling.{name}")


@pytest.fixture
def viewing(world: World) -> tuple[World, list[str]]:
    """The world's rows, clock and directory, with scheduling bound to a tripwire."""
    touched: list[str] = []
    tripwire = _NoScheduling(touched)
    service = SwapsService(
        lambda: SimpleNamespace(
            clock=world.clock, scheduling=tripwire, member_directory=world.directory, notifier=world.spy
        )
    )
    return world._replace(service=service), touched


FAR = datetime(2026, 11, 19, 8, 0)  # SYNTHETIC start instants handed to view; no shift row holds any of them
VIEW_REQUESTS = (
    Req(941, A3, MO, SAM, "requested", T(11, 9)),
    Req(942, A4, PAT, SAM, "accepted", T(11, 9), T(11, 10)),
    Req(943, A1, MO, OLA, "declined", T(8, 9), T(8, 10), "unavailable"),
    Req(
        944, A1, MO, SAM, "refused", T(9, 9), T(9, 10), decision=Dec(981, PAT, "refused", "policy", T(9, 12))
    ),
    Req(
        945, A1, MO, NED, "approved", T(10, 9), T(10, 10), decision=Dec(982, AVI, "approved", None, T(10, 12))
    ),
    Req(946, SOON, MO, SAM, "requested", T(9, 9)),
    Req(947, EDGE, MO, OLA, "accepted", T(9, 9), T(9, 10)),
)


def test_arm9_view_answers_pending_and_requestable_per_assignment_without_reading_scheduling(
    viewing: tuple[World, list[str]],
) -> None:
    """IR-07 and R-swaps-06 for MO on a published week. The triples' holders and start instants are the only
    truth: the assignment rows name other members, and the shift rows lie in December."""
    world, touched = viewing
    _put(world.engine, *VIEW_REQUESTS)
    triples = [
        (A1, MO, FAR),  # only closed requests (declined, refused, approved)
        (A2, MO, FAR),  # no request
        (A3, MO, FAR),  # an open requested request
        (A4, PAT, FAR),  # another's row with an open accepted request
        (A6, SAM, FAR),  # another's row, no request
        (SOON, MO, datetime(2026, 11, 13, 8, 0)),  # only an expired requested request
        (EDGE, MO, NOW + DAY24),  # only an accepted request, expired now: the deadline is NOW
        (NEAR, MO, NOW + DAY24 + MINUTE),  # no request; the deadline is one minute ahead
        (A8, MO, FAR),  # MO by the triple (the assignment row names NED)
    ]
    with db.unit_of_work(world.engine):
        answer = world.service.view(MO, True, iter(triples))
    assert answer == {
        A1: AssignmentView(pending=None, requestable=True),
        A2: AssignmentView(pending=None, requestable=True),
        A3: AssignmentView(pending="requested", requestable=False),
        A4: AssignmentView(pending="accepted", requestable=False),
        A6: AssignmentView(pending=None, requestable=False),
        SOON: AssignmentView(pending=None, requestable=False),
        EDGE: AssignmentView(pending=None, requestable=False),
        NEAR: AssignmentView(pending=None, requestable=True),
        A8: AssignmentView(pending=None, requestable=True),
    }
    assert touched == []


def test_arm9_view_judges_open_and_the_deadline_by_the_start_instant_it_is_given(
    viewing: tuple[World, list[str]],
) -> None:
    """The same stored requests, other start instants: SOON's and EDGE's requests are open when their
    assignments start late enough, and A3's request expires when A3 starts within 24 hours."""
    world, touched = viewing
    _put(world.engine, *VIEW_REQUESTS)
    with db.unit_of_work(world.engine):
        answer = world.service.view(MO, True, [(SOON, MO, FAR), (EDGE, MO, FAR), (A3, MO, NOW + DAY24)])
    assert answer == {
        SOON: AssignmentView(pending="requested", requestable=False),
        EDGE: AssignmentView(pending="accepted", requestable=False),
        A3: AssignmentView(pending=None, requestable=False),
    }
    assert touched == []


def test_arm9_nothing_is_requestable_on_a_week_that_is_not_published(
    viewing: tuple[World, list[str]],
) -> None:
    world, touched = viewing
    _put(world.engine, *VIEW_REQUESTS)
    with db.unit_of_work(world.engine):
        answer = world.service.view(
            MO, False, [(A1, MO, FAR), (A2, MO, FAR), (NEAR, MO, NOW + DAY24 + MINUTE)]
        )
    assert answer == {a: AssignmentView(pending=None, requestable=False) for a in (A1, A2, NEAR)}
    assert touched == []


def test_arm9_requestable_is_judged_for_the_caller_id_given(viewing: tuple[World, list[str]]) -> None:
    world, touched = viewing
    _put(world.engine, *VIEW_REQUESTS)
    with db.unit_of_work(world.engine):
        answer = world.service.view(SAM, True, [(A6, SAM, FAR), (A2, MO, FAR), (A4, PAT, FAR)])
    assert answer == {
        A6: AssignmentView(pending=None, requestable=True),
        A2: AssignmentView(pending=None, requestable=False),
        A4: AssignmentView(pending="accepted", requestable=False),
    }
    assert touched == []


def test_arm9_an_empty_input_answers_an_empty_mapping(viewing: tuple[World, list[str]]) -> None:
    world, touched = viewing
    _put(world.engine, *VIEW_REQUESTS)
    with db.unit_of_work(world.engine):
        assert world.service.view(MO, True, []) == {}
    assert touched == []


# ====================================================================================== no session (D-14)
NO_SESSION_REQUESTS = (
    Req(961, A3, MO, SAM, "requested", T(11, 9)),
    Req(962, A4, PAT, SAM, "accepted", T(11, 9), T(11, 10)),
)
NO_SESSION_CALLS: dict[str, Call] = {
    "view": lambda s: s.view(MO, True, [(A1, MO, FAR)]),
    "request": _request(MO),
    "answer": _answer(SAM, 961),
    "decide": lambda s: s.decide(C[AVI], 962, "approve"),
    "mine": lambda s: s.mine(C[MO]),
    "pending": lambda s: s.pending(C[AVI]),
}
OPERATIONS = ("request", "answer", "decide", "mine", "pending")


@pytest.mark.parametrize("call", list(NO_SESSION_CALLS.values()), ids=list(NO_SESSION_CALLS))
def test_d14_with_no_session_current_every_method_raises_no_current_session(
    world: World, tmp_path: Path, monkeypatch: pytest.MonkeyPatch, call: Call
) -> None:
    """Called outside any unit of work, each method lets db.NoCurrentSession propagate. Every argument would
    otherwise succeed: a non-party decider, valid ids and reasons, a non-empty view input. So no check that
    could run without a session can answer first. The working directory is the test's own, so a method that
    quietly opened a session on a default workspace writes nothing into the repository."""
    _put(world.engine, *NO_SESSION_REQUESTS)
    monkeypatch.chdir(tmp_path)
    monkeypatch.delenv("ROTA_WORKSPACE", raising=False)
    with pytest.raises(db.NoCurrentSession):
        call(world.service)
    assert world.spy.sent == []
    assert world.scheduling.transfers == []


class _Abandon(Exception):
    """Raised at the end of a unit of work, after the service returned, so that the unit rolls back."""


WRITES: dict[str, Call] = {name: NO_SESSION_CALLS[name] for name in ("request", "answer", "decide")}


@pytest.mark.parametrize("call", list(WRITES.values()), ids=list(WRITES))
def test_d14_a_write_commits_nothing_itself(world: World, call: Call) -> None:
    """D-14: a service never commits; the caller's unit of work does. When the caller's unit rolls back after
    a successful write, the swaps tables are as they were, so a decision, its transfer and its notifications
    commit together or not at all (R-swaps-04; design/INTERFACES.md, The request's session)."""
    _put(world.engine, *NO_SESSION_REQUESTS)
    before = _stored(world.engine)
    with pytest.raises(_Abandon):
        with db.unit_of_work(world.engine):
            call(world.service)
            raise _Abandon
    assert _stored(world.engine) == before


def test_d14_the_no_session_cases_cover_exactly_the_six_methods() -> None:
    """Keeps the cases above complete: SwapsPort's one method and the five operations, each a method of the
    service."""
    port = {name for name in vars(ports.SwapsPort) if not name.startswith("_")}
    assert port == {"view"}
    assert set(NO_SESSION_CALLS) == port | set(OPERATIONS)
    for name in NO_SESSION_CALLS:
        assert callable(getattr(SwapsService, name, None)), name
