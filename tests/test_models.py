"""ADU-01 arms 1–3: the stored entities, their constraints, their types — asserted against the database."""

from __future__ import annotations

import re
from datetime import date, datetime, time
from pathlib import Path

import pytest
from sqlalchemy import Date, DateTime, Time, inspect, select
from sqlalchemy.exc import IntegrityError

from app import db, models

ROOT = Path(__file__).resolve().parents[1]


def _member(**kw):
    base = dict(name="Mo", email="mo@example.test", role="member", active=True, passcode_hash="x", token=None)
    base.update(kw)
    return models.Member(**base)


def test_the_entities_exist_as_tables_with_their_key_fields_and_a_fresh_file_per_workspace(
    tmp_path: Path,
) -> None:
    engine = db.engine_for(tmp_path / "one")
    assert (tmp_path / "one" / "rota.sqlite").exists()
    names = set(inspect(engine).get_table_names())
    assert names == {
        "members",
        "weeks",
        "shifts",
        "assignments",
        "swap_requests",
        "decisions",
        "notifications",
    }
    cols = {t: {c["name"] for c in inspect(engine).get_columns(t)} for t in names}
    assert {"id", "name", "email", "role", "active", "passcode_hash", "token"} <= cols["members"]
    assert cols["weeks"] >= {"start_date", "state"} and "id" not in cols["weeks"]
    assert {"id", "week_start", "date", "start", "end", "slots"} <= cols["shifts"]
    assert {"id", "shift_id", "member_id"} <= cols["assignments"]
    assert {
        "id",
        "assignment_id",
        "requester_id",
        "counterpart_id",
        "reason",
        "state",
        "created_at",
        "answered_at",
        "answer_reason",
    } <= cols["swap_requests"]
    assert {"id", "request_id", "decider_id", "outcome", "reason", "decided_at"} <= cols["decisions"]
    assert {"id", "recipient_id", "event", "text", "created_at", "read"} <= cols["notifications"]
    other = db.engine_for(tmp_path / "two")
    with db.session_for(engine) as s:
        s.add(_member())
        s.commit()
    with db.session_for(other) as s:
        assert s.scalars(select(models.Member)).all() == []  # workspaces are independent files


def test_the_constraints_hold_at_the_database(tmp_path: Path) -> None:
    engine = db.engine_for(tmp_path)
    with db.session_for(engine) as s:
        s.add(_member(email="Mo@Example.test"))
        s.commit()
        s.add(_member(email="mo@example.test"))
        with pytest.raises(IntegrityError):
            s.commit()
        s.rollback()
        s.add(_member(email="x@example.test", role="boss"))
        with pytest.raises(IntegrityError):
            s.commit()
        s.rollback()
        s.add(models.Week(start_date=date(2026, 11, 9), state="draft"))
        s.commit()
        s.add(
            models.Shift(
                week_start=date(2026, 11, 9), date=date(2026, 11, 9), start=time(8), end=time(12), slots=0
            )
        )
        with pytest.raises(IntegrityError):
            s.commit()
        s.rollback()
        s.add(models.Week(start_date=date(2026, 11, 16), state="open"))
        with pytest.raises(IntegrityError):
            s.commit()
        s.rollback()
        shift = models.Shift(
            week_start=date(2026, 11, 9), date=date(2026, 11, 9), start=time(8), end=time(12), slots=2
        )
        s.add(shift)
        s.commit()
        a = models.Assignment(shift_id=shift.id, member_id=1)
        s.add(a)
        s.commit()
        s.add(
            models.SwapRequest(
                assignment_id=a.id,
                requester_id=1,
                counterpart_id=1,
                reason="sick",
                state="expired",
                created_at=datetime(2026, 11, 5, 9),
            )
        )
        with pytest.raises(IntegrityError):
            s.commit()
        s.rollback()


def test_timestamps_are_naive_dates_are_dates_ids_are_creation_ordered_and_nothing_reads_the_clock(
    tmp_path: Path,
) -> None:
    for table in models.Base.metadata.tables.values():
        for col in table.columns:
            if isinstance(col.type, DateTime):
                assert col.type.timezone is False, f"{table.name}.{col.name} must be naive"
            if col.name in {"date", "start_date"}:
                assert isinstance(col.type, Date)
            if col.name in {"start", "end"}:
                assert isinstance(col.type, Time)
    engine = db.engine_for(tmp_path)
    with db.session_for(engine) as s:
        first = _member(email="a@example.test")
        second = _member(email="b@example.test")
        s.add(first)
        s.commit()
        s.add(second)
        s.commit()
        assert first.id == 1 and second.id == 2
    src = (ROOT / "src" / "app" / "models.py").read_text() + (ROOT / "src" / "app" / "db.py").read_text()
    assert not re.search(r"datetime\.(now|utcnow|today)\(|date\.today\(", src)
