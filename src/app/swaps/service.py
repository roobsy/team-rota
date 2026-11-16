"""The swaps service (ADU-07, layer 3): request, answer, decide, mine and pending, and the SwapsPort that
scheduling reads for the board's badge (IR-07; design/INTERFACES.md, SwapsPort).

- Sessions (D-14). Every method takes db.current_session() before anything else and never opens, commits or
  closes one, so with none current db.NoCurrentSession propagates. A decision, its transfer and its
  notifications are written in the caller's session and commit together (R-swaps-04).
- Refusals. Every refusal is ports.Refused, and every check comes before the first write. The orders: request
  is arm 2's; answer is not_found → not_counterpart → wrong_state → past_deadline → validation (arm 3;
  PRODUCT-DESIGN, Refusals); decide is forbidden → not_found → party_to_swap → wrong_state → past_deadline →
  validation (Q-22 (a)). Within validation, invalid_request (an answer or outcome outside its two values)
  precedes reason_required and invalid_reason (PRODUCT-DESIGN, Refusals); no arm pins it.
- Bindings (D-15). The clock, scheduling, the member directory and the notifier are the composition root's
  bindings, read at call time.
- Other domains. The shift's date, start, start instant, week state and holders come from SchedulingPort
  (IR-01), the transfer is SchedulingPort's (IR-02), names, activeness and the deciders come from
  MemberDirectory (IR-09), and the events go to the Notifier (IR-03); swaps never reads another domain's rows.
  forbidden is judged on the Caller's role. SwapsPort.view judges each assignment by the holder and the start
  instant scheduling hands it and never calls scheduling back (IR-07).
- The request row (Q-21 (a)): state is stored; display_state, awaiting and party are derived on read, expired
  from the clock (nothing stored, nobody notified, R-swaps-06); party is per viewer, so False on decide, whose
  caller is never a party (Q-22 (a)); decision is None until there is one.
- Recipients. SwapAccepted goes to the requester and every decider who is not a party, each once (R-swaps-05);
  SwapApproved and SwapRefused go to both members less an inactive one (arms 4 and 6).
"""

from __future__ import annotations

from collections.abc import Callable, Iterable
from dataclasses import dataclass
from datetime import date, datetime, time
from typing import Protocol

from sqlalchemy.orm import Session

from app import db, models
from app.ports import (
    AssignmentInfo,
    AssignmentNotFound,
    AssignmentView,
    Caller,
    Clock,
    MemberDirectory,
    Notifier,
    Refused,
    SchedulingPort,
    SwapAccepted,
    SwapApproved,
    SwapDeclined,
    SwapRefused,
    SwapRequested,
    TransferRefused,
)
from app.swaps import repo, rules

DECIDING_ROLES = ("admin", "planner")  # decide and see the pending decisions (Permissions)
PUBLISHED = "published"
ACCEPT, DECLINE = "accept", "decline"
APPROVE, REFUSE = "approve", "refuse"


class Bindings(Protocol):
    """The composition root's bindings the service reads (D-15); main.Ports satisfies it, so swaps never
    imports main."""

    clock: Clock
    scheduling: SchedulingPort
    member_directory: MemberDirectory
    notifier: Notifier


@dataclass(frozen=True)
class DecisionValue:
    """The contract's Decision, with its request_id (Q-21 (a))."""

    id: int
    request_id: int
    decider_id: int
    outcome: str
    reason: str | None
    decided_at: datetime


@dataclass(frozen=True)
class RequestRow:
    """The request row of R-swaps-09: the contract's SwapRequest, its 17 required fields (Q-21 (a))."""

    id: int
    assignment_id: int
    requester_id: int
    counterpart_id: int
    shift_date: date
    shift_start: time
    requester_name: str
    counterpart_name: str
    reason: str
    state: str
    display_state: str
    awaiting: str
    created_at: datetime
    answered_at: datetime | None
    answer_reason: str | None
    decision: DecisionValue | None
    party: bool


def _decision_value(decision: models.Decision) -> DecisionValue:
    return DecisionValue(
        id=decision.id,
        request_id=decision.request_id,
        decider_id=decision.decider_id,
        outcome=decision.outcome,
        reason=decision.reason,
        decided_at=decision.decided_at,
    )


