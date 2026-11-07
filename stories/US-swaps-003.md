---
id: US-swaps-003
title: Planner approves or refuses
domain: swaps
persona: Pat
journey: J-04
step: 5
roles: [admin, planner]
data: [SwapRequest, Approval]
arms:
  - { arm: "approving an accepted request records an approval and moves the request to approved", kind: deterministic }
  - { arm: "refusing records the reason code and moves the request to refused", kind: deterministic }
  - { arm: "a planner who is the requester or the counterpart is refused with reason party_to_swap; the admin may decide instead", kind: deterministic }
  - { arm: "approving a request that is not accepted is refused with reason wrong_state", kind: deterministic }
---
## Story
As a planner, I want to approve or refuse an accepted swap with a reason so that the roster changes only by decision.

## Rules
See design/domains/swaps/spec.md — the rules this story serves are referenced by id there.

## Data touched
SwapRequest, Approval (owned by swaps)

## Out of scope
Anything the journey step does not name; no free text, no optimisation, no second team.
