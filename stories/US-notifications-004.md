---
id: US-notifications-004
title: Both members are told the outcome
domain: notifications
persona: Mo
journey: J-04
step: 7
roles: [admin, planner, member]
data: [Notification]
arms:
  - { arm: "on approval (swap_approved) both members receive one notification naming the shift's date and start and the new holder's name", kind: deterministic }
  - { arm: "on refusal (swap_refused) the requester and, when still active, the counterpart receive one notification carrying the reason code (fairness, coverage, policy, other, counterpart_overlap or counterpart_inactive); with counterpart_inactive only the requester receives it, since the counterpart is inactive (R-notifications-03)", kind: deterministic }
---
## Story
As a member, I want to be told the outcome, with the reason when refused, so that nothing pending looks done.

## Rules
The rules this story serves are in the notifications domain spec, referenced by id there.

## Data touched
Notification (owned)

## Out of scope
Appeals.
Anything the journey step does not name; no free text, no optimisation, no second team.
