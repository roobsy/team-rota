---
id: US-identity-001
title: Admin adds a member
domain: identity
persona: Avi
journey: J-01
step: 1
roles: [admin]
data: [Member, Role]
arms:
  - { arm: "a member added with name, email and role member appears in the team list as active", kind: deterministic }
  - { arm: "adding a member with an email already on the team is refused with reason duplicate_email", kind: deterministic }
  - { arm: "a planner or member calling the action is refused with reason forbidden", kind: deterministic }
---
## Story
As an admin, I want to add a member with a role so that they can be assigned and can sign in.

## Rules
See design/domains/identity/spec.md — the rules this story serves are referenced by id there.

## Data touched
Member, Role (owned by identity)

## Out of scope
Anything the journey step does not name; no free text, no optimisation, no second team.
