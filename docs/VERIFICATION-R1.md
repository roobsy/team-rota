# VERIFICATION-R1 — docs/PACK-q07-retire-amends.md v1.1 at 7d1e7d4 against HEAD bc98783
2026-11-08 · verifier session · read-only · gate run: `46 passed, 1 warning in 17.89s` (HEAD bc98783, `uv run pytest tests/ -q -m "not timing" -p no:cacheprovider`; `git status --short` before and after: `?? uv.lock`); lint `All checks passed!`

## 0. Snapshot gate
merge-base --is-ancestor: ok · drift on governing documents: 0 commits (allowed 0) · result: proceed
`adu snapshot check 7d1e7d4` → "snapshot OK: 7d1e7d4 is an ancestor of HEAD bc98783; governing documents unchanged since (0 commit(s), allowed 0)", exit 0. `git diff --stat 7d1e7d4 HEAD`: SESSION-JOURNAL.md and the pack only.
Start checks: `adu status` → Now: ADU-03; Q-07 open, blocking. `UV_PROJECT_ENVIRONMENT`=`C:\dev\team-rota-data\.venv`, `PYTHONUTF8` empty, `ADU_PLUGIN_ROOT`=`C:\dev\adu-lifecycle`. The interpreter line printed `C:\dev\team-rota-data\.venv cp1252 0`. `adu role set verifier` ran (it writes the session mark under `.adu/sessions/`, which is gitignored). `adu next-id V` was not run (FB-31). The plugin is at 2855b8c, not the 4b63bb0 the pack cites (pack :29). `git diff --stat 4b63bb0 2855b8c` shows FEEDBACK.md only, so `scripts/adu.mjs` is unchanged and its line numbers hold.

## 1. Earlier rounds
None. No `docs/VERIFICATION-*.md` existed before this report. v1.0 (3082fd4) was never verified.

## 2. Claims about the repository
**Method.** I parsed the pack with my own line-based parser, independent of the pack's regex: it finds 109 replace blocks and 1 file deletion, the same as the pack's count (pack :734). Each `replace exactly` text was compared character for character with the LF-normalised blob from `git show 7d1e7d4:<file>`, or for E-blocks with the text as B leaves it. Each was checked for exactly one occurrence, a start at the stated line, and a full-line block starting at a line start. Blocks were applied bottom-up, and blocks sharing an anchor in reverse pack order, with each block re-located in the current text before it was applied. Every match was exact, so no markup-ignored fallback was needed.

