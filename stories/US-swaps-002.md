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
  - { arm: "the counterpart's accept moves the request to accepted with accepted_at from the clock; a decline moves it to declined with the reason code", kind: deterministic }
  - { arm: "anyone but the counterpart answering is refused with reason not_counterpart", kind: deterministic }
  - { arm: "answering a request that is not in state requested is refused with reason wrong_state", kind: deterministic }
  - { arm: "answering after the shift's deadline is refused with reason past_deadline", kind: deterministic }
  - { arm: "a decline without a reason code is refused with reason reason_required; one outside the enumerated codes with reason invalid_reason", kind: deterministic }
  - { arm: "the inbox shows the accept and decline controls only to the counterpart and only while the request is in state requested", kind: deterministic }
---
## Story
As a counterpart, I want to accept or decline so that the request moves or ends.

## Rules
The rules this story serves are in the swaps domain spec, referenced by id there.

## Data touched
SwapRequest (owned)

## Out of scope
Counter-proposals.
Anything the journey step does not name; no free text, no optimisation, no second team.
