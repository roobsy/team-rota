"""Swaps' persistence (ADU-07, layer 3): the swap_requests and decisions rows of the data model.

Every function works in the session the service passes, which is always db.current_session() (D-14): nothing
here opens, commits or closes a session, reads the clock or checks a rule. Members, shifts and assignments are
other domains' rows and are never read here; swaps asks MemberDirectory and SchedulingPort (IR-01, IR-09).
"""

from __future__ import annotations

from collections.abc import Iterable
from datetime import datetime

from sqlalchemy import or_, select
from sqlalchemy.orm import Session

from app.models import Decision, SwapRequest


# ---- requests
def get_request(session: Session, request_id: int) -> SwapRequest | None:
    return session.get(SwapRequest, request_id)


def add_request(
    session: Session,
    *,
    assignment_id: int,
    requester_id: int,
    counterpart_id: int,
    reason: str,
    state: str,
    created_at: datetime,
) -> SwapRequest:
    """A new request; flushed, so the store has assigned its id."""
    request = SwapRequest(
        assignment_id=assignment_id,
        requester_id=requester_id,
        counterpart_id=counterpart_id,
        reason=reason,
        state=state,
        created_at=created_at,
    )
    session.add(request)
    session.flush()
    return request


def requests_on(session: Session, assignment_ids: Iterable[int], states: Iterable[str]) -> list[SwapRequest]:
    """The requests on these assignments stored in one of `states`, by id."""
    ids, wanted = list(assignment_ids), list(states)
    if not ids:
        return []
    query = (
        select(SwapRequest)
        .where(SwapRequest.assignment_id.in_(ids), SwapRequest.state.in_(wanted))
        .order_by(SwapRequest.id)
    )
    return list(session.scalars(query))


def requests_of_member(session: Session, member_id: int) -> list[SwapRequest]:
    """Every request the member is party to, newest first by created_at, then id descending (R-swaps-09)."""
    query = (
        select(SwapRequest)
        .where(or_(SwapRequest.requester_id == member_id, SwapRequest.counterpart_id == member_id))
        .order_by(SwapRequest.created_at.desc(), SwapRequest.id.desc())
    )
    return list(session.scalars(query))


def requests_in_state(session: Session, state: str) -> list[SwapRequest]:
    """The requests stored in `state`, oldest first by answered_at, then id ascending (R-swaps-09)."""
    query = (
        select(SwapRequest)
        .where(SwapRequest.state == state)
        .order_by(SwapRequest.answered_at.asc(), SwapRequest.id.asc())
    )
    return list(session.scalars(query))


# ---- decisions
def add_decision(
    session: Session,
    *,
    request_id: int,
    decider_id: int,
    outcome: str,
    reason: str | None,
    decided_at: datetime,
) -> Decision:
    """A new decision; flushed, so the store has assigned its id."""
    decision = Decision(
        request_id=request_id, decider_id=decider_id, outcome=outcome, reason=reason, decided_at=decided_at
    )
    session.add(decision)
    session.flush()
    return decision


def decisions_of(session: Session, request_ids: Iterable[int]) -> dict[int, Decision]:
    """The decision of each of these requests that has one, by request id (one per request, R-swaps-04)."""
    ids = list(request_ids)
    if not ids:
        return {}
    query = select(Decision).where(Decision.request_id.in_(ids)).order_by(Decision.id)
    return {d.request_id: d for d in session.scalars(query)}
