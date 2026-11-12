# VERIFICATION-R2 — docs/PACK-q07-retire-amends.md v1.2 at 7d1e7d4 against HEAD 1745ed2
2026-11-12 · verifier session · read-only · gate run: `46 passed, 1 warning in 20.44s` (HEAD 1745ed2, `uv run pytest tests/ -q -m "not timing" -p no:cacheprovider`; `git status --short` before and after: `?? uv.lock`); lint `All checks passed!`

## 0. Snapshot gate
merge-base --is-ancestor: ok · drift on governing documents: 0 commits (allowed 0) · result: proceed
`adu snapshot check 7d1e7d4` → "snapshot OK: 7d1e7d4 is an ancestor of HEAD 1745ed2; governing documents unchanged since (0 commit(s), allowed 0)", exit 0. `git diff --stat 7d1e7d4 HEAD`: SESSION-JOURNAL.md, the pack, docs/VERIFICATION-R1.md only.
Start checks: `adu status` → Now: ADU-03; Q-07 open, blocking ("— STOP"). `UV_PROJECT_ENVIRONMENT` = `C:\dev\team-rota-data\.venv`, `PYTHONUTF8` empty, `ADU_PLUGIN_ROOT` = `C:\dev\adu-lifecycle`. Interpreter line: `C:\dev\team-rota-data\.venv cp1252 0`. `git status --short`: `?? uv.lock`. `adu role set verifier` ran (a session mark under `.adu/`, gitignored). `adu next-id V` was not run (FB-31). Plugin HEAD is c77cbeb; `git diff --stat 4b63bb0 c77cbeb` lists FEEDBACK.md only (3 insertions).

## 1. Earlier rounds
R1 (docs/VERIFICATION-R1.md, on v1.1 at bc98783) ended `STOP — MECHANICAL` (:227). Its dispositions, against pack v1.2:

