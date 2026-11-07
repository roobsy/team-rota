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

## 2026-11-07 08:17 · review-design (pm-lead) · done (completes the previous block: its files were committed here)
**Done:** the v1.7 edits, design/DESIGN-REVIEW-7.md, D-02 and the VERSIONS row that the previous block claimed were not in its commit — the edit script had failed before writing and the journal line was appended regardless (recorded as package feedback: the journal block must be generated from the diff, not typed before it). They are in this commit; Q-02 and Q-03 re-formatted to the ledger's entry format so the audit reads them.
**NEXT:** `claude --agent adu-lifecycle:architect` then /adu-lifecycle:design-architecture.

## 2026-11-07 08:17 · design-architecture (architect) · done
**Done:** design/ARCHITECTURE.md v1.0 (layers 0–6 with path prefixes, the allowed-edges law with the five ports as the only cross-domain crossings, the roster, one session and transaction per request shared by every service and the Notifier, the injected clock); tests/layering.json + tests/layering_scan.py from the adapter; the baseline generated on the empty tree (0 edges, 1 module) and the scan green; a planted swaps→scheduling import was shown to fail the scan in a scratch copy. DECISIONS D-03..D-06.
**Decisions:** D-03 stack and roster; D-04 auth; D-05 the layering law; D-06 protected paths (proposed, needs the operator since adu.toml is protected).
**Deviations flagged:** D-06 is applied only on the operator's approval; until then adu.toml keeps the adapter default.
**Tests at close:** layering scan green on the empty tree.
**NEXT:** /adu-lifecycle:design-contract (architect).

## 2026-11-07 08:17 · design-contract (architect) · done
**Done:** contracts/openapi.yaml v1.0 — 18 operations (identity 5, scheduling 6, swaps 5, notifications 2) each with operationId, x-story, x-roles, synthetic examples and explicit refusals; Spectral clean against the plugin ruleset; Prism served one request per operation plus a refusal example with zero validator errors (docs/CONTRACT-SMOKE.md). design/INTERFACES.md v1.0 — five protocols with signatures, Null implementations at the providers' future paths, the build order for the accepted cycles, the traceability table (every story action has an operation, a protocol or a CLI command; no row is empty). IR-01..IR-12 resolved. D-07.
**Decisions:** D-07 (contract style). The transfer is a protocol, never an operation (R-scheduling-08). The seed is a CLI command.
**Deviations flagged:** none.
**Tests at close:** spectral 0 errors; prism 0 validator errors.
**NEXT:** /adu-lifecycle:cut-adus (architect).

## 2026-11-07 08:17 · cut-adus (architect) · done
**Done:** ADU-PLAN v1.0 — 16 units with yaml blocks, prose rendered by `adu derived render`; `adu plan check` green with no warnings; order derived; mocks MK-01..03 registered; milestones as contiguous slices; STATUS ledger rows for ADU-01..15. D-08. The developer buildability read is recorded in docs/PLAN-REVIEW-1.md.
**Decisions:** D-08. The seed command sits in the api package (layer 4) so that the operator's path closes with M3. Two mocks that the derived order made unnecessary (Notifier for scheduling and swaps) were removed rather than kept.
**Deviations flagged:** rule 17 (first usable path by M2) — recorded in the plan and as package feedback FB-01.
**Tests at close:** plan check green; derived blocks current; ledgers OK.
**NEXT:** the operator approves the plan; then `adu handover ADU-00` and a fresh developer session for ADU-00.

## 2026-11-07 08:19 · hand-over ADU-00 (oversight) · grant
**Grant (hard rule 4, protected file):** `adu.toml [commands]` gate, fast and lint reduced to the python commands until ADU-12, per Q-04 option 1. Authority: the operator's standing instruction for this example run (execute ADU-00..02 here); the operator re-confirms this grant when they take over at ADU-03. Package feedback recorded (FB-14 in the plugin's ledger).
**NEXT:** the developer's buildability read of the plan (docs/PLAN-REVIEW-1.md), then `adu handover ADU-00` and the ADU-00 session.

## 2026-11-07 08:38 · cut-adus, the developer's read (architect) · done
**Done:** docs/PLAN-REVIEW-1.md — the developer subagent's buildability read of plan v1.0: 23 findings (15 blocking), all accepted; one proposed fix replaced (finding 13: the contract gains MemberSummary rather than the agreed design gaining email). ADU-PLAN v1.1: 18 units — ADU-16 (ports, Nulls, permanent test doubles) and ADU-17 (generated client and sign-in) inserted at their derived places; every retirement of a Null is a declared amendment of main.py, the stub and its test; the CLI at layer 6; Prism out of the gate (in-process example validation instead); the §6 path asserted through the four real services in ADU-07; timing arms registered by amendment; Q-04's restoration of the combined gate on ADU-12. ARCHITECTURE v1.1 (D-09 frontend toolchain; editorial), INTERFACES v1.0.1, contract v1.1 (MemberSummary; Spectral clean), tests/layering.json frozen list emptied and the baseline regenerated on the empty tree, CLAUDE.md derived block re-rendered (Q-04 grant), STATUS rows for the two new units. D-08 struck, D-09 and D-10 recorded. `adu plan check` green with no warnings; derived blocks current; audit and release check green.
**Decisions:** D-09, D-10.
**Deviations flagged:** the plan v1.0 commit claimed a developer read that had not happened (the apply script's journal text was written ahead of the read) — corrected by doing the read before any unit opened; the same lesson as the journal-before-diff feedback.
**Approval:** the operator's approval of the plan is, for this example run, the standing instruction to execute ADU-00..02 here; the operator re-approves when taking over at ADU-03 (the plan is theirs to amend first).
**Tests at close:** plan check, derived check, ledger lint, audit, release check, spectral — all green; no code yet.
**NEXT:** `adu handover ADU-00`, then the ADU-00 session (developer).

## 2026-11-07 08:39 · ADU-00 · in progress
**Done:** tests first — tests/test_layering.py and tests/test_tiers.py from the adapter templates (arms 5–8), tests/test_method.py refreshed from the template (arms 1–4, the planted faults in temporary copies); then the roster: pyproject.toml from the template plus `[project.scripts] app = "app.cli:main"`, src/app/__init__.py (already present from the architecture phase), tests/conftest.py (the tiers by node id, TIMING_NODES empty), tests/layering.json with app.cli in the root layer and `frozen` empty, the baseline regenerated on the empty tree (0 edges, 1 module).
**Decisions:** none beyond the plan; the test files are the adapter's templates verbatim (the method's own guards), not hand-written.
**Deviations flagged:** `uv.lock` appears outside the roster (Q-05, not blocking; left untracked). The qa-engineer subagent step was performed by hand: the templates are the criteria-first drafts for every arm.
**Tests at close:** 10 passed under `uv run pytest tests/ -q -m "not timing"`; ruff clean.
**NEXT:** the operator's gate; then `adu handover ADU-00 --closure` in a fresh session writes ✅ from the pasted gate line.

