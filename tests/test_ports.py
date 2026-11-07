"""ADU-16 arms 1, 2, 5, 6: the five protocols, the doubles that satisfy them, the ports' isolation, no vacuous
oracle."""

from __future__ import annotations

import inspect
import re
from datetime import date, datetime, time
from pathlib import Path

from support import doubles

from app import ports

ROOT = Path(__file__).resolve().parents[1]


def test_the_five_protocols_and_their_values_exist_with_the_stated_signatures() -> None:
    for name in ("Clock", "MemberDirectory", "SchedulingPort", "SwapsPort", "Notifier"):
        assert getattr(ports, name).__class__.__name__ in {"_ProtocolMeta", "type"}
    assert set(inspect.signature(ports.MemberDirectory.caller_for_token).parameters) == {"self", "token"}
    assert set(inspect.signature(ports.SchedulingPort.transfer).parameters) == {
        "self",
        "assignment_id",
        "to_member_id",
    }
    assert set(inspect.signature(ports.SchedulingPort.has_assignment_after).parameters) == {
        "self",
        "member_id",
        "now",
    }
    assert set(inspect.signature(ports.SwapsPort.view).parameters) == {
        "self",
        "caller_id",
        "week_published",
        "assignments",
    }
    assert set(inspect.signature(ports.Notifier.notify).parameters) == {"self", "event"}
    caller = ports.Caller(member_id=1, name="Avi", role="admin", active=True)
    info = ports.AssignmentInfo(
        assignment_id=1,
        holder_id=2,
        shift_id=3,
        shift_date=date(2026, 11, 9),
        start=time(8),
        end=time(12),
        start_at=datetime(2026, 11, 9, 8),
        week_start=date(2026, 11, 9),
        week_state="published",
        holder_ids=(2, 4),
    )
    view = ports.AssignmentView(pending=None, requestable=False)
    assert caller.role == "admin" and info.holder_ids == (2, 4) and view.requestable is False
    events = [
        ports.WeekPublished,
        ports.SwapRequested,
        ports.SwapAccepted,
        ports.SwapDeclined,
        ports.SwapApproved,
        ports.SwapRefused,
        ports.MemberAdded,
        ports.RoleChanged,
        ports.MemberDeactivated,
    ]
    assert [e.code for e in events] == list(ports.EVENT_CODES)
    assert not hasattr(ports, "FixedClock")  # the fixed clock is a test double, not a port
    assert isinstance(ports.SystemClock().now(), datetime)


def test_the_doubles_satisfy_their_protocols_and_are_settable() -> None:
    spy = doubles.SpyNotifier()
    spy.notify(ports.MemberAdded(member_id=4, role="member"))
    assert [type(e).__name__ for e in spy.sent] == ["MemberAdded"]
    sched = doubles.FakeSchedulingPort()
    sched.set_has_assignment_after(7, True)
    assert (
        sched.has_assignment_after(7, datetime(2026, 11, 5, 9)) is True
        and sched.has_assignment_after(8, datetime(2026, 11, 5, 9)) is False
    )
    sched.set_transfer_outcome("counterpart_overlap")
    try:
        sched.transfer(1, 2)
    except ports.TransferRefused as e:
        assert e.reason == "counterpart_overlap"
    else:
        raise AssertionError("the configured refusal did not fire")
    swaps = doubles.FakeSwapsPort()
    swaps.set_view(5, ports.AssignmentView(pending="requested", requestable=False))
    out = swaps.view(1, True, [(5, 1, datetime(2026, 11, 9, 8)), (6, 1, datetime(2026, 11, 9, 12))])
    assert out[5].pending == "requested" and out[6] == ports.AssignmentView(pending=None, requestable=False)
    members = doubles.FakeMemberDirectory()
    members.add(1, "Avi", "admin", active=True, token="tok_a")
    members.add(2, "Mo", "member", active=False)
    assert members.caller_for_token("tok_a") == ports.Caller(
        member_id=1, name="Avi", role="admin", active=True
    )
    assert (
        members.caller_for_token("nope") is None
        and members.is_active(9) is None
        and members.is_active(2) is False
    )
    assert members.decider_ids() == [1] and members.active_member_ids() == [1]
    clock = doubles.FixedClock(datetime(2026, 11, 5, 9))
    assert clock.now() == datetime(2026, 11, 5, 9)
    clock.advance(minutes=30)
    assert clock.now() == datetime(2026, 11, 5, 9, 30)
    for proto, obj in (
        (ports.Notifier, spy),
        (ports.SchedulingPort, sched),
        (ports.SwapsPort, swaps),
        (ports.MemberDirectory, members),
        (ports.Clock, clock),
    ):
        assert isinstance(obj, proto)


def test_the_ports_module_imports_nothing_of_the_product() -> None:
    src = (ROOT / "src" / "app" / "ports.py").read_text(encoding="utf-8")
    assert not re.search(r"^\s*(from|import) app\b", src, re.M)


def test_no_double_is_a_vacuous_oracle() -> None:
    assert doubles.VACUOUS == (), (
        "a double that round-trips its input must be listed and never used as an oracle"
    )
    swaps = doubles.FakeSwapsPort()
    assert swaps.view(1, True, [(5, 1, datetime(2026, 11, 9, 8))]) == {
        5: ports.AssignmentView(pending=None, requestable=False)
    }
