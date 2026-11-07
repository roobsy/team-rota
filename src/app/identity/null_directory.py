"""NullDirectory — replaced by ADU-03, class not shape. Resolves synthetic tokens for the contract unit's auth."""

from __future__ import annotations

from app.ports import Caller, Role


class NullDirectory:
    """replaced by ADU-03, class not shape"""

    def caller_for_token(self, token: str) -> Caller | None:
        if token == "tok_admin":
            return Caller(member_id=1, name="Member 1", role="admin", active=True)
        if token.startswith("tok_") and token[4:].isdigit():
            n = int(token[4:])
            return Caller(member_id=n, name=f"Member {n}", role="member", active=True)
        return None

    def is_active(self, member_id: int) -> bool | None:
        return True

    def role_of(self, member_id: int) -> Role:
        return "member"

    def name_of(self, member_id: int) -> str:
        return f"Member {member_id}"

    def active_member_ids(self) -> list[int]:
        return []

    def decider_ids(self) -> list[int]:
        return []