| R1 item | Status | Where in pack v1.2 | Evidence |
|---|---|---|---|
| N-1 (R1 :170–:180) | CARRIED OUT | E-6b.10 :3091–:3100; E-6a.9 :3205–:3214; twin: B-4.2 :757, B-4.3 :779, output :1138–:1141 | The text E-6b.10 appends equals R1's clause (R1 :177) with "under D-p3" → "under the request's current session of design/INTERFACES.md (Domain services)" and no other change (checked by string substitution). Twin re-run with the pack's script: 2 passed; 1 failed (gate 1 failed, 45 passed); 1 failed. With my own scaffold: 3 passed; 2 failed (gate 2 failed, 45 passed); 2 failed (gate 4 failed, 43 passed) (§4). What the clause targets is new finding N-1 (§5). |
| N-2 (R1 :182–:187) | CARRIED OUT | B-2.7 Q-p5 :215; E-5a.14 :2698–:2708 (row :2707); E-5b.1 :2710–:2720 (row :2719); B-3.16 :692–:704; B-5 :2067; E-5 :2561–:2564; E-5a.1 :2566–:2574; D-2 :2213, :2218, :2227, :2234 | Q-p5 reads "**Blocking:** no — not for ADU-03, ADU-09, ADU-05 or ADU-07" (:215). Both rows have STATUS.md:29's five cells (O · Due · Where · Approval · Status). That is 6 pipes, checked in all 1,088 rulings. The Approval cell names "the ruling of E-5 (a)" or "(b)", and Where cites plugin FB-32. My own simulated apply on an export of HEAD (D-12…D-18, Q-08…Q-13, O-02) gives "Open blocking questions: none", "Now: ADU-03", "Open non-blocking questions: Q-02, Q-03, Q-05, Q-12" and "O-02 due ADU-04" (§4). |
| M-1 (R1 :191–:196) | CARRIED OUT | E-2b.8 :2369 (Q-07's resolution); E-2b.9 :2379 (the VERSIONS row, naming `files` and `depends`); E-2b.10–.12 :2389–:2417 (with E-5 (a), on E-5a.13/.8/.9's text); E-2b.13–.18 :2419–:2479 (with E-5 (b): v1.2, header, §Decisions, Current row, History title, ARCHITECTURE row) | Each matched in context in every ruling that selects it (both routes). Under E-2 (b) no composed file keeps "amends src/app/ports.py", "in `src/app/ports.py` is the one" or "ADU-16's module by a declared" (own scan). |
| M-2 (R1 :197–:199) | CARRIED OUT | E-3b.5 :2527 (without E-2 (b)); E-3b.6 :2537 | Under E-3 (b), and under E-3 (b) with E-2 (b), no composed file keeps `detail=""`, `detail, **extra` or `.detail` (own scan). |
| M-3 (R1 :200), row 40 | CARRIED OUT | E-1b.1 :2250; E-1b.2 :2260; E-1b.3 :2270–:2280 (position at :2271); E-1b.4 :2282; E-4 (b) as E-4b.1 :2551 | E-1b.1 uses B-2.4's string as it is: "injects `FakeMemberDirectory` through `create_app(member_directory=…)`, holding the member and token it needs" (post-B INTERFACES.md:126). The doubles line sits after ADU-03's tests/test_nulls.py line and before its ports.py line. Under E-1 (b) no composed file keeps "FakeMemberDirectory holding" (own scan). |
| Note: plugin HEAD (R1 :203) | CARRIED OUT | A-2 :36 | c77cbeb; 4b63bb0..c77cbeb changes FEEDBACK.md only (measured) |
| Note: A-2's last row (R1 :204), row 63 | CARRIED OUT | A-2 :44 | "Only :160 … and :161 … name `Refused`" |
| Note: E-7 (b) rules the later constructors (R1 :205) | CARRIED OUT | E-7 (b) :3218 | "Ruling (b) also rules the constructors of ADU-09's, ADU-05's and ADU-07's services" |
| Note: ARCHITECTURE.md:18 (R1 :206), row 79, §2.6 E-7 (a)'s seam (R1 :118) | CARRIED OUT | E-7a.5–.6 :3328–:3346; E-7b.4–.5 :3261–:3279; E-7a.4 :3318–:3326; D-p4 (a) :3303 | matched at post-B INTERFACES.md:129, :117 and ARCHITECTURE.md:18 |
| Notes: commit no API arm sees; ADU-04's route (R1 :207–:208) | CARRIED OUT | Q-p5 :214 ("Two more points sit inside the same wall"); B-3.16 :701 | — |
| Note: T-03.4's comment (R1 :209) | CARRIED OUT | T-03.4 :302 | "# member 1 with token tok_1, the caller the 501 loop needs (Q-07)" names no Null |
| Note: E-9.P and "is read as" (R1 :210), §2.6 E-9 | CARRIED OUT | E-9a.2 :3484 and E-9c.2 :3520 ("is superseded by the contract's Member"); :3464; E-9.P :3538 | the version is left to the pm-lead |
| Note: resolved questions keep "Blocking: yes" (R1 :211) | CARRIED OUT | E-5 (a) :2562 | adu.mjs:81 filters `q.open && q.blocking`; none is listed (measured) |
| Note: derived render (R1 :212) | CARRIED OUT | B-4.4 :2058 | 0 files rewritten (both runs) |
| §2.6 B-2.3 (R1 :115) | CARRIED OUT | B-2.3 :95, :102 (§Refused is a section of its own before §Domain services); :108 cites contracts/openapi.yaml:646 | openapi.yaml:646 reads "x-when-to-use: assert the code, never the detail text" verbatim. R1's :656 is PublishProblem's shorter "assert the code". |
| §2.6 E-8 (R1 :120), row 81 | CARRIED OUT, one line wrong | D-p5 (a) :3389 quotes hard rule 5 in full; E-8 (b) :3350 makes the scan point | the scan reports src/app/synthetic.py:12, not :70 (row 71) |
| row 82 (E-9) | CARRIED OUT | E-9 :3459 | DESIGN-REVIEW-7.md:36: "9. design/PRODUCT-DESIGN.md line 17" |
| row 83 (Part C) | CARRIED OUT | Part C :2132, :2133, :2134–:2137 | With `git grep` at 7d1e7d4, "the five protocols" is at ADU-PLAN.md:99 and tests/test_ports.py:1, and at SESSION-JOURNAL.md:153, a record. VERSIONS.md:90 reads "five protocols". test_nulls.py:1 is listed. Each E-6–E-9 term is found only where the row says. |
| §3 B-3.3 / T-03.6 (R1 :135) | CARRIED OUT | B-3.3 :567 | "line 105's two checks become two assert statements for the line length" |
| Q-p6 (R1 :217–:225) | CARRIED OUT | B-2.7 :220–:225; E-10 :3548–:4192 | (1) Complete text: (a) E-10a.1–.34, (b) E-10b.1–.11, (c) E-10c.1–.8, (d) E-10d.1–.6, each matched in every ruling. (2) The table (:3557–:3569) is true except one reason (row 70). (3) A recommendation with four reasons (:3571–:3577). (4) Rehearsed: after all four stages the four files collect together (5 tests) and the gate is green (43 passed); renamed `test_service.py` they give 3 errors (re-run, and own stand-ins). |

