---
id: US-identity-005
title: Operator seeds the first admin
domain: identity
persona: Avi
journey: J-01
step: 1
roles: []
data: [Member, Role]
arms:
  - { arm: "on an empty team the seed command creates one active admin with the given name, email and passcode and prints the member id", kind: deterministic }
  - { arm: "on a team that already has any member the seed command is refused with reason team_not_empty", kind: deterministic }
  - { arm: "the seeded admin's stored passcode hash verifies the given passcode and nothing else", kind: deterministic }
---
## Story
As the operator, I want to seed the first admin with a command outside the API so that the team can be set up at all (an admin is needed to add anyone).

## Rules
The rules this story serves are in the identity domain spec, referenced by id there.

## Data touched
Member, Role (owned)

## Out of scope
No second seed, no reset, no import.
Anything the journey step does not name; no free text, no optimisation, no second team.
