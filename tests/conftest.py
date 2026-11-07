"""Test tiers, applied by node id — never by a decorator on a test (tests of completed units are immutable).

gate   = pytest -m "not timing"       (the operator's gate; closes a unit)
fast   = pytest -m "not calibration"  (a session's inner loop; the session-end hook; never closes a unit)
timing = pytest -m timing             (wall-clock budget arms; run deliberately; reported, never gating)

Every timing arm is also calibration-marked, so the fast tier excludes it without a second list. A prefix that
matches nothing is a stale pattern and fails test_tiers.py.
"""

from __future__ import annotations

import pytest

#: node-id prefixes of tests that measure a distribution, a rate, a frontier or a budget, each with its reason
CALIBRATION_NODES: dict[str, str] = {
    # "tests/test_calibration.py": "measures detection power; minutes, not seconds",
}
#: exact node ids of wall-clock budget arms, each naming its deterministic sibling in the gate
TIMING_NODES: dict[str, str] = {
    # "tests/test_cli.py::TestTheChainFitsItsBudget::test_whole_chain": "sibling: tests/test_cli_chain.py",
}


def pytest_configure(config: pytest.Config) -> None:
    config.addinivalue_line(
        "markers", "calibration: measures a distribution, a rate, a frontier or a budget (fast tier excludes)"
    )
    config.addinivalue_line("markers", "timing: a wall-clock budget arm (never gates; also calibration)")


def pytest_collection_modifyitems(config: pytest.Config, items: list[pytest.Item]) -> None:
    for item in items:
        if any(item.nodeid.startswith(p) for p in CALIBRATION_NODES):
            item.add_marker(pytest.mark.calibration)
        if item.nodeid in TIMING_NODES:
            item.add_marker(pytest.mark.timing)
            item.add_marker(pytest.mark.calibration)
