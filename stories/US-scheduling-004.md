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
  - { arm: "a shift with a pending swap shows a pending badge naming the state, never an approved look", kind: deterministic }
  - { arm: "the board for a draft week is visible to planners and admins only (reason week_draft for members)", kind: deterministic }
  - { arm: "the board renders within budget", kind: quantitative, statistic: p95_ms, threshold: 300, n: 50, seed: 20261107, tolerance: "50 ms" }
---
## Story
As a member, I want to see the week board so that I know who holds every shift and what is pending.

## Rules
See design/domains/scheduling/spec.md — the rules this story serves are referenced by id there.

## Data touched
Week, Shift, Assignment, SwapRequest (owned by scheduling; others read through an interface)

## Out of scope
Anything the journey step does not name; no free text, no optimisation, no second team.