R1's §2.6 E-8 remark on `hmac.compare_digest` and the token formats ("harmless") asked for no change, and none was made.

## 2. Claims about the repository
**Method.** I used two routes.
1. The pack's script, extracted byte for byte from :1207–:2009 and re-run in the scratchpad. Its 416 output lines equal the pasted :787–:1202, apart from timings, scratch paths and object addresses.
2. My own line-based parser, independent of the pack's regex. It finds 196 replace blocks (B 24, T 24, E 148) and 1 deletion. B-blocks were checked against the LF-normalised blobs of `git show 7d1e7d4:<file>` and T-blocks stage by stage. E-blocks were checked in post-B text and in each of the 1,088 rulings, with my own selection, order and checks.

Every match was exact, so no markup-ignored fallback was needed.

### 2.1 B-blocks against the 7d1e7d4 blobs
| # | Block (pack line) | C / W / U | Evidence (file:line at 7d1e7d4) | Replacement matched |
|---|---|---|---|---|
| 1 | B-2.1 (:70) | C | DECISIONS.md:16, end of the last line (16 lines) | exact, unique, within the line |
| 2 | B-2.2 (:83) | C | design/INTERFACES.md:2 | exact, unique, within the line |
| 3 | B-2.3 (:94) | C | design/INTERFACES.md:79 | exact, unique, whole line |
| 4 | B-2.4 (:140) | C | design/INTERFACES.md:91 | exact, unique |
| 5 | B-2.5 (:153) | C | design/INTERFACES.md:103 | exact, unique |
| 6 | B-2.6 (:164) | C | OPEN-QUESTIONS.md:53 | exact, unique |
| 7 | B-2.7 (:175) | C | OPEN-QUESTIONS.md:59, the last line (59 lines) | exact, unique |
| 8 | B-2.8 (:228) | C | VERSIONS.md:14; Current (:9–:14) has no INTERFACES row | exact, unique |
| 9 | B-2.9 (:240) | C | VERSIONS.md:117, end of the last line | exact, unique, within the line |
| 10–11 | B-3.1 (:537), B-3.2 (:547) | C | ADU-PLAN.md:2, :6 (fragments) | exact, unique, within the line |
| 12–23 | B-3.3 (:558), B-3.4 (:570), B-3.5 (:582), B-3.6 (:593), B-3.7 (:605), B-3.8 (:616), B-3.9 (:626), B-3.10 (:638), B-3.11 (:649), B-3.12 (:659), B-3.13 (:671), B-3.14 (:682) | C | ADU-PLAN.md:151, :153, :159, :182, :184, :188, :208, :210, :216, :240, :242, :246, each a whole line | 12/12 |
| 24 | B-3.16 (:692) | C | ADU-PLAN.md:285 (blank) and :286 "### ADU-06 — Scheduling API" | exact, unique |

Applied bottom-up and re-located one by one, all 24 still match at their lines (own).

### 2.2 T-blocks, stage by stage
| # | Blocks | C / W / U | Evidence | Replacement matched |
|---|---|---|---|---|
| 25 | T-03.1–.6 (:262–:329) | C | conformance :1, :19, :23, :61, :102, :105 (7d1e7d4) | 6/6 |
| 26 | T-03.7–.10 (:333–:377) | C | test_nulls :11, :17, :28, :36; T-03.10 includes the two trailing blank lines | 4/4 |
| 27 | T-09.1–.6 (:381–:440) | C | conformance :24, :110; test_nulls :11, :18, :28, :48 (after T-03) | 6/6 |
| 28 | T-05.1–.6 (:444–:508) | C | conformance :24, :108; test_nulls :11, :15, :24, :30 (after T-09) | 6/6 |
| 29 | T-07.1–.2 (:512–:529), T-07.3 (:531) | C | conformance :24, :108 (after T-05). Before deletion, test_nulls holds only the NullSwapsPort import, its two entries and its test, as :532 says | 2/2; deletion as stated |
| 30 | T-03.4, the only T-block changed since v1.1 | C | own block-by-block diff of v1.1 and v1.2 (its comment) | — |

