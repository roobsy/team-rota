---
id: US-swaps-003
title: Planner or admin decides
domain: swaps
persona: Pat
journey: J-04
step: 5
roles: [admin, planner]
data: [SwapRequest, Decision, Assignment]
arms:
  - { arm: "approving an accepted request first transfers the assignment through scheduling and then records one decision (decider, outcome approved, decided_at) and the request mirrors approved", kind: deterministic }
  - { arm: "refusing an accepted request records one decision with outcome refused and the reason code, and the request mirrors refused", kind: deterministic }
  - { arm: "a decision by the requester or the counterpart, whether planner or admin, is refused with reason party_to_swap", kind: deterministic }
  - { arm: "an admin who is not a party decides a request a planner is party to", kind: deterministic }
  - { arm: "deciding a request that is not in state accepted is refused with reason wrong_state", kind: deterministic }
  - { arm: "deciding after the shift's deadline is refused with reason past_deadline", kind: deterministic }
  - { arm: "when the transfer is refused (counterpart_overlap or counterpart_inactive) the decision is recorded refused with that reason, the decider is the member who attempted the approval, and the request mirrors refused", kind: deterministic }
  - { arm: "a refusal without a reason code is refused with reason reason_required; one outside the enumerated codes with reason invalid_reason", kind: deterministic }
  - { arm: "a member calling the action is refused with reason forbidden", kind: deterministic }
  - { arm: "the inbox shows the approve and refuse controls only to an admin or planner who is not a party, and after the decision shows the outcome and the reason", kind: deterministic }
---
## Story
As a planner or admin, I want to approve or refuse an accepted swap with a reason so that the roster changes only by a recorded decision.

## Rules
The rules this story serves are in the swaps domain spec, referenced by id there.

## Data touched
SwapRequest, Decision (owned); Assignment (read through scheduling's interface)

## Out of scope
Delegation, multi-step approval.
Anything the journey step does not name; no free text, no optimisation, no second team.
