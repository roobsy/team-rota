---
id: US-scheduling-002
title: Planner assigns members to shifts
domain: scheduling
persona: Pat
journey: J-02
step: 2
roles: [admin, planner]
data: [Shift, Assignment, Member]
arms:
  - { arm: "an active member assigned to a shift with a free slot holds it", kind: deterministic }
  - { arm: "assigning a member twice to one shift is refused with reason already_assigned", kind: deterministic }
  - { arm: "assigning a member to a shift whose half-open interval [start, end) intersects one they hold on the same date is refused with reason overlapping_shift", kind: deterministic }
  - { arm: "assigning to a shift whose slots are all held is refused with reason shift_full (the assign order is week_published, already_assigned, overlapping_shift, shift_full, member_inactive)", kind: deterministic }
  - { arm: "assigning an inactive member is refused with reason member_inactive", kind: deterministic }
  - { arm: "removing an assignment from a shift of a draft week frees the slot; in a published week it is refused with reason week_published", kind: deterministic }
  - { arm: "a member calling the action is refused with reason forbidden", kind: deterministic }
  - { arm: "the Week board's shift-assign control assigns a member chosen from the members list and the holder-row appears; shift-unassign removes it while the week is a draft", kind: deterministic }
---
## Story
As a planner, I want to assign members to shifts, and undo a mistake while the week is a draft, so that every slot has a holder.

## Rules
The rules this story serves are in the scheduling domain spec, referenced by id there.

## Data touched
Shift, Assignment (owned); Member (read through identity's interface)

## Out of scope
Auto-assignment, fairness scoring, availability.
Anything the journey step does not name; no free text, no optimisation, no second team.
