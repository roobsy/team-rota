---
id: US-identity-001
title: Admin adds a member and sees the team list
domain: identity
persona: Avi
journey: J-01
step: 2
roles: [admin, planner, member]
data: [Member, Role]
arms:
  - { arm: "a member added with name, email, role and passcode appears in the team list as active", kind: deterministic }
  - { arm: "adding a member with an email already on the team (compared case-insensitively) is refused with reason duplicate_email", kind: deterministic }
  - { arm: "adding a member with a role outside admin, planner, member is refused with reason invalid_role", kind: deterministic }
  - { arm: "a planner or member calling the add action is refused with reason forbidden", kind: deterministic }
  - { arm: "any signed-in caller lists the members with id, name, role and active only (never passcode or token), ordered by name (compared case-insensitively) then id ascending; an operation naming a member id that names nobody is refused not_found", kind: deterministic }
  - { arm: "the Team screen's member-add form submits and the new member appears in team-list with its role and active state; the form is shown to admins only", kind: deterministic }
---
## Story
As an admin, I want to add a member with a role and a passcode so that they can be assigned and can sign in; as anyone, I want to see who is on the team.

## Rules
The rules this story serves are in the identity domain spec, referenced by id there.

## Data touched
Member, Role (owned)

## Out of scope
Invitations, passcode resets, bulk import. (Roles: arms 1–4 and 6 are the admin's; arm 5, the list, is every role's.)
Anything the journey step does not name; no free text, no optimisation, no second team.
