# VERIFICATION-R3 — docs/PACK-q07-retire-amends.md v1.3 at 7d1e7d4 against HEAD d38925b
2026-11-13 · verifier session · read-only · gate run: `46 passed, 1 warning in 26.34s` (HEAD d38925b, `uv run pytest tests/ -q -m "not timing" -p no:cacheprovider`; `git status --short` before and after: `?? uv.lock`); lint `All checks passed!`

## 0. Snapshot gate
merge-base --is-ancestor: ok · drift on governing documents: 0 commits (allowed 0) · result: proceed
`adu snapshot check 7d1e7d4` → "snapshot OK: 7d1e7d4 is an ancestor of HEAD d38925b; governing documents unchanged since (0 commit(s), allowed 0)", exit 0. `git diff --stat 7d1e7d4 HEAD`: SESSION-JOURNAL.md, the pack, docs/VERIFICATION-R1.md and docs/VERIFICATION-R2.md only.
Start checks: `adu status` → Now: ADU-03; Q-07 open, blocking ("— STOP"). `UV_PROJECT_ENVIRONMENT` = `C:\dev\team-rota-data\.venv`, `PYTHONUTF8` empty, `ADU_PLUGIN_ROOT` = `C:\dev\adu-lifecycle`. Interpreter line: `C:\dev\team-rota-data\.venv cp1252 0`. `git status --short`: `?? uv.lock`. Plugin HEAD ae191e2; `git diff --stat 4b63bb0 HEAD` lists FEEDBACK.md only (4 insertions). `adu role set verifier` ran (a session mark, gitignored). `adu next-id V` was not run (FB-31); the id R3 is named by hand.

## 1. Earlier rounds
R1 (docs/VERIFICATION-R1.md, v1.1 at bc98783) ended `STOP — MECHANICAL` (R1 :227); R2 (docs/VERIFICATION-R2.md, v1.2 at 1745ed2) ended `STOP — MECHANICAL` (R2 :224).

**Method.** Own parser (§2) on v1.2 (`git show 1745ed2:docs/PACK-q07-retire-amends.md`) and v1.3, blocks compared by id: 196 in each, none added or removed; 160 identical; 36 changed. Of the 36, 25 change only the pack's self-reference "v1.2" → "v1.3" (E-5a.14, E-5b.1, E-6b.8, E-6b.9, E-6a.7, E-6a.8, E-7a.2, E-7a.3, E-7b.2, E-7b.3, E-8a.3, E-8a.4, E-8b.3, E-8b.4, E-9a.2, E-9a.3, E-9c.2, E-9c.3, E-10a.29, E-10a.32, E-10b.6, E-10b.9, E-10c.6, E-10d.1, E-10d.4). The other 11 are B-2.7, B-3.5, B-3.8, B-3.11, B-3.14, B-3.16, E-6b.1, E-6b.10, E-6a.1, E-6a.9 and E-10c.3; each is re-checked below. Prose outside the blocks was word-diffed (`git diff --word-diff 1745ed2 d38925b`).

### 1.1 R2's finding and notes (R2 §5, :189–:219)
| R2 item | Status | Where in v1.3 | Evidence |
|---|---|---|---|
| N-1 (R2 :194–:204) | CARRIED OUT | E-6b.10 :3458–:3467; E-6a.9 :3572–:3581; option (b) :3071; the reasons and the thirteen units :3074–:3092; B-4.2 :767–:768; B-4.3 part 7 :794–:798, stand-ins :1584–:1653, routers :1655–:1687, output :1201–:1204, :1229–:1237 | R2's fix 1, refined. Own word diff of E-6b.10's new text against v1.2's: "a request to a stubbed operation answers 501 not_built with Bearer <a token …>" → "a route the test registers itself on that app, at a path the contract does not declare and taking its caller from Depends(app.api.deps.require_caller), answers 200 with the id seed_admin returned for Bearer <the token …>", plus "the clause sends no request to an operation of the contract and imports nothing from src/app/api/contract_stubs.py, so it holds while the API units move their operations out of the stubs and after ADU-08 deletes that module". E-6a.9 changes the same way. R2's third twin is four API twins. The unit list is checked in §2.5 row 44. Twins re-run with the pack's script and with my own scaffold: §4 |
| Note: E-10 (c)'s grant reason (R2 :210) | CARRIED OUT | E-10's table :3933; E-10c.3 :4436; B-4.1 :761; A-2 :39; B-3.15 :742; D-2 step 7 :2579; guard queries :750, :756, :1116, :1122, :1131 | The cell now reads "it lies outside adu.toml's code_roots (adu.toml:7), so the guard applies no roster to it (plugin scripts/adu.mjs:689–691) and allows it in every tree". My guard grid: pyproject.toml is allowed in 10 of 10 trees (§4) |
| Note: E-8 (b)'s line (R2 :211) | CARRIED OUT | E-8 (b) :3717; output :1185, :1227 | `git show 7d1e7d4:src/app/synthetic.py`, line 12: `import random`; the re-run prints `src\app\synthetic.py:12: stdlib random imported` |
| Note: E-1 (b), E-4 (b) unlabelled (R2 :212) | CARRIED OUT | E-1 (b) :2593 and E-4 (b) :2896 ("as rehearsed in B-4.3, part 6"); B-4.2 :769; output :1144–:1178 | Re-run equal. By arithmetic too: T-03.4 goes from 3 lines to 1 and T-03.5 from 3 to 1, so either alone gives :108/:106/:106 and both give :106/:104/:104 |
| Note: composed as text only (R2 :213–:216) | CARRIED OUT | E-2b.3 :2664 and E-1b.3 :2617, both now rehearsed (output :1177, :1181–:1183); E-7 (a) :3584, E-8 (b) :3717, E-9 (c) :3829 and E-7b.1 :3589 say "composed as text" | Re-run equal |
| Note: ADU-11's route (R2 :217) | CARRIED OUT | E-6b.1 :3359; E-6a.1 :3480; E-6 :3095; Q-p5 :222; B-3.16 :709; B-5 :2387 | Q-p5: "First, ADU-04's router and ADU-11's command (`app seed-admin`, ADU-PLAN.md:378) must reach the IdentityService … Whatever is ruled keeps `Ports.member_directory` bound to the identity service itself" |
| Note: Part C, "five protocols" (R2 :218) | CARRIED OUT | Part C :2452 | `git grep -n "five protocols" 7d1e7d4` gives ADU-PLAN.md:99, SESSION-JOURNAL.md:105 and :153, VERSIONS.md:90 and tests/test_ports.py:1, each as the row reads |
| Note: D-2 step 6 (R2 :219) | CARRIED OUT | D-2 :2575 | My simulated apply on an export of HEAD: STATUS.md:41. My composition under E-10 (d): :42 |

