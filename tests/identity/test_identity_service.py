"""ADU-03 (Identity service), criteria-first: the seven acceptance arms of the ADU-PLAN.md entry.

Arm -> tests (each name is a test function below; [n] = its parametrised cases):
  arm 1, retires MK-04
    test_arm1_create_app_binds_the_identity_service_as_the_member_directory
    test_arm1_the_null_directory_module_no_longer_exists
    test_arm1_no_module_under_src_or_tests_imports_the_null_directory
    test_arm1_the_import_scan_finds_every_import_form_and_ignores_a_string [11]  (the scan's twin)
    test_arm1_a_route_of_the_tests_own_takes_its_caller_from_the_requests_current_session
    test_arm1_with_no_session_current_each_method_raises_no_current_session [12]
    test_arm1_the_no_session_cases_cover_every_directory_method_and_service_operation
    (not repeated here, as the arm says: the contract unit's tests and tests/test_nulls.py pass after the
    granted edits; the gate checks that)
  arm 2, seed_admin
    test_arm2_seed_admin_on_an_empty_team_creates_one_active_admin_and_emits_nothing
    test_arm2_seed_admin_stores_a_salted_sha256_that_verifies_the_passcode_and_nothing_else
    test_arm2_seed_admin_on_a_non_empty_team_raises_team_not_empty_and_changes_nothing
  arm 3, add_member
    test_arm3_add_member_creates_an_active_member_with_the_role_and_emits_member_added [3]
    test_arm3_add_member_refuses_duplicate_email_compared_case_insensitively [3]
    test_arm3_add_member_refuses_invalid_role [3]
    test_arm3_add_member_refuses_forbidden_to_a_caller_who_is_not_an_admin [2]
    test_arm3_add_member_refusal_order_is_forbidden_then_duplicate_email_then_invalid_role [4]
  arm 4, change_role
    test_arm4_change_role_changes_the_role_and_emits_role_changed [3]
    test_arm4_change_role_to_the_same_role_is_a_no_op_answering_the_unchanged_member [2]
    test_arm4_an_inactive_members_role_may_change_and_nobody_is_notified
    test_arm4_change_role_refuses_last_admin_for_the_only_active_admin [3]
    test_arm4_change_role_moves_an_admin_while_another_active_admin_remains  (twin of last_admin)
    test_arm4_change_role_refuses_invalid_role [3]
    test_arm4_change_role_refuses_not_found_for_an_unknown_id
    test_arm4_change_role_refuses_forbidden_to_a_caller_who_is_not_an_admin [2]
    test_arm4_change_role_refusal_order_is_forbidden_then_not_found_then_invalid_role [4]
  arm 5, deactivate
    test_arm5_deactivate_sets_active_false_keeps_the_row_and_emits_member_deactivated
    test_arm5_deactivate_refuses_future_assignments_when_the_scheduling_port_answers_true
    test_arm5_future_assignments_is_asked_of_the_target_not_of_another_member  (twin of future_assignments)
    test_arm5_deactivate_refuses_last_admin_for_the_only_active_admin [2]
    test_arm5_deactivate_takes_an_admin_out_while_another_active_admin_remains  (twin of last_admin)
    test_arm5_deactivate_refuses_member_inactive_on_a_repeat_and_emits_nothing
    test_arm5_deactivate_refuses_not_found_for_an_unknown_id
    test_arm5_deactivate_refuses_forbidden_to_a_caller_who_is_not_an_admin [2]
    test_arm5_deactivate_refusal_order_follows_the_buckets_and_the_storys_state_order [5]
  arm 6, sign_in
    test_arm6_sign_in_matches_the_email_case_insensitively_and_issues_the_sources_token [3]
    test_arm6_sign_in_matches_a_mixed_case_stored_email_typed_in_lower_case
    test_arm6_a_second_sign_in_replaces_the_earlier_token
    test_arm6_caller_for_token_is_none_for_an_unknown_token
    test_arm6_caller_for_token_is_none_for_an_inactive_members_previously_issued_token [2]
    test_arm6_sign_in_refuses_invalid_credentials_and_changes_nothing [5]
    test_arm6_credentials_are_verified_before_the_active_check [3]
  arm 7, MemberDirectory and list_members
    test_arm7_caller_for_token_resolves_a_signed_in_member_to_their_caller [3]
    test_arm7_is_active_answers_true_false_or_none_for_an_unknown_id
    test_arm7_role_of_answers_the_role_or_raises_member_not_found_for_an_unknown_id
    test_arm7_name_of_answers_the_name_or_raises_member_not_found_for_an_unknown_id
    test_arm7_active_member_ids_excludes_the_inactive
    test_arm7_decider_ids_are_the_active_admins_and_planners
    test_arm7_list_members_answers_every_member_by_name_case_insensitively_then_id [3]
    test_arm7_list_members_rows_carry_id_name_role_active_and_never_email_passcode_or_token
  design/INTERFACES.md (IdentityService value types; used by arms 3, 6, 7)
    test_interfaces_the_identity_values_are_frozen_dataclasses_with_their_declared_fields [3]
  the entry's amends (assertions of amended modules, not arms)
    test_amend_db_current_session_raises_no_current_session_outside_a_unit_of_work
    test_amend_db_unit_of_work_makes_its_session_current_commits_on_return_and_closes
    test_amend_db_unit_of_work_rolls_back_on_raise_and_restores_the_previous_state
    test_amend_db_use_session_and_unit_of_work_nest_and_restore_the_previous_session
    test_amend_ports_refused_carries_its_reason_and_the_extra_fields_a_story_names

SYNTHETIC: every value in this module is invented for the test: the names (Ada, Pia, Mo, Abe, Bo, Zed, bea,
al, Al, Pat, Uma), the @example.test emails, the passcodes of the form pass-<local part>-<n>, and the tokens
and salts of SyntheticSource (D-16), whose counter is the generator that reproduces them. No real data.

How the tests reach the service (design/INTERFACES.md, Domain services): each call runs in its own
`with db.unit_of_work(engine):` and every read-back in a second one; a refusal is asserted with
pytest.raises(Refused) around the block, which leaves it rolled back, and only `.reason` is asserted. The
bindings are FixedClock, FakeSchedulingPort and SpyNotifier from tests/support/doubles.py. An inactive member
is arranged through the data model (World.set_active), so only the row's active flag changes; deactivate
itself is exercised by arm 5 and by the by-service case of arm 6.
"""

