---
id: US-scheduling-005
title: Member filters the board to their shifts
domain: scheduling
persona: Mo
journey: J-03
step: 2
roles: [admin, planner, member]
data: [Assignment]
arms:
  - { arm: "the mine filter shows only shifts the member holds, in the same order", kind: deterministic }
  - { arm: "a member with no shifts sees an explicit empty state, not a blank board", kind: deterministic }
---
## Story
As a member, I want to filter the board to my shifts so that I see my week at a glance.

## Rules
See design/domains/scheduling/spec.md — the rules this story serves are referenced by id there.

## Data touched
Assignment (owned by scheduling)

## Out of scope
Anything the journey step does not name; no free text, no optimisation, no second team.
