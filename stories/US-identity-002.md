---
id: US-identity-002
title: Admin changes a member's role
domain: identity
persona: Avi
journey: J-01
step: 2
roles: [admin]
data: [Member, Role]
arms:
  - { arm: "a member's role changes to the named role and the change is visible in the team list", kind: deterministic }
  - { arm: "changing the last admin to another role is refused with reason last_admin", kind: deterministic }
---
## Story
As an admin, I want to change a member's role so that duties follow people, not accounts.

## Rules
See design/domains/identity/spec.md — the rules this story serves are referenced by id there.

## Data touched
Member, Role (owned by identity)

## Out of scope
Anything the journey step does not name; no free text, no optimisation, no second team.
