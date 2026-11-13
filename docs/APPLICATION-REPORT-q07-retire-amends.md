# APPLICATION-REPORT — docs/PACK-q07-retire-amends.md v1.3 applied on 2026-11-13
documents only · no file under the code roots changed · verdict applied: READY WITH MECHANICAL ADAPTATIONS (docs/VERIFICATION-R3.md, last line)

Release-manager session, 2026-11-13 20:46–, on `main` at HEAD 5b19ad8. Preconditions, each checked before the first edit:
- The interpreter line, `uv run python -c "import sys, locale; print(sys.prefix, locale.getpreferredencoding(False), sys.flags.utf8_mode)"`, printed `C:\dev\team-rota-data\.venv cp1252 0`.
- `UV_PROJECT_ENVIRONMENT` = `C:\dev\team-rota-data\.venv`, `PYTHONUTF8` empty, `ADU_PLUGIN_ROOT` = `C:\dev\adu-lifecycle` (plugin HEAD ae191e2).
- docs/VERIFICATION-R3.md (header: "docs/PACK-q07-retire-amends.md v1.3 at 7d1e7d4") ends `VERDICT: READY WITH MECHANICAL ADAPTATIONS`.
- `adu snapshot check 7d1e7d4` → "snapshot OK: 7d1e7d4 is an ancestor of HEAD 5b19ad8; governing documents unchanged since (0 commit(s), allowed 0)", exit 0.
- `git status --short` → `?? uv.lock` (Q-05).
- `adu role set release-manager`.

The operator's rulings, verbatim, pasted at the end of the apply prompt:
```
E-1 (a)
E-2 (a)
E-3 (a)
E-4 (a)
E-5 (a)
E-6 (b)
E-7 (b)
E-8 (a)
E-9 (a)
E-10 (a)
E-11 (yes: Owed row O-03 due ADU-12 for Q-p7.)
```
There is one option for each of E-1–E-5 and E-10. E-5 is (a), and there is one option for each of E-6–E-9. Every ruled option has text in the pack: E-1, E-2, E-3 and E-4 (a) have no E-block of their own (they are B as written, or B-2.T), and E-5a, E-6b, E-7b, E-8a, E-9a and E-10a do. The ruling is the pack's recommended set (B-4.3's "recommended options"). E-11 is not a bracket of Part E: it is the operator's approval, given in the oversight session, of an Owed row for R3's Q-p7 (§4).

## 1. Identifier mapping (re-derived against HEAD)
`adu next-id D` → `D-12`, `adu next-id Q` → `Q-08`, `adu next-id O` → `O-02` at HEAD 5b19ad8, before any edit: main took none. Ids were allocated in the order they stand. After the apply, `adu next-id` answers `D-19`, `Q-15` and `O-04`.

