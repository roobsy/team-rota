---
id: US-swaps-001
title: Member requests a swap
domain: swaps
persona: Mo
journey: J-04
step: 1
roles: [admin, planner, member]
data: [SwapRequest, Assignment, Shift, Week, Member]
arms:
  - { arm: "a request for an assignment the member holds on a published week, naming an eligible counterpart and a reason code, is recorded in state requested with created_at from the clock, and the response is the request row of R-swaps-09", kind: deterministic }
  - { arm: "a request for an assignment the member does not hold is refused with reason not_holder", kind: deterministic }
  - { arm: "a request at or after the shift's deadline (24 hours before the shift's start instant, by the clock) is refused with reason past_deadline", kind: deterministic }
  - { arm: "a second request for the same assignment while one is open is refused with reason request_open", kind: deterministic }
  - { arm: "a request on an assignment of a draft week is refused with reason week_draft", kind: deterministic }
  - { arm: "a counterpart who is the requester, is inactive, or already holds a slot on that shift is refused with reason counterpart_self, counterpart_inactive or counterpart_on_shift respectively, checked in that order", kind: deterministic }
  - { arm: "a request without a reason code is refused with reason reason_required; one outside the enumerated codes with reason invalid_reason", kind: deterministic }
  - { arm: "the swap-request-form offers as swap-counterpart the eligible members by name (active, not the requester, not holding a slot on that shift — composed in the browser from the members list and the board; the server refuses the rest), submits, and the inbox shows the new request with swap-state requested; holder-request-swap on the member's own holder-row opens the form for that assignment", kind: deterministic }
---
## Story
As a member, I want to request a swap with a counterpart and a reason so that I can hand over a shift I cannot work.

## Rules
The rules this story serves are in the swaps domain spec, referenced by id there.

## Data touched
SwapRequest (owned); Assignment (read through scheduling's interface), Shift (read through scheduling's interface), Week (read through scheduling's interface), Member (read through identity's interface)

## Out of scope
Free-text reasons, open calls to anyone, partial shifts. Withdrawal or cancellation by the requester (a request ends only by the counterpart's answer, a decision or expiry — a deliberate omission in this version).
Anything the journey step does not name; no free text, no optimisation, no second team.
