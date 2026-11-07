# SESSION-JOURNAL — Team Rota
Append-only, newest last; never edit an earlier block. Every session appends exactly one block before it ends — done, blocked or interrupted — and appends it **before** the gate runs, because a session that dies during the gate cannot write it afterwards.

Block format:
```
## YYYY-MM-DD HH:MM · ADU-nn (or: Defect session FB-nn · verification R<n> · design-change loop · closure) · done | in progress | blocked
**Done:** files and behaviours, as bullets.
**Decisions:** each with the design section or D-nn that justifies it.
**Deviations flagged:** Q-nn, or "none".
**Tests at close:** N passed, M failed · lint clean (filled after the gate; "pending" until then).
**NEXT:** the single most specific next action — a file and a behaviour, not a topic.
```
A recorded approval (hard rule 1, 4 or 6) is a paragraph in the block of the session that granted it: file, lines, what was permitted, the measurement. An approval that lives only on a branch or in a chat has not happened.

## 2026-11-07 06:18 · bootstrap · done
**Done:** `adu scaffold --name "Team Rota" --adapter python-fastapi-uv,react-vite-vitest --profile toy`; `adu init --check` green; derived blocks rendered.
**Decisions:** adapters python-fastapi-uv + react-vite-vitest (the stack the operator chose on 2026-11-07); profile toy (gate budget 300 s).
**Deviations flagged:** none.
**Tests at close:** none yet (ADU-00 brings the first).
**NEXT:** pm-lead session: /adu-lifecycle:discover → design/PRODUCT-BRIEF.md approved and pinned.

## 2026-11-07 06:18 · discover (pm-lead) · done
**Done:** design/PRODUCT-BRIEF.md v1.0 — purpose, three personas, the North Star, four never-becomes, non-goals, success; approved by the operator; pinned (`adu pins add`); D-01 appended; CLAUDE.md identity lines filled from the brief; VERSIONS row.
**Decisions:** D-01 (the brief is the fixed point of purpose).
**Deviations flagged:** none. The discovery questions were answered from the operator's own description of the product (a shift roster with planner/member/admin roles, swaps with approval, a weekly board) — recorded here so the example states its source.
**Tests at close:** none yet.
**NEXT:** pm-lead session: /adu-lifecycle:design-product → design/PRODUCT-DESIGN.md v1.0 with `adu design check` green.

## 2026-11-07 06:19 · design-product (pm-lead) · done
**Done:** design/PRODUCT-DESIGN.md v1.0 — three personas, five journeys (J-01..J-05, 18 steps each naming its domain), five screens with anchors, four domains (identity, scheduling, swaps, notifications), eight entities with one owner each, three roles, the permissions matrix; `adu design check` green.
**Decisions:** Q-01 ruled — the admin approves a swap the planner is party to (segregation of duties; becomes R-swaps-05); the board shows pending swaps on their shifts (North Star: nothing pending hidden).
**Deviations flagged:** none.
**Tests at close:** none yet.
**NEXT:** pm-lead session: /adu-lifecycle:write-stories (recruit pm-swaps first, --reason segregation) → 18 stories, four specs, `adu stories check` green.

## 2026-11-07 06:20 · write-stories (pm-lead, pm-swaps) · done
**Done:** `adu recruit swaps --reason segregation` (pm-swaps rendered to .claude/agents/pm-swaps.md, DOMAIN-REGISTER row, fence design/domains/swaps/**, stories/US-swaps-*.md — proven: an edit outside the fence is refused by the guard); 18 stories (one per journey step; 46 arms, one quantitative with its five parameters) and four domain specs (21 rules); four INTERFACE-REQUEST rows; `adu stories check` green: 18 stories cover 18 steps.
**Recruited:** pm-swaps (segregation: approvers must not design the rules they approve under).
**Decisions:** reason codes enumerated in R-swaps-07; the swap deadline is 24 h before the shift (R-swaps-01) — a design choice recorded in the spec, to be confirmed in review.
**Deviations flagged:** none.
**Tests at close:** none yet.
**NEXT:** pm-lead session: /adu-lifecycle:review-design → architect and developer subagents in parallel, DESIGN-REVIEW-1.

## 2026-11-07 06:36 · review-design round 1 (pm-lead) · in progress
**Done:** DESIGN-REVIEW-1 convened: architect and developer as parallel independent subagents (fresh contexts, the brief and nothing else); 25 + 31 findings, both `VERDICT: CHANGES REQUIRED`; all 56 dispositioned in design/DESIGN-REVIEW-1.md (none declined; 14 were the same point raised twice); applied as PRODUCT-DESIGN v1.1 (22 journey steps), 22 stories, specs v1.1, IR-01..IR-10; `adu design check` and `adu stories check` green.
**Decisions (recorded in the review, not in chat):** sign-in = email + passcode → bearer token (A1/D1); first admin seeded by an operator command (A2); weeks implicit from a Monday (A3/D3); approval atomic, transfer first, the system records a refused Decision on counterpart_overlap / counterpart_inactive (A5/D4/D5); expiry derived on read, never stored or notified (A6/D9); any non-party admin or planner decides (A7, generalising Q-01); R-notifications-01 enumerated and widened with account-change stories rather than narrowing brief §4 (A14); the quantitative arm fixed to a seeded fixture, server-side p95, timing tier (A15/D6).
**Deviations flagged:** the swaps rows were applied by the lead on pm-swaps' behalf (the lead convenes the review; the fence binds the pm-swaps agent, not the lead) — recorded here so segregation stays visible.
**Tests at close:** design check and stories check green; no code yet.
**NEXT:** round 2 — fresh architect and developer reviewers on v1.1; the gate is both AGREED in the same round, then D-02.
