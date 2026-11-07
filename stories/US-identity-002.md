---
id: US-identity-002
title: Admin changes a member's role
domain: identity
persona: Avi
journey: J-01
step: 3
roles: [admin]
data: [Member, Role]
arms:
  - { arm: "a member's role changes to the named role and the change is visible in the team list", kind: deterministic }
  - { arm: "changing the last active admin to another role is refused with reason last_admin", kind: deterministic }
  - { arm: "changing to a role outside admin, planner, member is refused with reason invalid_role", kind: deterministic }
  - { arm: "a planner or member calling the action is refused with reason forbidden", kind: deterministic }
  - { arm: "a change to the role the member already holds changes nothing and emits nothing; an inactive member's role may be changed and nobody is notified", kind: deterministic }
  - { arm: "the Team screen's member-role control changes the role shown in team-list", kind: deterministic }
---
## Story
As an admin, I want to change a member's role so that duties follow people, not accounts.

## Rules
The rules this story serves are in the identity domain spec, referenced by id there.

## Data touched
Member, Role (owned)

## Out of scope
Role history.
Anything the journey step does not name; no free text, no optimisation, no second team.
