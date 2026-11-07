---
id: US-identity-001
title: Admin adds a member
domain: identity
persona: Avi
journey: J-01
step: 2
roles: [admin]
data: [Member, Role]
arms:
  - { arm: "a member added with name, email, role and passcode appears in the team list as active", kind: deterministic }
  - { arm: "adding a member with an email already on the team is refused with reason duplicate_email", kind: deterministic }
  - { arm: "adding a member with a role outside admin, planner, member is refused with reason invalid_role", kind: deterministic }
  - { arm: "a planner or member calling the action is refused with reason forbidden", kind: deterministic }
  - { arm: "the Team screen's add form submits and the new member appears in the list with its role and active state", kind: deterministic }
---
## Story
As an admin, I want to add a member with a role and a passcode so that they can be assigned and can sign in.

## Rules
The rules this story serves are in the identity domain spec, referenced by id there.

## Data touched
Member, Role (owned)

## Out of scope
Invitations, passcode resets, bulk import.
Anything the journey step does not name; no free text, no optimisation, no second team.
