---
id: US-scheduling-006
title: Transfer moves the assignment
domain: scheduling
persona: Pat
journey: J-04
step: 6
roles: [admin, planner]
data: [Assignment, Member]
arms:
  - { arm: "a transfer requested by swaps through the scheduling interface makes the counterpart the assignment's holder and the board shows it", kind: deterministic }
  - { arm: "a transfer whose counterpart would then hold an overlapping shift is refused with reason counterpart_overlap and the assignment is unchanged", kind: deterministic }
  - { arm: "a transfer whose counterpart is inactive is refused with reason counterpart_inactive and the assignment is unchanged", kind: deterministic }
---
## Story
As a member, I want the approved swap reflected on the board so that the roster is the truth. The transfer is internal: it is reached only through the scheduling interface by the decider's approval, never by a call of its own.

## Rules
The rules this story serves are in the scheduling domain spec, referenced by id there.

## Data touched
Assignment (owned); Member (read through identity's interface)

## Out of scope
An operation of its own in the API.
Anything the journey step does not name; no free text, no optimisation, no second team.
