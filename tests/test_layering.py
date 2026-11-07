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