from __future__ import annotations

import ast
import json
from collections.abc import Callable
from dataclasses import FrozenInstanceError, astuple, dataclass, fields, is_dataclass
from datetime import datetime
from pathlib import Path
from types import SimpleNamespace
from typing import Any, NamedTuple

import pytest
from fastapi import Depends
from fastapi.testclient import TestClient
from sqlalchemy import Engine, inspect, select
from support.doubles import FakeSchedulingPort, FixedClock, SpyNotifier

from app import db, models, ports
from app.api.deps import get_session, require_caller
from app.identity.service import IdentityService, MemberSummary, MemberValue, SignInValue
from app.main import create_app
from app.ports import Refused

ROOT = Path(__file__).resolve().parents[2]
NOW = datetime(2026, 11, 16, 9)  # SYNTHETIC: the FixedClock's instant, a Monday morning
UNKNOWN_ID = 9_999  # names no member in any arrangement of this module
PROBE_PATH = "/__adu03_probe__"  # a path the contract does not declare (asserted in the route test)
NULL_DIRECTORY = "app.identity.null_directory"


# ---------------------------------------------------------------------------------------------------- harness
class SyntheticSource:
    """SYNTHETIC token and salt source (D-16). A counter is its generator, so every run reproduces the same
    values; each call answers a distinct value (the token column is unique). It records what it handed out,
    so a test can tell that the service stored the source's value and not one of its own."""

    def __init__(self) -> None:
        self.tokens: list[str] = []
        self.salts: list[str] = []

    def token(self) -> str:
        self.tokens.append(f"tok-{len(self.tokens) + 1:03d}")
        return self.tokens[-1]

    def salt(self) -> str:
        self.salts.append(f"salt{len(self.salts) + 1:04d}")
        return self.salts[-1]


class Row(NamedTuple):
    """A member row read back through the data model (models.Member) in its own unit of work."""

    id: int
    name: str
    email: str
    role: str
    active: bool
    passcode_hash: str
    token: str | None


def _rows(engine: Engine) -> list[Row]:
    with db.unit_of_work(engine) as session:
        members = session.scalars(select(models.Member).order_by(models.Member.id)).all()
        return [Row(m.id, m.name, m.email, m.role, m.active, m.passcode_hash, m.token) for m in members]


def _caller(member_id: int, name: str, role: str) -> ports.Caller:
    return ports.Caller(member_id=member_id, name=name, role=role, active=True)


def _salt_of(passcode_hash: str) -> str:
    return passcode_hash.split("$", 1)[0]


def _passcode(email: str) -> str:
    return f"pass-{email.split('@')[0]}-1"


@dataclass
class World:
    engine: Engine
    clock: FixedClock
    scheduling: FakeSchedulingPort
    spy: SpyNotifier
    source: SyntheticSource
    service: IdentityService

    def run(self, operation: Callable[..., Any], *args: Any) -> Any:
        """One unit of work around one call (INTERFACES.md:93): commits on return, rolls back on raise."""
        with db.unit_of_work(self.engine):
            return operation(*args)

    def refusal(self, operation: Callable[..., Any], *args: Any) -> str:
        """The reason of the Refused the call raises; pytest.raises sits around the unit of work, which
        therefore rolls back."""
        with pytest.raises(Refused) as refused:
            self.run(operation, *args)
        return refused.value.reason

    def rows(self) -> list[Row]:
        return _rows(self.engine)

    def row(self, member_id: int) -> Row:
        (found,) = [r for r in self.rows() if r.id == member_id]
        return found

    def value(self, member_id: int) -> MemberValue:
        r = self.row(member_id)
        return MemberValue(id=r.id, name=r.name, email=r.email, role=r.role, active=r.active)

    def add(self, caller: ports.Caller, name: str, email: str, role: str, passcode: str) -> MemberValue:
        return self.run(self.service.add_member, caller, name, email, role, passcode)

    def set_active(self, member_id: int, active: bool) -> None:
        """Arrangement through the data model (ADU-01), not the service: only the row's active flag changes,
        so its role and its token stay as they were."""
        with db.unit_of_work(self.engine) as session:
            session.get(models.Member, member_id).active = active


@dataclass(frozen=True)
class Team:
    admin: ports.Caller
    planner: ports.Caller
    member: ports.Caller


@pytest.fixture
def world(tmp_path: Path):
    clock, scheduling, spy, source = FixedClock(NOW), FakeSchedulingPort(), SpyNotifier(), SyntheticSource()
    bindings = SimpleNamespace(clock=clock, scheduling=scheduling, notifier=spy)
    engine = db.engine_for(tmp_path)
    yield World(engine, clock, scheduling, spy, source, IdentityService(lambda: bindings, source))
    engine.dispose()


@pytest.fixture
def admin(world: World) -> ports.Caller:
    """SYNTHETIC: Ada, the seeded admin, alone on the team."""
    admin_id = world.run(world.service.seed_admin, "Ada", "ada@example.test", "pass-ada-1")
    return _caller(admin_id, "Ada", "admin")


@pytest.fixture
def team(world: World, admin: ports.Caller) -> Team:
    """SYNTHETIC: Ada (admin, seeded), Pia (planner) and Mo (member), all active; the spy starts empty."""
    pia = world.add(admin, "Pia", "pia@example.test", "planner", "pass-pia-1")
    mo = world.add(admin, "Mo", "mo@example.test", "member", "pass-mo-1")
    world.spy.sent.clear()
    return Team(admin=admin, planner=_caller(pia.id, "Pia", "planner"), member=_caller(mo.id, "Mo", "member"))


def _target(team: Team, key: str) -> int:
    return UNKNOWN_ID if key == "unknown" else getattr(team, key).member_id


# ---------------------------------------------------------------------------------------------------- arm 1
def test_arm1_create_app_binds_the_identity_service_as_the_member_directory(tmp_path: Path) -> None:
    directory = create_app(workspace=tmp_path).state.ports.member_directory
    assert isinstance(directory, IdentityService)
    assert isinstance(directory, ports.MemberDirectory)


def test_arm1_the_null_directory_module_no_longer_exists() -> None:
    assert not (ROOT / "src" / "app" / "identity" / "null_directory.py").exists()


