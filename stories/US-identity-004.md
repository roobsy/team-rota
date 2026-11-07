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
  - { arm: "an active member who signs in with their email and passcode receives a token, and every later operation carrying it acts as that member", kind: deterministic }
  - { arm: "a wrong passcode or an unknown email is refused with reason invalid_credentials (one reason for both)", kind: deterministic }
  - { arm: "an inactive member is refused with reason member_inactive", kind: deterministic }
  - { arm: "any operation other than sign-in without a valid token is refused with reason unauthenticated", kind: deterministic }
  - { arm: "the sign-in screen's form submits and lands the member on the week board", kind: deterministic }
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
