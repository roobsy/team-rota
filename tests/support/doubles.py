"""Permanent test doubles for the five ports (ADU-16). Consumer units test against these, never against a Null.

None of these round-trips its input as an oracle: a Fake answers what a test configured into it, and the test
asserts the consumer's behaviour given that answer (rule 13). VACUOUS lists any double that would merely echo —
there is none; a consumer test that asserts the configured value itself is vacuous and must say so.
"""

from __future__ import annotations

from datetime import datetime, timedelta
from typing import Iterable

from app import ports

VACUOUS: tuple[str, ...] = ()


class FixedClock:
    def __init__(self, at: datetime) -> None:
        self._at = at

    def now(self) -> datetime:
        return self._at

    def advance(self, **delta: int) -> None:
        self._at = self._at + timedelta(**delta)


class SpyNotifier:
    def __init__(self) -> None:
        self.sent: list[ports.Event] = []

    def notify(self, event: ports.Event) -> None:
        self.sent.append(event)


class FakeSchedulingPort:
    def __init__(self) -> None:
        self._assignments: dict[int, ports.AssignmentInfo] = {}
        self._after: dict[int, bool] = {}
        self._intersecting: set[tuple[int, int]] = set()
        self._transfer_reason: str | None = None
        self.transfers: list[tuple[int, int]] = []

    def set_assignment(self, info: ports.AssignmentInfo) -> None:
        self._assignments[info.assignment_id] = info

    def set_has_assignment_after(self, member_id: int, value: bool) -> None:
        self._after[member_id] = value

    def set_intersecting(self, member_id: int, shift_id: int, value: bool = True) -> None:
        if value:
            self._intersecting.add((member_id, shift_id))
        else:
            self._intersecting.discard((member_id, shift_id))

    def set_transfer_outcome(self, reason: str | None) -> None:
        self._transfer_reason = reason

    def assignment(self, assignment_id: int) -> ports.AssignmentInfo:
        if assignment_id not in self._assignments:
            raise ports.AssignmentNotFound(assignment_id)
        return self._assignments[assignment_id]

    def holds_intersecting_shift(self, member_id: int, shift_id: int) -> bool:
        return (member_id, shift_id) in self._intersecting

    def transfer(self, assignment_id: int, to_member_id: int) -> None:
        if self._transfer_reason:
            raise ports.TransferRefused(self._transfer_reason)
        self.transfers.append((assignment_id, to_member_id))

    def has_assignment_after(self, member_id: int, now: datetime) -> bool:
        return self._after.get(member_id, False)


class FakeSwapsPort:
    def __init__(self) -> None:
        self._views: dict[int, ports.AssignmentView] = {}
        self.calls: list[tuple[int, bool, list[tuple[int, int, datetime]]]] = []

    def set_view(self, assignment_id: int, view: ports.AssignmentView) -> None:
        self._views[assignment_id] = view

    def view(
        self, caller_id: int, week_published: bool, assignments: Iterable[tuple[int, int, datetime]]
    ) -> dict[int, ports.AssignmentView]:
        rows = list(assignments)
        self.calls.append((caller_id, week_published, rows))
        return {
            a: self._views.get(a, ports.AssignmentView(pending=None, requestable=False)) for a, _h, _s in rows
        }


class FakeMemberDirectory:
    def __init__(self) -> None:
        self._members: dict[int, tuple[str, str, bool]] = {}
        self._tokens: dict[str, int] = {}

    def add(
        self, member_id: int, name: str, role: str, active: bool = True, token: str | None = None
    ) -> None:
        self._members[member_id] = (name, role, active)
        if token:
            self._tokens[token] = member_id

    def caller_for_token(self, token: str) -> ports.Caller | None:
        member_id = self._tokens.get(token)
        if member_id is None:
            return None
        name, role, active = self._members[member_id]
        return ports.Caller(member_id=member_id, name=name, role=role, active=active) if active else None

    def is_active(self, member_id: int) -> bool | None:
        return self._members[member_id][2] if member_id in self._members else None

    def role_of(self, member_id: int) -> str:
        if member_id not in self._members:
            raise ports.MemberNotFound(member_id)
        return self._members[member_id][1]

    def name_of(self, member_id: int) -> str:
        if member_id not in self._members:
            raise ports.MemberNotFound(member_id)
        return self._members[member_id][0]

    def active_member_ids(self) -> list[int]:
        return [m for m, (_n, _r, a) in self._members.items() if a]

    def decider_ids(self) -> list[int]:
        return [m for m, (_n, r, a) in self._members.items() if a and r in ("admin", "planner")]
