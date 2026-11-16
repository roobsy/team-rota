"""Swaps' rules as pure functions (ADU-07, layer 3): no session, no clock, no other domain.

The service reads the clock and the shift's start instant (from SchedulingPort, or from the triple scheduling
hands to SwapsPort.view) and computes with these before it writes (design/ARCHITECTURE.md, Persistence and
concurrency rules: compute first, then write).
"""

from __future__ import annotations

from datetime import datetime, timedelta

REQUESTED, ACCEPTED, DECLINED, APPROVED, REFUSED = "requested", "accepted", "declined", "approved", "refused"
EXPIRED = "expired"  # a display state only, derived on read; never stored (R-swaps-06)
OPEN_STATES = (REQUESTED, ACCEPTED)

#: every request, answer and decision is allowed while now < the shift's start instant - 24 h (R-swaps-01)
DEADLINE_BEFORE_START = timedelta(hours=24)

# the reason codes a caller may send, per operation (R-swaps-07); the system codes counterpart_overlap and
# counterpart_inactive are written by the transfer only, so a caller who sends one is refused invalid_reason
REQUEST_REASONS = ("sick", "family", "travel", "other")
DECLINE_REASONS = ("unavailable", "other")
REFUSE_REASONS = ("fairness", "coverage", "policy", "other")


def deadline(start_at: datetime) -> datetime:
    """The instant from which nothing more may happen on the assignment's swaps (R-swaps-01)."""
    return start_at - DEADLINE_BEFORE_START


def before_deadline(now: datetime, start_at: datetime) -> bool:
    """The half-open rule of PRODUCT-DESIGN, The clock: allowed while now < deadline."""
    return now < deadline(start_at)


def is_open(state: str, now: datetime, start_at: datetime) -> bool:
    """Open is stored requested or accepted and now < deadline (R-swaps-06)."""
    return state in OPEN_STATES and before_deadline(now, start_at)


def display_state(state: str, now: datetime, start_at: datetime) -> str:
    """The stored state, or expired for a stored requested or accepted request past its deadline."""
    return EXPIRED if state in OPEN_STATES and not before_deadline(now, start_at) else state


def awaiting(state: str, now: datetime, start_at: datetime) -> str:
    """Who acts next (R-swaps-09): the counterpart while open in requested, a decider while open in accepted,
    none otherwise."""
    if not is_open(state, now, start_at):
        return "none"
    return "counterpart" if state == REQUESTED else "decider"


def requestable(
    caller_id: int, holder_id: int, week_published: bool, has_open: bool, now: datetime, start_at: datetime
) -> bool:
    """The caller may request a swap on the assignment now: own row, published week, no open request,
    now < deadline (IR-07)."""
    return caller_id == holder_id and week_published and not has_open and before_deadline(now, start_at)


def reason_problem(reason: str | None, allowed: tuple[str, ...]) -> str | None:
    """The validation code for a reason that must be given (reason_required, invalid_reason), or None."""
    if reason is None:
        return "reason_required"
    return None if reason in allowed else "invalid_reason"
