---
id: US-identity-003
title: Admin deactivates a member
domain: identity
persona: Avi
journey: J-01
step: 4
roles: [admin]
data: [Member, Assignment, Shift, Week]
arms:
  - { arm: "a deactivated member stays in the team list with active false and their row is not deleted", kind: deterministic }
  - { arm: "a deactivated member cannot sign in (reason member_inactive), and a token issued before deactivation is refused on the next operation with reason unauthenticated", kind: deterministic }
  - { arm: "deactivating a member who holds an assignment on any shift, draft or published week, whose start instant is after now is refused with reason future_assignments", kind: deterministic }
  - { arm: "deactivating the last active admin is refused with reason last_admin", kind: deterministic }
  - { arm: "a planner or member calling the action is refused with reason forbidden", kind: deterministic }
  - { arm: "the Team screen's member-deactivate control deactivates and team-list shows the member inactive; the refusals are shown with their reason", kind: deterministic }
---
## Story
As an admin, I want to deactivate a member so that they are no longer assigned or signed in while their row stays. (That their past assignments still show on the board and their requests in the inbox is asserted by the scheduling and swaps stories, which own those lists.)

## Rules
The rules this story serves are in the identity domain spec, referenced by id there.

## Data touched
Member (owned); Assignment (read through scheduling's interface), Shift (read through scheduling's interface), Week (read through scheduling's interface)

## Out of scope
Reactivation, deletion.
Anything the journey step does not name; no free text, no optimisation, no second team.
