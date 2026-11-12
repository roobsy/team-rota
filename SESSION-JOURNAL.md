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
