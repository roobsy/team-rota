---
id: US-notifications-003
title: Requester and deciders are told of the answer
domain: notifications
persona: Pat
journey: J-04
step: 4
roles: [admin, planner, member]
data: [Notification, SwapRequest]
arms:
  - { arm: "on accept the requester and every member eligible to decide the request (every admin and planner who is not a party) receive one notification each naming the request and its state accepted", kind: deterministic }
  - { arm: "on decline only the requester is notified, with the reason code", kind: deterministic }
---
## Story
As the requester and as someone who may decide, we want to be told of the counterpart's answer so that a decision can follow.

## Rules
The rules this story serves are in the notifications domain spec, referenced by id there.

## Data touched
Notification (owned); SwapRequest (read through swaps's interface)

## Out of scope
Escalation, reminders.
Anything the journey step does not name; no free text, no optimisation, no second team.
