"""ADU-02 arms 3, 4, 5, 7: the served contract against contracts/openapi.json; auth on every operation; every
x-synthetic example validates against the schemas; the composition root binds an implementation of each
port (the Null until its provider lands) and the clock."""

from __future__ import annotations

import json
import sys
from datetime import datetime
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "tests"))

from support.doubles import FakeMemberDirectory, FixedClock  # noqa: E402

from app import ports  # noqa: E402
from app.api import contract_stubs  # noqa: E402
from app.main import create_app  # noqa: E402
from app.scheduling.null_port import NullSchedulingPort  # noqa: E402
from app.swaps.null_port import NullSwapsPort  # noqa: E402

CONTRACT = json.loads((ROOT / "contracts" / "openapi.json").read_text(encoding="utf-8"))
METHODS = ("get", "post", "put", "patch", "delete")


def contract_ops() -> dict[tuple[str, str], dict]:
    return {(m, p): op for p, ops in CONTRACT["paths"].items() for m, op in ops.items() if m in METHODS}


def served_ops(doc: dict) -> dict[tuple[str, str], dict]:
    return {(m, p): op for p, ops in doc["paths"].items() for m, op in ops.items() if m in METHODS}


def test_every_contract_operation_is_served_with_the_same_identity_and_nothing_else(tmp_path: Path) -> None:
    doc = create_app(workspace=tmp_path).openapi()
    want, have = contract_ops(), served_ops(doc)
    assert set(have) == set(want)
    for key, op in want.items():
        got = have[key]
        assert got["operationId"] == op["operationId"], key
        assert set(got["responses"]) == set(op["responses"]), (
            key,
            set(got["responses"]) ^ set(op["responses"]),
        )
        assert got.get("x-roles") == op.get("x-roles") and got.get("x-story") == op.get("x-story"), key
        assert got.get("tags") == op.get("tags"), key
        assert "501" not in got["responses"]  # the placeholder is outside the contract
    assert not {"HTTPValidationError", "ValidationError"} & set(doc["components"]["schemas"])


def test_every_operation_except_sign_in_answers_401_without_a_token_and_501_not_built_with_one(
    tmp_path: Path,
) -> None:
    directory = FakeMemberDirectory()  # member 1 with token tok_1, the caller the 501 loop needs (Q-07)
    directory.add(1, "Member 1", "member", token="tok_1")
    client = TestClient(create_app(workspace=tmp_path, member_directory=directory))
    for (method, path), op in contract_ops().items():
        url = contract_stubs.example_path(path)
        body = contract_stubs.example_body(op)
        r = client.request(method.upper(), url, json=body)
        if op["operationId"] == "identity.sign_in":
            assert r.status_code == 501 and r.json()["reason"] == "not_built", op["operationId"]
            continue
        assert r.status_code == 401 and r.json()["reason"] == "unauthenticated", (op["operationId"], r.text)
        r = client.request(method.upper(), url, json=body, headers={"Authorization": "Bearer tok_1"})
        assert r.status_code == 501 and r.json()["reason"] == "not_built", (op["operationId"], r.text)
        bad = client.request(method.upper(), url, json=body, headers={"Authorization": "Bearer garbage"})
        assert bad.status_code == 401


def test_every_synthetic_example_validates_against_its_schema() -> None:
    checked = 0
    for (_m, _p), op in contract_ops().items():
        body = op.get("requestBody", {}).get("content", {}).get("application/json")
        if body:
            for name, ex in body.get("examples", {}).items():
                assert ex.get("x-synthetic") is True, (op["operationId"], name)
                contract_stubs.validate_example(body["schema"], ex["value"])
                checked += 1
        for code, resp in op["responses"].items():
            resp = contract_stubs.resolve(resp)
            content = resp.get("content", {}).get("application/json")
            if not content:
                continue
            for name, ex in content.get("examples", {}).items():
                assert ex.get("x-synthetic") is True, (op["operationId"], code, name)
                contract_stubs.validate_example(content["schema"], ex["value"])
                checked += 1
    assert checked >= 60


def test_an_example_that_breaks_its_schema_is_caught() -> None:
    with pytest.raises(Exception):
        contract_stubs.validate_example({"$ref": "#/components/schemas/Member"}, {"id": "x"})


def test_the_composition_root_binds_an_implementation_per_port_and_an_injectable_clock(
    tmp_path: Path,
) -> None:
    app = create_app(workspace=tmp_path)
    p = app.state.ports
    assert isinstance(p.member_directory, ports.MemberDirectory)
    assert isinstance(p.scheduling, NullSchedulingPort)
    assert isinstance(p.swaps, NullSwapsPort) and isinstance(p.notifier, ports.Notifier)
    assert isinstance(p.clock, ports.SystemClock)
    fixed = FixedClock(datetime(2026, 11, 5, 9))
    app2 = create_app(workspace=tmp_path, clock=fixed)
    assert app2.state.ports.clock.now() == datetime(2026, 11, 5, 9)
    for proto, obj in (
        (ports.MemberDirectory, p.member_directory),
        (ports.SchedulingPort, p.scheduling),
        (ports.SwapsPort, p.swaps),
        (ports.Notifier, p.notifier),
        (ports.Clock, p.clock),
    ):
        assert isinstance(obj, proto)


def test_one_session_per_request_shared_by_the_request(tmp_path: Path) -> None:
    app = create_app(workspace=tmp_path)
    seen: list[int] = []

    @app.get("/__probe__")
    def probe(
        a=contract_stubs.SESSION_DEP, b=contract_stubs.SESSION_DEP
    ) -> dict:  # two dependents, one session
        seen.append(id(a))
        return {"same": a is b}

    client = TestClient(app)
    assert client.get("/__probe__").json() == {"same": True}
    assert client.get("/__probe__").json() == {"same": True}
    assert len(seen) == 2 and (tmp_path / "rota.sqlite").exists()