### 2.3 E-blocks against the text as B leaves it
| # | Claim | C / W / U | Evidence | Replacement matched |
|---|---|---|---|---|
| 31 | every E-block at its stated line (:812–:961) | C | 144 of 148 are unique at their stated line in post-B text alone (own) | 144/148 alone |
| 32 | the blocks "on the text E-xx writes": E-2b.10, .11, .12 (with E-5 (a)), E-10b.2 (with E-2 (b)) | C | each found once at VERSIONS.md:125, ARCHITECTURE.md:2, :52 and ADU-PLAN.md:148, after the other blocks of its file, in every ruling that selects it | 4/4 in context |
| 33 | conditional blocks: E-2b.13–.18 (with E-5 (b)); E-3b.5, E-10b.1, E-10c.1 (without E-2 (b)) | C | selected and matched only under their condition (own selection) | — |
| 34 | 1,088 rulings, 0 failures (:765–:770, :963–:972) | C | Own enumeration: 1,088/1,088, with the same block ranges per class (69–93 … 7–32). In every ruling: the DECISIONS rows D-p1… stand last and in id order; the Owed rows stand O-01, O-p1 (, O-p2), each with five cells; open and blocking questions are read as ledgers.mjs:77–85 reads them; under E-5 (a) INTERFACES keeps no Q-p1…Q-p4 | — |
| 35 | the constructor's three fragments compose (:3222) | C | own: all 8 E-6 × E-7 × E-8 compositions read as one valid signature | — |
| 36 | E-1 (b) and E-4 (b) shifts "T-09.2 :108, T-05.2 :106, T-07.2 :106; … by 4" (:2247, :2549) | C | own, applying the stated T-text: either alone gives 108/106/106, both give 106/104/104 | — |
| 37 | E-9.P (:3537) | C | design/PRODUCT-DESIGN.md:18, which B leaves untouched | 1/1 |
| 38 | E-10a.1–.28 rename the path and nothing else (:3549) | C | own: each new text equals its old text with tests/<d>/test_service.py → tests/<d>/test_<d>_service.py | — |

### 2.4 Part A-2, row by row
| # | Row (pack line) | C / W / U | Evidence |
|---|---|---|---|
| 39 | conformance :23 (:25) | C | `from app.identity.null_directory import NullDirectory  # noqa: E402`; twin 1 reproduced |
| 40 | :25–27 (:26) | C | the other three Null imports |
| 41 | :61, :70–71 (:27) | C | `TestClient(create_app(workspace=tmp_path))`; twin 2 reproduced (401 at :70) |
| 42 | :105–106 (:28) | C | four class checks on two lines |
| 43 | :111–118 (:29) | C | five `isinstance(obj, proto)` pairs |
| 44 | ADU-PLAN.md:129, :132 (:30) | C | the quoted text is there |
| 45 | test_nulls :11, :17, :28, :36 (:31) | C | import, `REPLACED`, protocol map, own test |
| 46 | test_nulls :12–14, :18–20, :29–31, :46, :57, :63 (:32) | C | as stated |
| 47 | main.py:40–43, :53–56 (:33) | C | keyword-only ports; `x or Null…()` per port |
| 48 | contract_stubs.py:82–84, :118–123 (:34) | C | `raise NotBuilt(op["operationId"])`; `caller=CALLER_DEP` when security ≠ [] |
| 49 | doubles.py:95–112; null_directory.py:15–17 (:35) | C | `add(…, token=…)` maps the token (:104–105); the Null's `tok_<n>` Caller at :15–17 |
| 50 | adu.mjs:687; c77cbeb; FB-28 (:36) | C | the immutability check reads no `amends`; FEEDBACK.md:33 `open` |
| 51 | adu.mjs:692–693 (:37) | C | roster = files + tests + amends files |
| 52 | adu.mjs:704 (:38) | C | the `rm` refusal names only the ledgers |
| 53 | ports.py:28–41 (:39) | C | MemberNotFound :28, AssignmentNotFound :32, TransferRefused :36–41 |
| 54 | test_ports.py:21, :38, :66, :117–118 (:40) | C | as stated; green with the illustrative `Refused` (re-run) |
| 55 | layering.json `forbidden` (:41) | C | `["scheduling","identity"]`, `["swaps","identity"]`, `["notifications","identity"]` |
| 56 | layering_scan.py:46–57, :101–104 (:42) | C | `layer_of` → None; `if li and lt and li != lt …` |
| 57 | INTERFACES.md, whole file (:43) | C | no IdentityService, no Refused |
| 58 | ADU-PLAN.md:160–165 (:44) | C | only :160 and :161 name Refused; :165 names MemberNotFound |
| 59 | ledgers.mjs:83–85; adu.mjs:81–82; FB-32 (:45) | C | `**Blocking:**` read with no unit scope; every open and blocking question listed with "— STOP"; FEEDBACK.md:37 `open` |
| 60 | adu.mjs:398 (:46) | C | `# expect: "Now: ${id}", "Open blocking questions: none", "Plan check: OK"` |
| 61 | STATUS.md:28–31; ledgers.mjs:26–27; adu.mjs:85–86; `next-id O` (:47) | C | columns O, Due, Where, Approval, Status; regex `O-\d+`; filter `^(paid|closed|done)`; `adu next-id O` → O-02 at HEAD |
| 62 | plan.mjs:234 (:48) | C | rule 19, a ✅ unit with an open Owed row |
| 63 | ADU-PLAN.md:149, :180, :206, :238 (:49) | C | four `tests/<domain>/test_service.py` |
| 64 | no `__init__.py` under tests/; pyproject (:50) | C | `git ls-tree` gives 0 hits; pyproject.toml:27–29 has testpaths and pythonpath, and no addopts; 3 errors reproduced; FEEDBACK.md:38 `open` |
| 65 | plan.mjs:181, :214, :219 (:51) | C | depends derived from unmocked consumes, stub owners and amends (:79–:97); an arm file must be in `tests:` (:214); every test file needs an arm (:219) |