class _Rows:
    """Builds the request rows of one call for one viewer: each assignment is asked of scheduling once and
    each name of the member directory once."""

    def __init__(self, bound: Bindings, now: datetime, viewer_id: int, *known: AssignmentInfo) -> None:
        self._scheduling, self._directory = bound.scheduling, bound.member_directory
        self._now, self._viewer_id = now, viewer_id
        self._infos = {info.assignment_id: info for info in known}
        self._names: dict[int, str] = {}

    def info(self, assignment_id: int) -> AssignmentInfo:
        if assignment_id not in self._infos:
            self._infos[assignment_id] = self._scheduling.assignment(assignment_id)
        return self._infos[assignment_id]

    def name(self, member_id: int) -> str:
        if member_id not in self._names:
            self._names[member_id] = self._directory.name_of(member_id)
        return self._names[member_id]

    def row(self, request: models.SwapRequest, decision: models.Decision | None) -> RequestRow:
        info = self.info(request.assignment_id)
        return RequestRow(
            id=request.id,
            assignment_id=request.assignment_id,
            requester_id=request.requester_id,
            counterpart_id=request.counterpart_id,
            shift_date=info.shift_date,
            shift_start=info.start,
            requester_name=self.name(request.requester_id),
            counterpart_name=self.name(request.counterpart_id),
            reason=request.reason,
            state=request.state,
            display_state=rules.display_state(request.state, self._now, info.start_at),
            awaiting=rules.awaiting(request.state, self._now, info.start_at),
            created_at=request.created_at,
            answered_at=request.answered_at,
            answer_reason=request.answer_reason,
            decision=None if decision is None else _decision_value(decision),
            party=self._viewer_id in (request.requester_id, request.counterpart_id),
        )


def _past_deadline(info: AssignmentInfo) -> Refused:
    when = rules.deadline(info.start_at).isoformat(sep=" ", timespec="minutes")
    return Refused("past_deadline", f"The deadline for this shift passed at {when}.")


def _reason_refusal(problem: str, allowed: tuple[str, ...]) -> Refused:
    if problem == "reason_required":
        return Refused(problem, "A reason is required.")
    return Refused(problem, f"The reason must be one of {', '.join(allowed)}.")


def _unique(ids: Iterable[int]) -> tuple[int, ...]:
    return tuple(dict.fromkeys(ids))