### 1.2 The header's line 4: FB-34's class, searched in the pack
| Finding (pack :4) | Status | Where | Evidence |
|---|---|---|---|
| (1) E-6b.10, E-6a.9 | CARRIED OUT | as N-1 above | — |
| (2) Q-p5's option (b) | CARRIED OUT | B-2.7, Q-p5 :224 | v1.2: "iterates the operations contract_stubs still registers". v1.3: "iterates only the operations the app still serves from the stubs, read from its own route table and never by importing the stubs module (plugin FB-34) … after ADU-08 the loop has no operation left, as ADU-08's own arm asserts (ADU-PLAN.md:357)" |
| (3) the other API arms and main.py | CARRIED OUT | Q-p5's Conflict :222; A-2 :57–:58; B-3.16 :709; B-5 :2387 | :222 reads "ADU-06's, ADU-10's and ADU-08's arms ask the same check (:307, :331, :358) without naming a helper … src/app/main.py imports the module too (line 16) … None of the four API entries declares the conformance test, or main.py, in its `amends`". O-p1's Where cell (E-5a.14 :3054) names Q-p5, which carries it |
| (4) the retirement arms' gate clause | CARRIED OUT | B-3.5 :598, B-3.8 :631, B-3.11 :664, B-3.14 :697 | In each, the only change since v1.2 is the words "which the gate checks at this unit's close and no test of this file repeats" (own diff) |
| The "checked" list | CONFIRMED, with four blocks unnamed | :4 | It names every arm, amends line, T-block, D-p row, question, pointer and Owed row my parser finds, except four option variants of named blocks: E-1b.1 and E-1b.2 (the INTERFACES text and B-3.3's text under E-1 (b)), E-3b.5 (B-3.4's ports.py line under E-3 (b)) and E-4b.1 (B-3.3 under E-4 (b)). E-1b.1 and E-1b.2 describe T-03.4's alternative, the 501 loop through the stubs, which Q-p5 and O-p1 already carry; the other two assert nothing through a removed artefact |

### 1.3 R1's dispositions (R2 §1), in v1.3
| R1 item | Status in v1.3 | Where | Evidence |
|---|---|---|---|
| N-1 | HOLDS, block changed | E-6b.10 :3466 | The clause still covers E-6b.6's db.py and deps.py lines. Both twins fail, re-run and own (§4) |
| N-2 | HOLDS, blocks changed | B-2.7, Q-p5 :223; E-5a.14 :3054 and E-5b.1 :3066 (version only); B-3.16 :709 | Q-p5 reads "**Blocking:** no — not for ADU-03, ADU-09, ADU-05 or ADU-07". B-3.16 still names the Owed row and rule 19. My simulated apply gives "Open blocking questions: none" and "O-02 due ADU-04" |
| M-1, M-2, M-3, and E-4 (b) | HOLD, blocks identical | E-2b.8–.18 :2716–:2826; E-3b.5–.6 :2874–:2892; E-1b.1–.4 :2596–:2636; E-4b.1 :2898 | My scan of all 1,088 rulings finds no left-over text. Under E-2 (b) there is no "amends src/app/ports.py", "in `src/app/ports.py` is the one" or "ADU-16's module by a declared". Under E-3 (b) there is no `detail=""`, `detail, **extra` or `.detail`. Under E-1 (b) there is no "FakeMemberDirectory holding", and under E-4 (b) no rename clause |
| Note: plugin HEAD | HOLDS, updated | A-2 :37 | ae191e2, measured |
| Note: A-2's Refused row | HOLDS | A-2 :46 | identical |
| Note: E-7 (b) rules the later constructors | HOLDS | E-7 (b) :3585 | identical |
| Note: ARCHITECTURE.md:18 and E-7 (a)'s seam | HOLD | E-7a.4–.6 :3685–:3713; E-7b.4–.5 :3628–:3646 | identical |
| Notes: the commit no API arm sees; ADU-04's route | HOLD, text changed | Q-p5 :222; B-3.16 :709 | Both points are kept, and ADU-11 is added |
| Note: T-03.4's comment | HOLDS | T-03.4 :310 | identical |
| Note: E-9.P and "superseded" | HOLDS | E-9a.2 :3851 and E-9c.2 :3887 (version only); E-9.P :3904 | — |
| Note: resolved questions keep "Blocking: yes" | HOLDS | E-5 (a) :2909 | identical; my apply lists no resolved question |
| Note: `adu derived render` | HOLDS | B-4.4 :2378 | My apply: 0 files rewritten |
| §2.6 B-2.3 | HOLDS | B-2.3 :102–:146 | identical |
| §2.6 E-8, hard rule 5 in full | HOLDS | E-8a.3 :3756 | version only |
| row 82 (E-9) | HOLDS | E-9 :3826 | The only prose change is the added sentence at :3829 |
| row 83 (Part C) | HOLDS, corrected | Part C :2452 | as §1.1 |
| §3 B-3.3 and T-03.6 | HOLD | B-3.3 :575; T-03.6 :327 | identical |
| Q-p6 | HOLDS | B-2.7's Q-p6 :228–:233 (md5 identical); E-10 :3915–:4558 | Only the table's (c) grant cell and E-10c.3 changed, as §1.1 says |