### 2.5 Other claims
| # | Claim (pack line) | C / W / U | Evidence |
|---|---|---|---|
| 66 | B-3 intro (:535) | C | each B-3 `amends` line names ADU-02 or ADU-16, already amended; no files/tests/depends/size/arm-count change in B-3 |
| 67 | B-3.16 "(ADU-PLAN.md:385)", ":384" (:693) | C | :384 the Layer 6 prose; :385 "**Owed at this unit: O-01 (FB-02, release M1).**" |
| 68 | E-6b.10's reason, plan.mjs:160 (:3092) | C | `findProvisionalIds` → error |
| 69 | the guard queries (:736–:746, :1093–:1115) | C; one is not discriminating | Own queries, 12 paths × 8 roster variants (§4). Each allowed path is refused in the trees without its option, except pyproject.toml, which is allowed in all 8, 7d1e7d4 included |
| 70 | E-10's table (:3557–:3569) | C, except one cell **W** | Confirmed: 24 arms, 7/4/7/6 (own count); ADU-09's S cap of 3 files (plan.mjs:11); no protected path (adu.toml:19); ADU-00 owns pyproject.toml (ADU-PLAN.md:39); order unchanged (all 144 texts); 46 green in importlib mode. **Wrong**, the "a grant" cell of (c) (:3566): "the guard honours `amends` on a non-test file (plugin scripts/adu.mjs:692–693; asked in B-4.3)". pyproject.toml is outside `code_roots` (adu.toml:7, `["src","tests","frontend/src","frontend/tests"]`), so guardEdit never reaches the roster for it (adu.mjs:691). The cell's conclusion, "none", holds |
| 71 | E-8 (b) "would fail … also today, on src/app/synthetic.py:70" (:3350) | **W** (line) | the scan run on the export prints `src\app\synthetic.py:12: stdlib random imported`; :70 is `rng = random.Random(seed)`. The point stands |
| 72 | E-8 (a) passes that scan (implied at :3389) | C | determinism_scan.py flags stdlib `random` and `np.random.*` (:5, :27–:32), not `secrets` |
| 73 | E-8 (b) "624 32-bit words" (:3350); E-10 (c) "test modules cannot import one another" (:3575) | U (external; not re-researched) | stated plainly as consequences |
| 74 | Part C (:2121–:2145) | C | `git grep` at 7d1e7d4; the service test paths are in ADU-PLAN.md only; :2138's line list uses 7d1e7d4 numbering |
| 75 | D-2's ids (:2207–:2213) | C | `adu next-id` at HEAD: D-12, Q-08, O-02 |
| 76 | B-4.4 "the export's journal is the snapshot's" (:2013) | C | the script exports 7d1e7d4; my apply on HEAD names the 2026-11-12 10:40 block |
| 77 | the B-5 and E-6 probes (:2070–:2114, :2732–:2978) | C (not re-run) | each section is byte-identical to v1.1 (md5 per section); R1 re-ran both (R1 :159–:160) |

