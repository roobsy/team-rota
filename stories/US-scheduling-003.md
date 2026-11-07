---
id: US-scheduling-003
title: Planner publishes the week
domain: scheduling
persona: Pat
journey: J-02
step: 3
roles: [admin, planner]
data: [Week, Shift, Assignment]
arms:
  - { arm: "a draft week with every slot filled becomes published", kind: deterministic }
  - { arm: "publishing a week with an empty slot is refused with reason unfilled_slots and the slots are listed", kind: deterministic }
  - { arm: "creating or editing a shift of a published week is refused with reason week_published", kind: deterministic }
---
## Story
As a planner, I want to publish the week so that it becomes the truth everyone sees.

## Rules
See design/domains/scheduling/spec.md — the rules this story serves are referenced by id there.

## Data touched
Week, Shift, Assignment (owned by scheduling)

## Out of scope
Anything the journey step does not name; no free text, no optimisation, no second team.
