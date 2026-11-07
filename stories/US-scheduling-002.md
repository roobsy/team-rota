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
  - { arm: "assigning a member to a shift overlapping one they hold is refused with reason overlapping_shift", kind: deterministic }
  - { arm: "assigning to a full shift is refused with reason shift_full", kind: deterministic }
---
## Story
As a planner, I want to assign members to shifts so that every slot has a holder.

## Rules
See design/domains/scheduling/spec.md — the rules this story serves are referenced by id there.

## Data touched
Shift, Assignment, Member (owned by scheduling; others read through an interface)

## Out of scope
Anything the journey step does not name; no free text, no optimisation, no second team.
