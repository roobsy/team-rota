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
  - { arm: "the board lists every shift of the week in date, start then shift id order, each holder as a holder-row ordered by assignment id ascending with assignment id, member id, name (an inactive holder still listed), pending (requested, accepted or absent) and requestable; requestable is true only for the caller's own row on a published week while now < the deadline by the injected clock and no request is open on it — computed by swaps (IR-07), never in the browser — and holder-request-swap is shown exactly on requestable rows", kind: deterministic }
  - { arm: "each holder-row shows its pending value as holder-pending-badge with the text requested or accepted; an assignment whose requests are all declined, refused, approved or expired shows none (open as defined once in R-swaps-06, answered by swaps)", kind: deterministic }
  - { arm: "the board of a draft week is returned to planners and admins only (board-draft shows Not published yet); a member is refused with reason week_draft", kind: deterministic }
  - { arm: "any signed-in caller lists the weeks, newest first by start_date, each with its state — members see published weeks only — together with the current week: the latest published week whose start_date is on or before today by the clock, or none (board-none shows No week yet); the browser never computes it; week-picker offers the listed weeks and selecting one shows its board", kind: deterministic }
  - { arm: "the p95 server-side response time of the board operation over the seeded fixture of R-scheduling-09 (seed 20261107), 50 sequential calls through the in-process test client after 5 untimed warm-ups, p95 by nearest rank: pass at or below 300 ms; above 300 up to 350 ms reported as within tolerance; above 350 ms red — called by the fixture's start_date with mine unset, as the fixture's admin; in the timing tier, reported, never gating (within tolerance passes and is reported as such; red fails the timing arm)", kind: quantitative, statistic: p95_ms, threshold: 300, n: 50, seed: 20261107, tolerance: "50 ms", tier: timing }
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
