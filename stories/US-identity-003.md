---
id: US-identity-003
title: Admin deactivates a member
domain: identity
persona: Avi
journey: J-01
step: 3
roles: [admin]
data: [Member, Assignment]
arms:
  - { arm: "a deactivated member keeps their history and is shown inactive", kind: deterministic }
  - { arm: "a deactivated member cannot be assigned to a shift (reason member_inactive)", kind: deterministic }
  - { arm: "deactivating a member with an assignment in a published future week is refused with reason future_assignments", kind: deterministic }
---
## Story
As an admin, I want to deactivate a member so that they are no longer assigned while their history stays.

## Rules
See design/domains/identity/spec.md — the rules this story serves are referenced by id there.

## Data touched
Member, Assignment (owned by identity; others read through an interface)

## Out of scope
Anything the journey step does not name; no free text, no optimisation, no second team.
