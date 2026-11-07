---
id: US-scheduling-004
title: Member opens the week board
domain: scheduling
persona: Mo
journey: J-03
step: 1
roles: [admin, planner, member]
data: [Week, Shift, Assignment]
arms:
  - { arm: "the board lists every shift of the week in date, start then shift id order, each holder as a holder-row with member id and name (a shift held by an inactive member still lists them); the caller's own holder-rows of a published week carry holder-request-swap while now < the deadline", kind: deterministic }
  - { arm: "each holder-row carries the open request on that assignment as holder-pending-badge with the text requested or accepted; an assignment whose requests are all declined, refused, approved or expired carries none (open as defined once in R-swaps-06, answered by swaps)", kind: deterministic }
  - { arm: "the board of a draft week is returned to planners and admins only (board-draft shows Not published yet); a member is refused with reason week_draft", kind: deterministic }
  - { arm: "any signed-in caller lists the weeks, newest first by start_date, each with its state — members see published weeks only — together with the current week: the latest published week whose start_date is on or before today by the clock, or none (board-none shows No week yet); the browser never computes it", kind: deterministic }
  - { arm: "the p95 server-side response time of the board operation over the seeded fixture of R-scheduling-09 (seed 20261107), 50 sequential calls through the in-process test client after 5 untimed warm-ups, p95 by nearest rank: pass at or below 300 ms; above 300 up to 350 ms reported as within tolerance; above 350 ms red — called by the fixture's start_date with mine unset, as the fixture's admin; in the timing tier, reported, never gating", kind: quantitative, statistic: p95_ms, threshold: 300, n: 50, seed: 20261107, tolerance: "50 ms", tier: timing }
---
## Story
As a member, I want to see the week board so that I know who holds every shift and what is pending.

## Rules
The rules this story serves are in the scheduling domain spec, referenced by id there.

## Data touched
Week, Shift, Assignment (owned)

## Out of scope
Month views, printing, colour themes.
Anything the journey step does not name; no free text, no optimisation, no second team.
