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
  - { arm: "a draft week with every slot filled becomes published (a week always has at least one shift, since it comes into being with its first)", kind: deterministic }
  - { arm: "publishing a week with an empty slot is refused with reason unfilled_slots and the refusal carries unfilled: a list of {shift_id, date, start, unfilled} rows in board order (date, start, then shift id)", kind: deterministic }
  - { arm: "publishing a start_date for which no week exists is refused with reason not_found", kind: deterministic }
  - { arm: "creating a shift, assigning, unassigning or publishing again in a published week is refused with reason week_published; nothing is emitted", kind: deterministic }
  - { arm: "a member calling the action is refused with reason forbidden", kind: deterministic }
  - { arm: "the Week board's week-publish control publishes and the board shows the week as published; the unfilled_slots refusal lists the shifts", kind: deterministic }
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