## 2. Claims about the repository
**Method.** I used two routes.
1. The pack's script, extracted byte for byte from :1281–:2329 (1,049 lines) and re-run in the scratchpad (`python -I`, the project's venv, `ADU_PLUGIN_ROOT` set). Its 472 output lines equal the pasted :805–:1276 once timings, object addresses, scratch-path prefixes and the pack-path argument are normalised. Three lines differ, all in those parts.
2. My own line-based parser, independent of the pack's regex. It finds 196 replace blocks (B 24, T 24, E 148) and 1 deletion. B-blocks were checked against the LF-normalised blobs of `git show 7d1e7d4:<file>`, both in sequence and each on the untouched blob. T-blocks were checked stage by stage. E-blocks were checked in each of the 1,088 rulings, with my own enumeration, selection, order and checks.

Every match was exact, so no markup-ignored fallback was needed.

### 2.1 B-blocks against the 7d1e7d4 blobs
| # | Block (pack line) | C / W / U | Evidence (file:line at 7d1e7d4) | Replacement matched |
|---|---|---|---|---|
| 1 | B-2.1 (:78) | C | DECISIONS.md:16, end of the last line | exact, unique, within the line |
| 2–5 | B-2.2 (:91), B-2.3 (:102), B-2.4 (:148), B-2.5 (:161) | C | design/INTERFACES.md:2 (fragment), :79, :91, :103 | 4/4 |
| 6–7 | B-2.6 (:172), B-2.7 (:183) | C | OPEN-QUESTIONS.md:53, :59 (the last line) | 2/2 |
| 8–9 | B-2.8 (:236), B-2.9 (:248) | C | VERSIONS.md:14; :117, end of the last line | 2/2 |
| 10–11 | B-3.1 (:545), B-3.2 (:555) | C | ADU-PLAN.md:2, :6 (fragments) | 2/2 |
| 12–23 | B-3.3 (:566), B-3.4 (:578), B-3.5 (:590), B-3.6 (:601), B-3.7 (:613), B-3.8 (:624), B-3.9 (:634), B-3.10 (:646), B-3.11 (:657), B-3.12 (:667), B-3.13 (:679), B-3.14 (:690) | C | ADU-PLAN.md:151, :153, :159, :182, :184, :188, :208, :210, :216, :240, :242, :246, each a whole line | 12/12 |
| 24 | B-3.16 (:700) | C | ADU-PLAN.md:285 (blank) and :286 "### ADU-06 — Scheduling API" | exact, unique |

### 2.2 T-blocks, stage by stage
| # | Blocks | C / W / U | Evidence | Replacement matched |
|---|---|---|---|---|
| 25 | T-03.1–.6 (:270–:337) | C | conformance :1, :19, :23, :61, :102, :105 (7d1e7d4) | 6/6 |
| 26 | T-03.7–.10 (:341–:385) | C | test_nulls :11, :17, :28, :36 | 4/4 |
| 27 | T-09.1–.6 (:389–:448) | C | conformance :24, :110; test_nulls :11, :18, :28, :48 (after T-03) | 6/6 |
| 28 | T-05.1–.6 (:452–:516) | C | conformance :24, :108; test_nulls :11, :15, :24, :30 (after T-09) | 6/6 |
| 29 | T-07.1–.2 (:520–:537); T-07.3 (:539) | C | conformance :24, :108 (after T-05); afterwards the conformance test names no Null (own) | 2/2; the deletion as stated |
| 30 | all 24 T-blocks and the deletion | C | identical to v1.2 (own block diff) | — |

### 2.3 E-blocks against the text as B leaves it
| # | Claim | C / W / U | Evidence |
|---|---|---|---|
| 31 | every E-block at its stated line (:830–:979) | C | Own: each of the 147 option blocks is selected by at least one ruling and matches, unique, at its stated line in every ruling that selects it. E-9.P is at design/PRODUCT-DESIGN.md:18, unique, and B does not touch it |
| 32 | the blocks "on the text E-xx writes" (E-2b.10–.12, E-10b.2) | C | applied after the other blocks of their file, they are found at VERSIONS.md:125, ARCHITECTURE.md:2, :52 and ADU-PLAN.md:148 |
| 33 | conditional blocks (E-2b.13–.18 with E-5 (b); E-3b.5, E-10b.1, E-10c.1 without E-2 (b)) | C | selected and matched only under their condition |
| 34 | 1,088 rulings, 0 failures, block counts 69–93 … 7–32 (:982–:990) | C | Own enumeration: 1,088/1,088, with the same counts per class. In each ruling: the D-p rows stand last and in id order; the Owed rows are O-01, O-p1 (and O-p2), each with five cells; the open and blocking questions are as ledgers.mjs:81–85 reads them; the residue scans of §1.3 are clean; ADU-PLAN.md holds no provisional id |
| 35 | 144 distinct ADU-PLAN.md texts (:1108) | C | 144 in my own composition |

