"""ADU-00 — the method guard: the one test that checks the method itself.

Every check here is shown to fire on a planted fault in a temporary copy of the project (guard on the guard):
a method that cannot check itself was absent for Crucible's first sessions, when a filename kept its
constitution from auto-loading. These tests call the plugin's `adu` command; they never read the ledgers
themselves (the command is the one reader).
"""
from __future__ import annotations

import os
import shutil
import subprocess
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
IGNORE = shutil.ignore_patterns(".venv", "node_modules", ".git", "__pycache__", ".pytest_cache", "frontend")


def plugin_root() -> Path:
    env = os.environ.get("ADU_PLUGIN_ROOT")
    marker = ROOT / ".adu" / "plugin-root"
    if env:
        return Path(env)
    if marker.exists():
        return Path(marker.read_text(encoding="utf-8").strip())
    raise AssertionError(
        "the adu plugin root is unknown on this machine: set ADU_PLUGIN_ROOT, or open the project once in a "
        "Claude Code session with the adu-lifecycle plugin installed (its SessionStart hook writes .adu/plugin-root)"
    )


def adu(*args: str, cwd: Path = ROOT) -> subprocess.CompletedProcess[str]:
    cli = plugin_root() / "scripts" / "adu.mjs"
    return subprocess.run(["node", str(cli), *args], cwd=cwd, capture_output=True, text=True, check=False)


@pytest.fixture
def copy(tmp_path: Path) -> Path:
    dst = tmp_path / "copy"
    shutil.copytree(ROOT, dst, ignore=IGNORE)
    return dst


def test_the_bootstrap_manifest_and_its_invariants_hold() -> None:
    r = adu("init", "--check")
    assert r.returncode == 0, r.stderr
    assert "init OK" in r.stdout


def test_a_planted_wrong_pin_in_a_copy_fails_pins_check(copy: Path) -> None:
    pins = [l for l in (copy / "PINS.lock").read_text(encoding="utf-8").splitlines() if l and not l.startswith("#")]
    assert pins, "nothing is pinned yet: pin the brief first (adu pins add design/PRODUCT-BRIEF.md)"
    pinned = copy / pins[0].split()[1]
    pinned.write_text(pinned.read_text(encoding="utf-8") + "\nedited after the pin\n", encoding="utf-8")
    r = adu("pins", "check", cwd=copy)
    assert r.returncode == 2 and "content differs from its pin" in r.stderr


def test_a_duplicated_now_line_in_a_copy_fails_ledger_lint(copy: Path) -> None:
    status = copy / "STATUS.md"
    text = status.read_text(encoding="utf-8")
    status.write_text(text.replace("## Now:", "## Now: ADU-00\n\n## Now:", 1), encoding="utf-8")
    r = adu("ledger", cwd=copy)
    assert r.returncode == 2 and '"## Now:" lines' in r.stderr


def test_plan_check_passes_here_and_fails_on_a_planted_cycle(copy: Path) -> None:
    assert adu("plan", "check").returncode == 0, adu("plan", "check").stderr
    plan = copy / "ADU-PLAN.md"
    text = plan.read_text(encoding="utf-8")
    # ADU-00 consumes an interface that a new unit provides while that unit consumes ADU-00's — a cycle
    text = text.replace("consumes: []", "consumes: [cycle.probe]", 1)
    text += (
        "\n### ADU-99 — Planted cycle\n```yaml adu\nid: ADU-99\ntitle: Planted cycle\nlayer: 3\ndomain: platform\n"
        "stories: []\nprovides: [cycle.probe]\nconsumes: [method.guard]\ndepends: [ADU-00]\nfiles: [src/app/x.py]\n"
        "tests: [tests/test_x.py]\namends: []\nmocks: []\nsize: S\nacceptance:\n"
        "  - { arm: a, file: tests/test_x.py, kind: deterministic }\n  - { arm: b, file: tests/test_x.py, kind: deterministic }\n"
        "  - { arm: c, file: tests/test_x.py, kind: deterministic }\n  - { arm: d, file: tests/test_x.py, kind: deterministic }\nowed: []\n```\n"
    )
    plan.write_text(text, encoding="utf-8")
    r = adu("plan", "check", cwd=copy)
    assert r.returncode == 2 and "cycle" in r.stderr