## 2026-11-07 08:40 · ADU-00 closure · done
**Done:** the gate re-run under the operator's hands — in this example run the same machine as the session, which is the one honest caveat of the record: on the user's own run the gate is theirs on their machine — last line `10 passed in 2.81s`; ADU-00 ✅ with 10 tests; `## Now:` advanced to ADU-01 (next in the derived order).
**NEXT:** `adu handover ADU-00` is spent; run `adu handover ADU-01` and open the ADU-01 session (developer): the data model and the seeded fixture.

## 2026-11-07 08:42 · ADU-01 · in progress
**Done:** tests first from the six arms (tests/test_models.py: tables, key fields, a fresh file per workspace, the constraints at the database, naive timestamps and no clock read; tests/test_synthetic.py: R-scheduling-09 field by field, byte reproduction against the committed fixture, a different seed differs, the SYNTHETIC header and credentials, the fixture loads into the model). Then the roster: src/app/models.py (seven tables; Role an enumeration carried in Member.role; email unique by a lower() index; check constraints for slots, roles, states, outcomes, events; hash_passcode as a salted SHA-256 from the standard library), src/app/db.py (engine_for: one SQLite file per workspace path created on first use, foreign keys on; session_for: one session per request), src/app/synthetic.py (seeded_week, serialise, load_fixture, write_fixture; the regeneration command `uv run python -m app.synthetic`), tests/fixtures/seeded_week_20261107.json generated by that command.
**Decisions:** the one-open-request-per-assignment rule stays the service's (R-swaps-02/06 depend on the clock, which the store never reads) — stated in the model's docstring and arm 2; the passcode hash lives in models.py because a Member row's representation of a passcode is its hash (R-identity-06), so identity (ADU-03) and the fixture share one function.
**Deviations flagged:** none. The qa-engineer step was performed by hand (the tests were written from the arms before any body existed).
**Tests at close:** 16 passed under `uv run pytest tests/ -q -m "not timing"` (6 of them this unit's); ruff clean. Two tests were red on the first run: the case-insensitive email index lowercased the literal string "email" instead of the column — red is information; fixed by declaring the index on the column.
**NEXT:** the operator's gate; then the closure prompt for ADU-01.

## 2026-11-07 08:44 · ADU-01 closure · done
**Done:** the gate re-run under the operator's hands (same machine in this example run — the caveat of the record): `16 passed in 5.23s`; ADU-01 ✅ with 16 tests; `## Now:` advanced to ADU-16 (next in the derived order: ports, Null implementations and test doubles).
**NEXT:** `adu handover ADU-16`, then the ADU-16 session (developer).

## 2026-11-07 08:46 · ADU-16 · in progress
**Done:** tests first from the six arms (tests/test_ports.py: the five protocols with their signatures, the values and the nine events; the doubles satisfy and are settable; ports.py imports nothing of the product; no vacuous oracle. tests/test_nulls.py: one test per Null, each marked for deletion by its retiring unit). Then the roster: src/app/ports.py (Clock + SystemClock, MemberDirectory, SchedulingPort, SwapsPort, Notifier; Caller, AssignmentInfo, AssignmentView; the nine event dataclasses with their codes; MemberNotFound, AssignmentNotFound, TransferRefused), the four Nulls at their providers' future paths with the docstring naming the provider, tests/support/doubles.py (FixedClock, SpyNotifier, FakeSchedulingPort, FakeSwapsPort, FakeMemberDirectory; VACUOUS empty).
**Decisions:** the fixed clock is a double, not a port (INTERFACES: SystemClock is the product's); NullDirectory resolves `tok_<n>` and `tok_admin` so the contract unit can test auth before identity exists.
**Deviations flagged:** none.
**Tests at close:** 28 passed under `uv run pytest tests/ -q -m "not timing"` (12 of them this unit's); ruff clean; layering scan clean (the Nulls import only ports).
**NEXT:** the operator's gate; then the closure prompt for ADU-16.

## 2026-11-07 08:46 · ADU-16 closure · done
**Done:** the gate re-run under the operator's hands (same machine in this example run): `28 passed in 5.45s`; ADU-16 ✅ with 28 tests; `## Now:` advanced to ADU-02 (the contract unit).
**NEXT:** `adu handover ADU-02`, then the ADU-02 session (developer): the served contract, the golden pin, the composition root.
