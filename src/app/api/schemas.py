"""The contract's schemas as pydantic models, built from contracts/openapi.json at import (ADU-02).

One source: every `components.schemas` entry of the contract becomes a model with the same name, fields,
titles,
descriptions, examples and x-when-to-use, so the served document mirrors the contract and the
field-metadata lint
reads the same text. Fields the contract declares optional stay optional (the lenient read of the
design's refusal
rules); enumerated outputs are Literals; request enumerations that the domain checks stay strings.
"""

from __future__ import annotations

import json
from datetime import date
from pathlib import Path
from typing import Any, Literal

from pydantic import BaseModel, Field, create_model

CONTRACT_JSON = Path(__file__).resolve().parents[3] / "contracts" / "openapi.json"
CONTRACT: dict[str, Any] = json.loads(CONTRACT_JSON.read_text(encoding="utf-8"))
SCHEMAS: dict[str, dict[str, Any]] = CONTRACT["components"]["schemas"]
EXTRA_KEYS = ("example", "x-when-to-use", "x-values")

MODELS: dict[str, type[BaseModel]] = {}


def _ref_name(ref: str) -> str:
    return ref.rsplit("/", 1)[1]


def annotation(spec: dict[str, Any]) -> Any:
    """The Python annotation for a contract schema (used for fields, response models and example
    validation)."""
    if "$ref" in spec:
        return MODELS[_ref_name(spec["$ref"])]
    if "allOf" in spec and len(spec["allOf"]) == 1:
        return annotation(spec["allOf"][0])
    if "oneOf" in spec:
        parts = [annotation(s) for s in spec["oneOf"]]
        out = parts[0]
        for p in parts[1:]:
            out = out | p
        return out
    typ = spec.get("type")
    nullable = isinstance(typ, list) and "null" in typ
    if isinstance(typ, list):
        typ = [t for t in typ if t != "null"][0]
    if "enum" in spec:
        values = tuple(v for v in spec["enum"] if v is not None)
        base: Any = Literal[values]  # type: ignore[valid-type]
    elif typ == "null":
        return type(None)
    elif typ == "string":
        base = date if spec.get("format") == "date" else str
    elif typ == "integer":
        base = int
    elif typ == "number":
        base = float
    elif typ == "boolean":
        base = bool
    elif typ == "array":
        base = list[annotation(spec["items"])]  # type: ignore[misc]
    else:
        base = dict[str, Any]
    return base | None if nullable else base


def _extra(spec: dict[str, Any]):
    """A callable, so that keys with a null value (example: null) and the title of a $ref field survive."""
    keys = {k: spec[k] for k in EXTRA_KEYS if k in spec}
    if "title" in spec:
        keys["title"] = spec["title"]

    def apply(schema: dict[str, Any]) -> None:
        schema.update(keys)

    return apply


def _field(spec: dict[str, Any], required: bool) -> tuple[Any, Any]:
    default = ... if required else None
    ann = annotation(spec)
    if not required and ann is not type(None):
        ann = ann | None
    field = Field(
        default, title=spec.get("title"), description=spec.get("description"), json_schema_extra=_extra(spec)
    )
    return ann, field


def _build(name: str) -> type[BaseModel]:
    if name in MODELS:
        return MODELS[name]
    spec = SCHEMAS[name]
    for prop in spec.get("properties", {}).values():  # dependencies first (the contract has no cycles)
        for ref in _refs_in(prop):
            _build(ref)
    required = set(spec.get("required", []))
    fields = {pname: _field(pspec, pname in required) for pname, pspec in spec.get("properties", {}).items()}
    model = create_model(name, __module__=__name__, **fields)  # type: ignore[call-overload]
    model.__doc__ = spec.get("description", "")
    MODELS[name] = model
    return model


def _refs_in(spec: Any) -> list[str]:
    if isinstance(spec, dict):
        if "$ref" in spec:
            return [_ref_name(spec["$ref"])]
        return [r for v in spec.values() for r in _refs_in(v)]
    if isinstance(spec, list):
        return [r for v in spec for r in _refs_in(v)]
    return []


for _name in SCHEMAS:
    _build(_name)
globals().update(MODELS)
__all__ = ["CONTRACT", "MODELS", "annotation", *MODELS]
