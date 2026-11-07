# swaps — domain spec
v1.0 · owned by pm-swaps. The business rules of this domain, each testable, each naming the story it serves.

## Rules
| Rule | Statement | Serves | Testable as |
|---|---|---|---|
| R-swaps-01 | Only the holder requests a swap of an assignment, before the shift's deadline (24 h before start) | US-swaps-001 | not_holder, past_deadline |
| R-swaps-02 | One open request per assignment | US-swaps-001 | request_open |
| R-swaps-03 | Only the named counterpart answers, only in state requested | US-swaps-002 | not_counterpart, wrong_state |
| R-swaps-04 | Only an accepted request can be approved or refused; every refusal carries a reason code | US-swaps-003 | wrong_state; reason required |
| R-swaps-05 | Nobody decides a swap they are party to; the admin decides those | US-swaps-003, US-swaps-005 | party_to_swap; decide_by_admin |
| R-swaps-06 | A request undecided at the deadline is expired, never pending | US-swaps-004 | expired state |
| R-swaps-07 | Reason codes are enumerated: sick, family, travel, other (request); unavailable, other (decline); fairness, coverage, policy, other (refusal) | all | the enum |

## Interfaces this domain needs from others
- scheduling: read an assignment's holder and shift (deadline), transfer an assignment on approval (INTERFACE-REQUESTS rows 1–2).
- notifications: a Notifier to emit the request/answer/outcome events (row 3).
