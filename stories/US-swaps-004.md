---
id: US-swaps-004
title: Member sees their open requests
domain: swaps
persona: Mo
journey: J-05
step: 1
roles: [admin, planner, member]
data: [SwapRequest]
arms:
  - { arm: "the member's requests are listed with state and the party whose action is awaited", kind: deterministic }
  - { arm: "a request past its shift's deadline without a decision is shown expired, never pending", kind: deterministic }
---
## Story
As a member, I want to see my open requests and who is holding them up so that nothing is hidden.

## Rules
See design/domains/swaps/spec.md — the rules this story serves are referenced by id there.

## Data touched
SwapRequest (owned by swaps)

## Out of scope
Anything the journey step does not name; no free text, no optimisation, no second team.
