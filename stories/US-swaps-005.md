---
id: US-swaps-005
title: Planner sees pending approvals
domain: swaps
persona: Pat
journey: J-05
step: 2
roles: [admin, planner]
data: [SwapRequest]
arms:
  - { arm: "every accepted request awaiting approval is listed oldest first", kind: deterministic }
  - { arm: "requests the planner is party to are listed but marked decide_by_admin", kind: deterministic }
---
## Story
As a planner, I want to see every pending approval so that no swap waits unseen.

## Rules
See design/domains/swaps/spec.md — the rules this story serves are referenced by id there.

## Data touched
SwapRequest (owned by swaps)

## Out of scope
Anything the journey step does not name; no free text, no optimisation, no second team.
