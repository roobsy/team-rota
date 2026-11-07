---
id: US-notifications-001
title: Members are told the week is published
domain: notifications
persona: Mo
journey: J-02
step: 4
roles: [admin, planner, member]
data: [Notification, Member, Week]
arms:
  - { arm: "every active member receives one notification naming the week when it is published", kind: deterministic }
  - { arm: "an inactive member receives none", kind: deterministic }
---
## Story
As a member, I want to be told when a week is published so that I see it the same minute.

## Rules
See design/domains/notifications/spec.md — the rules this story serves are referenced by id there.

## Data touched
Notification, Member, Week (owned by notifications; others read through an interface)

## Out of scope
Anything the journey step does not name; no free text, no optimisation, no second team.