### 2.4 Part A-2, row by row
Rows :26–:36, :38 and :40–:53 are identical to v1.2. R2 §2.4 (rows 39–65) confirmed them against the same 7d1e7d4 blobs and plugin lines, and I re-read the ones this round leans on: adu.mjs:687, :692–:693, :704, :81–:82, :85–:86 and :398; ledgers.mjs:26–27 and :83–85; plan.mjs:160, :181, :214, :219 and :234. Each still reads as the row says.
| # | Row (pack line) | C / W / U | Evidence |
|---|---|---|---|
| 36 | adu.mjs:687; plugin ae191e2; FB-28 (:37) | C | `git -C C:\dev\adu-lifecycle rev-parse --short HEAD` → ae191e2; `git diff --stat 4b63bb0 HEAD` → FEEDBACK.md only. At :687, `… stateOf.get(e.id) === 'done' && listOf(e.yaml?.tests).map(norm).includes(p) && !granted) deny(…)` reads no `amends`. FEEDBACK.md:33 is FB-28, `open` |
| 37 | adu.mjs:689–691; adu.toml:7 (:39) | C | :689 `const codeRoots = listOf(cfg.project.code_roots)`; :691 applies the roster only if `codeRoots.some((cr) => p === cr \|\| p.startsWith(cr + '/'))`; adu.toml:7 `code_roots = ["src","tests","frontend/src","frontend/tests"]`. Measured: pyproject.toml is allowed in 10 of 10 trees |
| 38 | ADU-PLAN.md:128, :273, :299, :325, :349; FEEDBACK.md:39 (:54) | C | :128 "gone once the last router lands (ADU-08)"; :273, :299 and :325 "move out of the stubs module"; :349 "the stubs module is now empty and deleted". FEEDBACK.md:39 is FB-34, `open` |
| 39 | contract_stubs.py:28–29; deps.py:33 (:55) | C | :28 `SESSION_DEP = Depends(get_session)`, :29 `CALLER_DEP = Depends(require_caller)`; deps.py:33 `def require_caller(request: Request, creds: … = Depends(bearer)) -> Caller:`. No entry at ADU-PLAN.md:170–525 amends deps.py |
| 40 | contracts/openapi.json paths; schemas.py:21–22 (:56) | C | 17 paths and 18 operations (identity 5, scheduling 6, swaps 5, notifications 2). No path's first segment is a parameter, and none starts `/__probe__`. schemas.py:21 is `CONTRACT_JSON = …` and :22 is `CONTRACT: dict[str, Any] = json.loads(…)` |
| 41 | main.py:16, :24, :72–76, :78 (:57) | C | :16 `from app.api import contract_stubs`; :24 `CONTRACT = contract_stubs.CONTRACT`; :72–76 the `@app.exception_handler(contract_stubs.NotBuilt)` handler; :78 `contract_stubs.register(app)`. Later amendments of main.py: ADU-09 :182, ADU-05 :208 and ADU-07 :240 only |
| 42 | ADU-PLAN.md:281, :307, :331, :358; contract_stubs.py:46 (:58) | C | only :281 names "the conformance helper from ADU-02"; :46 `def validate_example(schema, value)` |
| 43 | ADU-PLAN.md:507, :510 (:59) | C, by reading | :507 `files: ["src/app/serve.py", …]`; :510 is the amendment of ADU-11's cli.py. ADU-15 does not amend main.py, so its guard roster refuses that file. What the clause needs is that `create_app` gains no route or mount ahead of the test's route. That condition carries weight: with a catch-all mounted at `/` inside `create_app`, my clause tests answer 404 (§4). The row's wording, "nothing is mounted on the app `create_app` returns", is looser than that (Note) |

### 2.5 Other claims
| # | Claim (pack line) | C / W / U | Evidence |
|---|---|---|---|
| 44 | E-6, the thirteen later units checked (:3085–:3092) | C, one omission | Own read of each entry at positions 6–18, covering what it adds (`files`, `tests`), amends and deletes. ADU-09 :178–:184, ADU-05 :204–:211 and ADU-07 :236–:242 add their service files and amend main.py, their Null and test_nulls. ADU-05 also amends tests/conftest.py (:211, TIMING_NODES), which E-6's "rebind only their own lines of src/app/main.py" leaves out. That amendment registers a timing node and touches no surface the clause asserts through. ADU-04 :270–:273, ADU-06 :296–:299, ADU-10 :322–:325 and ADU-08 :346–:349 each add src/app/api/<domain>.py and amend contract_stubs.py; ADU-08 deletes it. ADU-12 :397–:401, ADU-17 :426–:430, ADU-13 :453–:457 and ADU-14 :480–:484 touch frontend/ only, plus ADU-12's adu.toml and CLAUDE.md. ADU-11 :372–:374 adds cli.py and test_cli.py and amends nothing. ADU-15 :507–:514 adds serve.py, playwright.config.ts and RUNBOOK.md, and amends cli.py, vite.config.ts, package.json, conftest.py and adu.toml. None amends deps.py, db.py or ADU-03's test, and none amends main.py beyond the three binding lines |
| 45 | "`require_caller` itself and the 401 Problem it raises: … asserted again by ADU-04's second arm" (:3080) | C | ADU-PLAN.md:278 |
| 46 | B-3.16: "which this unit's fifth arm uses" (:709) | C | ADU-04's fifth arm is :281 |
| 47 | Q-p5's new citations (:222, :224) | C | ADU-PLAN.md:378, :357; main.py :16, :24, :72–76, :78 |
| 48 | B-4.2: "with `require_caller` cut off from `get_session` the full gate is no longer green" (:767) | C | re-run: 1 failed, 45 passed; own: 1 failed, 48 passed |
| 49 | header :3: "after ADU-08 no form of v1.2's clause can be met" | C | ADU-PLAN.md:349, :357: no stubbed operation is left |
| 50 | D-2's ids (:2553–:2559) | C | `adu next-id` at HEAD: D-12, Q-08, O-02 |
| 51 | D-2 step 6: STATUS.md:40, then :41, or :42 under E-10 (d) (:2575) | C | STATUS.md:40 at HEAD is the M1 Log line. My apply: :41. My composition under E-10 (d): :42 |
| 52 | B-4.4: "the export's journal is the snapshot's" (:2333) | C | my apply on an export of HEAD names the 2026-11-12 21:44 block |
| 53 | the B-5 and E-6 probes (:2390–:2434, :3099–:3345) | C (not re-run) | each section is byte-identical to v1.2 (md5). R2 found them identical to v1.1, and R1 re-ran both |
| 54 | E-8 (b) "624 32-bit words"; E-10 (c) "test modules cannot import one another" | U (external; not re-researched) | stated as consequences, labelled |

