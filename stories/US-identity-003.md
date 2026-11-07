---
id: US-identity-003
title: Admin deactivates a member
domain: identity
persona: Avi
journey: J-01
step: 4
roles: [admin]
data: [Member, Assignment, Week, SwapRequest]
arms:
  - { arm: "a deactivated member stays in the team list with active false; their past assignments remain on the board and their swap requests remain in the inbox", kind: deterministic }
  - { arm: "a deactivated member cannot sign in (reason member_inactive)", kind: deterministic }
  - { arm: "deactivating a member who holds an assignment in a published week whose start_date is after the clock's today is refused with reason future_assignments", kind: deterministic }
  - { arm: "deactivating the last active admin is refused with reason last_admin", kind: deterministic }
  - { arm: "a planner or member calling the action is refused with reason forbidden", kind: deterministic }
---
## Story
As an admin, I want to deactivate a member so that they are no longer assigned or signed in while their history stays.

## Rules
The rules this story serves are in the identity domain spec, referenced by id there.

## Data touched
Member (owned); Assignment (read through scheduling's interface), Week (read through scheduling's interface), SwapRequest (read through swaps's interface)

## Out of scope
Reactivation, deletion.
Anything the journey step does not name; no free text, no optimisation, no second team.
