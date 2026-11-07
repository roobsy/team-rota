# swaps — domain spec
v1.1 · owned by pm-swaps. The business rules of this domain, each testable, each naming the story it serves. v1.1 applies the dispositions of DESIGN-REVIEW-1.

## Rules
| Rule | Statement | Serves | Testable as |
|---|---|---|---|
| R-swaps-01 | Only the holder requests a swap of an assignment, on a published week, before the deadline: 24 hours before the shift's start instant by the injected clock | US-swaps-001 | not_holder, week_draft, past_deadline |
| R-swaps-02 | One open request (state requested or accepted) per assignment | US-swaps-001 | request_open |
| R-swaps-03 | Only the named counterpart answers, only in state requested, only before the deadline | US-swaps-002 | not_counterpart, wrong_state, past_deadline |
| R-swaps-04 | Only an accepted request is decided, only before the deadline; approval is one atomic action: transfer through scheduling first, then one Decision row (approved) and the request mirrors it; a refused transfer records a Decision refused with the transfer's reason and the decider who attempted it; a refusal records a Decision refused with the reason code | US-swaps-003 | wrong_state, past_deadline; the Decision row and the mirrored state |
| R-swaps-05 | Nobody decides a swap they are party to; any admin or planner who is not a party decides; the pending list marks requests the viewer is party to | US-swaps-003, US-swaps-005 | party_to_swap; the party mark |
| R-swaps-06 | A request in state requested or accepted whose deadline has passed is shown expired: derived on read from the clock, never stored, never notified | US-swaps-004 | the expired display state |
| R-swaps-07 | Reason codes are enumerated and required: request sick, family, travel, other; decline unavailable, other; refusal fairness, coverage, policy, other; the transfer's counterpart_overlap and counterpart_inactive are recorded as refusal reasons by the system | US-swaps-001, US-swaps-002, US-swaps-003 | reason_required, invalid_reason; the enum |
| R-swaps-08 | The counterpart is an active member other than the requester who holds no slot on that shift | US-swaps-001 | counterpart_inactive, counterpart_on_shift, counterpart_self |
| R-swaps-09 | Lists are ordered by a stored timestamp: a member's requests newest first by created_at; pending decisions oldest first by accepted_at | US-swaps-004, US-swaps-005 | the order |

## Interfaces this domain needs from others
- scheduling: read an assignment's holder and its shift's start instant (IR-01); transfer an assignment to the counterpart, refused on overlap or inactivity (IR-02)
- notifications: a Notifier to emit the request / answer / outcome events (IR-03)
- identity: whether the counterpart is active, and member names for notification text (IR-09)
