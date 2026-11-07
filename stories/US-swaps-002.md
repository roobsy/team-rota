---
id: US-swaps-002
title: Counterpart accepts or declines
domain: swaps
persona: Mo
journey: J-04
step: 3
roles: [admin, planner, member]
data: [SwapRequest]
arms:
  - { arm: "the counterpart's accept moves the request to accepted; a decline moves it to declined with the reason code", kind: deterministic }
  - { arm: "anyone but the counterpart answering is refused with reason not_counterpart", kind: deterministic }
  - { arm: "answering a request that is not in state requested is refused with reason wrong_state", kind: deterministic }
---
## Story
As a counterpart, I want to accept or decline so that the request moves or ends.

## Rules
See design/domains/swaps/spec.md — the rules this story serves are referenced by id there.

## Data touched
SwapRequest (owned by swaps)

## Out of scope
Anything the journey step does not name; no free text, no optimisation, no second team.
