---
id: US-swaps-004
title: Member sees their requests
domain: swaps
persona: Mo
journey: J-05
step: 1
roles: [admin, planner, member]
data: [SwapRequest]
arms:
  - { arm: "every request where the member is requester or counterpart, in every state, is listed newest first by created_at, each with its state and the party awaited: counterpart while requested, decider while accepted, none otherwise", kind: deterministic }
  - { arm: "a request in state requested or accepted whose deadline has passed by the clock is shown expired, never pending; nothing is stored and nobody is notified", kind: deterministic }
  - { arm: "the inbox lists them with swap-state and swap-awaiting", kind: deterministic }
---
## Story
As a member, I want to see my requests and who is holding them up so that nothing is hidden.

## Rules
The rules this story serves are in the swaps domain spec, referenced by id there.

## Data touched
SwapRequest (owned)

## Out of scope
Archiving, search.
Anything the journey step does not name; no free text, no optimisation, no second team.
