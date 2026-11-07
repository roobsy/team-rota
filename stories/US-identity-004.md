---
id: US-identity-004
title: Member signs in
domain: identity
persona: Mo
journey: J-01
step: 5
roles: [admin, planner, member]
data: [Member]
arms:
  - { arm: "an active member who signs in with their email (matched case-insensitively, as R-identity-02 compares it) and passcode receives a token and who they are (id, name, role); every later operation carrying the token acts as that member; a new sign-in replaces the earlier token", kind: deterministic }
  - { arm: "a wrong passcode or an unknown email is refused with reason invalid_credentials (one reason for both); credentials are verified before the active check, so an inactive member with a wrong passcode gets invalid_credentials too", kind: deterministic }
  - { arm: "an inactive member is refused with reason member_inactive", kind: deterministic }
  - { arm: "each of identity's operations other than sign-in without a valid token is refused with reason unauthenticated; the rule holds for every operation of the product and is verified once by a test that walks the served route table", kind: deterministic }
  - { arm: "the sign-in-form's sign-in-email and sign-in-passcode submit via sign-in-submit and land the member on the week board for the current week served by the API", kind: deterministic }
---
## Story
As a member, I want to sign in with my email and passcode so that the roster knows who I am.

## Rules
The rules this story serves are in the identity domain spec, referenced by id there.

## Data touched
Member (owned)

## Out of scope
Password reset, sessions expiring, remember-me, more than one team.
Anything the journey step does not name; no free text, no optimisation, no second team.