### 2.6 What B-2.3 and E-6–E-10 settle
- **B-2.3.** Identical to v1.2. It stands as R1 §2.6 and R2 §2.6 found it.
- **E-6 (b).** E-6b.1's seed-command bullet (:3359) now names the object, "the identity service that app binds as `Ports.member_directory` (ADU-03 arm 1)". It hands on "whether the command reaches it there or through another binding" to Q-p5 by name, and Q-p5 stays open under every ruling. E-6b.10 is the arm. Together they settle the session point and nothing else.
- **E-6 (a).** The same, at E-6a.1 :3480 and E-6a.9.
- **E-7, E-8, E-9.** Their blocks changed only in version references, and their option texts gained the "composed as text" labels (§1.1). They stand as R2 §2.6 found them.
- **E-10.** The table is true. My count is 24 arms renamed, 7/4/7/6: ADU-PLAN.md:159–165, :188–191, :216–221 with :223, and :246–248 with :252–254. That is 28 fragments, E-10a.1–.28, being 4 `tests:` lines and 24 arms. The (c) grant cell (:3933) gives the reason that holds (§1.1), and the order is unchanged in all 144 plan texts.

### 2.7 What the pack does not claim
**(i) The pack's own unrehearsed reliances**
| Reliance | Where the pack relies on it | Said so there? |
|---|---|---|
| E-6a.9 is not rehearsed | B-4.2 :768 | Yes: "Not rehearsed: E-6 (a) has no scaffold in this pack". E-6a.9's Why (:3573) does not repeat it |
| E-7 (a)'s constructor, composed as text | E-7 (a) :3584 | Yes: "composed as text with each option of E-6 and E-8 (B-4.3, part 3) and is not run with a stand-in" |
| E-8 (b)'s constructor | E-8 (b) :3717 | Yes |
| E-9 (c)'s values | E-9 (c) :3829 | Yes |
| E-7b.1's other compositions | E-7b.1 :3589 | Yes: "only E-7 (b) with E-8 (a) is also run" |
| the scaffolding: stand-in services and their tests, the main.py rebinding, the illustrative `Refused` and current session, the stand-in `TokenDirectory` and `src/app/refusals.py`, the stand-in routers with their main.py and stubs-module edits | B-4.3 :801 | Yes, all named. The stand-in routers' 200s without the contract's shapes are said there too |
| E-10 (b) and (c), measured with stand-in files on the 7d1e7d4 tree, not through the stages | B-4.2 :770; E-10 :3915 | Yes |
| E-9.P is the pm-lead's, not applied | :12; :3831; :3904; D-2 :2567 | Yes |
| E-6's checks of ADU-12, ADU-17, ADU-13, ADU-14, ADU-11 and ADU-15 | E-6 :3088–:3090 | By reading; no rehearsal is claimed (true: §2.5 row 44) |
| A-2 :59, nothing mounted ahead of the test's route | E-6 :3090 | By reading; it holds (row 43) |
| D-2 step 6's ":42 under E-10 (d)" | D-2 :2575 | By arithmetic, not labelled; my composition confirms it |
| B-4.4: the STATUS Log line D-2 writes is not simulated | :2333 | Yes |

**(ii) My own search.** I searched three things.
- The pack: every arm, amends line, T-block, D-p row, question with its options, pointer and Owed row my parser finds. That is the header's list plus E-1b.1, E-1b.2, E-3b.5 and E-4b.1.
- The plan, ADU-PLAN.md:29–525: each unit's arms and `amends`, against the `files`, `amends` and deletions of every unit after it in the derived order. For the pack's ADU-03 text that means positions 6–18.
- What ADU-03's, ADU-09's, ADU-05's, ADU-07's and ADU-04's sessions would meet under the recommended rulings: rosters, grants, files, arms, the `bound`/`source` constructor, D-p3's three owners, layering, the E-10 (a) names, and ADU-05's timing sibling. The conftest assertion at :211 names no path.

What I found:
- **In the pack.** Nothing beyond the header's four findings. T-03.4's 501 loop through the stubs is carried by Q-p5 and O-p1.
- **In the plan, already covered.** ADU-02's 501 loop and the API units' validation helper (Q-p5, O-p1); the test_nulls entries of ADU-16's arms (D-p1).
- **Checked and not of the class.** ADU-00's "TIMING_NODES is empty until ADU-05 registers its arm" (:53): tests/test_tiers.py:48–53 checks only for stale entries, not for emptiness. The MSW handlers and the Prism mock: no unit removes them.
- **In the plan, covered by no block, question, option or Owed row (→ Q-p7, §6).** All four are in M4, outside Q-07:
  1. ADU-12 :407 renders the shell "with placeholder routes in frontend/src/routes.ts". ADU-17 :429, ADU-13 :456 and ADU-14 :483 point those routes at the real pages, and none amends frontend/tests/shell.test.tsx. This is plugin FB-34's rule as worded ("a placeholder … that a later unit is planned to … replace").
  2. ADU-17 :436 lands on the week-board route, "a placeholder page until ADU-13", and ADU-13 :456 replaces it. The arm names the state as temporary, so a test of the route rather than the page holds.
  3. ADU-12 :411 asserts the combined gate, fast and lint "again and CLAUDE.md's derived block is current (adu derived check green)". ADU-15 :514 changes adu.toml's gate, and CLAUDE.md:43–49 is derived from adu.toml. It is protected (adu.toml:19) and declared by ADU-12 (:401), not by ADU-15. Measured: a gate change in adu.toml makes `adu derived check` exit 2 on CLAUDE.md.
  4. ADU-12 :406 says "the dependency set is exactly D-09's", and D-09 (DECISIONS.md:14) lists @playwright/test. Yet ADU-15 :512 "gains … @playwright/test (D-09)".

  Points 1, 2 and 4 are readings: whether a test goes red depends on how its session writes it. Point 3's stale block is measured. None of them touches the pack's text.

