---
id: US-swaps-004
title: Member sees their requests
domain: swaps
persona: Mo
journey: J-05
step: 1
roles: [admin, planner, member]
data: [SwapRequest, Decision, Shift, Member]
arms:
  - { arm: "every request where the member is requester or counterpart, in every state, is listed newest first by created_at then id descending, each with its shift's date and start, the other party's name, its state, its answer_reason and its decision when one exists, and the party awaited: counterpart while open in requested, decider while open in accepted, none otherwise", kind: deterministic }
  - { arm: "a request in state requested or accepted whose deadline has passed by the clock is shown expired, never pending; nothing is stored and nobody is notified", kind: deterministic }
  - { arm: "a request whose other party is inactive is still listed", kind: deterministic }
  - { arm: "the inbox lists them with swap-state, swap-awaiting and swap-decision", kind: deterministic }
---
## Story
As a member, I want to see my requests and who is holding them up so that nothing is hidden.

## Rules
The rules this story serves are in the swaps domain spec, referenced by id there.

## Data touched
SwapRequest, Decision (owned); Shift (read through scheduling's interface, IR-01); Member (read through identity's interface, IR-09)

## Out of scope
Archiving, search.
Anything the journey step does not name; no free text, no optimisation, no second team.
