---
id: US-notifications-002
title: Counterpart is told of the request
domain: notifications
persona: Mo
journey: J-04
step: 2
roles: [admin, planner, member]
data: [Notification, SwapRequest]
arms:
  - { arm: "the counterpart receives one notification naming the shift, the requester and the reason code", kind: deterministic }
  - { arm: "nobody else is notified at this step", kind: deterministic }
---
## Story
As a counterpart, I want to be told of a request so that I can answer it.

## Rules
The rules this story serves are in the notifications domain spec, referenced by id there.

## Data touched
Notification (owned); SwapRequest (read through swaps's interface)

## Out of scope
Reminders.
Anything the journey step does not name; no free text, no optimisation, no second team.