### 2.6 What B-2.3 and E-6–E-10 settle
- **B-2.3.** Since v1.1 it changes only §Refused's place and the source of "assert the code" (:95, :102, :108). Otherwise it stands as R1 §2.6 found it.
- **E-6 (b).** It settles the session, and E-6b.10 adds the arm R1 asked for. That arm's target is N-1.
- **E-6 (a).** The same, through E-6a.9, with the same target (N-1).
- **E-7 (a), (b).** Each settles the collaborators. E-7a.4–.6 and E-7b.4–.5 also add the omitted third cycle to INTERFACES (post-B :129) and ARCHITECTURE.md:18, and say so (:3216).
- **E-8, E-9.** They settle the source and the values. D-p5 (a) quotes hard rule 5 in full (:3389, as CLAUDE.md hard rule 5 reads), and D-p6 says "superseded".
- **E-10.** Each option changes only what its column says, and no option changes a T-block. Plan check is OK and the order unchanged for every text. The table is true except row 70's reason.
  - (a): 4 `tests:` lines and 24 arm files (path only), plus D-p7, Q-p6 and VERSIONS.
  - (b): the four `files:` lines (E-10b.1 or .2, .3–.5), plus D-p7, Q-p6 and VERSIONS.
  - (c): ADU-03's `depends` (E-10c.1, not with E-2 (b)) and `amends` (E-10c.2), plus D-p7, Q-p6 and VERSIONS.
  - (d): the O-p2 row, ADU-09's pointer, Q-p6's ruling and VERSIONS.

## 3. Criteria
| Arm / criterion | Five parameters | Can it fail (how) | Twin / mock / retirement | Finding |
|---|---|---|---|---|
| ADU-03 arm 1, :159 → B-3.5 (unchanged since v1.1) | n/a (deterministic) | as R1 §3: the binding is not the identity service or fails `ports.MemberDirectory`; null_directory.py exists; any import of it remains; either edited test is red | retires MK-04 | not weakened (R1 §3) |
| ADU-03 arm 1 with E-6b.10 | n/a | It fails if `require_caller` does not depend on `get_session` or `get_session` is sync (measured, both routes), and if a method with no current session does not raise `db.NoCurrentSession`. **It also fails, with nothing wrong in ADU-03, once the API unit that serves the probed operation lands** (measured) | twin measured | **N-1** |
| ADU-03 arm 1 with E-6a.9 | n/a | it fails if the directory's own session does not see the issued token; not rehearsed (the pack says so, :758); the same dependence on a stub | — | **N-1** |
| ADU-09, ADU-05, ADU-07 arm 1 (B-3.8, B-3.11, B-3.14; unchanged since v1.1) | n/a | as R1 §3 | retire MK-02, MK-01, MK-03 | not weakened |
| the 24 arms whose `file:` E-10 (a) renames (E-10a.2–.28) | n/a | arm text unchanged (row 38) | — | not weakened |
| ADU-02 arms :126–:133 after T-03 … T-07 | n/a | :129: 401 without a token and with `garbage` unchanged (:69, :72–73); 501 with tok_1 now against the injected double. :132: class checks become protocol checks; the clock and session tests are unchanged. :128 and :130 are untouched | — | kept; the gate after each stage is green (§4) |
| ADU-16 arms :99–:104 | n/a | the test_nulls entries leave with each Null, as :102 prescribes; test_ports.py stays unchanged and green with `Refused` | — | kept |
| Amendments ↔ T-blocks, both directions | — | — | — | B-3.3 ↔ T-03.1–.6 (now naming the split, :567); B-3.4 ↔ T-03.7–.10; B-3.6 ↔ T-09.1–.2; B-3.7 ↔ T-09.3–.6; B-3.9 ↔ T-05.1–.2; B-3.10 ↔ T-05.3–.6; B-3.12 ↔ T-07.1–.2; B-3.13 ↔ T-07.3. B-3.4's ports.py line and E-6b.6's db.py and deps.py lines falsify no immutable test (rehearsed: test_ports, test_models, test_synthetic and the session-sharing test are green). E-1b.3 (doubles.py) would hit test_ports.py:122–123 (`doubles.VACUOUS == ()`) only if TokenDirectory were labelled vacuous; its line says nothing else changes. Not rehearsed. E-2b.3 (layering.json, "test_layering.py stays green unchanged"): not rehearsed. E-10c.2 (pyproject.toml): measured, the 46 pass in importlib mode |
| Additions ↔ acceptance | — | — | — | E-6b.6 ↔ E-6b.10: R1 N-1 is closed. E-10 (b)'s `__init__.py` files and (c)'s addopts have no arm; without them, collection fails in the gate (measured) |
| Quantitative criteria | none (B-4.1) | — | no pin changes, no stochastic arm | no false-failure rate to re-derive |

## 4. Measurements
All runs are deterministic (seed n/a, interval —), made in the scratchpad (`…\scratchpad\r2run`, `\own`), never in the repository. `git status --short` stayed `?? uv.lock` throughout.