class SwapsService:
    """Implements ports.SwapsPort and the swaps operations; the composition root binds it as Ports.swaps
    (ADU-07 arm 1)."""

    def __init__(self, bound: Callable[[], Bindings]) -> None:
        self._bound = bound

    # ---- SwapsPort (IR-07)
    def view(
        self, caller_id: int, week_published: bool, assignments: Iterable[tuple[int, int, datetime]]
    ) -> dict[int, AssignmentView]:
        """Per (assignment_id, holder_id, start_at): pending, the open request's state or None, and
        requestable, own row, published week, no open request and now < deadline (R-swaps-01, -02, -06).
        The start instant is the one given; scheduling is never called back."""
        session = db.current_session()
        triples = list(assignments)
        now = self._bound().clock.now()
        stored: dict[int, list[models.SwapRequest]] = {}
        for request in repo.requests_on(session, (a for a, _holder, _at in triples), rules.OPEN_STATES):
            stored.setdefault(request.assignment_id, []).append(request)
        views: dict[int, AssignmentView] = {}
        for assignment_id, holder_id, start_at in triples:
            open_ = [r for r in stored.get(assignment_id, ()) if rules.is_open(r.state, now, start_at)]
            views[assignment_id] = AssignmentView(
                pending=open_[-1].state if open_ else None,
                requestable=rules.requestable(
                    caller_id, holder_id, week_published, bool(open_), now, start_at
                ),
            )
        return views

    # ---- operations (the contract's operationIds swaps.<action>)
    def request(
        self, caller: Caller, assignment_id: int, counterpart_id: int, reason: str | None
    ) -> RequestRow:
        """R-swaps-01, -02, -08: the holder of an assignment on a published week asks a counterpart to take
        it. Recorded requested with created_at from the clock; the counterpart is told (SwapRequested)."""
        session = db.current_session()
        bound = self._bound()
        now = bound.clock.now()
        directory = bound.member_directory
        try:
            info = bound.scheduling.assignment(assignment_id)
        except AssignmentNotFound:
            raise Refused("not_found", f"No assignment has the id {assignment_id}.") from None
        active = directory.is_active(counterpart_id)
        if active is None:
            raise Refused("not_found", f"No member has the id {counterpart_id}.")
        if info.holder_id != caller.member_id:
            raise Refused("not_holder", "Only the holder of this shift may ask to swap it.")
        if info.week_state != PUBLISHED:
            raise Refused("week_draft", f"The week of {info.week_start.isoformat()} is a draft.")
        if self._has_open(session, info, now):
            raise Refused("request_open", "This shift already has an open swap request.")
        if counterpart_id == caller.member_id:
            raise Refused("counterpart_self", "You cannot swap a shift with yourself.")
        name = directory.name_of(counterpart_id)
        if not active:
            raise Refused("counterpart_inactive", f"{name} is inactive.")
        if counterpart_id in info.holder_ids:
            raise Refused("counterpart_on_shift", f"{name} already holds a slot on this shift.")
        if bound.scheduling.holds_intersecting_shift(counterpart_id, info.shift_id):
            raise Refused("counterpart_overlap", f"{name} holds a shift that overlaps this one.")
        if not rules.before_deadline(now, info.start_at):
            raise _past_deadline(info)
        problem = rules.reason_problem(reason, rules.REQUEST_REASONS)
        if problem:
            raise _reason_refusal(problem, rules.REQUEST_REASONS)
        created = repo.add_request(
            session,
            assignment_id=assignment_id,
            requester_id=caller.member_id,
            counterpart_id=counterpart_id,
            reason=reason,
            state=rules.REQUESTED,
            created_at=now,
        )
        row = _Rows(bound, now, caller.member_id, info).row(created, None)
        bound.notifier.notify(
            SwapRequested(
                request_id=created.id,
                shift_date=info.shift_date,
                shift_start=info.start,
                requester_name=row.requester_name,
                reason=row.reason,
                recipient_id=counterpart_id,
            )
        )
        return row

    def answer(self, caller: Caller, request_id: int, answer: str, reason: str | None = None) -> RequestRow:
        """R-swaps-03, -05: the counterpart accepts (the requester and every decider who is not a party are
        told, SwapAccepted) or declines with a reason (the requester is told, SwapDeclined); answered_at is
        the clock's."""
        session = db.current_session()
        bound = self._bound()
        now = bound.clock.now()
        request = self._get(session, request_id)
        if caller.member_id != request.counterpart_id:
            raise Refused("not_counterpart", "Only the member asked may answer this request.")
        if request.state != rules.REQUESTED:
            raise Refused("wrong_state", f"The request is {request.state}; only a requested one is answered.")
        info = bound.scheduling.assignment(request.assignment_id)
        if not rules.before_deadline(now, info.start_at):
            raise _past_deadline(info)
        if answer not in (ACCEPT, DECLINE):
            raise Refused("invalid_request", "The answer must be accept or decline.")
        if answer == ACCEPT and reason is not None:
            raise Refused("invalid_reason", "An acceptance carries no reason.")
        if answer == DECLINE:
            problem = rules.reason_problem(reason, rules.DECLINE_REASONS)
            if problem:
                raise _reason_refusal(problem, rules.DECLINE_REASONS)
        request.state = rules.ACCEPTED if answer == ACCEPT else rules.DECLINED
        request.answered_at = now
        request.answer_reason = reason
        session.flush()
        row = _Rows(bound, now, caller.member_id, info).row(request, None)
        if answer == ACCEPT:
            parties = (request.requester_id, request.counterpart_id)
            deciders = (d for d in bound.member_directory.decider_ids() if d not in parties)
            event = SwapAccepted(
                request_id=request.id,
                shift_date=info.shift_date,
                shift_start=info.start,
                counterpart_name=row.counterpart_name,
                recipient_ids=_unique([request.requester_id, *deciders]),
            )
        else:
            event = SwapDeclined(
                request_id=request.id,
                shift_date=info.shift_date,
                shift_start=info.start,
                counterpart_name=row.counterpart_name,
                reason=reason,
                recipient_id=request.requester_id,
            )
        bound.notifier.notify(event)
        return row

    def decide(self, caller: Caller, request_id: int, outcome: str, reason: str | None = None) -> RequestRow:
        """R-swaps-04, -05, -07: a planner or admin who is not a party approves (the transfer through
        SchedulingPort first, then one Decision and the mirrored state) or refuses with a reason. A refused
        transfer is not a refusal: the Decision is recorded refused with the transfer's reason, by the
        caller. Both members less an inactive one are told (SwapApproved, SwapRefused). Answers the request
        row with the decision embedded."""
        session = db.current_session()
        if caller.role not in DECIDING_ROLES:
            raise Refused("forbidden", "Only a planner or an admin may decide a swap.")
        bound = self._bound()
        now = bound.clock.now()
        request = self._get(session, request_id)
        if caller.member_id in (request.requester_id, request.counterpart_id):
            raise Refused(
                "party_to_swap", "You are a party to this swap; another planner or admin decides it."
            )
        if request.state != rules.ACCEPTED:
            raise Refused("wrong_state", f"The request is {request.state}; only an accepted one is decided.")
        info = bound.scheduling.assignment(request.assignment_id)
        if not rules.before_deadline(now, info.start_at):
            raise _past_deadline(info)
        if outcome not in (APPROVE, REFUSE):
            raise Refused("invalid_request", "The outcome must be approve or refuse.")
        if outcome == APPROVE and reason is not None:
            raise Refused("invalid_reason", "An approval carries no reason.")
        if outcome == REFUSE:
            problem = rules.reason_problem(reason, rules.REFUSE_REASONS)
            if problem:
                raise _reason_refusal(problem, rules.REFUSE_REASONS)
        recorded, why = (rules.APPROVED, None) if outcome == APPROVE else (rules.REFUSED, reason)
        if outcome == APPROVE:
            try:
                bound.scheduling.transfer(request.assignment_id, request.counterpart_id)
            except TransferRefused as refused:
                recorded, why = rules.REFUSED, refused.reason
        decision = repo.add_decision(
            session,
            request_id=request.id,
            decider_id=caller.member_id,
            outcome=recorded,
            reason=why,
            decided_at=now,
        )
        request.state = recorded
        session.flush()
        row = _Rows(bound, now, caller.member_id, info).row(request, decision)
        directory = bound.member_directory
        members = (request.requester_id, request.counterpart_id)
        recipients = tuple(m for m in members if directory.is_active(m))
        if recorded == rules.APPROVED:
            event = SwapApproved(
                request_id=request.id,
                shift_date=info.shift_date,
                shift_start=info.start,
                new_holder_name=row.counterpart_name,
                recipient_ids=recipients,
            )
        else:
            event = SwapRefused(
                request_id=request.id,
                shift_date=info.shift_date,
                shift_start=info.start,
                reason=why,
                recipient_ids=recipients,
            )
        bound.notifier.notify(event)
        return row

    def mine(self, caller: Caller) -> list[RequestRow]:
        """R-swaps-09: every request the caller is party to, every state, newest first by created_at, then
        id descending; an inactive other party is still listed."""
        session = db.current_session()
        bound = self._bound()
        requests = repo.requests_of_member(session, caller.member_id)
        decisions = repo.decisions_of(session, (r.id for r in requests))
        rows = _Rows(bound, bound.clock.now(), caller.member_id)
        return [rows.row(r, decisions.get(r.id)) for r in requests]

    def pending(self, caller: Caller) -> list[RequestRow]:
        """R-swaps-09: the open accepted requests, oldest first by answered_at, then id ascending, the same
        for every planner and admin, with party per viewer; an accepted request past its deadline is
        absent."""
        session = db.current_session()
        if caller.role not in DECIDING_ROLES:
            raise Refused("forbidden", "Only a planner or an admin sees the pending decisions.")
        bound = self._bound()
        now = bound.clock.now()
        rows = _Rows(bound, now, caller.member_id)
        accepted = repo.requests_in_state(session, rules.ACCEPTED)
        open_ = [r for r in accepted if rules.is_open(r.state, now, rows.info(r.assignment_id).start_at)]
        decisions = repo.decisions_of(session, (r.id for r in open_))
        return [rows.row(r, decisions.get(r.id)) for r in open_]

    # ---- helpers
    @staticmethod
    def _get(session: Session, request_id: int) -> models.SwapRequest:
        request = repo.get_request(session, request_id)
        if request is None:
            raise Refused("not_found", f"No swap request has the id {request_id}.")
        return request

    @staticmethod
    def _has_open(session: Session, info: AssignmentInfo, now: datetime) -> bool:
        """R-swaps-02: one open request per assignment."""
        stored = repo.requests_on(session, [info.assignment_id], rules.OPEN_STATES)
        return any(rules.is_open(r.state, now, info.start_at) for r in stored)
