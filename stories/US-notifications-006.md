---
id: US-notifications-006
title: Member is told of changes to their account
domain: notifications
persona: Mo
journey: J-01
step: 6
roles: [admin, planner, member]
data: [Notification]
arms:
  - { arm: "an added member receives one notification (member_added) naming their role", kind: deterministic }
  - { arm: "a member whose role changed receives one notification (role_changed) naming the new role", kind: deterministic }
  - { arm: "a deactivated member receives one notification (member_deactivated), the one event that reaches an inactive recipient; it is verified through the notifications read model since the member can no longer sign in", kind: deterministic }
  - { arm: "nobody else is notified of these three events", kind: deterministic }
---
## Story
As a member, I want to be told when I am added, my role changes or I am deactivated so that no change to my account is silent.

## Rules
The rules this story serves are in the notifications domain spec, referenced by id there.

## Data touched
Notification (owned)

## Out of scope
Email or push delivery; the product records notifications, the screen shows them.
Anything the journey step does not name; no free text, no optimisation, no second team.
