"""Guard on the tiers: every test is in exactly one tier, no pattern is stale, timing implies calibration."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import conftest

ROOT = Path(__file__).resolve().parents[1]


def _collected(marker_expr: str) -> set[str]:
    out = subprocess.run(
        [
            sys.executable,
            "-m",
            "pytest",
            "tests/",
            "-q",
            "--collect-only",
            "-m",
            marker_expr,
            "-p",
            "no:cacheprovider",
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    ).stdout
    return {line.strip() for line in out.splitlines() if "::" in line}


def test_every_test_is_in_the_gate_or_the_timing_tier_and_not_both() -> None:
    gate = _collected("not timing")
    timing = _collected("timing")
    assert not (gate & timing)
    assert gate | timing == _collected("")


def test_timing_arms_are_also_calibration_so_the_fast_tier_excludes_them() -> None:
    assert _collected("timing") <= _collected("calibration")
    assert not (_collected("not calibration") & _collected("timing"))


def test_no_tier_pattern_is_stale() -> None:
    everything = _collected("")
    for prefix in conftest.CALIBRATION_NODES:
        assert any(n.startswith(prefix) for n in everything), f"stale calibration pattern: {prefix}"
    for node in conftest.TIMING_NODES:
        assert node in everything, f"stale timing node: {node}"
