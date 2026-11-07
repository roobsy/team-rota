---
id: US-scheduling-004
title: Member opens the week board
domain: scheduling
persona: Mo
journey: J-03
step: 1
roles: [admin, planner, member]
data: [Week, Shift, Assignment, SwapRequest]
arms:
  - { arm: "the board lists every shift of the week in date and start order with its holders", kind: deterministic }
  - { arm: "a shift with a request in state requested or accepted shows a badge whose text is that state; a shift whose requests are all declined, refused, approved or expired shows no badge", kind: deterministic }
  - { arm: "the board of a draft week is returned to planners and admins only; a member is refused with reason week_draft", kind: deterministic }
  - { arm: "the p95 server-side response time of the board operation over a seeded week (seed 20261107: 7 days x 3 shifts x 2 slots, 12 active members, 5 open requests), 50 sequential requests through the in-process test client, is within budget; reported in the timing tier, never gating", kind: quantitative, statistic: p95_ms, threshold: 300, n: 50, seed: 20261107, tolerance: "50 ms", tier: timing }
---
## Story
As a member, I want to see the week board so that I know who holds every shift and what is pending.

## Rules
The rules this story serves are in the scheduling domain spec, referenced by id there.

## Data touched
Week, Shift, Assignment (owned); SwapRequest (read through swaps's interface)

## Out of scope
Month views, printing, colour themes.
Anything the journey step does not name; no free text, no optimisation, no second team.
