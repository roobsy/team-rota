---
id: US-swaps-005
title: Planner or admin sees pending decisions
domain: swaps
persona: Pat
journey: J-05
step: 2
roles: [admin, planner]
data: [SwapRequest]
arms:
  - { arm: "every accepted request awaiting a decision is listed oldest first by accepted_at, the same list for any admin or planner", kind: deterministic }
  - { arm: "requests the viewer is party to are listed and marked party, with no decide controls", kind: deterministic }
  - { arm: "a member calling the action is refused with reason forbidden", kind: deterministic }
---
## Story
As a planner or admin, I want to see every pending decision so that no swap waits unseen.

## Rules
The rules this story serves are in the swaps domain spec, referenced by id there.

## Data touched
SwapRequest (owned)

## Out of scope
Assignment of decisions to a named decider.
Anything the journey step does not name; no free text, no optimisation, no second team.
