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

## 2026-11-07 06:53 · review-design round 2 (pm-lead) · in progress
**Done:** DESIGN-REVIEW-2 convened with fresh reviewers (a two-agent workflow, structured findings): architect 25, developer 27, 14 blocking each, both `VERDICT: CHANGES REQUIRED`; all 52 dispositioned in design/DESIGN-REVIEW-2.md and applied as PRODUCT-DESIGN v1.2, specs v1.2, 22 stories (107 arms), IR-01..IR-11; `adu design check` and `adu stories check` green.
**Decisions (in the review table):** typed Notifier events with self-contained payloads, the emitter names recipients (A1/D5/D6); the caller resolved once by the API layer (A4, IR-11); refusal shape, not_found and precedence (A6/D8); approval after a refused transfer succeeds and returns the decision (A9/D11); "open" defined once, expired never pending (A12/D2); answer_reason and answered_at (A11/D4); list members and list weeks with the current week served by the API (A7/D14); the service cycles accepted explicitly through ports (A18/D17).
**Deviations flagged:** round 2 was heavier than round 1 in blocking findings (14 + 14 vs. the first round's, which did not grade severity) — the second reading found what the first round's fixes created (A5: implicit weeks + immutable shifts made no_shifts unconstructible). Recorded for the retro: dispositions applied independently can conflict; a round-3 read is the check.
**Tests at close:** design check and stories check green; no code yet.
**NEXT:** round 3 — fresh architect and developer reviewers on v1.2; the gate is both AGREED in the same round, then D-02.

## 2026-11-07 07:05 · review-design round 3 (pm-lead) · in progress
**Done:** DESIGN-REVIEW-3 with fresh reviewers: architect 11 findings (1 blocking: scheduling cannot name week_published's recipients — IR-12), developer 11 (1 blocking: publishing an already published week — refused week_published); both `VERDICT: CHANGES REQUIRED`; all 22 dispositioned in design/DESIGN-REVIEW-3.md and applied as PRODUCT-DESIGN v1.3 (Reason codes table with bucket and HTTP status), specs v1.3, 22 stories (108 arms), IR-01..IR-12; checks green.
**Decisions:** the status mapping by bucket (401/403/404/409/422); within-bucket order = the arms' order; credentials verified before the active check; one decide operation; the seed emits nothing; the same-role change is a no-op.
**Deviations flagged:** none. The rounds are converging: 56 → 52 → 22 findings, 28 → 2 blocking.
**Tests at close:** design check and stories check green; no code yet.
**NEXT:** round 4 — fresh reviewers on v1.3; both AGREED closes the gate and records D-02.

## 2026-11-07 07:18 · review-design round 4 (pm-lead) · in progress
**Done:** DESIGN-REVIEW-4 with fresh reviewers: architect 13 (3 blocking), developer 15 (2 blocking; one shared), both `VERDICT: CHANGES REQUIRED`; all 28 dispositioned and applied as PRODUCT-DESIGN v1.4, specs v1.4, IR-07 widened; checks green.
**Decisions:** holder-rows carry pending and requestable, both computed by swaps (one owner for the 24-hour rule); the state bucket orders the target's own state first across stories; counterpart checks self → inactive → on_shift; swap_refused drops an inactive party; one answer operation; invalid_request for shape failures.
**Deviations flagged:** three of the four blocking findings were created by round-3 fixes (the within-bucket order rule; the request control). Recorded for the retro: every rule added to settle one guess should be re-read against the arms it touches before the round closes.
**Tests at close:** design check and stories check green; no code yet.
**NEXT:** round 5 — fresh reviewers on v1.4; both AGREED closes the gate and records D-02.

## 2026-11-07 07:35 · review-design round 5 (pm-lead) · in progress
**Done:** DESIGN-REVIEW-5 with fresh reviewers: architect 13 (3 blocking), developer 8 (2 blocking), the three distinct blocking findings raised by both; both `VERDICT: CHANGES REQUIRED`; all 21 dispositioned and applied as PRODUCT-DESIGN v1.5, specs v1.5, IR-07 restated exactly; Q-02 and Q-03 opened as purpose questions for the operator (not blocking); checks green.
**Decisions:** invalid_request only for an unreadable body, the domain enumerates role and reason codes; the state bucket leads with exactly week_published, week_draft (request), wrong_state; IR-07: scheduling passes facts, swaps computes pending and requestable; one request row (R-swaps-09) for every swap write and list.
**Deviations flagged:** none.
**Tests at close:** design check, stories check and ledger lint green; no code yet.
**NEXT:** round 6 — fresh reviewers on v1.5; both AGREED closes the gate and records D-02.

## 2026-11-07 07:59 · review-design round 6 (pm-lead) · in progress
**Done:** DESIGN-REVIEW-6 with fresh reviewers: developer `VERDICT: AGREED` (14 cosmetic findings), architect `VERDICT: CHANGES REQUIRED` (7, one blocking: deactivating an already inactive member); all 21 dispositioned and applied as PRODUCT-DESIGN v1.6, specs v1.6, IR-01/06/09 restated; checks green. Both repositories now have a GitHub remote; main is pushed after every commit.
**Decisions:** a repeated deactivation is refused member_inactive and emits nothing; counterpart_overlap is checked at request time as well as at transfer; the API reads bodies leniently so that earlier buckets answer first.
**Deviations flagged:** none.
**Tests at close:** design check, stories check and ledger lint green; no code yet.
**NEXT:** round 7 — fresh reviewers on v1.6; both AGREED closes the gate and records D-02.

## 2026-11-07 08:16 · review-design (pm-lead) · done
**Done:** DESIGN-REVIEW-7: both reviewers `VERDICT: AGREED` in the same round — the gate. 16 cosmetic findings applied as PRODUCT-DESIGN v1.7, specs v1.7; D-02 recorded. Seven rounds in all: 56 → 52 → 22 → 28 → 21 → 21 → 16 findings; blocking 28 (ungraded) → 14+14 → 2 → 4 → 3 → 1 → 0; 155 findings dispositioned, none declined, every one in a review file with where it landed.
**Decisions:** D-02 (the agreed design). Q-02 and Q-03 stay open for the operator, not blocking.
**Deviations flagged:** the skill's brief had no severity grading; rounds converged only after the brief defined blocking vs cosmetic (round 3 on) — package feedback FB-02, FB-11, FB-12.
**Tests at close:** design check, stories check, ledger lint, audit green; no code yet.
**NEXT:** `claude --agent adu-lifecycle:architect` then /adu-lifecycle:design-architecture.
