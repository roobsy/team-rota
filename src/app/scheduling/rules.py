"""Scheduling's rules as pure functions (ADU-05, layer 3): no session, no clock, no other domain.

The service computes with these before it writes (design/ARCHITECTURE.md, Persistence and concurrency rules:
compute first, then write).
"""

from __future__ import annotations

import re
from datetime import date, datetime, time, timedelta

WEEK_DAYS = 7
#: a time of day as the contract writes it, HH:MM from 00:00 to 23:59 (R-scheduling-01: "at most 23:59")
_TIME_OF_DAY = re.compile(r"([01][0-9]|2[0-3]):([0-5][0-9])")


def is_week_start(start_date: date) -> bool:
    """A week is keyed by its Monday (R-scheduling-01)."""
    return start_date.weekday() == 0


def within_week(start_date: date, day: date) -> bool:
    """The seven days from start_date (R-scheduling-01)."""
    return start_date <= day < start_date + timedelta(days=WEEK_DAYS)


def time_of_day(text: str | None) -> time | None:
    """The time of day `text` names as HH:MM, or None when it names none (missing, not text, out of range)."""
    if not isinstance(text, str):
        return None
    match = _TIME_OF_DAY.fullmatch(text)
    return None if match is None else time(int(match.group(1)), int(match.group(2)))


def valid_interval(start: time | None, end: time | None) -> bool:
    """Both are times of day on the shift's date and end is after start; a shift never crosses midnight."""
    return start is not None and end is not None and end > start


def valid_slots(slots: object) -> bool:
    """slots is an integer of at least one (R-scheduling-01)."""
    return isinstance(slots, int) and not isinstance(slots, bool) and slots >= 1


def intersects(start: time, end: time, other_start: time, other_end: time) -> bool:
    """Two half-open intervals [start, end) on the same date intersect (R-scheduling-02)."""
    return start < other_end and other_start < end


def start_instant(day: date, start: time) -> datetime:
    """A shift's start instant is its date plus its start time (PRODUCT-DESIGN, The clock)."""
    return datetime.combine(day, start)


def current_week(published_start_dates: list[date], today: date) -> date | None:
    """The latest published week whose start_date is on or before today, or None (R-scheduling-06)."""
    begun = [d for d in published_start_dates if d <= today]
    return max(begun) if begun else None