## 3. Criteria
| Arm / criterion | Five parameters | Can it fail (how) | Twin / mock / retirement | Finding |
|---|---|---|---|---|
| ADU-03 arm 1, :159 → B-3.5 (:598) | n/a (deterministic) | As R1 §3: the binding is not the identity service or fails `ports.MemberDirectory`; null_directory.py exists; an import of it remains; an edited test is red in the gate. The added words, "which the gate checks at this unit's close and no test of this file repeats", move no check: the gate at the close runs both tests, as it did for "stay green unchanged" at 7d1e7d4 | retires MK-04 | not weakened |
| ADU-03 arm 1 with E-6b.10 (:3466) | n/a | Measured to fail, both routes, when `require_caller` does not depend on `get_session`, and when `get_session` is sync. Own extra mutation: it also fails when `get_session` is async but does not make the session current. By the clause's wording it fails for a token resolved to another member (the id check), and for a method with no current session that does not raise `db.NoCurrentSession`. It does not fail when nothing is wrong in ADU-03: it passes in four API twins, both routes. It escapes (by reading) a directory method that opens a session of its own, if the method the test calls raises (Note) | twin measured | Not weakened against v1.2's clause. v1.2's form also drove a contract route with both the caller and the session dependency, and the NotBuilt handler; ADU-02's 401/501 loop keeps doing that with the injected double until Q-p5's loop. None of it is ADU-03's wiring. v1.3 adds the member-id check, which a 501 could not make |
| ADU-03 arm 1 with E-6a.9 (:3580) | n/a | It fails if the directory's own short session does not see the issued token, if the token resolves to another member, or if the 401 path is broken. Not rehearsed (B-4.2 :768). It goes through the same route of the test's own, so nothing a later unit removes | — | not weakened |
| ADU-09, ADU-05, ADU-07 arm 1 (B-3.8 :631, B-3.11 :664, B-3.14 :697) | n/a | as R1 §3, with the same added words | retire MK-02, MK-01, MK-03 | not weakened |
| the 24 arms E-10 (a) renames (E-10a.2–.28) | n/a | identical to v1.2: the path changes, nothing else (R2 row 38) | — | not weakened |
| ADU-02 arms :126–:133 after T-03 … T-07 | n/a | as R2 §3 (T-blocks identical). The gate after each stage is green: re-run 46/45/44/43, which is 44/42/40/38 completed tests plus 2/3/4/5 stand-ins | — | kept |
| ADU-16 arms :99–:104 | n/a | test_ports.py stays green with `Refused` added (re-run; own scaffold) | — | kept |
| Amendments ↔ T-blocks, both directions | — | — | — | As R2 §3, the blocks being identical: B-3.3 ↔ T-03.1–.6; B-3.4 ↔ T-03.7–.10; B-3.6 ↔ T-09.1–.2; B-3.7 ↔ T-09.3–.6; B-3.9 ↔ T-05.1–.2; B-3.10 ↔ T-05.3–.6; B-3.12 ↔ T-07.1–.2; B-3.13 ↔ T-07.3. The non-test amends hit no immutable test, all measured. B-3.4's ports.py: test_ports green. E-6b.6's db.py and deps.py: test_models, test_synthetic and the session-sharing test green (re-run gate 46; own gate 49). E-1b.3's doubles.py, now rehearsed: test_ports 4 passed. E-2b.3's layering.json, now rehearsed: 7 passed. E-10c.2's pyproject.toml: 46 passed in importlib mode |
| Additions ↔ acceptance | — | — | — | E-6b.6 ↔ E-6b.10 (twins measured). E-10 (b)'s and (c)'s files have no arm; the gate catches their absence (3 errors measured) |
| Quantitative criteria | none (B-4.1 :761) | — | no pin changes, no stochastic arm | no false-failure rate to re-derive |

## 4. Measurements
All runs are deterministic (seed n/a, interval —), made in the scratchpad (`…\scratchpad\r3\run`, `\own`, `\ownrun`, `\apply-*`, `\guard-*`, `\plan-*`, `\m4probe`), never in the repository. `git status --short` stayed `?? uv.lock` throughout. "Re-run" is the pack's script; "own" is my parser, composition, scaffold and apply.

