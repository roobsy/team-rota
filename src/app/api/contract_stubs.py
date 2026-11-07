"""Every operation of the contract, served as a 501 not_built placeholder until its router lands (ADU-02).

The routes are registered from contracts/openapi.json with the contract's operationId, tags, parameters,
request
body, declared responses, x-story and x-roles, so the served document mirrors the contract from the
first commit
and the golden pin never changes shape while handlers fill in. The 501 is deliberately outside the
contract: absent
from the served document, exempt from the conformance helper, gone once the last router lands (ADU-08).
"""

from __future__ import annotations

import inspect
from datetime import date
from typing import Any

from fastapi import Depends, FastAPI, Path, Query, Response
from pydantic import TypeAdapter
from sqlalchemy.orm import Session

from app.api import schemas
from app.api.deps import get_session, require_caller
from app.ports import Caller

CONTRACT = schemas.CONTRACT
METHODS = ("get", "post", "put", "patch", "delete")
SESSION_DEP = Depends(get_session)
CALLER_DEP = Depends(require_caller)


class NotBuilt(Exception):
    def __init__(self, operation_id: str) -> None:
        super().__init__(operation_id)
        self.operation_id = operation_id


def resolve(obj: dict[str, Any]) -> dict[str, Any]:
    """Follows a $ref into components.responses / components.parameters."""
    if "$ref" in obj:
        section, name = obj["$ref"].split("/")[-2:]
        return CONTRACT["components"][section][name]
    return obj


def validate_example(schema: dict[str, Any], value: Any) -> None:
    TypeAdapter(schemas.annotation(schema)).validate_python(value)


def _param_annotation(spec: dict[str, Any]) -> Any:
    return schemas.annotation(spec)


def example_path(path: str) -> str:
    """The path with every parameter replaced by its contract example."""
    out = path
    for name, p in CONTRACT["components"]["parameters"].items():
        out = out.replace("{" + name + "}", str(p["schema"]["example"]))
    return out


def example_body(op: dict[str, Any]) -> Any:
    body = op.get("requestBody", {}).get("content", {}).get("application/json")
    if not body:
        return None
    first = next(iter(body.get("examples", {}).values()), None)
    return first["value"] if first else None


def _response_models(op: dict[str, Any]) -> dict[int, dict[str, Any]]:
    out: dict[int, dict[str, Any]] = {}
    for code, resp in op["responses"].items():
        resp = resolve(resp)
        entry: dict[str, Any] = {"description": resp.get("description", "")}
        content = resp.get("content", {}).get("application/json")
        if content:
            entry["model"] = schemas.annotation(content["schema"])
        out[int(code)] = entry
    return out


def _make_handler(op: dict[str, Any], params: list[inspect.Parameter]):
    def handler(**_kwargs: Any) -> Any:
        raise NotBuilt(op["operationId"])

    handler.__signature__ = inspect.Signature(params)  # type: ignore[attr-defined]
    handler.__name__ = op["operationId"].replace(".", "_")
    return handler


def register(app: FastAPI) -> None:
    for path, ops in CONTRACT["paths"].items():
        for method, op in ops.items():
            if method not in METHODS:
                continue
            params: list[inspect.Parameter] = []
            for raw in op.get("parameters", []):
                p = resolve(raw)
                ann = _param_annotation(p["schema"])
                if p["in"] == "path":
                    default = Path(..., description=p.get("description", ""))
                else:
                    default = Query(p["schema"].get("default"), description=p.get("description", ""))
                    if not p.get("required", False) and ann is not date:
                        ann = ann | None if p["schema"].get("default") is None else ann
                params.append(
                    inspect.Parameter(
                        p["name"], inspect.Parameter.KEYWORD_ONLY, default=default, annotation=ann
                    )
                )
            body = op.get("requestBody", {}).get("content", {}).get("application/json")
            if body:
                params.append(
                    inspect.Parameter(
                        "body", inspect.Parameter.KEYWORD_ONLY, annotation=schemas.annotation(body["schema"])
                    )
                )
            if op.get("security", [{"bearer": []}]) != []:
                params.append(
                    inspect.Parameter(
                        "caller", inspect.Parameter.KEYWORD_ONLY, default=CALLER_DEP, annotation=Caller
                    )
                )
            params.append(
                inspect.Parameter(
                    "session", inspect.Parameter.KEYWORD_ONLY, default=SESSION_DEP, annotation=Session
                )
            )
            responses = _response_models(op)
            success = min(c for c in responses if 200 <= c < 300)
            kwargs: dict[str, Any] = {}
            if "model" in responses[success]:
                kwargs["response_model"] = responses[success]["model"]
            else:
                kwargs["response_class"] = Response
            app.add_api_route(
                path,
                _make_handler(op, params),
                methods=[method.upper()],
                operation_id=op["operationId"],
                tags=op.get("tags"),
                summary=op.get("summary"),
                description=op.get("description"),
                status_code=success,
                responses={c: r for c, r in responses.items() if c != success},
                openapi_extra={k: op[k] for k in ("x-story", "x-roles") if k in op},
                **kwargs,
            )
