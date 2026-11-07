---
id: US-swaps-002
title: Counterpart accepts or declines
domain: swaps
persona: Mo
journey: J-04
step: 3
roles: [admin, planner, member]
data: [SwapRequest, Shift, Member]
arms:
  - { arm: "accept and decline are one answer operation with an outcome: accept moves the request to accepted with answered_at from the clock and no answer_reason; decline moves it to declined with answer_reason set to the reason code (required) and answered_at from the clock", kind: deterministic }
  - { arm: "anyone but the counterpart answering is refused with reason not_counterpart", kind: deterministic }
  - { arm: "answering a request that is not in state requested is refused with reason wrong_state", kind: deterministic }
  - { arm: "answering at or after the shift's deadline is refused with reason past_deadline", kind: deterministic }
  - { arm: "a decline without a reason code is refused with reason reason_required; one outside the enumerated codes, or a reason sent with outcome accept, with reason invalid_reason", kind: deterministic }
  - { arm: "the inbox shows swap-accept, swap-decline and swap-decline-reason only to the counterpart and only while the request is open in state requested", kind: deterministic }
---
## Story
As a counterpart, I want to accept or decline so that the request moves or ends.

## Rules
The rules this story serves are in the swaps domain spec, referenced by id there.

## Data touched
SwapRequest (owned); Shift (read through scheduling's interface, IR-01); Member (read through identity's interface, IR-09)

## Out of scope
Counter-proposals.
Anything the journey step does not name; no free text, no optimisation, no second team.
