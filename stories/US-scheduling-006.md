---
id: US-scheduling-006
title: Transfer moves the assignment
domain: scheduling
persona: Pat
journey: J-04
step: 6
roles: []
data: [Assignment, Member]
arms:
  - { arm: "a transfer requested by swaps through the scheduling interface, inside the caller's transaction, makes the counterpart the assignment's holder and the board shows it", kind: deterministic }
  - { arm: "a transfer whose counterpart would then hold an overlapping shift — a slot on the same shift counts — is refused with reason counterpart_overlap and the assignment is unchanged", kind: deterministic }
  - { arm: "a transfer whose counterpart is inactive is refused with reason counterpart_inactive and the assignment is unchanged", kind: deterministic }
  - { arm: "no HTTP route performs a transfer (asserted against the served route table); the interface is called directly in scheduling's tests", kind: deterministic }
---
## Story
As the roster, I move the assignment to the counterpart when a decider approves, so that the board is the truth. The transfer is internal: reached only through the scheduling interface by the decider's approval; Mo is the beneficiary, nobody is the caller.

## Rules
The rules this story serves are in the scheduling domain spec, referenced by id there.

## Data touched
Assignment (owned); Member (read through identity's interface)

## Out of scope
An operation of its own in the API.
Anything the journey step does not name; no free text, no optimisation, no second team.
