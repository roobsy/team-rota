# scheduling — domain spec
v1.2 · owned by pm-lead. The business rules of this domain, each testable, each naming the story it serves. v1.3 applies the dispositions of DESIGN-REVIEW-3.

## Rules
| Rule | Statement | Serves | Testable as |
|---|---|---|---|
| R-scheduling-01 | A week is the seven days from a Monday, keyed by that start_date, and comes into being in state draft with its first shift (so a week always has a shift); a shift lies on one of those days with start and end as times of day on that date, end after start, never crossing midnight; slots is at least one | US-scheduling-001 | not_week_start, outside_week, invalid_interval, invalid_slots |
| R-scheduling-02 | An active member holds at most one slot per shift and no two shifts whose half-open intervals [start, end) intersect on the same date — a slot on the same shift counts as an overlap; an inactive member is never assigned or transferred to | US-scheduling-002, US-scheduling-006 | already_assigned, overlapping_shift, member_inactive; counterpart_overlap, counterpart_inactive on transfer |
| R-scheduling-03 | A week publishes only when every slot is filled; the refusal lists the unfilled shifts (shift id, date, start, unfilled); an unknown start_date is not_found | US-scheduling-003 | unfilled_slots, not_found |
| R-scheduling-04 | A published week changes only through a transfer requested by swaps; creating, assigning, unassigning and publishing again are refused on it and nothing is emitted; an assignment of a draft week may be removed | US-scheduling-002, US-scheduling-003, US-scheduling-006 | week_published; the transfer on approval |
| R-scheduling-05 | The board lists shifts by date, start, then shift id; each holder-row carries the open request on that assignment (requested or accepted, open as R-swaps-06 defines it, answered by swaps through IR-07) and nothing otherwise; a pending request never looks done | US-scheduling-004 | the badge text equals the open request's state, per holder-row |
| R-scheduling-06 | A draft week's board is returned to planners and admins only; the weeks list shows members published weeks only; the current week (latest published with start_date on or before today) is served by the API, never computed in the browser | US-scheduling-004 | week_draft; the list and the current week |
| R-scheduling-07 | A shift holds at most slots assignments | US-scheduling-002 | shift_full |
| R-scheduling-08 | The transfer is an internal interface for swaps, running inside the caller's transaction and committing nothing itself; no operation performs it | US-scheduling-006 | the interface called directly in scheduling's tests; the contract's operation ids include no transfer and no API module imports the transfer function (layering); the end-to-end path is US-swaps-003 |
| R-scheduling-09 | The seeded fixture seeded_week(seed): clock fixed at 2026-11-05 09:00 (Thursday); start_date 2026-11-09; 7 days × shifts 08:00–12:00, 12:00–16:00, 16:00–20:00 × 2 slots (42 slots); 12 active members (1 admin, 2 planners, 9 members) assigned round-robin over members in id order with no overlap; the week published; open requests on the first 5 assignments alternating requested and accepted; the seeded generator draws the synthetic names and emails (under example.test) and the counterparts among the eligible — that is what the seed varies | US-scheduling-004 and the timing arm | the fixture reproduces byte for byte for one seed and differs for another in names and counterparts |

## Interfaces this domain needs from others
- identity: whether a member is active, their role, and their name for holder-rows (IR-06); the ids of every active member, for week_published's recipients (IR-12)
- swaps: the open requests among the assignments scheduling passes with their start instants, open as R-swaps-06 defines it (IR-07)
- notifications: emit week_published (IR-08)
