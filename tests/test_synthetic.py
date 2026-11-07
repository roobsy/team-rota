"""ADU-01 arms 4–6: seeded_week implements R-scheduling-09 and reproduces the committed fixture bytes."""

from __future__ import annotations

import json
from datetime import date, datetime, time
from pathlib import Path

from sqlalchemy import select

from app import db, models
from app.synthetic import FIXTURE_NAMES, load_fixture, seeded_week, serialise

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "tests" / "fixtures" / "seeded_week_20261107.json"
SHIFT_TIMES = [(time(8), time(12)), (time(12), time(16)), (time(16), time(20))]


def test_seeded_week_implements_the_rule_and_reproduces_the_committed_bytes(tmp_path: Path) -> None:
    fx = seeded_week(20261107)
    assert serialise(fx) == FIXTURE.read_bytes()
    assert serialise(seeded_week(20261107)) == serialise(fx)  # a second run, same bytes
    assert fx["clock"] == "2026-11-05T09:00:00"
    members = fx["members"]
    assert [m["id"] for m in members] == list(range(1, 13))
    assert [m["role"] for m in members] == ["admin", "planner", "planner"] + ["member"] * 9
    assert all(m["active"] for m in members)
    assert fx["weeks"] == [{"start_date": "2026-11-09", "state": "published"}]
    shifts = fx["shifts"]
    assert len(shifts) == 21 and all(s["slots"] == 2 for s in shifts)
    expected = [
        (date(2026, 11, 9 + d).isoformat(), st.isoformat("minutes"), en.isoformat("minutes"))
        for d in range(7)
        for st, en in SHIFT_TIMES
    ]
    assert [(s["date"], s["start"], s["end"]) for s in shifts] == expected
    assignments = fx["assignments"]
    assert len(assignments) == 42
    # round-robin over all 12 members in id order; slots walked by date, start, slot index; ids follow the w
    walk = [(s["id"], slot) for s in shifts for slot in range(2)]
    for i, (a, (shift_id, _)) in enumerate(zip(assignments, walk)):
        assert a["id"] == i + 1 and a["shift_id"] == shift_id and a["member_id"] == (i % 12) + 1
    requests = fx["swap_requests"]
    assert [r["assignment_id"] for r in requests] == [1, 2, 3, 4, 5]
    assert [r["state"] for r in requests] == ["requested", "accepted", "requested", "accepted", "requested"]
    assert all(r["reason"] == "other" for r in requests)
    by_id = {a["id"]: a for a in assignments}
    shift_of = {s["id"]: s for s in shifts}
    for r in requests:
        holder = by_id[r["assignment_id"]]["member_id"]
        assert r["requester_id"] == holder and r["counterpart_id"] != holder
        assert members[r["counterpart_id"] - 1]["active"]
        sh = shift_of[by_id[r["assignment_id"]]["shift_id"]]
        same_day = [
            by_id[a["id"]]
            for a in assignments
            if shift_of[a["shift_id"]]["date"] == sh["date"] and a["member_id"] == r["counterpart_id"]
        ]
        for a in same_day:  # not on that shift and no intersecting shift that day (R-swaps-08)
            other = shift_of[a["shift_id"]]
            assert other["id"] != sh["id"]
            assert other["end"] <= sh["start"] or other["start"] >= sh["end"]
        assert r["created_at"] == "2026-11-05T09:00:00"
        assert (r["answered_at"] is not None) == (r["state"] == "accepted")
    # the fixture loads into the model
    engine = db.engine_for(tmp_path)
    load_fixture(engine, fx)
    with db.session_for(engine) as s:
        assert len(s.scalars(select(models.Assignment)).all()) == 42
        assert s.get(models.Week, date(2026, 11, 9)).state == "published"
        admin = s.get(models.Member, 1)
        assert admin.token == fx["admin_token"] and admin.passcode_hash == members[0]["passcode_hash"]
        assert isinstance(s.get(models.SwapRequest, 1).created_at, datetime)


def test_a_different_seed_produces_different_names_and_counterparts() -> None:
    a, b = seeded_week(20261107), seeded_week(1)
    assert serialise(a) != serialise(b)
    assert [m["name"] for m in a["members"]] != [m["name"] for m in b["members"]]
    assert [r["counterpart_id"] for r in a["swap_requests"]] != [
        r["counterpart_id"] for r in b["swap_requests"]
    ] or [m["passcode"] for m in a["members"]] != [m["passcode"] for m in b["members"]]


def test_the_fixture_file_is_labelled_synthetic_exposes_credentials_and_names_nobody_real() -> None:
    raw = json.loads(FIXTURE.read_text(encoding="utf-8"))
    assert list(raw)[0] == "SYNTHETIC" and "no real person" in raw["SYNTHETIC"]
    assert raw["admin_token"] and all(m["passcode"] and m["passcode_hash"] for m in raw["members"])
    for m in raw["members"]:
        assert m["name"] in FIXTURE_NAMES and m["email"].endswith("@example.test")
