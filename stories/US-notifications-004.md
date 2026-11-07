---
id: US-notifications-004
title: Both members are told the outcome
domain: notifications
persona: Mo
journey: J-04
step: 7
roles: [admin, planner, member]
data: [Notification, SwapRequest, Approval]
arms:
  - { arm: "on approval both members receive one notification naming the shift and the new holder", kind: deterministic }
  - { arm: "on refusal both members receive one notification carrying the reason code", kind: deterministic }
---
## Story
As a member, I want to be told the outcome, with the reason when refused, so that nothing pending looks done.

## Rules
See design/domains/notifications/spec.md — the rules this story serves are referenced by id there.

## Data touched
Notification, SwapRequest, Approval (owned by notifications; others read through an interface)

## Out of scope
Anything the journey step does not name; no free text, no optimisation, no second team.
