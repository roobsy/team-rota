"""The layering ratchet as a test, with its guard on the guard (a planted crossing is caught)."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCAN = ROOT / "tests" / "layering_scan.py"


def run(root: Path, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(SCAN), "--root", str(root), *args], capture_output=True, text=True, check=False
    )


def test_the_real_tree_has_no_forbidden_crossing_and_matches_the_baseline() -> None:
    r = run(ROOT)
    assert r.returncode == 0, r.stdout + r.stderr


def test_a_planted_forbidden_import_is_caught(tmp_path: Path) -> None:
    pkg = tmp_path / "src" / "app"
    (pkg / "core").mkdir(parents=True)
    (pkg / "api").mkdir()
    (pkg / "__init__.py").write_text("", encoding="utf-8")
    (pkg / "core" / "__init__.py").write_text("", encoding="utf-8")
    (pkg / "core" / "rules.py").write_text("from app.api import routes\n", encoding="utf-8")
    (pkg / "api" / "__init__.py").write_text("", encoding="utf-8")
    (pkg / "api" / "routes.py").write_text("x = 1\n", encoding="utf-8")
    (tmp_path / "tests").mkdir()
    (tmp_path / "tests" / "layering.json").write_text(
        json.dumps(
            {
                "package_root": "src",
                "package": "app",
                "layers": {"core": ["app.core.*"], "api": ["app.api.*"]},
                "forbidden": [["core", "api"]],
                "frozen": [],
            }
        ),
        encoding="utf-8",
    )
    assert run(tmp_path, "--write-baseline").returncode == 0
    r = run(tmp_path)
    assert r.returncode == 1 and "app.core.rules imports app.api.routes" in r.stdout


def test_the_baseline_fails_both_ways(tmp_path: Path) -> None:
    pkg = tmp_path / "src" / "app"
    pkg.mkdir(parents=True)
    (pkg / "__init__.py").write_text("", encoding="utf-8")
    (pkg / "models.py").write_text("_secret = 1\n", encoding="utf-8")
    (pkg / "service.py").write_text("from app.models import _secret\n", encoding="utf-8")
    (tmp_path / "tests").mkdir()
    (tmp_path / "tests" / "layering.json").write_text(
        json.dumps({"package_root": "src", "package": "app", "layers": {}, "forbidden": [], "frozen": []}),
        encoding="utf-8",
    )
    assert run(tmp_path, "--write-baseline").returncode == 0
    assert run(tmp_path).returncode == 0
    (pkg / "service.py").write_text("from app.models import _secret, _other\n", encoding="utf-8")
    (pkg / "models.py").write_text("_secret = 1\n_other = 2\n", encoding="utf-8")
    r = run(tmp_path)
    assert r.returncode == 1 and "new frozen edge not in the baseline" in r.stdout
    (pkg / "service.py").write_text("x = 1\n", encoding="utf-8")
    r = run(tmp_path)
    assert r.returncode == 1 and "baseline edge no longer in the code" in r.stdout


# FB-01 (defect session 2026-11-07; Q-06 ruled option 1: appended here, lines 1-71 untouched).
# The operator's first own gate (a default Windows PowerShell: cp1252 locale, PYTHONUTF8 unset) failed the
# two planted tests above: the scan's child died with UnicodeEncodeError on the arrows and dashes of its
# messages, because a piped stdout takes the locale encoding. Every earlier gate ran with PYTHONUTF8=1 and no
# test forced a non-UTF-8 child. The tests below force the child to cp1252 (PYTHONIOENCODING=cp1252,
# PYTHONUTF8=0), so they fail in any shell, on any platform, while the scan prints a character cp1252 cannot
# encode.
# SYNTHETIC: the planted packages are written into tmp_path by the tests themselves; no fixture file is read.

REGENERATE = "python tests/layering_scan.py --write-baseline"


def cp1252_env() -> dict[str, str]:
    import os  # imported here, not at the top: the Q-06 grant is an append after line 71, nothing above it

    env = {k: v for k, v in os.environ.items() if k not in ("PYTHONUTF8", "PYTHONIOENCODING")}
    return {**env, "PYTHONIOENCODING": "cp1252", "PYTHONUTF8": "0"}


def run_cp1252(root: Path, *args: str) -> tuple[int, str, str]:
    """Run the scan with a cp1252 stdout; decode its output as cp1252, the encoding the child was given."""
    r = subprocess.run(
        [sys.executable, str(SCAN), "--root", str(root), *args],
        capture_output=True,
        env=cp1252_env(),
        check=False,
    )
    return r.returncode, r.stdout.decode("cp1252"), r.stderr.decode("cp1252", errors="backslashreplace")


def test_the_forced_child_really_writes_strict_cp1252() -> None:
    """Control: if the environment stopped forcing cp1252, the FB-01 tests would pass without testing."""
    probe = "import sys; print(sys.stdout.encoding, sys.stdout.errors, sys.flags.utf8_mode)"
    r = subprocess.run([sys.executable, "-c", probe], capture_output=True, env=cp1252_env(), check=False)
    assert r.stdout.decode("ascii").split() == ["cp1252", "strict", "0"]


def test_the_scan_source_is_ascii_only() -> None:
    """Every message the scan can print, including ones no planted tree reaches, encodes in any locale."""
    lines = SCAN.read_text(encoding="utf-8").splitlines()
    offenders = [(n, line) for n, line in enumerate(lines, 1) if not line.isascii()]
    assert offenders == []


def test_a_forbidden_crossing_is_reported_on_a_cp1252_stdout(tmp_path: Path) -> None:
    pkg = tmp_path / "src" / "app"
    (pkg / "core").mkdir(parents=True)
    (pkg / "api").mkdir()
    (pkg / "__init__.py").write_text("", encoding="utf-8")
    (pkg / "core" / "__init__.py").write_text("", encoding="utf-8")
    (pkg / "core" / "rules.py").write_text("from app.api import routes\n", encoding="utf-8")
    (pkg / "api" / "__init__.py").write_text("", encoding="utf-8")
    (pkg / "api" / "routes.py").write_text("x = 1\n", encoding="utf-8")
    (tmp_path / "tests").mkdir()
    (tmp_path / "tests" / "layering.json").write_text(
        json.dumps(
            {
                "package_root": "src",
                "package": "app",
                "layers": {"core": ["app.core.*"], "api": ["app.api.*"]},
                "forbidden": [["core", "api"]],
                "frozen": [],
            }
        ),
        encoding="utf-8",
    )
    finding = (
        f"{Path('src', 'app', 'core', 'rules.py')}:1 - app.core.rules imports app.api.routes "
        "(core->api: forbidden by the layering law)"
    )

    code, out, err = run_cp1252(tmp_path, "--write-baseline")
    assert code == 0, err
    assert "not frozen (forbidden, the next run fails on it): " + finding in out

    code, out, err = run_cp1252(tmp_path)
    assert code == 1, err
    assert "UnicodeEncodeError" not in err
    assert finding in out


def test_both_baseline_directions_are_reported_on_a_cp1252_stdout(tmp_path: Path) -> None:
    pkg = tmp_path / "src" / "app"
    pkg.mkdir(parents=True)
    (pkg / "__init__.py").write_text("", encoding="utf-8")
    (pkg / "models.py").write_text("_secret = 1\n_other = 2\n", encoding="utf-8")
    (pkg / "service.py").write_text("from app.models import _secret\n", encoding="utf-8")
    (tmp_path / "tests").mkdir()
    (tmp_path / "tests" / "layering.json").write_text(
        json.dumps({"package_root": "src", "package": "app", "layers": {}, "forbidden": [], "frozen": []}),
        encoding="utf-8",
    )
    code, out, err = run_cp1252(tmp_path, "--write-baseline")
    assert code == 0, err
    code, out, err = run_cp1252(tmp_path)
    assert code == 0, out + err

    (pkg / "service.py").write_text("from app.models import _secret, _other\n", encoding="utf-8")
    code, out, err = run_cp1252(tmp_path)
    assert code == 1, err
    assert "UnicodeEncodeError" not in err
    assert (
        "new frozen edge not in the baseline: app.service -> app.models ._other "
        f"({Path('src', 'app', 'service.py')}:1) - regenerate deliberately: {REGENERATE}"
    ) in out

    (pkg / "service.py").write_text("x = 1\n", encoding="utf-8")
    code, out, err = run_cp1252(tmp_path)
    assert code == 1, err
    assert "UnicodeEncodeError" not in err
    assert (
        "baseline edge no longer in the code: app.service -> app.models ._secret "
        f"- the baseline is stale: {REGENERATE}"
    ) in out