| Quantity | Subject's value (n) | Verifier's value (n, seed) | Interval | Agrees |
|---|---|---|---|---|
| blocks parsed | 196 (B 24, T 24, E 148) + 1 deletion (:787) | same, own parser | — | yes |
| B-blocks at their line in the blobs | 24/24 (:788–:811) | 24/24 (re-run and own) | — | yes |
| T-blocks per stage | 10, 6, 6, 2 + 1 deletion (:1128–:1159) | same (both routes) | — | yes |
| E-blocks, narrowest ruling | 148 OK (:812–:961) | re-run: same; own: 144 alone in post-B + 4 layered in context | — | yes |
| rulings | 1,088, 0 failures, block ranges per class (:963–:972) | 1,088/1,088 with the same ranges (both); own also checks row cell counts | — | yes |
| distinct plan texts / `adu plan check` | 144; exit 0; one output (:1090–:1091) | 144 (own composition); all exit 0, one output; order equal to the 7d1e7d4 export for all 144 | — | yes |
| plan check and order: B-3; recommended (B-3, E-6 (b), E-10 (a)) | `plan OK: 18 units`, the order of B-3.15 (:710–:732, :1042–:1088) | same; order identical to the pristine export (both) | — | yes |
| guard | :1093–:1115 | re-run: same answers. Own 12 × 8 grid: each allow is refused without its option, except pyproject.toml (allowed at 7d1e7d4 too) | — | yes; one query is not discriminating |
| E-10 on the 7d1e7d4 tree: planned / (a) / (b) / (c) without the files / (c) with them | 3 errors / 50 / 50 / 46 / 50 passed (:1118–:1122) | re-run: same. Own stand-ins (one test name in all four files): 3 errors / 50 / 50 / — / 50 | — | yes |
| baseline, export A | 46 passed, lint clean (:1124) | 46 passed, lint clean | — | yes |
| E-6 (b) scaffold, outside / inside a unit of work | NoCurrentSession / None (:1125) | same | — | yes |
| twin 1 / twin 2 | ModuleNotFoundError / 401 at :70 (:1126–:1127) | same | — | yes |
| N-1 twin: wiring right | 2 passed (:1138) | re-run: 2 passed. Own scaffold (own db.py, own deps.py edit, own stand-in, 3 tests): 3 passed, gate 47 passed | — | yes |
| N-1 twin: `require_caller` without `get_session` | 1 failed, 1 passed; gate 1 failed, 45 passed (:1139–:1140) | re-run: same. Own: 2 failed, 1 passed; gate 2 failed, 45 passed | — | yes |
| N-1 twin: `get_session` sync | 1 failed, 1 passed (:1141) | re-run: same. Own: 2 failed; gate 4 failed, 43 passed (ADU-02's 401/501 and session tests as well, as R1 :158 found) | — | yes |
| E-6b.10 as worded, once a router serves the probed operation (no subject value) | — | Own: with `scheduling.list_weeks` taken out of the stubs and served at GET /weeks, the stubbed-operation test has 1 failed; the probe-route test passes | — | → N-1 |
| gate after T-03 / T-09 / T-05 / T-07 | 46 / 45 / 44 / 43 passed, lint clean (:1142–:1160) | same: 44/42/40/38 completed tests (R1 :154) + 2/3/4/5 stand-ins | — | yes |
| after all four stages; the four files collected; the E-10 twin | no Null left; 5 collected; 3 errors (:1161–:1163) | same | — | yes |
| simulated apply, recommended | 94 blocks into 7 files; ledger lint, plan check, render (0 files), derived check and pins check OK; "Open blocking questions: none" (:1165–:1188) | Re-run: same. Own, on an export of HEAD, own substitution (D-12…D-18, Q-08…Q-13, O-02): the same outputs; Now: ADU-03; Q-12 non-blocking; O-02 due ADU-04 | — | yes |
| simulated apply, E-5 (b) | 59 blocks into 6 files; Q-08…Q-11 STOP; Q-12 non-blocking (:1190–:1200) | same (both) | — | yes |
| the scan's line for `random` | synthetic.py:70 (:3350) | synthetic.py:12 | — | no (the line only) |
| E-1 (b) and E-4 (b) line shifts | 108/106/106; "by 4" (:2247, :2549) | 108/106/106; 106/104/104 | — | yes |
| gate at HEAD | 46 passed (STATUS.md:40) | 46 passed, 1 warning in 20.44s; lint clean | — | yes |
| B-5 and E-6 probes | as pasted | not re-run: unchanged since v1.1 (row 77) | — | — |

There is no stochastic arm, so there is no binomial to check.

## 5. Findings
### Substantive (S-n)
None. D-p1's mechanism, E-6 (b)'s current session and E-10 (a)'s names behave as stated (§4).

### Needed edits (N-n)
**N-1 · E-6b.10 (and E-6a.9) tie ADU-03's own arm to a stubbed operation (blocking).**
- **The text.** E-6b.10 (pack :3099) appends to ADU-03's arm 1: "a request to a stubbed operation answers 501 not_built with Bearer <a token sign_in issued in that workspace> and 401 unauthenticated with Bearer garbage (require_caller reads the request's current session)". E-6a.9 (:3213) uses the same words, which are R1's (R1 :177).
- **The stubs go away.** ADU-04's amends says "the five identity operations move out of the stubs module" (ADU-PLAN.md:273). ADU-06 (:299), ADU-10 (:325) and ADU-08 (:349) do the same for theirs, and the 501 is "gone once the last router lands (ADU-08)" (:128). Q-p5 (pack :214) says "ADU-08 deletes src/app/api/contract_stubs.py".
- **The break.** Once ADU-03 is ✅ its test is immutable (CLAUDE.md hard rule 1).
  - Whichever operation the test sends, the API unit that serves it turns ADU-03's test red. After ADU-08 there is no stubbed operation left to send.
  - The pack's own stand-in sends `GET /members` (:1532), which is identity.list_members (contracts/openapi.yaml:72–74), so it goes red at ADU-04.
