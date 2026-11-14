"""ADU-16 arms 3–4: one test per Null — each test is deleted together with its Null by the retiring unit
(its amends); the file goes with the last Null (ADU-07)."""

from __future__ import annotations

from datetime import datetime

import pytest

from app import ports
from app.swaps.null_port import NullSwapsPort

REPLACED = {
    NullSwapsPort: "ADU-07",
}


@pytest.mark.parametrize("cls", list(REPLACED))
def test_each_null_names_its_provider_and_satisfies_its_protocol(cls: type) -> None:
    assert f"replaced by {REPLACED[cls]}, class not shape" in (cls.__doc__ or "")
    proto = {
        NullSwapsPort: ports.SwapsPort,
    }[cls]
    assert isinstance(cls(), proto)


def test_null_swaps_port_answers_nothing_pending_and_nothing_requestable() -> None:  # deleted by ADU-07
    assert NullSwapsPort().view(1, True, [(5, 1, datetime(2026, 11, 9, 8))]) == {
        5: ports.AssignmentView(pending=None, requestable=False)
    }
