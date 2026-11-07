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
  - { arm: "a shift created with date, start, end and slots in the week named by its Monday start_date appears in that week, which comes into being in state draft with its first shift", kind: deterministic }
  - { arm: "a start_date that is not a Monday is refused with reason not_week_start", kind: deterministic }
  - { arm: "a shift whose date is not within the week's seven days is refused with reason outside_week", kind: deterministic }
  - { arm: "a shift whose end is not after its start (times of day on the shift's date; a shift never crosses midnight) is refused with reason invalid_interval", kind: deterministic }
  - { arm: "a shift with fewer than one slot is refused with reason invalid_slots", kind: deterministic }
  - { arm: "a member calling the action is refused with reason forbidden", kind: deterministic }
---
## Story
As a planner, I want to create the shifts of a week so that the week can be staffed.

## Rules
The rules this story serves are in the scheduling domain spec, referenced by id there.

## Data touched
Week, Shift (owned)

## Out of scope
Editing or deleting a shift (shifts are immutable once created in this version), templates, recurring weeks.
Anything the journey step does not name; no free text, no optimisation, no second team.