- **Nothing covers it.** No API entry amends ADU-03's test. Q-p5 (:214), ADU-04's pointer (B-3.16, :701) and the Where cell of both O-p1 rows (:2707, :2719) name only tests/api/test_contract_conformance.py and the helpers.
- **Measured (§4).** I took `scheduling.list_weeks` out of the stubs and served it with a router. The stubbed-operation form of the clause then fails. The same clause tested through a route the test registers itself passes, and it still fails under both of R1's mutations.
- **Fix.** The architect chooses one of these:
  1. In E-6b.10's new text, replace "a request to a stubbed operation answers 501 not_built with Bearer <a token sign_in issued in that workspace> and 401 unauthenticated with Bearer garbage" with "a route the test registers on that app, taking its caller from deps.require_caller, answers 200 with the caller's member id for Bearer <a token sign_in issued in that workspace> and 401 unauthenticated for Bearer garbage". Make the same change in E-6a.9. The route has the shape of the probe route at tests/api/test_contract_conformance.py:125–130. B-4.3's stand-in test then follows this form, with a third twin: the probed operation served by a router.
  2. Keep the words, and name ADU-03's test file in Q-p5's Conflict (:214), in B-3.16 (:701) and in both O-p1 rows (:2707, :2719), as one more completed test inside the API units' wall.

### Mechanical (M-n)
None for the apply step.

### Notes
- **E-10's table, the (c) grant cell (:3566), and B-4.3's guard query (:1111).** pyproject.toml lies outside `code_roots` (adu.toml:7), so the guard never applies a roster to it (adu.mjs:689–691). Measured: it is allowed in all 8 trees, 7d1e7d4 included. "No grant" holds, but the stated reason does not. Under (c), keeping pyproject.toml inside the roster rests on the session, not the guard.
- **E-8 (b) (:3350).** The scan reports synthetic.py:12, not :70. R1's row 81 carried :70.
- **E-1 (b) (:2247) and E-4 (b) (:2549).** They do not say that their T-text and line shifts are unrehearsed; only D-1 says so (:2178). Applying the stated text confirms the shifts.
- **Composed as text only, not labelled where stated:**
  - E-2b.3's "test_layering.py stays green unchanged" (:2324);
  - E-1b.3's doubles.py line;
  - the constructor shapes of E-7 (a), E-8 (b) and E-9 (c). B-4.3 binds the stand-in only "as E-7 (b) and E-8 (a) construct it" (:777).
- **ADU-11's route to the service.** ADU-11 creates the admin "through the composition root" (ADU-PLAN.md:378) by calling `seed_admin`, which the composition root binds only as `Ports.member_directory`. E-6b.1 (:2992) says "calls `seed_admin`" without saying on which object. Q-p5's second point (:214) names ADU-04's router only. ADU-11 (position 17) comes after Q-p5's loop.
- **Part C (:2132).** VERSIONS.md:90 reads "five protocols", without "the". The phrase is also at SESSION-JOURNAL.md:153, a ledger. The disposition is unaffected.
- **D-2 step 6 (:2229).** It cites STATUS.md:40 for the gate line. After the apply adds the Owed row it is :41 (B-4.4 :2033).

## 6. Provisional questions
None.

VERDICT: STOP — MECHANICAL
