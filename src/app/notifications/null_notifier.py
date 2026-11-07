"""NullNotifier — replaced by ADU-09, class not shape. Records what it is asked to send; writes nothing."""

from __future__ import annotations

from app.ports import Event


class NullNotifier:
    """replaced by ADU-09, class not shape"""

    def __init__(self) -> None:
        self.sent: list[Event] = []

    def notify(self, event: Event) -> None:
        self.sent.append(event)
