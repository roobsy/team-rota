"""The served contract carries the field metadata the UI reads; a negative control proves the lint fires."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from app.main import create_app  # noqa: E402

# ---- the field-metadata lint, from the adapter's metadata_lint.py.tmpl (ADU-02 keeps it inside this
# test file)

REQUIRED = ("title", "description", "example")
CHOICE_EXTRA = ("x-when-to-use",)


def lint_openapi(document: dict) -> list[str]:
    findings: list[str] = []
    for name, schema in (document.get("components", {}).get("schemas", {}) or {}).items():
        for prop, spec in (schema.get("properties", {}) or {}).items():
            if not isinstance(spec, dict):
                continue
            for key in REQUIRED:
                if key not in spec or (isinstance(spec.get(key), str) and not spec[key].strip()):
                    findings.append(f"{name}.{prop}: missing {key}")
            if spec.get("type") in ("number", "integer") or "enum" in spec:
                for key in CHOICE_EXTRA:
                    if key not in spec:
                        findings.append(f"{name}.{prop}: missing {key} (numeric or enum)")
    return findings


def test_the_served_contract_passes_the_metadata_lint() -> None:
    assert lint_openapi(create_app().openapi()) == []


def test_the_lint_fires_on_a_bare_property() -> None:
    doc = {"components": {"schemas": {"Bare": {"properties": {"count": {"type": "integer"}}}}}}
    findings = lint_openapi(doc)
    assert "Bare.count: missing title" in findings
    assert "Bare.count: missing x-when-to-use (numeric or enum)" in findings
