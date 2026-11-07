"""NullSwapsPort — replaced by ADU-07, class not shape."""

from __future__ import annotations

from datetime import datetime
from typing import Iterable

from app.ports import AssignmentView


class NullSwapsPort:
    """replaced by ADU-07, class not shape"""

    def view(
        self, caller_id: int, week_published: bool, assignments: Iterable[tuple[int, int, datetime]]
    ) -> dict[int, AssignmentView]:
        return {
            assignment_id: AssignmentView(pending=None, requestable=False)
            for assignment_id, _h, _s in assignments
        }
