"""The identity service (ADU-03, layer 3): members, roles and sign-in, and the MemberDirectory that the other
domains and the API layer read (design/INTERFACES.md, IdentityService and MemberDirectory).

- Sessions (D-14). Every method reads and writes in db.current_session() and never opens, commits or closes
  one. Each method takes that session before any check, so with none current db.NoCurrentSession propagates.
- Refusals. Every refusal is ports.Refused. Checks run in the cross-cutting order forbidden → not_found →
  state → validation (R-identity-08), and within a bucket in the order the story's arms list them
  (PRODUCT-DESIGN, cross-cutting rules). Every check comes before the first write, so a refusal changes
  nothing.
- Bindings (D-15). The clock, the scheduling port and the notifier are the composition root's bindings, read
  at call time.
- Credentials (D-16). Tokens and salts come from the TokenSource passed in.
"""

from __future__ import annotations

import hmac
import secrets
from collections.abc import Callable
from dataclasses import dataclass
from typing import Protocol

from sqlalchemy.orm import Session

from app import db, models
from app.identity import repo
from app.ports import (
    Caller,
    Clock,
    MemberAdded,
    MemberDeactivated,
    MemberNotFound,
    Notifier,
    Refused,
    RoleChanged,
    SchedulingPort,
)

ADMIN = "admin"
DECIDER_ROLES = ("admin", "planner")
INVALID_ROLE = "Role must be admin, planner or member."


class Bindings(Protocol):
    """The composition root's bindings the service reads (D-15); main.Ports satisfies it, so identity never
    imports main."""

    clock: Clock
    scheduling: SchedulingPort
    notifier: Notifier


class TokenSource(Protocol):
    """Where bearer tokens and passcode salts come from (D-16)."""

    def token(self) -> str: ...
    def salt(self) -> str: ...


class SecretsSource:
    """The product's TokenSource (D-16): the standard library's secrets, never random."""

    def token(self) -> str:
        return secrets.token_urlsafe(32)

    def salt(self) -> str:
        return secrets.token_hex(8)


@dataclass(frozen=True)
class MemberValue:
    """The contract's Member (D-17)."""

    id: int
    name: str
    email: str
    role: str
    active: bool


@dataclass(frozen=True)
class SignInValue:
    """The contract's Token (D-17)."""

    token: str
    member: MemberValue


@dataclass(frozen=True)
class MemberSummary:
    """A member as the team list shows it: never email, passcode or token (R-identity-09; D-17)."""

    id: int
    name: str
    role: str
    active: bool


def _value(member: models.Member) -> MemberValue:
    return MemberValue(
        id=member.id, name=member.name, email=member.email, role=member.role, active=member.active
    )


def _verifies(passcode_hash: str, passcode: str) -> bool:
    """Recomputes models.hash_passcode with the stored salt (the text before '$'); compared in constant
    time."""
    salt = passcode_hash.split("$", 1)[0]
    candidate = models.hash_passcode(passcode, salt)
    return hmac.compare_digest(candidate.encode("utf-8"), passcode_hash.encode("utf-8"))


