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
  - { arm: "a draft week with at least one shift and every slot filled becomes published", kind: deterministic }
  - { arm: "publishing a week with an empty slot is refused with reason unfilled_slots and the refusal lists the unfilled shifts as rows of shift id, date, start and unfilled count", kind: deterministic }
  - { arm: "publishing a week with no shifts is refused with reason no_shifts", kind: deterministic }
  - { arm: "creating a shift, assigning or unassigning in a published week is refused with reason week_published", kind: deterministic }
  - { arm: "a member calling the action is refused with reason forbidden", kind: deterministic }
---
## Story
As a planner, I want to publish the week so that it becomes the truth everyone sees.

## Rules
The rules this story serves are in the scheduling domain spec, referenced by id there.

## Data touched
Week, Shift, Assignment (owned)

## Out of scope
Unpublishing, partial publication.
Anything the journey step does not name; no free text, no optimisation, no second team.
