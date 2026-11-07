---
id: US-notifications-003
title: Requester and planner are told of the answer
domain: notifications
persona: Pat
journey: J-04
step: 4
roles: [admin, planner, member]
data: [Notification, SwapRequest]
arms:
  - { arm: "on accept the requester and every planner receive one notification naming the request and its state accepted", kind: deterministic }
  - { arm: "on decline only the requester is notified, with the reason", kind: deterministic }
---
## Story
As the requester and as the planner, we want to be told of the counterpart's answer so that approval can follow.

## Rules
See design/domains/notifications/spec.md — the rules this story serves are referenced by id there.

## Data touched
Notification, SwapRequest (owned by notifications; others read through an interface)

## Out of scope
Anything the journey step does not name; no free text, no optimisation, no second team.