### 2.1 B-blocks against the 7d1e7d4 blobs
| # | Block (pack line) | C / W / U | Evidence (file:line at 7d1e7d4) | Replacement matched |
|---|---|---|---|---|
| 1 | B-2.1 (:54) | C | DECISIONS.md:16, end of the last line (file has 16 lines, so D-p1, D-p2 land as rows 17–18) | exact, unique |
| 2 | B-2.2 (:67) | C | design/INTERFACES.md:2 "v1.0.1 (design v1.7, D-02)" | exact, unique |
| 3 | B-2.3 (:78) | C | design/INTERFACES.md:79 "## Test doubles (ADU-16, permanent — never deleted)" | exact, unique |
| 4 | B-2.4 (:124) | C | design/INTERFACES.md:91 "## Build order …" | exact, unique |
| 5 | B-2.5 (:137) | C | design/INTERFACES.md:103 | exact, unique |
| 6 | B-2.6 (:148) | C | OPEN-QUESTIONS.md:53 | exact, unique |
| 7 | B-2.7 (:159) | C | OPEN-QUESTIONS.md:59 "**Resolution:** none yet." (the file's last line) | exact, unique |
| 8 | B-2.8 (:205) | C | VERSIONS.md:14; Current (:9–14) has no INTERFACES row, as stated | exact, unique |
| 9 | B-2.9 (:217) | C | VERSIONS.md:117, end of the last line | exact, unique |
| 10 | B-3.1 (:514) | C | ADU-PLAN.md:2 | exact, unique |
| 11 | B-3.2 (:524) | C | ADU-PLAN.md:6, mid-line fragment | exact, unique |
| 12–23 | B-3.3 (:535), B-3.4 (:547), B-3.5 (:559), B-3.6 (:570), B-3.7 (:582), B-3.8 (:593), B-3.9 (:603), B-3.10 (:615), B-3.11 (:626), B-3.12 (:636), B-3.13 (:648), B-3.14 (:659) | C | ADU-PLAN.md:151, :153, :159, :182, :184, :188, :208, :210, :216, :240, :242, :246, each a whole line | exact, unique, 12/12 |

### 2.2 T-blocks, stage by stage (T-03 on 7d1e7d4, each later stage on the previous stage's output)
| # | Blocks | C / W / U | Evidence | Replacement matched |
|---|---|---|---|---|
| 24 | T-03.1–T-03.6 (:239–:296) | C | tests/api/test_contract_conformance.py:1, :19, :23, :61, :102, :105 | 6/6 exact |
| 25 | T-03.7–T-03.10 (:310–:337) | C | tests/test_nulls.py:11, :17, :28, :36; T-03.10 includes the two trailing blank lines | 4/4 exact |
| 26 | T-09.1–T-09.6 (:358–:404) | C | conformance :24, :110; test_nulls :11, :18, :28, :48 (post-T-03) | 6/6 exact |
| 27 | T-05.1–T-05.6 (:421–:467) | C | conformance :24, :108; test_nulls :11, :15, :24, :30 (post-T-09) | 6/6 exact |
| 28 | T-07.1–T-07.2 (:489–:498), T-07.3 (:508) | C | conformance :24, :108 (post-T-05). Before deletion, test_nulls.py holds only the NullSwapsPort import, `REPLACED`/protocol-map entries and its test, as T-07.3 states | 2/2 exact; deletion as stated |
| 29 | T-03.6 note "the line 113 characters, over ruff's 110" (:297) | C | measured 113; pyproject.toml `line-length = 110` | — |

### 2.3 E-blocks against the text as B leaves it
| # | Blocks | C / W / U | Evidence (post-B file:line) | Replacement matched |
|---|---|---|---|---|
| 30 | E-2b.1–.7 (:1765–:1825) | C | ADU-PLAN.md:147, :148, :155; design/ARCHITECTURE.md:12; design/INTERFACES.md:80; DECISIONS.md:18 (×2) | 7/7, alone and with E-3b |
| 31 | E-3b.1–.4 (:1839–:1869) | C | DECISIONS.md:18 (×2); design/INTERFACES.md:83, :85 | 4/4 |
| 32 | E-5a.1–.13 (:1889–:2009) | C | OPEN-QUESTIONS.md:59, :61, :68, :75, :82; INTERFACES.md:2; ARCHITECTURE.md:2 (×2), :52; VERSIONS.md:12, :120, :124 (×2) | 13/13 |
| 33 | E-6a.1–.8 (:2390–:2481) | C | INTERFACES.md:88, :93, :94, :95, :112; ARCHITECTURE.md:42; DECISIONS.md:18; OPEN-QUESTIONS.md:65 | 8/8 |
| 34 | E-6b.1–.9 (:2279–:2378) | C | INTERFACES.md:88, :93, :94, :112; ARCHITECTURE.md:42; ADU-PLAN.md:153; VERSIONS.md:123; DECISIONS.md:18; OPEN-QUESTIONS.md:65 | 9/9 |
| 35 | E-7a.1–.3, E-7b.1–.3 (:2498–:2563) | C | INTERFACES.md:94; DECISIONS.md:18; OPEN-QUESTIONS.md:72 | 6/6 |
| 36 | E-8a.1–.4, E-8b.1–.4 (:2580–:2672) | C | INTERFACES.md:94; ARCHITECTURE.md:45; DECISIONS.md:18; OPEN-QUESTIONS.md:78 | 8/8 |
| 37 | E-9a.1–.3, E-9c.1–.3 (:2693–:2750) | C | INTERFACES.md:102; DECISIONS.md:18; OPEN-QUESTIONS.md:85 | 6/6 |
| 38 | E-9.P (:2764) | C | design/PRODUCT-DESIGN.md:18 (B does not touch it) | 1/1 |
| 39 | "B-4.3 composes all 16" (:2499, :721) | C | all 16 combinations of E-6–E-9 with E-5 (a), each alone and with E-2 (b) + E-3 (b): 31/32 blocks and 42/43 blocks. Every block matched at its line, and the last six DECISIONS rows stand D-p1…D-p6 in id order. The only heading left `· open` is Q-p5, the only "**Resolution:** none yet." left is Q-p5's, and no Q-p1…Q-p4 reference is left in INTERFACES.md | 32/32 |
| 40 | E-1 (b) (:1757) "in B-3.3 and B-2.4 'FakeMemberDirectory holding member 1 ('Member 1', member, active) with token tok_1' becomes 'TokenDirectory'" | **W** | the string is in B-3.3's new text; it is absent from B-2.4's, which reads "injects `FakeMemberDirectory` through `create_app(member_directory=…)`, holding the member and token it needs" (pack :132) | — (M-3) |
| 41 | E-1 (b) / E-4 (b) line shifts "T-09.2 :108, T-05.2 :106, T-07.2 :106; … by 4" (:1757, :1882) | C | by arithmetic: T-03.4 is 3 lines → 1 and T-03.5 is 3 → 1, and T-03.1 keeps 3 lines. Not rehearsed (prose only, no blocks) | — |
| 42 | E-4 (b)'s clause to delete from B-3.3 (:1882) | C | present verbatim in B-3.3's new text | — |
| 43 | E-3 (b)'s "B-3.4's ports.py line reads …" and "tests assert `.reason`" (:1878) | C (text exists) | "gains Refused(reason, detail, **extra)" is in B-3.4, and "tests assert `.reason`, never `.detail`" is in B-2.3, but no block carries either change (M-2) | — |

### 2.4 Part A-2, row by row
| # | Row (pack line) | C / W / U | Evidence |
|---|---|---|---|
| 44 | conformance :23 module-level import (:18) | C | tests/api/test_contract_conformance.py:23 `from app.identity.null_directory import NullDirectory  # noqa: E402`; collection error reproduced (§4) |
| 45 | :25–27 the other three imports (:19) | C | lines 25–27 |
| 46 | :61, :70–71 (:20) | C | :61 `TestClient(create_app(workspace=tmp_path))`; :70–71 `Bearer tok_1` → `501 not_built`; 401 with the real directory reproduced (twin 2) |
| 47 | :105–106 class checks (:21) | C | four `isinstance(…, Null…)` on two lines |
| 48 | :111–118 protocol loop (:22) | C | five `(proto, obj)` pairs, `assert isinstance(obj, proto)` |
| 49 | ADU-PLAN.md:129, :132 (:23) | C | :129 "through MemberDirectory — the Null until ADU-03"; :132 "binds an implementation of each protocol (the Null until its provider lands)" |
| 50 | test_nulls :11, :17, :28, :36 (:24) | C | import, `REPLACED`, protocol map, own test |
| 51 | test_nulls :12–14, :18–20, :29–31, :46, :57, :63 (:25) | C | as stated |
| 52 | main.py:40–43, :53–56 (:26) | C | keyword-only `member_directory`…`notifier`; `x or Null…()` per port |
| 53 | contract_stubs.py:82–84, :118–123 (:27) | C | :83–84 `def handler(**_kwargs): raise NotBuilt(op["operationId"])`; :118–123 adds `caller=CALLER_DEP` when security ≠ []; no role check anywhere in the handler |
| 54 | doubles.py:95–112; null_directory.py:15–17 (:28) | C | `FakeMemberDirectory()` starts with empty `_members`/`_tokens` (:97–98); `add(…, token=…)` maps the token (:104–105); `caller_for_token` answers None for an unmapped token (:109–110) and for an inactive member (:112). `add(1, "Member 1", "member", token="tok_1")` gives `Caller(member_id=1, name="Member 1", role="member", active=True)`, the same as null_directory.py:15–17 for `tok_1` |
| 55 | plugin adu.mjs:687 (:29) | C | `… listOf(e.yaml?.tests).map(norm).includes(p) && !granted) deny(…immutable (hard rule 1)…)` (`amends` is not read on this path); FB-28 at plugin FEEDBACK.md:33, status `open` |
| 56 | adu.mjs:692–693 (:30) | C | `roster = new Set([...files, ...tests, ...amends.map((a) => a && a.file)])` |
| 57 | adu.mjs:704 (:31) | C | the `rm` refusal regex names only STATUS, SESSION-JOURNAL, OPEN-QUESTIONS, FEEDBACK, RETRO, VERSIONS, DECISIONS |
| 58 | ports.py:28–41 (:32) | C | `MemberNotFound` :28, `AssignmentNotFound` :32, `TransferRefused(reason)` :36–41 |
| 59 | test_ports.py:21, :38, :66, :117–118 (:33) | C | as stated; with a `Refused` class added to ports.py the gate stays green (§4) |
| 60 | layering.json `forbidden` (:34) | C | `["scheduling","identity"]`, `["swaps","identity"]`, `["notifications","identity"]` present |
| 61 | layering_scan.py:46–57, :101–104 (:35) | C | `layer_of` → None; `if li and lt and li != lt …`; tests/test_layering.py has no check for unlayered modules |
| 62 | INTERFACES.md whole file (:36) | C | no IdentityService, no Refused |
| 63 | ADU-PLAN.md:160–165 "… and raise `Refused(<reason>)`" (:37) | C, loosely | only :160 ("raises Refused(team_not_empty)") and :161 ("raised as Refused") name Refused; :162–:164 list reasons only; :165 names `MemberNotFound` |

### 2.5 Other claims
| # | Claim (pack line) | C / W / U | Evidence |
|---|---|---|---|
| 64 | A-1 quotes (:11–13) | C | ADU-PLAN.md:151, :159; ruling verbatim at OPEN-QUESTIONS.md:58; option 1 at :56 |
| 65 | B-3 intro: plan check rejects a provisional id; no files/tests/depends/size/arm-count change; each new `amends` names a unit already amended (:512) | C | plugin scripts/lib/plan.mjs:160 (`findProvisionalIds`). ADU-03 (:150–153), ADU-09 (:181–184), ADU-05 (:207–211) and ADU-07 (:239–242) already amend ADU-02 and ADU-16 |
| 66 | "Falsifies:" lines of B-3.3, B-3.4, B-3.6, B-3.7, B-3.9, B-3.10, B-3.12, B-3.13 (:536–:649) | C | conformance :23/:105/:61/:70; :25/:106; :26/:105; :27/:106; test_nulls :11/:17/:28/:36; :12/:20/:31/:63; :13/:18/:29/:46 |
| 67 | B-3.15 plan check and order, with B-3, with E-2 (b), with E-6 (b) (:669–:697, :928–:1015) | C | §4 (i) |
| 68 | the guard queries (:699–:705, :975–:989) | C | §4 (i): at 7d1e7d4 both tests refused as tests of completed ADU-16 / ADU-02, and ports.py refused as outside ADU-03's roster. With B-3, the two tests are still refused (FB-28) and ports.py is allowed. With B-3 + E-6 (b), db.py and deps.py are allowed |
| 69 | B-4.1 "none proposed … no pin changes … no twin owed" (:710) | C | every rewritten arm is `kind: deterministic`; no pinned file in any block |
| 70 | B-5 / Q-p1 probe output (:1653–:1657) | C | §4 (iii) |
| 71 | Q-p1 citations (:170) | C | main.py:52–58; ARCHITECTURE.md:42; INTERFACES.md:44, :77; ports.py:178–184, :206; test_ports.py:21; deps.py:33–40, :50 |
| 72 | Q-p2 citations (:177) | C | ADU-PLAN.md:203, :146; INTERFACES.md:92, :82 |
| 73 | Q-p3 citations (:184) | C | ARCHITECTURE.md:45; CLAUDE.md hard rule 5, quoted in full; models.py:52–54; synthetic.py:75, :85 |
| 74 | Q-p4 citations (:191) | C | openapi.yaml:104, :144, :178, :44; schemas Token :676, Member :684; PRODUCT-DESIGN.md:18 |
| 75 | Q-p5 citations (:198) | C | conformance :58–73, :66–67, :22, :63–64, :83, :86, :92, :99, :127; ADU-PLAN.md:273, :299, :325, :349, :281; contract_stubs.py:46 |
| 76 | Q-p5 "**Blocking:** yes for ADU-04 …; not for ADU-03, ADU-09, ADU-05 or ADU-07" (:199) and E-5 (a) "Q-p5 alone open, blocking ADU-04 … ADU-03 is handed over after the apply" (:1885) | **W** (against the tooling) | plugin scripts/lib/ledgers.mjs:83–85 reads `**Blocking:** yes` with no unit scope, and adu.mjs:81–82 lists every open + blocking question with "— STOP". Measured on the simulated apply (§4): `Open blocking questions: Q-12 (design-change loop Q-07 (the API units)) — STOP: a blocking question means stop, not proceed-and-guess`, with `Now: ADU-03`. The hand-over's C1 expects `"Open blocking questions: none"` (adu.mjs:398). → N-2 |
| 77 | E-6 (b) outside a request: the seed command, a test, no session current (:2026–:2029; E-6b.1 :2289–:2292) | C | all three stated. The seed-command text agrees with ADU-PLAN.md:378 ("creates the admin through the composition root and prints its id (exit 0)") and :379 ("exits 2 and prints team_not_empty"), and with PRODUCT-DESIGN.md:27 ("team_not_empty (the seed command: exit status 2, no HTTP)") |
| 78 | E-6 (b) measured behaviours 1–7 (:2031–:2038) | C | §4 (iii), both the pack's probe and an independent one |
| 79 | E-7 "INTERFACES.md:92 lists identity ↔ scheduling but not identity ↔ notifications" (:2493) | C | also true of design/ARCHITECTURE.md:18, which E-7 does not cite |
| 80 | E-7 (b) "the service is built inside the container's own constructor (src/app/main.py:52–58)" (:2495) | C | `app.state.ports = Ports(member_directory=… , …)` |
| 81 | E-8 (b) "the opt-in determinism scan … would also fail on `random` … it is not [enabled]" (:2577) | C | plugin adapters/python-fastapi-uv/determinism_scan.py docstring and `findings_for`; adu.toml `[adapter]` has only `name`. The scan would fail today on src/app/synthetic.py:70 as well, so the point is not specific to (b) |
| 82 | E-9 "PRODUCT-DESIGN.md:18 was added by DESIGN-REVIEW-7 finding 9 (design/DESIGN-REVIEW-7.md:36)" (:2686) | C | finding 9 at :36 (which names "line 17"); the three writes are `x-roles: [admin]` (openapi.yaml:95, :134, :175) |
| 83 | Part C hits (:1664–:1681) | C, one loose row | `git grep` at 7d1e7d4 confirms each row except "the five protocols": the phrase is at ADU-PLAN.md:99 and tests/test_ports.py:1, not at ARCHITECTURE.md:18 or INTERFACES.md:4. The disposition ("stays") is unaffected. tests/test_nulls.py:1's docstring ("one test per Null") is not listed |
| 84 | E-4 "git grep finds no other reference to the old name" (:1881) | C | only tests/api/test_contract_conformance.py:102 |
| 85 | D-2 ids "D-12 … D-17", "Q-08 … Q-12" (:1728–:1729) | C | `adu next-id D` → D-12; `adu next-id Q` → Q-08 |

### 2.6 What the IdentityService section and E-6–E-9 settle (D-1 item 4g)
- **B-2.3 §IdentityService.** Every signature and table cell traces to ADU-PLAN.md:159–165, spec.md:7–15, openapi.yaml (:32, :59, :77, :93, :104–126, :144–167, :178–196, :672, :693, :709–719), INTERFACES.md:21–28, :97, and PRODUCT-DESIGN.md:12, :14, :18, :27, :32. Three points use more than one source:
  - `passcode: str | None` comes from openapi.yaml:59 ("a missing passcode counts as wrong") and ADU-PLAN.md:277, against `required: [email, passcode]` at :672, under PRODUCT-DESIGN.md:14's lenient read.
  - `role: str | None` comes from MemberCreate and RoleChange, which do not require it (:709, :719).
  - The bucket order cites R-identity-08, which defers to PRODUCT-DESIGN.md:14's order.

  The open points are marked at the constructor line and the values comment (Q-p1–Q-p4). Two additions have no source (cosmetic, Notes): "tests assert `.reason`, never `.detail`" (pack :92; the nearest source is openapi.yaml:656, "x-when-to-use: assert the code"), and §Refused is placed inside "## Protocols" although it is not a protocol.
- **E-6 (a).** Settles the session point and amends ARCHITECTURE.md:42, saying so (E-6a.6). Its consequence for ADU-09 and ADU-05 is stated (:2022). It contradicts nothing it does not amend.
- **E-6 (b).** Settles the session point. It also fixes where the commit happens (the API layer, before it answers), which follows from the measured exit-after-response. It amends ARCHITECTURE.md:42 (E-6b.5). It is consistent with ARCHITECTURE.md:13–14 (layers 3 and 4 may import layer 1, `app.db`), ports.py:193 ("commits nothing") and :206 ("in the caller's session"). It states all three outside-request owners. Its additions have no acceptance arm: N-1.
- **E-7 (a).** Settles the point. Its seam contradicts INTERFACES.md:82 ("each provider unit replaces its own line by amendment"); D-p4 (a) says so (:2560) but does not amend :82.
- **E-7 (b).** Settles the point. D-p4 adds "Every later service is built the same way" (:2523), which fixes the constructor shape of ADU-09, ADU-05 and ADU-07. That goes beyond Q-p2's question as worded (the IdentityService), and E-7 (b)'s option text (:2495) does not say it (Note).
- **E-8 (a) and (b).** Each settles the source and amends ARCHITECTURE.md:45, saying so. Both also fix `hmac.compare_digest` and the token and salt formats, which go beyond the source point (harmless). D-p5 (a) quotes hard rule 5 as "randomness only through a passed generator" and drops "where the adapter says so" (CLAUDE.md hard rule 5).
- **E-9 (a) and (c).** Each settles the values and their home. D-p6 says PRODUCT-DESIGN.md:18 "is read as" the contract's Member. In effect it supersedes that line: openapi.yaml:697 uses the same words for MemberSummary ("as the team list shows them … never the email"). Q-p4 states the conflict openly, and the contract outranks PRODUCT-DESIGN in CLAUDE.md's authority order (6 before 7).
- **Composition.** All 16 combinations, alone and under E-2 (b) + E-3 (b), match and compose (§2.3 row 39). The composed constructors read as valid signatures in every combination inspected (bbaa, aabc + E-2b/E-3b, baba).

## 3. Criteria
| Arm / criterion | Five parameters | Can it fail (how) | Twin / mock / retirement | Finding |
|---|---|---|---|---|
| ADU-03 arm 1, ADU-PLAN.md:159 → B-3.5 | n/a (deterministic) | if `create_app(workspace=tmp_path)` binds something other than the identity service or something failing `ports.MemberDirectory`; if null_directory.py exists; if any import of `app.identity.null_directory` remains (main.py:18, conformance :23, test_nulls :11 at 7d1e7d4); if the conformance test or test_nulls is red in the gate (twins 1–2 measured). "exactly the edits … declared" can fail only on the oversight session's diff audit, as "unchanged" could before | retires MK-04 (ADU-PLAN.md:123) | Not weakened. Old: "MemberDirectory is bound to the identity service; … and its test_nulls test are deleted; the contract unit's tests stay green unchanged". New: concrete binding plus protocol, file absence plus an import scan, and the gate after the declared edits. Relaxing "unchanged" is the ruling's own (OPEN-QUESTIONS.md:58). Under E-6 (b), see N-1 |
| ADU-09 arm 1, :188 → B-3.8 | n/a | the same, for NullNotifier; keeps "the identity tests … stay green unchanged" | retires MK-02 | Not weakened; adds the contract unit's tests, which the old arm omitted |
| ADU-05 arm 1, :216 → B-3.11 | n/a | the same, for NullSchedulingPort; keeps the identity-tests clause | retires MK-01 | Not weakened |
| ADU-07 arm 1, :246 → B-3.14 | n/a | the same, and fails if tests/test_nulls.py or any of the four Null modules survives | retires MK-03 | Not weakened |
| ADU-02 arms :128, :130 after T-03…T-07 | n/a | conformance :41–55 and :76–99 untouched by any T-block | — | Kept |
| ADU-02 arm :129 after T-03.4 | n/a | 401 without a token (:69) and with `garbage` (:72–73) unchanged, now against the injected FakeMemberDirectory | — | Kept as the arm words it ("through MemberDirectory"). The composition root's default directory is no longer exercised over HTTP by any gate test until ADU-04 (:278); see N-1 |
| ADU-02 arm :132 after T-03.6 … T-07.2 | n/a | class checks become protocol checks (duplicating :111–118); clock :107–110 and session :121–135 unchanged | — | Kept: the arm pins "an implementation of each protocol" |
| ADU-16 arms :101–:102 | n/a | entries leave with each Null, as :102 prescribes ("each deleted together with its Null by the retiring unit (declared in that unit's amends)") | — | Kept. B-3 also covers the shared parametrised test's entries, which :102 does not name |
| Amendments ↔ T-blocks (both directions) | — | — | — | B-3.3 ↔ T-03.1–.6; B-3.4 (test_nulls) ↔ T-03.7–.10; B-3.6 ↔ T-09.1–.2; B-3.7 ↔ T-09.3–.6; B-3.9 ↔ T-05.1–.2; B-3.10 ↔ T-05.3–.6; B-3.12 ↔ T-07.1–.2; B-3.13 ↔ T-07.3. Every T-block is named by its B-3 line, and every B-3 test line has its T-blocks. B-3.3 does not name T-03.6's split into two statements (cosmetic; "no other assertion changes" holds). B-3.4's ports.py line hits no immutable test (measured) |
| E-6b.6's db.py and deps.py lines (under E-6 (b)) | — | **cannot fail at ADU-03**: measured, the ADU-03-stage gate is 44 passed with `require_caller` not depending on `get_session`, while every authenticated request through the default directory answers 500 | — | **N-1** |
| Quantitative criteria | none (B-4.1) | — | no pin is changed, so no twin is owed; no stochastic arm, so there is no false-failure rate to re-derive | C |

## 4. Measurements
All runs are deterministic (seed n/a, interval —) and were made in the scratchpad (`…\scratchpad\exp`, `\vst`, `\rehearsal`, `\combos`, `\probe1-3`), never in the repository. `git status --short` stayed `?? uv.lock` throughout.

| Quantity | Subject's value (n) | Verifier's value (n, seed) | Interval | Agrees |
|---|---|---|---|---|
| replace blocks / deletions parsed | 109 / 1 (:734) | 109 / 1, own line parser | — | yes |
| B-blocks matched, unique, at line | 23/23 (:735–:757) | 23/23 | — | yes |
| T-blocks matched per stage | 10, 6, 6, 2 + 1 deletion (:1021–:1048) | 10, 6, 6, 2 + 1 | — | yes |
| E-blocks matched singly | 62 (:758–:830) | 62 | — | yes |
| 16 combinations (alone / + E-2b + E-3b) | 31–32 / 42–43 blocks, rows in order (:833–:864) | same; sequential re-location | — | yes |
| `adu plan check` with B-3 | `plan OK: 18 units`, order as listed (:673–:674) | same; `adu plan order` output identical to the pristine export (md5 edeed79a…) | — | yes |
| … with B-3 + E-2 (b); B-3 + E-6 (b); B-3 + E-2 (b) + E-6 (b) | plan OK, order unchanged (:951–:1015) | plan OK; the same md5 in all four | — | yes |
| guard: tests ×2 / ports.py at 7d1e7d4 | exit 2 / 2 / 2 (:700–:702) | 2 / 2 / 2 | — | yes |
| guard with B-3 (and + E-6 (b)) | tests 2, 2; ports.py 0; db.py, deps.py 2 (then 0) (:980–:989) | same. Extra: with E-2 (b), refusals.py and layering.json 0 and ports.py 2; tests/support/doubles.py 2 throughout | — | yes |
| baseline gate, export with B-3 + E-6 (b) | 46 passed; lint clean (:1017) | 46 passed (the pack's script, re-run) | — | yes |
| gate after T-03 / T-09 / T-05 / T-07 | 44 / 42 / 40 / 38; lint clean (:1031–:1049) | pack's script: 44 / 42 / 40 / 38, lint clean. Own stand-ins and own scaffold: 44 / 42 / 40 / 38; at T-09…T-07 the lint findings were only in my stand-ins (src/app/notifications/service.py:3, src/app/swaps/service.py:3), none in the edited tests | — | yes |
| twin 1 (Null deleted, test unedited) | `ModuleNotFoundError: No module named 'app.identity.null_directory'` (:1019) | same | — | yes |
| twin 2 (import + class check only) | fails at :70 with 401 (:1020) | same | — | yes |
| E-6 (b) scaffold, outside / inside a unit of work | `NoCurrentSession` / `None` (:1018) | same | — | yes |
| E-6 (b) wiring mutations (no subject value) | — | correct wiring: gate 44 passed; HTTP `Bearer garbage` → 401, a real workspace token → 501 not_built. `require_caller` without `Depends(get_session)`: **gate 44 passed**, HTTP 500 / 500. `get_session` left sync: gate 2 failed (401/501 test, session-sharing test) | — | → N-1 |
| B-5 probe (sync vs async generator dependency) | None / visible; reset `ValueError` from the sync teardown (:1653–:1657) | same (the pack's probe re-run; own probe: sync reset raises "<Token var=… created in a different Context", async reset clean) | — | yes |
| E-6 probe items 1–7 | as pasted (:2264–:2276) | same, except thread names (the pack's probe re-run). Own probe without middleware: async dep seen by the sync dep and the endpoint; 3 committed writes on the worker thread persist, no SQLite thread error; a raise after yield (default scope) answers 200; 8 concurrent requests → 8 distinct sessions, no reset error | — | yes |
| simulated apply of the recommended set with ids substituted (D-12…D-17, Q-08…Q-12) (no subject value) | — | `ledgers OK`; `plan OK: 18 units`; `derived blocks OK` (render rewrites 0 files); `pins OK (1 pinned)`; `adu status`: **"Open blocking questions: Q-12 … — STOP"** with Now: ADU-03 | — | → N-2 |
| gate at HEAD | 46 passed (STATUS.md:40, 28.77s) | 46 passed in 17.89s | — | yes |
| test basenames (outside the pack) | — | two `tests/<domain>/test_service.py` without `__init__.py` on the 7d1e7d4 pyproject (pytest 9.2.0): `ERROR tests/notifications/test_service.py … 1 error during collection` | — | → Q-p6 |

## 5. Findings
### Substantive (S-n)
None. The mechanism of D-p1 (amends plus a per-session grant) and E-6 (b)'s current session both behave as stated (§4).

### Needed edits (N-n)
**N-1 · E-6 (b) adds amendments that no ADU-03 arm covers (blocking).**
- E-6b.6 (pack :2351–:2352) gives ADU-03 `{ unit: ADU-01, file: src/app/db.py … }` and `{ unit: ADU-02, file: src/app/api/deps.py, assertion: "get_session becomes an async generator dependency … require_caller depends on it, so caller_for_token reads the request's session …" }`.
- ADU-03's arms (ADU-PLAN.md:159–165, arm 1 as B-3.5 rewrites it) assert none of `NoCurrentSession`, `current_session`, `use_session`, `unit_of_work`, or the request path through `require_caller`.
- After T-03.4, no gate test sends a token through the composition root's default directory before ADU-04's arm at ADU-PLAN.md:278.
- Measured (§4): with `require_caller` not depending on `get_session`, every authenticated request answers 500, yet the ADU-03-stage gate is 44 passed. ADU-09, ADU-05 and ADU-07 would close on the same tree, and ADU-04 would then meet a fault in deps.py, which is not in its roster.
- Fix: E-6 (b) gains a plan block on ADU-03's arm 1 (post-B ADU-PLAN.md:161, B-3.5's text). Append before the closing quote:

  `; under D-p3, with the identity service bound by create_app(workspace=tmp_path), a request to a stubbed operation answers 501 not_built with Bearer <a token sign_in issued in that workspace> and 401 unauthenticated with Bearer garbage (require_caller reads the request's current session), and an IdentityService method called with no session current raises db.NoCurrentSession`

  It is checked like the other E-blocks, and the rehearsal then includes this twin.
- Under E-6 (a), the same HTTP path is unexercised before ADU-04 (the directory's own-session wiring). (a) amends no ADU-02 file beyond main.py, so it is cosmetic there.

**N-2 · Q-p5 entered "Blocking: yes" stops ADU-03 after the apply (blocking).**
- B-2.7 (pack :199) enters Q-p5 open with "**Blocking:** yes for ADU-04 (derived position 9); not for ADU-03, ADU-09, ADU-05 or ADU-07."
- The plugin has no unit scope. ledgers.mjs:83–85 sets `blocking` from `**Blocking:** yes`, and adu.mjs:81–82 prints every open + blocking question with "— STOP".
- Measured on the simulated apply: `Open blocking questions: Q-12 (design-change loop Q-07 (the API units)) — STOP: a blocking question means stop, not proceed-and-guess`, with `Now: ADU-03`. CLAUDE.md authority 3 says "an open blocking Q-nn means stop", and the hand-over's C1 expects "Open blocking questions: none" (adu.mjs:398).
- This contradicts E-5 (a) (pack :1885, "ADU-03 is handed over after the apply"), B-5 (:1611) and D-2 step 7 (:1741).
- Fix: enter Q-p5 as `**Blocking:** no — not for ADU-03, ADU-09, ADU-05 or ADU-07; it must be ruled before ADU-04 opens`. Track that duty where the tooling surfaces it, as O-01 is: an owed row in STATUS.md (:31 pattern) due ADU-04, and a pointer under ADU-04's entry, as ADU-PLAN.md:385 does for ADU-11. Alternatively the architect chooses another mechanism. Then align B-5 (:1611), E-5 (a) (:1885), E-5a.1 (:1896) and D-2 (:1729, :1741).

### Mechanical (M-n)
These apply only if a non-recommended option is ruled.
- **M-1 · E-2 (b).** Four texts must change if E-2 (b) is ruled:
  - B-2.7's Q-07 resolution (post-B OPEN-QUESTIONS.md:59) "ADU-03 amends src/app/ports.py" must read "ADU-03 adds src/app/refusals.py and amends tests/layering.json".
  - B-2.9's VERSIONS row (post-B VERSIONS.md:123) "ADU-03 amends src/app/ports.py (Refused, D-p2)" must read the same way, and must also name ADU-03's `depends` gaining ADU-00 and `files` gaining refusals.py.
  - Under E-5 (a), E-5a.13's ARCHITECTURE row must also name the layer-2 row change of E-2b.4.
  - Under E-5 (b) with E-2 (b), design/ARCHITECTURE.md changes (E-2b.4) with no version bump and no VERSIONS row.
  The pack's journal flagged the first two ("a v1.0 gap, for the verifier"); the composed text shows them.
- **M-2 · E-3 (b).** Its two consequential edits (pack :1878) have no block:
  - B-3.4's ports.py line: "gains Refused(reason, detail, **extra)" → "gains Refused(reason, **extra)" (post-B ADU-PLAN.md:155);
  - design/INTERFACES.md:85: "tests assert `.reason`, never `.detail`" → "tests assert `.reason`".
- **M-3 · E-1 (b).** Its instruction (pack :1757) names a string that B-2.4 does not contain (row 40). The apply must replace "injects `FakeMemberDirectory` through `create_app(member_directory=…)`, holding the member and token it needs" (post-B design/INTERFACES.md, B-2.4's paragraph) with "injects `TokenDirectory` through `create_app(member_directory=…)`". The new `{ unit: ADU-16, file: tests/support/doubles.py, … }` line has no stated position in ADU-03's `amends`.

### Notes
- Plugin HEAD is 2855b8c, not the 4b63bb0 the pack cites (pack :29); `scripts/adu.mjs` is unchanged between them.
- A-2's last row (pack :37) overstates: only ADU-PLAN.md:160–161 name `Refused` (row 63).
- E-7 (b)'s D-p4 "Every later service is built the same way" (pack :2523) rules the constructors of ADU-09, ADU-05 and ADU-07. Say so in E-7 (b)'s option text (:2495), so the operator rules it knowingly.
- design/ARCHITECTURE.md:18 also omits identity ↔ notifications. E-7 cites only INTERFACES.md:92, and neither is amended.
- D-p3 puts the commit in the API layer, but the arms of ADU-04, ADU-06, ADU-10 and ADU-08 do not assert that a write is visible to the next request. ADU-15's API end-to-end arm (ADU-PLAN.md:518) would catch a missing commit.
- B-2.3 binds the IdentityService only as `Ports.member_directory` (main.py:27–33), and how ADU-04's router reaches it is unstated. Because T-03.4 injects a FakeMemberDirectory there, at ADU-04 that test's app has no identity service. This is inside Q-p5's wall; ADU-04's hand-over must settle it.
- T-03.4's comment "# resolves tok_1 as the retired NullDirectory did (Q-07)" names a Null class. ADU-07's arm asserts imports, so it holds; a text scan for class names would match.
- E-9.P is labelled editorial (v1.7.1), but it changes what the design text says a write answers; VERSIONS.md:4 calls a requirement change a minor bump. That is the pm-lead's call. D-p6's "is read as" is in effect "is superseded by".
- Q-p1–Q-p4, entered resolved, keep "**Blocking:** yes — for ADU-03". This is harmless: `adu status` filters on open first, and they are not listed (measured).
- In the simulated apply, ADU-03's entry is unchanged by `adu derived render` (0 files rewritten).

## 6. Provisional questions
Numbered after the pack's Q-p1–Q-p5 to avoid a collision; the apply step allocates the ids.

**Q-p6 · 2026-11-08 · verification R1 (outside the pack; the plan's test paths) · open**
- **Conflict:** ADU-03, ADU-09, ADU-05 and ADU-07 each place their tests at `tests/<domain>/test_service.py` (ADU-PLAN.md:149, :180, :206, :238). tests/ holds no `__init__.py`, and pyproject.toml sets no import mode (`[tool.pytest.ini_options]`, 7d1e7d4).
- **Measured:** with pytest 9.2.0, two such files fail collection: `ERROR tests/notifications/test_service.py … Interrupted: 1 error during collection`. ADU-09, position 6, is the first to meet it. Its fix is outside ADU-09's roster: an `__init__.py` under tests/, or ADU-00's pyproject.toml.
- **Blocking:** no for ADU-03; yes before ADU-09 opens.
- **Options:**
  - (a) each service unit declares `tests/<domain>/__init__.py` in its `files`;
  - (b) ADU-09 amends ADU-00's pyproject.toml with `addopts = "--import-mode=importlib"`;
  - (c) unique basenames per domain, a plan edit that renames ADU-03's test file too, so it is cheapest before ADU-03 opens.
- **Recommendation:** none from the verifier; the architect's.

VERDICT: STOP — MECHANICAL