def _imported_names(source: str, module: tuple[str, ...]) -> set[str]:
    """Every dotted name an Import or ImportFrom node of `source` can bind; a relative import is resolved
    against `module`, the importing module's dotted parts. A string literal is never an import node, so it
    cannot match."""
    names: set[str] = set()
    for node in ast.walk(ast.parse(source)):
        if isinstance(node, ast.Import):
            names.update(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            base = list(module[: len(module) - node.level]) if node.level else []
            full = ".".join([*base, *(node.module.split(".") if node.module else [])])
            names.add(full)
            names.update(f"{full}.{alias.name}" for alias in node.names)
    return names


def _imports_null_directory(source: str, module: tuple[str, ...]) -> bool:
    names = _imported_names(source, module)
    return any(n == NULL_DIRECTORY or n.startswith(NULL_DIRECTORY + ".") for n in names)


def _module_parts(path: Path) -> tuple[str, ...]:
    for top in (ROOT / "src", ROOT / "tests"):
        if path.is_relative_to(top):
            return path.relative_to(top).with_suffix("").parts
    raise AssertionError(f"{path} is under neither src/ nor tests/")


def test_arm1_no_module_under_src_or_tests_imports_the_null_directory() -> None:
    files = sorted(p for top in ("src", "tests") for p in (ROOT / top).rglob("*.py"))
    assert Path(__file__).resolve() in files, "the scan must cover tests/identity"
    offenders = [
        p.relative_to(ROOT).as_posix()
        for p in files
        if _imports_null_directory(p.read_text(encoding="utf-8"), _module_parts(p))
    ]
    assert offenders == []


MAIN = ("app", "main")
SERVICE = ("app", "identity", "service")


@pytest.mark.parametrize(
    "source, module, found",
    [
        pytest.param("from app.identity.null_directory import NullDirectory\n", MAIN, True, id="from"),
        pytest.param("import app.identity.null_directory\n", MAIN, True, id="import"),
        pytest.param("import app.identity.null_directory as nd\n", MAIN, True, id="import-as"),
        pytest.param("from app.identity import null_directory\n", ("test_x",), True, id="from-package"),
        pytest.param("from . import null_directory\n", SERVICE, True, id="relative"),
        pytest.param("from .null_directory import NullDirectory\n", SERVICE, True, id="relative-from"),
        pytest.param(
            "from ..identity.null_directory import NullDirectory\n", ("app", "api", "deps"), True, id="up-two"
        ),
        pytest.param(
            "TEXT = 'from app.identity.null_directory import NullDirectory'\n", MAIN, False, id="string"
        ),
        pytest.param("from app.identity.service import IdentityService\n", MAIN, False, id="sibling"),
        pytest.param("from app.identity import service\n", MAIN, False, id="sibling-from-package"),
        pytest.param("import app.identity\n", MAIN, False, id="the-package-alone"),
    ],
)
def test_arm1_the_import_scan_finds_every_import_form_and_ignores_a_string(
    source: str, module: tuple[str, ...], found: bool
) -> None:
    """The falsification twin of the scan above: the same helper reports each import form of the retired
    module and none of a string literal or a sibling, so an empty offender list carries information."""
    assert _imports_null_directory(source, module) is found


def test_arm1_a_route_of_the_tests_own_takes_its_caller_from_the_requests_current_session(
    tmp_path: Path,
) -> None:
    """The identity service bound by create_app (its source the product's random one) seeds and signs in; a
    GET route this test registers at an undeclared path resolves its caller through deps.require_caller, so
    the token is read in the request's current session. No request goes to a contract operation and nothing
    is imported from app.api.contract_stubs."""
    contract_paths = json.loads((ROOT / "contracts" / "openapi.json").read_text(encoding="utf-8"))["paths"]
    assert PROBE_PATH not in contract_paths
    web = create_app(workspace=tmp_path)
    service = web.state.ports.member_directory
    engine = db.engine_for(tmp_path)
    with db.unit_of_work(engine):
        admin_id = service.seed_admin("Ada", "ada@example.test", "pass-ada-1")
    with db.unit_of_work(engine):
        token = service.sign_in("ada@example.test", "pass-ada-1").token
    engine.dispose()

    @web.get(PROBE_PATH, response_model=None)
    def probe(caller: ports.Caller = Depends(require_caller), session=Depends(get_session)):
        return {"member_id": caller.member_id, "request_session_is_current": db.current_session() is session}

    with TestClient(web) as client:
        signed_in = client.get(PROBE_PATH, headers={"Authorization": f"Bearer {token}"})
        garbage = client.get(PROBE_PATH, headers={"Authorization": "Bearer garbage"})
    assert signed_in.status_code == 200
    assert signed_in.json() == {"member_id": admin_id, "request_session_is_current": True}
    assert garbage.status_code == 401
    assert garbage.json()["reason"] == "unauthenticated"


#: an admin Caller for the operations that take one; with it every argument below passes each check that needs
#: no store (an admin caller, a known role, a non-empty passcode), so a call can answer only by reading the
#: current session, and a method that refused early or opened a session of its own would not raise
#: NoCurrentSession
NO_SESSION_ADMIN = _caller(1, "Ada", "admin")
NO_SESSION_CALLS: dict[str, Callable[[IdentityService], object]] = {
    "MemberDirectory.caller_for_token": lambda s: s.caller_for_token("tok-001"),
    "MemberDirectory.is_active": lambda s: s.is_active(1),
    "MemberDirectory.role_of": lambda s: s.role_of(1),
    "MemberDirectory.name_of": lambda s: s.name_of(1),
    "MemberDirectory.active_member_ids": lambda s: s.active_member_ids(),
    "MemberDirectory.decider_ids": lambda s: s.decider_ids(),
    "IdentityService.seed_admin": lambda s: s.seed_admin("Ada", "ada@example.test", "pass-ada-1"),
    "IdentityService.add_member": lambda s: s.add_member(
        NO_SESSION_ADMIN, "Mo", "mo@example.test", "member", "pass-mo-1"
    ),
    "IdentityService.change_role": lambda s: s.change_role(NO_SESSION_ADMIN, 2, "planner"),
    "IdentityService.deactivate": lambda s: s.deactivate(NO_SESSION_ADMIN, 2),
    "IdentityService.sign_in": lambda s: s.sign_in("ada@example.test", "pass-ada-1"),
    "IdentityService.list_members": lambda s: s.list_members(NO_SESSION_ADMIN),
}
SERVICE_OPERATIONS = ("seed_admin", "add_member", "change_role", "deactivate", "sign_in", "list_members")


@pytest.mark.parametrize("call", list(NO_SESSION_CALLS.values()), ids=list(NO_SESSION_CALLS))
def test_arm1_with_no_session_current_each_method_raises_no_current_session(
    world: World, tmp_path: Path, monkeypatch: pytest.MonkeyPatch, call: Callable[[IdentityService], object]
) -> None:
    """Called outside any unit of work, the method lets db.NoCurrentSession propagate. The working directory
    is the test's own, so a method that quietly opened a session on a default workspace writes nothing into
    the repository."""
    monkeypatch.chdir(tmp_path)
    monkeypatch.delenv("ROTA_WORKSPACE", raising=False)
    with pytest.raises(db.NoCurrentSession):
        call(world.service)


def test_arm1_the_no_session_cases_cover_every_directory_method_and_service_operation() -> None:
    """Keeps the 12 cases above complete: it fails when ports.MemberDirectory gains a method the table lacks,
    or when IdentityService lacks a method the table calls."""
    directory = {name for name in vars(ports.MemberDirectory) if not name.startswith("_")}
    assert {k.split(".")[1] for k in NO_SESSION_CALLS if k.startswith("MemberDirectory.")} == directory
    assert {k.split(".")[1] for k in NO_SESSION_CALLS if k.startswith("IdentityService.")} == set(
        SERVICE_OPERATIONS
    )
    for name in sorted(directory | set(SERVICE_OPERATIONS)):
        assert callable(getattr(IdentityService, name, None)), name


# ---------------------------------------------------------------------------------------------------- arm 2
def test_arm2_seed_admin_on_an_empty_team_creates_one_active_admin_and_emits_nothing(world: World) -> None:
    assert world.rows() == []
    new_id = world.run(world.service.seed_admin, "Ada", "ada@example.test", "pass-ada-1")
    assert isinstance(new_id, int)
    assert [(r.id, r.name, r.email, r.role, r.active) for r in world.rows()] == [
        (new_id, "Ada", "ada@example.test", "admin", True)
    ]
    assert world.spy.sent == []


def test_arm2_seed_admin_stores_a_salted_sha256_that_verifies_the_passcode_and_nothing_else(
    world: World,
) -> None:
    """Stored as models.hash_passcode(passcode, <a salt the source gave>), never the plain passcode; sign_in,
    which recomputes the hash with the stored salt, accepts the passcode and refuses a near miss."""
    new_id = world.run(world.service.seed_admin, "Ada", "ada@example.test", "pass-ada-1")
    stored = world.row(new_id).passcode_hash
    assert stored != "pass-ada-1"
    assert "pass-ada-1" not in stored
    salt = _salt_of(stored)
    assert salt in world.source.salts
    assert stored == models.hash_passcode("pass-ada-1", salt)
    assert world.run(world.service.sign_in, "ada@example.test", "pass-ada-1").member.id == new_id
    for near_miss in ("pass-ada-2", "PASS-ADA-1", "pass-ada-1 "):
        assert world.refusal(world.service.sign_in, "ada@example.test", near_miss) == "invalid_credentials"


def test_arm2_seed_admin_on_a_non_empty_team_raises_team_not_empty_and_changes_nothing(world: World) -> None:
    world.run(world.service.seed_admin, "Ada", "ada@example.test", "pass-ada-1")
    before = world.rows()
    reason = world.refusal(world.service.seed_admin, "Abe", "abe@example.test", "pass-abe-1")
    assert reason == "team_not_empty"
    assert world.rows() == before
    assert len(world.rows()) == 1
    assert world.spy.sent == []


# ---------------------------------------------------------------------------------------------------- arm 3
@pytest.mark.parametrize("role", ["admin", "planner", "member"])
def test_arm3_add_member_creates_an_active_member_with_the_role_and_emits_member_added(
    world: World, admin: ports.Caller, role: str
) -> None:
    added = world.add(admin, "Mo", "mo@example.test", role, "pass-mo-1")
    assert added == MemberValue(id=added.id, name="Mo", email="mo@example.test", role=role, active=True)
    assert added.id != admin.member_id
    assert len(world.rows()) == 2
    row = world.row(added.id)
    assert (row.name, row.email, row.role, row.active) == ("Mo", "mo@example.test", role, True)
    assert _salt_of(row.passcode_hash) in world.source.salts
    assert row.passcode_hash == models.hash_passcode("pass-mo-1", _salt_of(row.passcode_hash))
    assert world.spy.sent == [ports.MemberAdded(member_id=added.id, role=role)]


@pytest.mark.parametrize(
    "email, mo_inactive",
    [
        pytest.param("mo@example.test", False, id="same-case"),
        pytest.param("MO@Example.test", False, id="other-case"),
        pytest.param("Mo@example.TEST", True, id="of-an-inactive-member"),
    ],
)
def test_arm3_add_member_refuses_duplicate_email_compared_case_insensitively(
    world: World, team: Team, email: str, mo_inactive: bool
) -> None:
    if mo_inactive:
        world.set_active(team.member.member_id, False)
    before = world.rows()
    assert world.refusal(world.service.add_member, team.admin, "Bo", email, "member", "pass-bo-1") == (
        "duplicate_email"
    )
    assert world.rows() == before
    assert world.spy.sent == []


@pytest.mark.parametrize("role", ["owner", "", None])
def test_arm3_add_member_refuses_invalid_role(world: World, team: Team, role: str | None) -> None:
    before = world.rows()
    reason = world.refusal(world.service.add_member, team.admin, "Bo", "bo@example.test", role, "pass-bo-1")
    assert reason == "invalid_role"
    assert world.rows() == before
    assert world.spy.sent == []


@pytest.mark.parametrize("caller_key", ["planner", "member"])
def test_arm3_add_member_refuses_forbidden_to_a_caller_who_is_not_an_admin(
    world: World, team: Team, caller_key: str
) -> None:
    caller = getattr(team, caller_key)
    before = world.rows()
    reason = world.refusal(world.service.add_member, caller, "Bo", "bo@example.test", "member", "pass-bo-1")
    assert reason == "forbidden"
    assert world.rows() == before
    assert world.spy.sent == []


@pytest.mark.parametrize(
    "caller_key, email, role, reason",
    [
        pytest.param("planner", "mo@example.test", "owner", "forbidden", id="forbidden-before-both"),
        pytest.param("member", "MO@example.test", None, "forbidden", id="forbidden-before-both-missing-role"),
        pytest.param("admin", "MO@example.test", "owner", "duplicate_email", id="state-before-validation"),
        pytest.param("admin", "mo@example.test", None, "duplicate_email", id="state-before-missing-role"),
    ],
)
def test_arm3_add_member_refusal_order_is_forbidden_then_duplicate_email_then_invalid_role(
    world: World, team: Team, caller_key: str, email: str, role: str | None, reason: str
) -> None:
    before = world.rows()
    caller = getattr(team, caller_key)
    assert world.refusal(world.service.add_member, caller, "Bo", email, role, "pass-bo-1") == reason
    assert world.rows() == before
    assert world.spy.sent == []


# ---------------------------------------------------------------------------------------------------- arm 4
@pytest.mark.parametrize(
    "target_key, role", [("member", "planner"), ("member", "admin"), ("planner", "member")]
)
def test_arm4_change_role_changes_the_role_and_emits_role_changed(
    world: World, team: Team, target_key: str, role: str
) -> None:
    target = getattr(team, target_key)
    before = world.row(target.member_id)
    changed = world.run(world.service.change_role, team.admin, target.member_id, role)
    assert changed == MemberValue(
        id=target.member_id, name=before.name, email=before.email, role=role, active=True
    )
    after = world.row(target.member_id)
    assert (after.role, after.active) == (role, True)
    assert world.spy.sent == [ports.RoleChanged(member_id=target.member_id, role=role)]


@pytest.mark.parametrize("target_key", ["member", "admin"], ids=["a-member", "the-only-admin-stays-admin"])
def test_arm4_change_role_to_the_same_role_is_a_no_op_answering_the_unchanged_member(
    world: World, team: Team, target_key: str
) -> None:
    target = getattr(team, target_key)
    unchanged = world.value(target.member_id)
    before = world.rows()
    assert world.run(world.service.change_role, team.admin, target.member_id, target.role) == unchanged
    assert world.rows() == before
    assert world.spy.sent == []


def test_arm4_an_inactive_members_role_may_change_and_nobody_is_notified(world: World, team: Team) -> None:
    mo = team.member.member_id
    world.set_active(mo, False)
    changed = world.run(world.service.change_role, team.admin, mo, "planner")
    assert changed == MemberValue(id=mo, name="Mo", email="mo@example.test", role="planner", active=False)
    row = world.row(mo)
    assert (row.role, row.active) == ("planner", False)
    assert world.spy.sent == []


@pytest.mark.parametrize(
    "role, inactive_second_admin",
    [
        pytest.param("planner", False, id="to-planner"),
        pytest.param("member", False, id="to-member"),
        pytest.param("planner", True, id="an-inactive-second-admin-does-not-count"),
    ],
)
def test_arm4_change_role_refuses_last_admin_for_the_only_active_admin(
    world: World, team: Team, role: str, inactive_second_admin: bool
) -> None:
    if inactive_second_admin:
        abe = world.add(team.admin, "Abe", "abe@example.test", "admin", "pass-abe-1")
        world.set_active(abe.id, False)
        world.spy.sent.clear()
    before = world.rows()
    assert world.refusal(world.service.change_role, team.admin, team.admin.member_id, role) == "last_admin"
    assert world.rows() == before
    assert world.spy.sent == []


def test_arm4_change_role_moves_an_admin_while_another_active_admin_remains(world: World, team: Team) -> None:
    """The twin of last_admin: the refusal is about the team's last active admin, not about admins as such."""
    world.add(team.admin, "Abe", "abe@example.test", "admin", "pass-abe-1")
    world.spy.sent.clear()
    ada = team.admin.member_id
    assert world.run(world.service.change_role, team.admin, ada, "planner").role == "planner"
    assert world.row(ada).role == "planner"
    assert world.spy.sent == [ports.RoleChanged(member_id=ada, role="planner")]


@pytest.mark.parametrize("role", ["owner", "", None])
def test_arm4_change_role_refuses_invalid_role(world: World, team: Team, role: str | None) -> None:
    before = world.rows()
    assert world.refusal(world.service.change_role, team.admin, team.member.member_id, role) == "invalid_role"
    assert world.rows() == before
    assert world.spy.sent == []


def test_arm4_change_role_refuses_not_found_for_an_unknown_id(world: World, team: Team) -> None:
    before = world.rows()
    assert world.refusal(world.service.change_role, team.admin, UNKNOWN_ID, "planner") == "not_found"
    assert world.rows() == before
    assert world.spy.sent == []


@pytest.mark.parametrize("caller_key, target_key", [("planner", "member"), ("member", "planner")])
def test_arm4_change_role_refuses_forbidden_to_a_caller_who_is_not_an_admin(
    world: World, team: Team, caller_key: str, target_key: str
) -> None:
    before = world.rows()
    caller, target = getattr(team, caller_key), _target(team, target_key)
    assert world.refusal(world.service.change_role, caller, target, "admin") == "forbidden"
    assert world.rows() == before
    assert world.spy.sent == []


@pytest.mark.parametrize(
    "caller_key, role, reason",
    [
        pytest.param("planner", "owner", "forbidden", id="forbidden-before-not_found-and-invalid_role"),
        pytest.param("member", None, "forbidden", id="forbidden-before-not_found-and-a-missing-role"),
        pytest.param("admin", "owner", "not_found", id="not_found-before-invalid_role"),
        pytest.param("admin", None, "not_found", id="not_found-before-a-missing-role"),
    ],
)
def test_arm4_change_role_refusal_order_is_forbidden_then_not_found_then_invalid_role(
    world: World, team: Team, caller_key: str, role: str | None, reason: str
) -> None:
    before = world.rows()
    assert world.refusal(world.service.change_role, getattr(team, caller_key), UNKNOWN_ID, role) == reason
    assert world.rows() == before
    assert world.spy.sent == []


# ---------------------------------------------------------------------------------------------------- arm 5
def test_arm5_deactivate_sets_active_false_keeps_the_row_and_emits_member_deactivated(
    world: World, team: Team
) -> None:
    mo = team.member.member_id
    before = world.row(mo)
    answered = world.run(world.service.deactivate, team.admin, mo)
    assert world.spy.sent == [ports.MemberDeactivated(member_id=mo)]
    assert answered == MemberValue(id=mo, name="Mo", email="mo@example.test", role="member", active=False)
    after = world.row(mo)
    assert (after.name, after.email, after.role, after.active, after.passcode_hash) == (
        before.name,
        before.email,
        before.role,
        False,
        before.passcode_hash,
    )
    assert len(world.rows()) == 3
    assert MemberSummary(id=mo, name="Mo", role="member", active=False) in world.run(
        world.service.list_members, team.admin
    )
    assert world.run(world.service.is_active, mo) is False
    assert world.run(world.service.role_of, mo) == "member"
    assert world.run(world.service.name_of, mo) == "Mo"


def test_arm5_deactivate_refuses_future_assignments_when_the_scheduling_port_answers_true(
    world: World, team: Team
) -> None:
    mo = team.member.member_id
    world.scheduling.set_has_assignment_after(mo, True)
    before = world.rows()
    assert world.refusal(world.service.deactivate, team.admin, mo) == "future_assignments"
    assert world.rows() == before
    assert world.spy.sent == []


def test_arm5_future_assignments_is_asked_of_the_target_not_of_another_member(
    world: World, team: Team
) -> None:
    """The twin of future_assignments: another member's future assignment does not stop this deactivation."""
    mo = team.member.member_id
    world.scheduling.set_has_assignment_after(team.planner.member_id, True)
    assert world.run(world.service.deactivate, team.admin, mo).active is False
    assert world.spy.sent == [ports.MemberDeactivated(member_id=mo)]


@pytest.mark.parametrize(
    "inactive_second_admin", [False, True], ids=["alone", "an-inactive-second-admin-does-not-count"]
)
def test_arm5_deactivate_refuses_last_admin_for_the_only_active_admin(
    world: World, team: Team, inactive_second_admin: bool
) -> None:
    if inactive_second_admin:
        abe = world.add(team.admin, "Abe", "abe@example.test", "admin", "pass-abe-1")
        world.set_active(abe.id, False)
        world.spy.sent.clear()
    before = world.rows()
    assert world.refusal(world.service.deactivate, team.admin, team.admin.member_id) == "last_admin"
    assert world.rows() == before
    assert world.spy.sent == []


def test_arm5_deactivate_takes_an_admin_out_while_another_active_admin_remains(
    world: World, team: Team
) -> None:
    """The twin of last_admin: with a second active admin, the first may be deactivated."""
    abe = world.add(team.admin, "Abe", "abe@example.test", "admin", "pass-abe-1")
    world.spy.sent.clear()
    ada = team.admin.member_id
    assert world.run(world.service.deactivate, _caller(abe.id, "Abe", "admin"), ada).active is False
    assert world.row(ada).active is False
    assert world.spy.sent == [ports.MemberDeactivated(member_id=ada)]


def test_arm5_deactivate_refuses_member_inactive_on_a_repeat_and_emits_nothing(
    world: World, team: Team
) -> None:
    mo = team.member.member_id
    world.run(world.service.deactivate, team.admin, mo)
    world.spy.sent.clear()
    before = world.rows()
    assert world.refusal(world.service.deactivate, team.admin, mo) == "member_inactive"
    assert world.rows() == before
    assert world.spy.sent == []


def test_arm5_deactivate_refuses_not_found_for_an_unknown_id(world: World, team: Team) -> None:
    before = world.rows()
    assert world.refusal(world.service.deactivate, team.admin, UNKNOWN_ID) == "not_found"
    assert world.rows() == before
    assert world.spy.sent == []


@pytest.mark.parametrize("caller_key, target_key", [("planner", "member"), ("member", "planner")])
def test_arm5_deactivate_refuses_forbidden_to_a_caller_who_is_not_an_admin(
    world: World, team: Team, caller_key: str, target_key: str
) -> None:
    before = world.rows()
    caller, target = getattr(team, caller_key), _target(team, target_key)
    assert world.refusal(world.service.deactivate, caller, target) == "forbidden"
    assert world.rows() == before
    assert world.spy.sent == []


@pytest.mark.parametrize(
    "caller_key, target_key, future, target_inactive, reason",
    [
        pytest.param("planner", "unknown", False, False, "forbidden", id="forbidden-before-not_found"),
        pytest.param("planner", "member", True, True, "forbidden", id="forbidden-before-state"),
        pytest.param("admin", "unknown", True, False, "not_found", id="not_found-before-future_assignments"),
        pytest.param(
            "admin", "admin", True, False, "future_assignments", id="future_assignments-before-last_admin"
        ),
        pytest.param(
            "admin", "member", True, True, "future_assignments", id="future_assignments-before-inactive"
        ),
    ],
)
def test_arm5_deactivate_refusal_order_follows_the_buckets_and_the_storys_state_order(
    world: World,
    team: Team,
    caller_key: str,
    target_key: str,
    future: bool,
    target_inactive: bool,
    reason: str,
) -> None:
    """forbidden -> not_found -> state, and within state US-identity-003's order: future_assignments ->
    last_admin -> member_inactive."""
    target = _target(team, target_key)
    if target_inactive:
        world.set_active(target, False)
    world.scheduling.set_has_assignment_after(target, future)
    before = world.rows()
    assert world.refusal(world.service.deactivate, getattr(team, caller_key), target) == reason
    assert world.rows() == before
    assert world.spy.sent == []


# ---------------------------------------------------------------------------------------------------- arm 6
@pytest.mark.parametrize("typed", ["mo@example.test", "MO@EXAMPLE.TEST", "Mo@Example.Test"])
def test_arm6_sign_in_matches_the_email_case_insensitively_and_issues_the_sources_token(
    world: World, team: Team, typed: str
) -> None:
    mo = team.member.member_id
    signed = world.run(world.service.sign_in, typed, "pass-mo-1")
    assert isinstance(signed, SignInValue)
    assert signed.token in world.source.tokens
    assert signed.member == MemberValue(id=mo, name="Mo", email="mo@example.test", role="member", active=True)
    assert world.row(mo).token == signed.token
    assert world.run(world.service.caller_for_token, signed.token) == team.member
    assert world.spy.sent == []


def test_arm6_sign_in_matches_a_mixed_case_stored_email_typed_in_lower_case(world: World, team: Team) -> None:
    bea = world.add(team.admin, "Bea", "Bea@Example.test", "member", "pass-bea-1")
    signed = world.run(world.service.sign_in, "bea@example.test", "pass-bea-1")
    assert signed.member.id == bea.id
    assert world.run(world.service.caller_for_token, signed.token) == _caller(bea.id, "Bea", "member")


def test_arm6_a_second_sign_in_replaces_the_earlier_token(world: World, team: Team) -> None:
    first = world.run(world.service.sign_in, "mo@example.test", "pass-mo-1")
    second = world.run(world.service.sign_in, "mo@example.test", "pass-mo-1")
    assert first.token != second.token
    assert world.run(world.service.caller_for_token, first.token) is None
    assert world.run(world.service.caller_for_token, second.token) == ports.Caller(
        member_id=team.member.member_id, name="Mo", role="member", active=True
    )
    assert world.row(team.member.member_id).token == second.token


def test_arm6_caller_for_token_is_none_for_an_unknown_token(world: World, team: Team) -> None:
    issued = world.run(world.service.sign_in, "mo@example.test", "pass-mo-1").token
    assert world.run(world.service.caller_for_token, issued) == team.member
    for unknown in ("tok-999", "garbage", issued.upper()):
        assert world.run(world.service.caller_for_token, unknown) is None, unknown


@pytest.mark.parametrize("how", ["deactivated-by-the-service", "inactive-in-the-store"])
def test_arm6_caller_for_token_is_none_for_an_inactive_members_previously_issued_token(
    world: World, team: Team, how: str
) -> None:
    """In the store case only the active flag changes and the token stays in the row, so the None can come
    only from the active check (IR-11)."""
    mo = team.member.member_id
    issued = world.run(world.service.sign_in, "mo@example.test", "pass-mo-1").token
    assert world.run(world.service.caller_for_token, issued) == team.member
    if how == "deactivated-by-the-service":
        world.run(world.service.deactivate, team.admin, mo)
    else:
        world.set_active(mo, False)
        assert world.row(mo).token == issued
    assert world.run(world.service.caller_for_token, issued) is None


@pytest.mark.parametrize(
    "email, passcode",
    [
        pytest.param("mo@example.test", "pass-mo-2", id="wrong-passcode"),
        pytest.param("mo@example.test", "PASS-MO-1", id="wrong-case-passcode"),
        pytest.param("mo@example.test", "", id="empty-passcode"),
        pytest.param("mo@example.test", None, id="missing-passcode"),
        pytest.param("nobody@example.test", "pass-mo-1", id="unknown-email"),
    ],
)
def test_arm6_sign_in_refuses_invalid_credentials_and_changes_nothing(
    world: World, team: Team, email: str, passcode: str | None
) -> None:
    issued = world.run(world.service.sign_in, "mo@example.test", "pass-mo-1").token
    before = world.rows()
    assert world.refusal(world.service.sign_in, email, passcode) == "invalid_credentials"
    assert world.rows() == before
    assert world.run(world.service.caller_for_token, issued) == team.member
    assert world.spy.sent == []


@pytest.mark.parametrize(
    "passcode, reason",
    [
        pytest.param("pass-mo-2", "invalid_credentials", id="wrong-passcode"),
        pytest.param(None, "invalid_credentials", id="missing-passcode"),
        pytest.param("pass-mo-1", "member_inactive", id="right-passcode"),
    ],
)
def test_arm6_credentials_are_verified_before_the_active_check(
    world: World, team: Team, passcode: str | None, reason: str
) -> None:
    world.set_active(team.member.member_id, False)
    before = world.rows()
    assert world.refusal(world.service.sign_in, "mo@example.test", passcode) == reason
    assert world.rows() == before
    assert world.spy.sent == []


# ---------------------------------------------------------------------------------------------------- arm 7
#: SYNTHETIC roster (name, email, role, active); Zed is seeded, the rest are added in this order, so "al" has
#: a lower id than "Al". The names make both sort keys of list_members matter: a case-sensitive sort, a sort
#: by (lower name, name) and a sort by id each give another order.
ROSTER: tuple[tuple[str, str, str, bool], ...] = (
    ("Zed", "zed@example.test", "admin", True),
    ("bea", "bea@example.test", "member", False),
    ("al", "al.lower@example.test", "planner", True),
    ("Al", "al.upper@example.test", "member", True),
    ("Pat", "pat@example.test", "planner", False),
    ("Abe", "abe@example.test", "admin", False),
)
EMAIL = {name: email for name, email, _role, _active in ROSTER}
ROLE = {name: role for name, _email, role, _active in ROSTER}
ACTIVE = {name: active for name, _email, _role, active in ROSTER}
LISTED_ORDER = ("Abe", "al", "Al", "bea", "Pat", "Zed")


@pytest.fixture
def roster(world: World) -> dict[str, int]:
    """The ROSTER above, built through seed_admin and add_member; the inactive ones are set in the store."""
    (seeded, seeded_email, _role, _active), *added = ROSTER
    ids = {seeded: world.run(world.service.seed_admin, seeded, seeded_email, _passcode(seeded_email))}
    admin = _caller(ids[seeded], seeded, "admin")
    for name, email, role, _active in added:
        ids[name] = world.add(admin, name, email, role, _passcode(email)).id
    for name, _email, _role, active in ROSTER:
        if not active:
            world.set_active(ids[name], False)
    world.spy.sent.clear()
    return ids


@pytest.mark.parametrize("name", ["Zed", "al", "Al"])
def test_arm7_caller_for_token_resolves_a_signed_in_member_to_their_caller(
    world: World, roster: dict[str, int], name: str
) -> None:
    token = world.run(world.service.sign_in, EMAIL[name], _passcode(EMAIL[name])).token
    assert world.run(world.service.caller_for_token, token) == ports.Caller(
        member_id=roster[name], name=name, role=ROLE[name], active=True
    )


def test_arm7_is_active_answers_true_false_or_none_for_an_unknown_id(
    world: World, roster: dict[str, int]
) -> None:
    for name, member_id in roster.items():
        assert world.run(world.service.is_active, member_id) is ACTIVE[name], name
    assert world.run(world.service.is_active, UNKNOWN_ID) is None


def test_arm7_role_of_answers_the_role_or_raises_member_not_found_for_an_unknown_id(
    world: World, roster: dict[str, int]
) -> None:
    for name, member_id in roster.items():
        assert world.run(world.service.role_of, member_id) == ROLE[name], name
    with pytest.raises(ports.MemberNotFound):
        world.run(world.service.role_of, UNKNOWN_ID)


def test_arm7_name_of_answers_the_name_or_raises_member_not_found_for_an_unknown_id(
    world: World, roster: dict[str, int]
) -> None:
    for name, member_id in roster.items():
        assert world.run(world.service.name_of, member_id) == name
    with pytest.raises(ports.MemberNotFound):
        world.run(world.service.name_of, UNKNOWN_ID)


def test_arm7_active_member_ids_excludes_the_inactive(world: World, roster: dict[str, int]) -> None:
    active = sorted(roster[n] for n in ("Zed", "al", "Al"))
    assert sorted(world.run(world.service.active_member_ids)) == active


def test_arm7_decider_ids_are_the_active_admins_and_planners(world: World, roster: dict[str, int]) -> None:
    """Never a member (Al), an inactive planner (Pat) or an inactive admin (Abe)."""
    assert sorted(world.run(world.service.decider_ids)) == sorted(roster[n] for n in ("Zed", "al"))


@pytest.mark.parametrize("caller_name", ["Zed", "al", "Al"], ids=["an-admin", "a-planner", "a-member"])
def test_arm7_list_members_answers_every_member_by_name_case_insensitively_then_id(
    world: World, roster: dict[str, int], caller_name: str
) -> None:
    assert roster["al"] < roster["Al"]
    caller = _caller(roster[caller_name], caller_name, ROLE[caller_name])
    expected = [MemberSummary(id=roster[n], name=n, role=ROLE[n], active=ACTIVE[n]) for n in LISTED_ORDER]
    assert world.run(world.service.list_members, caller) == expected
    assert world.spy.sent == []


def test_arm7_list_members_rows_carry_id_name_role_active_and_never_email_passcode_or_token(
    world: World, roster: dict[str, int]
) -> None:
    token = world.run(world.service.sign_in, EMAIL["Zed"], _passcode(EMAIL["Zed"])).token
    listed = world.run(world.service.list_members, _caller(roster["Zed"], "Zed", "admin"))
    assert len(listed) == len(ROSTER)
    secret = {token} | {r.email for r in world.rows()} | {r.passcode_hash for r in world.rows()}
    secret |= {_passcode(email) for email in EMAIL.values()}
    for row in listed:
        assert type(row) is MemberSummary
        assert tuple(f.name for f in fields(row)) == ("id", "name", "role", "active")
        for absent in ("email", "passcode", "passcode_hash", "token"):
            assert not hasattr(row, absent), absent
        assert not {str(v) for v in astuple(row)} & secret


# ---------------------------------------------------------------------------------------------------- values
@pytest.mark.parametrize(
    "cls, names",
    [
        pytest.param("MemberValue", ("id", "name", "email", "role", "active"), id="MemberValue"),
        pytest.param("SignInValue", ("token", "member"), id="SignInValue"),
        pytest.param("MemberSummary", ("id", "name", "role", "active"), id="MemberSummary"),
    ],
)
def test_interfaces_the_identity_values_are_frozen_dataclasses_with_their_declared_fields(
    cls: str, names: tuple[str, ...]
) -> None:
    value_type = {"MemberValue": MemberValue, "SignInValue": SignInValue, "MemberSummary": MemberSummary}[cls]
    member = MemberValue(id=1, name="Ada", email="ada@example.test", role="admin", active=True)
    sample = {**vars(member), "token": "tok-001", "member": member}
    assert is_dataclass(value_type)
    assert tuple(f.name for f in fields(value_type)) == names
    value = value_type(**{n: sample[n] for n in names})
    with pytest.raises(FrozenInstanceError):
        setattr(value, names[0], sample[names[0]])


# ---------------------------------------------------------------------------------------------------- amends
def _synthetic_member(name: str = "Uma") -> models.Member:
    """SYNTHETIC: an invented member written straight through the data model."""
    email = f"{name.lower()}@example.test"
    return models.Member(
        name=name,
        email=email,
        role="member",
        active=True,
        passcode_hash=models.hash_passcode(_passcode(email), "saltuma1"),
        token=None,
    )


class RolledBack(Exception):
    """Raised inside a unit of work to make it roll back."""


def test_amend_db_current_session_raises_no_current_session_outside_a_unit_of_work() -> None:
    assert issubclass(db.NoCurrentSession, RuntimeError)
    with pytest.raises(db.NoCurrentSession):
        db.current_session()


def test_amend_db_unit_of_work_makes_its_session_current_commits_on_return_and_closes(tmp_path: Path) -> None:
    engine = db.engine_for(tmp_path)
    uma = _synthetic_member()
    with db.unit_of_work(engine) as session:
        assert db.current_session() is session
        session.add(uma)
    with pytest.raises(db.NoCurrentSession):
        db.current_session()
    assert inspect(uma).detached, "the session was not closed"
    assert [r.name for r in _rows(engine)] == ["Uma"]
    engine.dispose()


def test_amend_db_unit_of_work_rolls_back_on_raise_and_restores_the_previous_state(tmp_path: Path) -> None:
    engine = db.engine_for(tmp_path)
    with pytest.raises(RolledBack):
        with db.unit_of_work(engine) as session:
            session.add(_synthetic_member())
            session.flush()
            raise RolledBack
    with pytest.raises(db.NoCurrentSession):
        db.current_session()
    assert _rows(engine) == []
    engine.dispose()


def test_amend_db_use_session_and_unit_of_work_nest_and_restore_the_previous_session(tmp_path: Path) -> None:
    """use_session makes a session current for its block, restores the previous one on exit and commits
    nothing; a nested unit_of_work restores the outer session too."""
    engine = db.engine_for(tmp_path)
    with db.unit_of_work(engine) as outer:
        inner = db.session_for(engine)
        try:
            with db.use_session(inner) as used:
                assert used is inner
                assert db.current_session() is inner
                inner.add(_synthetic_member("Uma"))
                inner.flush()
            assert db.current_session() is outer
        finally:
            inner.close()
        with db.unit_of_work(engine) as nested:
            assert nested is not outer
            assert db.current_session() is nested
        assert db.current_session() is outer
    with pytest.raises(db.NoCurrentSession):
        db.current_session()
    assert _rows(engine) == [], "use_session committed"
    engine.dispose()


def test_amend_ports_refused_carries_its_reason_and_the_extra_fields_a_story_names() -> None:
    refused = Refused("unfilled_x", "d", unfilled=[1])
    assert isinstance(refused, Exception)
    assert refused.reason == "unfilled_x"
    assert refused.extra == {"unfilled": [1]}
    bare = Refused("team_not_empty")
    assert bare.reason == "team_not_empty"
    assert bare.extra == {}
