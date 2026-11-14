"""The composition root (ADU-02, layer 6): binds an implementation of each port — the Null until its provider
lands — and the clock, registers the contract's operations, and serves the contract document the golden
pins."""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path as FsPath
from typing import Any

from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.openapi.utils import get_openapi

from app.api import contract_stubs
from app.api.deps import ProblemError, problem_response
from app.identity.service import IdentityService, SecretsSource
from app.notifications.null_notifier import NullNotifier
from app.ports import Clock, MemberDirectory, Notifier, SchedulingPort, SwapsPort, SystemClock
from app.scheduling.null_port import NullSchedulingPort
from app.swaps.null_port import NullSwapsPort

CONTRACT = contract_stubs.CONTRACT


@dataclass
class Ports:
    member_directory: MemberDirectory
    scheduling: SchedulingPort
    swaps: SwapsPort
    notifier: Notifier
    clock: Clock


def create_app(
    workspace: FsPath | str | None = None,
    clock: Clock | None = None,
    *,
    member_directory: MemberDirectory | None = None,
    scheduling: SchedulingPort | None = None,
    swaps: SwapsPort | None = None,
    notifier: Notifier | None = None,
) -> FastAPI:
    info = CONTRACT["info"]
    app = FastAPI(
        title=info["title"],
        version=info["version"],
        description=info["description"],
        openapi_tags=CONTRACT.get("tags"),
    )
    app.state.ports = Ports(
        # ADU-03: the identity service reads these bindings at call time (D-15); its tokens and salts come
        # from the standard library's secrets (D-16)
        member_directory=member_directory or IdentityService(lambda: app.state.ports, SecretsSource()),
        scheduling=scheduling or NullSchedulingPort(),  # replaced by ADU-05
        swaps=swaps or NullSwapsPort(),  # replaced by ADU-07
        notifier=notifier or NullNotifier(),  # replaced by ADU-09
        clock=clock or SystemClock(),
    )
    app.state.workspace = FsPath(workspace or os.environ.get("ROTA_WORKSPACE", ".rota"))
    app.state.engine = None

    @app.exception_handler(ProblemError)
    async def _problem(_request: Request, exc: ProblemError):
        return problem_response(exc.status, exc.reason, exc.title, exc.detail, **exc.extra)

    @app.exception_handler(RequestValidationError)
    async def _invalid_request(_request: Request, exc: RequestValidationError):
        return problem_response(
            422, "invalid_request", "Request not understood", "The body does not match the schema."
        )

    @app.exception_handler(contract_stubs.NotBuilt)
    async def _not_built(_request: Request, exc: contract_stubs.NotBuilt):
        return problem_response(
            501, "not_built", "Not built", f"{exc.operation_id} is served by a later unit."
        )

    contract_stubs.register(app)

    def openapi() -> dict[str, Any]:
        if app.openapi_schema:
            return app.openapi_schema
        doc = get_openapi(
            title=app.title,
            version=app.version,
            description=app.description,
            routes=app.routes,
            tags=app.openapi_tags,
        )
        for path, ops in doc["paths"].items():
            declared = CONTRACT["paths"].get(path, {})
            for method, op in ops.items():
                keep = set(declared.get(method, {}).get("responses", {}))
                op["responses"] = {c: r for c, r in op["responses"].items() if c in keep}
        for name in ("HTTPValidationError", "ValidationError"):
            doc.get("components", {}).get("schemas", {}).pop(name, None)
        # the contract is the source of every property's metadata; pydantic drops the title of a $ref
        # field and a null example, so the served document takes them back from the contract
        for name, schema in doc.get("components", {}).get("schemas", {}).items():
            declared = CONTRACT["components"]["schemas"].get(name, {}).get("properties", {})
            for prop, spec in schema.get("properties", {}).items():
                for key in ("title", "description", "example", "x-when-to-use", "x-values"):
                    if key in declared.get(prop, {}) and key not in spec:
                        spec[key] = declared[prop][key]
        doc["servers"] = CONTRACT.get("servers", [])
        app.openapi_schema = doc
        return doc

    app.openapi = openapi  # type: ignore[method-assign]
    return app