| Quantity | Pack's value (n) | Verifier's value (n) | Interval | Agrees |
|---|---|---|---|---|
| blocks parsed | 196 (B 24, T 24, E 148) + 1 deletion (:805) | same (own parser) | — | yes |
| B-blocks at their line | 24/24 (:806–:829) | 24/24 (re-run; own, in sequence and each on the untouched blob) | — | yes |
| T-blocks per stage | 10, 6, 6, 2 + 1 deletion (:1191–:1222) | same (both) | — | yes |
| E-blocks | 148 OK (:830–:979) | re-run: same. Own: 147 option blocks, each matched in every ruling that selects it, and E-9.P at :18 | — | yes |
| rulings | 1,088, 0 failures, counts per class (:982–:990) | re-run: same. Own: 1,088/1,088, the same counts, plus cell counts and residue scans | — | yes |
| plan texts; `adu plan check` | 144; exit 0; one output (:1108–:1109) | 144 (own composition); all exit 0, one output; `adu plan order` identical to the 7d1e7d4 export for all 144 | — | yes |
| plan check and order: B-3; B-3 + E-6 (b) + E-10 (a) | `plan OK: 18 units`, the order of B-3.15 (:717–:740, :1060–:1106) | same for both; the order output is identical to the pristine export (md5 edeed79a…) | — | yes |
| guard | :1111–:1135 | Re-run: same. Own grid of 18 paths × 10 trees (7d1e7d4, B-3, recommended, E-10 (b), (c), (d), E-1 (b), E-2 (b), E-6 (a), E-5 (b)). Both completed tests are refused in all 10. Each option's own path is allowed only under that option: db.py and deps.py under E-6 (b); test_identity_service.py under E-10 (a); `__init__.py` under E-10 (b); doubles.py under E-1 (b); refusals.py and layering.json under E-2 (b), with ports.py refused there. pyproject.toml is allowed in all 10 | — | yes |
| E-10 on the 7d1e7d4 tree: planned / (a) / (b) / (c) without the files / (c) with them | 3 errors / 50 / 50 / 46 / 50 passed (:1138–:1142) | re-run: same | — | yes |
| E-1 (b), E-4 (b), both: T-09.2, T-05.2, T-07.2 | :108/:106/:106 for either; :106/:104/:104 for both (:1144–:1176) | re-run: same; by arithmetic, the same | — | yes |
| E-1b.3: test_ports.py with TokenDirectory | 4 passed (:1177) | re-run: same | — | yes |
| E-1 (b) with E-4 (b), stage T-03 | gate 46 passed, lint clean (:1178) | re-run: same | — | yes |
| E-2b.3: joined / planted and joined / planted, not joined | 7 passed / 1 failed / 7 passed (:1181–:1183) | re-run: same | — | yes |
| the scan, on 7d1e7d4 and after the stages | synthetic.py:12 (:1185, :1227) | re-run: same; line 12 is `import random` | — | yes |
| baseline gate, export A | 46 passed, lint clean (:1187) | re-run: same | — | yes |
| E-6 (b) scaffold, outside / inside a unit of work | NoCurrentSession / None (:1188) | re-run: same | — | yes |
| twin 1 / twin 2 | ModuleNotFoundError / 401 at :70 (:1189–:1190) | re-run: same | — | yes |
| clause, wiring right | 2 passed (:1201) | re-run: 2 passed. Own scaffold (own db.py, own deps.py edit, own identity stand-in, 5 tests written from the arm text): 5 passed | — | yes |
| clause, `require_caller` without `get_session` | 1 failed, 1 passed; gate 1 failed, 45 passed (:1202–:1203) | re-run: same. Own: 1 failed, 4 passed; gate 1 failed, 48 passed | — | yes |
| clause, `get_session` sync | 1 failed, 1 passed (:1204) | re-run: same. Own: 2 failed, 3 passed (`ValueError: … created in a different Context`) | — | yes |
| clause, `get_session` async but not making the session current | — | own: 1 failed, 4 passed (`NoCurrentSession`) | — | (an added twin) |
| gate after T-03 / T-09 / T-05 / T-07 | 46 / 45 / 44 / 43 passed, lint clean (:1205–:1223) | Re-run: same. Own scaffold at T-03: 49 passed (44 + 5 own). Its lint findings (F401, 2 × E501) are in my scaffold files only; none is in a T-edited test | — | yes |
| after all four stages; the four files collected; the E-10 twin | no Null left; 5 collected; 3 errors (:1224–:1226) | re-run: same | — | yes |
| API twins: E-6b.10's stand-in / v1.2's | passes in all five states / passes at ADU-07's close, fails in each of the four landings (:1230–:1234) | Re-run: same. Own twins: own routers per domain, the stubs skip the landed domains, and at ADU-08 the module is deleted and main.py rewritten without it. My clause passes (5 passed) in all five states. My v1.2-form test sends GET /weeks: it passes at ADU-07's close and with ADU-04 landed, and fails from ADU-06 on (200 from the scheduling router) | — | yes |
| the last twin: the stubs gone; both mutations | no module, no reference; 1 failed each (:1235–:1237) | re-run: same. Own: no module and no src file naming it; 1 failed (no dependency), 2 failed (sync) | — | yes |
| a catch-all mounted at `/` inside `create_app` | — | own: 2 failed (`{"detail":"Not Found"}`) | — | (A-2 :59's condition carries weight) |
| simulated apply, recommended | 94 blocks into 7 files; ledger lint, plan check, render (0 files), derived check and pins check OK; "Open blocking questions: none" (:1239–:1262) | Re-run: same. Own, on an export of HEAD d38925b from my own composition, with D-12…D-18, Q-08…Q-13, O-02 and `<apply-date>` 2026-11-13: `ledgers OK`; `plan OK: 18 units`; 0 files rewritten; `derived blocks OK`; `pins OK (1 pinned)`; Now: ADU-03; "Open blocking questions: none"; non-blocking Q-02, Q-03, Q-05, Q-12; O-02 due ADU-04; gate line STATUS.md:41; next ids D-19, Q-14, O-03 | — | yes |
| simulated apply, E-5 (b) | 59 blocks into 6 files; Q-08…Q-11 STOP; Q-12 non-blocking (:1264–:1274) | re-run: same. Own: the same outputs, with D-12, D-13 and D-14 (= D-p7) | — | yes |
| M-1 on my recommended apply: Q-p7 entered as Q-14 | — | `ledgers OK`; `plan OK`; `derived blocks OK`; "Open blocking questions: none"; "Open non-blocking questions: Q-02, Q-03, Q-05, Q-12, Q-14"; gate line still STATUS.md:41 | — | — |
| `adu derived check` after a gate change in adu.toml (for Q-p7) | — | own scratch export of 7d1e7d4: exit 2, `CLAUDE.md: derived block "status --commands" is stale` | — | → Q-p7 |
| the B-5 and E-6 probes | as pasted | not re-run: the sections are byte-identical to v1.2 (md5), and no line about them changed since R2 | — | — |
| gate at HEAD | 46 passed (STATUS.md:40) | 46 passed, 1 warning in 26.34s; lint clean | — | yes |

There is no stochastic arm, so there is no binomial to check.

## 5. Findings
### Substantive (S-n)
None. D-p1's mechanism, E-6 (b)'s current session, E-6b.10's route of the test's own and E-10 (a)'s names behave as stated (§4).

### Needed edits (N-n)
None. Every claim checked is CONFIRMED, apart from two external facts that are UNVERIFIABLE and labelled as consequences (§2). R2's N-1 and all six of its notes are carried out (§1.1), and R1's dispositions hold (§1.3).

### Mechanical (M-n)
**M-1 · Enter this round's Q-p7 (§6) in OPEN-QUESTIONS.md.** It is D-2 step 4's "round R3's mechanical adaptations".
- Append the entry in §6, as written, after the last line of the Q-p6 entry that B-2.7 and the ruled E-10 block leave, with one blank line before its heading.
- Its id is the next one from `adu next-id Q` after the pack's six: Q-14 if main took none. Record it in docs/APPLICATION-REPORT-q07-retire-amends.md beside D-2 step 1's mapping.
- It is entered `**Blocking:** no`, so D-2's expectations stand. `adu status` lists it among the open non-blocking questions; it prints "Open blocking questions: none" under E-5 (a); and the gate line stays STATUS.md:41 (:42 under E-10 (d)). Measured on my own apply (§4).
- No pack block, Part E option or Owed row changes. An Owed row due ADU-12 is the operator's to add.

### Notes
- E-6 (:3086) leaves out ADU-05's amendment of tests/conftest.py (ADU-PLAN.md:211). It touches nothing the clause asserts through (§2.5 row 44).
- E-6b.10's last sentence (:3466), "an IdentityService method called with no session current raises db.NoCurrentSession", is met by a test of one method. A MemberDirectory method that opened a session of its own would then pass the route check, because the token is committed. D-p3's "never opens a session quietly" (E-6b.1 :3357) would then rest on review. This is by reading; my scaffold tests three methods.
- A-2 :59 says "nothing is mounted on the app `create_app` returns". What holds, and what the clause needs, is narrower: `create_app` (main.py, outside ADU-15's roster) gains no route or mount ahead of the test's route. A catch-all mounted at `/` inside it makes the clause answer 404 (§4).
- The header's "checked" list (:4) does not name E-1b.1, E-1b.2, E-3b.5 or E-4b.1. They are option variants of blocks it does name, and none is of FB-34's class beyond T-03.4 (§1.2).
- My v1.2-form test (GET /weeks) survives ADU-04 and fails at ADU-06; the pack's (GET /members) fails at ADU-04. The break moves with the operation chosen and comes by ADU-08 at the latest, as R2 N-1 said.
- T-07.3 (:540) says the file then holds "only the NullSwapsPort import, its two entries and its test". It also holds the shared parametrised test, and "its two entries" are that test's (own, after T-05). The file is deleted whole, so nothing turns on this.

## 6. Provisional questions
Numbered after the pack's Q-p1–Q-p6. The apply step allocates the id (M-1) and enters the text between the fences, character for character.
~~~text
### Q-p7 · 2026-11-13 · verification R3 (the M4 units' arms against later M4 units) · open
**Conflict:** Four arms of the browser milestone assert a state that a later unit of M4 replaces, and no later entry declares an edit of the completed test (plugin FB-34's class, outside Q-07). (1) ADU-12's arm (ADU-PLAN.md:407, frontend/tests/shell.test.tsx) renders the navigation "with placeholder routes in frontend/src/routes.ts"; ADU-17, ADU-13 and ADU-14 amend routes.ts to point at the real pages (:429, :456, :483), and none amends shell.test.tsx. (2) ADU-17's arm (:436, frontend/tests/sign-in.test.tsx) lands on the week-board route, "a placeholder page until ADU-13", which ADU-13 replaces (:456). (3) ADU-12's arm (:411) asserts "adu.toml's gate, fast and lint are the combined commands again and CLAUDE.md's derived block is current (adu derived check green)"; ADU-15 amends adu.toml's gate (:514) but not CLAUDE.md, whose commands block (CLAUDE.md:43–49) is derived from adu.toml and which is protected (adu.toml:19). ADU-12 declares CLAUDE.md (:401); ADU-15 does not. Measured on a scratch export: a gate change in adu.toml makes `adu derived check` exit 2 ("CLAUDE.md: derived block "status --commands" is stale"). (4) ADU-12's arm (:406) says "the dependency set is exactly D-09's", and D-09 lists @playwright/test (DECISIONS.md:14), while ADU-15 says frontend/package.json "gains the test:e2e script and @playwright/test (D-09)" (:512). Whether each test goes red depends on how its session writes it; the arms as worded invite the pin. Found by verification R3's search for FB-34's class (docs/VERIFICATION-R3.md §2.7).
**Blocking:** no — not for any unit before ADU-12 (derived position 13); it must be ruled before ADU-12 opens. An entry marked blocking would stop whatever unit is Now (plugin FB-32); an Owed row due ADU-12, O-01's pattern, is the operator's to add.
**Options:** (a) a design-change loop before ADU-12 rewords ADU-12's arms at :406, :407 and :411 and ADU-17's at :436, so that each asserts only what still holds after ADU-17, ADU-13, ADU-14 and ADU-15 land, and adds CLAUDE.md to ADU-15's amends beside adu.toml: plan text of units not yet built. (b) Q-07's pattern: ADU-17, ADU-13, ADU-14 and ADU-15 each declare the completed test they break (ADU-12's, and for ADU-13 ADU-17's) in their amends and edit it under the operator's grant. (c) left to the oversight session's D-0 check of ADU-12's hand-over.
**Recommendation:** none from the verifier; the architect's.
**Resolution:** none yet.
~~~

VERDICT: READY WITH MECHANICAL ADAPTATIONS
