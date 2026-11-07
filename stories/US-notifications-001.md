---
id: US-notifications-001
title: Members are told the week is published
domain: notifications
persona: Mo
journey: J-02
step: 4
roles: [admin, planner, member]
data: [Notification]
arms:
  - { arm: "every active Member of any role receives one notification (week_published) whose text names the week's start_date, taken from the event payload", kind: deterministic }
  - { arm: "an inactive member receives none", kind: deterministic }
---
## Story
As a member, I want to be told when a week is published so that I see it the same minute.

## Rules
The rules this story serves are in the notifications domain spec, referenced by id there.

## Data touched
Notification (owned)

## Out of scope
Delivery channels.
Anything the journey step does not name; no free text, no optimisation, no second team.
