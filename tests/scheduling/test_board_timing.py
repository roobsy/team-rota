"""ADU-05 arm 7 - the board's p95 over seeded_week(20261107): the timing tier, reported, never gating.

Every member, name, e-mail, passcode, date and id here is SYNTHETIC. src/app/synthetic.py seeded_week(SEED)
generates them (R-scheduling-09), the same bytes on every run, and none is real data.

Arm 7 -> test_board_p95. tests/conftest.py TIMING_NODES registers it by its exact node id, so it is timing-
and calibration-marked. Its deterministic sibling in the gate is tests/scheduling/test_scheduling_service.py::
test_arm8_the_board_over_seeded_week_has_21_shifts_42_rows_5_pending_and_the_admins_requestable.
The arm's band logic has its own gate tests here, test_the_verdict_bands and test_nearest_rank, because a real
measurement never reaches the 300-350 band, so the band logic would otherwise go untested.

What is measured. The fixture is loaded into a fresh workspace. The caller is the fixture's admin, and the
call is board(caller, the fixture's start_date) with mine unset. 5 untimed warm-ups come first, then N=50
timed calls. Each call runs in its own unit of work, and time.perf_counter is read around the board call
itself. p95 is by nearest rank: the ceil(0.95 * n)-th smallest sample.
- p95 <= 300 ms passes.
- 300 < p95 <= 350 ms is within tolerance: it passes and emits a report line, as a pytest warning.
- p95 > 350 ms is red and fails.
The service's bindings are the deterministic sibling's doubles: FakeMemberDirectory filled from the fixture's
members, FakeSwapsPort with nothing configured, SpyNotifier, and FixedClock at the fixture's clock. So the
number is scheduling's own cost (its reads in the current session and the shaping of the value), not
identity's or swaps'.

The measuring command (the arm's measured_by):
    uv run python tests/scheduling/test_board_timing.py --measure
It prints n, min, p50, p95, max and the verdict, in ASCII only (the console is cp1252). Its exit status is 0
for pass or within tolerance, and 1 for red.
"""

from __future__ import annotations

import argparse
import sys
import tempfile
import time
import warnings
from collections.abc import Sequence
from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path
from types import SimpleNamespace

import pytest

if __name__ == "__main__":  # script mode: pytest's pythonpath (src, tests) is not set
    _ROOT = Path(__file__).resolve().parents[2]
    sys.path[:0] = [str(_ROOT / "src"), str(_ROOT / "tests")]

from support.doubles import FakeMemberDirectory, FakeSwapsPort, FixedClock, SpyNotifier  # noqa: E402

from app import db, ports, synthetic  # noqa: E402
from app.scheduling import service as scheduling_service  # noqa: E402

THRESHOLD_MS = 300
TOLERANCE_MS = 50
N = 50
WARMUPS = 5
SEED = 20261107
PERCENT = 95