class IdentityService:
    """Implements ports.MemberDirectory and the identity operations; the composition root binds it as
    Ports.member_directory (ADU-03 arm 1)."""

    def __init__(self, bound: Callable[[], Bindings], source: TokenSource) -> None:
        self._bound = bound
        self._source = source

    # ---- MemberDirectory (IR-04, IR-06, IR-09, IR-11, IR-12)
    def caller_for_token(self, token: str) -> Caller | None:
        """None for an unknown token and for an inactive member's token (IR-11)."""
        member = repo.by_token(db.current_session(), token)
        if member is None or not member.active:
            return None
        return Caller(member_id=member.id, name=member.name, role=member.role, active=True)

    def is_active(self, member_id: int) -> bool | None:
        """None for an id that names no member."""
        member = repo.get(db.current_session(), member_id)
        return None if member is None else member.active

    def role_of(self, member_id: int) -> str:
        return self._existing(db.current_session(), member_id).role

    def name_of(self, member_id: int) -> str:
        return self._existing(db.current_session(), member_id).name

    def active_member_ids(self) -> list[int]:
        return [m.id for m in repo.all_members(db.current_session()) if m.active]

    def decider_ids(self) -> list[int]:
        """The active admins and planners."""
        members = repo.all_members(db.current_session())
        return [m.id for m in members if m.active and m.role in DECIDER_ROLES]

    # ---- operations (design/INTERFACES.md, IdentityService)
    def seed_admin(self, name: str, email: str, passcode: str) -> int:
        """An empty team gets one active admin; emits nothing (R-identity-07)."""
        session = db.current_session()
        if repo.count(session) > 0:
            raise Refused("team_not_empty", "The team already has members; the first admin is seeded once.")
        member = repo.add(session, name=name, email=email, role=ADMIN, passcode_hash=self._hash(passcode))
        return member.id

    def add_member(
        self, caller: Caller, name: str, email: str, role: str | None, passcode: str
    ) -> MemberValue:
        """R-identity-01, -02; emits MemberAdded."""
        session = db.current_session()
        self._require_admin(caller, "add a member")
        if repo.by_email(session, email) is not None:
            raise Refused("duplicate_email", f"{email} is already on the team.")
        if role not in models.ROLES:
            raise Refused("invalid_role", INVALID_ROLE)
        member = repo.add(session, name=name, email=email, role=role, passcode_hash=self._hash(passcode))
        self._bound().notifier.notify(MemberAdded(member_id=member.id, role=member.role))
        return _value(member)

    def change_role(self, caller: Caller, member_id: int, role: str | None) -> MemberValue:
        """R-identity-01, -03. The role already held is a no-op that emits nothing. An inactive member's role
        changes and nobody is notified."""
        session = db.current_session()
        self._require_admin(caller, "change a role")
        member = self._found(session, member_id)
        if role != ADMIN and self._is_last_active_admin(session, member):
            raise Refused("last_admin", f"{member.name} is the last active admin.")
        if role not in models.ROLES:
            raise Refused("invalid_role", INVALID_ROLE)
        if role == member.role:
            return _value(member)
        member.role = role
        if member.active:
            self._bound().notifier.notify(RoleChanged(member_id=member.id, role=role))
        return _value(member)

    def deactivate(self, caller: Caller, member_id: int) -> MemberValue:
        """R-identity-03, -04, -05: active false, the row kept; emits MemberDeactivated. The state checks run
        in US-identity-003's order: future_assignments, last_admin, member_inactive."""
        session = db.current_session()
        self._require_admin(caller, "deactivate a member")
        member = self._found(session, member_id)
        bound = self._bound()
        if bound.scheduling.has_assignment_after(member.id, bound.clock.now()):
            raise Refused("future_assignments", f"{member.name} holds an assignment on a shift after now.")
        if self._is_last_active_admin(session, member):
            raise Refused("last_admin", f"{member.name} is the last active admin.")
        if not member.active:
            raise Refused("member_inactive", f"{member.name} is already inactive; nothing was emitted.")
        member.active = False
        bound.notifier.notify(MemberDeactivated(member_id=member.id))
        return _value(member)

    def sign_in(self, email: str, passcode: str | None) -> SignInValue:
        """R-identity-06. Credentials are verified before the active check, and a missing passcode counts as
        wrong. The new token replaces the member's earlier one. Emits nothing."""
        session = db.current_session()
        member = repo.by_email(session, email)
        if member is None or passcode is None or not _verifies(member.passcode_hash, passcode):
            raise Refused("invalid_credentials", "The email or passcode is wrong.")
        if not member.active:
            raise Refused("member_inactive", "This member is inactive.")
        member.token = self._source.token()
        return SignInValue(token=member.token, member=_value(member))

    def list_members(self, caller: Caller) -> list[MemberSummary]:
        """Every member, active and inactive, by name compared case-insensitively, then id (R-identity-09).
        Any signed-in caller may read it."""
        members = sorted(repo.all_members(db.current_session()), key=lambda m: (m.name.lower(), m.id))
        return [MemberSummary(id=m.id, name=m.name, role=m.role, active=m.active) for m in members]

    # ---- helpers
    def _hash(self, passcode: str) -> str:
        return models.hash_passcode(passcode, self._source.salt())

    @staticmethod
    def _require_admin(caller: Caller, action: str) -> None:
        if caller.role != ADMIN:
            raise Refused("forbidden", f"Only an admin may {action}.")

    @staticmethod
    def _found(session: Session, member_id: int) -> models.Member:
        member = repo.get(session, member_id)
        if member is None:
            raise Refused("not_found", f"No member has the id {member_id}.")
        return member

    @staticmethod
    def _existing(session: Session, member_id: int) -> models.Member:
        member = repo.get(session, member_id)
        if member is None:
            raise MemberNotFound(member_id)
        return member

    @staticmethod
    def _is_last_active_admin(session: Session, member: models.Member) -> bool:
        return member.active and member.role == ADMIN and repo.active_admin_count(session) <= 1
