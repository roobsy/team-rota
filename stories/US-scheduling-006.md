---
id: US-scheduling-006
title: Approval moves the assignment
domain: scheduling
persona: Mo
journey: J-04
step: 6
roles: [admin, planner, member]
data: [Assignment, SwapRequest]
arms:
  - { arm: "on approval the assignment's holder becomes the counterpart and the board shows it", kind: deterministic }
  - { arm: "the transfer is refused with reason counterpart_overlap if the counterpart now overlaps another shift, and the request is marked refused with that reason", kind: deterministic }
---
## Story
As a member, I want the approved swap reflected on the board so that the roster is the truth.

## Rules
See design/domains/scheduling/spec.md — the rules this story serves are referenced by id there.

## Data touched
Assignment, SwapRequest (owned by scheduling; others read through an interface)

## Out of scope
Anything the journey step does not name; no free text, no optimisation, no second team.
