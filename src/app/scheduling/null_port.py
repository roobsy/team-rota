"""NullSchedulingPort — replaced by ADU-05, class not shape."""

from __future__ import annotations

from datetime import datetime

from app.ports import AssignmentInfo, AssignmentNotFound


class NullSchedulingPort:
    """replaced by ADU-05, class not shape"""

    def assignment(self, assignment_id: int) -> AssignmentInfo:
        raise AssignmentNotFound(assignment_id)

    def holds_intersecting_shift(self, member_id: int, shift_id: int) -> bool:
        return False

    def transfer(self, assignment_id: int, to_member_id: int) -> None:
        return None

    def has_assignment_after(self, member_id: int, now: datetime) -> bool:
        return False