def nearest_rank(samples: Sequence[float], percent: int) -> float:
    """The nearest-rank percentile: the ceil(percent/100 * n)-th smallest sample, counted from 1. Integer
    arithmetic, so 95% of 20 is exactly the 19th."""
    ordered = sorted(samples)
    rank = -(-percent * len(ordered) // 100)
    return ordered[max(rank, 1) - 1]


def verdict(p95_ms: float) -> str:
    if p95_ms <= THRESHOLD_MS:
        return "pass"
    if p95_ms <= THRESHOLD_MS + TOLERANCE_MS:
        return "within tolerance"
    return "red"


@dataclass(frozen=True)
class Measurement:
    samples_ms: tuple[float, ...]
    shifts: int  # the measured board's size, so a refused or empty board cannot pass for a fast one
    holder_rows: int

    @property
    def p95_ms(self) -> float:
        return nearest_rank(self.samples_ms, PERCENT)

    @property
    def verdict(self) -> str:
        return verdict(self.p95_ms)

    def lines(self) -> list[str]:
        return [
            f"board over seeded_week({SEED}), the fixture's admin, mine unset; {WARMUPS} untimed warm-ups",
            f"n={len(self.samples_ms)} shifts={self.shifts} holder_rows={self.holder_rows}",
            f"min={min(self.samples_ms):.3f} ms",
            f"p50={nearest_rank(self.samples_ms, 50):.3f} ms",
            f"p95={self.p95_ms:.3f} ms (nearest rank)",
            f"max={max(self.samples_ms):.3f} ms",
            f"verdict: {self.verdict} (threshold {THRESHOLD_MS} ms, tolerance {TOLERANCE_MS} ms)",
        ]


def measure(workspace: Path, n: int = N, warmups: int = WARMUPS) -> Measurement:
    """The one measuring function, shared by test_board_p95 and --measure."""
    fixture = synthetic.seeded_week(SEED)
    engine = db.engine_for(workspace)
    try:
        synthetic.load_fixture(engine, fixture)
        directory = FakeMemberDirectory()
        for m in fixture["members"]:
            directory.add(m["id"], m["name"], m["role"], active=m["active"])
        bindings = SimpleNamespace(
            clock=FixedClock(datetime.fromisoformat(fixture["clock"])),
            member_directory=directory,
            swaps=FakeSwapsPort(),
            notifier=SpyNotifier(),
        )
        service = scheduling_service.SchedulingService(lambda: bindings)
        (admin,) = [m for m in fixture["members"] if m["role"] == "admin"]
        caller = ports.Caller(member_id=admin["id"], name=admin["name"], role=admin["role"], active=True)
        start_date = date.fromisoformat(fixture["weeks"][0]["start_date"])

        def once() -> tuple[float, object]:
            with db.unit_of_work(engine):
                began = time.perf_counter()
                board = service.board(caller, start_date)
                elapsed_ms = (time.perf_counter() - began) * 1000.0
            return elapsed_ms, board

        for _ in range(warmups):
            once()
        samples: list[float] = []
        board = None
        for _ in range(n):
            elapsed_ms, board = once()
            samples.append(elapsed_ms)
    finally:
        engine.dispose()  # release the SQLite file before the workspace is removed (Windows file locks)
    shifts = getattr(board, "shifts", ())
    return Measurement(tuple(samples), len(shifts), sum(len(s.holders) for s in shifts))


def test_board_p95(tmp_path: Path) -> None:
    measured = measure(tmp_path)
    report = " | ".join(measured.lines())
    assert (len(measured.samples_ms), measured.shifts, measured.holder_rows) == (N, 21, 42), report
    if measured.verdict == "within tolerance":
        warnings.warn(f"within tolerance: {report}", stacklevel=1)
    assert measured.verdict != "red", report


@pytest.mark.parametrize(
    "p95_ms, expected",
    [
        pytest.param(0.4, "pass", id="far-below"),
        pytest.param(300.0, "pass", id="at-the-threshold"),
        pytest.param(300.001, "within tolerance", id="just-above-the-threshold"),
        pytest.param(350.0, "within tolerance", id="at-the-tolerance"),
        pytest.param(350.001, "red", id="just-above-the-tolerance"),
    ],
)
def test_the_verdict_bands(p95_ms: float, expected: str) -> None:
    """The arm's three bands at their edges (pass <= 300 ms; 300-350 ms within tolerance; > 350 ms red).
    This is a gate test, because a real measurement never exercises the upper two."""
    assert verdict(p95_ms) == expected


@pytest.mark.parametrize(
    "n, rank",
    [pytest.param(50, 48, id="n50"), pytest.param(20, 19, id="n20"), pytest.param(1, 1, id="n1")],
)
def test_nearest_rank(n: int, rank: int) -> None:
    """p95 by nearest rank is the ceil(0.95 * n)-th smallest sample, whatever order the samples come in."""
    samples = [float(v) for v in range(n, 0, -1)]  # n, n-1, ..., 1: the k-th smallest is k
    assert nearest_rank(samples, PERCENT) == float(rank)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="ADU-05 arm 7: the board's p95 over seeded_week(20261107).")
    parser.add_argument(
        "--measure", action="store_true", help="measure and print n, min, p50, p95, max, verdict"
    )
    args = parser.parse_args(argv)
    if not args.measure:
        parser.print_help()
        return 2
    with tempfile.TemporaryDirectory(prefix="rota-board-timing-") as workspace:
        measured = measure(Path(workspace))
    for line in measured.lines():
        print(line)
    return 1 if measured.verdict == "red" else 0


if __name__ == "__main__":
    sys.exit(main())
