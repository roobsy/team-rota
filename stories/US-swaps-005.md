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
  - { arm: "every open accepted request is listed oldest first by answered_at then id ascending, each with its shift's date and start and both parties' names, the same list for any admin or planner; an accepted request whose deadline has passed is not listed (it shows expired in the parties' own lists)", kind: deterministic }
  - { arm: "requests the viewer is party to are listed and marked swap-party, with no decide controls", kind: deterministic }
  - { arm: "a request whose party is inactive is still listed to deciders", kind: deterministic }
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
