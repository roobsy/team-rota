# scheduling — domain spec
v1.1 · owned by pm-lead. The business rules of this domain, each testable, each naming the story it serves. v1.1 applies the dispositions of DESIGN-REVIEW-1.

## Rules
| Rule | Statement | Serves | Testable as |
|---|---|---|---|
| R-scheduling-01 | A week is the seven days from a Monday, named by that start_date, and comes into being in state draft with its first shift; a shift lies on one of those days with start and end as times of day on that date, end after start, never crossing midnight; slots is at least one | US-scheduling-001 | not_week_start, outside_week, invalid_interval, invalid_slots |
| R-scheduling-02 | An active member holds at most one slot per shift and no two shifts whose half-open intervals [start, end) intersect on the same date; an inactive member is never assigned or transferred to | US-scheduling-002, US-scheduling-006 | already_assigned, overlapping_shift, member_inactive, counterpart_overlap, counterpart_inactive |
| R-scheduling-03 | A week publishes only when it has at least one shift and every slot is filled; the refusal lists the unfilled shifts (shift id, date, start, unfilled) | US-scheduling-003 | unfilled_slots, no_shifts |
| R-scheduling-04 | A published week changes only through a transfer requested by swaps; creating, assigning and unassigning are refused on it; an assignment of a draft week may be removed | US-scheduling-002, US-scheduling-003, US-scheduling-006 | week_published; the transfer on approval |
| R-scheduling-05 | The board shows a badge on a shift with a request in state requested or accepted, whose text is that state, and no badge otherwise; a pending request never looks done | US-scheduling-004 | the badge text equals the state |
| R-scheduling-06 | A draft week's board is returned to planners and admins only | US-scheduling-004 | week_draft |
| R-scheduling-07 | A shift holds at most slots assignments | US-scheduling-002 | shift_full |
| R-scheduling-08 | The transfer is an internal interface for swaps, never an operation of the API | US-scheduling-006 | no operation exists; the interface is tested through swaps' approval |

## Interfaces this domain needs from others
- identity: whether a member is active, and their role for the draft-week rule (IR-06)
- swaps: the open requests per shift for the badge (IR-07)
- notifications: emit the week-published event (IR-08)
