"""The contract unit's golden pin: the served OpenAPI document equals the committed golden byte for byte.

This module is both the test and the regeneration command (`python tests/api/test_openapi_golden.py` writes
the golden), and it carries its own falsification twins: the same helper must pass on the control app and
fail on a copy with one added route and on one with a changed description. A pin that cannot fail is no pin.
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
GOLDEN = ROOT / "contracts" / "openapi.golden.json"
REGENERATE = "python tests/api/test_openapi_golden.py"

sys.path.insert(0, str(ROOT / "src"))
from app.main import create_app  # noqa: E402  (the app factory; every default resolved at call time)


def canonical(document: dict) -> bytes:
    text = json.dumps(document, sort_keys=True, separators=(",", ":"), ensure_ascii=True, allow_nan=False)
    return text.encode("ascii")


def served() -> dict:
    return create_app().openapi()


def assert_matches_golden(document: dict) -> None:
    actual = canonical(document)
    expected = GOLDEN.read_bytes() if GOLDEN.exists() else b""
    assert actual == expected, (
        f"the served contract differs from {GOLDEN.relative_to(ROOT)} "
        f"({len(actual)} vs {len(expected)} bytes). "
        f"If the change is intended and admitted by a DECISIONS row, regenerate deliberately: {REGENERATE}"
    )


def test_the_served_contract_equals_the_golden() -> None:
    assert_matches_golden(served())


def test_the_golden_is_one_line_without_a_trailing_newline() -> None:
    raw = GOLDEN.read_bytes()
    assert b"\n" not in raw and raw.endswith(b"}")


def test_an_added_route_breaks_the_equality() -> None:
    app = create_app()

    @app.get("/api/__contract_freeze_probe__")
    def _probe() -> dict:  # pragma: no cover - never called
        return {}

    doc = app.openapi()
    try:
        assert_matches_golden(doc)
    except AssertionError as e:
        assert "regenerate deliberately" in str(e)
    else:
        raise AssertionError("the equality carried no information: an added route did not break it")


def test_a_changed_description_breaks_the_equality() -> None:
    doc = served()
    doc["info"]["description"] = (doc["info"].get("description") or "") + " (probe)"
    try:
        assert_matches_golden(doc)
    except AssertionError:
        return
    raise AssertionError("a changed description did not break the equality")


def test_two_builds_in_one_process_serve_identical_bytes() -> None:
    assert canonical(served()) == canonical(served())


def test_the_regeneration_command_reproduces_the_committed_bytes(tmp_path: Path) -> None:
    out = tmp_path / "golden.json"
    cmd = [sys.executable, __file__, "--out", str(out)]
    r = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, check=False)
    assert r.returncode == 0, r.stderr
    assert out.read_bytes() == GOLDEN.read_bytes()


if __name__ == "__main__":
    target = GOLDEN
    if "--out" in sys.argv:
        target = Path(sys.argv[sys.argv.index("--out") + 1])
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(canonical(served()))
    print(f"golden written: {target} ({target.stat().st_size} bytes)")
