---
id: US-notifications-004
title: Both members are told the outcome
domain: notifications
persona: Mo
journey: J-04
step: 7
roles: [admin, planner, member]
data: [Notification, SwapRequest, Decision]
arms:
  - { arm: "on approval both members receive one notification naming the shift and the new holder", kind: deterministic }
  - { arm: "on refusal both members receive one notification carrying the reason code, including counterpart_overlap and counterpart_inactive", kind: deterministic }
---
## Story
As a member, I want to be told the outcome, with the reason when refused, so that nothing pending looks done.

## Rules
The rules this story serves are in the notifications domain spec, referenced by id there.

## Data touched
Notification (owned); SwapRequest (read through swaps's interface), Decision (read through swaps's interface)

## Out of scope
Appeals.
Anything the journey step does not name; no free text, no optimisation, no second team.
