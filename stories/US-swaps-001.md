---
id: US-swaps-001
title: Member requests a swap
domain: swaps
persona: Mo
journey: J-04
step: 1
roles: [admin, planner, member]
data: [SwapRequest, Assignment, Member]
arms:
  - { arm: "a request for an assignment the member holds, naming an active counterpart not on that shift and a reason code, is recorded in state requested", kind: deterministic }
  - { arm: "a request for an assignment the member does not hold is refused with reason not_holder", kind: deterministic }
  - { arm: "a request after the shift's deadline is refused with reason past_deadline", kind: deterministic }
  - { arm: "a second open request for the same assignment is refused with reason request_open", kind: deterministic }
---
## Story
As a member, I want to request a swap with a counterpart and a reason so that I can hand over a shift I cannot work.

## Rules
See design/domains/swaps/spec.md — the rules this story serves are referenced by id there.

## Data touched
SwapRequest, Assignment, Member (owned by swaps; others read through an interface)

## Out of scope
Anything the journey step does not name; no free text, no optimisation, no second team.
