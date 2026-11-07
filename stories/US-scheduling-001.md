---
id: US-scheduling-001
title: Planner creates the shifts of a week
domain: scheduling
persona: Pat
journey: J-02
step: 1
roles: [admin, planner]
data: [Week, Shift]
arms:
  - { arm: "a shift created with date, start, end and slots appears in the draft week", kind: deterministic }
  - { arm: "a shift whose end is not after its start is refused with reason invalid_interval", kind: deterministic }
  - { arm: "a shift outside the week's seven days is refused with reason outside_week", kind: deterministic }
---
## Story
As a planner, I want to create the shifts of a week so that the week can be staffed.

## Rules
See design/domains/scheduling/spec.md — the rules this story serves are referenced by id there.

## Data touched
Week, Shift (owned by scheduling)

## Out of scope
Anything the journey step does not name; no free text, no optimisation, no second team.
