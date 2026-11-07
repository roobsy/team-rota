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
  - { arm: "the mine parameter of the board operation returns only shifts the member holds, in the same order; board-filter-mine sets it", kind: deterministic }
  - { arm: "a member with no shifts sees the board-empty-mine state with the text \"No shifts this week\", not a blank board", kind: deterministic }
---
## Story
As a member, I want to filter the board to my shifts so that I see my week at a glance.

## Rules
The rules this story serves are in the scheduling domain spec, referenced by id there.

## Data touched
Assignment (owned)

## Out of scope
Saved filters.
Anything the journey step does not name; no free text, no optimisation, no second team.
