---
id: US-notifications-005
title: Member reads their notifications
domain: notifications
persona: Mo
journey: J-05
step: 3
roles: [admin, planner, member]
data: [Notification]
arms:
  - { arm: "a member's own notifications are listed newest first by created_at then id descending; nobody else's are ever returned", kind: deterministic }
  - { arm: "invoking mark-read from a notification-item control marks that notification read", kind: deterministic }
  - { arm: "marking another member's notification is refused with reason not_recipient", kind: deterministic }
  - { arm: "a member with none sees the notification-empty state with the text \"Nothing yet\"", kind: deterministic }
  - { arm: "the Notifications screen lists them as notification-item rows under notification-list", kind: deterministic }
---
## Story
As a member, I want to read my notifications so that I can see what changed and when.

## Rules
The rules this story serves are in the notifications domain spec, referenced by id there.

## Data touched
Notification (owned)

## Out of scope
Deleting, muting, grouping.
Anything the journey step does not name; no free text, no optimisation, no second team.
