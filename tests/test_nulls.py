"""ADU-16 arms 3–4: one test per Null — each test is deleted together with its Null by the retiring unit (its amends);
the file goes with the last Null (ADU-07)."""

from __future__ import annotations

from datetime import datetime

import pytest

from app import ports
from app.identity.null_directory import NullDirectory
from app.notifications.null_notifier import NullNotifier
from app.scheduling.null_port import NullSchedulingPort
from app.swaps.null_port import NullSwapsPort

REPLACED = {
    NullDirectory: "ADU-03",
    NullSchedulingPort: "ADU-05",
    NullSwapsPort: "ADU-07",
    NullNotifier: "ADU-09",
}


@pytest.mark.parametrize("cls", list(REPLACED))
def test_each_null_names_its_provider_and_satisfies_its_protocol(cls: type) -> None:
    assert f"replaced by {REPLACED[cls]}, class not shape" in (cls.__doc__ or "")
    proto = {
        NullDirectory: ports.MemberDirectory,
        NullSchedulingPort: ports.SchedulingPort,
        NullSwapsPort: ports.SwapsPort,
        NullNotifier: ports.Notifier,
    }[cls]
    assert isinstance(cls(), proto)


def test_null_directory_resolves_synthetic_tokens_and_answers_the_empty_value() -> None:  # deleted by ADU-03
    d = NullDirectory()
    assert d.caller_for_token("tok_7") == ports.Caller(
        member_id=7, name="Member 7", role="member", active=True
    )
    assert d.caller_for_token("tok_admin").role == "admin" and d.caller_for_token("garbage") is None
    assert d.is_active(7) is True and d.role_of(7) == "member" and d.name_of(7) == "Member 7"
    assert d.active_member_ids() == [] and d.decider_ids() == []


def test_null_scheduling_port_does_nothing_observable() -> None:  # deleted by ADU-05
    p = NullSchedulingPort()
    with pytest.raises(ports.AssignmentNotFound):
        p.assignment(1)
    assert (
        p.holds_intersecting_shift(1, 1) is False
        and p.has_assignment_after(1, datetime(2026, 11, 5, 9)) is False
    )
    assert p.transfer(1, 2) is None


def test_null_swaps_port_answers_nothing_pending_and_nothing_requestable() -> None:  # deleted by ADU-07
    assert NullSwapsPort().view(1, True, [(5, 1, datetime(2026, 11, 9, 8))]) == {
        5: ports.AssignmentView(pending=None, requestable=False)
    }


def test_null_notifier_records_and_writes_nothing() -> None:  # deleted by ADU-09
    n = NullNotifier()
    n.notify(ports.MemberAdded(member_id=1, role="admin"))
    assert len(n.sent) == 1 and type(n.sent[0]).__name__ == "MemberAdded"