| Provisional | Allocated | Where (after the apply) |
|---|---|---|
| D-p1 | D-12 | DECISIONS.md:17; cited at OPEN-QUESTIONS.md:53 (Q-07 → D-12), :59, :92; VERSIONS.md:120, :123; design/INTERFACES.md:2, :152 |
| D-p2 | D-13 | DECISIONS.md:18; OPEN-QUESTIONS.md:59; VERSIONS.md:123; design/INTERFACES.md:80 |
| D-p3 | D-14 | DECISIONS.md:19; OPEN-QUESTIONS.md:59, :61, :66; VERSIONS.md:123–125; design/INTERFACES.md:90, :106, :138; design/ARCHITECTURE.md:2, :42, :52 |
| D-p4 | D-15 | DECISIONS.md:20; OPEN-QUESTIONS.md:59, :68, :73; VERSIONS.md:125; design/INTERFACES.md:109 |
| D-p5 | D-16 | DECISIONS.md:21; OPEN-QUESTIONS.md:59, :75, :80; VERSIONS.md:125; design/INTERFACES.md:114; design/ARCHITECTURE.md:2, :45, :52 |
| D-p6 | D-17 | DECISIONS.md:22; OPEN-QUESTIONS.md:59, :82, :87; VERSIONS.md:120, :124; design/INTERFACES.md:2, :128 |
| D-p7 | D-18 | DECISIONS.md:23; OPEN-QUESTIONS.md:59, :96, :101; VERSIONS.md:120, :123 |
| Q-p1 | Q-08 | OPEN-QUESTIONS.md:61 (entered resolved → D-14); cited at :59, DECISIONS.md:19 |
| Q-p2 | Q-09 | OPEN-QUESTIONS.md:68 (resolved → D-15); :59, DECISIONS.md:20 |
| Q-p3 | Q-10 | OPEN-QUESTIONS.md:75 (resolved → D-16); :59, DECISIONS.md:21 |
| Q-p4 | Q-11 | OPEN-QUESTIONS.md:82 (resolved → D-17); :59, DECISIONS.md:22 |
| Q-p5 | Q-12 | OPEN-QUESTIONS.md:89 (open, `**Blocking:** no`); :59, STATUS.md:32 (O-02), VERSIONS.md:123, design/INTERFACES.md:92 |
| Q-p6 | Q-13 | OPEN-QUESTIONS.md:96 (resolved → D-18); :59, DECISIONS.md:23, VERSIONS.md:120, :123 |
| Q-p7 (R3 §6, M-1) | Q-14 | OPEN-QUESTIONS.md:103 (open, `**Blocking:** no`); STATUS.md:33 (O-03) |
| O-p1 | O-02 | STATUS.md:32, due ADU-04; cited at OPEN-QUESTIONS.md:59, :91, VERSIONS.md:123 |
| O-p7 (E-11's row) | O-03 | STATUS.md:33, due ADU-12 |

O-p2 does not exist: E-10 is (a), not (d). Every `<apply-date>` in the applied text reads `2026-11-13`, and every `docs/VERIFICATION-<id>.md` reads `docs/VERIFICATION-R3.md`. Substitutions made: D-12 ×8, D-13 ×4, D-14 ×13, D-15 ×6, D-16 ×9, D-17 ×9, D-18 ×6, Q-08 ×3, Q-09 ×3, Q-10 ×4, Q-11 ×3, Q-12 ×7, Q-13 ×5, Q-14 ×4, O-02 ×4, O-03 ×1. No provisional id is left in any tracked file outside the pack, the three verification reports and the journal (`git grep -nE "\b[DQO]-p[0-9]+\b"` with those excluded: no line).

O-03's Approval cell quotes E-11. The operator's literal words are `E-11 (yes: Owed row O-03 due ADU-12 for Q-p7.)`. The cell reads "…for Q-14.)" because the prompt substitutes both ids throughout the row, and `adu ledger lint` refuses a provisional id in a ledger. The literal words are kept here and in the journal block.

## 2. Changes, document by document
Applied by a script in the session scratchpad. It parses the pack's 196 replace blocks (B 24, T 24, E 148), as B-4.3 and R3 count them. Each B-block is checked against the 7d1e7d4 blob, which equals the working tree for every file touched. Each E-block is checked against the text as B leaves it. Each block occurs once in its file and starts at its stated line; whole-line blocks match whole lines. Blocks are applied bottom-up, right to left within a line. The DECISIONS rows share one anchor and go E-10, E-9, E-8, E-7, E-6, so they stand D-14 … D-18. Line endings stay CRLF, UTF-8 without BOM. Before ids were substituted, the composed text was compared with the pack's own excerpts of the recommended ruling. design/INTERFACES.md:87–139 is byte-identical to the pack's lines 1007–1059, and so are the OPEN-QUESTIONS headings (Q-07 … Q-p6, pack :994–1000). The Owed rows agree with pack :1002–1004.

| Document | From | To | What changed |
|---|---|---|---|
| ADU-PLAN.md | 1.2 | 1.3 | B-3.1 (header), B-3.2 (Shape of the cut), B-3.3–B-3.14 (the amends lines and retirement arms of ADU-03, ADU-09, ADU-05 and ADU-07), B-3.16 (ADU-04's pointer, now :292); E-6b.6 (ADU-03 amends src/app/db.py and src/app/api/deps.py, :153–154), E-6b.10 (arm 1's request-path clause, :163); E-10a.1–.28 (the four `tests:` lines and 24 arm files renamed `tests/<domain>/test_<domain>_service.py`). 525 → 533 lines; every line from the old :285 on moves by +8 |
| design/INTERFACES.md | 1.0.1 | 1.1 | B-2.2 (header), B-2.3 (§Refused, §Domain services, §IdentityService), B-2.4 (the retirement paragraph), B-2.5 (US-identity-005's trace); E-5a.6 (header: D-12–D-17); E-6b.1–.4 (the request's session; IdentityService in `db.current_session()`); E-7b.1, E-7b.4 (the `bound` constructor; three service cycles); E-8a.1 (the `TokenSource`); E-9a.1 (the frozen values). 124 → 187 lines. The Current row it lacked is added (B-2.8) |
| design/ARCHITECTURE.md | 1.1 | 1.2 | E-5a.7–.9 (header version and the decisions it rests on; §Decisions), E-6b.5 (:42, the request's session, D-14), E-7b.5 (:18, three cycles), E-8a.2 (:45, the one exception to "no randomness", D-16) |
| DECISIONS.md | — | — | D-12, D-13 (B-2.1); D-14 (E-6b.8), D-15 (E-7b.2), D-16 (E-8a.3), D-17 (E-9a.2), D-18 (E-10a.29), at :17–:23 in id order |
| OPEN-QUESTIONS.md | — | — | Q-07 resolved → D-12, with its Resolution line (B-2.6, B-2.7, E-5a.1, E-10a.30). Q-08–Q-13 entered (B-2.7). Q-08–Q-11 resolved (E-5a.2–.5, E-6b.9, E-7b.3, E-8a.4, E-9a.3) and Q-13 resolved (E-10a.31–.32). Q-12 open and non-blocking. Q-14 entered open and non-blocking (R3 M-1, §4) |
| VERSIONS.md | — | — | Current: ARCHITECTURE 1.2 (E-5a.10), the new INTERFACES 1.1 row, ADU-PLAN 1.3 (B-2.8). History: the section "2026-11-13 — ADU-PLAN v1.3, INTERFACES v1.1, ARCHITECTURE v1.2" (B-2.9, E-5a.11–.13, E-6b.7, E-10a.33–.34) |
| STATUS.md | — | — | Owed: O-02 due ADU-04 (E-5a.14) and O-03 due ADU-12 (E-11, the operator's row, with only its two ids and the date substituted). The Log line of this apply. The gate line `adu status` cites moves from :40 to :42 |
| SESSION-JOURNAL.md | — | — | this session's block |

Unchanged: contracts/ (yaml, json, golden), PINS.lock, adu.toml, CLAUDE.md, .claude/, every file under src/ and tests/. design/PRODUCT-BRIEF.md is unchanged (`adu pins check` → "pins OK (1 pinned)").

## 3. Chase — every renamed or redefined term, grepped into every artefact
Every row of Part C was run as `adu chase "<old>" "<new>"` after the apply, which covers the tracked .md/.py/.ts/.json/.yaml/.toml files. Hits in docs/PACK-q07-retire-amends.md, docs/VERIFICATION-R1/R2/R3.md and SESSION-JOURNAL.md are records and stay; Part C's preamble lists the ledgers, docs/PLAN-REVIEW-1.md and design/DESIGN-REVIEW-*.md as records too. Line numbers are as after the apply.

| Old → new | Hits (file:line), records left out | Changed · left (why) |
|---|---|---|
| "test_contract_conformance.py still passes" → B-3.3's text (4 hits) | OPEN-QUESTIONS.md:54 | changed at ADU-PLAN.md:151 (B-3.3). :54 is Q-07's Conflict, quoting the arm as raised: stays |
| "the contract unit's tests stay green unchanged" → B-3.5's clause (5) | OPEN-QUESTIONS.md:54 | changed at ADU-PLAN.md:163 (B-3.5); :54 stays (record) |
| "and its test_nulls test are deleted" → the widened arms (8) | OPEN-QUESTIONS.md:54 | changed at ADU-PLAN.md:163, :193, :222, :253 (B-3.5, .8, .11, .14); :54 stays |
| "test is deleted with its stub" → the four-place edit (5) | none | changed at ADU-PLAN.md:156, :189, :216, :249 (B-3.4, .7, .10, .13) |
| "stay green unchanged" → stays (26) | ADU-PLAN.md:153, :193, :222, :253; OPEN-QUESTIONS.md:54; docs/PLAN-REVIEW-1.md:5 | stays. :153 is D-14's new db.py line (ADU-01's tests). :193, :222 and :253 say the identity and scheduling suites use the doubles, which is true as written (Part C). :54 and PLAN-REVIEW-1 are records |
| "deleting the Null and its stub test" → B-3.2's text (2) | none | changed at ADU-PLAN.md:6 (B-3.2) |
| "one test per Null" → stays (6) | ADU-PLAN.md:102; tests/test_nulls.py:1 | stays: ADU-16's completed arm and its completed test's docstring; ADU-07 removes the file (T-07.3) |
| "the Null until ADU-03" / "the Null until its provider lands" → stays (5, 10) | ADU-PLAN.md:129, :132, :152; OPEN-QUESTIONS.md:54; docs/PLAN-REVIEW-1.md:5 | stays. :129 and :132 are ADU-02's arms, history and still true. :152 is B-3.3's new line quoting the docstring ADU-03 writes (T-03.1) |
| "golden still equal" / "golden unchanged" / "gone once the last router lands" → stays (2, 4, 7) | ADU-PLAN.md:128, :280, :307, :333; src/app/api/contract_stubs.py:9; docs/PLAN-REVIEW-1.md:9, :37 | stays: these are not retirements of a Null. The API units' wall is Q-12, owed as O-02 |
| `Refused` → D-13, §Refused (153) | ADU-PLAN.md:157, :164, :165 (ADU-03's ports.py line, arms 2–3); :227, :256, :258; DECISIONS.md:18; design/INTERFACES.md:41, :44, :68, :72, :79–:93, :130, :184; src/app/ports.py:36, :123, :158, :193; tests/support/doubles.py:70; tests/test_ports.py:60, :83; contracts/openapi.yaml:286, :410 (and the json and golden) | stays. The new term is defined at design/INTERFACES.md:79 (D-13). `TransferRefused`, `SwapRefused` and the contract's "Refused by a … rule" are other names. "refuses <code>" in later arms means `Refused(<code>)` (Part C) |
| `IdentityService` → §IdentityService (133) | ADU-PLAN.md:145, :151, :163, :241, :265, :275, :292, :378; design/ARCHITECTURE.md:45 | stays, and now resolves to design/INTERFACES.md:103 |
| "five protocols" → stays (13) | ADU-PLAN.md:99; VERSIONS.md:91 (Part C's :90, moved by B-2.8); tests/test_ports.py:1 | stays: `Refused` is an exception, not a protocol |
| "No randomness in the product" → E-8a.2 (10) | design/ARCHITECTURE.md:45; OPEN-QUESTIONS.md:76 | changed at ARCHITECTURE.md:45 (E-8a.2). :76 is Q-10's Conflict as raised: stays. Beside it, CLAUDE.md:33 (hard rule 5, "randomness only through a passed generator") stays: D-16 records that the source is passed |
| "a member as the team list shows it" → E-9.P (9) | design/PRODUCT-DESIGN.md:18; DECISIONS.md:22; OPEN-QUESTIONS.md:83; design/DESIGN-REVIEW-7.md:36 | left for the pm-lead: PRODUCT-DESIGN.md:18 is E-9.P's patch, not this apply (§6). D-17 records that the contract supersedes the line until then. The rest are records |
| "two cycles (…)" / "identity ↔ scheduling (IR-05 / IR-06) and scheduling ↔ swaps" → three cycles (4, 3) | none | changed at design/ARCHITECTURE.md:18 (E-7b.5) and design/INTERFACES.md:155 (E-7b.4). Also grepped as "↔": design/INTERFACE-REQUESTS.md:4 already names all three cycles (DESIGN-REVIEW-4 A8), so it agrees; the DESIGN-REVIEW hits are records |
| "One session and one write transaction per request" → stays, D-14 after it (2) | design/ARCHITECTURE.md:42 | stays, with E-6b.5's sentences appended. Also grepped as `get_session`: src/app/api/deps.py:50 (a sync generator today) and src/app/api/contract_stubs.py:23, :28 are code. ADU-03 rewrites `get_session` under its declared amends (ADU-PLAN.md:154, D-14), not this apply (documents only) |
| `tests/{identity,notifications,scheduling,swaps}/test_service.py` → `test_<domain>_service.py` (15, 10, 11, 10) | none | changed at ADU-PLAN.md's four `tests:` lines and 24 arm files (E-10a.1–.28). `test_service.py` alone: DECISIONS.md:23 (D-18) and OPEN-QUESTIONS.md:97 (Q-13's Conflict) name the old shape on purpose: stay |
| `test_the_composition_root_binds_a_null_per_port_and_an_injectable_clock` → `…_an_implementation_per_port_…` (3) | tests/api/test_contract_conformance.py:102 | left for ADU-03's session, which renames it under its grant (T-03.5, E-4 (a)); the apply edits no test |
| design/INTERFACES.md v1.0.1 → v1.1 (11; "1.0.1": 15) | design/INTERFACES.md:2; VERSIONS.md:102, :108, :124; ADU-PLAN.md:2; docs/PLAN-REVIEW-1.md:47, :54, :78 | changed at INTERFACES.md:2 (B-2.2) and VERSIONS Current (B-2.8). VERSIONS :102 and :108 are history, and :124 is this apply's From cell. **ADU-PLAN.md:2** is not in Part C: "cut … on 2026-11-07 from stories v1.7 (D-02), contracts/openapi.yaml v1.1, design/INTERFACES.md v1.0.1 and design/ARCHITECTURE.md v1.1". It stays: the clause is dated provenance of the 2026-11-07 cut and true as written, and VERSIONS.md, which wins on any disagreement, holds the current versions. A rewording is no text of the pack; it is an editorial candidate for the next plan patch (§7) |
| ADU-PLAN v1.2 → v1.3 (1; "ADU-PLAN v1.2": 6) | VERSIONS.md:115; FEEDBACK.md:21; RETRO.md:16, :17 | changed at ADU-PLAN.md:2 (B-3.1) and VERSIONS Current (B-2.8); the rest are history and records |
| Q-07 open, blocking → resolved → D-12 (161) | OPEN-QUESTIONS.md:53, :58, :59; ADU-PLAN.md's `q: Q-07` lines and :2, :6, :292; design/INTERFACES.md:2; VERSIONS.md:120; DECISIONS.md:17 | changed at OPEN-QUESTIONS.md:53, :59 (B-2.6, B-2.7). The plan cites Q-07 only, because plan check refuses a provisional id. `adu status`: "Open blocking questions: none" |
| Q-p5 "blocking ADU-04" → `**Blocking:** no`, owed by O-02 (2) | none | Q-12 is entered non-blocking (OPEN-QUESTIONS.md:91), with O-02 (STATUS.md:32) and ADU-04's pointer (ADU-PLAN.md:292) |
| "each with a `Null<Interface>` in the contract unit" → stays (2) | design/INTERFACES.md:2 | stays, as Part C rules: stale since v1.0.1 moved the Nulls to ADU-16; an editorial fix for the next INTERFACES patch (§7) |
| `<apply-date>`, `docs/VERIFICATION-<id>.md` (38, 15) | none | every one in the applied text replaced (2026-11-13; docs/VERIFICATION-R3.md) |
| the ADU-03 hand-over → regenerated after the apply | — | the oversight session's step (the journal block's NEXT): it must list the amends files and the two grant steps (plugin FB-30 (1), FB-28) |

## 4. Mechanical adaptations made (from the verification report)
| M-n | Adaptation | Where |
|---|---|---|
| M-1 | R3 §6's Q-p7 entered as written between its fences, character for character, with its id allocated by `adu next-id Q` after Q-08–Q-13 → Q-14. It goes after the last line of the Q-13 entry (Q-p6) that B-2.7 and E-10a leave, with one blank line before its heading, `**Blocking:** no` | OPEN-QUESTIONS.md:103–108 |

No pack block, Part E option or Owed row was changed by M-1, and the pack itself was not edited. `adu status` lists Q-14 among the open non-blocking questions and prints "Open blocking questions: none".

**E-11 (the operator's approval; not an M-n).** The row given in the apply prompt is appended to STATUS.md's Owed table directly after O-02's row. Q-p7 → Q-14, O-p7 → O-03 and `<apply-date>` → 2026-11-13 are substituted, and nothing else is changed (STATUS.md:33). `adu status` lists "O-03 due ADU-12".

**Line citations in the entries this apply wrote.** Q-08–Q-14 and O-03 cite ADU-PLAN.md and design/INTERFACES.md as at 7d1e7d4, because they were entered character for character. In this apply's text some of the cited lines have moved. This is the mapping (difflib, HEAD against the working tree); content was checked at each new line.

design/INTERFACES.md, cited by Q-08 (:44, :77) and Q-09 (:82, :92): :44 and :77 do not move. :82, the §Composition root bindings heading, is now :143. :92, the cycles line, is now :155, amended by E-7b.4. design/ARCHITECTURE.md's :18, :42 and :45 keep their numbers and are amended in place (E-7b.5, E-6b.5, E-8a.2).

ADU-PLAN.md, cited by Q-09, Q-12, Q-13, Q-14 and O-03:

| at 7d1e7d4 | in v1.3 | | at 7d1e7d4 | in v1.3 |
|---|---|---|---|---|
| :149, :180, :206, :238 (the `tests:` lines) | renamed by E-10a, now :149, :184, :211, :244 | | :401 | :409 |
| :203 | :208 | | :406, :407, :411 | :414, :415, :419 |
| :273, :281 | :280, :288 | | :429, :436 | :437, :444 |
| :299, :307 | :307, :315 | | :456, :483 | :464, :491 |
| :325, :331 | :333, :339 | | :512, :514 | :520, :522 |
| :349, :358 | :357, :366 | | :378, :384, :385 | :386, :392, :393 |

Lines up to :148 (ADU-02's :128–:132 included) do not move.

## 5. Gate
Expected count (the last STATUS.md Log line that records a gate run, STATUS.md:42 after the apply, :40 before): `46 passed in 28.77s` (the operator's, M1 close) · measured: `46 passed, 1 warning in 15.97s` (`uv run pytest tests/ -q -m "not timing"`, run once by this session after its journal block was appended; interpreter line `C:\dev\team-rota-data\.venv cp1252 0`) · lint: `All checks passed!` (`uv run ruff check`)

This loop changed no test, and the count equals the expected one. `git status --short` was the same before and after both commands. This session's run is recorded on the Log line STATUS.md:43, which ends `backward: n/a (documents only)`. It is not the operator's gate, and it closes no unit.

## 6. Not applied, and owed to others
- **B-2.T** (T-03.1–.10, T-09.1–.6, T-05.1–.6, T-07.1–.3): the retiring units' sessions make these, each under the operator's grant for that file in that session (D-12). The apply edits no test.
- **E-9.P** is for the pm-lead to make: a patch of design/PRODUCT-DESIGN.md:18 ("a member as the team list shows it …"), worded as E-9.P proposes or otherwise as long as it says what D-17 says. Whether it is v1.7.1 (editorial) or v1.8 (a requirement changed) is the pm-lead's call. It blocks nothing; ADU-03 and ADU-04 follow D-17.
- Options not ruled, which apply nothing: E-1b, E-2b, E-3b, E-4b, E-5b, E-6a, E-7a, E-8b, E-9c, E-10b, E-10c, E-10d. No ruled option has a conditional block or a block "on the text E-xx writes".
- Q-12 (O-02, due ADU-04) and Q-14 (O-03, due ADU-12) are open, each owed to a design-change loop before its unit opens.

## 7. Findings for the operator (none blocks the apply)
1. ADU-PLAN.md:2's provenance clause (§3) names INTERFACES v1.0.1 and ARCHITECTURE v1.1, the versions the plan was cut from on 2026-11-07. It is true as dated, but it is the kind of version pointer VERSIONS.md's header discourages. It is a candidate for the next plan patch, with design/INTERFACES.md:2's stale "each with a `Null<Interface>` in the contract unit" (Part C).
2. Q-14's and O-03's text cite ADU-PLAN.md lines as at 7d1e7d4 (:406, :407, :411, :436 and others); in v1.3 they are +8 (§4). ADU-12's loop should read them with §4's mapping.
3. `adu audit` (not one of the apply's checks) reports 13 "dangling" findings after the apply against 1 finding (O-01) on a HEAD export. Each is a "plugin FB-28/32/33/34" citation the apply wrote (STATUS.md:32, :33; ADU-PLAN.md:292; DECISIONS.md:17, :23; OPEN-QUESTIONS.md:90, :91, :97, :104, :105; design/INTERFACES.md:152). The audit reads them as this project's FEEDBACK ids and does not see the "plugin" prefix. This is plugin feedback, for the operator to carry upstream. `adu release check` → "release check OK".
