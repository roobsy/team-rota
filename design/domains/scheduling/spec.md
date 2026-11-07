# scheduling — domain spec
v1.0 · owned by pm-lead. The business rules of this domain, each testable, each naming the story it serves.

## Rules
| Rule | Statement | Serves | Testable as |
|---|---|---|---|
| R-scheduling-01 | A shift lies inside its week and ends after it starts | US-scheduling-001 | invalid_interval, outside_week |
| R-scheduling-02 | A member holds at most one slot per shift and no overlapping shifts | US-scheduling-002 | already_assigned, overlapping_shift |
| R-scheduling-03 | A week publishes only when every slot is filled | US-scheduling-003 | unfilled_slots lists the slots |
| R-scheduling-04 | A published week changes only through an approved swap | US-scheduling-003, US-scheduling-006 | week_published refusal; transfer on approval |
| R-scheduling-05 | The board never shows a pending swap as done | US-scheduling-004 | pending badge names the state |
| R-scheduling-06 | A draft week is visible to planners and admins only | US-scheduling-004 | week_draft refusal |

## Interfaces this domain needs from others
