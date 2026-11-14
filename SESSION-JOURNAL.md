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

## 2026-11-07 08:47 · ADU-16 lint follow-up · done
**Done:** six over-long docstring lines in ADU-16's files reflowed; `uv run ruff check` clean; gate unchanged (28 passed). The ADU-16 commit went in with those six findings because the session's script printed the lint summary and carried on — the closure's "ruff clean" was asserted, not checked. Recorded as package feedback (the closure prompt should demand the lint's last line pasted beside the gate's, and the Stop hook should refuse a closure block without both).

## 2026-11-07 08:49 · contract addendum (architect) · done
**Done:** contracts/openapi.json generated from the YAML by `npx --yes js-yaml` (D-11): ADU-02's stubs and its conformance test read the contract in process, and the roster gains no YAML parser. Regenerated with every contract change, in the same commit as the golden.
**NEXT:** the ADU-02 session.

## 2026-11-07 08:52 · ADU-02 · in progress
**Done:** tests first from the eight arms (tests/api/test_openapi_golden.py from the adapter template; tests/api/test_metadata.py with the adapter's lint inside; tests/api/test_contract_conformance.py: every contract operation served with the same identity and nothing else, 401 then 501 not_built on every operation but sign-in, every x-synthetic example validates against its schema, the composition root binds a Null per port and an injectable clock, one session per request). Then the roster: src/app/api/schemas.py (the contract's schemas as pydantic models built from contracts/openapi.json — one source, same titles, descriptions, examples, x-when-to-use), src/app/api/deps.py (the bearer resolved once per request through MemberDirectory; ProblemError and the Problem shape; one session per request), src/app/api/contract_stubs.py (every operation registered from the contract with its parameters, body, declared responses, x-story and x-roles, answering 501 not_built), src/app/main.py (create_app: the composition root binding the four Nulls and the clock; the served document pruned to the contract's codes; exception handlers for Problem, invalid_request and not_built), contracts/openapi.golden.json written by the regeneration command.
**Decisions:** the models are generated from the contract rather than typed by hand (D-11 made the JSON twin readable in process) — the served document cannot drift from the contract by a typo; FastAPI's own 422 shape is replaced by the Problem invalid_request and its two schemas removed from the served document (the contract declares neither). Framework validation answers invalid_request for a wrong-typed field before any state check — consistent with the design's "a wrong-typed one is invalid_request"; the lenient order holds for missing fields (declared optional) and for the enumerated strings the domain checks.
**Deviations flagged:** the gate was run once before this block was written (the order the skill fixes is block first); `adu init --check` caught it — a 🔨 unit with no journal block is an interrupted unit — which is the method working. uv.lock still untracked (Q-05).
**Tests at close:** 42 passed under `uv run pytest tests/ -q -m "not timing"` (14 of them this unit's: 6 golden incl. the two falsification twins, 2 metadata, 6 conformance); `uv run ruff check` clean (its last line: All checks passed!). The metadata lint was red twice on the way: pydantic drops the title of a $ref field and a null example — the served document now takes them back from the contract, which is the source.
**NEXT:** the operator's gate; then the closure prompt for ADU-02 — the last unit of this example run; the user takes over at ADU-03 with `adu handover ADU-03`.

## 2026-11-07 08:55 · ADU-02 closure · done
**Done:** the gate re-run under the operator's hands (same machine in this example run): `42 passed, 1 warning in 9.56s`; lint: `All checks passed!`; ADU-02 ✅ with 42 tests; `## Now:` advanced to ADU-03 (identity service). M1 (ADU-00, 01, 16, 02) is complete: the served contract equals the golden, every operation answers 501 not_built, the ports exist with Nulls and doubles, the seeded fixture reproduces byte for byte. `adu release check` green; the four mocks active as the plan expects (their providers not built).
**Hand-over to the operator:** this is where the example run ends and the user's hands-on run begins. The next action is `adu handover ADU-03` (generated and kept beside this record), pasted into a fresh developer session; the operator's own gate run closes it. Q-02, Q-03 and Q-05 stay open for the operator; M1 closes with /adu-lifecycle:release when the operator chooses to tag it.

## 2026-11-07 14:09 · release M1 (release manager) · blocked
**Done:**
- `adu status`: M1 = ADU-00, ADU-01, ADU-16, ADU-02 (ADU-PLAN Milestones), all ✅; Owed empty; no open blocking question (Q-02, Q-03, Q-05 open, non-blocking).
- `node "C:/dev/adu-lifecycle/scripts/adu.mjs" release check` → `release check OK`, exit 0 (pins, plan check, derived blocks, ledgers; the four Nulls stand behind ADU-03, 05, 07, 09, none ✅, so no mock is active behind a ✅ provider).
- Golden: `git log --oneline -- contracts/` — openapi.yaml last changed in ed4a633 (v1.1), before ADU-00 opened; inside M1 only d7e66ab (the JSON twin, D-11) and 2d403ec (the golden, first pinned by ADU-02). No contract change inside M1, so no regeneration was owed. The twin's fidelity to the YAML is not verified by this session (`npx --yes js-yaml` refused by the session's permission classifier; no YAML parser in the environment) — the operator's twin command checks it.
- FEEDBACK.md: Defects, Friction, Ideas all empty — nothing to triage.
- Preview on this session's machine, **not the gate**: `uv run pytest tests/ -q -m "not timing"` → `42 passed, 1 warning in 14.95s` (the warning: StarletteDeprecationWarning, httpx with starlette.testclient); `uv run ruff check` → `All checks passed!`; `uv run pytest tests/ -q -m timing` → `42 deselected, 1 warning in 0.71s`, exit 5 (no timing arm registered in M1).
- The record's caveat, carried forward: every M1 ✅ was written from a gate the session ran on its own machine (blocks 08:40, 08:44, 08:46, 08:55 say so); the milestone gate is the first on M1's tree under the operator's hands.
- Journal claims checked against the plugin's FEEDBACK.md: FB-14 (Q-04), FB-15 (Q-05), FB-17 (the ADU-16 lint closure) exist as stated.
**Decisions:** the tag goes on the commit holding exactly the tree the operator gates (HEAD c4ce7f0 plus this block); the RETRO section, the Log line and this block's close follow the tag in a second commit.
**Deviations flagged:** the Q-04 grant (adu.toml gate, fast, lint reduced to python) was to be re-confirmed by the operator on taking over (block 08:19) — asked in this session; the answer is recorded here. Q-05: the tag stands on a tree without uv.lock.
**Tests at close:** the operator's gate, red — `uv run pytest tests/ -q -m "not timing"` in a fresh PowerShell → `2 failed, 40 passed, 1 warning in 19.79s` (test_layering.py: the planted forbidden import, the baseline both ways; `UnicodeEncodeError 'charmap'`). The run is invalid on a second count: the interpreter was `C:\dev\crucible-data\.venv` (the User-level `UV_PROJECT_ENVIRONMENT`; `uv` uninstalled 14 and installed 19 packages there — the plugin's FB-20 again, and Crucible's environment is now altered). The encoding failure is independent of that: reproduced in the project's own environment (FB-01). Lint, timing and the twin check not run. No tag. The Q-04 grant re-confirmation: not yet answered.
**Triage:** FB-01 (new, the only entry) → defect session now, before the tag.
**NEXT:** `/adu-lifecycle:defect FB-01` in a fresh `claude --plugin-dir C:\dev\adu-lifecycle --agent adu-lifecycle:developer` (the developer runs the defect loop, PLAYBOOK loops table) launched from a PowerShell with `UV_PROJECT_ENVIRONMENT` set to `C:\dev\team-rota-data\.venv` and `PYTHONUTF8` unset; once its fix is on `main`, `/adu-lifecycle:release M1` again in a fresh `claude --plugin-dir C:\dev\adu-lifecycle --agent adu-lifecycle:release-manager`, from the operator's gate.

## 2026-11-07 16:34 · Defect session FB-01 · done
**Scope:** `tests/layering_scan.py` (the fix: made identical to the plugin adapter's `adapters/python-fastapi-uv/layering_scan.py`, plugin commit f6b0143, plugin FB-18) · `tests/test_fb01_scan_encoding.py` (new, the red test; a new file because `tests/test_layering.py` is completed ADU-00's test and immutable) · `ADU-PLAN.md` (ADU-00's `tests:` gains the new file, with an `amends:` line naming FB-01, the one plan edit a defect session may make) · ledgers: this block, FEEDBACK.md FB-01, the STATUS.md Log line. Nothing else.
**Hard-rule-6 grant, operator, 2026-11-07 16:33, in session:** the operator's instruction, verbatim: "the plugin's adapter already carries it at C:\dev\adu-lifecycle\adapters\python-fastapi-uv\layering_scan.py (plugin commit f6b0143, plugin FB-18): the scan's output is ASCII-only. The minimal fix is to make tests\layering_scan.py identical to that file. The failing test must force a cp1252 child (PYTHONIOENCODING=cp1252 and PYTHONUTF8=0 in the subprocess environment) so it is red in any shell." Permitted: `tests/layering_scan.py`, whole file, replaced by the adapter's text; `tests/test_fb01_scan_encoding.py`, created. Both are outside the Now unit's (ADU-03) roster, so the edit guard is given the same two grants (`adu grant add 37348940-54f4-4071-abde-8b96734405f7 …`). Measurement before the grant: `diff tests/layering_scan.py <adapter>` — six message lines (`→` → `->`, `—` → `-`) plus one docstring line ("Output is ASCII-only on purpose … (plugin FB-18)"); `grep -P '[^\x00-\x7F]'` on the adapter's file finds nothing.
**Reproduction before any edit:** `env -u PYTHONUTF8 uv run pytest tests/test_layering.py -q` → `2 failed, 1 passed in 0.72s`; `test_the_baseline_fails_both_ways` (test_layering.py:68) gets `stdout == ''` and stderr `UnicodeEncodeError: 'charmap' codec can't encode character '\u2192' in position 49: character maps to <undefined>`. This is the operator's fault, in the project's own environment (`C:\dev\team-rota-data\.venv`).
**Red, before the fix:** `uv run pytest tests/test_fb01_scan_encoding.py -q -p no:cacheprovider --tb=line` → `3 failed, 1 passed in 0.50s`, identical with `env -u PYTHONUTF8` (`3 failed, 1 passed in 0.59s`), so the forcing holds even in this session's `PYTHONUTF8=1` shell:
```
tests/test_fb01_scan_encoding.py:49: assert [(12, 'forbid...sym} "'), ...] == []
tests/test_fb01_scan_encoding.py:80: AssertionError: Traceback (most recent call last):   # --write-baseline under cp1252: exit 1, not 0
tests/test_fb01_scan_encoding.py:108: AssertionError: assert 'UnicodeEncodeError' not in 'Traceback (...defined>\r\n'
    UnicodeEncodeError: 'charmap' codec can't encode character '\u2192' in position 49: character maps to <undefined>
FAILED tests/test_fb01_scan_encoding.py::test_the_scan_source_is_ascii_only
FAILED tests/test_fb01_scan_encoding.py::test_a_forbidden_crossing_is_reported_on_a_cp1252_stdout
FAILED tests/test_fb01_scan_encoding.py::test_both_baseline_directions_are_reported_on_a_cp1252_stdout
3 failed, 1 passed in 0.50s
```
The one pass is the control `test_the_forced_child_really_writes_strict_cp1252` (the child reports `cp1252 strict 0`); it is green on both sides of the fix by design and fails only if the forcing stops working.
**The fix:** `cp` of the adapter's file over `tests/layering_scan.py`; `cmp` exits 0, so the files are identical. `git diff --stat`: 8 insertions, 7 deletions (six message lines, two docstring dashes, one docstring line). Afterwards `tests/test_fb01_scan_encoding.py` + `tests/test_layering.py` → `7 passed` both with `PYTHONUTF8` unset and with `PYTHONUTF8=1`; the scan on the real tree with `PYTHONIOENCODING=cp1252 PYTHONUTF8=0` exits 0.
**Q-06 raised and ruled:** step 5 as written (new file on ADU-00's `tests:` plus an `amends:` line) turned `adu plan check` red: `4 test files exceeds size M cap 3`, `has no arm assigned`, and a self-cycle from `amends: { unit: ADU-00 }` (83 errors). The plan edit was reverted at once and `plan OK` restored. The operator ruled option 1 in session at 16:39.
**Grant (hard rule 1), operator, 2026-11-07 16:39, in session:** `tests/test_layering.py`, append-only. The four FB-01 tests and their helpers go after line 71, and lines 1–71 (the module, its imports and ADU-00's three tests) stay byte-for-byte unchanged. `tests/test_fb01_scan_encoding.py` is deleted. Measurement: the plan-check output above. Machine grant: `adu grant add 37348940-… tests/test_layering.py "Q-06 ruled option 1 …"`.
**Red in the final home, before the fix:** HEAD's scan put back temporarily (`git show HEAD:tests/layering_scan.py`), then `uv run pytest tests/test_layering.py -q --tb=line` → `3 failed, 4 passed in 1.28s` (test_layering.py:111 the ASCII-only source, :142 `--write-baseline` under cp1252 exits 1 with a Traceback, :170 `UnicodeEncodeError` in stderr). The fix was restored with `cp`, `cmp` confirms it is identical, and the result is `7 passed` with `PYTHONUTF8=1` and with it unset.
**Done:**
- `tests/layering_scan.py` is now byte-identical to the plugin adapter's file at f6b0143 (plugin FB-18): its output is ASCII-only (`->`, `-`) and the docstring says why. Nothing else in it changed.
- `tests/test_layering.py`: four FB-01 tests appended after line 71, lines 1–71 unchanged (sha256 of `head -n 71` `f99682d9…` before and after; `git diff -U0` shows the single hunk `@@ -71,0 +72,112 @@`). They are: the control `test_the_forced_child_really_writes_strict_cp1252`, `test_the_scan_source_is_ascii_only`, `test_a_forbidden_crossing_is_reported_on_a_cp1252_stdout` and `test_both_baseline_directions_are_reported_on_a_cp1252_stdout`.
- `tests/test_fb01_scan_encoding.py`: created, shown red, deleted (Q-06 option 1). It never reaches a commit.
- ADU-PLAN.md ADU-00 gains one acceptance arm naming FB-01 on `tests/test_layering.py` (8 → 9 arms). `adu plan check` → `plan OK: 18 units`, order unchanged; `adu derived check` → `derived blocks OK`; `adu pins check` → `pins OK (1 pinned)`; `adu ledger` → `ledgers OK`.
- OPEN-QUESTIONS.md: Q-06 raised and resolved (option 1, operator, 16:39).
**Decisions:**
- The fix is the adapter's text verbatim, at the operator's instruction. The project's scan is a copy of the adapter template (its docstring, line 2), so staying identical keeps the next re-copy a no-op (plugin FB-18's own disposition: "a project scaffolded earlier makes its `tests/layering_scan.py` identical to the adapter's file in a defect session").
- The child is forced through its environment (`PYTHONIOENCODING=cp1252`, `PYTHONUTF8=0`, operator's instruction), and a control asserts that the child really reports `cp1252 strict 0`. Without the control, a forcing that silently stopped working would leave every FB-01 test vacuous.
- The tests assert the full message lines the operator reads, not only the absence of a crash. The ASCII-only source test also covers messages no planted tree reaches (`no baseline at …`, `the walk found …`); the invariant is the adapter's own (its docstring line 19).
- `import os` sits inside `cp1252_env()`, not in the import block: the grant is append-only after line 71.
- No `amends:` line: on ADU-00 itself it derives a self-dependency (Q-06 (c)). The new arm names FB-01 instead.
- The developer wrote the failing test, not the qa-engineer subagent: the defect skill's mandatory order (step 2) gives it to the session.
**Deviations flagged:**
- This session's shell had `PYTHONUTF8=1`, although the NEXT of block 14:09 asked for it unset. Every reproduction here ran with `env -u PYTHONUTF8`, the new tests force cp1252 whatever the shell, and the gate below runs both ways. The operator's own gate in a default PowerShell is still the one that counts.
- The defect skill's step 5 could not be applied as written (Q-06). The arm replaces the `amends:` line, and `tests/test_layering.py` (a completed unit's test) grew under a hard-rule-1 grant.
- `tests/layering_scan.py` was written with `cp`, not Edit/Write, so the edit guard was not consulted for that write. The grant was recorded first and `cmp` proves the content.
- Plugin feedback, for the operator to carry upstream (not this repository's to fix): (1) the defect skill's step 5 does not fit a unit already at its size's test-file cap and does not mention the arm-file rule; (2) `plan.mjs` derives `depends` from `amends.unit` without skipping the unit itself, so a self-amendment is a cycle.
**Tests at close:** the session's runs, **not the operator's gate**. `env -u PYTHONUTF8 uv run pytest tests/ -q -m "not timing"` → `46 passed, 1 warning in 15.46s`; the same with `PYTHONUTF8=1` → `46 passed, 1 warning in 15.52s` (42 before plus 4 new; the warning is the known StarletteDeprecationWarning). `uv run ruff check` → `All checks passed!`. Its first run found 4 × E501 in the appended lines, which were rewrapped inside the grant; lines 1–71 kept sha `f99682d9…`. `uv run pytest tests/ -q -m timing` → `46 deselected` (report only, no timing arm yet). `adu plan check` OK, `adu derived check` OK, `adu pins check` OK, `adu ledger` OK. `uv.lock` is left untracked (Q-05).
**NEXT:** the operator, in a fresh default Windows PowerShell (`PYTHONUTF8` unset, `UV_PROJECT_ENVIRONMENT` = `C:\dev\team-rota-data\.venv`), runs the gate and the lint, then commits and pushes `FB-01: the layering scan died on a cp1252 stdout (non-ASCII messages)`. After that, `/adu-lifecycle:release M1` again in a fresh `claude --plugin-dir C:\dev\adu-lifecycle --agent adu-lifecycle:release-manager`, from the operator's gate.

## 2026-11-07 17:37 · release M1 (release manager) · done
**Scope:** the M1 close after FB-01, from the operator's gate. Ledgers: FEEDBACK.md (FB-01 closed, FB-02), OPEN-QUESTIONS.md (the Q-04 re-confirmation), STATUS.md (O-01, the Log line), ADU-PLAN.md v1.2, VERSIONS.md, RETRO.md (the M1 section), and this block. The tag `m1-foundations` is on `c56ea77`, the tree the operator gated. No code, test or protected file changed.
**Grant re-confirmed (hard rule 4, Q-04), operator, 2026-11-07, in session, verbatim:** "Q-04 grant re-confirmed". It was given after the operator asked what they needed to know and was shown four things: the only change (`44a5dbf` removed the `npm --prefix frontend …` half of gate, fast and lint); why (no `frontend/`; Q-04 option 1); what it leaves out (nothing that exists; the five units that own frontend files sit at derived positions 13–18); and how it is undone (ADU-PLAN.md:399–400, and the arm at :410 that keeps ADU-12 from closing until the combined commands are back). Scope: M1 and derived positions 5–12. Recorded on Q-04 in OPEN-QUESTIONS.md.
**Done:**
- `adu status`: M1 = ADU-00, ADU-01, ADU-16, ADU-02, all ✅. Owed was empty at the start, and no blocking question was open. `c56ea77` = `origin/main` (FB-01 pushed).
- `adu release check` → `release check OK`, before and after this close's edits. Golden: `git log --oneline -- contracts/` shows no contract change inside M1, and nothing under contracts/ or src/ since `c4ce7f0`.
- The twin check the 14:09 block left open, done offline and read-only: `node -e` loading js-yaml 5.5.0 from `%LOCALAPPDATA%\npm-cache\_npx\bd03aaf280724e38`, comparing `load(openapi.yaml)` with `openapi.json` → `semantic EQUAL · bytes EQUAL`, exit 0. Bytes are compared against `JSON.stringify(doc, null, "  ") + "\n"`, the CLI's output. D-11's own command is `npx --yes js-yaml contracts/openapi.yaml > contracts/openapi.json`. In Windows PowerShell 5.1, `>` writes UTF-16 and a pipe re-encodes text, and the contract has 14 non-ASCII lines, so the next check should read the files from node and not redirect.
- Preview on this session's machine, not the gate (`UV_PROJECT_ENVIRONMENT` set explicitly, `PYTHONUTF8` unset): `46 passed, 1 warning in 24.88s` · `All checks passed!` · `46 deselected`.
- **The operator's gate**, a fresh Windows PowerShell: `git rev-parse --short HEAD` → `c56ea77`; `git status --short` → `?? uv.lock`; `sys.prefix, locale, utf8_mode` → `C:\dev\team-rota-data\.venv cp1252 0`; `uv run pytest tests/ -q -m "not timing"` → `46 passed, 1 warning in 28.77s`; `uv run ruff check` → `All checks passed!`; `uv run pytest tests/ -q -m timing` → `46 deselected, 1 warning in 1.11s` (reported, never gating; no timing arm in M1).
- Tag: `git tag -a m1-foundations c56ea77 -m "M1 Foundations: gate 46 passed in 28.77s; timing: none (46 deselected, no timing tests in M1)"`; `git push --tags` → `[new tag] m1-foundations`; `git ls-remote --tags origin` → `bcd108d… refs/tags/m1-foundations`, `c56ea77…^{}`.
- **Use-it run** (the retro's step 1). The session rehearsed it first against a loopback uvicorn with its workspace in the scratchpad. Then the operator ran it: window 1 ran `uv run uvicorn --factory app.main:create_app --host 127.0.0.1 --port 8000` with `ROTA_WORKSPACE=%TEMP%\rota-m1`. In window 2: `uv run python -m app.synthetic` → `C:\dev\team-rota\tests\fixtures\seeded_week_20261107.json`, and `git status --short` shows no fixture line (reproduced byte for byte); `served == golden: True | operations: 18`; `curl.exe -s -i /members` → `401` "Not signed in" "Sign in first."; with `Bearer tok_1` → `501` "Not built" "identity.list_members is served by a later unit."; `POST /auth/sign-in` with the contract's example body (`--data-binary @%TEMP%\signin.json`) → `501` "identity.sign_in is served by a later unit.". Question 4, the operator's words: "I'm not sure where M1 stands."
- RETRO.md M1 section written, with the light check: M1 is the first of four milestones, so the default schedule (full review at every second milestone and the last) puts the full reviews at M2 and M4. Question 4 is recorded as not established and carried to M2's full review.
- ADU-PLAN v1.2 (VERSIONS.md row): the FB-01 arm the defect session added (a requirement, so the minor bump); M1's usable-path cell corrected to ADU-02's arm (ADU-PLAN.md:129: 401 without a token, 501 with one, sign-in 501; `git grep "answers 501"` finds no other artefact that says it); ADU-11's entry carries O-01. After the edits: `plan OK: 18 units` (order unchanged), `derived blocks OK`, `pins OK (1 pinned)`, `ledgers OK`, `release check OK`.
**Triage:** FB-01 → closed by the operator's gate. The line is appended in place and the entry is not moved to `## Closed`: the ledger is append-only and merged by union, so a moved block would come back as a duplicate. FB-02 (new, found by this session's rehearsal) → deferred to ADU-11 as O-01. The operator, in session, verbatim: "0-01 approved" (read as O-01). No other FB entry is open.
**Decisions:**
- The tag is on `c56ea77` itself, not on this close's commit, so the tagged tree is exactly the gated one. Everything this close writes is ledger and plan text in one commit after the tag.
- FB-02 is deferred, not fixed now: no real data exists before ADU-11. O-01 states the outcome, not the means; moving the default workspace would be a design question.
- Question 4 is not rephrased, interpreted or answered from the tests. The operator's uncertainty is the record. It does not escalate the light check by itself (the rule escalates on the drift line or the backward series, neither of which looks wrong), but it is carried to M2's review by name.
**Deviations flagged:**
- This session's shell inherited the User-level `UV_PROJECT_ENVIRONMENT=C:\dev\crucible-data\.venv`. Every `uv` command here set `C:\dev\team-rota-data\.venv` first, so Crucible's venv was not touched. The session-end hook's last log (16:14) also shows `team-rota-data`. The User-level variable is still set, and Crucible's venv is still altered from 14:09; both are outside this project.
- At the operator's request this session checked every Crucible reference: `git grep -i crucible` → four lines, all intended. `.gitattributes:1,11` and `tests/test_method.py:4` are scaffold provenance comments (`ba9e5e6`); the two citations were checked against Crucible's FEEDBACK.md (FB-13 at :757, FB-20 at :257). SESSION-JOURNAL.md:192 is the record of the venv collision. Remote, plugin root, venv and local state name no Crucible path. This session read Crucible's RETRO.md and FEEDBACK.md read-only, as format examples, which was unnecessary since the plugin's templates are the authority; nothing from them entered this record.
- The first paste of the long `python -c` one-liner broke into PowerShell continuation lines; the second paste ran. That is a fault in the instruction, not the product: long one-liners go into a file next time.
- The retro skill's step 5 has the operator commit; this session commits and pushes the close, as it told the operator it would and with the operator's agreement.
- The tag is pushed and `uv.lock` stays untracked (Q-05).
**Plugin feedback, for the operator to carry upstream** (not this repository's to fix): (1) the release and closure gate blocks should print the interpreter, encoding and UTF-8 mode first (RETRO M1 q3; FB-20's mechanism); (2) the FEEDBACK template has a `## Closed` section but no rule for moving into it, which conflicts with append-only ledgers merged by union; (3) the STATUS Owed table's `Approval` column is not documented anywhere in the plugin; (4) the ADU-PLAN header the scaffold writes says prose under an entry is rendered and never hand-edited, while the entry template says hand-written prose is welcome; only the Mocks block is derived.
**Tests at close:** the operator's gate above, `46 passed, 1 warning in 28.77s`, lint clean, timing `46 deselected` (reported). After this close's edits: plan, derived, pins, ledger and release checks all OK.
**NEXT:** ADU-03 (Identity service, size M), the `## Now:` unit. The oversight session generates `adu handover ADU-03` and checks it against the plan entry. Then a fresh `claude --plugin-dir C:\dev\adu-lifecycle --agent adu-lifecycle:developer` runs it, launched from a PowerShell inside `C:\dev\team-rota` where the loader has printed `Team Rota environment: C:\dev\team-rota-data\.venv`. The User-level variable still names Crucible's venv, so the session confirms `$env:UV_PROJECT_ENVIRONMENT` before any `uv` command. ADU-03 consumes MK-01 and MK-02. At M2's close, the retro generates the full alignment review prompt and puts M1's question 4 ("I'm not sure where M1 stands") to the reviewer.

## 2026-11-07 20:20 · hand-over ADU-03 (oversight) · blocked
**Done:** `adu status` (Now: ADU-03, plan OK) and `adu handover ADU-03`, both exit 0, from the oversight session's clone of `c72b042`. The D-0 check of the generated hand-over against the ADU-03 entry, the interfaces it consumes and amends, and the open questions failed on two blocking points: ADU-03's first arm against ADU-02's completed `tests/api/test_contract_conformance.py` (lines 23, 70, 105; confirmed by the operator with `Select-String` on their clone), and the edit guard refusing `tests/test_nulls.py`, which ADU-03's `amends` declares. Two gaps: `Refused` and the IdentityService signatures are defined nowhere. Raised as Q-07 (blocking), with the evidence by file and line.
**Decisions:** the operator ruled Q-07 option 1, verbatim "Add both tests to ADU-03's amends". The operator asked that Q-07 be written by whoever is best placed to be accurate and unbiased: the oversight session found the conflict and records it; the pack is drafted by a separate architect session, verified by a fresh verifier and applied by the release manager, so the finder neither writes nor approves the fix.
**Deviations flagged:** the generated hand-over also carries faults of the plugin's generator, to be corrected when ADU-03 is handed over again (Linux paths when generated off the operator's machine; C1 without `--plugin-dir`; C1's roster without the `amends` files; section A expecting a clean `git status -sb` beside an untracked `uv.lock`; section B's `git add -A` committing `uv.lock` against Q-05; C2 without the interpreter line and without demanding the lint's last line). They are plugin feedback, carried upstream.
**Tests at close:** none run; no code, test or plan text changed. `adu ledger` → `ledgers OK`.
**NEXT:** `/adu-lifecycle:change-design Q-07` (stage 1, the pack) in a fresh `claude --plugin-dir C:\dev\adu-lifecycle --agent adu-lifecycle:architect` started inside `C:\dev\team-rota`; ADU-03 opens only after the apply step resolves Q-07.

## 2026-11-08 08:39 · design-change loop Q-07, stage 1 (architect) · done
**Done:**
- `adu status` (Now: ADU-03; Q-07 open, blocking) and `git rev-parse --short HEAD` → `7d1e7d4`, the snapshot the operator named. This session answers Q-07 and does not open ADU-03.
- docs/PACK-q07-retire-amends.md v1.0, snapshot 7d1e7d4, in the shape of the skill's pack-shape.md. It writes the operator's ruling (Q-07 option 1, "Add both tests to ADU-03's amends") without re-opening it:
  - B-1/B-2.1: D-p1 (the retirement edits, each under the operator's grant, because the guard does not honour `amends` on a completed unit's test, plugin FB-28) and D-p2 (`Refused(reason, detail="", **extra)` in src/app/ports.py).
  - B-2: design/INTERFACES.md §Refused, §Domain services with IdentityService, the retirement paragraph and the seed trace; Q-07 resolved, and Q-p1–Q-p5 drafted; VERSIONS rows.
  - B-2.T: the exact test edits each retiring session makes under its grant (ADU-03, ADU-09, ADU-05, ADU-07, in both files; ADU-07 removes tests/test_nulls.py).
  - B-3: 14 plan replacements (the four retirement arms and their `amends`, the Shape-of-the-cut sentence, the version).
  - Part C: the chase list.
  - Part D: the verify and apply prompts.
  - Part E: five operator decisions with recommendations.
- Checked on scratch exports of 7d1e7d4 (`git archive`, outside the repository), with the scratch script embedded in B-4.3:
  - All 58 replace blocks match character for character at their stated lines: 69 checks, 0 mismatches, including the E-options alone and combined.
  - With B-3 applied: `plan OK: 18 units`, order unchanged. The same holds with E-2 (b).
  - The guard on the amended plan still refuses both completed tests and allows src/app/ports.py.
  - The four stages give gate 46 → 44 → 42 → 40 → 38 passed, with lint clean at each, and stand-in services in place of the real ones. Afterwards no Null module and no Null import remain.
  - Twins at the ADU-03 stage: the unedited test fails at collection (`ModuleNotFoundError: No module named 'app.identity.null_directory'`). With only the import and the class check edited, the 501 assertion fails with 401.
- A ContextVar probe for Q-p1: set in a sync generator dependency, it is invisible to the endpoint; set in an async one, it is visible (fastapi 0.162.0, starlette 1.10.0).
**Decisions:**
- No existing double resolves `tok_1` as constructed (tests/support/doubles.py:95–112). The pack therefore gives the options as E-1 and recommends FakeMemberDirectory configured in the test; it does not choose.
- The IdentityService signatures come only from ADU-03's arms, R-identity-01..09 and the contract. Four points those sources do not settle are raised, not filled in: the request's session (Q-p1), the construction across the identity ↔ scheduling cycle (Q-p2), the token and salt source against ARCHITECTURE.md:45 "No randomness in the product" (Q-p3), and the returned values (Q-p4).
- The same wall at the API units (the 501 loop and the helpers in contract_stubs.py, which ADU-08 deletes) is outside Q-07's ruling. It is raised as Q-p5 and blocks ADU-04, not M2.
- The plan text cites only Q-07, because `adu plan check` rejects a provisional id in the plan.
- At ADU-03, line 105's protocol check is split into two asserts: as one line it is 113 characters, over ruff's 110.
**Deviations flagged:**
- The skill's stage-1 step 4 commits the pack. It is not committed, at the operator's instruction.
- If E-5 (a) is ruled, ADU-03 stays blocked after the apply, on Q-p1–Q-p4. This is stated in Part E, not hidden.
- The session ran across midnight, so the pack and this block carry 2026-11-08.
- No governing document, code, test or protected path was changed. The only files written in the repository are the pack and this block.
**Tests at close:** none — documents only. The scratch runs above are measurements on exports, not this tree's gate.
**NEXT:**
1. The operator commits the pack: `git add docs/PACK-q07-retire-amends.md SESSION-JOURNAL.md` then `git commit -m "docs: pack q07-retire-amends v1.0, snapshot 7d1e7d4"`.
2. In a fresh `claude --plugin-dir C:\dev\adu-lifecycle --agent adu-lifecycle:verifier` started inside `C:\dev\team-rota`, paste Part D-1 of the pack.
3. Rule Part E (E-1 … E-5) after the verdict.

## 2026-11-08 18:34 · design-change loop Q-07, stage 1 again (architect): pack v1.1 · done
**Done:**
- Start checks: `adu status` (Now: ADU-03; Q-07 open, blocking); `adu snapshot check 7d1e7d4` → OK (no commit since); `ADU_PLUGIN_ROOT` = `C:\dev\adu-lifecycle`. The interpreter line as given, `python -c …`, printed `C:\Python314 cp1252 0`, not the venv: bare `python` resolves to the system interpreter in this session's shells (Git Bash and `powershell -NoProfile`). `uv run python -c …` prints the expected `C:\dev\team-rota-data\.venv cp1252 0`.
- The connection dropped once mid-session, before anything was written. On resuming, the pack and the journal were still byte-identical to 3082fd4, and no draft of E-5–E-9 existed; nothing was left mixed.
- docs/PACK-q07-retire-amends.md v1.1 (snapshot 7d1e7d4; verification pending, round R1). It was assembled in the scratchpad from the 3082fd4 blob. All 58 v1.0 blocks and the E-1–E-4 text are byte-identical (checked by script). Allocated ids appear only in D-2's expected mapping.
  - E-6–E-9: Q-p1–Q-p4 become operator decisions. Each has the text of its recommended option and of one alternative, as E-blocks against the files as B leaves them. Together they complete design/INTERFACES.md §Domain services and §IdentityService, write D-p3–D-p6, amend design/ARCHITECTURE.md:42 (E-6) and :45 (E-8), add ADU-03's amends of src/app/db.py and src/app/api/deps.py (E-6 (b)), and write the four resolutions. E-6 (c), E-7 (c), E-8 (c) and E-9 (b) have no text.
  - E-6 (b) states the seed command, how a test makes a session current, and that a method with no current session raises `db.NoCurrentSession`. The new current-session probe (async generator dependency, the repository's engine) and its output are pasted.
  - E-9.P (PRODUCT-DESIGN.md:18) is the pm-lead's editorial text and is not in this apply.
  - E-5 rewritten: (a) with E-6–E-9 ruled, Q-p1–Q-p4 are entered resolved and Q-p5 open; (b) with none ruled, v1.0's open-and-blocking entries. A partial ruling stops the apply.
  - B-4.3's script extended and re-run in full: 109 blocks matched; the 16 combinations, alone and with E-2 (b) + E-3 (b), all match with the DECISIONS rows in id order. `plan OK: 18 units`, order unchanged, with B-3, with B-3 + E-6 (b), with B-3 + E-2 (b), and with B-3 + E-2 (b) + E-6 (b). The guard allows db.py and deps.py with E-6 (b) and still refuses both completed tests. Stages: gate 46 → 44 → 42 → 40 → 38, lint clean at each. The E-6 (b) scaffold raises `NoCurrentSession` outside a unit of work and answers `None` inside; the twins are unchanged.
  - D-1 and D-2 updated as asked; header v1.1, with a line saying what changed.
**Decisions:**
- The probe settled the commit's place. FastAPI 0.162 runs a default-scope yield-dependency's exit after the response is sent (a raise there still answers 200), so under E-6 (b) the API layer commits before it answers and never in the dependency's exit (D-p3).
- The constructor line is split into three adjacent fragments, one per decision, so any options compose. The four DECISIONS rows share one anchor and are applied E-9 first; the reading notes and D-2 say so.
- E-7 (b) is written as a zero-argument callable answering the container: the container cannot be passed while it is being built (src/app/main.py:52–58).
- E-8 (a) narrows v1.0's "never `random`" to "a credential never comes from `random`": src/app/synthetic.py is product code and takes a `random.Random(seed)`.
- E-9 (b) has no text (a breaking contract change), so the written alternative is (c), plain dicts.
- No apply rehearsal with substituted ids was run: it would put allocated ids into the pack's pasted output.
**Deviations flagged:**
- D-1 and D-2 use `uv run python -c …` for the interpreter line, not the bare `python -c …` as given (see Done).
- D-1 steps 3 and 5 changed beyond the list: step 3 names both 2026-11-08 drafting blocks, and step 5 re-runs E-6 (b)'s plan check and the E-6 probe, since the verifier re-runs every stated measurement.
- D-2 allocates Q ids for Q-p1–Q-p4 as well, where the instruction said Q-p5 "and any question still entered open". Entered resolved, they are still entries, and `adu ledger lint` refuses a provisional id in a governing document (plugin scripts/adu.mjs:225).
- Observed, not changed:
  - Under E-2 (b), B-2.7's Q-07 resolution and B-2.9's VERSIONS row still say "ADU-03 amends src/app/ports.py" (a v1.0 gap, for the verifier).
  - design/INTERFACES.md:92 lists two service cycles and omits identity ↔ notifications (IR-10 / IR-04); E-7 cites it and does not amend it.
  - Part C has no row for E-6–E-9's terms. Outside records, `git grep` finds "No randomness" only at design/ARCHITECTURE.md:45 and "a member as the team list shows it" only at design/PRODUCT-DESIGN.md:18.
- Not committed, at the operator's instruction. No governing document, code, test or protected path changed; the only files written in the repository are the pack and this block.
**Tests at close:** none — documents only. The scratch runs above are measurements on exports, not this tree's gate.
**NEXT:**
1. The operator commits: `git add docs/PACK-q07-retire-amends.md SESSION-JOURNAL.md` then `git commit -m "docs: pack q07-retire-amends v1.1, snapshot 7d1e7d4"`.
2. In a fresh `claude --plugin-dir C:\dev\adu-lifecycle --agent adu-lifecycle:verifier` started inside `C:\dev\team-rota`, paste Part D-1 of the pack.
3. Rule E-1 … E-9 after the verdict.

## 2026-11-08 22:45 · verification R1 · done
**Done:**
- Start checks: `adu status` (Now: ADU-03; Q-07 open, blocking); the three variables as D-1 names them; interpreter line `C:\dev\team-rota-data\.venv cp1252 0`; `git status --short` `?? uv.lock`; `adu role set verifier`. `adu snapshot check 7d1e7d4` → OK (0 commits of drift).
- Read the pack v1.1 in full, Q-07 (OPEN-QUESTIONS.md:53–59) and the journal blocks of 2026-11-07 20:20 and 2026-11-08 08:39 and 18:34. No earlier verification report exists.
- Checked every claim in docs/VERIFICATION-R1.md:
  - all 109 replace blocks and 1 deletion, with my own line parser: B against the 7d1e7d4 blobs, T stage by stage, E on post-B, and the 16 combinations alone and with E-2 (b) + E-3 (b);
  - every row of A-2;
  - the guard;
  - the amendments in both directions;
  - the arms against ADU-02's and ADU-16's;
  - B-2.3 and E-6–E-9 against the arms, R-identity-01..09, the contract and ARCHITECTURE.
- Measured in the scratchpad only:
  - `adu plan check`/`order` with B-3, + E-2 (b), + E-6 (b), and both;
  - the pack's rehearsal re-run, identical apart from timings;
  - my own stand-ins and current-session scaffold (gate 44/42/40/38);
  - wiring mutations;
  - both pack probes re-run, plus my own probe;
  - a simulated apply with ids D-12…D-17 and Q-08…Q-12.
- Gate once at HEAD: `46 passed, 1 warning in 17.89s`; `git status --short` unchanged.
**Decisions:** none; the verifier rules nothing. Findings:
- S: none.
- N-1: E-6 (b)'s db.py/deps.py amendments have no ADU-03 arm. Measured: with `require_caller` not depending on `get_session`, the ADU-03-stage gate is 44 passed while authenticated requests answer 500.
- N-2: Q-p5 entered "**Blocking:** yes" makes `adu status` print "Open blocking questions: Q-12 … — STOP" with Now: ADU-03, against E-5 (a) and D-2.
- M-1–M-3: the non-recommended E-2 (b), E-3 (b) and E-1 (b) leave text unadjusted.
- Provisional Q-p6, outside the pack: four `tests/<domain>/test_service.py` collide at collection (pytest 9.2.0), first at ADU-09.
**Deviations flagged:**
- The report was written through Bash heredocs; this session had no Write tool.
- `adu next-id V` was not run (FB-31); the id R1 was named by hand, as D-1 says.
- The plugin is at 2855b8c, not 4b63bb0; adu.mjs is unchanged between them.
- No governing document, code or test changed. The only files written are docs/VERIFICATION-R1.md and this block; the scratch work is under the session scratchpad.
**Tests at close:** gate `46 passed, 1 warning in 17.89s`; lint `All checks passed!`; `adu verdict check docs/VERIFICATION-R1.md` → `verdict OK: VERDICT: STOP — MECHANICAL`.
**NEXT:**
1. The operator commits: `git add docs/VERIFICATION-R1.md SESSION-JOURNAL.md` then `git commit -m "docs: verification R1 of pack q07-retire-amends v1.1 (STOP — MECHANICAL)"`.
2. The architect revises the pack to v1.2 (`/adu-lifecycle:change-design Q-07`, stage 1 again) for N-1 and N-2. M-1–M-3 and the Notes are optional, and Q-p6 is for the operator to rule on or defer. Then a fresh verifier runs round R2.
3. Nothing is applied; ADU-03 stays blocked on Q-07.

## 2026-11-12 10:28 · design-change loop Q-07, stage 1 again (architect): pack v1.2 · in progress
**Done:**
- Start checks: `adu status` (Now: ADU-03; Q-07 open, blocking). The interpreter line printed `C:\dev\team-rota-data\.venv cp1252 0`, and `ADU_PLUGIN_ROOT` is `C:\dev\adu-lifecycle`. `adu snapshot check 7d1e7d4` → OK against HEAD 99233a7 (0 commits of drift); the snapshot stays 7d1e7d4. Plugin HEAD is c77cbeb (FB-32 and FB-33 recorded); `git diff --stat 4b63bb0 c77cbeb` lists FEEDBACK.md only.
- Read docs/VERIFICATION-R1.md in full, docs/PACK-q07-retire-amends.md v1.1 in full, and the verifier's block of 2026-11-08 22:45.
- docs/PACK-q07-retire-amends.md revised to v1.2, dated 2026-11-12, `snapshot: 7d1e7d4`, status "verification pending (round R2)". Header line 3 maps each R1 finding to where it is handled.
  - N-1: E-6b.10 appends R1's clause to ADU-03's arm 1, and E-6a.9 adds the same request path under E-6 (a).
  - N-2: B-2.7 enters Q-p5 `**Blocking:** no`. E-5a.14 and E-5b.1 write the Owed row O-p1 due ADU-04 in STATUS.md's columns, with the Approval cell naming the E-5 ruling and plugin FB-32 cited. B-3.16 points ADU-04's entry to it. B-5, E-5, E-5a.1 and D-2 are aligned.
  - M-1 → E-2b.8–.18; M-2 → E-3b.5–.6; M-3 → E-1b.1–.4; E-4 (b) is written as E-4b.1.
  - Every R1 Note and cosmetic row: A-2, B-2.3, B-3.3, T-03.4, E-5, E-7 (E-7a.4–.6, E-7b.4–.5), E-8, E-9, Part C.
  - Q-p6 (plugin FB-33): B-2.7 enters it, and E-10 rules it with options (a) rename, (b) `__init__.py`, (c) importlib and (d) defer, each with full text, and a roster-consequence table. (a) is recommended.
  - D-1 is round R2's prompt; D-2 takes E-1 … E-10 and writes the Owed rows.
- B-4.3's script rewritten for v1.2 (scratch: …\scratchpad\rehearsal\pack_rehearse.py). Its text checks are done: 196 replace blocks (B 24, T 24, E 148) and 1 deletion parsed; every block at its line, alone and in each of the 1,088 rulings, with 0 failures. Its full run (plan checks, guard, the E-10 measurements, the four stages with the N-1 and E-10 twins, the simulated apply) is still running.
- Measured before the run, in scratch: as planned, four `tests/<domain>/test_service.py` give 3 collection errors ("import file mismatch"). Under (a) and (b), 50 passed. Under `--import-mode=importlib`, 46 passed without the files and 50 with them.
**Decisions:**
- R1's clause keeps its words except "under D-p3", written as "under the request's current session of design/INTERFACES.md (Domain services)": the plan may carry no provisional id (B-3; plugin scripts/lib/plan.mjs:160).
- The Owed row is a block of each E-5 option, so its Approval cell names the option ruled. The pointer under ADU-04 names no id, for the same plan rule.
- Adaptations that depend on another bracket are conditional blocks, "(with …)" / "(without …)", or blocks "on the text E-xx writes", never prose for the apply to carry.
- E-10 recommends (a). It edits plan text only, touches nothing completed or protected, and needs no grant. It is safe under every import mode and under FB-33's proposed check, and cheapest before ADU-03 opens. (d) was added because R1's NEXT offered deferral; the plugin's own fix is noted as not offered.
**Deviations flagged:**
- D-1 "keeps item 4h": v1.1's D-1 had items 4a–4g only, so 4h (what the pack does not claim) is written new.
- B-3.16 sits before B-3.15, so R1's references to B-3.15 (the plan check) still hold.
- A `python3 -` heredoc used for a lookup hung (likely the Windows store alias) and runs on as a background task; stopping it was refused by the permission classifier. It writes nothing.
- Not committed. In the repository only the pack and this block were written; no governing document, code, test or protected path changed.
**Tests at close:** none — documents only. The scratch runs are measurements on exports, not this tree's gate.
**NEXT:**
1. This session: when the rehearsal ends, paste its output into B-4.3, B-3.15 and B-4.4, and append the closing block of this session.

## 2026-11-12 10:40 · design-change loop Q-07, stage 1 again (architect): pack v1.2, rehearsal pasted · done
**Done:**
- Continues the 10:28 block of this session: the full rehearsal ran and its output is pasted.
- B-4.3's script (803 lines) is re-run in full. Its output (416 lines) and the script are pasted into B-4.3, each byte-identical to the run. B-3.15's plan-check lines and guard lines are taken from the same output. B-4.4, the simulated apply, is new.
- Results of the run, all in scratch exports, never in the repository:
  - Blocks: 196 replace blocks (B 24, T 24, E 148) and 1 deletion, each at its line. All 1,088 rulings compose with 0 failures, the DECISIONS and Owed rows in id order and the open and blocking questions as expected.
  - Plan check: 144 distinct ADU-PLAN.md texts give `plan OK: 18 units`, the same output and exit 0, with the order as at 7d1e7d4.
  - The guard: the two completed tests are still refused at every stage of the change (FB-28). With the recommended plan text, ports.py, db.py, deps.py and tests/identity/test_identity_service.py are allowed and tests/identity/test_service.py refused. Under their options, tests/identity/__init__.py, pyproject.toml, tests/support/doubles.py, src/app/refusals.py and tests/layering.json are allowed.
  - E-10 measured: 3 errors as planned; 50 passed under (a) and under (b); 46 passed under (c) without the files and 50 with them.
  - Stages: gate 46 / 45 / 44 / 43 passed (44 / 42 / 40 / 38 of them the completed units' tests, as in v1.1, the rest the stand-ins' 2 / 3 / 4 / 5), lint clean at each. v1.1's twins are unchanged.
  - N-1 twin: 2 passed with the wiring right. With `require_caller` cut off from `get_session` it is 1 failed, and the full gate 1 failed, 45 passed. With `get_session` sync it is 1 failed.
  - E-10 twin: the four files under `test_service.py` give 3 errors.
  - Simulated apply of the recommended rulings (D-12 … D-18, Q-08 … Q-13, O-02): `ledgers OK`, `plan OK`, derived render 0 files, `derived blocks OK`, `pins OK (1 pinned)`. `adu status` prints "Open blocking questions: none" with Now: ADU-03, Q-12 as non-blocking and O-02 due ADU-04. Under E-5 (b) it lists Q-08 … Q-11 as STOP and Q-12 as non-blocking.
- `adu snapshot check 7d1e7d4` → OK against HEAD 99233a7 at close.
**Decisions:**
- The first full run's lint finding (E501, 112 > 110) was in the rehearsal's own stand-in test docstring, not in any pack text. The template was shortened and the whole script re-run, so the pasted output is one clean run.
**Deviations flagged:**
- This session wrote two journal blocks. The stop hook required one while the rehearsal still ran (10:28, in progress); this block closes it.
- The `python3 -` background task of the 10:28 block may still be waiting. It writes nothing.
- Not committed. In the repository only docs/PACK-q07-retire-amends.md and SESSION-JOURNAL.md changed; no governing document, code, test or protected path.
**Tests at close:** none — documents only. The scratch gates above are measurements on exports, not this tree's gate.
**NEXT:**
1. The operator commits: `git add docs/PACK-q07-retire-amends.md SESSION-JOURNAL.md` then `git commit -m "docs: pack q07-retire-amends v1.2, snapshot 7d1e7d4"`.
2. In a fresh `claude --plugin-dir C:\dev\adu-lifecycle --agent adu-lifecycle:verifier` started inside `C:\dev\team-rota`, paste Part D-1 of the pack (round R2; report docs/VERIFICATION-R2.md, named by hand, FB-31).
3. After R2's verdict, rule E-1 … E-10; the apply is Part D-2.

## 2026-11-12 16:08 · verification R2 · done
**Done:**
- Start checks:
  - `adu status`: Now: ADU-03; Q-07 open, blocking.
  - The three variables are as D-1 names them, and the interpreter line prints `C:\dev\team-rota-data\.venv cp1252 0`.
  - `git status --short` shows `?? uv.lock`; `adu role set verifier` ran.
  - `adu snapshot check 7d1e7d4` → OK against HEAD 1745ed2 (0 commits of drift).
- Read in full: pack v1.2 and docs/VERIFICATION-R1.md. Also read Q-07 (OPEN-QUESTIONS.md:53–59); the journal blocks of 2026-11-07 20:20, 2026-11-08 08:39, 18:34 and 22:45, and 2026-11-12 10:28 and 10:40; and plugin FEEDBACK.md rows FB-28 and FB-31–FB-33.
- docs/VERIFICATION-R2.md checks:
  - R1's dispositions;
  - every B-, T- and E-block;
  - A-2, row by row;
  - the guard;
  - the amendments, in both directions;
  - the arms;
  - E-10's table;
  - what the pack leaves unrehearsed.
- Measured, in the scratchpad only:
  - the pack's script, re-run: its output equals the pasted output apart from timings and paths;
  - my own parser and my own composition of the 1,088 rulings;
  - `adu plan check` and `adu plan order` over all 144 plan texts;
  - a 12 × 8 guard grid;
  - E-10 with my own stand-ins;
  - my own N-1 scaffold and twins;
  - a simulated apply on an export of HEAD, with D-12…D-18, Q-08…Q-13 and O-02.
- Gate once at HEAD: `46 passed, 1 warning in 20.44s`; lint clean; `git status --short` unchanged.
**Decisions:** none; the verifier rules nothing. Findings:
- S: none.
- N-1: E-6b.10 (and E-6a.9) tie ADU-03's arm 1 to "a request to a stubbed operation".
  - The API units move every operation out of the stubs, and ADU-08 deletes the stubs module. ADU-03's completed test would then go red, and no entry declares that edit.
  - Measured: the clause as worded fails once a router serves the probed operation. A form that registers its own probe route passes, and still fails under both twins.
- Notes:
  - the reason E-10 (c) gives for needing no grant (pyproject.toml is outside `code_roots`);
  - E-8 (b)'s scan line (:12, not :70);
  - several places that do not say they are unrehearsed;
  - ADU-11's route to `seed_admin`.
- R1's N-1, N-2, M-1–M-3, Notes and Q-p6 were all carried out.
**Deviations flagged:**
- The report was written in parts through Bash heredocs, then assembled from the scratchpad: one long heredoc failed to parse. This session has no Write tool.
- `adu next-id V` was not run (FB-31); the id R2 was named by hand.
- The B-5 and E-6 probes were not re-run: their sections are byte-identical to v1.1.
- Two copies of the pack's text were written to `/tmp/` by mistake during a comparison. They were outside the repository and were deleted at once.
- In the repository, only docs/VERIFICATION-R2.md and this block were written; all other scratch work is under the session scratchpad.
**Tests at close:** gate `46 passed, 1 warning in 20.44s`; lint `All checks passed!`; `adu verdict check docs/VERIFICATION-R2.md` → `verdict OK: VERDICT: STOP — MECHANICAL`.
**NEXT:**
1. The operator commits: `git add docs/VERIFICATION-R2.md SESSION-JOURNAL.md` then `git commit -m "docs: verification R2 of pack q07-retire-amends v1.2 (STOP — MECHANICAL)"`.
2. The architect revises the pack to v1.3 for N-1 (`/adu-lifecycle:change-design Q-07`, stage 1 again). That covers E-6b.10 and E-6a.9, B-4.3's stand-in test, and a twin in which a router serves the probed operation. The Notes are optional. Then a fresh verifier runs round R3.
3. Nothing is applied; ADU-03 stays blocked on Q-07.

## 2026-11-12 21:44 · design-change loop Q-07, stage 1 again (architect): pack v1.3 · done
**Done:**
- Start checks: `adu status` (Now: ADU-03; Q-07 open, blocking). The interpreter line printed `C:\dev\team-rota-data\.venv cp1252 0`, and `ADU_PLUGIN_ROOT` is `C:\dev\adu-lifecycle`. `adu snapshot check 7d1e7d4` → OK against HEAD 9fe1263 (0 commits of drift); the snapshot stays 7d1e7d4. Plugin HEAD is ae191e2 (FB-34 recorded); `git diff --stat 4b63bb0 ae191e2` lists FEEDBACK.md only.
- Read docs/VERIFICATION-R2.md in full, pack v1.2 in full, docs/VERIFICATION-R1.md §1, the R2 verifier's block of 2026-11-12 16:08 and plugin FB-29 and FB-34. Also read the entries of the thirteen later units (ADU-PLAN.md:170–525), src/app/main.py, src/app/api/deps.py, src/app/api/contract_stubs.py and the contract's paths.
- docs/PACK-q07-retire-amends.md revised to v1.3, dated 2026-11-12, `snapshot: 7d1e7d4`, status "verification pending (round R3)". Header line 3 maps each R2 finding to where it is handled; line 4 records the search for FB-34's class.
  - R2 N-1: E-6b.10 and E-6a.9 assert the request path through a route ADU-03's own test registers. The route sits at a path the contract does not declare and takes its caller from `Depends(app.api.deps.require_caller)`; it answers 200 with the seeded admin's id for an issued token and 401 for `Bearer garbage`. The clause sends no request to a contract operation and imports nothing from the stubs module. E-6 gives the reasons for R2's first fix, refined, over the second, and the thirteen later units it was checked against.
  - R2's notes: E-10 (c)'s grant reason (pyproject.toml outside `code_roots`) in E-10's table, E-10c.3, B-4.1 and A-2; E-8 (b)'s src/app/synthetic.py:12, now run; E-1 (b), E-4 (b), E-1b.3 and E-2b.3 rehearsed; E-7 (a), E-8 (b), E-9 (c) and E-7b.1 labelled as composed text; ADU-11's route to `seed_admin` (E-6b.1, E-6a.1, E-6, Q-p5); Part C's "five protocols" row; D-2 step 6's STATUS.md line.
  - The class search found three more: Q-p5's option (b) read the stubs module, now reworded; ADU-06's, ADU-10's and ADU-08's response-validation arms and main.py's import of the stubs module, added to Q-p5's Conflict; and the four retirement arms' gate clause, which now says no test of the arm's file repeats it.
  - A-2 gains seven rows and cites plugin ae191e2; A-3 gains FB-34's rule; the pack's references to itself read v1.3. D-1 is round R3's prompt, with 5h in both its parts; D-2's precondition is R3's verdict.
- B-4.3's script extended (1049 lines) and re-run in full; its output (472 lines) is pasted into B-4.3, and B-3.15's and B-4.4's excerpts are taken from the same run. Results, all in scratch exports, never in the repository:
  - Blocks: 196 replace blocks (B 24, T 24, E 148) and 1 deletion, each at its line. All 1,088 rulings compose with 0 failures, with the DECISIONS and Owed rows in id order and the open and blocking questions as expected. Plan check: the 144 distinct ADU-PLAN.md texts give `plan OK: 18 units`, one output, exit 0, the order as at 7d1e7d4.
  - The guard answers as in v1.2. pyproject.toml is allowed at 7d1e7d4, with B-3 and under E-10 (c): it lies outside `code_roots`.
  - E-10 as before: 3 errors as planned; 50 passed under (a) and under (b); 46 and 50 under (c).
  - Part 6, new:
    - E-1 (b), E-4 (b) and both: their T-text is applied, and T-09.2, T-05.2 and T-07.2 are found at :108/:106/:106 (either alone) and :106/:104/:104 (both): 32 of 32 checks OK. At stage T-03 with both, the gate is green (46 passed) and the lint clean; tests/test_ports.py passes with the stand-in TokenDirectory (4 passed).
    - E-2b.3: tests/test_layering.py passes with refusals.py joined (7 passed). A planted import of identity is caught once joined (1 failed: "ports->identity: forbidden"), and escapes without the join (7 passed).
    - The determinism scan finds src\app\synthetic.py:12 only, on the 7d1e7d4 tree and after the stages.
  - Stages: the gate gives 46 / 45 / 44 / 43 passed, lint clean at each; v1.1's twins are unchanged.
  - E-6b.10's clause: 2 passed with the wiring right. With `require_caller` cut off from `get_session` it is 1 failed, and the full gate 1 failed, 45 passed. With `get_session` sync it is 1 failed.
  - The API twins:
    - The clause's stand-in passes (2 passed) at ADU-07's close and with ADU-04, ADU-06, ADU-10 and ADU-08 landed (5, 11, 13 and 18 of 18 operations served by a router). The last twin deletes the stubs module, and no reference to it is left under src/.
    - v1.2's stand-in passes at ADU-07's close and fails in each API twin: `assert (200, None) == (501, 'not_built')`.
    - In the last twin the clause still fails under both mutations.
  - Simulated apply, as in v1.2: `ledgers OK`, `plan OK`, derived render 0 files, `derived blocks OK`, `pins OK (1 pinned)`. `adu status` prints "Open blocking questions: none" with Now: ADU-03, Q-12 as non-blocking and O-02 due ADU-04. Under E-5 (b), Q-08 … Q-11 are listed as STOP.
  - Checked after the paste: the pasted output equals the run's; the script in the pack is byte-identical to the one that ran; and a re-run of parts 1–3 on the final pack gives the same 255 lines.
**Decisions:**
- R2 N-1: R2's first fix, refined in four ways: `require_caller` taken from `app.api.deps` by name (`contract_stubs.CALLER_DEP` goes with ADU-08); a path outside the contract; the seeded admin's id, not only 200; and the arm forbids a contract request and a stubs import. The second fix was not chosen: it keeps a pin on a temporary state, adds ADU-03's test to four grants, and cannot be met after ADU-08.
- The main.py import of the stubs module, and the other API units' validation arms, are entered in Q-p5's Conflict, not in a question of their own: they are the same wall, owed before ADU-04 (O-p1).
- The four retirement arms keep their gate clause and say that no test of the arm's file repeats it, rather than dropping it: the gate still checks it at the unit's close.
**Deviations flagged:**
- A Bash heredoc for D-1's text failed to parse, as R2's journal reports for its own. The text was written into the scratchpad with the Write tool and spliced by a scratch script. The old output was replaced by a placeholder during drafting, and the placeholder by the new run's output.
- Not committed. In the repository only docs/PACK-q07-retire-amends.md and this block were written; no governing document, code, test or protected path changed.
**Tests at close:** none — documents only. The scratch gates above are measurements on exports, not this tree's gate.
**NEXT:**
1. The operator commits: `git add docs/PACK-q07-retire-amends.md SESSION-JOURNAL.md` then `git commit -m "docs: pack q07-retire-amends v1.3, snapshot 7d1e7d4 (after verification R2)"`.
2. In a fresh `claude --plugin-dir C:\dev\adu-lifecycle --agent adu-lifecycle:verifier` started inside `C:\dev\team-rota`, paste Part D-1 of the pack (round R3; report docs/VERIFICATION-R3.md, named by hand, FB-31).
3. After R3's verdict (READY, or READY WITH MECHANICAL ADAPTATIONS), rule E-1 … E-10; the apply is Part D-2. Nothing is applied before; ADU-03 stays blocked on Q-07.

## 2026-11-13 17:49 · verification R3 · done
**Done:**
- Start checks:
  - `adu status`: Now: ADU-03; Q-07 open, blocking.
  - The three variables are as D-1 names them, and the interpreter line prints `C:\dev\team-rota-data\.venv cp1252 0`.
  - `git status --short` shows `?? uv.lock`.
  - The plugin is at ae191e2; `git diff --stat 4b63bb0 HEAD` lists FEEDBACK.md only.
  - `adu snapshot check 7d1e7d4` → OK against HEAD d38925b (0 commits of drift); `adu role set verifier` ran.
- Read: pack v1.3 in full; docs/VERIFICATION-R2.md in full; docs/VERIFICATION-R1.md; Q-07 (OPEN-QUESTIONS.md:53–59); the journal blocks of 2026-11-07 20:20, 2026-11-08 08:39, 18:34 and 22:45, and 2026-11-12 10:28, 10:40, 16:08 and 21:44; plugin FEEDBACK.md rows FB-28, FB-29 and FB-31–FB-34; and the ADU-PLAN.md entries of every unit.
- docs/VERIFICATION-R3.md checks:
  - R2's N-1 and its six notes;
  - the header's line-4 search;
  - R1's dispositions against v1.3, by an own block-by-block diff with v1.2;
  - every B-, T- and E-block;
  - A-2, row by row;
  - the guard;
  - the amendments, in both directions;
  - the arms;
  - E-10's table;
  - what the pack does not claim, in both parts.
- Measured, in the scratchpad only:
  - the pack's script, re-run: its output equals the pasted run apart from timings, addresses and paths;
  - my own parser and my own composition of the 1,088 rulings;
  - `adu plan check` and `adu plan order` over all 144 plan texts;
  - an 18 × 10 guard grid;
  - my own scaffold of the clause's twins and of four API twins;
  - my own simulated apply on an export of HEAD (D-12…D-18, Q-08…Q-13, O-02), and under E-5 (b);
  - `adu derived check` after a gate change in adu.toml.
- Gate once at HEAD: `46 passed, 1 warning in 26.34s`; lint clean; `git status --short` unchanged.
**Decisions:** none; the verifier rules nothing. Findings:
- S: none. N: none. R2's N-1 and notes are carried out, and R1's dispositions hold in v1.3.
- M-1: the apply step enters this round's provisional Q-p7, non-blocking, with the next Q id (Q-14 if main took none).
- Q-p7 lies outside the pack, in M4, and comes from the search for FB-34's class. ADU-12's arms pin the placeholder routes, the gate string and D-09's exact set, and ADU-17's pins a placeholder page; ADU-17, ADU-13, ADU-14 and ADU-15 change each of them. ADU-15 also changes adu.toml's gate without declaring CLAUDE.md, whose derived block then goes stale (measured).
- Notes:
  - E-6's unit list leaves out ADU-05's conftest amendment, which is harmless;
  - E-6b.10's "an IdentityService method" can be met by a test of one method;
  - A-2 :59's wording is looser than the condition the clause needs;
  - four option-variant blocks go unnamed in the header's checked list.
**Deviations flagged:**
- The report was written in parts through Bash heredocs in the scratchpad and then concatenated: this session has no Write tool, and long heredocs fail to parse here, as R2's and the architect's blocks report.
- `adu next-id V` was not run (FB-31); the id R3 was named by hand.
- The B-5 and E-6 probes were not re-run: their sections are byte-identical to v1.2.
- My own scaffold's lint findings (one F401, two E501) are in my scratch files, not in pack text.
- In the repository, only docs/VERIFICATION-R3.md and this block were written; all other work is under the session scratchpad.
**Tests at close:** gate `46 passed, 1 warning in 26.34s`; lint `All checks passed!`; `adu verdict check docs/VERIFICATION-R3.md` → `verdict OK` on its last line, READY WITH MECHANICAL ADAPTATIONS.
**NEXT:**
1. The operator commits: `git add docs/VERIFICATION-R3.md SESSION-JOURNAL.md` then `git commit -m "docs: verification R3 of pack q07-retire-amends v1.3 (READY WITH MECHANICAL ADAPTATIONS)"`.
2. The operator rules E-1 … E-10 (Part E).
3. The apply is Part D-2, in a fresh release-manager session with the rulings pasted. Its step 4 makes M-1: Q-p7, from docs/VERIFICATION-R3.md §6, entered with the next Q id. Nothing is applied before that, and ADU-03 stays blocked on Q-07 until the apply resolves it.

## 2026-11-13 20:58 · design-change loop Q-07, stage 4: apply of pack q07-retire-amends v1.3 (release manager) · done
**Done:**
- Start checks:
  - The interpreter line printed `C:\dev\team-rota-data\.venv cp1252 0`. `UV_PROJECT_ENVIRONMENT`, `PYTHONUTF8` (empty) and `ADU_PLUGIN_ROOT` are as the prompt names them.
  - docs/VERIFICATION-R3.md (pack v1.3 at 7d1e7d4) ends `VERDICT: READY WITH MECHANICAL ADAPTATIONS`.
  - `adu snapshot check 7d1e7d4` → OK against HEAD 5b19ad8 (0 commits of drift), exit 0.
  - `git status --short` → `?? uv.lock`; `adu role set release-manager` ran.
- The operator's rulings, verbatim: E-1 (a), E-2 (a), E-3 (a), E-4 (a), E-5 (a), E-6 (b), E-7 (b), E-8 (a), E-9 (a), E-10 (a), and "E-11 (yes: Owed row O-03 due ADU-12 for Q-p7.)". This is the pack's recommended set, and every ruled option has text in the pack.
- Ids, from `adu next-id D|Q|O` at HEAD (D-12, Q-08, O-02: main took none):
  - D-p1 … D-p7 → D-12 … D-18;
  - Q-p1 … Q-p6 → Q-08 … Q-13, and R3's Q-p7 → Q-14;
  - O-p1 → O-02, and E-11's row → O-03.
  - Afterwards `adu next-id` answers D-19, Q-15 and O-04.
- Applied B-2.1–B-2.9, B-3.1–B-3.14 and B-3.16, then the 70 ruled E-blocks: E-5a.1–.14, E-6b.1–.10, E-7b.1–.5, E-8a.1–.4, E-9a.1–.3 and E-10a.1–.34.
  - A scratch script did it. Each block occurs once in its file and starts at its stated line: B against the 7d1e7d4 blob, which equals the working tree; E against the text as B leaves it.
  - Blocks went bottom-up and right to left. The shared DECISIONS anchor went E-10 first and E-6 last, so DECISIONS.md:17–23 stand D-12 … D-18.
  - Before substitution, design/INTERFACES.md:87–139 is byte-identical to the pack's composed excerpt (pack :1007–1059), and the OPEN-QUESTIONS headings and Owed rows agree with it.
  - Not applied: B-2.T (the retiring sessions', each under its grant) and E-9.P (the pm-lead's patch of design/PRODUCT-DESIGN.md:18).
- E-11: the operator's row is STATUS.md:33, O-03 due ADU-12, directly after O-02, with only the ids and the date substituted. R3's M-1: Q-14 is entered at OPEN-QUESTIONS.md:103–108 as R3 §6 writes it, non-blocking.
- Chase: every Part C row ran through `adu chase`, and so did "↔", `get_session`, "randomness", `<apply-date>` and `VERIFICATION-<id>`. No provisional id is left outside the pack, the verification reports and this journal. Each hit is changed, or stays with its reason, in docs/APPLICATION-REPORT-q07-retire-amends.md §3.
- Checks after the apply:
  - `adu derived render` → 0 files rewritten. `adu plan check` → `plan OK: 18 units`, and `adu plan order` is identical to B-3.15's 18 lines.
  - `adu derived check` → `derived blocks OK`; `adu ledger lint` → `ledgers OK`; `adu pins check` → `pins OK (1 pinned)`; `adu release check` → `release check OK`.
  - `adu status`: Now ADU-03. "Open blocking questions: none". Non-blocking: Q-02, Q-03, Q-05, Q-12 and Q-14. Owed: O-01 due ADU-11, O-02 due ADU-04 and O-03 due ADU-12. The last gate run is cited at STATUS.md:42.
- Versions: ADU-PLAN 1.2 → 1.3; design/INTERFACES.md 1.0.1 → 1.1, with its first Current row; design/ARCHITECTURE.md 1.1 → 1.2. Q-07 is resolved → D-12.
- docs/APPLICATION-REPORT-q07-retire-amends.md written from the plugin's template: the mapping, the changes, the chase, M-1 and E-11, the line mapping, what was not applied, and the findings.
**Decisions:**
- O-03's Approval cell quotes E-11 with the ids substituted ("…for Q-14."), as the prompt instructs and `adu ledger lint` requires. The operator's literal words are `E-11 (yes: Owed row O-03 due ADU-12 for Q-p7.)`.
- Q-14 and O-03 keep their ADU-PLAN.md citations as at 7d1e7d4 (:406, :407, :411, :436 …), entered character for character. In v1.3 every plan line from the old :285 on is +8, and the report's §4 maps each cited line.
- ADU-PLAN.md:2's "cut … on 2026-11-07 from … design/INTERFACES.md v1.0.1 and design/ARCHITECTURE.md v1.1" is a chase hit Part C does not list. It stays: it is dated provenance and true as written, and VERSIONS.md holds the current versions. It is an editorial candidate for the next plan patch, with INTERFACES.md:2's stale "each with a `Null<Interface>` in the contract unit" (Part C).
**Deviations flagged:**
- This block is appended before the gate and its Tests line filled after, as the journal's header and the session protocol require. The prompt's step 6 lists the gate first.
- The STATUS Log line is typed in the shape of the M1 close line, because `adu log-line` takes only an ADU-nn.
- `adu audit` is not one of the apply's checks. After the apply it reports 13 "dangling" findings; on a HEAD export it reports none of that kind (its one finding there is O-01, owed). All 13 are "plugin FB-28/32/33/34" citations, which the audit reads as this project's FEEDBACK ids. This is plugin feedback, for the operator to carry upstream.
- No grant was asked for or used. No test, code, contract or protected path changed, and the pack was not edited. Not committed: the operator commits.
**Tests at close:** gate `46 passed, 1 warning in 15.97s` (`uv run pytest tests/ -q -m "not timing"`, run once, after this block was appended; the interpreter line printed `C:\dev\team-rota-data\.venv cp1252 0`). That is the count STATUS.md:42 records, and this loop changed no test. Lint `All checks passed!` (`uv run ruff check`). `git status --short` was unchanged by both. STATUS Log line: STATUS.md:43.
**NEXT:**
1. The operator commits: `git add ADU-PLAN.md DECISIONS.md OPEN-QUESTIONS.md STATUS.md VERSIONS.md design/ARCHITECTURE.md design/INTERFACES.md docs/APPLICATION-REPORT-q07-retire-amends.md SESSION-JOURNAL.md`, then `git commit -m "docs: apply pack q07-retire-amends (ADU-PLAN v1.3, INTERFACES v1.1, ARCHITECTURE v1.2)"`. `uv.lock` stays untracked (Q-05).
2. The ADU-03 hand-over. The oversight session regenerates `adu handover ADU-03` and checks it against the entry (ADU-PLAN.md:138–172); its section A expects "Open blocking questions: none". The hand-over must say:
   - "design updated: ADU-PLAN v1.3 (ADU-03's amends, tests and arm 1; the same pattern in ADU-09, ADU-05, ADU-07), INTERFACES v1.1 (§Refused, §Domain services — the request's session and IdentityService, the retirement paragraph), ARCHITECTURE v1.2 (§Layers, §Persistence and concurrency rules)";
   - in its first section, the two grants the session asks the operator for, `tests/api/test_contract_conformance.py` and `tests/test_nulls.py`, because the guard does not honour `amends` on a completed unit's test (plugin FB-28);
   - in its roster, the `amends` files, which C1 omits (plugin FB-30 (1)): src/app/main.py, src/app/ports.py, src/app/identity/null_directory.py (deleted), and under E-6 (b) src/app/db.py and src/app/api/deps.py. None of these needs a grant, because none is a test. Its test file is tests/identity/test_identity_service.py (E-10 (a));
   - that O-02, due ADU-04, is listed by `adu status` and is not ADU-03's, and neither is O-03, due ADU-12.
   The pm-lead's E-9.P patch follows in a pm-lead session and does not block ADU-03.

## 2026-11-13 21:30 · hand-over ADU-03 (oversight) · done
**Done:** The apply of pack q07-retire-amends v1.3 (`3b306ab`) audited against the pack: ADU-PLAN.md, design/INTERFACES.md and design/ARCHITECTURE.md are byte-identical (line endings normalised) to the oversight session's own simulated apply of the operator's rulings from the pack's script; DECISIONS.md and VERSIONS.md differ only by the apply date; the remaining differences are R3's Q-14, the operator's O-03 row and the Log line. `adu plan check` OK (18 units, order unchanged), `adu derived check`, `adu ledger`, `adu pins check` OK; `adu status`: Now ADU-03, open blocking questions none. No code or test changed since 7d1e7d4 (`git diff --stat 7d1e7d4 HEAD -- tests src pyproject.toml adu.toml` empty), so the pack's T-03.1–T-03.10 apply at their stated lines. `adu handover ADU-03` regenerated (exit 0) and checked (D-0) against the entry; corrected for the generator's known faults (plugin FB-19, FB-24, FB-17, FB-28, FB-30): Windows paths, `--plugin-dir`, the amends files in the roster, the two hard-rule-1 grants, the interpreter line, both last lines, staging by name instead of `git add -A` (Q-05).
**The operator's gate of the apply, a fresh Windows PowerShell on the applied tree before the commit:** `C:\dev\team-rota-data\.venv cp1252 0` · `46 passed, 1 warning in 16.42s` · `All checks passed!`. (The STATUS Log line of the apply records the release manager's own run, 15.97s.)
**Decisions:** the two grants for the completed tests are given in the hand-over's session prompt, scoped to exactly the pack's T-03.1–T-03.6 and T-03.7–T-03.10, as the operator's in-session approval; the session records each with `/adu-lifecycle:grant` before its first edit of that file. Arm 1's no-session clause is to be tested on every MemberDirectory method and every IdentityService operation, not one (R3 note on E-6b.10).
**Tests at close:** none run by this session; no code, test or plan text changed.
**NEXT:** ADU-03 in a fresh `claude --plugin-dir C:\dev\adu-lifecycle --agent adu-lifecycle:developer` started inside `C:\dev\team-rota`, from the hand-over the oversight session gave the operator; expected gate after the unit: 44 of today's tests (46 less the NullDirectory case of the shared parametrised test and the NullDirectory test) plus ADU-03's new tests.

## 2026-11-13 21:50 · ADU-03 · done
**Done:**
- Start checks. `adu status`: Now ADU-03; open blocking questions none; plan check OK; no other 🔨 row. Interpreter line `C:\dev\team-rota-data\.venv cp1252 0`. Read the last journal block, the open Q-02, Q-03, Q-05, Q-12 and Q-14, the ADU-03 entry (ADU-PLAN.md:138–172), design/INTERFACES.md §Refused, §Domain services, §IdentityService and §Composition root bindings, design/ARCHITECTURE.md §Layers and §Persistence and concurrency rules, DECISIONS D-12 … D-18, the identity spec, US-identity-001 … 005, US-notifications-006, the identity operations of contracts/openapi.yaml and docs/PACK-q07-retire-amends.md B-2.T. ADU-03 marked 🔨 at 2026-11-13 21:24 (STATUS.md:12).
- Tests first: the qa-engineer subagent drafted tests/identity/test_identity_service.py (54 test functions, 117 cases) from the seven arms and the public interfaces before any implementation body existed, and falsified it against a throwaway reference outside the repository (each deliberate break turned at least one case red). Accepted unchanged. Every arm is asserted there; the no-session clause is parametrised over all six MemberDirectory methods and all six IdentityService operations; nothing is labelled vacuous (three twins carry information only beside their refusal partners, as their docstrings say).
- src/app/ports.py gains `Refused(reason, detail="", **extra)` beside TransferRefused; nothing else changed (D-13).
- src/app/db.py gains `NoCurrentSession`, `current_session()`, `use_session(session)` and `unit_of_work(engine)` over one private ContextVar; engine_for and session_for unchanged (D-14).
- src/app/api/deps.py: `get_session` is an async generator dependency that makes the request's session current with `db.use_session` and closes it on the way out; `require_caller` depends on it; ProblemError, problem_response and engine_of unchanged. get_session now precedes require_caller because `Depends(get_session)` is evaluated at definition.
- src/app/identity/repo.py (member rows in the passed session) and src/app/identity/service.py: `IdentityService(bound, source)` implements MemberDirectory and seed_admin, add_member, change_role, deactivate, sign_in and list_members, with `Bindings`, `TokenSource`, `SecretsSource`, `MemberValue`, `SignInValue` and `MemberSummary` (D-15, D-16, D-17).
- src/app/main.py binds `IdentityService(lambda: app.state.ports, SecretsSource())` as `Ports.member_directory`; the NullDirectory import and binding are gone. src/app/identity/null_directory.py is deleted (retires MK-04).
- Before the retirement step the new file ran 115 passed, 2 failed: exactly the two retirement assertions (the file exists; tests/api/test_contract_conformance.py and tests/test_nulls.py import it). Then the two grants below were recorded, and T-03.1 … T-03.10 applied by a script that extracts each block verbatim from the pack and checks it occurs once at its stated line (all ten did). `git diff -- tests/api/test_contract_conformance.py` and `git diff -- tests/test_nulls.py` show exactly those blocks' edits and nothing else.
**Grant (hard rule 1), operator, 2026-11-13 21:48, in session:** tests/api/test_contract_conformance.py (ADU-02's completed test). Permitted: lines 1–3, 19, 23, 61, 102 and 105, exactly the edits T-03.1 … T-03.6 of docs/PACK-q07-retire-amends.md (B-2.T, from line 268), character for character, and nothing else. The operator's words in this session's prompt: "Grant 1: tests/api/test_contract_conformance.py — exactly the edits T-03.1 … T-03.6 of docs/PACK-q07-retire-amends.md, character for character, and nothing else. Reason: Q-07 ruled option 1; D-12." Measurement: with src/app/identity/null_directory.py deleted (arm 1), the module's import at line 23 fails its collection (pack A-1, B-4.3 twin 1), and with the identity service bound, `Bearer tok_1` resolves to no member, so the 401/501 loop at line 61 answers 401 (pack B-4.3). The guard does not honour `amends` on a completed unit's test (plugin FB-28). Machine grant: `adu grant add be512191-8ee2-4a05-b723-901747954877 tests/api/test_contract_conformance.py "Q-07 ruled option 1; D-12: T-03.1-T-03.6 only"`.
**Grant (hard rule 1), operator, 2026-11-13 21:48, in session:** tests/test_nulls.py (ADU-16's completed test). Permitted: lines 11, 17, 28 and 36–45, exactly the edits T-03.7 … T-03.10 of the same pack, character for character, and nothing else. The operator's words: "Grant 2: tests/test_nulls.py — exactly the edits T-03.7 … T-03.10 of the same pack, character for character, and nothing else. Reason: Q-07 ruled option 1; D-12." Measurement: the run of tests/identity/test_identity_service.py before the retirement step (115 passed, 2 failed) named tests/api/test_contract_conformance.py and tests/test_nulls.py as the modules under src/ and tests/ that still import app.identity.null_directory. Machine grant: `adu grant add be512191-8ee2-4a05-b723-901747954877 tests/test_nulls.py "Q-07 ruled option 1; D-12: T-03.7-T-03.10 only"`.
**Decisions:**
- Every method takes `db.current_session()` before any check, so with none current each raises NoCurrentSession whatever its arguments (D-14; design/INTERFACES.md §Domain services).
- Refusal order forbidden → not_found → state → validation, and within the state bucket the story's arm order (design/PRODUCT-DESIGN.md:14; R-identity-08). Hence deactivate asks `scheduling.has_assignment_after(member, clock.now())` of every found target, then last_admin, then member_inactive (US-identity-003 arms 3–5; INTERFACES §IdentityService deactivate row).
- change_role on the team's only active admin with an invalid or missing role answers last_admin, not invalid_role: state precedes validation (PRODUCT-DESIGN.md:14), the same order as add_member's duplicate_email before invalid_role, which the tests assert. This corner itself is not asserted (the qa-engineer's ambiguity 1, settled by that line).
- An email is stored as given and compared case-insensitively with Python's str.lower (models.py:73–74, R-identity-02). That is never weaker than the store's `lower(email)` index, because SQLite's lower folds ASCII only. Names sort by (name.lower(), id) (R-identity-09).
- team_not_empty is answered for a team with any member, active or inactive (US-identity-005 arm 2: "any member").
- A passcode is checked by recomputing models.hash_passcode with the stored salt, compared with hmac.compare_digest. A missing passcode counts as wrong (INTERFACES §IdentityService). Tokens are compared exactly.
- The bindings are read once per call through `bound()` (D-15). Refusal details follow the contract's example sentences where it has one; tests assert `.reason` only (INTERFACES §Refused).
**Deviations flagged:**
- Journal time order. The previous block is stamped 21:30, after this session started (session mark 21:21; `adu status` 21:22). The in-progress block I appended at 21:25, when the stop hook asked for one, made `adu init --check` (tests/test_method.py) and `adu ledger lint` fail with "SESSION-JOURNAL.md:618: block is out of time order". This block, rewritten in place at close, carries its close time, 21:50. For the operator: the oversight block's stamp is ahead of the clock.
- design/ARCHITECTURE.md:31 admits sqlalchemy at layer 1. repo.py and service.py (layer 3) import it (select, func, Session), as ADU-02's deps.py (layer 4) and contract_stubs.py (layer 2) already do. No package is added (hard rule 2), and tests/layering.json constrains product modules only. I read the column as where a package is admitted, not as an import wall, because the layer-3 repo.py the architecture names (ARCHITECTURE.md:13) cannot query without it. Not raised as a Q-nn; it is for the architect's next touch.
- ADU-PLAN.md's derived Mocks block still lists MK-04 as "active (provider not built)", and `adu derived check` passes. ADU-PLAN.md is outside this roster; its regeneration belongs to the closure.
- Q-02 (non-blocking) is built as written: deactivation does not touch the member's open requests. uv.lock stays untracked (Q-05). Nothing is committed.
**Tests at close:** gate `161 passed, 1 warning in 19.74s` (`uv run pytest tests/ -q -m "not timing"`, run once, after this block was appended; the interpreter line printed `C:\dev\team-rota-data\.venv cp1252 0`). That is 44 of the 46 earlier tests (46 less the NullDirectory case of the shared parametrised test and test_null_directory_resolves_synthetic_tokens_and_answers_the_empty_value) plus the 117 cases of tests/identity/test_identity_service.py. The warning is the starlette `httpx` deprecation the earlier gates show. Lint `All checks passed!` (`uv run ruff check`). Not the operator's run: ✅ is written from theirs.
**NEXT:** the operator runs the gate `uv run pytest tests/ -q -m "not timing"` and the lint `uv run ruff check` under their own hands, reviews the diff, and commits by name (`uv.lock` stays untracked, Q-05); then the closure prompt from `adu handover ADU-03 --closure`, which writes ✅ from the pasted gate output.

## 2026-11-14 07:20 · ADU-03 closure · done
**Done:**
- Start checks. `adu status` showed Now ADU-03, no open blocking questions and plan check OK. The last journal block is 2026-11-13 21:50 · ADU-03 · done, and its Tests at close counts 161 (SESSION-JOURNAL.md:643). HEAD was ee12929 ("ADU-03: Identity service"), and `git status --short` showed only `?? uv.lock`.
- The operator's three lines, verbatim. The operator ran them under their own hands, in a fresh PowerShell, on the tree they then committed:
  - `interpreter: C:\dev\team-rota-data\.venv cp1252 0`
  - `gate (uv run pytest tests/ -q -m "not timing"): 161 passed, 1 warning in 39.25s`
  - `lint (uv run ruff check): All checks passed!`
  Each meets the prompt's condition. The interpreter line is identical, the gate shows 161 passed with no failures (the count in ADU-03's block), and the lint is clean.
- STATUS.md:12: ADU-03 is now ✅, Completed 2026-11-14 07:20, Tests 161. Started and the unit's Log line (STATUS.md:44) are unchanged, and no Log line was added.
- STATUS.md:4: `## Now: ADU-09`, the unit after ADU-03 in `adu plan order` (6 of 18). ADU-09 stays ☐.
- Owed: no row is due at ADU-03 (O-01 is due at ADU-11, O-02 at ADU-04, O-03 at ADU-12), so none changed.
- Checks:
  - `adu ledger lint`: `ledgers OK`.
  - `adu derived check`: `ADU-PLAN.md: derived block "plan mocks" is stale (regenerate: adu derived render)`, exit 2. It named nothing else.
  - `adu derived render`: `1 file(s) rewritten`. `git diff ADU-PLAN.md` shows one line: MK-04's status went from `active (provider not built)` to `retired`.
  - Re-run: `adu derived check` gives `derived blocks OK` and `adu ledger lint` gives `ledgers OK`.
  - `adu plan mocks`: `MK-04 | MemberDirectory | in-process | ADU-02 | ADU-03 | retired`. MK-01, MK-02 and MK-03 remain active (provider not built).
- `adu status` after the change: Now ADU-09 — Notifications service · size S · layer 3 (domain services) · position 6/18. Depends: ADU-01, ADU-02, ADU-03 and ADU-16, all ✅.
**Decisions:**
- The Completed stamp is this session's clock when the row was written, in the ledger's `yyyy-MM-dd HH:mm` shape (STATUS.md:2: "Stamps are ISO local date-time"). The Tests cell is the operator's count.
- ADU-PLAN.md was changed by `adu derived render` alone, never by hand. Its diff is the MK-04 line.
**Deviations flagged:**
- None from the prompt. No grant was asked for or used. No code, test, contract, plan text or protected path changed. uv.lock stays untracked (Q-05). Nothing is committed.
- For information only, since timing never gates:
  - The operator's gate took 39.25s; the unit session's took 19.74s.
  - `adu status` still cites STATUS.md:43 as "Last gate run" (46 passed in 15.97s). It does not cite ADU-03's Log line at :44, because the `adu log-line` shape `gate in 19.74s` carries no pass count.
**Tests at close:** this session ran no gate. The unit closes on the operator's gate `161 passed, 1 warning in 39.25s` and lint `All checks passed!` above. After this block was appended: `adu ledger lint` gave `ledgers OK`, `adu init --check` gave `init OK: manifest of 13 files present, pins match, ledgers lint clean`, and `adu derived check` gave `derived blocks OK`.
**NEXT:**
1. The operator commits by name: `git add STATUS.md ADU-PLAN.md SESSION-JOURNAL.md`, then `git commit -m "ADU-03: closure"`. `uv.lock` stays untracked (Q-05).
2. ADU-09 — Notifications service. Its first action: the oversight session generates and checks `adu handover ADU-09` (the D-0 check against ADU-09's plan entry) and gives the operator the hand-over for a fresh developer session.

## 2026-11-14 07:58 · hand-over ADU-09 (oversight) · done
**Done:** ADU-03 closed on `main` (`ee12929` the unit, `c3d0ac0` the closure; the operator's gate `161 passed, 1 warning in 39.25s`, `All checks passed!`, interpreter `C:\dev\team-rota-data\.venv cp1252 0`). `adu status`: Now ADU-09 (size S, position 6/18), open blocking questions none, MK-04 retired. `adu handover ADU-09` generated (exit 0) and checked (D-0) against the entry: the pack's T-09.1–T-09.6 match the two completed tests at HEAD exactly once at their stated lines (checked with the pack's block parser); no file but the declared ones names the NullNotifier (`git grep`); the Notification model exists (src/app/models.py:134); the contract settles the values (`Notification`, `notifications.list`, `notifications.mark_read`) and R-notifications-01–04 the behaviour; D-14 (the current session) and D-15 (built from the bindings) apply. design/INTERFACES.md has no §NotificationsService: the session derives the two read operations only from the arms, the contract and the spec, with D-17's reading (the contract's shapes as frozen values in the service module) as the precedent, records each choice with its source, and stops with a Q-nn on any point those do not settle. The generated hand-over corrected for plugin FB-17, FB-19, FB-24, FB-28, FB-30, as at ADU-03.
**Raised:** Q-15 (non-blocking): ARCHITECTURE.md:31 admits sqlalchemy at layer 1 only; layers 3 and 4 import it (ADU-03's deviation 2).
**Tests at close:** none run by this session; no code or test changed.
**NEXT:** ADU-09 in a fresh `claude --plugin-dir C:\dev\adu-lifecycle --agent adu-lifecycle:developer` inside `C:\dev\team-rota`, from the oversight session's hand-over; expected gate after the unit: 159 of today's 161 (less the NullNotifier case of the shared parametrised test and test_null_notifier_records_and_writes_nothing) plus ADU-09's new tests.

## 2026-11-14 08:34 · ADU-09 · done
**Done:**
- Start checks. `adu status` showed Now ADU-09, open blocking questions none and plan check OK, with no other 🔨 row. The interpreter line is `C:\dev\team-rota-data\.venv cp1252 0`. I read the last journal block and Q-02, Q-03, Q-05, Q-12, Q-14 and Q-15 (all open and non-blocking). I also read the ADU-09 entry (ADU-PLAN.md:173–198), design/INTERFACES.md §Notifier, §Refused, §Domain services, §IdentityService and §Composition root bindings (with the retirement paragraph), design/ARCHITECTURE.md, DECISIONS D-12 … D-18, the notifications spec, US-notifications-001 … 006, the contract's `notifications.list`, `notifications.mark_read` and `Notification`, and src/app/models.py's Notification (line 134). Last, docs/PACK-q07-retire-amends.md T-09.1 … T-09.6 (from line 387); each target occurs once at its stated line at HEAD. ADU-09 is marked 🔨 at 2026-11-14 08:08 (STATUS.md).
- Tests first. Before any implementation body existed, the qa-engineer subagent drafted tests/notifications/test_notifications_service.py (25 test functions, 82 cases) from the four arms and the public interface derived below. It falsified the file against a throwaway reference outside the repository (the scratchpad's `qa09` mirror). Each deliberate break turned at least one case red: sort by id only, commit inside notify, read the row's `active` instead of asking the directory, text from the directory's name, no dedupe, skip MemberDeactivated too, mark another member's, a session of its own. I accepted the file unchanged. Every arm is asserted there. The no-session clause covers notify (twice, once with every recipient inactive), list and mark_read, with a self-test. Its twins are the import scan's 11 forms, the nine-event coverage checks and the text check's 10 cases (a control and nine single faults). Nothing is labelled vacuous; the docstring says which skip cases pass for a service that writes nothing, and which test fails such a service.
- src/app/notifications/repo.py adds, gets and lists rows, the recipient's own newest first (models.Notification), in the passed session. src/app/notifications/service.py holds `NotificationsService(bound)`, which implements ports.Notifier, with `list` and `mark_read`, `Bindings`, `NotificationValue`, `recipients_of` and `text_of`.
- src/app/main.py binds `NotificationsService(lambda: app.state.ports)` as `Ports.notifier`. The NullNotifier import and binding are gone, and src/app/notifications/null_notifier.py is deleted (retires MK-02).
- Before the retirement step the new file ran 80 passed, 2 failed: exactly the two retirement assertions (the Null exists; the two tests import it). With the Null deleted it ran 81 passed, 1 failed (the import scan, offenders as measured below). Then the two grants below were recorded, and a script (the scratchpad's `apply_t09.py`) applied T-09.1 … T-09.6. It extracts each block verbatim from the pack, checks the block occurs once in its file at its stated line, and replaces whole lines bottom-up in the file's own line endings. `git diff -- tests/api/test_contract_conformance.py` and `git diff -- tests/test_nulls.py` show exactly those six blocks' edits and nothing else. `git ls-files --eol` is unchanged (i/lf w/crlf). The new file then ran 82 passed.
**Grant (hard rule 1), operator, 2026-11-14 08:32, in session:** tests/api/test_contract_conformance.py (ADU-02's completed test), lines 24 and 110 only. Permitted: exactly the edits T-09.1 and T-09.2 of docs/PACK-q07-retire-amends.md (B-2.T, from line 387), character for character, and nothing else. T-09.1 deletes the NullNotifier import line. T-09.2 changes the class check `isinstance(p.notifier, NullNotifier)` to `isinstance(p.notifier, ports.Notifier)`. The operator's words in this session's prompt: "Grant 1: tests/api/test_contract_conformance.py — exactly the edits T-09.1 and T-09.2 of docs/PACK-q07-retire-amends.md, character for character, and nothing else. Reason: Q-07 ruled option 1; D-12." Measurement: with src/app/notifications/null_notifier.py deleted (arm 1) and the notifications service bound, test_arm1_no_module_under_src_or_tests_imports_the_null_notifier fails with offenders `['tests/api/test_contract_conformance.py', 'tests/test_nulls.py']` (81 passed, 1 failed). The guard does not honour `amends` on a completed unit's test (plugin FB-28). Machine grant: `adu grant add d2ad74b6-c61a-4e93-b49c-93f8b9e6f77c tests/api/test_contract_conformance.py "Q-07 ruled option 1; D-12: T-09.1-T-09.2 only"`.
**Grant (hard rule 1), operator, 2026-11-14 08:32, in session:** tests/test_nulls.py (ADU-16's completed test), lines 11, 18, 28 and 48–53 only. Permitted: exactly the edits T-09.3 … T-09.6 of the same pack, character for character, and nothing else. They delete the NullNotifier import, its REPLACED entry and its protocol-map entry, and test_null_notifier_records_and_writes_nothing together with the two blank lines before it. The operator's words: "Grant 2: tests/test_nulls.py — exactly the edits T-09.3 … T-09.6 of the same pack, character for character, and nothing else. Reason: Q-07 ruled option 1; D-12." Measurement: the same scan names tests/test_nulls.py. Machine grant: `adu grant add d2ad74b6-c61a-4e93-b49c-93f8b9e6f77c tests/test_nulls.py "Q-07 ruled option 1; D-12: T-09.3-T-09.6 only"`.
**Decisions:** design/INTERFACES.md has no §NotificationsService. Each choice below comes from the arms, the contract, the spec, D-14 and D-15, with D-17's reading as the precedent.
- Construction (D-15). `NotificationsService(bound)` takes one zero-argument callable and reads `.clock` and `.member_directory` at call time. `Bindings` is a Protocol of those two in the service module; the attribute names are main.Ports's fields, so Ports satisfies it and notifications imports neither main nor identity. main.py binds `NotificationsService(lambda: app.state.ports)`, and a test passes `lambda: SimpleNamespace(clock=…, member_directory=…)`.
- The read side's signatures:
  - Names and caller. `list(caller)` and `mark_read(caller, notification_id)` follow arm 3's names and the contract's operationIds `notifications.list` and `notifications.mark_read`, the way identity's methods follow `identity.<action>`. They take the `Caller` because §Domain services says "every operation a signed-in member performs takes the Caller".
  - Values. Both answer `NotificationValue`, a `@dataclass(frozen=True)` in src/app/notifications/service.py with the contract's six Notification fields (id, recipient_id, event, text, created_at, read). The contract's 200s answer an array of Notification and one Notification (contracts/openapi.yaml:548–590, :863), so `list` answers `list[NotificationValue]` and `mark_read` the row with read true (D-17's reading: the contract's shape as a frozen value beside the service, which the API layer maps). `created_at` is the naive datetime the model stores (models.py:141; the contract's "naive local date-time").
- Sessions (D-14). Every method takes `db.current_session()` before anything else, so with none current each raises `db.NoCurrentSession`, even a notify with nobody to write to. notify adds and flushes each row (repo.add) and never commits; the caller's unit of work or request commits.
- Recipients:
  - Who gets one (R-notifications-01, -03; IR-04). They come from the payload's own field (recipient_ids, recipient_id or member_id), deduplicated in payload order. Each is checked with `member_directory.is_active`, never the members row. A recipient it does not answer active for is skipped, except for MemberDeactivated, which is written without asking.
  - Unknown ids. "Not active" includes None, an id naming no member (ports.py:190), which no arm covers and no emitter produces; no branch or test was added for it.
  - The clock and other events. The clock is read once per notify, so one event's rows share a created_at. An object that is not one of the nine events raises TypeError, never a silent drop (R-notifications-01: no other event notifies).
- Text (R-notifications-02; arm 4):
  - Source and shape. Composed from the payload alone. The date is ISO and the start HH:MM, as the contract's examples render them. Names, the role and the reason code appear verbatim, and no id is shown.
  - "Names the state as it is" is read as the strictly stronger form: the past participle of the event's code appears (published, requested, accepted, declined, approved, refused, added, changed, deactivated), with what is still pending where something is ("it awaits your answer" for requested, "it awaits a decision" for accepted; the North Star's "what is still pending"). No later state is claimed.
  - Declined and refused texts also carry the shift's date and start. Their stories' arms (US-notifications-003, -004) name only the name and the reason, but the payload carries both and arm 4's list names "date and start". The tests do not require them there.
- mark_read refusals. not_found comes first, for an id naming nothing; then not_recipient, for another member's. The forbidden check needs the row, so R-identity-08's forbidden → not_found order cannot apply before the row exists; US-notifications-005 arms 2 and 3 name both outcomes. A repeat leaves read true and writes nothing. The details follow the contract's example ("This notification is not yours."); the tests assert `.reason` only (INTERFACES §Refused).
- The T-09 blocks were applied as whole-line replacements, an empty "with:" deleting the lines. That is the convention ADU-03's T-03 edits show at ee12929.
**Deviations flagged:**
- Q-16 (raised, non-blocking). The contract's swap_requested example text, "Mo asks you to take 2026-11-09 08:00–14:00 (sick)." (contracts/openapi.yaml:563, :582 and :872), carries an end time that SwapRequested does not (design/INTERFACES.md:64), so no text composed from the payload alone (R-notifications-02, ADU-09 arm 2) can reproduce it. This file's text twin also marks the example's phrasing as a fault (`no-state-word`). ADU-09 builds to the arm (authority 4 before 6). The raiser recommends (a): the architect rewrites the three examples before ADU-10 opens.
- ADU-PLAN.md's derived Mocks block still lists MK-02 as "active (provider not built)". ADU-PLAN.md is outside this roster; its regeneration (`adu derived render`) belongs to the closure, as at ADU-03.
- Q-15 (open, non-blocking): src/app/notifications/repo.py imports sqlalchemy (`select`, `Session`) as identity's repo does. No package is added (hard rule 2).
- The deletion was staged by `git rm` and then unstaged with `git reset -q -- src/app/notifications/null_notifier.py`, so the index is as HEAD left it.
- uv.lock stays untracked (Q-05). O-01, O-02 and O-03 are not this unit's. Nothing is committed.
**Tests at close:** gate `241 passed, 1 warning in 23.32s` (`uv run pytest tests/ -q -m "not timing"`, run once, after this block was appended; the interpreter line printed `C:\dev\team-rota-data\.venv cp1252 0`). That is 159 of the 161 earlier tests plus the 82 cases of tests/notifications/test_notifications_service.py. The two that left are the NullNotifier case of the shared parametrised test and test_null_notifier_records_and_writes_nothing, both of tests/test_nulls.py. The warning is the starlette `httpx` deprecation the earlier gates show. Lint `All checks passed!` (`uv run ruff check`). After the gate, this session wrote the Log line, this paragraph and Q-16 (ledgers only, no code or test). It then ran `uv run pytest tests/test_method.py -q` and `adu ledger lint` on the final tree; the results are in the closing message. Not the operator's run: ✅ is written from theirs.
**NEXT:** the operator runs the gate `uv run pytest tests/ -q -m "not timing"` and the lint `uv run ruff check` under their own hands and reviews the diff. Then they commit by name: src/app/notifications/service.py, src/app/notifications/repo.py, the deletion of src/app/notifications/null_notifier.py, src/app/main.py, tests/notifications/test_notifications_service.py, tests/api/test_contract_conformance.py, tests/test_nulls.py, STATUS.md, SESSION-JOURNAL.md and OPEN-QUESTIONS.md (Q-16) (`uv.lock` stays untracked, Q-05). Then comes the closure prompt from `adu handover ADU-09 --closure`, which writes ✅ from the pasted gate output and regenerates the derived Mocks block (MK-02 retired).

## 2026-11-14 09:05 · ADU-09 closure · done
**Done:**
- Start checks. `adu status` showed Now ADU-09, no open blocking questions and plan check OK. The last journal block is 2026-11-14 08:34 · ADU-09 · done, and its Tests at close counts 241 (SESSION-JOURNAL.md:714). HEAD was a7e0630 ("ADU-09: Notifications service"), and `git status --short` showed only `?? uv.lock`.
- The operator's three lines, verbatim. The operator ran them under their own hands, in a fresh PowerShell, on the tree they then committed:
  - `interpreter: C:\dev\team-rota-data\.venv cp1252 0`
  - `gate (uv run pytest tests/ -q -m "not timing"): 241 passed, 1 warning in 34.73s`
  - `lint (uv run ruff check): All checks passed!`
  Each meets the prompt's condition. The interpreter line is identical, the gate shows 241 passed with no failures (the count in ADU-09's block), and the lint is clean.
- STATUS.md:18: ADU-09 is now ✅, Completed 2026-11-14 09:04, Tests 241. Started and the unit's Log line (STATUS.md:45) are unchanged, and no Log line was added.
- STATUS.md:4: `## Now: ADU-05`, the unit after ADU-09 in `adu plan order` (7 of 18). ADU-05 stays ☐.
- Owed: no row is due at ADU-09 (O-01 is due at ADU-11, O-02 at ADU-04, O-03 at ADU-12), so none changed.
- Checks:
  - `adu ledger lint`: `ledgers OK`.
  - `adu derived check`: `ADU-PLAN.md: derived block "plan mocks" is stale (regenerate: adu derived render)`, exit 2. It named nothing else.
  - `adu derived render`: `derived blocks rendered (1 file(s) rewritten)`. `git diff ADU-PLAN.md` shows one line: MK-02's status went from `active (provider not built)` to `retired`.
  - Re-run: `adu derived check` gives `derived blocks OK` and `adu ledger lint` gives `ledgers OK`.
  - `adu plan mocks`: `MK-04 | MemberDirectory | in-process | ADU-02 | ADU-03 | retired` and `MK-02 | Notifier | in-process | ADU-03 | ADU-09 | retired`. MK-01 (SchedulingPort, provider ADU-05) and MK-03 (SwapsPort, provider ADU-07) remain active (provider not built).
- `adu status` after the change: Now ADU-05 — Scheduling service · size M · layer 3 (domain services) · position 7/18. Depends: ADU-00, ADU-01, ADU-02, ADU-03, ADU-09 and ADU-16, all ✅. Consumes through mocks: MK-03 (SwapsPort ← ADU-07, in-process).
**Decisions:**
- The Completed stamp is this session's clock when the row was written, in the ledger's `yyyy-MM-dd HH:mm` shape (STATUS.md:2: "Stamps are ISO local date-time"). The Tests cell is the operator's count.
- ADU-PLAN.md was changed by `adu derived render` alone, never by hand. Its diff is the MK-02 line.
**Deviations flagged:**
- None from the prompt. No grant was asked for or used. No code, test, contract, plan text or protected path changed. uv.lock stays untracked (Q-05). Nothing is committed.
- For information only, since timing never gates:
  - The operator's gate took 34.73s; the unit session's took 23.32s.
  - `adu status` still cites STATUS.md:43 as "Last gate run" (46 passed in 15.97s), as at ADU-03's closure: the `adu log-line` shape `gate in 23.32s` (STATUS.md:45) carries no pass count.
**Tests at close:** this session ran no gate. The unit closes on the operator's gate `241 passed, 1 warning in 34.73s` and lint `All checks passed!` above. After this block was appended: `adu ledger lint` gave `ledgers OK`, `adu init --check` gave `init OK: manifest of 13 files present, pins match, ledgers lint clean`, and `adu derived check` gave `derived blocks OK`.
**NEXT:**
1. The operator commits by name: `git add STATUS.md ADU-PLAN.md SESSION-JOURNAL.md`, then `git commit -m "ADU-09: closure"`. `uv.lock` stays untracked (Q-05).
2. ADU-05 — Scheduling service. Its first action: the oversight session generates and checks `adu handover ADU-05` (the D-0 check against ADU-05's plan entry) and gives the operator the hand-over for a fresh developer session.

## 2026-11-14 14:20 · hand-over ADU-05 (oversight) · done
**Done:** ADU-09 closed on `main` (`a7e0630` the unit, `68d11fc` the closure; the operator's gate `241 passed, 1 warning in 34.73s`, `All checks passed!`, interpreter `C:\dev\team-rota-data\.venv cp1252 0`). `adu status`: Now ADU-05 (size M, position 7/18), open blocking questions none, MK-02 and MK-04 retired. `adu handover ADU-05` generated and checked (D-0) against the entry: the pack's T-05.1–T-05.6 match the two completed tests at HEAD exactly once at their stated lines (the pack's block parser); no file but the declared ones names NullSchedulingPort (`git grep`); `tests/conftest.py` is one of ADU-00's `files`, not its `tests`, so ADU-05's amendment needs no grant, and `tests/test_tiers.py::test_no_tier_pattern_is_stale` requires the registered timing node to exist; the identity tests use FakeSchedulingPort, so the rebinding leaves them unchanged. The generated hand-over corrected for plugin FB-17, FB-19, FB-24, FB-28, FB-30, as before.
**Ledgers, with the operator's approval:** O-04 (due ADU-10, Q-16), the operator in this session, verbatim: "O-04 approved: Owed row due ADU-10 for Q-16." Raised: Q-17 (non-blocking), the Notifier's skip of a recipient unknown to identity, which ADU-09 chose and nothing pins.
**Tests at close:** none run by this session; no code or test changed.
**NEXT:** ADU-05 in a fresh `claude --plugin-dir C:\dev\adu-lifecycle --agent adu-lifecycle:developer` inside `C:\dev\team-rota`, from the oversight session's hand-over; expected gate after the unit: 239 of today's 241 (less the NullSchedulingPort case of the shared parametrised test and test_null_scheduling_port_does_nothing_observable) plus ADU-05's new gate tests; the timing test is deselected by the gate.

## 2026-11-14 14:36 · ADU-05 · blocked
**Done:**
- Start checks:
  - `adu status`: Now ADU-05, open blocking questions none, plan check OK, no other 🔨 row.
  - Interpreter line: `C:\dev\team-rota-data\.venv cp1252 0`.
- Read:
  - The last journal block (2026-11-14 14:20, hand-over ADU-05) and Q-02, Q-03, Q-05, Q-12, Q-14, Q-15, Q-16 and Q-17, all open and non-blocking.
  - The ADU-05 entry (ADU-PLAN.md:200–230).
  - design/INTERFACES.md: §SchedulingPort, §SwapsPort, §Notifier, §Refused, §Domain services, §IdentityService, and §Composition root bindings with the retirement paragraph.
  - design/ARCHITECTURE.md §Persistence and concurrency rules, and DECISIONS D-12 … D-18.
  - The scheduling spec, US-scheduling-001 … 006 and US-notifications-001.
  - The contract's six scheduling operations and their schemas.
  - PRODUCT-DESIGN's cross-cutting rules and Reason codes table: the refusal order the contract's description refers to.
  - Code: src/app/synthetic.py (`seeded_week`, `load_fixture`), src/app/ports.py, src/app/models.py, src/app/db.py, src/app/main.py and src/app/identity/service.py.
  - Tests: tests/support/doubles.py, tests/conftest.py and tests/test_tiers.py.
  - T-05.1 … T-05.6 of docs/PACK-q07-retire-amends.md (from line 450). Each target occurs at its stated line at HEAD: tests/api/test_contract_conformance.py:24 and :108; tests/test_nulls.py:11, :15, :24 and :30.
  - ADU-06's arms (ADU-PLAN.md:311, :313), only to quote them in Q-18.
  - The rest of what this session read, each for its reason:
    - src/app/identity/repo.py: the repo pattern, and Q-15's sqlalchemy import.
    - src/app/scheduling/null_port.py and src/app/swaps/null_port.py: the Null retired and the mock consumed (MK-01, MK-03).
    - tests/layering_scan.py and tests/layering.json: arm 6's layering assertion, and the scheduling → swaps edge, which is forbidden.
    - pyproject.toml: pytest's `pythonpath`, for the timing script's `--measure` mode.
    - The docstring of tests/notifications/test_notifications_service.py: the test-file pattern to hand the qa-engineer.
    - The pack's rehearsal stand-ins (docs/PACK-q07-retire-amends.md:1540–1600 and :1740–1770), found while searching for any recorded SchedulingService shape. They hold only a stand-in SchedulingPort and the rebinding line, so no board shape is recorded there.
    - OPEN-QUESTIONS.md's Q-04 and Q-07 (after Q-18 was written): how a ruling is recorded.
- STATUS.md:14 marks ADU-05 🔨 at 2026-11-14 14:30.
- I stopped before the tests: the sources the hand-over names leave the layout of the board and of create_shift's answer open (Q-18, blocking). Nothing else was done:
  - No qa-engineer draft, test file or source file was written.
  - No grant was recorded or used.
  - src/app/main.py, src/app/scheduling/null_port.py, tests/conftest.py and the two completed tests are untouched.
**Decisions:** none taken. The parts of the derivation that are settled are written into Q-18's "Assumed under every option": the construction (D-15), the six signatures, the other four values, create_shift's inputs, the date and time types, and the refusal order per operation. The three port cases no arm names are Q-19, so one ruling of Q-18 and Q-19 covers the service's whole interface.
**Deviations flagged:**
- Q-18 (raised, blocking): the layout of the board and of create_shift's answer. The arms give `{start_date, state, shifts: [{id, date, start, end, slots, holders}]}` and "the shift with its holder-rows". The contract gives `Board`, `BoardShift` and `Shift`, which is what the hand-over's D-17 reading asks for. The raiser recommends (a): the arms' layout, with `week_start` kept on the shift row.
- Q-19 (raised, non-blocking): three port cases no arm names:
  - transfer to an unknown member;
  - which reason transfer answers when the counterpart both overlaps and is inactive;
  - holds_intersecting_shift for an unknown shift.
  The raiser recommends (a), pinned by no test.
- Timing route (information for the architect; no question): the plan's arm as written can still be built.
  - US-scheduling-004's timing arm says "50 sequential calls through the in-process test client". ADU-05's arm 7 does not.
  - The board's route answers 501 until ADU-06, and ADU-06's entry has no timing arm.
  - So ADU-05 can only time the service call, and no unit measures the HTTP-level figure.
- No Log line was written. `adu log-line` needs a gate count and duration, and for a session that ran no gate its line reads "done · 0 tests · gate in 0:00", which would be untrue.
- uv.lock stays untracked (Q-05). Nothing is committed.
**Tests at close:** none run; no code or test changed (only STATUS.md, OPEN-QUESTIONS.md and this block).
**NEXT:**
1. The operator rules on Q-18, and Q-19 with it.
2. The ruling is recorded in OPEN-QUESTIONS.md before anything is built, the way Q-07 records one: a `**Ruling:**` line with the operator's words, and the heading changed from `open` to `resolved → …`. Until Q-18 is resolved, `adu status` prints "Open blocking questions: Q-18 … STOP", and every session stops on that.
   - Options (a) and (c) change no document: this session records the ruling if the operator gives it here, otherwise the oversight session does.
   - Option (b) rewords ADU-05's arms 2 and 5: it goes through `/adu-lifecycle:change-design Q-18`, and that loop's apply step resolves the entry.
3. A fresh ADU-05 hand-over that quotes the ruling starts at step (1), the qa-engineer's draft. ADU-05 stays 🔨 (Started 2026-11-14 14:30), and the operator decides whether that session restamps it.

## 2026-11-14 15:43 · ADU-05 · rulings recorded (Q-18, Q-19) · done
**Done:** The operator ruled on Q-18 and Q-19 in this session. Recorded in OPEN-QUESTIONS.md and nowhere else:
- Q-18:
  - The heading now reads `resolved → operator's ruling (no document change)`.
  - Its Resolution line holds the ruling verbatim, dated 2026-11-14, in the ADU-05 session: "Q-18: (a). The arms' layout: BoardValue(start_date, state, shifts), each shift a ShiftRow(id, week_start, date, start, end, slots, holders); create_shift answers the same ShiftRow with holders=(); ADU-06 maps the board onto the contract's Board. The "Assumed under every option" list in Q-18 is accepted as written. D-17 names the IdentityService only: for this service the arms come first, and the contract only where the arms are silent."
- Q-19:
  - Its heading stays open, and Blocking stays no.
  - A new Ruling line, "option (a) for the build, the operator, 2026-11-14, in the ADU-05 session", quotes the ruling verbatim: "Q-19: (a) for this unit's build, not pinned by a test. (c) stays owed: the architect writes the three answers into design/INTERFACES.md §SchedulingPort at the next INTERFACES patch, together with Q-15 and Q-17."
  - Its Resolution line now reads "none yet — (c) owed at the next INTERFACES patch".
- Nothing was built:
  - No qa-engineer draft, test file or source file, and no grant was recorded.
  - STATUS.md is unchanged: ADU-05 stays 🔨, Started 2026-11-14 14:30.
**Decisions:** none taken by this session; both rulings are the operator's.
**Deviations flagged:** none new.
**Tests at close:** none run; no code or test changed (only OPEN-QUESTIONS.md and this block).
**NEXT:** a fresh ADU-05 session, from a new hand-over generated by the oversight session that quotes the rulings of Q-18 and Q-19.

## 2026-11-14 18:05 · hand-over ADU-05, second (oversight) · done
**Done:** After the operator's rulings of Q-18 (option (a), resolved, OPEN-QUESTIONS.md:133–190) and Q-19 (option (a) for the build, (c) owed, :192–209), `adu handover ADU-05` checked again (D-0) at `87c5f29`: Now ADU-05 (🔨 since 14:30), open blocking questions none; the pack's T-05.1–T-05.6 still match the two completed tests at their stated lines (no code or test changed since 14:20). The first hand-over's source order was wrong: it named D-17's contract-shape reading as a source for every service value, which D-17 does not say (it names the IdentityService), and that is how Q-18 arose; the second hand-over states the order the documents give (CLAUDE.md's authority: the plan's arms, then the design, then the contract only where the arms are silent) and quotes both rulings. Added to the D-0 check from now on: every value shape an arm states is compared with the contract's before the hand-over is given.
**Tests at close:** none run by this session; no code or test changed.
**NEXT:** ADU-05 in a fresh `claude --plugin-dir C:\dev\adu-lifecycle --agent adu-lifecycle:developer` inside `C:\dev\team-rota`, from the second hand-over; expected gate after the unit: 239 of today's 241 plus ADU-05's new gate tests; the timing test is deselected by the gate and run once, reported.
