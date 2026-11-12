# PACK — q07-retire-amends
v1.2 · 2026-11-12 · snapshot: 7d1e7d4 · status: verification pending (round R2)
Changed from v1.1 (bc98783; docs/VERIFICATION-R1.md, STOP — MECHANICAL), finding by finding: **N-1** → E-6b.10 appends R1's clause to ADU-03's arm 1, with its "under D-p3" written as "under the request's current session of design/INTERFACES.md (Domain services)" because the plan may carry no provisional id; E-6a.9 adds the same request path under E-6 (a); B-4.3 rehearses the twin. **N-2** → B-2.7 enters Q-p5 non-blocking; E-5a.14 / E-5b.1 write the Owed row O-p1 due ADU-04 (plugin FB-32); B-3.16 points ADU-04's entry to it; B-5, E-5 and D-2 are aligned; B-4.4 shows the simulated apply's `adu status` ("Open blocking questions: none", Now ADU-03). **M-1** → E-2b.8–E-2b.18. **M-2** → E-3b.5–E-3b.6. **M-3** → E-1b.1–E-1b.4, with E-4 (b) written as E-4b.1. **Notes**, in order: A-2 cites plugin c77cbeb (scripts unchanged since 4b63bb0); A-2's last row names only :160–:161; E-7 (b) says it rules the later constructors; E-7a.5–.6 and E-7b.4–.5 add the third cycle to both documents, and E-7a.4 names (a)'s seam in INTERFACES; Q-p5's text carries the commit no API arm sees and ADU-04's route to the IdentityService; T-03.4's comment names no class; E-9 says "superseded" and leaves E-9.P's version to the pm-lead; E-5 says why the resolved questions keep their Blocking lines; B-4.4 reports the derived render. **R1's other rows**: B-2.3 (§Refused a section of its own; the source of "assert the code"), B-3.3 (the split line), E-8 (hard rule 5 quoted in full; the scan point), E-9 (review line 17), Part C (the five protocols; test_nulls.py:1; the E-6–E-9 terms). **Q-p6** (plugin FB-33) → B-2.7 enters it and E-10 rules it, with (a) recommended and rehearsed. B-4.3's script covers every block in every ruling the brackets allow and is re-run in full. D-1 is round R2's prompt. D-2 takes E-1 … E-10 and writes the Owed row.
Input to the loop, not a replacement for it: every proposal below is in the documents' own vocabulary, for a verifier to check first and the release-manager to apply second. Every identifier here is provisional (D-p1 … D-p7, Q-p1 … Q-p6, O-p1, O-p2) until the apply step allocates it with `adu next-id`; `<apply-date>` is the apply step's date. Drafted by the architect (`/adu-lifecycle:change-design Q-07`, stage 1); the operator's ruling is written here, not re-opened.

**How to read the replacement blocks.** Each block is headed `#### <id> · <file>:<line>` and gives `replace exactly:` and `with:` as fenced `text` blocks; the fence content is the text, character for character, with line endings normalised (the Windows working tree is CRLF, the blobs LF). "(within the line)" means the text is a fragment of that line, with no line ending of its own; a fragment that runs on into the next line says so. An empty `with:` block removes the lines, line endings included. A block's line is where its text starts. B-blocks are numbered against 7d1e7d4, and E-blocks against the file as B leaves it. T-blocks are numbered against the file as the previous retirement leaves it: 7d1e7d4 for ADU-03.
- **Order.** Within a file, blocks are applied from the bottom up, so every stated line stays valid. Within a line they go right to left.
- **Shared anchors.** Blocks that share one anchor go in reverse pack order, so the rows stand in id order. The DECISIONS rows of E-6–E-10 all anchor at the end of DECISIONS.md:18 and go E-10's first. The Owed rows of E-10 (d) and E-5 both anchor at the end of STATUS.md:31 and go E-10's first.
- **Conditional blocks.** A heading that says "(with E-5 (a))", "(with E-5 (b))", "(with E-2 (b))" or "(without E-2 (b))" is applied only when that ruling holds.
- **Blocks on another block's text.** A heading that says "on the text E-xx writes" anchors on text another E-block writes. It is numbered against the file as the other blocks of the ruled options leave it, and is applied after them.
- **E-9.P** is the pm-lead's text: it is checked here and not applied by the apply step.

Every block was matched and applied by the script in B-4.3, alone and in each of the 1,088 rulings the brackets allow; its outputs are pasted there.

## Part A — the finding

### A-1 Q-07, as recorded (OPEN-QUESTIONS.md:53–59)
Conflict, in short (the entry quotes it in full): ADU-03's first arm (ADU-PLAN.md:159) says "src/app/identity/null_directory.py and its test_nulls test are deleted; the contract unit's tests stay green unchanged". Its first amendment (ADU-PLAN.md:151) says "test_contract_conformance.py still passes". ADU-02's completed `tests/api/test_contract_conformance.py` cannot stay green unchanged when the Null goes. The edit guard refuses `tests/test_nulls.py` although ADU-03's `amends` declares it. `Refused` and the IdentityService signatures are defined nowhere.
**Ruling (OPEN-QUESTIONS.md:58):** option 1, the operator, 2026-11-07, verbatim: "Add both tests to ADU-03's amends".
Option 1 as the entry states it (:56): both tests in ADU-03's `amends`, each with a hard-rule-1 grant; the Null import and the class check become protocol checks; `tok_1` is served by injecting a test directory through `create_app(member_directory=…)`; arm 1 reads "green after the declared amendments"; the same pattern is written now into ADU-09, ADU-05 and ADU-07; `Refused` and an IdentityService section are added to INTERFACES in the same loop.

### A-2 The evidence at 7d1e7d4 (every line re-read for this pack)
| Where | What it says or does | Why it matters |
|---|---|---|
| tests/api/test_contract_conformance.py:23 | `from app.identity.null_directory import NullDirectory  # noqa: E402`, at module level | deleting the Null fails the collection of the whole module (reproduced: B-4.3, twin 1) |
| tests/api/test_contract_conformance.py:25–27 | the module-level imports of NullNotifier, NullSchedulingPort and NullSwapsPort | the same wall for ADU-09, ADU-05 and ADU-07 |
| tests/api/test_contract_conformance.py:61, :70–71 | `TestClient(create_app(workspace=tmp_path))`; `Bearer tok_1` must answer `501 not_built` | the app's default directory resolves `tok_1`; the real one on an empty workspace answers 401 (reproduced: twin 2) |
| tests/api/test_contract_conformance.py:105–106 | `isinstance(p.member_directory, NullDirectory)` and three more class checks | they pin the Null by class |
| tests/api/test_contract_conformance.py:111–118 | `isinstance(obj, proto)` for each of the five ports | the protocol check already exists; a class check that becomes a protocol check adds nothing new |
| ADU-PLAN.md:129, :132 (ADU-02 arms) | "through MemberDirectory — the Null until ADU-03"; "binds an implementation of each protocol (the Null until its provider lands)" | the arms pin a protocol; the test pins a class, which is more than the arms ask, so making it a protocol check narrows nothing an arm requires |
| tests/test_nulls.py:11, :17, :28, :36 | the NullDirectory import, its `REPLACED` entry, its protocol-map entry in the shared parametrised test, and its own test | "the NullDirectory test is deleted" (ADU-PLAN.md:153) undercounts the edit: four places, one of them in the test shared by all four Nulls |
| tests/test_nulls.py:12–14, :18–20, :29–31, :46, :57, :63 | the same four places for each of the other Nulls | ADU-09, ADU-05 and ADU-07 |
| src/app/main.py:40–43, :53–56 | `create_app(…, *, member_directory=…, scheduling=…, swaps=…, notifier=…)`; each port is the injected object or else the Null | the injection seam the ruling names already exists; no edit to main.py is needed for the test |
| src/app/api/contract_stubs.py:82–84, :118–123 | every stub raises `NotBuilt` for any resolved caller; there is no role check | the injected caller's role does not matter for the 501 |
| tests/support/doubles.py:95–112 | `FakeMemberDirectory()` holds no member; `caller_for_token` resolves only a token given to `add(…, token=…)`, and answers None for an inactive member | **no existing double resolves `tok_1` as constructed.** FakeMemberDirectory resolves it once the test calls `add(1, "Member 1", "member", token="tok_1")`, which reproduces exactly the Caller the Null gave (`Caller(member_id=1, name="Member 1", role="member", active=True)`, src/app/identity/null_directory.py:15–17). The options are E-1 |
| plugin `scripts/adu.mjs:687` (plugin HEAD c77cbeb; `git diff --stat 4b63bb0 c77cbeb` lists FEEDBACK.md only, so every line cited from `scripts/` reads as it did at 4b63bb0) | a path in a completed unit's `tests:` is denied unless granted; `amends` is not consulted | every edit of a completed unit's test needs the operator's grant, with or without an `amends` line (plugin FB-28, plugin FEEDBACK.md:33, open) |
| plugin `scripts/adu.mjs:692–693` | the Now unit's roster is `files` + `tests` + `amends` files | `amends` is honoured for non-test files (main.py, a Null, ports.py, doubles.py, layering.json); no grant is needed there |
| plugin `scripts/adu.mjs:704` | the bash guard refuses `rm` only of the ledgers | removing `tests/test_nulls.py` at ADU-07 is not seen by any guard; the grant and the journal are its only record |
| src/app/ports.py:28–41 | `MemberNotFound`, `AssignmentNotFound`, `TransferRefused(reason)` with `.reason` | the cross-domain exceptions already live in the layer-2 module; `TransferRefused` is the precedent shape for `Refused` |
| tests/test_ports.py:21, :38, :66, :117–118 | the pinned signatures (`caller_for_token(self, token)`, `notify(self, event)`), `not hasattr(ports, "FixedClock")`, and "ports imports nothing of the product" | adding `Refused` to ports.py breaks none of them (rehearsed: B-4.3) |
| tests/layering.json, `forbidden` | `["scheduling","identity"]`, `["swaps","identity"]`, `["notifications","identity"]` and every other cross-domain pair | a `Refused` defined in identity's own module could not be imported by any later service |
| tests/layering_scan.py:46–57, :101–104 | `layer_of` returns None for a module in no layer, and no edge from or to such a module is ever flagged | a new module outside `tests/layering.json`'s layers would escape the ratchet |
| design/INTERFACES.md (whole file) | five protocols, doubles, bindings, build order, CLI, traceability; no IdentityService and no Refused | the two gaps the ruling names |
| ADU-PLAN.md:160–165 | arms 2–7 name seed_admin, add_member, change_role, deactivate, sign_in, caller_for_token, list_members and MemberSummary. Only :160 ("raises Refused(team_not_empty)") and :161 ("raised as Refused") name `Refused`; :162–:164 list reasons only, and :165 names `MemberNotFound` | the sources of the IdentityService section (B-2.3) |
| plugin `scripts/lib/ledgers.mjs:83–85`; `scripts/adu.mjs:81–82` | a question blocks when its body says `**Blocking:** yes`, with no field for which unit; `adu status` lists every open blocking question with "— STOP", whatever unit is Now | a question that blocks only ADU-04, entered `**Blocking:** yes`, stops ADU-03 (measured by R1, finding N-2; plugin FB-32, plugin FEEDBACK.md:37, open). Q-p5 is therefore entered non-blocking and owed by a row due at ADU-04 (E-5) |
| plugin `scripts/adu.mjs:398` | the hand-over's section A expects `adu status` to print "Open blocking questions: none" | ADU-03's hand-over after the apply needs no open blocking question |
| STATUS.md:28–31; plugin `scripts/lib/ledgers.mjs:26–27`, `scripts/adu.mjs:85–86` | the Owed table's columns are O, Due, Where, Approval, Status; `adu status` prints every row not paid, closed or done as "O-nn due ADU-nn (Where)" | an Owed row is shown in every session, as O-01 is; `adu next-id O` answers O-02 at HEAD |
| plugin `scripts/lib/plan.mjs:234` | plan check refuses a ✅ unit while an Owed row due at it is open (rule 19) | the row cannot be forgotten at ADU-04's close; that it is ruled before ADU-04 opens is the pointer's and the hand-over's (B-3.16) |
| ADU-PLAN.md:149, :180, :206, :238 | ADU-03, ADU-09, ADU-05 and ADU-07 each place a test file at `tests/<domain>/test_service.py` | four test files with one basename |
| tests/ (no `__init__.py` anywhere); pyproject.toml `[tool.pytest.ini_options]` (`testpaths`, `pythonpath = ["src", "tests"]`, no import mode) | pytest's default `prepend` mode imports each test file under its basename | the second `test_service.py` fails collection ("import file mismatch": 3 errors with all four, B-4.3; plugin FB-33, plugin FEEDBACK.md:38, open). `pythonpath` keeps `support` and `layering_scan` importable under any import mode |
| plugin `scripts/lib/plan.mjs:181`, :214, :219 | an entry's declared `depends` must equal the derived one, which counts every unit its `amends` names; an arm's `file` must be in `tests:`, and every `tests:` path needs an arm | an `amends` of ADU-00's file adds ADU-00 to `depends` (E-10 (c)); an `__init__.py` cannot sit in `tests:` without an arm, so E-10 (b) puts it in `files:` |

### A-3 What a correct mechanism must do, and must never do
**Must:** let each provider retire its Null in one session, together with every completed test that names that Null, edited exactly where it names it and nowhere else. Keep every assertion ADU-02's and ADU-16's arms require: the served operations' identity; 401 without a token and with an unknown one; 501 not_built with a resolved caller; every example validates; an implementation of each protocol bound; the injectable clock; one session per request. Keep hard rule 1 in the operator's hands: one grant per file, per session, recorded in that session's journal. Leave the other Nulls' tests untouched until their own provider. Define `Refused` and IdentityService before ADU-03 implements them, with every point the sources do not settle left visibly open. Let every service unit's test file collect beside the others'. Leave the Now unit free of a question that blocks only a later one (plugin FB-32).
**Must never:** skip, xfail or delete an assertion that is not about the Null. Weaken the 501 check (to "not 401", say). Bring the Null back under another name as the default binding. Let a later unit's edit ride on ADU-03's grant. Invent a signature the arms, the identity spec and the contract do not settle. Add a wiring that no arm of the unit that writes it can catch broken.

## Part B — the proposal

### B-1 DECISIONS rows (provisional)
| ID | Decision | Rationale / status |
|---|---|---|
| D-p1 | **Retiring a Null edits the completed tests that name it. Each such test is declared in the retiring unit's `amends` and edited only under the operator's grant.** The import goes, a class check becomes a protocol check, and a test that needs a resolved caller injects a double through `create_app(member_directory=…)`. Nothing else in the test changes. The edit guard does not honour `amends` on a completed unit's test (plugin FB-28), so the retiring session obtains the grant (`adu grant add <session> <file> "<reason>"`) before its first edit and records it in its journal block. | Q-07 option 1, ruled by the operator 2026-11-07, verbatim "Add both tests to ADU-03's amends". ADU-02's arms pin a protocol, not a class (ADU-PLAN.md:129, :132). Applies to ADU-03, ADU-09, ADU-05, ADU-07 |
| D-p2 | **`Refused(reason, detail="", **extra)` in `src/app/ports.py` is the one domain refusal.** Every service raises it for a refusal a story names. `reason` is a code of the Reason codes table, `detail` the plain sentence, `extra` the fields a story names. It carries no HTTP status: the API layer maps the bucket per operation (D-07), and the seed command exits 2. ADU-03 adds it to ADU-16's module by a declared amendment. | Part E-2, E-3. ports.py already holds the cross-domain exceptions and imports nothing of the product, so every service, the API and the CLI reach it without a forbidden edge. `TransferRefused` is the precedent shape |

E-6–E-10 add D-p3 … D-p7 (Part E), each in the text of the option the operator rules.

### B-2 Document amendments
The two rows above become B-2.1. The rest: design/INTERFACES.md (B-2.2–B-2.5), OPEN-QUESTIONS.md (B-2.6–B-2.7), VERSIONS.md (B-2.8–B-2.9). No change to design/ARCHITECTURE.md, the contract, the golden, PINS.lock, adu.toml or any test. STATUS.md gains one Owed row, written by the ruled option of E-5 (E-5a.14 or E-5b.1), and a second only under E-10 (d).

#### B-2.1 · DECISIONS.md:16
Why: D-p1, D-p2 (B-1).
replace exactly (within the line):
~~~text
raised by ADU-02's first read of its arms (reading the contract in process needs a parser the roster lacks) |
~~~
with:
~~~text
raised by ADU-02's first read of its arms (reading the contract in process needs a parser the roster lacks) |
| D-p1 | **Retiring a Null edits the completed tests that name it — each declared in the retiring unit's `amends` and edited only under the operator's grant.** The import goes, a class check becomes a protocol check (`isinstance(x, ports.<Interface>)`), and a test that needs a resolved caller injects a double through `create_app(member_directory=…)`; nothing else in the test changes. The edit guard does not honour `amends` on a completed unit's test (plugin FB-28; `scripts/adu.mjs:687`), so the retiring session obtains `adu grant add <session> <file> "<reason>"` from the operator before its first edit and records the grant in its journal block. ADU-03, ADU-09, ADU-05 and ADU-07 carry it for `tests/api/test_contract_conformance.py` and `tests/test_nulls.py` (removed by ADU-07 with the last Null). | <apply-date>, operator: Q-07 option 1, verbatim "Add both tests to ADU-03's amends" (2026-11-07), written by docs/PACK-q07-retire-amends.md; ADU-02's arms pin a protocol, not a class (ADU-PLAN.md:129, :132), so the edit narrows nothing an arm asks for; design/INTERFACES.md §Composition root bindings |
| D-p2 | **`Refused(reason, detail="", **extra)` in `src/app/ports.py` is the one domain refusal.** Every service raises it for a refusal a story names: `reason` is a code of PRODUCT-DESIGN's Reason codes table, `detail` the plain sentence, `extra` the fields a story names; it carries no HTTP status (the API layer maps the reason to its bucket's status per operation, D-07; the seed command exits 2). ADU-03 adds it to ADU-16's module by a declared amendment. | <apply-date>, operator (Part E of docs/PACK-q07-retire-amends.md); `src/app/ports.py` already holds the cross-domain exceptions (`MemberNotFound`, `AssignmentNotFound`, `TransferRefused`) and imports nothing of the product, so every service, the API and the CLI reach it without a forbidden edge (`tests/layering.json`); `TransferRefused` is the precedent shape; design/INTERFACES.md §Refused |
~~~

#### B-2.2 · design/INTERFACES.md:2
Why: the version, for a requirement added (the IdentityService and Refused sections).
replace exactly (within the line):
~~~text
v1.0.1 (design v1.7, D-02)
~~~
with:
~~~text
v1.1 (design v1.7, D-02; Q-07: D-p1, D-p2)
~~~

#### B-2.3 · design/INTERFACES.md:79
Why: D-p2 (Refused), and the IdentityService section the ruling asks for. Signatures come only from ADU-03's arms (ADU-PLAN.md:159–165), R-identity-01..09 (design/domains/identity/spec.md:7–15) and contracts/openapi.yaml. Each point those sources do not settle is marked open with its question (B-5). §Refused is a section of its own after the protocols, because it is an exception, not a protocol.
replace exactly:
~~~text
## Test doubles (ADU-16, permanent — never deleted)
~~~
with:
~~~text
## Refused (every domain → the API layer and the operator's command; an exception, not a protocol)
Provider: ADU-03, in `src/app/ports.py` beside `MemberNotFound`, `AssignmentNotFound` and `TransferRefused` (D-p2; ADU-03 amends ADU-16's module). Consumers: every service raises it; the API units map it to a Problem; the seed command (ADU-11) maps `team_not_empty` to exit status 2.
```
class Refused(Exception):
    def __init__(self, reason: str, detail: str = "", **extra: object) -> None   # .reason, .detail, .extra
```
Invariants: `reason` is a code of PRODUCT-DESIGN's Reason codes table (the values of the contract's `Problem.reason` and `PublishProblem.reason`, and `team_not_empty`); `detail` is the refusal's plain sentence and `extra` the fields a story names (`unfilled` for publish), because a refusal is {reason, detail, and the extra fields a story names} (PRODUCT-DESIGN, cross-cutting rules); `Refused` carries no HTTP status — the API layer maps the reason to its bucket's status per operation (D-07); a refusal changes nothing (services check before they write); tests assert `.reason`, never `.detail` (the contract's `Problem.reason`: "x-when-to-use: assert the code, never the detail text", contracts/openapi.yaml:646); `TransferRefused` stays the transfer's own signal (IR-02) and is never re-raised as `Refused` (an approval whose transfer was refused succeeds).

## Domain services (called by the API layer and the operator's command; not ports)
A service is called only from the layers above it — the API, the composition root, the CLI; another domain reaches it only through the ports above (D-05). Every operation a signed-in member performs takes the `Caller` that `deps.py` resolved (R-identity-06, IR-11); every refusal is `Refused(<reason>)`. A point the arms, the domain spec and the contract do not settle is marked open with its question, never filled in.

### IdentityService (identity → the identity API, the seed command)
Provider: ADU-03 (`src/app/identity/service.py`, persistence in `src/app/identity/repo.py`). Consumers: ADU-04 (the five identity operations), ADU-11 (`app seed-admin`), and ADU-07's §6 arm through the composition root. The same object implements MemberDirectory and is bound as it in `src/app/main.py` (ADU-03 arm 1).
```
class IdentityService:                          # implements MemberDirectory (above), and:
    def __init__(self, ...)                     # collaborators the arms name: a Clock, a SchedulingPort (IR-05), a Notifier (IR-10); how they are given: Q-p2; the request's session: Q-p1; the token and salt source: Q-p3 (all open)
    def seed_admin(self, name: str, email: str, passcode: str) -> int
    def add_member(self, caller: Caller, name: str, email: str, role: str | None, passcode: str) -> MemberValue
    def change_role(self, caller: Caller, member_id: int, role: str | None) -> MemberValue
    def deactivate(self, caller: Caller, member_id: int) -> MemberValue
    def sign_in(self, email: str, passcode: str | None) -> SignInValue
    def list_members(self, caller: Caller) -> list[MemberSummary]
# MemberValue: the contract's Member fields (id, name, email, role, active); SignInValue: the token and a MemberValue (the contract's Token);
# MemberSummary: id, name, role, active (ADU-03 arm 7). Their names, types and home: Q-p4 (open).
```
| Operation | Rule (source) | Emits | Refused with, by bucket (R-identity-08: forbidden → not_found → state → validation) |
|---|---|---|---|
| seed_admin | an empty team gets one active admin; the passcode stored as a salted SHA-256; answers the new id; no caller — an operator command outside the API (R-identity-07; ADU-03 arm 2) | nothing | state: team_not_empty |
| add_member | an active member with the role; the email unique, compared case-insensitively; a role that is missing or not admin, planner or member is invalid_role (R-identity-01, -02; the contract's MemberCreate.role is optional and "checked by identity") | MemberAdded(member_id, role) | forbidden (the caller is not an admin) · state: duplicate_email · validation: invalid_role |
| change_role | the same role is a no-op that answers the unchanged member and emits nothing; an inactive member's role may change and nobody is notified; the team keeps an active admin (R-identity-01, -03) | RoleChanged(member_id, role), except for the no-op and an inactive member | forbidden · not_found · state: last_admin · validation: invalid_role |
| deactivate | active false, the row kept; refused while `scheduling.has_assignment_after(member_id, clock.now())` (R-identity-03, -04, -05) | MemberDeactivated(member_id) | forbidden · not_found · state: future_assignments, last_admin, member_inactive (a repeat; nothing emitted) — their order within the bucket is US-identity-003's (PRODUCT-DESIGN, cross-cutting rules) |
| sign_in | the email matched case-insensitively and the passcode verified before the active check; a missing passcode counts as wrong; the new token replaces the member's earlier one; no caller (R-identity-06; the contract's 401 for identity.sign_in) | nothing | unauthenticated bucket: invalid_credentials (wrong or missing passcode, unknown email) · forbidden bucket: member_inactive (only after a correct passcode) |
| list_members | every member, active and inactive, as MemberSummary — never email, passcode or token — by name compared case-insensitively, then id (R-identity-09) | nothing | none: any signed-in caller |
| MemberDirectory | the six methods above over identity's own rows: caller_for_token is None for an unknown token and for an inactive member's (IR-11); is_active is None for an unknown id; role_of and name_of raise MemberNotFound; active_member_ids (IR-12); decider_ids the active admins and planners | — | none: no caller |

## Test doubles (ADU-16, permanent — never deleted)
~~~

#### B-2.4 · design/INTERFACES.md:91
Why: D-p1, the retirement pattern, beside the bindings it rebinds.
replace exactly:
~~~text
## Build order (the cycles, accepted explicitly — DESIGN-REVIEW-2 A18/D17)
~~~
with:
~~~text
**Retiring a Null (D-p1).** The provider unit rebinds its line in `src/app/main.py`, deletes the Null, and edits every completed test that names the Null by class: the import goes; a class check becomes a protocol check (`isinstance(x, ports.<Interface>)`); a test that needs a resolved caller injects `FakeMemberDirectory` through `create_app(member_directory=…)`, holding the member and token it needs. Each such test is a declared `amends` line of the provider and a hard-rule-1 edit: the session asks the operator for the grant (`adu grant add <session> <file> "<reason>"`) before its first edit, because the edit guard does not honour `amends` on a completed unit's test (plugin FB-28), and records the grant in its journal block. In this plan: ADU-03 (NullDirectory), ADU-09 (NullNotifier), ADU-05 (NullSchedulingPort) and ADU-07 (NullSwapsPort; `tests/test_nulls.py` removed with it), each editing `tests/api/test_contract_conformance.py` and `tests/test_nulls.py`.

## Build order (the cycles, accepted explicitly — DESIGN-REVIEW-2 A18/D17)
~~~

#### B-2.5 · design/INTERFACES.md:103
Why: the CLI is not an operation, so the in-process call it makes is the trace.
replace exactly:
~~~text
| US-identity-005 | seed the first admin | CLI `app seed-admin` |
~~~
with:
~~~text
| US-identity-005 | seed the first admin | CLI `app seed-admin` (IdentityService.seed_admin) |
~~~

#### B-2.6 · OPEN-QUESTIONS.md:53
Why: Q-07 is resolved by this loop.
replace exactly:
~~~text
### Q-07 · 2026-11-07 · ADU-03 (hand-over, the D-0 check) · open
~~~
with:
~~~text
### Q-07 · 2026-11-07 · ADU-03 (hand-over, the D-0 check) · resolved → D-p1
~~~

#### B-2.7 · OPEN-QUESTIONS.md:59
Why: the resolution and where it now lives. The questions this loop raises (B-5) are entered after it, each with its allocated id.
replace exactly:
~~~text
**Resolution:** none yet.
~~~
with:
~~~text
**Resolution:** option 1, as ruled. Applied <apply-date> from docs/PACK-q07-retire-amends.md (verified in docs/VERIFICATION-<id>.md): D-p1 (the retirement edits, each under the operator's grant) and D-p2 (Refused); ADU-PLAN v1.3 (the amends and retirement arms of ADU-03, ADU-09, ADU-05 and ADU-07; ADU-03 amends src/app/ports.py); design/INTERFACES.md v1.1 (§Refused, §Domain services with IdentityService, the retirement paragraph). The IdentityService section's open points are Q-p1–Q-p4; the same wall at the API units is Q-p5, entered non-blocking and owed before ADU-04 (O-p1); the four service units' same-named test files, found by verification R1, are Q-p6.

### Q-p1 · 2026-11-08 · design-change loop Q-07 (IdentityService) · open
**Conflict:** the real IdentityService is bound once, in `create_app` (src/app/main.py:52–58), before any request exists, yet it must read and write in the request's one session (design/ARCHITECTURE.md:42; design/INTERFACES.md:44, :77). The MemberDirectory methods take no session (src/app/ports.py:178–184; tests/test_ports.py:21 pins `caller_for_token(self, token)`), and `require_caller` resolves the caller through it without depending on `get_session` (src/app/api/deps.py:33–40, :50). ADU-03's arms, R-identity-01..09 and the contract do not say how the service reaches the session. The same seam decides the Notifier's write "in the caller's session" (ports.py:206) at ADU-09 and `SchedulingPort.transfer` at ADU-05, both of which must commit atomically with the caller's write (R-swaps-04). Measured (the pack's B-5 probe; fastapi 0.162.0, starlette 1.10.0, the project's venv): a ContextVar set in a sync generator dependency, the shape of `get_session`, is not visible to a sync endpoint (`None`), and its teardown runs in another Context (`ValueError: … was created in a different Context` on reset). Set in an async generator dependency, it is visible.
**Blocking:** yes — for ADU-03: the IdentityService section names no session until this is ruled.
**Options:** (a) explicit: every IdentityService operation takes the request's `session` as its first parameter (ADU-04 passes the one from `get_session`); the MemberDirectory methods read through a short session of their own on the workspace's engine (committed state). Consequence: no change to the ports or deps.py; but the Notifier and the transfer, which must write in the caller's transaction, cannot use it, so ADU-09 and ADU-05 need a second mechanism. (b) a request-scoped current session: the API layer makes the request's session current in an async dependency (deps.py, ADU-02's `files`, amended by ADU-03 without a grant), `require_caller` depends on it, and every port implementation bound in main.py reads it. Consequence: one mechanism for every port, read or write; it must be set from an async dependency (the measurement above). (c) per-request construction: deps.py builds the services and ports with the request's session and `app.state.ports` holds factories. Consequence: ADU-02's composition root changes shape, and with it the `isinstance` checks on `app.state.ports` in its completed test.
**Recommendation:** (b), ruled once for all four services: it is the only option that also serves the Notifier's and the transfer's atomic writes.
**Resolution:** none yet.

### Q-p2 · 2026-11-08 · design-change loop Q-07 (IdentityService) · open
**Conflict:** ADU-03's arms name three collaborators — the clock (arm 5: `has_assignment_after(member, now)`), a SchedulingPort (the FakeSchedulingPort, arm 5) and a Notifier (the SpyNotifier, arm 3) — but not how they are given. At ADU-05 the real SchedulingService consumes MemberDirectory (ADU-PLAN.md:203) while the identity service consumes SchedulingPort (:146), so both objects, bound once in `create_app`, need each other: design/INTERFACES.md:92 accepts this cycle at the import level only, and :82 says "each provider unit replaces its own line by amendment", which a constructor argument cannot do on a cycle.
**Blocking:** yes — for ADU-03: its constructor is what ADU-05 rewires.
**Options:** (a) constructor values, `IdentityService(clock, scheduling, notifier)`; ADU-05 closes the cycle after construction (an attribute set in main.py). (b) the service receives the composition root's `Ports` container (main.py:27–33; duck-typed, so identity never imports main) and reads `ports.scheduling` and `ports.notifier` at call time; each provider still replaces only its own line, and no setter exists. (c) the collaborators are passed with each call. Consequence: every API call site carries them; the arms do not suggest it.
**Recommendation:** (b).
**Resolution:** none yet.

### Q-p3 · 2026-11-08 · design-change loop Q-07 (IdentityService) · open
**Conflict:** ADU-03 arm 2 stores the passcode "as a salted SHA-256" and arm 6 "issues a token", but design/ARCHITECTURE.md:45 says "No randomness in the product", and CLAUDE.md hard rule 5 allows randomness "only through a passed generator where the adapter says so". A salt and an opaque bearer token are random by nature, and nothing names their source. `models.hash_passcode(passcode, salt)` (src/app/models.py:52–54) takes the salt as given; the fixture draws salts and tokens from its seeded generator (src/app/synthetic.py:75, :85).
**Blocking:** yes — for ADU-03 (arms 2, 3 and 6).
**Options:** (a) the service takes a token-and-salt source in its constructor; the composition root passes one built on the standard library's `secrets` (no new dependency), tests pass a deterministic one, and a DECISIONS row amends ARCHITECTURE.md:45 to "no randomness in the product except the injected token and salt source (`secrets`); never `random`". (b) a seeded `random.Random` passed in, the synthetic generator's pattern. Consequence: reproducible, but a bearer token becomes guessable from the seed, which is unacceptable for a credential. (c) a deterministic salt (from the email) and a token derived by HMAC from a configured secret. Consequence: no randomness, but the secret is an operator-held configuration the design does not mention.
**Recommendation:** (a).
**Resolution:** none yet.

### Q-p4 · 2026-11-08 · design-change loop Q-07 (IdentityService) · open
**Conflict:** arm 2 settles `seed_admin → id` and arm 7 names `MemberSummary` (id, name, role, active) for list_members. Arm 6 says sign_in "returns the member" without a shape, and arms 3–5 name no return for add_member, change_role and deactivate. The contract answers `Member` (id, name, email, role, active) for add_member 201, change_role 200 and deactivate 200, and `Token {token, member: Member}` for sign-in (contracts/openapi.yaml:104, :144, :178, :44; schemas :676, :684). design/PRODUCT-DESIGN.md:18 says a write answers "a member as the team list shows it", and the list never shows the email (R-identity-09). Where the value types live is unstated.
**Blocking:** yes — for ADU-03: ADU-04 consumes these values and ADU-03's tests assert them.
**Options:** (a) the contract wins, since ADU-02's golden pins it: the service returns a frozen value with the contract Member's fields for the three writes, (token, that value) for sign_in, and MemberSummary for list_members, all defined in src/app/identity/service.py (no other domain consumes them in process, D-05); PRODUCT-DESIGN.md:18 is read as "the member's row", and the pm-lead rewords it editorially. (b) the design wins: the writes answer MemberSummary, and the contract's three Member responses lose `email`. Consequence: a breaking contract change (D-07), so a design-change loop and a regenerated golden.
**Recommendation:** (a).
**Resolution:** none yet.

### Q-p5 · 2026-11-08 · design-change loop Q-07 (the API units) · open
**Conflict:** tests/api/test_contract_conformance.py:58–73 expects every operation except sign-in to answer `501 not_built` with a resolved caller, and sign-in to answer 501 (:66–67). ADU-04, ADU-06, ADU-10 and ADU-08 move their operations out of the stubs (ADU-PLAN.md:273, :299, :325, :349), after which those operations answer their real codes. ADU-08 deletes `src/app/api/contract_stubs.py`, which the test imports (line 22) for `example_path`, `example_body`, `validate_example`, `resolve` and `SESSION_DEP` (:63–64, :83, :86, :92, :99, :127); ADU-04's arm (ADU-PLAN.md:281) also uses "the conformance helper from ADU-02", which is `contract_stubs.validate_example` (src/app/api/contract_stubs.py:46). None of the four API entries declares the conformance test in its `amends`. This is Q-07's wall again, one milestone later. Two more points sit inside the same wall. First, ADU-04's router must reach the IdentityService, which the composition root binds only as `Ports.member_directory` (design/INTERFACES.md §IdentityService), while the 401/501 test's app binds a FakeMemberDirectory there (T-03.4 of docs/PACK-q07-retire-amends.md). Second, the arms of ADU-04, ADU-06, ADU-10 and ADU-08 do not assert that a write is visible to the next request, so only ADU-15's end-to-end arm (ADU-PLAN.md:518) would catch a write the API layer never commits.
**Blocking:** no — not for ADU-03, ADU-09, ADU-05 or ADU-07. It must be ruled before ADU-04 (derived position 9) opens, and the Owed row O-p1 (STATUS.md, due ADU-04) and ADU-04's entry carry that duty: `adu status` reads `**Blocking:** yes` as blocking whatever unit is Now (plugin FB-32).
**Options:** (a) the D-p1 pattern: each API unit's `amends` gains the conformance test under a grant; the 501 loop leaves out the operations its router now serves (sign-in leaves at ADU-04); ADU-08 moves the helpers to a surviving module and repoints the imports. Consequence: four more edits of a completed test. (b) one re-cut before ADU-04: the helpers move to a permanent module (e.g. tests/support/contract.py), and the 501 assertion iterates the operations contract_stubs still registers, so no later unit edits the test again. Consequence: one hard-rule-1 edit, made by ADU-04 or by a contract-maintenance unit.
**Recommendation:** (b), decided in a design-change loop before ADU-04 opens.
**Resolution:** none yet.

### Q-p6 · 2026-11-08 · verification R1 (the plan's test paths) · open
**Conflict:** ADU-03, ADU-09, ADU-05 and ADU-07 each place a test file at `tests/<domain>/test_service.py` (ADU-PLAN.md:149, :180, :206, :238). tests/ holds no `__init__.py`, and pyproject.toml's `[tool.pytest.ini_options]` sets no import mode, so pytest imports each test file under its basename and the second `test_service.py` fails collection ("import file mismatch"). Measured with pytest 9.2.0 on the 7d1e7d4 tree: docs/VERIFICATION-R1.md §4, and docs/PACK-q07-retire-amends.md B-4.3 (3 errors with all four). ADU-09, at derived position 6, is the first to meet it, and the fix is outside ADU-09's roster. Nothing in the method checks test basenames (plugin FB-33).
**Blocking:** no — not for ADU-03; it must be settled before ADU-09 opens. Once ADU-03 is ✅, renaming its test file is an edit of a completed unit's test (hard rule 1).
**Options:** (a) unique basenames, `tests/<domain>/test_<domain>_service.py`: a plan edit of the four units' `tests:` and arm files. (b) each service unit's `files:` gains `tests/<domain>/__init__.py`. (c) ADU-03 amends ADU-00's pyproject.toml with `addopts = "--import-mode=importlib"`. (d) deferred to a design-change loop before ADU-09, with an Owed row due ADU-09.
**Recommendation:** (a), ruled in this loop (docs/PACK-q07-retire-amends.md, Part E-10): it edits plan text only, and it is cheapest before ADU-03 opens.
**Resolution:** none yet.
~~~

#### B-2.8 · VERSIONS.md:14
Why: the versions this loop sets; design/INTERFACES.md has no Current row at 7d1e7d4 (its own header says v1.0.1).
replace exactly:
~~~text
| ADU-PLAN.md | 1.2 | the plan |
~~~
with:
~~~text
| design/INTERFACES.md | 1.1 | in-process interfaces (the ports, the domain services, the traceability) |
| ADU-PLAN.md | 1.3 | the plan |
~~~

#### B-2.9 · VERSIONS.md:117
Why: the History row of this loop.
replace exactly (within the line):
~~~text
ADU-11's entry carries the O-01 pointer (FB-02). |
~~~
with:
~~~text
ADU-11's entry carries the O-01 pointer (FB-02). |

### <apply-date> — ADU-PLAN v1.3, INTERFACES v1.1: Q-07, D-p1, D-p2 — the retirement edits under grants, Refused, IdentityService, the service units' test files (Q-p6)
| Document | From | To | What changed |
|---|---|---|---|
| ADU-PLAN.md | 1.2 | 1.3 | ADU-03, ADU-09, ADU-05, ADU-07: amends gain tests/api/test_contract_conformance.py and widen tests/test_nulls.py, each edited under the operator's grant (D-p1); ADU-03 amends src/app/ports.py (Refused, D-p2); the four retirement arms rewritten so they can be met; the Shape-of-the-cut sentence on retirement; ADU-04's entry points to the Owed row of Q-p5 (O-p1); the service units' test files: Q-p6; a requirement changed, hence the minor bump |
| design/INTERFACES.md | 1.0.1 | 1.1 | §Refused; §Domain services with IdentityService (signatures from ADU-03's arms, R-identity-01..09 and the contract; open points Q-p1–Q-p4); the retirement paragraph under the composition-root bindings; US-identity-005's trace names IdentityService.seed_admin; first row in Current |
~~~

### B-2.T The edits the retiring sessions make under their grants (normative content; not applied by the apply step)
Each block below is what the corresponding `amends` line in B-3 declares. The unit session makes these edits, only after the operator's grant for that file in that session. The apply step does not make them. They were applied stage by stage to the scratch export (B-4.3). Each stage also ran the gate and the lint there, with stand-in services in place of the real ones.

**ADU-03 — tests/api/test_contract_conformance.py** (at 7d1e7d4; T-03.2 and T-03.4 are E-1 option (a), T-03.1 and T-03.5 E-4 option (a))

#### T-03.1 · tests/api/test_contract_conformance.py:1
replace exactly:
~~~text
"""ADU-02 arms 3, 4, 5, 7: the served contract against contracts/openapi.json; auth on every operation; every
x-synthetic example validates against the schemas; the composition root binds a Null per port and the
clock."""
~~~
with:
~~~text
"""ADU-02 arms 3, 4, 5, 7: the served contract against contracts/openapi.json; auth on every operation; every
x-synthetic example validates against the schemas; the composition root binds an implementation of each
port (the Null until its provider lands) and the clock."""
~~~

#### T-03.2 · tests/api/test_contract_conformance.py:19
replace exactly:
~~~text
from support.doubles import FixedClock  # noqa: E402
~~~
with:
~~~text
from support.doubles import FakeMemberDirectory, FixedClock  # noqa: E402
~~~

#### T-03.3 · tests/api/test_contract_conformance.py:23
replace exactly:
~~~text
from app.identity.null_directory import NullDirectory  # noqa: E402
~~~
with:
~~~text
~~~

#### T-03.4 · tests/api/test_contract_conformance.py:61
replace exactly:
~~~text
    client = TestClient(create_app(workspace=tmp_path))
~~~
with:
~~~text
    directory = FakeMemberDirectory()  # member 1 with token tok_1, the caller the 501 loop needs (Q-07)
    directory.add(1, "Member 1", "member", token="tok_1")
    client = TestClient(create_app(workspace=tmp_path, member_directory=directory))
~~~

#### T-03.5 · tests/api/test_contract_conformance.py:102
replace exactly:
~~~text
def test_the_composition_root_binds_a_null_per_port_and_an_injectable_clock(tmp_path: Path) -> None:
~~~
with:
~~~text
def test_the_composition_root_binds_an_implementation_per_port_and_an_injectable_clock(
    tmp_path: Path,
) -> None:
~~~

#### T-03.6 · tests/api/test_contract_conformance.py:105
The protocol check makes the line 113 characters, over ruff's 110 (pyproject.toml `line-length`). The two assertions are therefore written as two statements, unchanged otherwise.
replace exactly:
~~~text
    assert isinstance(p.member_directory, NullDirectory) and isinstance(p.scheduling, NullSchedulingPort)
~~~
with:
~~~text
    assert isinstance(p.member_directory, ports.MemberDirectory)
    assert isinstance(p.scheduling, NullSchedulingPort)
~~~

**ADU-03 — tests/test_nulls.py** (at 7d1e7d4)

#### T-03.7 · tests/test_nulls.py:11
replace exactly:
~~~text
from app.identity.null_directory import NullDirectory
~~~
with:
~~~text
~~~

#### T-03.8 · tests/test_nulls.py:17
replace exactly:
~~~text
    NullDirectory: "ADU-03",
~~~
with:
~~~text
~~~

#### T-03.9 · tests/test_nulls.py:28
replace exactly:
~~~text
        NullDirectory: ports.MemberDirectory,
~~~
with:
~~~text
~~~

#### T-03.10 · tests/test_nulls.py:36
The block ends with the two blank lines that follow the function.
replace exactly:
~~~text
def test_null_directory_resolves_synthetic_tokens_and_answers_the_empty_value() -> None:  # deleted by ADU-03
    d = NullDirectory()
    assert d.caller_for_token("tok_7") == ports.Caller(
        member_id=7, name="Member 7", role="member", active=True
    )
    assert d.caller_for_token("tok_admin").role == "admin" and d.caller_for_token("garbage") is None
    assert d.is_active(7) is True and d.role_of(7) == "member" and d.name_of(7) == "Member 7"
    assert d.active_member_ids() == [] and d.decider_ids() == []


~~~
with:
~~~text
~~~

**ADU-09 — both files, as ADU-03 leaves them**

#### T-09.1 · tests/api/test_contract_conformance.py:24
replace exactly:
~~~text
from app.notifications.null_notifier import NullNotifier  # noqa: E402
~~~
with:
~~~text
~~~

#### T-09.2 · tests/api/test_contract_conformance.py:110
replace exactly:
~~~text
    assert isinstance(p.swaps, NullSwapsPort) and isinstance(p.notifier, NullNotifier)
~~~
with:
~~~text
    assert isinstance(p.swaps, NullSwapsPort) and isinstance(p.notifier, ports.Notifier)
~~~

#### T-09.3 · tests/test_nulls.py:11
replace exactly:
~~~text
from app.notifications.null_notifier import NullNotifier
~~~
with:
~~~text
~~~

#### T-09.4 · tests/test_nulls.py:18
replace exactly:
~~~text
    NullNotifier: "ADU-09",
~~~
with:
~~~text
~~~

#### T-09.5 · tests/test_nulls.py:28
replace exactly:
~~~text
        NullNotifier: ports.Notifier,
~~~
with:
~~~text
~~~

#### T-09.6 · tests/test_nulls.py:48
The block starts with the two blank lines before the function, the last in the file.
replace exactly:
~~~text


def test_null_notifier_records_and_writes_nothing() -> None:  # deleted by ADU-09
    n = NullNotifier()
    n.notify(ports.MemberAdded(member_id=1, role="admin"))
    assert len(n.sent) == 1 and type(n.sent[0]).__name__ == "MemberAdded"
~~~
with:
~~~text
~~~

**ADU-05 — both files, as ADU-09 leaves them**

#### T-05.1 · tests/api/test_contract_conformance.py:24
replace exactly:
~~~text
from app.scheduling.null_port import NullSchedulingPort  # noqa: E402
~~~
with:
~~~text
~~~

#### T-05.2 · tests/api/test_contract_conformance.py:108
replace exactly:
~~~text
    assert isinstance(p.scheduling, NullSchedulingPort)
~~~
with:
~~~text
    assert isinstance(p.scheduling, ports.SchedulingPort)
~~~

#### T-05.3 · tests/test_nulls.py:11
replace exactly:
~~~text
from app.scheduling.null_port import NullSchedulingPort
~~~
with:
~~~text
~~~

#### T-05.4 · tests/test_nulls.py:15
replace exactly:
~~~text
    NullSchedulingPort: "ADU-05",
~~~
with:
~~~text
~~~

#### T-05.5 · tests/test_nulls.py:24
replace exactly:
~~~text
        NullSchedulingPort: ports.SchedulingPort,
~~~
with:
~~~text
~~~

#### T-05.6 · tests/test_nulls.py:30
The block ends with the two blank lines that follow the function.
replace exactly:
~~~text
def test_null_scheduling_port_does_nothing_observable() -> None:  # deleted by ADU-05
    p = NullSchedulingPort()
    with pytest.raises(ports.AssignmentNotFound):
        p.assignment(1)
    assert (
        p.holds_intersecting_shift(1, 1) is False
        and p.has_assignment_after(1, datetime(2026, 11, 5, 9)) is False
    )
    assert p.transfer(1, 2) is None


~~~
with:
~~~text
~~~

**ADU-07 — both files, as ADU-05 leaves them**

#### T-07.1 · tests/api/test_contract_conformance.py:24
replace exactly:
~~~text
from app.swaps.null_port import NullSwapsPort  # noqa: E402
~~~
with:
~~~text
~~~

#### T-07.2 · tests/api/test_contract_conformance.py:108
replace exactly:
~~~text
    assert isinstance(p.swaps, NullSwapsPort) and isinstance(p.notifier, ports.Notifier)
~~~
with:
~~~text
    assert isinstance(p.swaps, ports.SwapsPort) and isinstance(p.notifier, ports.Notifier)
~~~

#### T-07.3 · tests/test_nulls.py — delete the file
By then it holds only the NullSwapsPort import, its two entries and its test (ADU-16 arm 4: "the file as a whole is removed with the last Null"). The bash guard does not see the removal (plugin `scripts/adu.mjs:704` refuses `rm` only of the ledgers), so the grant and the journal block are its only record.

### B-3 Plan amendments
Every `amends` line the pattern needs, and every retirement arm rewritten so it can be met. The plan text cites `Q-07` only, because `adu plan check` rejects a provisional id anywhere in the plan (plugin `scripts/lib/plan.mjs`, `findProvisionalIds`). No `files`, `tests`, `depends`, size or arm count changes. Each new `amends` line names a unit already in the entry's `amends` (ADU-02, ADU-16), so the derived `depends` and the order are unchanged. B-3.16 adds a prose pointer under ADU-04's entry. The test paths, and under some options `files` and `depends`, change only by the option of E-10 the operator rules (Part E).

#### B-3.1 · ADU-PLAN.md:2
replace exactly (within the line):
~~~text
v1.2 (the release manager's bump at M1's close; what changed is in VERSIONS.md)
~~~
with:
~~~text
v1.3 (the apply step of the Q-07 design-change loop; what changed is in VERSIONS.md)
~~~

#### B-3.2 · ADU-PLAN.md:6
Why: the Shape-of-the-cut sentence says a retirement amends "the Null and its stub test", which undercounts it (Part C).
replace exactly (within the line):
~~~text
the provider's acceptance retires the mock by rebinding `src/app/main.py` and deleting the Null and its stub test — both declared as `amends`, because they are other units' files.
~~~
with:
~~~text
the provider's acceptance retires the mock by rebinding `src/app/main.py`, deleting the Null, and editing the completed tests that name it (`tests/test_nulls.py`, `tests/api/test_contract_conformance.py`) — all declared as `amends`, because they are other units' files, and the two tests edited only under the operator's grant (Q-07).
~~~

#### B-3.3 · ADU-PLAN.md:151
Falsifies: tests/api/test_contract_conformance.py:23 (the import), :105 (the class check), :61/:70 (the default app's directory for `Bearer tok_1`). The test rename and docstring clause are E-4 (a).
replace exactly:
~~~text
  - { unit: ADU-02, file: src/app/main.py, assertion: "the composition root binds the real IdentityService as MemberDirectory; test_contract_conformance.py still passes", q: none }
~~~
with:
~~~text
  - { unit: ADU-02, file: src/app/main.py, assertion: "the composition root binds the real IdentityService as MemberDirectory; the NullDirectory import and its binding go", q: Q-07 }
  - { unit: ADU-02, file: tests/api/test_contract_conformance.py, assertion: "a completed unit's test, edited under the operator's grant (hard rule 1, Q-07): the NullDirectory import goes; the class check isinstance(p.member_directory, NullDirectory) becomes isinstance(p.member_directory, ports.MemberDirectory), and line 105's two checks become two assert statements for the line length; the 401/501 test builds its app with create_app(workspace=tmp_path, member_directory=directory), directory a FakeMemberDirectory holding member 1 ('Member 1', member, active) with token tok_1, so Bearer tok_1 still answers 501 not_built; the composition-root test is renamed test_the_composition_root_binds_an_implementation_per_port_and_an_injectable_clock and the module docstring reads 'binds an implementation of each port (the Null until its provider lands)'; no other assertion changes", q: Q-07 }
~~~

#### B-3.4 · ADU-PLAN.md:153
Falsifies: tests/test_nulls.py:11, :17, :28, :36. The ports.py line falsifies nothing: tests/test_ports.py stays green unchanged (rehearsed).
replace exactly:
~~~text
  - { unit: ADU-16, file: tests/test_nulls.py, assertion: "the NullDirectory test is deleted with its stub", q: none }
~~~
with:
~~~text
  - { unit: ADU-16, file: tests/test_nulls.py, assertion: "a completed unit's test, edited under the operator's grant (hard rule 1, Q-07): the NullDirectory import, its REPLACED entry and its protocol-map entry go, and test_null_directory_resolves_synthetic_tokens_and_answers_the_empty_value is deleted; the other Nulls' imports, entries and tests are unchanged", q: Q-07 }
  - { unit: ADU-16, file: src/app/ports.py, assertion: "gains Refused(reason, detail, **extra), the one domain refusal (design/INTERFACES.md, Refused); nothing else in the module changes and tests/test_ports.py stays green unchanged", q: Q-07 }
~~~

#### B-3.5 · ADU-PLAN.md:159
Why: ADU-03 arm 1 rewritten so it can be met. The parts its own test file can assert are made concrete; the rest is the gate's, as before.
replace exactly:
~~~text
  - { arm: "retires MK-04: MemberDirectory is bound to the identity service; src/app/identity/null_directory.py and its test_nulls test are deleted; the contract unit's tests stay green unchanged", file: tests/identity/test_service.py, kind: deterministic }
~~~
with:
~~~text
  - { arm: "retires MK-04: create_app(workspace=tmp_path) binds the identity service as MemberDirectory and it satisfies ports.MemberDirectory; src/app/identity/null_directory.py no longer exists and no module under src/ or tests/ imports app.identity.null_directory; the contract unit's tests and tests/test_nulls.py pass in the gate after exactly the edits this entry's amends declare on them, each made under the operator's grant (Q-07)", file: tests/identity/test_service.py, kind: deterministic }
~~~

#### B-3.6 · ADU-PLAN.md:182
Falsifies: the NullNotifier import and the `isinstance(p.notifier, NullNotifier)` check (tests/api/test_contract_conformance.py:25, :106 at 7d1e7d4).
replace exactly:
~~~text
  - { unit: ADU-02, file: src/app/main.py, assertion: "the composition root binds the real Notifier", q: none }
~~~
with:
~~~text
  - { unit: ADU-02, file: src/app/main.py, assertion: "the composition root binds the real Notifier; the NullNotifier import and its binding go", q: Q-07 }
  - { unit: ADU-02, file: tests/api/test_contract_conformance.py, assertion: "a completed unit's test, edited under the operator's grant (hard rule 1, Q-07): the NullNotifier import goes and the class check isinstance(p.notifier, NullNotifier) becomes isinstance(p.notifier, ports.Notifier); no other assertion changes", q: Q-07 }
~~~

#### B-3.7 · ADU-PLAN.md:184
Falsifies: tests/test_nulls.py:12, :20, :31, :63 (at 7d1e7d4).
replace exactly:
~~~text
  - { unit: ADU-16, file: tests/test_nulls.py, assertion: "the NullNotifier test is deleted with its stub", q: none }
~~~
with:
~~~text
  - { unit: ADU-16, file: tests/test_nulls.py, assertion: "a completed unit's test, edited under the operator's grant (hard rule 1, Q-07): the NullNotifier import, its REPLACED entry and its protocol-map entry go, and test_null_notifier_records_and_writes_nothing is deleted; the remaining Nulls' imports, entries and tests are unchanged", q: Q-07 }
~~~

#### B-3.8 · ADU-PLAN.md:188
replace exactly:
~~~text
  - { arm: "retires MK-02: Notifier is bound to the notifications service; src/app/notifications/null_notifier.py and its test_nulls test are deleted; the identity tests (which use the SpyNotifier double) stay green unchanged", file: tests/notifications/test_service.py, kind: deterministic }
~~~
with:
~~~text
  - { arm: "retires MK-02: create_app(workspace=tmp_path) binds the notifications service as Notifier and it satisfies ports.Notifier; src/app/notifications/null_notifier.py no longer exists and no module under src/ or tests/ imports app.notifications.null_notifier; the contract unit's tests and tests/test_nulls.py pass in the gate after exactly the edits this entry's amends declare on them, each made under the operator's grant (Q-07); the identity tests (which use the SpyNotifier double) stay green unchanged", file: tests/notifications/test_service.py, kind: deterministic }
~~~

#### B-3.9 · ADU-PLAN.md:208
Falsifies: the NullSchedulingPort import and the `isinstance(p.scheduling, NullSchedulingPort)` check (tests/api/test_contract_conformance.py:26, :105 at 7d1e7d4).
replace exactly:
~~~text
  - { unit: ADU-02, file: src/app/main.py, assertion: "the composition root binds the real SchedulingService as SchedulingPort", q: none }
~~~
with:
~~~text
  - { unit: ADU-02, file: src/app/main.py, assertion: "the composition root binds the real SchedulingService as SchedulingPort; the NullSchedulingPort import and its binding go", q: Q-07 }
  - { unit: ADU-02, file: tests/api/test_contract_conformance.py, assertion: "a completed unit's test, edited under the operator's grant (hard rule 1, Q-07): the NullSchedulingPort import goes and the class check isinstance(p.scheduling, NullSchedulingPort) becomes isinstance(p.scheduling, ports.SchedulingPort); no other assertion changes", q: Q-07 }
~~~

#### B-3.10 · ADU-PLAN.md:210
Falsifies: tests/test_nulls.py:13, :18, :29, :46 (at 7d1e7d4).
replace exactly:
~~~text
  - { unit: ADU-16, file: tests/test_nulls.py, assertion: "the NullSchedulingPort test is deleted with its stub", q: none }
~~~
with:
~~~text
  - { unit: ADU-16, file: tests/test_nulls.py, assertion: "a completed unit's test, edited under the operator's grant (hard rule 1, Q-07): the NullSchedulingPort import, its REPLACED entry and its protocol-map entry go, and test_null_scheduling_port_does_nothing_observable is deleted; the remaining Null's import, entries and test are unchanged", q: Q-07 }
~~~

#### B-3.11 · ADU-PLAN.md:216
replace exactly:
~~~text
  - { arm: "retires MK-01: SchedulingPort is bound to the scheduling service; src/app/scheduling/null_port.py and its test_nulls test are deleted; the identity tests (FakeSchedulingPort double) stay green unchanged", file: tests/scheduling/test_service.py, kind: deterministic }
~~~
with:
~~~text
  - { arm: "retires MK-01: create_app(workspace=tmp_path) binds the scheduling service as SchedulingPort and it satisfies ports.SchedulingPort; src/app/scheduling/null_port.py no longer exists and no module under src/ or tests/ imports app.scheduling.null_port; the contract unit's tests and tests/test_nulls.py pass in the gate after exactly the edits this entry's amends declare on them, each made under the operator's grant (Q-07); the identity tests (FakeSchedulingPort double) stay green unchanged", file: tests/scheduling/test_service.py, kind: deterministic }
~~~

#### B-3.12 · ADU-PLAN.md:240
Falsifies: the NullSwapsPort import and the `isinstance(p.swaps, NullSwapsPort)` check (tests/api/test_contract_conformance.py:27, :106 at 7d1e7d4).
replace exactly:
~~~text
  - { unit: ADU-02, file: src/app/main.py, assertion: "the composition root binds the real SwapsService as SwapsPort", q: none }
~~~
with:
~~~text
  - { unit: ADU-02, file: src/app/main.py, assertion: "the composition root binds the real SwapsService as SwapsPort; the NullSwapsPort import and its binding go, and no Null is bound any more", q: Q-07 }
  - { unit: ADU-02, file: tests/api/test_contract_conformance.py, assertion: "a completed unit's test, edited under the operator's grant (hard rule 1, Q-07): the NullSwapsPort import goes and the class check isinstance(p.swaps, NullSwapsPort) becomes isinstance(p.swaps, ports.SwapsPort), so the file imports no Null; no other assertion changes", q: Q-07 }
~~~

#### B-3.13 · ADU-PLAN.md:242
Falsifies: the whole of tests/test_nulls.py (ADU-16 arms 3–4).
replace exactly:
~~~text
  - { unit: ADU-16, file: tests/test_nulls.py, assertion: "the NullSwapsPort test is deleted with its stub; the file is removed with this last Null", q: none }
~~~
with:
~~~text
  - { unit: ADU-16, file: tests/test_nulls.py, assertion: "a completed unit's test, removed under the operator's grant (hard rule 1, Q-07): the file, which by then holds only the NullSwapsPort import, entries and test, is deleted with this last Null", q: Q-07 }
~~~

#### B-3.14 · ADU-PLAN.md:246
replace exactly:
~~~text
  - { arm: "retires MK-03: SwapsPort is bound to the swaps service; src/app/swaps/null_port.py and its test_nulls test are deleted (test_nulls.py removed with the last Null); the scheduling tests (FakeSwapsPort double) stay green unchanged", file: tests/swaps/test_service.py, kind: deterministic }
~~~
with:
~~~text
  - { arm: "retires MK-03: create_app(workspace=tmp_path) binds the swaps service as SwapsPort and it satisfies ports.SwapsPort; src/app/swaps/null_port.py and tests/test_nulls.py no longer exist and no module under src/ or tests/ imports a Null (app.identity.null_directory, app.notifications.null_notifier, app.scheduling.null_port, app.swaps.null_port); the contract unit's tests pass in the gate after exactly the edits this entry's amends declare on them, each made under the operator's grant (Q-07); the scheduling tests (FakeSwapsPort double) stay green unchanged", file: tests/swaps/test_service.py, kind: deterministic }
~~~

#### B-3.16 · ADU-PLAN.md:285
Why: Q-p5 is entered non-blocking (plugin FB-32). The duty to rule it before ADU-04 opens is carried where every session sees it: the Owed row due ADU-04 (E-5a.14 or E-5b.1), and this pointer, as ADU-11's entry carries O-01's (ADU-PLAN.md:385). It names no provisional id, because the plan may carry none. The block starts with the blank line before ADU-06's heading, so the pointer follows ADU-04's yaml block directly, as ADU-11's prose does (ADU-PLAN.md:384). It sits before B-3.15 because B-3.15 is the check of all sixteen.
replace exactly:
~~~text

### ADU-06 — Scheduling API
~~~
with:
~~~text
**Owed before this unit opens (Q-07's design-change loop).** The API units' wall is open. ADU-02's completed `tests/api/test_contract_conformance.py` expects 501 not_built from every operation this unit moves out of the stubs. It also imports the helpers of `src/app/api/contract_stubs.py`, which ADU-08 deletes and this unit's fifth arm uses. The question is entered non-blocking with an Owed row due at this unit in STATUS.md, which `adu status` lists in every session, because a question entered `**Blocking:** yes` would stop whatever unit is Now (plugin FB-32). It is ruled in a design-change loop before this unit's hand-over. The same loop settles how this unit's router reaches the IdentityService, which the composition root binds only as `Ports.member_directory`, and whether the API units' arms assert that a committed write is visible to the next request. Until then this entry's `amends` and arms stand as written; `adu plan check` refuses its ✅ while the row is open (rule 19).

### ADU-06 — Scheduling API
~~~

#### B-3.15 The plan after the change, checked on a scratch copy
`git archive 7d1e7d4` exported to the scratchpad (outside the repository), B-3.1–B-3.14 and B-3.16 applied by the B-4.3 script, then `adu plan check` and `adu plan order` with the working directory inside the copy (B-4.3's output, part 4):

~~~text
$ adu plan check   # scratch copy with B-3 applied, exit 0
plan OK: 18 units, order ADU-00 → ADU-01 → ADU-16 → ADU-02 → ADU-03 → ADU-09 → ADU-05 → ADU-07 → ADU-04 → ADU-06 → ADU-10 → ADU-08 → ADU-12 → ADU-17 → ADU-13 → ADU-14 → ADU-11 → ADU-15

$ adu plan order   # scratch copy with B-3 applied, exit 0
 1. ADU-00 — Scaffold and method guard (layer 0, size M)
 2. ADU-01 — Data model and the seeded fixture (layer 1, size M)
 3. ADU-16 — Ports, Null implementations and test doubles (layer 2, size M)
 4. ADU-02 — Contract unit: served contract, golden pin, composition root (layer 2, size M)
 5. ADU-03 — Identity service (layer 3, size M)
 6. ADU-09 — Notifications service (layer 3, size S)
 7. ADU-05 — Scheduling service (layer 3, size M)
 8. ADU-07 — Swaps service (layer 3, size M)
 9. ADU-04 — Identity API (layer 4, size M)
10. ADU-06 — Scheduling API (layer 4, size M)
11. ADU-10 — Notifications API (layer 4, size S)
12. ADU-08 — Swaps API (layer 4, size M)
13. ADU-12 — UI foundation: the Vite scaffold, the shell and the anchor lint (layer 5, size L)
14. ADU-17 — Generated client and sign-in (layer 5, size M)
15. ADU-13 — UI: Team and Week board (layer 5, size M)
16. ADU-14 — UI: Swap request, Swap inbox, Notifications (layer 5, size M)
17. ADU-11 — Operator command: seed the first admin (layer 6, size S)
18. ADU-15 — End-to-end vertical path and packaging (layer 6, size M)
~~~

The order is the one `adu plan order` gives at 7d1e7d4 (the script compares the two: True), with 18 units, ADU-03 at 5, ADU-09 at 6, ADU-05 at 7 and ADU-07 at 8. The recommended options' plan text (B-3, E-6 (b), E-10 (a)) gives the same check and order. So does each of the 144 distinct ADU-PLAN.md texts among the 1,088 rulings (part 4). The pristine export and this one also check the guard (part 5, which also asks about every option's roster). The grants are still needed after the apply; each message is cut at 150 characters by the script:

~~~text
guard edit tests/test_nulls.py --role developer (at 7d1e7d4) -> exit 2: adu guard: refused to edit tests/test_nulls.py: tests/test_nulls.py is a test file of completed unit ADU-16: tests of completed ADUs are immutable (ha
guard edit tests/api/test_contract_conformance.py --role developer (at 7d1e7d4) -> exit 2: adu guard: refused to edit tests/api/test_contract_conformance.py: tests/api/test_contract_conformance.py is a test file of completed unit ADU-02: tes
guard edit src/app/ports.py --role developer (at 7d1e7d4) -> exit 2: adu guard: refused to edit src/app/ports.py: src/app/ports.py is outside ADU-03's roster (files, tests, amends). Stay inside this unit's specified fil
guard edit src/app/db.py --role developer (at 7d1e7d4) -> exit 2: adu guard: refused to edit src/app/db.py: src/app/db.py is outside ADU-03's roster (files, tests, amends). Stay inside this unit's specified files (ha
guard edit src/app/api/deps.py --role developer (at 7d1e7d4) -> exit 2: adu guard: refused to edit src/app/api/deps.py: src/app/api/deps.py is outside ADU-03's roster (files, tests, amends). Stay inside this unit's specifi
guard edit tests/test_nulls.py --role developer (with B-3 applied) -> exit 2: adu guard: refused to edit tests/test_nulls.py: tests/test_nulls.py is a test file of completed unit ADU-16: tests of completed ADUs are immutable (ha
guard edit tests/api/test_contract_conformance.py --role developer (with B-3 applied) -> exit 2: adu guard: refused to edit tests/api/test_contract_conformance.py: tests/api/test_contract_conformance.py is a test file of completed unit ADU-02: tes
guard edit src/app/ports.py --role developer (with B-3 applied) -> exit 0: allow src/app/ports.py
guard edit src/app/db.py --role developer (with B-3 applied) -> exit 2: adu guard: refused to edit src/app/db.py: src/app/db.py is outside ADU-03's roster (files, tests, amends). Stay inside this unit's specified files (ha
guard edit src/app/api/deps.py --role developer (with B-3 applied) -> exit 2: adu guard: refused to edit src/app/api/deps.py: src/app/api/deps.py is outside ADU-03's roster (files, tests, amends). Stay inside this unit's specifi
~~~

### B-4 Criteria
#### B-4.1 Quantitative criteria and pins
None proposed. Every arm this pack rewrites is deterministic. No pin changes: the contract, `contracts/openapi.golden.json` and PINS.lock are untouched, so no golden is regenerated and no twin is owed. With no stochastic arm there is no false-failure rate to state. Under E-10 (c), pyproject.toml is neither pinned (PINS.lock pins design/PRODUCT-BRIEF.md alone) nor protected (adu.toml `[protected]`).

#### B-4.2 Can each rewritten arm fail?
- ADU-03 arm 1 (B-3.5) fails if `create_app()` still binds the Null or anything that does not satisfy `ports.MemberDirectory`; if `src/app/identity/null_directory.py` exists; if any file under src/ or tests/ imports it (as main.py:18, the conformance test :23 and test_nulls.py :11 do at 7d1e7d4); or if either edited test is red in the gate. The rewrite narrows nothing ADU-02's arms require: 401 without a token and with `garbage`, 501 with `tok_1`, an implementation of each protocol bound, the clock, one session per request. Each is still asserted by the unchanged lines.
- ADU-09, ADU-05 and ADU-07 arm 1 (B-3.8, B-3.11, B-3.14) fail the same way for their own Null. ADU-07's also fails if tests/test_nulls.py or any Null module survives.
- Twins, rehearsed (B-4.3): at stage ADU-03 the unedited conformance test fails at collection once the Null is deleted, and with only the import and class-check edits (no injected directory) the 401/501 test fails with 401. Each part of T-03 is therefore needed.
- ADU-03 arm 1 under E-6 (b), with E-6b.10's clause (R1 N-1), also fails in three cases. The composition root's directory may not read the request's session: `require_caller` does not depend on `deps.get_session`, or `get_session` is a sync dependency. Then a request carrying a token `sign_in` issued is not answered 501 not_built. It also fails if an IdentityService method called with no session current does not raise `db.NoCurrentSession`. Rehearsed (B-4.3): a stand-in test of the clause passes with the wiring right and fails under each of the two mutations. With `require_caller` cut off from `get_session`, the full gate is no longer green, where R1 measured 44 passed.
- ADU-03 arm 1 under E-6 (a), with E-6a.9's clause, fails if the directory's own short session does not see the token `sign_in` committed. Not rehearsed: E-6 (a) has no scaffold in this pack.
- E-10: under (a), each arm's file must exist under its new name, and the four collect together; rehearsed with four stand-in files: the gate is green under the new names, and the same four under the planned name fail collection with 3 errors. (b) and (c) were measured on the 7d1e7d4 tree with four stand-in files (B-4.3); (d) changes no path, and ADU-09's collection still fails until its loop rules.

#### B-4.3 The rehearsal (reproducible; scratch only)
The script below, `pack_rehearse.py`, was run with the project's venv interpreter (`C:\dev\team-rota-data\.venv\Scripts\python.exe -I`) as `pack_rehearse.py C:\dev\team-rota docs\PACK-q07-retire-amends.md <scratchpad>\rehearsal\run`, with `ADU_PLUGIN_ROOT` set to `C:\dev\adu-lifecycle` (plugin HEAD c77cbeb). Its run is in eight parts; the numbers are the script's own comments.
1. It parses this pack and checks every B-block against the 7d1e7d4 blob: the text unique in its file, starting at the stated line. Blocks are applied bottom-up, right to left within a line; blocks that share an anchor go in reverse pack order, and a block "on the text E-xx writes" after the others of its file.
2. It checks every E-block against the text as B leaves it, in the narrowest ruling that applies it. First each option alone, its unconditional blocks and those "(without E-2 (b))". Then each conditional block in its context, which prints that block only: E-2 (b) with E-5 (a) and with E-5 (b), E-10 (b) with E-2 (b), and E-3 (b) and E-10 (c) with E-2 (b), whose "without" blocks drop out. Then E-9.P, the pm-lead's text, against PRODUCT-DESIGN.md.
3. It composes every ruling the brackets allow, 1,088 in all. E-1–E-4 and E-10 are ruled always: 2 × 2 × 2 × 2 × 4. E-5 (a) comes with each of the 16 rulings of E-6–E-9, and E-5 (b) with none: 17. For each ruling it checks five things:
   - every block at its line;
   - the DECISIONS rows D-p1 … in id order, last in the file;
   - the Owed rows O-01, O-p1 (and O-p2) in id order;
   - the open and blocking questions as `adu status` would read them: none blocking under E-5 (a), and Q-p1 … Q-p4 under E-5 (b);
   - this loop's open questions: Q-p5 (and Q-p6 under E-10 (d)), and no Q-p1 … Q-p4 left in INTERFACES under E-5 (a).
   It prints the recommended ruling's OPEN-QUESTIONS headings, Owed table and §Domain services as composed.
4. It runs `adu plan check` and `adu plan order` on B-3 alone and on the recommended plan text (B-3, E-6 (b), E-10 (a)), and compares the order with 7d1e7d4's. It then runs `adu plan check` on each distinct ADU-PLAN.md text among the 1,088 rulings.
5. It asks the guard, at 7d1e7d4, with B-3 and with the recommended plan text, about the two completed tests, ports.py, db.py and deps.py, and about the renamed and the old test path. Then it asks about each option's own roster: E-10 (b) and (c), E-1 (b), E-2 (b).
6. It measures E-10's options on the 7d1e7d4 tree, with one stand-in test in each of the four service test files: as planned, (a), (b), and (c) without and with the files. (c) is set as E-10c.2's line says, by `addopts` in pyproject.toml.
7. It runs the four stages in the derived order, on the export with the recommended plan text. Each stage deletes the Null and binds a stand-in "real" service that satisfies the protocol: identity's resolves only a token it issued itself, the worst case for line 70. Each stage also writes a stand-in service test under E-10 (a)'s name, applies its T-blocks (each also unique, at its stated line), then runs the gate and the lint. ADU-03's stage does more:
   - It adds the illustrative `Refused` (the D-p2 shape) to ports.py.
   - It adds E-6 (b)'s illustrative current session to db.py and deps.py. It binds the identity stand-in as E-7 (b) and E-8 (a) construct it, with `caller_for_token`, `seed_admin` and `sign_in` in `db.current_session()`. It then asks the composition root's directory for a token outside and inside a unit of work.
   - It runs v1.1's twins.
   - After T-03, it runs the N-1 twin: the stand-in test of E-6b.10's clause with the wiring right, with `require_caller` cut off from `get_session` (R1's mutation; the full gate too), and with `get_session` a sync dependency.
   After the four stages, it collects the four service test files together, and then runs the E-10 twin: the same four files renamed `test_service.py`.
8. It makes the simulated apply in two exports: the recommended rulings, and E-5 (b). The ids are substituted as D-2 allocates them if main took none, `<apply-date>` is 2026-11-12, and the report is docs/VERIFICATION-R2.md. It then runs `adu ledger lint`, `adu plan check`, `adu derived render`, `adu derived check`, `adu pins check` and `adu status` (B-4.4).

The stand-ins, their tests, the main.py rebinding, the illustrative `Refused` and the illustrative current session are scaffolding for the rehearsal, not proposed text: each session writes its own implementation and its own tests. With `PACK_REHEARSE_QUICK=1` the script stops after part 3 (the text checks only).

The full output of the run:
~~~text
pack: C:\dev\team-rota\docs\PACK-q07-retire-amends.md · 196 replace blocks (B 24, T 24, E 148) · 1 file deletions · snapshot 7d1e7d4
B-2.1     DECISIONS.md:16   occurrences=1 starts-at=16 OK (against the 7d1e7d4 blob)
B-2.5     design/INTERFACES.md:103  occurrences=1 starts-at=103 OK (against the 7d1e7d4 blob)
B-2.4     design/INTERFACES.md:91   occurrences=1 starts-at=91 OK (against the 7d1e7d4 blob)
B-2.3     design/INTERFACES.md:79   occurrences=1 starts-at=79 OK (against the 7d1e7d4 blob)
B-2.2     design/INTERFACES.md:2    occurrences=1 starts-at=2 OK (against the 7d1e7d4 blob)
B-2.7     OPEN-QUESTIONS.md:59   occurrences=1 starts-at=59 OK (against the 7d1e7d4 blob)
B-2.6     OPEN-QUESTIONS.md:53   occurrences=1 starts-at=53 OK (against the 7d1e7d4 blob)
B-2.9     VERSIONS.md:117  occurrences=1 starts-at=117 OK (against the 7d1e7d4 blob)
B-2.8     VERSIONS.md:14   occurrences=1 starts-at=14 OK (against the 7d1e7d4 blob)
B-3.16    ADU-PLAN.md:285  occurrences=1 starts-at=285 OK (against the 7d1e7d4 blob)
B-3.14    ADU-PLAN.md:246  occurrences=1 starts-at=246 OK (against the 7d1e7d4 blob)
B-3.13    ADU-PLAN.md:242  occurrences=1 starts-at=242 OK (against the 7d1e7d4 blob)
B-3.12    ADU-PLAN.md:240  occurrences=1 starts-at=240 OK (against the 7d1e7d4 blob)
B-3.11    ADU-PLAN.md:216  occurrences=1 starts-at=216 OK (against the 7d1e7d4 blob)
B-3.10    ADU-PLAN.md:210  occurrences=1 starts-at=210 OK (against the 7d1e7d4 blob)
B-3.9     ADU-PLAN.md:208  occurrences=1 starts-at=208 OK (against the 7d1e7d4 blob)
B-3.8     ADU-PLAN.md:188  occurrences=1 starts-at=188 OK (against the 7d1e7d4 blob)
B-3.7     ADU-PLAN.md:184  occurrences=1 starts-at=184 OK (against the 7d1e7d4 blob)
B-3.6     ADU-PLAN.md:182  occurrences=1 starts-at=182 OK (against the 7d1e7d4 blob)
B-3.5     ADU-PLAN.md:159  occurrences=1 starts-at=159 OK (against the 7d1e7d4 blob)
B-3.4     ADU-PLAN.md:153  occurrences=1 starts-at=153 OK (against the 7d1e7d4 blob)
B-3.3     ADU-PLAN.md:151  occurrences=1 starts-at=151 OK (against the 7d1e7d4 blob)
B-3.2     ADU-PLAN.md:6    occurrences=1 starts-at=6 OK (against the 7d1e7d4 blob)
B-3.1     ADU-PLAN.md:2    occurrences=1 starts-at=2 OK (against the 7d1e7d4 blob)
E-1b.1    design/INTERFACES.md:126  occurrences=1 starts-at=126 OK (E-1b on post-B)
E-1b.3    ADU-PLAN.md:154  occurrences=1 starts-at=154 OK (E-1b on post-B)
E-1b.2    ADU-PLAN.md:152  occurrences=1 starts-at=152 OK (E-1b on post-B)
E-1b.4    VERSIONS.md:123  occurrences=1 starts-at=123 OK (E-1b on post-B)
E-2b.3    ADU-PLAN.md:155  occurrences=1 starts-at=155 OK (E-2b on post-B)
E-2b.2    ADU-PLAN.md:148  occurrences=1 starts-at=148 OK (E-2b on post-B)
E-2b.1    ADU-PLAN.md:147  occurrences=1 starts-at=147 OK (E-2b on post-B)
E-2b.4    design/ARCHITECTURE.md:12   occurrences=1 starts-at=12 OK (E-2b on post-B)
E-2b.5    design/INTERFACES.md:80   occurrences=1 starts-at=80 OK (E-2b on post-B)
E-2b.7    DECISIONS.md:18   occurrences=1 starts-at=18 OK (E-2b on post-B)
E-2b.6    DECISIONS.md:18   occurrences=1 starts-at=18 OK (E-2b on post-B)
E-2b.8    OPEN-QUESTIONS.md:59   occurrences=1 starts-at=59 OK (E-2b on post-B)
E-2b.9    VERSIONS.md:123  occurrences=1 starts-at=123 OK (E-2b on post-B)
E-3b.2    DECISIONS.md:18   occurrences=1 starts-at=18 OK (E-3b on post-B)
E-3b.1    DECISIONS.md:18   occurrences=1 starts-at=18 OK (E-3b on post-B)
E-3b.6    design/INTERFACES.md:85   occurrences=1 starts-at=85 OK (E-3b on post-B)
E-3b.4    design/INTERFACES.md:85   occurrences=1 starts-at=85 OK (E-3b on post-B)
E-3b.3    design/INTERFACES.md:83   occurrences=1 starts-at=83 OK (E-3b on post-B)
E-3b.5    ADU-PLAN.md:155  occurrences=1 starts-at=155 OK (E-3b on post-B)
E-4b.1    ADU-PLAN.md:152  occurrences=1 starts-at=152 OK (E-4b on post-B)
E-5a.5    OPEN-QUESTIONS.md:82   occurrences=1 starts-at=82 OK (E-5a on post-B)
E-5a.4    OPEN-QUESTIONS.md:75   occurrences=1 starts-at=75 OK (E-5a on post-B)
E-5a.3    OPEN-QUESTIONS.md:68   occurrences=1 starts-at=68 OK (E-5a on post-B)
E-5a.2    OPEN-QUESTIONS.md:61   occurrences=1 starts-at=61 OK (E-5a on post-B)
E-5a.1    OPEN-QUESTIONS.md:59   occurrences=1 starts-at=59 OK (E-5a on post-B)
E-5a.6    design/INTERFACES.md:2    occurrences=1 starts-at=2 OK (E-5a on post-B)
E-5a.9    design/ARCHITECTURE.md:52   occurrences=1 starts-at=52 OK (E-5a on post-B)
E-5a.8    design/ARCHITECTURE.md:2    occurrences=1 starts-at=2 OK (E-5a on post-B)
E-5a.7    design/ARCHITECTURE.md:2    occurrences=1 starts-at=2 OK (E-5a on post-B)
E-5a.13   VERSIONS.md:124  occurrences=1 starts-at=124 OK (E-5a on post-B)
E-5a.12   VERSIONS.md:124  occurrences=1 starts-at=124 OK (E-5a on post-B)
E-5a.11   VERSIONS.md:120  occurrences=1 starts-at=120 OK (E-5a on post-B)
E-5a.10   VERSIONS.md:12   occurrences=1 starts-at=12 OK (E-5a on post-B)
E-5a.14   STATUS.md:31   occurrences=1 starts-at=31 OK (E-5a on post-B)
E-5b.1    STATUS.md:31   occurrences=1 starts-at=31 OK (E-5b on post-B)
E-6a.5    design/INTERFACES.md:112  occurrences=1 starts-at=112 OK (E-6a on post-B)
E-6a.4    design/INTERFACES.md:95   occurrences=1 starts-at=95 OK (E-6a on post-B)
E-6a.3    design/INTERFACES.md:94   occurrences=1 starts-at=94 OK (E-6a on post-B)
E-6a.2    design/INTERFACES.md:93   occurrences=1 starts-at=93 OK (E-6a on post-B)
E-6a.1    design/INTERFACES.md:88   occurrences=1 starts-at=88 OK (E-6a on post-B)
E-6a.6    design/ARCHITECTURE.md:42   occurrences=1 starts-at=42 OK (E-6a on post-B)
E-6a.7    DECISIONS.md:18   occurrences=1 starts-at=18 OK (E-6a on post-B)
E-6a.8    OPEN-QUESTIONS.md:65   occurrences=1 starts-at=65 OK (E-6a on post-B)
E-6a.9    ADU-PLAN.md:161  occurrences=1 starts-at=161 OK (E-6a on post-B)
E-6b.4    design/INTERFACES.md:112  occurrences=1 starts-at=112 OK (E-6b on post-B)
E-6b.3    design/INTERFACES.md:94   occurrences=1 starts-at=94 OK (E-6b on post-B)
E-6b.2    design/INTERFACES.md:93   occurrences=1 starts-at=93 OK (E-6b on post-B)
E-6b.1    design/INTERFACES.md:88   occurrences=1 starts-at=88 OK (E-6b on post-B)
E-6b.5    design/ARCHITECTURE.md:42   occurrences=1 starts-at=42 OK (E-6b on post-B)
E-6b.10   ADU-PLAN.md:161  occurrences=1 starts-at=161 OK (E-6b on post-B)
E-6b.6    ADU-PLAN.md:153  occurrences=1 starts-at=153 OK (E-6b on post-B)
E-6b.7    VERSIONS.md:123  occurrences=1 starts-at=123 OK (E-6b on post-B)
E-6b.8    DECISIONS.md:18   occurrences=1 starts-at=18 OK (E-6b on post-B)
E-6b.9    OPEN-QUESTIONS.md:65   occurrences=1 starts-at=65 OK (E-6b on post-B)
E-7a.5    design/INTERFACES.md:129  occurrences=1 starts-at=129 OK (E-7a on post-B)
E-7a.4    design/INTERFACES.md:117  occurrences=1 starts-at=117 OK (E-7a on post-B)
E-7a.1    design/INTERFACES.md:94   occurrences=1 starts-at=94 OK (E-7a on post-B)
E-7a.2    DECISIONS.md:18   occurrences=1 starts-at=18 OK (E-7a on post-B)
E-7a.3    OPEN-QUESTIONS.md:72   occurrences=1 starts-at=72 OK (E-7a on post-B)
E-7a.6    design/ARCHITECTURE.md:18   occurrences=1 starts-at=18 OK (E-7a on post-B)
E-7b.4    design/INTERFACES.md:129  occurrences=1 starts-at=129 OK (E-7b on post-B)
E-7b.1    design/INTERFACES.md:94   occurrences=1 starts-at=94 OK (E-7b on post-B)
E-7b.2    DECISIONS.md:18   occurrences=1 starts-at=18 OK (E-7b on post-B)
E-7b.3    OPEN-QUESTIONS.md:72   occurrences=1 starts-at=72 OK (E-7b on post-B)
E-7b.5    design/ARCHITECTURE.md:18   occurrences=1 starts-at=18 OK (E-7b on post-B)
E-8a.1    design/INTERFACES.md:94   occurrences=1 starts-at=94 OK (E-8a on post-B)
E-8a.2    design/ARCHITECTURE.md:45   occurrences=1 starts-at=45 OK (E-8a on post-B)
E-8a.3    DECISIONS.md:18   occurrences=1 starts-at=18 OK (E-8a on post-B)
E-8a.4    OPEN-QUESTIONS.md:78   occurrences=1 starts-at=78 OK (E-8a on post-B)
E-8b.1    design/INTERFACES.md:94   occurrences=1 starts-at=94 OK (E-8b on post-B)
E-8b.2    design/ARCHITECTURE.md:45   occurrences=1 starts-at=45 OK (E-8b on post-B)
E-8b.3    DECISIONS.md:18   occurrences=1 starts-at=18 OK (E-8b on post-B)
E-8b.4    OPEN-QUESTIONS.md:78   occurrences=1 starts-at=78 OK (E-8b on post-B)
E-9a.1    design/INTERFACES.md:102  occurrences=1 starts-at=102 OK (E-9a on post-B)
E-9a.2    DECISIONS.md:18   occurrences=1 starts-at=18 OK (E-9a on post-B)
E-9a.3    OPEN-QUESTIONS.md:85   occurrences=1 starts-at=85 OK (E-9a on post-B)
E-9c.1    design/INTERFACES.md:102  occurrences=1 starts-at=102 OK (E-9c on post-B)
E-9c.2    DECISIONS.md:18   occurrences=1 starts-at=18 OK (E-9c on post-B)
E-9c.3    OPEN-QUESTIONS.md:85   occurrences=1 starts-at=85 OK (E-9c on post-B)
E-10a.28  ADU-PLAN.md:259  occurrences=1 starts-at=259 OK (E-10a on post-B)
E-10a.27  ADU-PLAN.md:258  occurrences=1 starts-at=258 OK (E-10a on post-B)
E-10a.26  ADU-PLAN.md:257  occurrences=1 starts-at=257 OK (E-10a on post-B)
E-10a.25  ADU-PLAN.md:253  occurrences=1 starts-at=253 OK (E-10a on post-B)
E-10a.24  ADU-PLAN.md:252  occurrences=1 starts-at=252 OK (E-10a on post-B)
E-10a.23  ADU-PLAN.md:251  occurrences=1 starts-at=251 OK (E-10a on post-B)
E-10a.22  ADU-PLAN.md:242  occurrences=1 starts-at=242 OK (E-10a on post-B)
E-10a.21  ADU-PLAN.md:227  occurrences=1 starts-at=227 OK (E-10a on post-B)
E-10a.20  ADU-PLAN.md:225  occurrences=1 starts-at=225 OK (E-10a on post-B)
E-10a.19  ADU-PLAN.md:224  occurrences=1 starts-at=224 OK (E-10a on post-B)
E-10a.18  ADU-PLAN.md:223  occurrences=1 starts-at=223 OK (E-10a on post-B)
E-10a.17  ADU-PLAN.md:222  occurrences=1 starts-at=222 OK (E-10a on post-B)
E-10a.16  ADU-PLAN.md:221  occurrences=1 starts-at=221 OK (E-10a on post-B)
E-10a.15  ADU-PLAN.md:220  occurrences=1 starts-at=220 OK (E-10a on post-B)
E-10a.14  ADU-PLAN.md:209  occurrences=1 starts-at=209 OK (E-10a on post-B)
E-10a.13  ADU-PLAN.md:194  occurrences=1 starts-at=194 OK (E-10a on post-B)
E-10a.12  ADU-PLAN.md:193  occurrences=1 starts-at=193 OK (E-10a on post-B)
E-10a.11  ADU-PLAN.md:192  occurrences=1 starts-at=192 OK (E-10a on post-B)
E-10a.10  ADU-PLAN.md:191  occurrences=1 starts-at=191 OK (E-10a on post-B)
E-10a.9   ADU-PLAN.md:182  occurrences=1 starts-at=182 OK (E-10a on post-B)
E-10a.8   ADU-PLAN.md:167  occurrences=1 starts-at=167 OK (E-10a on post-B)
E-10a.7   ADU-PLAN.md:166  occurrences=1 starts-at=166 OK (E-10a on post-B)
E-10a.6   ADU-PLAN.md:165  occurrences=1 starts-at=165 OK (E-10a on post-B)
E-10a.5   ADU-PLAN.md:164  occurrences=1 starts-at=164 OK (E-10a on post-B)
E-10a.4   ADU-PLAN.md:163  occurrences=1 starts-at=163 OK (E-10a on post-B)
E-10a.3   ADU-PLAN.md:162  occurrences=1 starts-at=162 OK (E-10a on post-B)
E-10a.2   ADU-PLAN.md:161  occurrences=1 starts-at=161 OK (E-10a on post-B)
E-10a.1   ADU-PLAN.md:149  occurrences=1 starts-at=149 OK (E-10a on post-B)
E-10a.29  DECISIONS.md:18   occurrences=1 starts-at=18 OK (E-10a on post-B)
E-10a.32  OPEN-QUESTIONS.md:100  occurrences=1 starts-at=100 OK (E-10a on post-B)
E-10a.31  OPEN-QUESTIONS.md:96   occurrences=1 starts-at=96 OK (E-10a on post-B)
E-10a.30  OPEN-QUESTIONS.md:59   occurrences=1 starts-at=59 OK (E-10a on post-B)
E-10a.34  VERSIONS.md:123  occurrences=1 starts-at=123 OK (E-10a on post-B)
E-10a.33  VERSIONS.md:120  occurrences=1 starts-at=120 OK (E-10a on post-B)
E-10b.5   ADU-PLAN.md:241  occurrences=1 starts-at=241 OK (E-10b on post-B)
E-10b.4   ADU-PLAN.md:208  occurrences=1 starts-at=208 OK (E-10b on post-B)
E-10b.3   ADU-PLAN.md:181  occurrences=1 starts-at=181 OK (E-10b on post-B)
E-10b.1   ADU-PLAN.md:148  occurrences=1 starts-at=148 OK (E-10b on post-B)
E-10b.6   DECISIONS.md:18   occurrences=1 starts-at=18 OK (E-10b on post-B)
E-10b.9   OPEN-QUESTIONS.md:100  occurrences=1 starts-at=100 OK (E-10b on post-B)
E-10b.8   OPEN-QUESTIONS.md:96   occurrences=1 starts-at=96 OK (E-10b on post-B)
E-10b.7   OPEN-QUESTIONS.md:59   occurrences=1 starts-at=59 OK (E-10b on post-B)
E-10b.11  VERSIONS.md:123  occurrences=1 starts-at=123 OK (E-10b on post-B)
E-10b.10  VERSIONS.md:120  occurrences=1 starts-at=120 OK (E-10b on post-B)
E-10c.2   ADU-PLAN.md:156  occurrences=1 starts-at=156 OK (E-10c on post-B)
E-10c.1   ADU-PLAN.md:147  occurrences=1 starts-at=147 OK (E-10c on post-B)
E-10c.3   DECISIONS.md:18   occurrences=1 starts-at=18 OK (E-10c on post-B)
E-10c.6   OPEN-QUESTIONS.md:100  occurrences=1 starts-at=100 OK (E-10c on post-B)
E-10c.5   OPEN-QUESTIONS.md:96   occurrences=1 starts-at=96 OK (E-10c on post-B)
E-10c.4   OPEN-QUESTIONS.md:59   occurrences=1 starts-at=59 OK (E-10c on post-B)
E-10c.8   VERSIONS.md:123  occurrences=1 starts-at=123 OK (E-10c on post-B)
E-10c.7   VERSIONS.md:120  occurrences=1 starts-at=120 OK (E-10c on post-B)
E-10d.1   STATUS.md:31   occurrences=1 starts-at=31 OK (E-10d on post-B)
E-10d.2   ADU-PLAN.md:197  occurrences=1 starts-at=197 OK (E-10d on post-B)
E-10d.4   OPEN-QUESTIONS.md:100  occurrences=1 starts-at=100 OK (E-10d on post-B)
E-10d.3   OPEN-QUESTIONS.md:59   occurrences=1 starts-at=59 OK (E-10d on post-B)
E-10d.6   VERSIONS.md:123  occurrences=1 starts-at=123 OK (E-10d on post-B)
E-10d.5   VERSIONS.md:120  occurrences=1 starts-at=120 OK (E-10d on post-B)
E-2b.12   design/ARCHITECTURE.md:52   occurrences=1 starts-at=52 OK (E-2b with E-5a)
E-2b.11   design/ARCHITECTURE.md:2    occurrences=1 starts-at=2 OK (E-2b with E-5a)
E-2b.10   VERSIONS.md:125  occurrences=1 starts-at=125 OK (E-2b with E-5a)
E-2b.15   design/ARCHITECTURE.md:52   occurrences=1 starts-at=52 OK (E-2b with E-5b)
E-2b.14   design/ARCHITECTURE.md:2    occurrences=1 starts-at=2 OK (E-2b with E-5b)
E-2b.13   design/ARCHITECTURE.md:2    occurrences=1 starts-at=2 OK (E-2b with E-5b)
E-2b.18   VERSIONS.md:124  occurrences=1 starts-at=124 OK (E-2b with E-5b)
E-2b.17   VERSIONS.md:120  occurrences=1 starts-at=120 OK (E-2b with E-5b)
E-2b.16   VERSIONS.md:12   occurrences=1 starts-at=12 OK (E-2b with E-5b)
E-10b.2   ADU-PLAN.md:148  occurrences=1 starts-at=148 OK (E-10b with E-2b)
(E-3b with E-2b: no conditional E-3b block applies; its other blocks, with E-2b's, all at their lines: True)
(E-10c with E-2b: no conditional E-10c block applies; its other blocks, with E-2b's, all at their lines: True)
E-9.P     design/PRODUCT-DESIGN.md:18   occurrences=1 starts-at=18 OK (E-9.P on post-B: the pm-lead's, not applied)

every ruling the brackets allow (E-1..E-4 and E-10 always; E-6..E-9 all four with E-5 (a), none with (b)):
E-5a with E-10a: 256 rulings, 69–93 E-blocks each; all blocks at their lines, DECISIONS and Owed rows in id order, open and blocking questions as expected: 256/256
E-5a with E-10b: 256 rulings, 45–69 E-blocks each; all blocks at their lines, DECISIONS and Owed rows in id order, open and blocking questions as expected: 256/256
E-5a with E-10c: 256 rulings, 43–66 E-blocks each; all blocks at their lines, DECISIONS and Owed rows in id order, open and blocking questions as expected: 256/256
E-5a with E-10d: 256 rulings, 41–65 E-blocks each; all blocks at their lines, DECISIONS and Owed rows in id order, open and blocking questions as expected: 256/256
E-5b with E-10a:  16 rulings, 35–60 E-blocks each; all blocks at their lines, DECISIONS and Owed rows in id order, open and blocking questions as expected: 16/16
E-5b with E-10b:  16 rulings, 11–36 E-blocks each; all blocks at their lines, DECISIONS and Owed rows in id order, open and blocking questions as expected: 16/16
E-5b with E-10c:  16 rulings, 9–33 E-blocks each; all blocks at their lines, DECISIONS and Owed rows in id order, open and blocking questions as expected: 16/16
E-5b with E-10d:  16 rulings, 7–32 E-blocks each; all blocks at their lines, DECISIONS and Owed rows in id order, open and blocking questions as expected: 16/16
total: 1088 rulings; failures: 0


OPEN-QUESTIONS.md headings with the recommended options (E-1a E-2a E-3a E-4a E-5a E-6b E-7b E-8a E-9a E-10a):
### Q-07 · 2026-11-07 · ADU-03 (hand-over, the D-0 check) · resolved → D-p1
### Q-p1 · 2026-11-08 · design-change loop Q-07 (IdentityService) · resolved → D-p3
### Q-p2 · 2026-11-08 · design-change loop Q-07 (IdentityService) · resolved → D-p4
### Q-p3 · 2026-11-08 · design-change loop Q-07 (IdentityService) · resolved → D-p5
### Q-p4 · 2026-11-08 · design-change loop Q-07 (IdentityService) · resolved → D-p6
### Q-p5 · 2026-11-08 · design-change loop Q-07 (the API units) · open
### Q-p6 · 2026-11-08 · verification R1 (the plan's test paths) · resolved → D-p7
STATUS.md Owed table, its rows cut at 110 characters:
| O | Due | Where | Approval | Status |
| O-01 | ADU-11 | FB-02: the workspace database (`rota.sqlite`, default workspace `.rota`) can never be added 
| O-p1 | ADU-04 | Q-p5: the API units' wall on tests/api/test_contract_conformance.py and the helpers of src/a

design/INTERFACES.md with the recommended options, lines 87–139:
## Domain services (called by the API layer and the operator's command; not ports)
A service is called only from the layers above it — the API, the composition root, the CLI; another domain reaches it only through the ports above (D-05). Every operation a signed-in member performs takes the `Caller` that `deps.py` resolved (R-identity-06, IR-11); every refusal is `Refused(<reason>)`. A point the arms, the domain spec and the contract do not settle is marked open with its question, never filled in.

**The request's session (D-p3).** Every service, and every port implementation `src/app/main.py` binds, reads and writes in the current session, `db.current_session()`, and never opens, commits or closes one. With no session current, `db.current_session()` raises `db.NoCurrentSession`; a service method lets it propagate and never opens a session quietly. Exactly three owners make a session current:
- **A request.** `deps.get_session` is an async generator dependency. It opens the request's one session on `engine_of(request)`, makes it current with `db.use_session(session)` for the whole request, and yields it. On the way out it restores the previous current session and closes this one, which rolls back whatever was not committed. It is async because a ContextVar set in a sync dependency is not visible to the endpoint. `require_caller` depends on it, so `caller_for_token` reads the request's session. The API layer commits a write after the service returns and before it answers, never in the dependency's exit: FastAPI runs that exit after the response is sent, so a failure there would leave a 200 standing. Both behaviours are measured in docs/PACK-q07-retire-amends.md, Part E-6.
- **The operator's command.** `app seed-admin` (ADU-11) builds the app with `create_app(workspace)` and calls `seed_admin` inside `with db.unit_of_work(db.engine_for(app.state.workspace)):`. The block commits when `seed_admin` returns, and the command then prints the id (exit 0). `Refused("team_not_empty")` rolls the block back, and the command prints the reason and exits 2.
- **A test.** A service unit's tests (ADU-03's first) wrap each call in `with db.unit_of_work(db.engine_for(tmp_path)):` and read back in a second unit of work. A refusal is asserted with `pytest.raises(Refused)` around the block, which leaves it rolled back. No test sets the ContextVar itself; a test calls a service outside a unit of work only to assert `db.NoCurrentSession`.
```
# src/app/db.py gains (ADU-03, by amendment of ADU-01's module; layer 1, so every service, the API and the CLI reach it):
class NoCurrentSession(RuntimeError)
def current_session() -> Session                               # the current session; raises NoCurrentSession when none is
def use_session(session: Session) -> ContextManager[Session]    # current for the block, the previous one restored on exit; commits nothing
def unit_of_work(engine: Engine) -> ContextManager[Session]     # session_for(engine) made current; commits on return, rolls back on raise, closes
```
Invariants: one ContextVar, private to `src/app/db.py`. `use_session` restores the previous session with the token it set, so nested blocks and concurrent requests stay apart. `engine_for` and `session_for` do not change. The transfer (ADU-05) and the Notifier (ADU-09) write in the same current session, so a decision, its transfer and its notifications commit together (R-swaps-04).

### IdentityService (identity → the identity API, the seed command)
Provider: ADU-03 (`src/app/identity/service.py`, persistence in `src/app/identity/repo.py`). Consumers: ADU-04 (the five identity operations), ADU-11 (`app seed-admin`), and ADU-07's §6 arm through the composition root. The same object implements MemberDirectory and is bound as it in `src/app/main.py` (ADU-03 arm 1).
```
class IdentityService:                          # implements MemberDirectory (above), and the operations below — every method in db.current_session() (D-p3):
    def __init__(
        self,
        bound: Callable[[], Bindings],          # the composition root's bindings, read at call time (D-p4): .clock (Clock),
                                                #   .scheduling (SchedulingPort, IR-05), .notifier (Notifier, IR-10); Bindings is a Protocol of those
                                                #   three in src/app/identity/service.py, which main.Ports satisfies, so identity never imports main;
                                                #   main.py binds IdentityService(lambda: app.state.ports, …); a test passes
                                                #   lambda: SimpleNamespace(clock=FixedClock(…), scheduling=FakeSchedulingPort(), notifier=SpyNotifier())
        source: TokenSource,                    # the token and the salt (D-p5): TokenSource is a Protocol in src/app/identity/service.py,
                                                #   token() -> str and salt() -> str; the product's SecretsSource (same module) answers
                                                #   secrets.token_urlsafe(32) and secrets.token_hex(8); main.py passes SecretsSource(), a test a
                                                #   deterministic source; seed_admin and add_member store models.hash_passcode(passcode, source.salt());
                                                #   sign_in stores source.token() as the member's one token and checks a passcode by recomputing
                                                #   models.hash_passcode with the stored salt (the text before '$'), compared with hmac.compare_digest
    ) -> None
    def seed_admin(self, name: str, email: str, passcode: str) -> int
    def add_member(self, caller: Caller, name: str, email: str, role: str | None, passcode: str) -> MemberValue
    def change_role(self, caller: Caller, member_id: int, role: str | None) -> MemberValue
    def deactivate(self, caller: Caller, member_id: int) -> MemberValue
    def sign_in(self, email: str, passcode: str | None) -> SignInValue
    def list_members(self, caller: Caller) -> list[MemberSummary]
# MemberValue: the contract's Member fields (id, name, email, role, active); SignInValue: the token and a MemberValue (the contract's Token);
# MemberSummary: id, name, role, active (ADU-03 arm 7). All three are frozen dataclasses (`@dataclass(frozen=True)`) defined in src/app/identity/service.py beside the service; no other domain consumes them in process (D-05), and the API layer maps them onto the contract's Member, Token and MemberSummary (D-p6).
```
| Operation | Rule (source) | Emits | Refused with, by bucket (R-identity-08: forbidden → not_found → state → validation) |
|---|---|---|---|
| seed_admin | an empty team gets one active admin; the passcode stored as a salted SHA-256; answers the new id; no caller — an operator command outside the API (R-identity-07; ADU-03 arm 2) | nothing | state: team_not_empty |
| add_member | an active member with the role; the email unique, compared case-insensitively; a role that is missing or not admin, planner or member is invalid_role (R-identity-01, -02; the contract's MemberCreate.role is optional and "checked by identity") | MemberAdded(member_id, role) | forbidden (the caller is not an admin) · state: duplicate_email · validation: invalid_role |
| change_role | the same role is a no-op that answers the unchanged member and emits nothing; an inactive member's role may change and nobody is notified; the team keeps an active admin (R-identity-01, -03) | RoleChanged(member_id, role), except for the no-op and an inactive member | forbidden · not_found · state: last_admin · validation: invalid_role |
| deactivate | active false, the row kept; refused while `scheduling.has_assignment_after(member_id, clock.now())` (R-identity-03, -04, -05) | MemberDeactivated(member_id) | forbidden · not_found · state: future_assignments, last_admin, member_inactive (a repeat; nothing emitted) — their order within the bucket is US-identity-003's (PRODUCT-DESIGN, cross-cutting rules) |
| sign_in | the email matched case-insensitively and the passcode verified before the active check; a missing passcode counts as wrong; the new token replaces the member's earlier one; no caller (R-identity-06; the contract's 401 for identity.sign_in) | nothing | unauthenticated bucket: invalid_credentials (wrong or missing passcode, unknown email) · forbidden bucket: member_inactive (only after a correct passcode) |
| list_members | every member, active and inactive, as MemberSummary — never email, passcode or token — by name compared case-insensitively, then id (R-identity-09) | nothing | none: any signed-in caller |
| MemberDirectory | the six methods above over identity's own rows, read in the current session (with none current, each raises db.NoCurrentSession; D-p3): caller_for_token is None for an unknown token and for an inactive member's (IR-11); is_active is None for an unknown id; role_of and name_of raise MemberNotFound; active_member_ids (IR-12); decider_ids the active admins and planners | — | none: no caller |

$ adu plan check   # scratch copy with B-3 applied, exit 0
plan OK: 18 units, order ADU-00 → ADU-01 → ADU-16 → ADU-02 → ADU-03 → ADU-09 → ADU-05 → ADU-07 → ADU-04 → ADU-06 → ADU-10 → ADU-08 → ADU-12 → ADU-17 → ADU-13 → ADU-14 → ADU-11 → ADU-15

$ adu plan order   # scratch copy with B-3 applied, exit 0
 1. ADU-00 — Scaffold and method guard (layer 0, size M)
 2. ADU-01 — Data model and the seeded fixture (layer 1, size M)
 3. ADU-16 — Ports, Null implementations and test doubles (layer 2, size M)
 4. ADU-02 — Contract unit: served contract, golden pin, composition root (layer 2, size M)
 5. ADU-03 — Identity service (layer 3, size M)
 6. ADU-09 — Notifications service (layer 3, size S)
 7. ADU-05 — Scheduling service (layer 3, size M)
 8. ADU-07 — Swaps service (layer 3, size M)
 9. ADU-04 — Identity API (layer 4, size M)
10. ADU-06 — Scheduling API (layer 4, size M)
11. ADU-10 — Notifications API (layer 4, size S)
12. ADU-08 — Swaps API (layer 4, size M)
13. ADU-12 — UI foundation: the Vite scaffold, the shell and the anchor lint (layer 5, size L)
14. ADU-17 — Generated client and sign-in (layer 5, size M)
15. ADU-13 — UI: Team and Week board (layer 5, size M)
16. ADU-14 — UI: Swap request, Swap inbox, Notifications (layer 5, size M)
17. ADU-11 — Operator command: seed the first admin (layer 6, size S)
18. ADU-15 — End-to-end vertical path and packaging (layer 6, size M)
(adu plan order as at 7d1e7d4: True)

$ adu plan check   # scratch copy with the recommended options' plan text: B-3, E-6 (b), E-10 (a), exit 0
plan OK: 18 units, order ADU-00 → ADU-01 → ADU-16 → ADU-02 → ADU-03 → ADU-09 → ADU-05 → ADU-07 → ADU-04 → ADU-06 → ADU-10 → ADU-08 → ADU-12 → ADU-17 → ADU-13 → ADU-14 → ADU-11 → ADU-15

$ adu plan order   # scratch copy with the recommended options' plan text: B-3, E-6 (b), E-10 (a), exit 0
 1. ADU-00 — Scaffold and method guard (layer 0, size M)
 2. ADU-01 — Data model and the seeded fixture (layer 1, size M)
 3. ADU-16 — Ports, Null implementations and test doubles (layer 2, size M)
 4. ADU-02 — Contract unit: served contract, golden pin, composition root (layer 2, size M)
 5. ADU-03 — Identity service (layer 3, size M)
 6. ADU-09 — Notifications service (layer 3, size S)
 7. ADU-05 — Scheduling service (layer 3, size M)
 8. ADU-07 — Swaps service (layer 3, size M)
 9. ADU-04 — Identity API (layer 4, size M)
10. ADU-06 — Scheduling API (layer 4, size M)
11. ADU-10 — Notifications API (layer 4, size S)
12. ADU-08 — Swaps API (layer 4, size M)
13. ADU-12 — UI foundation: the Vite scaffold, the shell and the anchor lint (layer 5, size L)
14. ADU-17 — Generated client and sign-in (layer 5, size M)
15. ADU-13 — UI: Team and Week board (layer 5, size M)
16. ADU-14 — UI: Swap request, Swap inbox, Notifications (layer 5, size M)
17. ADU-11 — Operator command: seed the first admin (layer 6, size S)
18. ADU-15 — End-to-end vertical path and packaging (layer 6, size M)
(adu plan order as at 7d1e7d4: True)

144 distinct ADU-PLAN.md texts among the 1088 rulings; adu plan check exit codes [0]; distinct outputs 1:
  [144 texts] plan OK: 18 units, order ADU-00 → ADU-01 → ADU-16 → ADU-02 → ADU-03 → ADU-09 → ADU-05 → ADU-07 → ADU-04 → ADU-06 → ADU-10 → ADU-08 → ADU-12 → ADU-17 → ADU-13 → ADU-14 → ADU-11 → ADU-15

guard edit tests/test_nulls.py --role developer (at 7d1e7d4) -> exit 2: adu guard: refused to edit tests/test_nulls.py: tests/test_nulls.py is a test file of completed unit ADU-16: tests of completed ADUs are immutable (ha
guard edit tests/api/test_contract_conformance.py --role developer (at 7d1e7d4) -> exit 2: adu guard: refused to edit tests/api/test_contract_conformance.py: tests/api/test_contract_conformance.py is a test file of completed unit ADU-02: tes
guard edit src/app/ports.py --role developer (at 7d1e7d4) -> exit 2: adu guard: refused to edit src/app/ports.py: src/app/ports.py is outside ADU-03's roster (files, tests, amends). Stay inside this unit's specified fil
guard edit src/app/db.py --role developer (at 7d1e7d4) -> exit 2: adu guard: refused to edit src/app/db.py: src/app/db.py is outside ADU-03's roster (files, tests, amends). Stay inside this unit's specified files (ha
guard edit src/app/api/deps.py --role developer (at 7d1e7d4) -> exit 2: adu guard: refused to edit src/app/api/deps.py: src/app/api/deps.py is outside ADU-03's roster (files, tests, amends). Stay inside this unit's specifi
guard edit tests/test_nulls.py --role developer (with B-3 applied) -> exit 2: adu guard: refused to edit tests/test_nulls.py: tests/test_nulls.py is a test file of completed unit ADU-16: tests of completed ADUs are immutable (ha
guard edit tests/api/test_contract_conformance.py --role developer (with B-3 applied) -> exit 2: adu guard: refused to edit tests/api/test_contract_conformance.py: tests/api/test_contract_conformance.py is a test file of completed unit ADU-02: tes
guard edit src/app/ports.py --role developer (with B-3 applied) -> exit 0: allow src/app/ports.py
guard edit src/app/db.py --role developer (with B-3 applied) -> exit 2: adu guard: refused to edit src/app/db.py: src/app/db.py is outside ADU-03's roster (files, tests, amends). Stay inside this unit's specified files (ha
guard edit src/app/api/deps.py --role developer (with B-3 applied) -> exit 2: adu guard: refused to edit src/app/api/deps.py: src/app/api/deps.py is outside ADU-03's roster (files, tests, amends). Stay inside this unit's specifi
guard edit tests/test_nulls.py --role developer (recommended: B-3, E-6 (b), E-10 (a)) -> exit 2: adu guard: refused to edit tests/test_nulls.py: tests/test_nulls.py is a test file of completed unit ADU-16: tests of completed ADUs are immutable (ha
guard edit tests/api/test_contract_conformance.py --role developer (recommended: B-3, E-6 (b), E-10 (a)) -> exit 2: adu guard: refused to edit tests/api/test_contract_conformance.py: tests/api/test_contract_conformance.py is a test file of completed unit ADU-02: tes
guard edit src/app/ports.py --role developer (recommended: B-3, E-6 (b), E-10 (a)) -> exit 0: allow src/app/ports.py
guard edit src/app/db.py --role developer (recommended: B-3, E-6 (b), E-10 (a)) -> exit 0: allow src/app/db.py
guard edit src/app/api/deps.py --role developer (recommended: B-3, E-6 (b), E-10 (a)) -> exit 0: allow src/app/api/deps.py
guard edit tests/identity/test_identity_service.py --role developer (recommended: B-3, E-6 (b), E-10 (a)) -> exit 0: allow tests/identity/test_identity_service.py
guard edit tests/identity/test_service.py --role developer (recommended: B-3, E-6 (b), E-10 (a)) -> exit 2: adu guard: refused to edit tests/identity/test_service.py: tests/identity/test_service.py is outside ADU-03's roster (files, tests, amends). Stay insi
guard edit tests/identity/__init__.py --role developer (with E-10 (b), else as recommended) -> exit 0: allow tests/identity/__init__.py
guard edit pyproject.toml --role developer (with E-10 (c), else as recommended) -> exit 0: allow pyproject.toml
guard edit tests/support/doubles.py --role developer (with E-1 (b), else as recommended) -> exit 0: allow tests/support/doubles.py
guard edit src/app/refusals.py --role developer (with E-2 (b), else as recommended) -> exit 0: allow src/app/refusals.py
guard edit tests/layering.json --role developer (with E-2 (b), else as recommended) -> exit 0: allow tests/layering.json
guard edit src/app/ports.py --role developer (with E-2 (b), else as recommended) -> exit 2: adu guard: refused to edit src/app/ports.py: src/app/ports.py is outside ADU-03's roster (files, tests, amends). Stay inside this unit's specified fil

E-10, measured on the 7d1e7d4 tree with one stand-in test per service test file:
as planned: four tests/<domain>/test_service.py: exit 2: 1 warning, 3 errors in 1.21s | import file mismatch:
(a) tests/<domain>/test_<domain>_service.py: exit 0: 50 passed, 1 warning in 22.98s
(b) tests/<domain>/__init__.py beside test_service.py: exit 0: 50 passed, 1 warning in 22.77s
(c) addopts in pyproject.toml, no service test file yet: exit 0: 46 passed, 1 warning in 22.99s
(c) addopts in pyproject.toml, four test_service.py: exit 0: 50 passed, 1 warning in 23.22s

baseline (export A, the recommended plan text, no stage yet): gate exit 0: 46 passed, 1 warning in 22.92s · lint exit 0: All checks passed!
E-6 (b) scaffold, the composition root's directory: exit 0: outside a unit of work -> NoCurrentSession; inside db.unit_of_work -> None
twin 1 (Null deleted, conformance test unedited): exit 2: E   ModuleNotFoundError: No module named 'app.identity.null_directory' | 1 warning, 1 error in 1.12s
twin 2 (import and class check edited, no injected directory): exit 1: test_contract_conformance.py:70: AssertionError: ('identity.list_members', '{"type":"about:blank","title":"Not signed in","detail":"Sign in first.","reason":"unauthentica | 1 failed, 5 passed, 1 warning in 1.54s
T-03.6    tests/api/test_contract_conformance.py:105  occurrences=1 starts-at=105 OK (stage T-03)
T-03.5    tests/api/test_contract_conformance.py:102  occurrences=1 starts-at=102 OK (stage T-03)
T-03.4    tests/api/test_contract_conformance.py:61   occurrences=1 starts-at=61 OK (stage T-03)
T-03.3    tests/api/test_contract_conformance.py:23   occurrences=1 starts-at=23 OK (stage T-03)
T-03.2    tests/api/test_contract_conformance.py:19   occurrences=1 starts-at=19 OK (stage T-03)
T-03.1    tests/api/test_contract_conformance.py:1    occurrences=1 starts-at=1 OK (stage T-03)
T-03.10   tests/test_nulls.py:36   occurrences=1 starts-at=36 OK (stage T-03)
T-03.9    tests/test_nulls.py:28   occurrences=1 starts-at=28 OK (stage T-03)
T-03.8    tests/test_nulls.py:17   occurrences=1 starts-at=17 OK (stage T-03)
T-03.7    tests/test_nulls.py:11   occurrences=1 starts-at=11 OK (stage T-03)
N-1 twin, wiring right: tests/identity/test_identity_service.py: exit 0: 2 passed, 1 warning in 1.19s
N-1 twin, require_caller without Depends(get_session): tests/identity/test_identity_service.py: exit 1: 1 failed, 1 passed, 1 warning in 1.16s | c15c40e1022d\scratchpad\rehearsal\run\A-plan-and-stages\src\app\db.py:47: app.db.NoCurrentSession: no session is current
  the full gate with that wiring (R1 measured 44 passed and HTTP 500): gate exit 1: 1 failed, 45 passed, 1 warning in 22.91s · lint exit 0: All checks passed!
N-1 twin, get_session a sync generator dependency: tests/identity/test_identity_service.py: exit 1: 1 failed, 1 passed, 1 warning in 1.11s | e='app.db.current_session' default=None at 0x0000019343503C90> at 0x0000019345CD8940> was created in a different Context
after stage T-03: gate exit 0: 46 passed, 1 warning in 22.64s · lint exit 0: All checks passed! (of which 2 in the stand-in service tests)
T-09.2    tests/api/test_contract_conformance.py:110  occurrences=1 starts-at=110 OK (stage T-09)
T-09.1    tests/api/test_contract_conformance.py:24   occurrences=1 starts-at=24 OK (stage T-09)
T-09.6    tests/test_nulls.py:48   occurrences=1 starts-at=48 OK (stage T-09)
T-09.5    tests/test_nulls.py:28   occurrences=1 starts-at=28 OK (stage T-09)
T-09.4    tests/test_nulls.py:18   occurrences=1 starts-at=18 OK (stage T-09)
T-09.3    tests/test_nulls.py:11   occurrences=1 starts-at=11 OK (stage T-09)
after stage T-09: gate exit 0: 45 passed, 1 warning in 24.71s · lint exit 0: All checks passed! (of which 3 in the stand-in service tests)
T-05.2    tests/api/test_contract_conformance.py:108  occurrences=1 starts-at=108 OK (stage T-05)
T-05.1    tests/api/test_contract_conformance.py:24   occurrences=1 starts-at=24 OK (stage T-05)
T-05.6    tests/test_nulls.py:30   occurrences=1 starts-at=30 OK (stage T-05)
T-05.5    tests/test_nulls.py:24   occurrences=1 starts-at=24 OK (stage T-05)
T-05.4    tests/test_nulls.py:15   occurrences=1 starts-at=15 OK (stage T-05)
T-05.3    tests/test_nulls.py:11   occurrences=1 starts-at=11 OK (stage T-05)
after stage T-05: gate exit 0: 44 passed, 1 warning in 25.65s · lint exit 0: All checks passed! (of which 4 in the stand-in service tests)
T-07.2    tests/api/test_contract_conformance.py:108  occurrences=1 starts-at=108 OK (stage T-07)
T-07.1    tests/api/test_contract_conformance.py:24   occurrences=1 starts-at=24 OK (stage T-07)
T-07.3    tests/test_nulls.py deleted
after stage T-07: gate exit 0: 43 passed, 1 warning in 24.56s · lint exit 0: All checks passed! (of which 5 in the stand-in service tests)
after all four: Null modules left: none; tests/test_nulls.py exists: False; imports of a Null module under src/ and tests/: none
the four service test files under E-10 (a)'s names, collected together: 5 tests collected in 0.94s
E-10 twin, the same four files renamed tests/<domain>/test_service.py: gate exit 2: 1 warning, 3 errors in 1.26s · lint exit 0: All checks passed!

simulated apply, recommended: 94 blocks into 7 files; ids substituted: D-p1→D-12, D-p2→D-13, D-p3→D-14, D-p4→D-15, D-p5→D-16, D-p6→D-17, D-p7→D-18, O-p1→O-02, Q-p1→Q-08, Q-p2→Q-09, Q-p3→Q-10, Q-p4→Q-11, Q-p5→Q-12, Q-p6→Q-13; provisional ids left: none
$ adu ledger lint -> exit 0: ledgers OK
$ adu plan check -> exit 0: plan OK: 18 units, order ADU-00 → ADU-01 → ADU-16 → ADU-02 → ADU-03 → ADU-09 → ADU-05 → ADU-07 → ADU-04 → ADU-06 → ADU-10 → ADU-08 → ADU-12 → ADU-17 →
$ adu derived render -> exit 0: derived blocks rendered (0 file(s) rewritten)
$ adu derived check -> exit 0: derived blocks OK
$ adu pins check -> exit 0: pins OK (1 pinned)
$ adu status
ADU status — Team Rota · 2026-11-12 10:38
Now: ADU-03 — Identity service · size M · layer 3 (domain services) · position 5/18 in the derived order
Depends: ADU-01 ✅, ADU-02 ✅, ADU-16 ✅
Consumes through mocks: MK-01 (SchedulingPort ← ADU-05, in-process), MK-02 (Notifier ← ADU-09, in-process)
Ledger row: planned
Last journal block: 2026-11-07 20:20 · hand-over ADU-03 (oversight) · blocked
NEXT (from the journal): `/adu-lifecycle:change-design Q-07` (stage 1, the pack) in a fresh `claude --plugin-dir C:\dev\adu-lifecycle --agent adu-lifecycle:architect` started inside `C:\dev\team-rota`; ADU-03 opens only after the apply step resolves Q-07.
Open blocking questions: none
Open non-blocking questions: Q-02, Q-03, Q-05, Q-12
Owed items: O-01 due ADU-11 (FB-02: the workspace database (`rota.sqlite`, default workspace `.rota`) can never be added to git before real data is seeded; `.gitignore` is in no roster, so editing it needs a grant); O-02 due ADU-04 (Q-12: the API units' wall on tests/api/test_contract_conformance.py and the helpers of src/app/api/contract_stubs.py is ruled in a design-change loop before ADU-04 opens (ADU-PLAN.md, ADU-04's pointer); Q-12 is entered non-blocking because `adu status` reads `**Blocking:** yes` as a stop for every unit, not ADU-04 alone (plugin FB-32))
Last gate run: 46 passed in 28.77s (STATUS.md:41)
Plan check: OK
Commands (from adu.toml):
  gate:   uv run pytest tests/ -q -m "not timing"
  fast:   uv run pytest tests/ -q -m "not calibration"
  timing: uv run pytest tests/ -q -m timing
  lint:   uv run ruff check

simulated apply, E-5 (b), else as recommended: 59 blocks into 6 files; ids substituted: D-p1→D-12, D-p2→D-13, D-p7→D-14, O-p1→O-02, Q-p1→Q-08, Q-p2→Q-09, Q-p3→Q-10, Q-p4→Q-11, Q-p5→Q-12, Q-p6→Q-13; provisional ids left: none
$ adu ledger lint -> exit 0: ledgers OK
$ adu plan check -> exit 0: plan OK: 18 units, order ADU-00 → ADU-01 → ADU-16 → ADU-02 → ADU-03 → ADU-09 → ADU-05 → ADU-07 → ADU-04 → ADU-06 → ADU-10 → ADU-08 → ADU-12 → ADU-17 →
$ adu derived render -> exit 0: derived blocks rendered (0 file(s) rewritten)
$ adu derived check -> exit 0: derived blocks OK
$ adu pins check -> exit 0: pins OK (1 pinned)
$ adu status
Now: ADU-03 — Identity service · size M · layer 3 (domain services) · position 5/18 in the derived order
Open blocking questions: Q-08 (design-change loop Q-07 (IdentityService)), Q-09 (design-change loop Q-07 (IdentityService)), Q-10 (design-change loop Q-07 (IdentityService)), Q-11 (design-change loop Q-07 (IdentityService)) — STOP: a blocking question means stop, not proceed-and-guess
Open non-blocking questions: Q-02, Q-03, Q-05, Q-12
Owed items: O-01 due ADU-11 (FB-02: the workspace database (`rota.sqlite`, default workspace `.rota`) can never be added to git before real data is seeded; `.gitignore` is in no roster, so editing it needs a grant); O-02 due ADU-04 (Q-12: the API units' wall on tests/api/test_contract_conformance.py and the helpers of src/app/api/contract_stubs.py is ruled in a design-change loop before ADU-04 opens (ADU-PLAN.md, ADU-04's pointer); Q-12 is entered non-blocking because `adu status` reads `**Blocking:** yes` as a stop for every unit, not ADU-04 alone (plugin FB-32))

all blocks matched: True
~~~

The script (`pack_rehearse.py`):
~~~python
"""Re-runs the mechanical claims of docs/PACK-q07-retire-amends.md (v1.2) on scratch exports of its snapshot.

Never writes to the repository: blobs are read with `git show`, trees exported with `git archive`, and every
write lands under <scratch>. Run with the project's venv interpreter, isolated:
    python -I pack_rehearse.py <repo> <pack.md> <scratch> [<plugin-root>]
"""

from __future__ import annotations

import hashlib
import io
import itertools
import os
import re
import shutil
import subprocess
import sys
import tarfile
from pathlib import Path

SNAP = "7d1e7d4"
REPO, PACK, SCRATCH = (Path(a) for a in sys.argv[1:4])
PLUGIN = Path(sys.argv[4]) if len(sys.argv) > 4 else Path(r"C:\dev\adu-lifecycle")
PY = Path(sys.executable)
RUFF = PY.with_name("ruff.exe") if PY.with_name("ruff.exe").exists() else PY.with_name("ruff")
ENV = {k: v for k, v in os.environ.items() if k != "PYTHONUTF8"}

BLOCK = re.compile(
    r"^#### (?P<id>[BTE]-[\w.]+) · (?P<file>[^\s:]+):(?P<line>\d+)(?P<rest>[^\n]*)\n"
    r"(?:(?!#### |replace exactly)[^\n]*\n)*"
    r"replace exactly(?P<inline> \(within the line\))?:\n~~~text\n(?P<old>[\s\S]*?)~~~\n"
    r"with:\n~~~text\n(?P<new>[\s\S]*?)~~~\n",
    re.M,
)
DELETE = re.compile(r"^#### (?P<id>T-[\w.]+) · (?P<file>\S+) — delete the file$", re.M)
COND = re.compile(r"\b(with|without) E-(\d+) \(([a-d])\)")  # "(with E-5 (a))", "(without E-2 (b))" in a heading
OPT = re.compile(r"^E-(\d+)([a-d])\.\d+$")


def blocks(text: str) -> list[dict]:
    out = []
    for i, m in enumerate(BLOCK.finditer(text)):
        old, new = m["old"], m["new"]
        if m["inline"]:
            old, new = old[:-1], (new[:-1] if new.endswith("\n") else new)
        o = OPT.match(m["id"])
        out.append({"id": m["id"], "file": m["file"], "line": int(m["line"]), "old": old, "new": new,
                    "inline": bool(m["inline"]), "idx": i, "opt": (int(o[1]), o[2]) if o else None,
                    "conds": [(w == "with", int(n), x) for w, n, x in COND.findall(m["rest"])],
                    "layered": "on the text" in m["rest"]})
    return out


def locate(text: str, b: dict) -> tuple[int, int | None]:
    n = text.count(b["old"])
    if n != 1:
        return n, None
    pos = text.find(b["old"])
    if not b["inline"] and pos and text[pos - 1] != "\n":
        return n, -1  # matched mid-line
    return n, text.count("\n", 0, pos) + 1


def apply_group(texts: dict[str, str], group: list[dict], label: str, report: list[str] | None,
                show: set[str] | None = None) -> bool:
    ok = True
    by_file: dict[str, list[dict]] = {}
    for b in group:
        by_file.setdefault(b["file"], []).append(b)
    for f, bs in by_file.items():
        text = texts[f]
        # bottom-up, right to left within a line; blocks sharing an anchor in reverse pack order; a block "on
        # the text E-xx writes" after the others of its file
        for b in sorted(bs, key=lambda x: (not x["layered"], text.find(x["old"]), x["idx"]), reverse=True):
            n, line = locate(text, b)
            good = n == 1 and line == b["line"]
            ok &= good
            if report is not None and (show is None or b["id"] in show):
                report.append(f"{b['id']:9} {f}:{b['line']:<4} occurrences={n} starts-at={line} "
                              f"{'OK' if good else 'MISMATCH'} ({label})")
            if good:
                text = text.replace(b["old"], b["new"], 1)
        texts[f] = text
    return ok


def git_show(path: str) -> str:
    return subprocess.run(["git", "-C", str(REPO), "show", f"{SNAP}:{path}"], capture_output=True, check=True,
                          encoding="utf-8").stdout.replace("\r\n", "\n")


def export(name: str) -> Path:
    dest = SCRATCH / name
    shutil.rmtree(dest, ignore_errors=True)
    dest.mkdir(parents=True)
    data = subprocess.run(["git", "-C", str(REPO), "archive", SNAP], capture_output=True, check=True).stdout
    with tarfile.open(fileobj=io.BytesIO(data)) as tar:
        tar.extractall(dest, filter="data")
    return dest


def read(tree: Path, rel: str) -> str:
    return (tree / rel).read_text(encoding="utf-8").replace("\r\n", "\n")


def write(tree: Path, rel: str, text: str) -> None:
    (tree / rel).parent.mkdir(parents=True, exist_ok=True)
    (tree / rel).write_text(text, encoding="utf-8", newline="\n")


def run(cmd: list[str], cwd: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(cmd, cwd=cwd, capture_output=True, encoding="utf-8", errors="replace", env=ENV)


def adu(tree: Path, *args: str) -> subprocess.CompletedProcess[str]:
    return run(["node", str(PLUGIN / "scripts" / "adu.mjs"), *args], tree)


def last(text: str, pattern: str) -> str:
    hits = [ln for ln in text.splitlines() if re.search(pattern, ln)]
    return hits[-1].strip() if hits else "(no line matching " + pattern + ")"


def first(text: str, pattern: str) -> str:
    hits = [ln for ln in text.splitlines() if re.search(pattern, ln)]
    return hits[0].strip() if hits else "(no line matching " + pattern + ")"


def pytest(tree: Path, *args: str) -> subprocess.CompletedProcess[str]:
    return run([str(PY), "-m", "pytest", *args, "-q", "-p", "no:cacheprovider"], tree)


def gate(tree: Path) -> str:
    r = pytest(tree, "tests/", "-m", "not timing")
    lint = run([str(RUFF), "check"], tree)
    return f"gate exit {r.returncode}: {last(r.stdout, r'passed|failed|error')} · lint exit {lint.returncode}: " \
           f"{last(lint.stdout + lint.stderr, r'.')}"


# ---- the rulings the brackets allow: E-1..E-4 and E-10 always; E-6..E-9 all four with E-5 (a), none with (b)
def rulings():
    for r1, r2, r3, r4, r10 in itertools.product("ab", "ab", "ab", "ab", "abcd"):
        base = {1: r1, 2: r2, 3: r3, 4: r4, 10: r10}
        for o6, o7, o8, o9 in itertools.product("ab", "ab", "ab", "ac"):
            yield {**base, 5: "a", 6: o6, 7: o7, 8: o8, 9: o9}
        yield {**base, 5: "b"}


def code(r: dict) -> str:
    return " ".join(f"E-{n}{r[n]}" for n in sorted(r))


def selected(allb: list[dict], ruling: dict) -> list[dict]:
    out = []
    for b in allb:
        if b["opt"] is None:
            continue
        n, o = b["opt"]
        if ruling.get(n) == o and all((ruling.get(cn) == co) == want for want, cn, co in b["conds"]):
            out.append(b)
    return out


def questions(text: str) -> dict[str, tuple[bool, bool | None]]:
    """As plugin scripts/lib/ledgers.mjs reads them: (open, blocking) per heading, provisional ids included."""
    heads = [(m.start(), m[1], m[2]) for m in re.finditer(r"^### (Q-(?:\d+|p\d+))\s*·[^·]+·[^·]+·\s*(.+)$", text, re.M)]
    out = {}
    for k, (pos, qid, state) in enumerate(heads):
        body = text[pos: heads[k + 1][0] if k + 1 < len(heads) else len(text)]
        b = re.search(r"\*\*Blocking:\*\*\s*(yes|no)", body, re.I)
        out[qid] = (state.lower().startswith("open"), (b[1].lower() == "yes") if b else None)
    return out


# ---- scaffolding for the rehearsal only: stand-ins for the real services and their tests, never proposed text
STAND_INS = {
    "src/app/identity/service.py": '''"""Rehearsal stand-in (scratch only, not the product): a MemberDirectory over the current session (E-6 (b)),
built as E-7 (b) and E-8 (a) construct it, with just enough seed_admin and sign_in for E-6b.10's clause."""

from __future__ import annotations

import secrets
from collections.abc import Callable
from dataclasses import dataclass
from typing import Any

from sqlalchemy import func, select

from app import db, models
from app.ports import Caller, MemberNotFound, Refused, Role


class SecretsSource:
    def token(self) -> str:
        return secrets.token_urlsafe(32)

    def salt(self) -> str:
        return secrets.token_hex(8)


@dataclass(frozen=True)
class SignInValue:
    token: str
    member_id: int


class IdentityService:
    def __init__(self, bound: Callable[[], Any], source: SecretsSource) -> None:
        self._bound, self._source = bound, source

    def seed_admin(self, name: str, email: str, passcode: str) -> int:
        session = db.current_session()
        if session.scalar(select(func.count()).select_from(models.Member)):
            raise Refused("team_not_empty")
        salted = models.hash_passcode(passcode, self._source.salt())
        member = models.Member(name=name, email=email, role="admin", active=True, passcode_hash=salted)
        session.add(member)
        session.flush()
        return member.id

    def sign_in(self, email: str, passcode: str | None) -> SignInValue:
        session = db.current_session()
        by_email = select(models.Member).where(func.lower(models.Member.email) == email.lower())
        member = session.scalar(by_email)
        salt = member.passcode_hash.split("$")[0] if member else ""
        if member is None or passcode is None or models.hash_passcode(passcode, salt) != member.passcode_hash:
            raise Refused("invalid_credentials")
        member.token = self._source.token()
        session.flush()
        return SignInValue(token=member.token, member_id=member.id)

    def caller_for_token(self, token: str) -> Caller | None:
        member = db.current_session().scalar(select(models.Member).where(models.Member.token == token))
        if member is None or not member.active:
            return None
        return Caller(member_id=member.id, name=member.name, role=member.role, active=member.active)

    def is_active(self, member_id: int) -> bool | None:
        return None

    def role_of(self, member_id: int) -> Role:
        raise MemberNotFound(member_id)

    def name_of(self, member_id: int) -> str:
        raise MemberNotFound(member_id)

    def active_member_ids(self) -> list[int]:
        return []

    def decider_ids(self) -> list[int]:
        return []
''',
    "src/app/notifications/service.py": '''"""Rehearsal stand-in (scratch only, not the product): a Notifier that writes nothing."""

from __future__ import annotations

from app.ports import Event


class NotificationsService:
    def notify(self, event: Event) -> None:
        return None
''',
    "src/app/scheduling/service.py": '''"""Rehearsal stand-in (scratch only, not the product): a SchedulingPort with no assignment."""

from __future__ import annotations

from datetime import datetime

from app.ports import AssignmentInfo, AssignmentNotFound


class SchedulingService:
    def assignment(self, assignment_id: int) -> AssignmentInfo:
        raise AssignmentNotFound(assignment_id)

    def holds_intersecting_shift(self, member_id: int, shift_id: int) -> bool:
        return False

    def transfer(self, assignment_id: int, to_member_id: int) -> None:
        return None

    def has_assignment_after(self, member_id: int, now: datetime) -> bool:
        return False
''',
    "src/app/swaps/service.py": '''"""Rehearsal stand-in (scratch only, not the product): a SwapsPort with nothing pending."""

from __future__ import annotations

from datetime import datetime
from typing import Iterable

from app.ports import AssignmentView


class SwapsService:
    def view(
        self, caller_id: int, week_published: bool, assignments: Iterable[tuple[int, int, datetime]]
    ) -> dict[int, AssignmentView]:
        return {a: AssignmentView(pending=None, requestable=False) for a, _h, _s in assignments}
''',
}
IDENTITY_TEST = '''"""Rehearsal stand-in (scratch only, not the product): E-6b.10's clause of ADU-03 arm 1, against the
directory the composition root binds."""

from __future__ import annotations

from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from app import db, ports
from app.main import create_app


def test_a_request_reads_the_current_session_through_the_bound_directory(tmp_path: Path) -> None:
    app = create_app(workspace=tmp_path)
    service = app.state.ports.member_directory
    assert isinstance(service, ports.MemberDirectory)
    with db.unit_of_work(db.engine_for(tmp_path)):
        service.seed_admin("Ada", "ada@example.test", "pass-1")
    with db.unit_of_work(db.engine_for(tmp_path)):
        token = service.sign_in("ada@example.test", "pass-1").token
    client = TestClient(app)
    issued = client.get("/members", headers={"Authorization": f"Bearer {token}"})
    garbage = client.get("/members", headers={"Authorization": "Bearer garbage"})
    assert (issued.status_code, issued.json()["reason"]) == (501, "not_built")
    assert (garbage.status_code, garbage.json()["reason"]) == (401, "unauthenticated")


def test_a_method_called_with_no_session_current_raises(tmp_path: Path) -> None:
    service = create_app(workspace=tmp_path).state.ports.member_directory
    with pytest.raises(db.NoCurrentSession):
        service.sign_in("ada@example.test", "pass-1")
'''
BOUND_TEST = '''"""Rehearsal stand-in (scratch only, not the product): the {domain} stand-in is the bound port."""

from __future__ import annotations

from pathlib import Path

from app import ports
from app.main import create_app


def test_the_composition_root_binds_the_{domain}_stand_in(tmp_path: Path) -> None:
    bound = create_app(workspace=tmp_path).state.ports.{attr}
    assert isinstance(bound, ports.{proto}) and type(bound).__name__ == "{cls}"
'''
STAGES = [  # (stage, domain, Null module, stand-in, main.py rebinding, stand-in test, its test count)
    ("T-03", "identity", "src/app/identity/null_directory.py", "src/app/identity/service.py", [
        ("from app.identity.null_directory import NullDirectory\n",
         "from app.identity.service import IdentityService, SecretsSource\n"),
        ("member_directory=member_directory or NullDirectory(),  # replaced by ADU-03",
         "member_directory=member_directory or IdentityService(lambda: app.state.ports, SecretsSource()),")],
     IDENTITY_TEST, 2),
    ("T-09", "notifications", "src/app/notifications/null_notifier.py", "src/app/notifications/service.py", [
        ("from app.notifications.null_notifier import NullNotifier\n",
         "from app.notifications.service import NotificationsService\n"),
        ("notifier=notifier or NullNotifier(),  # replaced by ADU-09", "notifier=notifier or NotificationsService(),")],
     BOUND_TEST.format(domain="notifications", attr="notifier", proto="Notifier", cls="NotificationsService"), 1),
    ("T-05", "scheduling", "src/app/scheduling/null_port.py", "src/app/scheduling/service.py", [
        ("from app.scheduling.null_port import NullSchedulingPort\n", "from app.scheduling.service import SchedulingService\n"),
        ("scheduling=scheduling or NullSchedulingPort(),  # replaced by ADU-05",
         "scheduling=scheduling or SchedulingService(),")],
     BOUND_TEST.format(domain="scheduling", attr="scheduling", proto="SchedulingPort", cls="SchedulingService"), 1),
    ("T-07", "swaps", "src/app/swaps/null_port.py", "src/app/swaps/service.py", [
        ("from app.swaps.null_port import NullSwapsPort\n", "from app.swaps.service import SwapsService\n"),
        ("swaps=swaps or NullSwapsPort(),  # replaced by ADU-07", "swaps=swaps or SwapsService(),")],
     BOUND_TEST.format(domain="swaps", attr="swaps", proto="SwapsPort", cls="SwapsService"), 1),
]
REFUSED = ("        self.reason = reason\n",
           '        self.reason = reason\n\n\nclass Refused(Exception):\n'
           '    """Illustrative D-p2 shape (rehearsal only): a refusal a story names; no HTTP status."""\n\n'
           '    def __init__(self, reason: str, detail: str = "", **extra: object) -> None:\n'
           '        super().__init__(reason)\n'
           '        self.reason, self.detail, self.extra = reason, detail, extra\n')
# the illustrative current session of E-6 (b): db.py gains it, deps.py makes it current in an async dependency
DB_IMPORTS = ("from pathlib import Path\n",
              "from collections.abc import Iterator\nfrom contextlib import contextmanager\n"
              "from contextvars import ContextVar\nfrom pathlib import Path\n")
DB_CURRENT = '''

_CURRENT: ContextVar[Session | None] = ContextVar("app.db.current_session", default=None)


class NoCurrentSession(RuntimeError):
    """Illustrative E-6 (b) shape (rehearsal only): a service called with no session current."""


def current_session() -> Session:
    session = _CURRENT.get()
    if session is None:
        raise NoCurrentSession("no session is current")
    return session


@contextmanager
def use_session(session: Session) -> Iterator[Session]:
    token = _CURRENT.set(session)
    try:
        yield session
    finally:
        _CURRENT.reset(token)


@contextmanager
def unit_of_work(engine: Engine) -> Iterator[Session]:
    session = session_for(engine)
    try:
        with use_session(session):
            yield session
        session.commit()
    except BaseException:
        session.rollback()
        raise
    finally:
        session.close()
'''
DEPS = '''"""Request plumbing (ADU-02; rehearsal scaffold of E-6 (b), scratch only): the caller resolved once per
request through MemberDirectory, one session per request made current for the whole request, and the Problem
refusal shape of the cross-cutting rules."""

from __future__ import annotations

from collections.abc import AsyncIterator

from fastapi import Depends, Request
from fastapi.responses import JSONResponse
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session

from app import db
from app.ports import Caller

bearer = HTTPBearer(auto_error=False, scheme_name="bearer")


class ProblemError(Exception):
    """A refusal: {reason, detail, ...}; the status follows the bucket of the Reason codes table."""

    def __init__(self, status: int, reason: str, title: str, detail: str, **extra: object) -> None:
        super().__init__(reason)
        self.status, self.reason, self.title, self.detail, self.extra = status, reason, title, detail, extra


def problem_response(status: int, reason: str, title: str, detail: str, **extra: object) -> JSONResponse:
    return JSONResponse(
        {"type": "about:blank", "title": title, "detail": detail, "reason": reason, **extra}, status
    )


def engine_of(request: Request):
    app = request.app
    if app.state.engine is None:
        app.state.engine = db.engine_for(app.state.workspace)
    return app.state.engine


async def get_session(request: Request) -> AsyncIterator[Session]:
    """One session per request, current for the whole request: async, because a ContextVar set in a sync
    dependency is not visible to the endpoint; closing it rolls back what the router did not commit."""
    session = db.session_for(engine_of(request))
    try:
        with db.use_session(session):
            yield session
    finally:
        session.close()


def require_caller(
    request: Request,
    creds: HTTPAuthorizationCredentials | None = Depends(bearer),
    _session: Session = Depends(get_session),
) -> Caller:
    """unauthenticated before anything else: no token, an unknown token or an inactive member's token
    (R-identity-06); the request's session is current, so caller_for_token reads it."""
    token = creds.credentials if creds else None
    caller = request.app.state.ports.member_directory.caller_for_token(token) if token else None
    if caller is None:
        raise ProblemError(401, "unauthenticated", "Not signed in", "Sign in first.")
    return caller
'''
# N-1's twins: the wiring R1 broke, and the sync dependency
MUTATIONS = [
    ("require_caller without Depends(get_session)", DEPS.replace("    _session: Session = Depends(get_session),\n", "")),
    ("get_session a sync generator dependency", DEPS.replace("async def get_session(", "def get_session(")),
]
CHECK_E6B = '''import sys
from pathlib import Path

sys.path.insert(0, "src")
from app import db  # noqa: E402
from app.main import create_app  # noqa: E402

ws = Path(sys.argv[1])
directory = create_app(workspace=ws).state.ports.member_directory
try:
    directory.caller_for_token("tok_1")
    outside = "a session was current (unexpected)"
except db.NoCurrentSession:
    outside = "NoCurrentSession"
with db.unit_of_work(db.engine_for(ws)):
    inside = directory.caller_for_token("tok_1")
print(f"outside a unit of work -> {outside}; inside db.unit_of_work -> {inside}")
'''
E10_STAND_IN = '"""Scratch stand-in for {d}\'s service test (E-10 measurement only)."""\n\n\n' \
               'def test_{d}_stand_in() -> None:\n    assert True\n'
DOMAINS = ("identity", "notifications", "scheduling", "swaps")
RECOMMENDED = {1: "a", 2: "a", 3: "a", 4: "a", 5: "a", 6: "b", 7: "b", 8: "a", 9: "a", 10: "a"}
MAP_A = {**{f"D-p{i}": f"D-{11 + i}" for i in range(1, 8)}, **{f"Q-p{i}": f"Q-{7 + i:02d}" for i in range(1, 7)},
         "O-p1": "O-02", "O-p2": "O-03"}
MAP_B = {"D-p1": "D-12", "D-p2": "D-13", "D-p7": "D-14", **{f"Q-p{i}": f"Q-{7 + i:02d}" for i in range(1, 7)},
         "O-p1": "O-02", "O-p2": "O-03"}


def scaffold(tree: Path, stage: tuple, first_stage: bool) -> None:
    _stage, domain, null, stand_in, rebinding, test_text, _n = stage
    (tree / null).unlink()
    write(tree, stand_in, STAND_INS[stand_in])
    write(tree, f"tests/{domain}/test_{domain}_service.py", test_text)  # E-10 (a)'s name
    main = read(tree, "src/app/main.py")
    for old, new in rebinding:
        assert main.count(old) == 1, old
        main = main.replace(old, new)
    write(tree, "src/app/main.py", main)
    if first_stage:  # ADU-03: the illustrative Refused (D-p2) and the illustrative current session (E-6 (b))
        ports = read(tree, "src/app/ports.py")
        assert ports.count(REFUSED[0]) == 1
        write(tree, "src/app/ports.py", ports.replace(*REFUSED))
        dbm = read(tree, "src/app/db.py")
        assert dbm.count(DB_IMPORTS[0]) == 1
        write(tree, "src/app/db.py", dbm.replace(*DB_IMPORTS) + DB_CURRENT)
        write(tree, "src/app/api/deps.py", DEPS)


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8")  # adu prints "→"; a cp1252 console would die on it (FB-01's lesson)
    pack = PACK.read_text(encoding="utf-8").replace("\r\n", "\n")
    allb = blocks(pack)
    deletes = [m.groupdict() for m in DELETE.finditer(pack)]
    ok = True
    kinds = {k: sum(b["id"].startswith(k) for b in allb) for k in ("B-", "T-", "E-")}
    print(f"pack: {PACK} · {len(allb)} replace blocks (B {kinds['B-']}, T {kinds['T-']}, E {kinds['E-']}) · "
          f"{len(deletes)} file deletions · snapshot {SNAP}")

    # 1. B-blocks against the snapshot's blobs; the post-B text of every document
    report: list[str] = []
    bgroup = [b for b in allb if b["id"].startswith("B-")]
    post = {f: git_show(f) for f in {b["file"] for b in bgroup}}
    ok &= apply_group(post, bgroup, "against the 7d1e7d4 blob", report)

    def e_texts(eg: list[dict]) -> dict[str, str]:
        texts = dict(post)
        for f in {b["file"] for b in eg} - set(texts):
            texts[f] = git_show(f)
        return texts

    # 2. every E-block in the narrowest ruling that applies it: each option alone (its unconditional blocks, and
    #    those "without E-2 (b)"); then each conditional block in its context, reporting only that block
    singles = sorted({b["opt"] for b in allb if b["opt"]})
    for n, o in singles:
        eg = selected(allb, {1: "a", 2: "a", 3: "a", 4: "a", n: o})
        ok &= apply_group(e_texts(eg), eg, f"E-{n}{o} on post-B", report)
    for label, ctx, shown in (("E-2b with E-5a", {2: "b", 5: "a"}, "E-2b"), ("E-2b with E-5b", {2: "b", 5: "b"}, "E-2b"),
                              ("E-10b with E-2b", {2: "b", 10: "b"}, "E-10b"),
                              ("E-3b with E-2b", {2: "b", 3: "b"}, "E-3b"), ("E-10c with E-2b", {2: "b", 10: "c"}, "E-10c")):
        eg = selected(allb, {1: "a", 3: "a", 4: "a", **ctx})
        cond = {b["id"] for b in eg if b["id"].startswith(shown + ".") and b["conds"]}
        sub: list[str] = []
        good = apply_group(e_texts(eg), eg, label, sub, show=cond)
        ok &= good
        report += sub or [f"({label}: no conditional {shown} block applies; its other blocks, with E-2b's, all at their "
                          f"lines: {good})"]
    eg = [b for b in allb if b["id"] == "E-9.P"]
    ok &= apply_group(e_texts(eg), eg, "E-9.P on post-B: the pm-lead's, not applied", report)
    print("\n".join(report))

    # 3. every ruling the brackets allow: all blocks at their lines, rows in id order, the questions as status reads
    print("\nevery ruling the brackets allow (E-1..E-4 and E-10 always; E-6..E-9 all four with E-5 (a), none with (b)):")
    plans: dict[str, list[str]] = {}
    tally: dict[tuple[str, str], list] = {}
    composed: dict[str, str] = {}
    failures: list[str] = []
    for r in rulings():
        eg = selected(allb, r)
        texts = e_texts(eg)
        good = apply_group(texts, eg, "", None)
        d_rows = [x for x in re.findall(r"^\| (D-\w+) \|", texts["DECISIONS.md"], re.M) if x.startswith("D-p")]
        d_exp = ["D-p1", "D-p2"] + (["D-p3", "D-p4", "D-p5", "D-p6"] if r[5] == "a" else []) + \
                ([] if r[10] == "d" else ["D-p7"])
        tail = re.findall(r"^\| (D-\w+) \|", texts["DECISIONS.md"], re.M)[-len(d_exp):]
        o_rows = re.findall(r"^\| (O-\w+) \|", texts["STATUS.md"], re.M)
        o_exp = ["O-01", "O-p1"] + (["O-p2"] if r[10] == "d" else [])
        qs = questions(texts["OPEN-QUESTIONS.md"])
        blocking = sorted(q for q, (op, bl) in qs.items() if op and bl)
        b_exp = [] if r[5] == "a" else ["Q-p1", "Q-p2", "Q-p3", "Q-p4"]
        open_q = sorted(q for q, (op, _bl) in qs.items() if op and q.startswith("Q-p"))
        open_exp = (["Q-p5"] if r[5] == "a" else ["Q-p1", "Q-p2", "Q-p3", "Q-p4", "Q-p5"]) + \
                   (["Q-p6"] if r[10] == "d" else [])
        clean = r[5] == "b" or not re.search(r"Q-p[1-4]", texts["design/INTERFACES.md"])
        checks = (good, d_rows == d_exp == tail, o_rows == o_exp, blocking == b_exp, open_q == open_exp, clean)
        key = ("E-5a" if r[5] == "a" else "E-5b", f"E-10{r[10]}")
        t = tally.setdefault(key, [0, 0, set()])
        t[0] += 1
        t[1] += all(checks)
        t[2].add(len(eg))
        if not all(checks):
            failures.append(f"{code(r)}: {checks}")
        plans.setdefault(texts["ADU-PLAN.md"], []).append(code(r))
        if r == RECOMMENDED:
            composed = texts
    for (e5, e10), (n, good_n, sizes) in sorted(tally.items()):
        print(f"{e5} with {e10}: {n:3} rulings, {min(sizes)}–{max(sizes)} E-blocks each; all blocks at their lines, "
              f"DECISIONS and Owed rows in id order, open and blocking questions as expected: {good_n}/{n}")
    total = sum(v[0] for v in tally.values())
    print(f"total: {total} rulings; failures: {len(failures)}")
    print("\n".join(failures[:20]))
    ok &= not failures

    heads = [ln for ln in composed["OPEN-QUESTIONS.md"].splitlines() if ln.startswith("### Q-")]
    print(f"\nOPEN-QUESTIONS.md headings with the recommended options ({code(RECOMMENDED)}):")
    print("\n".join(heads[-7:]))
    owed = [ln for ln in composed["STATUS.md"].splitlines() if ln.startswith("| O")]
    print("STATUS.md Owed table, its rows cut at 110 characters:")
    print("\n".join(ln[:110] for ln in owed))
    sec = composed["design/INTERFACES.md"]
    start, end = sec.index("## Domain services"), sec.index("## Test doubles")
    print(f"\ndesign/INTERFACES.md with the recommended options, lines {sec.count(chr(10), 0, start) + 1}–"
          f"{sec.count(chr(10), 0, end)}:")
    print(sec[start:end].rstrip("\n"))
    if os.environ.get("PACK_REHEARSE_QUICK"):  # the text checks only (sections 1-3), for drafting
        print(f"\nall blocks matched: {ok}")
        return 0 if ok else 1

    # 4. the plan: B-3 alone (export B), the recommended options' plan text (export A), every distinct plan text
    a, b3, h, p = export("A-plan-and-stages"), export("B-plan-B3"), export("H-pristine"), export("P-plan-texts")
    write(b3, "ADU-PLAN.md", post["ADU-PLAN.md"])
    write(a, "ADU-PLAN.md", composed["ADU-PLAN.md"])
    pristine = adu(h, "plan", "order").stdout
    for label, tree in (("scratch copy with B-3 applied", b3),
                        ("scratch copy with the recommended options' plan text: B-3, E-6 (b), E-10 (a)", a)):
        for args in (("plan", "check"), ("plan", "order")):
            r = adu(tree, *args)
            print(f"\n$ adu {' '.join(args)}   # {label}, exit {r.returncode}\n{(r.stdout + r.stderr).rstrip()}")
        print(f"(adu plan order as at 7d1e7d4: {adu(tree, 'plan', 'order').stdout == pristine})")
    outs: dict[str, int] = {}
    exits = set()
    for text in plans:
        write(p, "ADU-PLAN.md", text)
        r = adu(p, "plan", "check")
        exits.add(r.returncode)
        outs[(r.stdout + r.stderr).strip()] = outs.get((r.stdout + r.stderr).strip(), 0) + 1
    print(f"\n{len(plans)} distinct ADU-PLAN.md texts among the {total} rulings; adu plan check exit codes {sorted(exits)}; "
          f"distinct outputs {len(outs)}:")
    for out, n in outs.items():
        print(f"  [{n} texts] {out}")
    ok &= exits == {0} and len(outs) == 1

    # 5. the guard, at 7d1e7d4, with B-3, with the recommended plan text, and with each option's own roster
    trees = [("at 7d1e7d4", h, ("tests/test_nulls.py", "tests/api/test_contract_conformance.py", "src/app/ports.py",
                                "src/app/db.py", "src/app/api/deps.py")),
             ("with B-3 applied", b3, ("tests/test_nulls.py", "tests/api/test_contract_conformance.py", "src/app/ports.py",
                                       "src/app/db.py", "src/app/api/deps.py")),
             ("recommended: B-3, E-6 (b), E-10 (a)", a, ("tests/test_nulls.py", "tests/api/test_contract_conformance.py",
                                                         "src/app/ports.py", "src/app/db.py", "src/app/api/deps.py",
                                                         "tests/identity/test_identity_service.py",
                                                         "tests/identity/test_service.py"))]
    for label, ctx, paths in (("with E-10 (b)", {10: "b"}, ("tests/identity/__init__.py",)),
                              ("with E-10 (c)", {10: "c"}, ("pyproject.toml",)),
                              ("with E-1 (b)", {1: "b"}, ("tests/support/doubles.py",)),
                              ("with E-2 (b)", {2: "b"}, ("src/app/refusals.py", "tests/layering.json", "src/app/ports.py"))):
        r = {**RECOMMENDED, **ctx}
        eg = selected(allb, r)
        texts = e_texts(eg)
        apply_group(texts, eg, "", None)
        tree = export("G-" + label.replace(" ", "").replace("(", "").replace(")", ""))
        write(tree, "ADU-PLAN.md", texts["ADU-PLAN.md"])
        trees.append((label + ", else as recommended", tree, paths))
    print()
    for label, tree, paths in trees:
        for path in paths:
            r = adu(tree, "guard", "edit", path, "--role", "developer")
            msg = (r.stdout + r.stderr).strip().replace("\n", " ")
            print(f"guard edit {path} --role developer ({label}) -> exit {r.returncode}: {msg[:150]}")

    # 6. E-10's options measured on the 7d1e7d4 tree, one stand-in test in each of the four service test files
    print("\nE-10, measured on the 7d1e7d4 tree with one stand-in test per service test file:")
    for label, name_of, init, importlib, with_files in (
            ("as planned: four tests/<domain>/test_service.py", lambda d: "test_service.py", False, False, True),
            ("(a) tests/<domain>/test_<domain>_service.py", lambda d: f"test_{d}_service.py", False, False, True),
            ("(b) tests/<domain>/__init__.py beside test_service.py", lambda d: "test_service.py", True, False, True),
            ("(c) addopts in pyproject.toml, no service test file yet", lambda d: "test_service.py", False, True, False),
            ("(c) addopts in pyproject.toml, four test_service.py", lambda d: "test_service.py", False, True, True)):
        tree = export("M-" + re.sub(r"\W+", "", label)[:24])
        if importlib:
            pyproject = read(tree, "pyproject.toml")
            anchor = 'pythonpath = ["src", "tests"]\n'
            assert pyproject.count(anchor) == 1
            write(tree, "pyproject.toml", pyproject.replace(anchor, anchor + 'addopts = "--import-mode=importlib"\n'))
        if with_files:
            for d in DOMAINS:
                write(tree, f"tests/{d}/{name_of(d)}", E10_STAND_IN.format(d=d))
                if init:
                    write(tree, f"tests/{d}/__init__.py", "")
        r = pytest(tree, "tests/", "-m", "not timing")
        err = first(r.stdout, r"^ERROR|import file mismatch")
        print(f"{label}: exit {r.returncode}: {last(r.stdout, r'passed|failed|error')}"
              f"{' | ' + err[:110] if not err.startswith('(no line') else ''}")

    # 7. the stages, in the derived order, on export A (the recommended options' plan text)
    print(f"\nbaseline (export A, the recommended plan text, no stage yet): {gate(a)}")
    stand_in_tests = 0
    for stage in STAGES:
        name, domain = stage[0], stage[1]
        first_stage = name == "T-03"
        scaffold(a, stage, first_stage)
        stand_in_tests += stage[6]
        if first_stage:  # the current session through the composition root, then the twins: each part of T-03 is needed
            ws = SCRATCH / "E6b-check-workspace"
            shutil.rmtree(ws, ignore_errors=True)
            r = run([str(PY), "-c", CHECK_E6B, str(ws)], a)
            print(f"E-6 (b) scaffold, the composition root's directory: exit {r.returncode}: "
                  f"{last(r.stdout + r.stderr, r'.')}")
            r = pytest(a, "tests/api/test_contract_conformance.py")
            print(f"twin 1 (Null deleted, conformance test unedited): exit {r.returncode}: "
                  f"{first(r.stdout, r'ModuleNotFoundError')} | {last(r.stdout, r'error|passed|failed')}")
            conf = {"tests/api/test_contract_conformance.py": read(a, "tests/api/test_contract_conformance.py")}
            partial = [b for b in allb if b["id"] in ("T-03.3", "T-03.6")]
            apply_group(conf, partial, "twin 2", [])
            write(a, "tests/api/test_contract_conformance.py", conf["tests/api/test_contract_conformance.py"])
            r = pytest(a, "tests/api/test_contract_conformance.py", "--tb=line")
            print(f"twin 2 (import and class check edited, no injected directory): exit {r.returncode}: "
                  f"{first(r.stdout, r'test_contract_conformance\.py:\d+: ').split('tests' + chr(92) + 'api' + chr(92))[-1][:170]} | {last(r.stdout, r'passed|failed')}")
            write(a, "tests/api/test_contract_conformance.py", git_show("tests/api/test_contract_conformance.py"))
        group = [b for b in allb if b["id"].startswith(name + ".")]
        texts = {f: read(a, f) for f in {b["file"] for b in group}}
        srep: list[str] = []
        ok &= apply_group(texts, group, f"stage {name}", srep)
        for f, t in texts.items():
            write(a, f, t)
        for dl in deletes:
            if dl["id"].startswith(name + "."):
                (a / dl["file"]).unlink()
                srep.append(f"{dl['id']:9} {dl['file']} deleted")
        print("\n".join(srep))
        if first_stage:  # N-1's twin: E-6b.10's clause, with the wiring right and broken as R1 broke it
            clause = "tests/identity/test_identity_service.py"
            for label, deps in [("wiring right", DEPS), *MUTATIONS]:
                write(a, "src/app/api/deps.py", deps)
                r = pytest(a, clause, "--tb=line")
                failed = first(r.stdout, r"(Error|assert|\.py:\d+)")
                print(f"N-1 twin, {label}: {clause}: exit {r.returncode}: {last(r.stdout, r'passed|failed|error')}"
                      f"{' | ' + failed[-120:] if r.returncode else ''}")
                if label.startswith("require_caller"):
                    print(f"  the full gate with that wiring (R1 measured 44 passed and HTTP 500): {gate(a)}")
            write(a, "src/app/api/deps.py", DEPS)
        print(f"after stage {name}: {gate(a)} (of which {stand_in_tests} in the stand-in service tests)")
    left = [str(q.relative_to(a)) for q in (a / "src").rglob("null_*.py")]
    imports = run(["git", "grep", "--no-index", "-I", "-n", "-E", r"null_(directory|notifier|port)", "--", "src", "tests"], a)
    print(f"after all four: Null modules left: {left or 'none'}; tests/test_nulls.py exists: "
          f"{(a / 'tests/test_nulls.py').exists()}; imports of a Null module under src/ and tests/: "
          f"{imports.stdout.strip() or 'none'}")
    files = [f"tests/{d}/test_{d}_service.py" for d in DOMAINS]
    r = pytest(a, *files, "--collect-only")
    print(f"the four service test files under E-10 (a)'s names, collected together: {last(r.stdout, r'collected|error')}")
    for d in DOMAINS:
        (a / f"tests/{d}/test_{d}_service.py").rename(a / f"tests/{d}/test_service.py")
    print(f"E-10 twin, the same four files renamed tests/<domain>/test_service.py: {gate(a)}")
    for d in DOMAINS:
        (a / f"tests/{d}/test_service.py").rename(a / f"tests/{d}/test_{d}_service.py")

    # 8. the simulated apply: the recommended rulings, and E-5 (b), with the ids substituted as D-2 allocates them
    for label, r, mapping, full in (("recommended", RECOMMENDED, MAP_A, True),
                                    ("E-5 (b), else as recommended", {1: "a", 2: "a", 3: "a", 4: "a", 5: "b", 10: "a"},
                                     MAP_B, False)):
        eg = selected(allb, r)
        texts = e_texts(eg)
        apply_group(texts, eg, "", None)
        tree = export("S-" + re.sub(r"\W+", "", label)[:20])
        used = set()
        for f, t in texts.items():
            t = re.sub(r"\b[DQO]-p\d+\b", lambda m: (used.add(m[0]), mapping[m[0]])[1], t)
            t = t.replace("<apply-date>", "2026-11-12").replace("docs/VERIFICATION-<id>.md", "docs/VERIFICATION-R2.md")
            write(tree, f, t)
        left = [f for f in texts if re.search(r"\b(ADU|Q|D|FB|O|MK)-p\d+\b", read(tree, f))]
        print(f"\nsimulated apply, {label}: {len(eg) + len(bgroup)} blocks into {len(texts)} files; ids substituted: "
              f"{', '.join(f'{k}→{mapping[k]}' for k in sorted(used, key=lambda x: (x[0], int(x[3:]))))}; "
              f"provisional ids left: {left or 'none'}")
        for args in (("ledger", "lint"), ("plan", "check"), ("derived", "render"), ("derived", "check"), ("pins", "check")):
            res = adu(tree, *args)
            print(f"$ adu {' '.join(args)} -> exit {res.returncode}: {(res.stdout + res.stderr).strip().splitlines()[0][:150]}")
        st = (adu(tree, "status").stdout or "").rstrip()
        print("$ adu status")
        print("\n".join(ln for ln in st.splitlines()
                        if full or ln.startswith(("Now:", "Open blocking", "Open non-blocking", "Owed items"))))
    print(f"\nall blocks matched: {ok}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
~~~

#### B-4.4 The simulated apply (part 8 of B-4.3's run)
These are the apply's own checks (D-2 steps 4 and 6), run on a scratch export of 7d1e7d4. The blocks of a ruling were applied first, with the ids substituted as D-2 allocates them if main took none, `<apply-date>` as 2026-11-12 and the report as docs/VERIFICATION-R2.md. The export's journal is the snapshot's, so `adu status` names that journal's last block (2026-11-07 20:20), not the apply's; and the STATUS Log line D-2 writes is not simulated. From B-4.3's output:

~~~text
simulated apply, recommended: 94 blocks into 7 files; ids substituted: D-p1→D-12, D-p2→D-13, D-p3→D-14, D-p4→D-15, D-p5→D-16, D-p6→D-17, D-p7→D-18, O-p1→O-02, Q-p1→Q-08, Q-p2→Q-09, Q-p3→Q-10, Q-p4→Q-11, Q-p5→Q-12, Q-p6→Q-13; provisional ids left: none
$ adu ledger lint -> exit 0: ledgers OK
$ adu plan check -> exit 0: plan OK: 18 units, order ADU-00 → ADU-01 → ADU-16 → ADU-02 → ADU-03 → ADU-09 → ADU-05 → ADU-07 → ADU-04 → ADU-06 → ADU-10 → ADU-08 → ADU-12 → ADU-17 →
$ adu derived render -> exit 0: derived blocks rendered (0 file(s) rewritten)
$ adu derived check -> exit 0: derived blocks OK
$ adu pins check -> exit 0: pins OK (1 pinned)
$ adu status
ADU status — Team Rota · 2026-11-12 10:38
Now: ADU-03 — Identity service · size M · layer 3 (domain services) · position 5/18 in the derived order
Depends: ADU-01 ✅, ADU-02 ✅, ADU-16 ✅
Consumes through mocks: MK-01 (SchedulingPort ← ADU-05, in-process), MK-02 (Notifier ← ADU-09, in-process)
Ledger row: planned
Last journal block: 2026-11-07 20:20 · hand-over ADU-03 (oversight) · blocked
NEXT (from the journal): `/adu-lifecycle:change-design Q-07` (stage 1, the pack) in a fresh `claude --plugin-dir C:\dev\adu-lifecycle --agent adu-lifecycle:architect` started inside `C:\dev\team-rota`; ADU-03 opens only after the apply step resolves Q-07.
Open blocking questions: none
Open non-blocking questions: Q-02, Q-03, Q-05, Q-12
Owed items: O-01 due ADU-11 (FB-02: the workspace database (`rota.sqlite`, default workspace `.rota`) can never be added to git before real data is seeded; `.gitignore` is in no roster, so editing it needs a grant); O-02 due ADU-04 (Q-12: the API units' wall on tests/api/test_contract_conformance.py and the helpers of src/app/api/contract_stubs.py is ruled in a design-change loop before ADU-04 opens (ADU-PLAN.md, ADU-04's pointer); Q-12 is entered non-blocking because `adu status` reads `**Blocking:** yes` as a stop for every unit, not ADU-04 alone (plugin FB-32))
Last gate run: 46 passed in 28.77s (STATUS.md:41)
Plan check: OK
Commands (from adu.toml):
  gate:   uv run pytest tests/ -q -m "not timing"
  fast:   uv run pytest tests/ -q -m "not calibration"
  timing: uv run pytest tests/ -q -m timing
  lint:   uv run ruff check

simulated apply, E-5 (b), else as recommended: 59 blocks into 6 files; ids substituted: D-p1→D-12, D-p2→D-13, D-p7→D-14, O-p1→O-02, Q-p1→Q-08, Q-p2→Q-09, Q-p3→Q-10, Q-p4→Q-11, Q-p5→Q-12, Q-p6→Q-13; provisional ids left: none
$ adu ledger lint -> exit 0: ledgers OK
$ adu plan check -> exit 0: plan OK: 18 units, order ADU-00 → ADU-01 → ADU-16 → ADU-02 → ADU-03 → ADU-09 → ADU-05 → ADU-07 → ADU-04 → ADU-06 → ADU-10 → ADU-08 → ADU-12 → ADU-17 →
$ adu derived render -> exit 0: derived blocks rendered (0 file(s) rewritten)
$ adu derived check -> exit 0: derived blocks OK
$ adu pins check -> exit 0: pins OK (1 pinned)
$ adu status
Now: ADU-03 — Identity service · size M · layer 3 (domain services) · position 5/18 in the derived order
Open blocking questions: Q-08 (design-change loop Q-07 (IdentityService)), Q-09 (design-change loop Q-07 (IdentityService)), Q-10 (design-change loop Q-07 (IdentityService)), Q-11 (design-change loop Q-07 (IdentityService)) — STOP: a blocking question means stop, not proceed-and-guess
Open non-blocking questions: Q-02, Q-03, Q-05, Q-12
Owed items: O-01 due ADU-11 (FB-02: the workspace database (`rota.sqlite`, default workspace `.rota`) can never be added to git before real data is seeded; `.gitignore` is in no roster, so editing it needs a grant); O-02 due ADU-04 (Q-12: the API units' wall on tests/api/test_contract_conformance.py and the helpers of src/app/api/contract_stubs.py is ruled in a design-change loop before ADU-04 opens (ADU-PLAN.md, ADU-04's pointer); Q-12 is entered non-blocking because `adu status` reads `**Blocking:** yes` as a stop for every unit, not ADU-04 alone (plugin FB-32))
~~~

What it shows, in five points:
- Under the recommended rulings, `adu status` prints "Open blocking questions: none" with Now: ADU-03, as the hand-over's section A expects (plugin scripts/adu.mjs:398).
- Q-p5, allocated Q-12, is listed among the open non-blocking questions, and O-p1, allocated O-02, among the owed items, due ADU-04: R1 N-2 is closed.
- The four questions entered resolved (Q-08 … Q-11) keep their `**Blocking:** yes — for ADU-03` lines and are listed nowhere, because `adu status` reads a question's state first.
- `adu derived render` rewrites no file, so ADU-03's entry is unchanged by it (R1 Notes).
- Under E-5 (b), Q-08 … Q-11 stop ADU-03, which is Now, and Q-12 is still not among them.

### B-5 Questions (provisional)
Q-p1 … Q-p6, in full, are the text B-2.7 enters into OPEN-QUESTIONS.md (each with its allocated id). In short:
- **Q-p1 (blocking ADU-03):** how the IdentityService, bound once, reaches the request's session. Recommended (b): a request-scoped current session set by an async dependency, for all four services. Measured: a ContextVar set in a sync generator dependency is invisible to the endpoint; set in an async one, it is visible (the probe below).
- **Q-p2 (blocking ADU-03):** how it receives its collaborators across the identity ↔ scheduling cycle. Recommended (b): the composition root's `Ports` container, read at call time.
- **Q-p3 (blocking ADU-03):** the token and salt source against "No randomness in the product". Recommended (a): an injected `secrets`-based source and a DECISIONS row amending ARCHITECTURE.md:45.
- **Q-p4 (blocking ADU-03):** the returned values and their home. Recommended (a): the contract's Member fields, values defined in identity's service module; PRODUCT-DESIGN.md:18 reworded editorially.
- **Q-p5 (non-blocking; owed before ADU-04):** the API units' wall on the same test and the helpers in contract_stubs.py, with ADU-04's route to the IdentityService and the commit no API arm sees. Recommended (b): one re-cut before ADU-04. It is entered `**Blocking:** no`, and the Owed row O-p1 due ADU-04 (E-5a.14 or E-5b.1) and ADU-04's pointer (B-3.16) carry the duty, because `adu status` would stop ADU-03 on a blocking question (R1 N-2; plugin FB-32).
- **Q-p6 (non-blocking for ADU-03; before ADU-09):** the four `tests/<domain>/test_service.py` fail collection together (R1; plugin FB-33). Ruled in this apply as E-10, recommended (a): unique basenames.

The probe behind Q-p1 (scratch; `python -I`, the project's venv):
~~~text
"""Scratch probe for the pack's Q-p1: is a ContextVar set inside a FastAPI dependency visible to the endpoint?"""
import contextvars
from fastapi import Depends, FastAPI
from fastapi.testclient import TestClient

CURRENT = contextvars.ContextVar("current", default=None)
app = FastAPI()

def sync_dep():
    CURRENT.set("set-by-sync-generator-dependency")
    try:
        yield
    finally:
        pass  # no reset: the first run showed the teardown runs in another Context

async def async_dep():
    CURRENT.set("set-by-async-generator-dependency")
    try:
        yield
    finally:
        pass  # no reset: the first run showed the teardown runs in another Context

@app.get("/sync-dep/sync-endpoint")
def a(_=Depends(sync_dep)):
    return {"seen": CURRENT.get()}

@app.get("/async-dep/sync-endpoint")
def b(_=Depends(async_dep)):
    return {"seen": CURRENT.get()}

c = TestClient(app)
for path in ("/sync-dep/sync-endpoint", "/async-dep/sync-endpoint"):
    print(path, "->", c.get(path).json())
import fastapi, starlette
print("fastapi", fastapi.__version__, "starlette", starlette.__version__)
~~~
Output:
~~~text
/sync-dep/sync-endpoint -> {'seen': None}
/async-dep/sync-endpoint -> {'seen': 'set-by-async-generator-dependency'}
fastapi 0.162.0 starlette 1.10.0
~~~
The first run, with `CURRENT.reset(token)` in the sync dependency's `finally`, ended in `ValueError: <Token var=<ContextVar name='current' …>> was created in a different Context`, raised from the sync dependency's teardown.

## Part C — the chase list
For the apply step's `adu chase "<old>" "<new>"`. Hits were found with `git grep` at 7d1e7d4 over the documents, the sources and the tests; ledgers (SESSION-JOURNAL, OPEN-QUESTIONS, FEEDBACK) and docs/PLAN-REVIEW-1.md are records and stay.

| old term / id / count | new | where it is expected to appear, and the disposition |
|---|---|---|
| "test_contract_conformance.py still passes" | "the NullDirectory import and its binding go", plus the conformance `amends` line | ADU-PLAN.md:151 only → B-3.3 |
| "the contract unit's tests stay green unchanged" | "the contract unit's tests and tests/test_nulls.py pass in the gate after exactly the edits this entry's amends declare on them, each made under the operator's grant (Q-07)" | ADU-PLAN.md:159 only → B-3.5 |
| "and its test_nulls test are deleted" | the widened arm text | ADU-PLAN.md:159, :188, :216, :246 → B-3.5, B-3.8, B-3.11, B-3.14 |
| "the <Null> test is deleted with its stub" | the full four-place edit | ADU-PLAN.md:153, :184, :210, :242 → B-3.4, B-3.7, B-3.10, B-3.13 |
| "stay green unchanged" for the identity tests and the scheduling tests | stays | ADU-PLAN.md:188, :216, :246: true as written — those suites use the doubles and no retirement edits them (the B-4.3 stages confirm the gate stays green) |
| "deleting the Null and its stub test — both declared as `amends`" | "deleting the Null, and editing the completed tests that name it … the two tests edited only under the operator's grant (Q-07)" | ADU-PLAN.md:6 → B-3.2 |
| "one test per Null, each deleted together with its Null by the retiring unit" | stays | ADU-PLAN.md:102 (ADU-16, completed): the record of what ADU-16 built; the shared parametrised test it does not mention is covered by each retiring unit's `amends` (B-3) |
| "the Null until ADU-03" / "the Null until its provider lands" | stays | ADU-PLAN.md:129, :132 (ADU-02's arms): history, and still true |
| "golden still equal" / "golden unchanged" / "the 501 placeholder … gone once the last router lands" | stays | ADU-PLAN.md:128, :273, :299, :325, :349, :357: not retirements of a Null; the API units' wall is Q-p5 |
| `Refused` (new term, defined by D-p2) | `src/app/ports.py` `Refused(reason, detail="", **extra)` | ADU-PLAN.md:160, :161 name it; B-2.3 defines it. "refuses <code>" in the arms of ADU-05, ADU-07 and ADU-09 means `Refused(<code>)`: stays |
| `IdentityService` (term gains a section) | design/INTERFACES.md §IdentityService | ADU-PLAN.md:145, :151, :235, :258, :268: stays, now resolvable |
| "the five protocols" | stays | ADU-PLAN.md:99 (ADU-16's arm), tests/test_ports.py:1 (its docstring) and VERSIONS.md:90 (a History row): `Refused` is an exception like `TransferRefused`, not a protocol, and §Refused is a section of its own after "## Protocols" (B-2.3) |
| "one test per Null" | stays | tests/test_nulls.py:1, the module docstring of ADU-16's completed test: no retirement edits it, and ADU-07 removes the file (T-07.3); ADU-PLAN.md:102 as the row above says |
| "No randomness in the product" | the ruled text of E-8 | design/ARCHITECTURE.md:45 only → E-8a.2 or E-8b.2 |
| "a member as the team list shows it" | the pm-lead's wording (E-9.P) | design/PRODUCT-DESIGN.md:18 → the pm-lead's patch, not this apply; design/DESIGN-REVIEW-7.md:36 is a record and stays |
| "two cycles (identity ↔ scheduling, scheduling ↔ swaps)" / "identity ↔ scheduling (IR-05 / IR-06) and scheduling ↔ swaps" | the three cycles, identity ↔ notifications added | design/ARCHITECTURE.md:18 and design/INTERFACES.md:92 → E-7a.5–.6 or E-7b.4–.5 |
| "One session and one write transaction per request" | stays, with the ruled sentence of E-6 after it | design/ARCHITECTURE.md:42 → E-6a.6 or E-6b.5, which append and change nothing before them |
| `tests/identity/test_service.py`, `tests/notifications/test_service.py`, `tests/scheduling/test_service.py`, `tests/swaps/test_service.py` | under E-10 (a): `tests/<domain>/test_<domain>_service.py` | ADU-PLAN.md only: the `tests:` lines :149, :180, :206, :238 and the arms' files :159–:165, :188–:191, :216–:221, :223, :246–:248, :252–:254 → E-10a.1–E-10a.28; under (b), (c) and (d) they stay |
| `test_the_composition_root_binds_a_null_per_port_and_an_injectable_clock` (E-4 a) | `test_the_composition_root_binds_an_implementation_per_port_and_an_injectable_clock` | tests/api/test_contract_conformance.py:102 only (`git grep` finds no other reference): renamed by ADU-03's session, not by the apply |
| design/INTERFACES.md v1.0.1 | v1.1 | INTERFACES.md:2 (B-2.2); VERSIONS.md Current has no INTERFACES row at 7d1e7d4 (B-2.8) |
| ADU-PLAN v1.2 | v1.3 | ADU-PLAN.md:2 (B-3.1); VERSIONS.md:14 (B-2.8) |
| Q-07 open, blocking | resolved → D-p1 | OPEN-QUESTIONS.md:53, :59 (B-2.6, B-2.7); `adu status` reads it from there |
| Q-p5 "blocking ADU-04" (pack v1.1) | `**Blocking:** no`, owed by O-p1 | not in any governing document at 7d1e7d4: B-2.7 enters it so; STATUS.md gains the Owed row (E-5a.14 or E-5b.1) and ADU-PLAN.md ADU-04's pointer (B-3.16) |
| "each with a `Null<Interface>` in the contract unit" | stays (observed, not this change's term) | design/INTERFACES.md:2: stale since v1.0.1 moved the Nulls to ADU-16 (:14 says so); an editorial fix for the next INTERFACES patch, recorded here so it is not lost |
| the ADU-03 hand-over (`adu handover ADU-03`) | regenerated after the apply | it must list the `amends` files and the two grant steps (plugin FB-30 (1): C1 omits `amends`; plugin FB-28: no grant step) — the oversight session's D-0 check |

## Part D — prompts

### D-1 The verify prompt (round R2)
For a fresh `claude --plugin-dir C:\dev\adu-lifecycle --agent adu-lifecycle:verifier`, started from a PowerShell inside `C:\dev\team-rota`:

~~~text
Verification round R2 for Team Rota: /adu-lifecycle:verify docs/PACK-q07-retire-amends.md

You are a fresh verifier; you wrote neither this pack nor round R1's report, and you change nothing in the repository except your report and your journal block.

1. `adu status`: expect Now: ADU-03 and Q-07 open and blocking (the pack answers Q-07; it does not open ADU-03). Then confirm three variables before any `uv` or python command: `$env:UV_PROJECT_ENVIRONMENT` is `C:\dev\team-rota-data\.venv` (the User-level variable names another project's venv); `$env:PYTHONUTF8` is empty; and `$env:ADU_PLUGIN_ROOT` is `C:\dev\adu-lifecycle` (in Git Bash, `echo $ADU_PLUGIN_ROOT`). Without the last, every scratch gate shows 4 failures in tests/test_method.py (plugin FB-19), which are not the pack's. Then the interpreter line, `uv run python -c "import sys, locale; print(sys.prefix, locale.getpreferredencoding(False), sys.flags.utf8_mode)"`: expect `C:\dev\team-rota-data\.venv cp1252 0`. A bare `python -c …` may print `C:\Python314 cp1252 0`: that is the system interpreter, not the gate's, and not a finding. `git status --short` is expected to show `?? uv.lock` only (Q-05): the pack v1.2 is committed.
2. Snapshot gate: `adu snapshot check 7d1e7d4`. Exit 2 → the report is the command's output and `VERDICT: STOP — STALE`; nothing else is verified.
3. Read the pack (v1.2) in full, then docs/VERIFICATION-R1.md in full. Then OPEN-QUESTIONS.md:53–59 (Q-07), and the SESSION-JOURNAL.md blocks of: 2026-11-07 20:20 (the hand-over that raised Q-07); the pack's drafting sessions (2026-11-08 08:39, v1.0; 2026-11-08 18:34, v1.1; 2026-11-12, v1.2); and 2026-11-08 22:45 (verification R1). Then the plugin's FEEDBACK.md rows FB-28 and FB-31 to FB-33 (C:\dev\adu-lifecycle\FEEDBACK.md).
4. Round R1's dispositions. For each, report CARRIED OUT / PARTLY / NOT CARRIED OUT, with the pack's line where it is carried out; this is section 1 of your report.
   a. N-1: E-6b.10 appends R1's clause (docs/VERIFICATION-R1.md:177) to ADU-03's arm 1 (post-B ADU-PLAN.md:161), with "under D-p3" written as "under the request's current session of design/INTERFACES.md (Domain services)". B-4.3 rehearses the twin: the stand-in test of the clause fails with `require_caller` not depending on `get_session` and with `get_session` sync, and passes with the wiring right. Re-run that twin yourself.
   b. N-2: Q-p5 is entered `**Blocking:** no` (B-2.7). The Owed row O-p1, due ADU-04, is written in STATUS.md's columns (O | Due | Where | Approval | Status) by E-5a.14 or E-5b.1, with the Approval cell naming the E-5 ruling and plugin FB-32 cited. ADU-04's pointer is B-3.16. B-5, E-5, E-5a.1 and D-2 are aligned. On your own simulated apply with ids substituted, `adu status` prints "Open blocking questions: none" with Now: ADU-03 (B-4.4 shows the pack's).
   c. M-1: E-2b.8–E-2b.18, including R1's E-5 (a) and E-5 (b) cases.
   d. M-2: E-3b.5 (without E-2 (b)) and E-3b.6.
   e. M-3: E-1b.1–E-1b.4, with B-2.4's string as it is and the doubles line's stated position; and E-4 (b), written as E-4b.1.
   f. Each Note of R1 §5, and each cosmetic remark in R1 §2–§3: rows 40, 63, 79, 81, 82 and 83, §2.6 on B-2.3, E-7, E-8 and E-9, and §3 on B-3.3 and T-03.6. The pack's header (line 3) maps each to where it is handled; confirm each there.
   g. Q-p6: entered by B-2.7 and ruled as E-10. Check four things: the complete text of options (a)–(d); each option's roster consequences (E-10's table); a recommendation with reasons; and the recommended option rehearsed (with all four stages applied, the four service test files collect together and the gate is green).
5. Claims, each CONFIRMED / WRONG / UNVERIFIABLE with file and line, as R1 §2 did:
   a. every B-block (B-2.1–B-2.9, B-3.1–B-3.14, B-3.16) against the 7d1e7d4 blob (`git show 7d1e7d4:<file>`): text character for character with line endings normalised, unique in its file, starting at the stated line;
   b. every T-block (B-2.T) against the file as the previous T-stage leaves it, starting from 7d1e7d4 for T-03. Each E-block against the text as B leaves it: a conditional block under its condition, and a block "on the text E-xx writes" after the other ruled blocks of its file;
   c. Part A-2's table, row by row, its new rows included: plugin scripts/lib/ledgers.mjs:26–27 and :83–85; scripts/adu.mjs:81–82, :85–86 and :398; scripts/lib/plan.mjs:181, :214, :219 and :234 (the plugin at C:\dev\adu-lifecycle);
   d. the guard, as R1 checked it, and for the new rosters. Under E-10 (a), the renamed test path is allowed and the old one refused. Under E-10 (b), `tests/identity/__init__.py` is allowed; under E-10 (c), `pyproject.toml`; under E-1 (b), `tests/support/doubles.py`;
   e. every amendment names the file and the assertion it falsifies, in both directions;
   f. that no arm is weakened: each rewritten arm, E-6a.9 and E-6b.10 included, against the arm it replaces and against ADU-02's arms (ADU-PLAN.md:126–133) and ADU-16's (:99–104); say how each can fail;
   g. as R1's 4g: B-2.3 and the completed texts of E-6–E-9 each settle exactly their point. Then the same for E-10's options: each changes only what its column of E-10's table says, and the table is true (which units' `tests:`, arms' `file:`, T-blocks and plan lines change; whether a completed unit's file or a protected path is touched; whether a grant is needed);
   h. what the pack does not claim. List each thing the pack leaves unrehearsed, or states only by arithmetic or by reading, and check that it says so where it relies on it. At least:
      - E-6 (a)'s clause (E-6a.9) is not rehearsed;
      - the T-text of E-1 (b) and E-4 (b) is stated, not rehearsed: its line shifts are arithmetic;
      - the stand-in services, the stand-in tests, the illustrative `Refused` and the illustrative current session are scaffolding, not proposed text;
      - E-10 (b) and (c) are measured with stand-in files on the 7d1e7d4 tree, not through the four stages;
      - E-9.P is the pm-lead's and is not applied.
6. Measurements, in your own scratchpad, never in the repository:
   (i) `git archive 7d1e7d4` into a scratch folder, apply B-3, and run `adu plan check` and `adu plan order` with the working directory inside the copy. Repeat with the recommended options' plan text (B-3, E-6 (b), E-10 (a)), and compare both with B-3.15. Then check as many of the other rulings' plan texts as you judge needed; B-4.3 runs all of them.
   (ii) Re-run B-4.3's rehearsal (the pack's script, or your own equivalent). Compare, per stage, the gate count, the lint and the twins (v1.1's two, the N-1 twin and the E-10 twin). Compare the 1,088 rulings and the E-10 option measurements.
   (iii) Your own simulated apply of the recommended rulings with ids substituted (D-12 … D-18, Q-08 … Q-13 and O-02, if main took none): `adu ledger lint`, `adu plan check`, `adu derived render` and `adu derived check`, `adu pins check`, `adu status`. Then the same under E-5 (b): `adu status` lists the allocated Q-p1 … Q-p4 as blocking and Q-p5 as non-blocking.
   (iv) The ContextVar probe of B-5 and the current-session probe of E-6 need re-running only if a pack line about them changed since R1. None did; say so if you skip them.
   Table: the pack's value · yours · verdict per cell.
7. Optional, once: `uv run pytest tests/ -q -m "not timing" -p no:cacheprovider` at HEAD, expect `46 passed`; `git status --short` unchanged afterwards.
8. The report: docs/VERIFICATION-R2.md, named by hand, because `adu next-id V` crashes with EISDIR, and would print V-1, not R2, if it ran (plugin FB-31). Use the skill's report shape, with section 1 holding R1's dispositions (item 4), each with file and line. The verdict is the last line and the token VERDICT appears nowhere else; `adu verdict check docs/VERIFICATION-R2.md` passes. Then your journal block. Write nothing else.
~~~

### D-2 The apply prompt
For a fresh `claude --plugin-dir C:\dev\adu-lifecycle --agent adu-lifecycle:release-manager`, started from a PowerShell inside `C:\dev\team-rota`, after round R2's report and the operator's rulings on Part E:

~~~text
Design-change loop, stage 4 (apply) for Team Rota: /adu-lifecycle:change-design apply docs/PACK-q07-retire-amends.md

First, the interpreter line: `uv run python -c "import sys, locale; print(sys.prefix, locale.getpreferredencoding(False), sys.flags.utf8_mode)"` prints `C:\dev\team-rota-data\.venv cp1252 0` (a bare `python -c …` may print `C:\Python314 …`, the system interpreter, which is not the gate's).

Preconditions — stop and tell me if any fails:
- docs/VERIFICATION-R2.md, for this pack at v1.2, ends `VERDICT: READY` or `VERDICT: READY WITH MECHANICAL ADAPTATIONS`.
- My rulings on Part E (E-1 … E-10) are pasted at the end of this prompt, verbatim. There is one option for each of E-1, E-2, E-3, E-4, E-5 and E-10. There is one for each of E-6 … E-9 if E-5 is (a), and none if it is (b).
- `adu snapshot check 7d1e7d4` exits 0.
- `$env:UV_PROJECT_ENVIRONMENT` is `C:\dev\team-rota-data\.venv`, `$env:PYTHONUTF8` is empty, and `$env:ADU_PLUGIN_ROOT` is `C:\dev\adu-lifecycle`.

1. First: re-derive every provisional identifier against HEAD and record the mapping in docs/APPLICATION-REPORT-q07-retire-amends.md (from the plugin's templates/reports/APPLICATION-REPORT.md).
   - DECISIONS rows, from `adu next-id D`, in the order they stand: D-p1, D-p2; then D-p3 … D-p6 under E-5 (a); then D-p7 unless E-10 is (d). If main took none, that is:
     - all seven: D-12 … D-18;
     - E-5 (a) with E-10 (d): D-12 … D-17;
     - E-5 (b): D-12, D-13 and D-14 (= D-p7);
     - E-5 (b) with E-10 (d): D-12, D-13.
   - Questions, from `adu next-id Q`: Q-p1 … Q-p6 are Q-08 … Q-13 if main took none. Each is an entry, whether entered open or resolved, so each takes its id.
   - Owed rows, from `adu next-id O`: O-p1 is O-02 if main took none. O-p2 exists only under E-10 (d), and takes the next id (O-03).
   - Replace every provisional id, every `<apply-date>` and every `docs/VERIFICATION-<id>.md` (→ docs/VERIFICATION-R2.md) in the text you apply. Never renumber to dodge a number main took.
2. Apply B-2.1–B-2.9, B-3.1–B-3.14 and B-3.16 block by block: bottom-up within each file, right to left within a line, each `replace exactly` matching character for character with line endings normalised. A miss is a stop, not a guess.
   - For each bracket, apply the blocks of the option I ruled, on top of B. Of the conditional blocks, apply those whose heading's condition my rulings meet. A block "on the text E-xx writes" goes after the other blocks of its file.
   - Shared anchors: the DECISIONS rows go E-10, E-9, E-8, E-7, E-6, and the Owed rows of STATUS.md go E-10 (d), then E-5, so each stands in id order.
   - STATUS.md: write the Owed row O-p1 (E-5a.14 or E-5b.1), and O-p2 under E-10 (d), with their allocated ids and the Approval cell as the block writes it.
   - A ruled option whose text is not in the pack stops the apply, and so does a ruling of some but not all of E-6–E-9.
   - Do not apply B-2.T: those edits belong to the retiring units' sessions, each under its own grant.
   - Do not apply E-9.P either: it is the pm-lead's patch of PRODUCT-DESIGN.md:18. Record it in the application report as the pm-lead's to make.
3. Chase every row of Part C with `adu chase "<old>" "<new>"`; change each hit or record in the application report why it stays.
4. Make round R2's mechanical adaptations, if it lists any, in the governing documents (never in the pack). Then run:
   - `adu derived render`;
   - `adu plan check`: expect `plan OK: 18 units` and the order of B-3.15;
   - `adu derived check`, `adu ledger lint`, and `adu pins check` (no pinned file changes);
   - `adu status`: expect "Open blocking questions: none" under E-5 (a), or the allocated Q-p1 … Q-p4 under E-5 (b), and the Owed row or rows listed.
5. Versions as the blocks write them: ADU-PLAN 1.2 → 1.3; design/INTERFACES.md 1.0.1 → 1.1 (it gains the Current row it lacked); design/ARCHITECTURE.md 1.1 → 1.2 under E-5 (a), and under E-5 (b) only with E-2 (b). Q-07 is resolved as B-2.6–B-2.7 write it.
6. Run the gate once, `uv run pytest tests/ -q -m "not timing"`, then the lint, `uv run ruff check`, and report the last line of each. Expect `46 passed …` (STATUS.md:40; this loop changes no test) and `All checks passed!`; any other count or any lint finding is a stop. Then write your journal block and a STATUS Log line ending `backward: n/a (documents only)`. I commit with the message `docs: apply pack q07-retire-amends (ADU-PLAN v1.3, INTERFACES v1.1, ARCHITECTURE v1.2)`, without ARCHITECTURE v1.2 when it did not move.
7. NEXT in your journal block, under E-5 (a): the ADU-03 hand-over is next. The oversight session regenerates `adu handover ADU-03` and checks it against the entry; its section A expects "Open blocking questions: none". The hand-over must say:
   - "design updated: ADU-PLAN v1.3 (ADU-03's amends, tests and arm 1; the same pattern in ADU-09, ADU-05, ADU-07), INTERFACES v1.1 (§Refused, §Domain services — the request's session and IdentityService, the retirement paragraph), ARCHITECTURE v1.2 (§Layers, §Persistence and concurrency rules)";
   - in its first section, the two grants the session asks me for (`tests/api/test_contract_conformance.py`, `tests/test_nulls.py`), since the guard does not honour amends on a completed unit's test (plugin FB-28);
   - in its roster, the amends files, which C1 omits (plugin FB-30 (1)). Under E-6 (b) that is src/app/db.py and src/app/api/deps.py, which need no grant because they are not tests. Under E-1 (b) it is tests/support/doubles.py, under E-2 (b) src/app/refusals.py and tests/layering.json, and under E-10 (c) pyproject.toml. Under E-10 (a), its test file is tests/identity/test_identity_service.py;
   - that the Owed row O-p1 (allocated), due ADU-04, is listed by `adu status` and is not ADU-03's; under E-10 (d), O-p2 is due ADU-09.
   The pm-lead's E-9.P patch follows in a pm-lead session and does not block ADU-03.
   Under E-5 (b), ADU-03 still does not open: I rule the allocated Q-p1 … Q-p4 first, and the ADU-03 hand-over follows their loop.

My rulings on Part E:
<paste here>
~~~

## Part E — the operator's decisions
Each bracket's options have their text in this pack. An option without text stops the apply: E-1 (c), E-6 (c), E-7 (c), E-8 (c) and E-9 (b) are such options. E-6–E-9 are ruled all four or none; E-5 says how each case is entered. E-1–E-5 and E-10 are ruled with every apply. Every adaptation an option needs in another bracket's text is a block of its own, conditional where it depends on that bracket's ruling, so no option carries an adaptation into the apply.

**1. Which double answers `Bearer tok_1` in the 401/501 test.** No existing double resolves `tok_1` as constructed (Part A-2).
[(a) recommended: `FakeMemberDirectory`, configured in the test with `add(1, "Member 1", "member", token="tok_1")`, the same Caller the Null gave; nothing but the test changes (T-03.2, T-03.4, B-3.3, B-2.4)
| (b) a new double `TokenDirectory` in tests/support/doubles.py that resolves any `tok_<id>` as the Null did — blocks E-1b.1–E-1b.4 below. ADU-03 gains an `amends` line for tests/support/doubles.py, after its tests/test_nulls.py line (a `files` path of ADU-16, so no grant). The session's text changes too: T-03.2 reads `from support.doubles import FixedClock, TokenDirectory  # noqa: E402`, and T-03.4's three lines become `    client = TestClient(create_app(workspace=tmp_path, member_directory=TokenDirectory()))`, so the later conformance lines move up by 2 (T-09.2 :108, T-05.2 :106, T-07.2 :106; with E-4 (b) as well, by 4). The consequence: the Null's behaviour lives on under another name, and tests/test_ports.py does not cover the new double
| (c) the real IdentityService with an admin seeded in tmp_path and the token sign_in issues — no text in this pack: the edit depends on Q-p1–Q-p4; choosing it stops the apply]

#### E-1b.1 · design/INTERFACES.md:126
replace exactly (within the line):
~~~text
injects `FakeMemberDirectory` through `create_app(member_directory=…)`, holding the member and token it needs
~~~
with:
~~~text
injects `TokenDirectory` (tests/support/doubles.py, which resolves `tok_<id>` as the retired Null did) through `create_app(member_directory=…)`
~~~

#### E-1b.2 · ADU-PLAN.md:152
replace exactly (within the line):
~~~text
the 401/501 test builds its app with create_app(workspace=tmp_path, member_directory=directory), directory a FakeMemberDirectory holding member 1 ('Member 1', member, active) with token tok_1, so Bearer tok_1 still answers 501 not_built
~~~
with:
~~~text
the 401/501 test builds its app with create_app(workspace=tmp_path, member_directory=TokenDirectory()), so Bearer tok_1 still answers 501 not_built
~~~

#### E-1b.3 · ADU-PLAN.md:154
The doubles line goes after ADU-03's tests/test_nulls.py line, beside its other ADU-16 lines.
replace exactly (within the line):
~~~text
the other Nulls' imports, entries and tests are unchanged", q: Q-07 }
~~~
with:
~~~text
the other Nulls' imports, entries and tests are unchanged", q: Q-07 }
  - { unit: ADU-16, file: tests/support/doubles.py, assertion: "gains TokenDirectory, a MemberDirectory double that resolves tok_<id> to an active member 'Member <id>' of role member, as the retired NullDirectory did; nothing else in the module changes", q: Q-07 }
~~~

#### E-1b.4 · VERSIONS.md:123
replace exactly (within the line):
~~~text
the Shape-of-the-cut sentence on retirement;
~~~
with:
~~~text
ADU-03 amends tests/support/doubles.py (TokenDirectory); the Shape-of-the-cut sentence on retirement;
~~~

**2. Where `Refused` lives.**
[(a) recommended: `src/app/ports.py` (ADU-16's module), by the `amends` line in B-3.4; no grant (a `files` path), no layering change
| (b) a new module `src/app/refusals.py` in ADU-03's own `files`, joined to the ports layer in tests/layering.json (ADU-00's file, an `amends` line; otherwise the module escapes the scan, Part A-2), with ADU-03's `depends` gaining ADU-00 — blocks E-2b.1–E-2b.7 below; the order is unchanged (E-2b plan check in B-4.3)]
Not offered: a module in identity's own package. Every later service importing it would be a forbidden edge (`["scheduling","identity"]` and the rest in tests/layering.json).

#### E-2b.1 · ADU-PLAN.md:147
replace exactly:
~~~text
depends: [ADU-01, ADU-02, ADU-16]
~~~
with:
~~~text
depends: [ADU-00, ADU-01, ADU-02, ADU-16]
~~~

#### E-2b.2 · ADU-PLAN.md:148
replace exactly:
~~~text
files: ["src/app/identity/service.py", "src/app/identity/repo.py"]
~~~
with:
~~~text
files: ["src/app/identity/service.py", "src/app/identity/repo.py", "src/app/refusals.py"]
~~~

#### E-2b.3 · ADU-PLAN.md:155
replace exactly:
~~~text
  - { unit: ADU-16, file: src/app/ports.py, assertion: "gains Refused(reason, detail, **extra), the one domain refusal (design/INTERFACES.md, Refused); nothing else in the module changes and tests/test_ports.py stays green unchanged", q: Q-07 }
~~~
with:
~~~text
  - { unit: ADU-00, file: tests/layering.json, assertion: "app.refusals joins the ports layer, so every layer that may import the ports may import Refused and app.refusals may import nothing of the product; test_layering.py stays green unchanged", q: Q-07 }
~~~

#### E-2b.4 · design/ARCHITECTURE.md:12
replace exactly (within the line):
~~~text
`src/app/ports.py`, `src/app/*/null_*.py`
~~~
with:
~~~text
`src/app/ports.py`, `src/app/refusals.py`, `src/app/*/null_*.py`
~~~

#### E-2b.5 · design/INTERFACES.md:80
replace exactly (within the line):
~~~text
in `src/app/ports.py` beside `MemberNotFound`, `AssignmentNotFound` and `TransferRefused` (D-p2; ADU-03 amends ADU-16's module)
~~~
with:
~~~text
in `src/app/refusals.py`, a layer-2 module of its own (D-p2; ADU-03's own file, joined to the ports layer in `tests/layering.json`)
~~~

#### E-2b.6 · DECISIONS.md:18
replace exactly (within the line):
~~~text
 in `src/app/ports.py` is the one domain refusal.**
~~~
with:
~~~text
 in `src/app/refusals.py`, a layer-2 module of its own, is the one domain refusal.**
~~~

#### E-2b.7 · DECISIONS.md:18
replace exactly (within the line):
~~~text
ADU-03 adds it to ADU-16's module by a declared amendment. | <apply-date>, operator (Part E of docs/PACK-q07-retire-amends.md); `src/app/ports.py` already holds the cross-domain exceptions (`MemberNotFound`, `AssignmentNotFound`, `TransferRefused`) and imports nothing of the product, so every service, the API and the CLI reach it without a forbidden edge (`tests/layering.json`);
~~~
with:
~~~text
The module is ADU-03's own file, joined to the ports layer in `tests/layering.json` by ADU-03's amendment of ADU-00's file. | <apply-date>, operator (Part E of docs/PACK-q07-retire-amends.md); a module of its own leaves ADU-16's module untouched, at the price of an ARCHITECTURE layer-row change and a layering amendment;
~~~

E-2b.8–E-2b.18 carry (b) into the texts that name the module or version ARCHITECTURE (R1 M-1). E-2b.8 and E-2b.9 apply whenever (b) is ruled. E-2b.10–E-2b.12 apply with E-5 (a), on the version texts E-5 (a) writes. E-2b.13–E-2b.18 apply with E-5 (b), which versions nothing else in ARCHITECTURE, so (b) alone moves it to v1.2.

#### E-2b.8 · OPEN-QUESTIONS.md:59
replace exactly (within the line):
~~~text
ADU-03 amends src/app/ports.py)
~~~
with:
~~~text
ADU-03 adds src/app/refusals.py and amends tests/layering.json)
~~~

#### E-2b.9 · VERSIONS.md:123
replace exactly (within the line):
~~~text
ADU-03 amends src/app/ports.py (Refused, D-p2);
~~~
with:
~~~text
ADU-03 adds src/app/refusals.py to its `files` and ADU-00 to its `depends`, and amends tests/layering.json (Refused, D-p2);
~~~

#### E-2b.10 · VERSIONS.md:125 (with E-5 (a); on the text E-5a.13 writes)
replace exactly (within the line):
~~~text
| design/ARCHITECTURE.md | 1.1 | 1.2 | §Layers: the service graph's cycles
~~~
with:
~~~text
| design/ARCHITECTURE.md | 1.1 | 1.2 | §Layers: the layer-2 row gains `src/app/refusals.py` (D-p2), and the service graph's cycles
~~~

#### E-2b.11 · design/ARCHITECTURE.md:2 (with E-5 (a); on the text E-5a.8 writes)
replace exactly (within the line):
~~~text
D-09 (the frontend toolchain), D-p3 (the request's session)
~~~
with:
~~~text
D-09 (the frontend toolchain), D-p2 (Refused's module), D-p3 (the request's session)
~~~

#### E-2b.12 · design/ARCHITECTURE.md:52 (with E-5 (a); on the text E-5a.9 writes)
replace exactly (within the line):
~~~text
· D-09 (the frontend toolchain) · D-p3
~~~
with:
~~~text
· D-09 (the frontend toolchain) · D-p2 (Refused's module) · D-p3
~~~

#### E-2b.13 · design/ARCHITECTURE.md:2 (with E-5 (b))
replace exactly (within the line):
~~~text
v1.1 · owned by the architect
~~~
with:
~~~text
v1.2 · owned by the architect
~~~

#### E-2b.14 · design/ARCHITECTURE.md:2 (with E-5 (b))
replace exactly (within the line):
~~~text
Rests on D-03..D-06 and D-09 (the frontend toolchain).
~~~
with:
~~~text
Rests on D-03..D-06, D-09 (the frontend toolchain) and D-p2 (Refused's module).
~~~

#### E-2b.15 · design/ARCHITECTURE.md:52 (with E-5 (b))
replace exactly (within the line):
~~~text
· D-09 (the frontend toolchain).
~~~
with:
~~~text
· D-09 (the frontend toolchain) · D-p2 (Refused's module).
~~~

#### E-2b.16 · VERSIONS.md:12 (with E-5 (b))
replace exactly:
~~~text
| design/ARCHITECTURE.md | 1.1 | architecture contract |
~~~
with:
~~~text
| design/ARCHITECTURE.md | 1.2 | architecture contract |
~~~

#### E-2b.17 · VERSIONS.md:120 (with E-5 (b))
replace exactly (within the line):
~~~text
ADU-PLAN v1.3, INTERFACES v1.1: Q-07
~~~
with:
~~~text
ADU-PLAN v1.3, INTERFACES v1.1, ARCHITECTURE v1.2: Q-07
~~~

#### E-2b.18 · VERSIONS.md:124 (with E-5 (b))
The block's replacement ends the INTERFACES row and adds the ARCHITECTURE row on a line of its own.
replace exactly (within the line):
~~~text
first row in Current |
~~~
with:
~~~text
first row in Current |
| design/ARCHITECTURE.md | 1.1 | 1.2 | §Layers: the layer-2 row gains `src/app/refusals.py` (D-p2); the header and §Decisions name D-p2: a requirement changed, hence the minor bump |
~~~

**3. The shape of `Refused`.**
[(a) recommended: `Refused(reason, detail="", **extra)`, since a refusal is {reason, detail, the extra fields a story names} (PRODUCT-DESIGN cross-cutting rules), and the service is the one that knows the plain truth to say
| (b) `Refused(reason, **extra)`, `TransferRefused`'s shape, with the API layer composing the Problem's detail from the reason and the extra fields — blocks E-3b.1–E-3b.4 below]

#### E-3b.1 · DECISIONS.md:18
replace exactly (within the line):
~~~text
**`Refused(reason, detail="", **extra)`
~~~
with:
~~~text
**`Refused(reason, **extra)`
~~~

#### E-3b.2 · DECISIONS.md:18
replace exactly (within the line):
~~~text
`reason` is a code of PRODUCT-DESIGN's Reason codes table, `detail` the plain sentence, `extra` the fields a story names;
~~~
with:
~~~text
`reason` is a code of PRODUCT-DESIGN's Reason codes table and `extra` the fields a story names (the API layer composes the Problem's detail);
~~~

#### E-3b.3 · design/INTERFACES.md:83
replace exactly:
~~~text
    def __init__(self, reason: str, detail: str = "", **extra: object) -> None   # .reason, .detail, .extra
~~~
with:
~~~text
    def __init__(self, reason: str, **extra: object) -> None   # .reason, .extra
~~~

#### E-3b.4 · design/INTERFACES.md:85
replace exactly (within the line):
~~~text
`detail` is the refusal's plain sentence and `extra` the fields a story names (`unfilled` for publish), because a refusal is {reason, detail, and the extra fields a story names} (PRODUCT-DESIGN, cross-cutting rules);
~~~
with:
~~~text
`extra` carries the fields a story names (`unfilled` for publish), and the API layer composes the Problem's detail from the reason and the extra fields;
~~~

E-3b.5 and E-3b.6 are (b)'s two consequential edits (R1 M-2). E-3b.5 applies only without E-2 (b), because E-2b.3 replaces the whole ports.py line.

#### E-3b.5 · ADU-PLAN.md:155 (without E-2 (b))
replace exactly (within the line):
~~~text
gains Refused(reason, detail, **extra)
~~~
with:
~~~text
gains Refused(reason, **extra)
~~~

#### E-3b.6 · design/INTERFACES.md:85
replace exactly (within the line):
~~~text
tests assert `.reason`, never `.detail` (the contract's
~~~
with:
~~~text
tests assert `.reason` (the contract's
~~~

**4. The composition-root test's name and the module docstring, which say "binds a Null per port".** Both are false from ADU-03 on.
[(a) recommended: ADU-03 renames the test to `test_the_composition_root_binds_an_implementation_per_port_and_an_injectable_clock` and rewords the docstring (T-03.5, T-03.1). The new name holds in every state, Nulls included, so no later unit renames again. `git grep` finds no other reference to the old name
| (b) both unchanged: the session drops T-03.1 and T-03.5, and B-3.3's conformance line loses its rename clause (block E-4b.1 below); the later conformance lines move up by 2 (T-09.2 :108, T-05.2 :106, T-07.2 :106; with E-1 (b) as well, by 4) — consequence: a test whose name states what is no longer true]

#### E-4b.1 · ADU-PLAN.md:152
replace exactly (within the line):
~~~text
; the composition-root test is renamed test_the_composition_root_binds_an_implementation_per_port_and_an_injectable_clock and the module docstring reads 'binds an implementation of each port (the Null until its provider lands)'
~~~
with:
~~~text
~~~

**5. The status of the questions this loop raises (B-5).**
Under either option Q-p5 is entered open and `**Blocking:** no`, as B-2.7 writes it. The duty to rule it before ADU-04 opens is an Owed row due ADU-04 (E-5a.14 or E-5b.1), with ADU-04's pointer (B-3.16). The reason is plugin FB-32: `adu status` lists every open `**Blocking:** yes` question as a STOP for whatever unit is Now (plugin scripts/adu.mjs:81–82), so a Q-p5 entered blocking would stop ADU-03 (R1 N-2, measured). The row's Approval cell names your ruling of this bracket. Q-p6 is ruled by E-10 under either option.
[(a) recommended, with E-6–E-9 ruled: Q-p1–Q-p4 are entered resolved by this apply, and of this loop's questions only Q-p5 stays open (and Q-p6, if E-10 (d) defers it). Each of Q-p1–Q-p4 is headed `resolved → D-p3` … `D-p6` (E-5a.2–E-5a.5), and its Resolution line is the one the option you rule in E-6–E-9 writes: the ruling, and where it now lives. Q-07's resolution says so (E-5a.1). The version lines follow (E-5a.6–E-5a.13): design/INTERFACES.md's header names D-p1–D-p6, and design/ARCHITECTURE.md goes from v1.1 to v1.2, because E-6 amends its line 42, E-7 its line 18 and E-8 its line 45, whichever options are ruled. E-5a.14 writes the Owed row. The four questions entered resolved keep their `**Blocking:** yes — for ADU-03` lines as the record of the question as raised; `adu status` reads a question's state first and lists no resolved one (measured on the simulated apply, B-4.4). ADU-03 is handed over after the apply: `adu status` then prints "Open blocking questions: none" with Now ADU-03 (B-4.4)
| (b) with none of E-6–E-9 ruled: Q-p1–Q-p4 enter open and blocking ADU-03, which is Now, so the global STOP of plugin FB-32 is the right one there. Q-p5 enters open and non-blocking, exactly as B-2.7 writes it. No E-6–E-9 block is applied, and of E-5 only E-5b.1, the Owed row. Q-07 is resolved by this apply, but ADU-03 opens only after you rule Q-p1–Q-p4 (in the oversight session, as Q-07 was), and their text is written by the next design-change loop. This is v1.0's recommendation]
A ruling of some but not all of E-6–E-9 stops the apply: there is no text for a section half settled and half open. v1.0's other option is withdrawn: Q-p1–Q-p4 non-blocking, with ADU-03 proceeding on the recommended options as its own assumption. With E-6–E-9 written out, ruling them costs no further loop, and the withdrawn option would leave ADU-03's session making four choices that ADU-04, ADU-09 and ADU-05 inherit.

#### E-5a.1 · OPEN-QUESTIONS.md:59
replace exactly (within the line):
~~~text
The IdentityService section's open points are Q-p1–Q-p4;
~~~
with:
~~~text
The IdentityService section's four open points, raised and ruled in the same loop, are resolved by this apply: Q-p1 → D-p3, Q-p2 → D-p4, Q-p3 → D-p5, Q-p4 → D-p6 (design/INTERFACES.md §Domain services and §IdentityService);
~~~

#### E-5a.2 · OPEN-QUESTIONS.md:61
replace exactly:
~~~text
### Q-p1 · 2026-11-08 · design-change loop Q-07 (IdentityService) · open
~~~
with:
~~~text
### Q-p1 · 2026-11-08 · design-change loop Q-07 (IdentityService) · resolved → D-p3
~~~

#### E-5a.3 · OPEN-QUESTIONS.md:68
replace exactly:
~~~text
### Q-p2 · 2026-11-08 · design-change loop Q-07 (IdentityService) · open
~~~
with:
~~~text
### Q-p2 · 2026-11-08 · design-change loop Q-07 (IdentityService) · resolved → D-p4
~~~

#### E-5a.4 · OPEN-QUESTIONS.md:75
replace exactly:
~~~text
### Q-p3 · 2026-11-08 · design-change loop Q-07 (IdentityService) · open
~~~
with:
~~~text
### Q-p3 · 2026-11-08 · design-change loop Q-07 (IdentityService) · resolved → D-p5
~~~

#### E-5a.5 · OPEN-QUESTIONS.md:82
replace exactly:
~~~text
### Q-p4 · 2026-11-08 · design-change loop Q-07 (IdentityService) · open
~~~
with:
~~~text
### Q-p4 · 2026-11-08 · design-change loop Q-07 (IdentityService) · resolved → D-p6
~~~

#### E-5a.6 · design/INTERFACES.md:2
replace exactly (within the line):
~~~text
v1.1 (design v1.7, D-02; Q-07: D-p1, D-p2)
~~~
with:
~~~text
v1.1 (design v1.7, D-02; Q-07: D-p1–D-p6)
~~~

#### E-5a.7 · design/ARCHITECTURE.md:2
replace exactly (within the line):
~~~text
v1.1 · owned by the architect
~~~
with:
~~~text
v1.2 · owned by the architect
~~~

#### E-5a.8 · design/ARCHITECTURE.md:2
replace exactly (within the line):
~~~text
Rests on D-03..D-06 and D-09 (the frontend toolchain).
~~~
with:
~~~text
Rests on D-03..D-06, D-09 (the frontend toolchain), D-p3 (the request's session) and D-p5 (the token and salt source).
~~~

#### E-5a.9 · design/ARCHITECTURE.md:52
replace exactly (within the line):
~~~text
· D-09 (the frontend toolchain).
~~~
with:
~~~text
· D-09 (the frontend toolchain) · D-p3 (the request's session) · D-p5 (the token and salt source).
~~~

#### E-5a.10 · VERSIONS.md:12
replace exactly:
~~~text
| design/ARCHITECTURE.md | 1.1 | architecture contract |
~~~
with:
~~~text
| design/ARCHITECTURE.md | 1.2 | architecture contract |
~~~

#### E-5a.11 · VERSIONS.md:120
replace exactly (within the line):
~~~text
— ADU-PLAN v1.3, INTERFACES v1.1: Q-07, D-p1, D-p2 — the retirement edits under grants, Refused, IdentityService
~~~
with:
~~~text
— ADU-PLAN v1.3, INTERFACES v1.1, ARCHITECTURE v1.2: Q-07, D-p1–D-p6 — the retirement edits under grants, Refused, IdentityService and its session, collaborators, token source and values
~~~

#### E-5a.12 · VERSIONS.md:124
replace exactly (within the line):
~~~text
open points Q-p1–Q-p4);
~~~
with:
~~~text
the session, the constructor and collaborators, the token and salt source and the returned values as ruled, D-p3–D-p6);
~~~

#### E-5a.13 · VERSIONS.md:124
The block's replacement ends the INTERFACES row and adds the ARCHITECTURE row on a line of its own.
replace exactly (within the line):
~~~text
first row in Current |
~~~
with:
~~~text
first row in Current |
| design/ARCHITECTURE.md | 1.1 | 1.2 | §Layers: the service graph's cycles name identity ↔ notifications (IR-10 / IR-04) beside the other two (with D-p4); §Persistence and concurrency rules: the request's session (D-p3), and the token and salt source as the one exception to "no randomness in the product" (D-p5); the header and §Decisions name the decisions it now rests on: a requirement changed, hence the minor bump |
~~~

#### E-5a.14 · STATUS.md:31
The Owed row (plugin FB-32). The block's replacement ends O-01's row and adds the new row on a line of its own, in the table's columns: O | Due | Where | Approval | Status.
replace exactly (within the line):
~~~text
| operator, 2026-11-07 17:37, release M1: "0-01 approved" | open |
~~~
with:
~~~text
| operator, 2026-11-07 17:37, release M1: "0-01 approved" | open |
| O-p1 | ADU-04 | Q-p5: the API units' wall on tests/api/test_contract_conformance.py and the helpers of src/app/api/contract_stubs.py is ruled in a design-change loop before ADU-04 opens (ADU-PLAN.md, ADU-04's pointer); Q-p5 is entered non-blocking because `adu status` reads `**Blocking:** yes` as a stop for every unit, not ADU-04 alone (plugin FB-32) | operator, <apply-date>: the ruling of E-5 (a) on docs/PACK-q07-retire-amends.md v1.2 (Q-p5 entered open and non-blocking, owed before ADU-04) | open |
~~~

#### E-5b.1 · STATUS.md:31
The same row as E-5a.14, with the Approval cell naming (b).
replace exactly (within the line):
~~~text
| operator, 2026-11-07 17:37, release M1: "0-01 approved" | open |
~~~
with:
~~~text
| operator, 2026-11-07 17:37, release M1: "0-01 approved" | open |
| O-p1 | ADU-04 | Q-p5: the API units' wall on tests/api/test_contract_conformance.py and the helpers of src/app/api/contract_stubs.py is ruled in a design-change loop before ADU-04 opens (ADU-PLAN.md, ADU-04's pointer); Q-p5 is entered non-blocking because `adu status` reads `**Blocking:** yes` as a stop for every unit, not ADU-04 alone (plugin FB-32) | operator, <apply-date>: the ruling of E-5 (b) on docs/PACK-q07-retire-amends.md v1.2 (Q-p5 entered open and non-blocking, owed before ADU-04) | open |
~~~

**6. How the IdentityService, bound once, reaches the request's session (Q-p1).** B-2.7 states the question in full. Each option's blocks complete design/INTERFACES.md §Domain services and §IdentityService (as B-2.3 leaves them), write D-p3, amend design/ARCHITECTURE.md:42, add the request path through the composition root's own directory to ADU-03's arm 1, and write Q-p1's resolution.
[(a) explicit: every IdentityService operation takes the session it runs in as its first parameter, and the MemberDirectory methods read through short sessions of their own — blocks E-6a.1–E-6a.9. There is no change to the ports, deps.py or db.py. The consequences: each request opens a second session for the directory's reads, and those reads see committed state only; the Notifier's and the transfer's writes in the caller's transaction get no mechanism, so ADU-09 and ADU-05 each need a design-change loop before they open (this apply enters no question for that: E-5 (a) enters Q-p5 alone). ADU-03's arm 1 gains the request path through the directory's own session (E-6a.9), which no gate test exercises before ADU-04 otherwise
| (b) recommended: a request-scoped current session — blocks E-6b.1–E-6b.10. `db.current_session()` answers it; the async dependency `deps.get_session` makes it current for a request, and `db.unit_of_work(engine)` for the operator's command and for tests. With none current, a method raises `db.NoCurrentSession`. The API layer commits a write before it answers. ADU-03 gains two `amends` lines, for src/app/db.py (ADU-01's) and src/app/api/deps.py (ADU-02's); neither is a test, so neither needs a grant, and the order is unchanged (B-4.3). ADU-03's arm 1 gains R1's clause (E-6b.10): a request carrying a token `sign_in` issued, through the directory `create_app(workspace=tmp_path)` binds, answers 501 not_built, and a method with no session current raises `db.NoCurrentSession`. A broken wiring of deps.py therefore fails ADU-03's own tests, where R1 measured a green gate with every authenticated request answering 500 (R1 N-1; rehearsed in B-4.3)
| (c) per-request construction — no text: it changes the shape of ADU-02's composition root (`app.state.ports` would hold factories) and with it the `isinstance` checks of ADU-02's completed test (tests/api/test_contract_conformance.py:105–118). This loop does not open that wall; choosing (c) stops the apply]

Under (b), outside a request (E-6b.1 states it in full; in short):
- **The seed command (ADU-11, `app seed-admin`)** builds the app with `create_app(workspace)` and calls `seed_admin` inside `with db.unit_of_work(db.engine_for(app.state.workspace)):`. The block commits when `seed_admin` returns, and the command then prints the id (exit 0). `Refused("team_not_empty")` rolls the block back, and the command prints the reason and exits 2.
- **A test of ADU-03** wraps each call in `with db.unit_of_work(db.engine_for(tmp_path)):` and reads back in a second unit of work. A refusal is asserted with `pytest.raises(Refused)` around the block, which leaves it rolled back. No test sets the ContextVar itself.
- **When no session is current**, every MemberDirectory and IdentityService method raises `db.NoCurrentSession` from `db.current_session()`. None opens a session quietly.

Measured. v1.0's probe (B-5) showed that a ContextVar set in a sync generator dependency is not visible to the endpoint. The probe below re-runs the case (b) recommends: an async generator dependency, the repository's own `app.db` engine, and real writes. It shows:
1. The current session is seen by a sync dependency (the shape of `require_caller`) and by the sync endpoint, and it is the very session `Depends(get_session)` gives.
2. A write committed in the endpoint persists. The session is opened on the event loop's thread, used and committed on a worker thread, and closed back on the loop's thread, with no SQLite thread error.
3. A refusal after a flush reaches the dependency, which rolls back: no row survives.
4. Outside any request, `NoCurrentSession` is raised.
5. With the default (request) scope, the dependency's exit runs after the response is returned. A raise there still answers 200, so the commit must come before the answer, never in the exit. With `scope="function"` the same raise answers 500.
6. Four concurrent requests (httpx `ASGITransport`) see four distinct sessions, each its own throughout.
7. The reset in the dependency's exit never fails.

The probe (scratch; the project's venv, `python -I probe_current_session.py C:\dev\team-rota <scratch>`):
~~~python
"""Scratch probe for the pack's E-6 (b): a request-scoped current session set by an async generator dependency.

Run with the project's venv, isolated, from any directory:  python -I probe_current_session.py <repo> <scratch-dir>
It imports the repository's own app.db and app.models (read-only) and writes only under <scratch-dir>.
"""

from __future__ import annotations

import asyncio
import contextvars
import sys
import threading
import time
from contextlib import contextmanager
from pathlib import Path

REPO, SCRATCH = Path(sys.argv[1]), Path(sys.argv[2])
sys.path.insert(0, str(REPO / "src"))

import fastapi  # noqa: E402
import httpx  # noqa: E402
import sqlalchemy  # noqa: E402
import starlette  # noqa: E402
from fastapi import Depends, FastAPI, Request  # noqa: E402
from fastapi.responses import JSONResponse  # noqa: E402
from fastapi.testclient import TestClient  # noqa: E402
from sqlalchemy import func, select  # noqa: E402

from app import db, models  # noqa: E402

# ---- the illustrative shape of E-6 (b) (scratch only; ADU-03 writes its own)
_CURRENT: contextvars.ContextVar = contextvars.ContextVar("app.db.current_session", default=None)


class NoCurrentSession(RuntimeError):
    pass


def current_session():
    s = _CURRENT.get()
    if s is None:
        raise NoCurrentSession("no session is current")
    return s


@contextmanager
def use_session(session):
    token = _CURRENT.set(session)
    try:
        yield session
    finally:
        _CURRENT.reset(token)  # raises ValueError if the exit runs in another Context


EVENTS: list[str] = []
ERRORS: list[str] = []
WORKSPACE = SCRATCH / "probe-workspace"
ENGINE = db.engine_for(WORKSPACE)


async def get_session(request: Request):
    session = db.session_for(ENGINE)
    EVENTS.append(f"dep-enter:{threading.current_thread().name}")
    try:
        with use_session(session):
            try:
                yield session
            except Exception as exc:
                EVENTS.append(f"dep-saw:{type(exc).__name__}")
                session.rollback()
                raise
            finally:
                EVENTS.append(f"dep-exit:{threading.current_thread().name}")
    except ValueError as exc:  # the reset in another Context
        ERRORS.append(f"reset: {exc}")
        raise
    finally:
        session.close()


def require_caller_like(session=Depends(get_session)) -> int:  # a sync dependency, as require_caller is
    return id(current_session())


class Refusal(Exception):
    pass


app = FastAPI()


@app.exception_handler(Refusal)
async def _refusal(_r: Request, _e: Refusal):
    return JSONResponse({"reason": "refused"}, 409)


@app.middleware("http")
async def mark_response(request: Request, call_next):
    response = await call_next(request)
    EVENTS.append("response-returned-to-middleware")
    return response


@app.get("/read")
def read(session=Depends(get_session), seen_by_dep: int = Depends(require_caller_like)) -> dict:
    cur = current_session()
    return {"endpoint_sees_current": cur is session, "sync_dependency_saw_same": seen_by_dep == id(session)}


@app.post("/write")
def write(session=Depends(get_session)) -> dict:
    n = current_session().scalar(select(func.count()).select_from(models.Member))
    current_session().add(models.Member(name=f"P{n}", email=f"p{n}@example.test", role="member",
                                        active=True, passcode_hash="x$y"))
    current_session().commit()  # the router commits before it answers (E-6 (b))
    EVENTS.append(f"endpoint-committed:{threading.current_thread().name}")
    return {"members": n + 1}


@app.post("/refuse")
def refuse(session=Depends(get_session)) -> dict:
    current_session().add(models.Member(name="R", email="r@example.test", role="member", active=True,
                                        passcode_hash="x$y"))
    current_session().flush()
    raise Refusal()


async def teardown_raises_request_scope(request: Request):
    yield "x"
    EVENTS.append("teardown(request scope) raising")
    raise RuntimeError("commit failed in teardown")


async def teardown_raises_function_scope(request: Request):
    yield "x"
    EVENTS.append("teardown(function scope) raising")
    raise RuntimeError("commit failed in teardown")


@app.get("/teardown-request")
def t_request(_=Depends(teardown_raises_request_scope)) -> dict:
    return {"ok": True}


@app.get("/teardown-function")
def t_function(_=Depends(teardown_raises_function_scope, scope="function")) -> dict:
    return {"ok": True}


@app.get("/slow")
def slow(session=Depends(get_session)) -> dict:
    mine = id(current_session())
    time.sleep(0.2)
    return {"same_after_sleep": id(current_session()) == mine == id(session), "id": mine}


def count_members() -> int:
    s = db.session_for(ENGINE)
    try:
        return s.scalar(select(func.count()).select_from(models.Member))
    finally:
        s.close()


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8")
    c = TestClient(app, raise_server_exceptions=False)
    print("fastapi", fastapi.__version__, "starlette", starlette.__version__, "sqlalchemy", sqlalchemy.__version__,
          "httpx", httpx.__version__, "python", sys.version.split()[0])

    EVENTS.clear()
    print("1 sync endpoint and sync dependency see the current session:", c.get("/read").json())
    print("  order:", EVENTS)

    EVENTS.clear()
    r1, r2 = c.post("/write"), c.post("/write")
    print("2 a write committed by the endpoint, real engine:", r1.status_code, r1.json(), r2.status_code, r2.json(),
          "| members in a fresh session:", count_members())
    print("  order:", EVENTS)

    EVENTS.clear()
    before = count_members()
    r = c.post("/refuse")
    print("3 a refusal after a flush:", r.status_code, r.json(), "| members before/after:", before, count_members())
    print("  order:", EVENTS)

    try:
        current_session()
        print("4 outside any request: a session is current (unexpected)")
    except NoCurrentSession as exc:
        print("4 outside any request: NoCurrentSession raised:", exc)

    EVENTS.clear()
    r = c.get("/teardown-request")
    print("5 teardown raises, default (request) scope -> client sees", r.status_code, r.text[:60])
    print("  order:", EVENTS)
    EVENTS.clear()
    r = c.get("/teardown-function")
    print("6 teardown raises, scope='function' -> client sees", r.status_code, r.text[:60])
    print("  order:", EVENTS)

    async def concurrent() -> list[dict]:
        transport = httpx.ASGITransport(app=app)
        async with httpx.AsyncClient(transport=transport, base_url="http://probe") as ac:
            rs = await asyncio.gather(*(ac.get("/slow") for _ in range(4)))
        return [x.json() for x in rs]

    rs = asyncio.run(concurrent())
    print("7 four concurrent requests:", [x["same_after_sleep"] for x in rs], "| distinct sessions:",
          len({x["id"] for x in rs}))
    print("errors from the reset in the dependency's exit:", ERRORS or "none")
    return 0


if __name__ == "__main__":
    sys.exit(main())
~~~
Output (stdout and stderr):
~~~text
C:\dev\team-rota-data\.venv\Lib\site-packages\fastapi\testclient.py:1: StarletteDeprecationWarning: Using `httpx` with `starlette.testclient` is deprecated; install `httpx2` instead.
  from starlette.testclient import TestClient as TestClient  # noqa
fastapi 0.162.0 starlette 1.10.0 sqlalchemy 2.1.8 httpx 0.28.1 python 3.12.13
1 sync endpoint and sync dependency see the current session: {'endpoint_sees_current': True, 'sync_dependency_saw_same': True}
  order: ['dep-enter:asyncio-portal-2168fa17380', 'response-returned-to-middleware', 'dep-exit:asyncio-portal-2168fa17380']
2 a write committed by the endpoint, real engine: 200 {'members': 1} 200 {'members': 2} | members in a fresh session: 2
  order: ['dep-enter:asyncio-portal-2168fac0c80', 'endpoint-committed:AnyIO worker thread', 'response-returned-to-middleware', 'dep-exit:asyncio-portal-2168fac0c80', 'dep-enter:asyncio-portal-2168fac02f0', 'endpoint-committed:AnyIO worker thread', 'response-returned-to-middleware', 'dep-exit:asyncio-portal-2168fac02f0']
3 a refusal after a flush: 409 {'reason': 'refused'} | members before/after: 2 2
  order: ['dep-enter:asyncio-portal-2168fb38770', 'dep-saw:Refusal', 'dep-exit:asyncio-portal-2168fb38770', 'response-returned-to-middleware']
4 outside any request: NoCurrentSession raised: no session is current
5 teardown raises, default (request) scope -> client sees 200 {"ok":true}
  order: ['response-returned-to-middleware', 'teardown(request scope) raising']
6 teardown raises, scope='function' -> client sees 500 Internal Server Error
  order: ['teardown(function scope) raising']
7 four concurrent requests: [True, True, True, True] | distinct sessions: 4
errors from the reset in the dependency's exit: none
~~~

#### E-6b.1 · design/INTERFACES.md:88
Why: the mechanism, its three owners and what happens with none (the operator's three points).
replace exactly (within the line):
~~~text
A point the arms, the domain spec and the contract do not settle is marked open with its question, never filled in.
~~~
with:
~~~text
A point the arms, the domain spec and the contract do not settle is marked open with its question, never filled in.

**The request's session (D-p3).** Every service, and every port implementation `src/app/main.py` binds, reads and writes in the current session, `db.current_session()`, and never opens, commits or closes one. With no session current, `db.current_session()` raises `db.NoCurrentSession`; a service method lets it propagate and never opens a session quietly. Exactly three owners make a session current:
- **A request.** `deps.get_session` is an async generator dependency. It opens the request's one session on `engine_of(request)`, makes it current with `db.use_session(session)` for the whole request, and yields it. On the way out it restores the previous current session and closes this one, which rolls back whatever was not committed. It is async because a ContextVar set in a sync dependency is not visible to the endpoint. `require_caller` depends on it, so `caller_for_token` reads the request's session. The API layer commits a write after the service returns and before it answers, never in the dependency's exit: FastAPI runs that exit after the response is sent, so a failure there would leave a 200 standing. Both behaviours are measured in docs/PACK-q07-retire-amends.md, Part E-6.
- **The operator's command.** `app seed-admin` (ADU-11) builds the app with `create_app(workspace)` and calls `seed_admin` inside `with db.unit_of_work(db.engine_for(app.state.workspace)):`. The block commits when `seed_admin` returns, and the command then prints the id (exit 0). `Refused("team_not_empty")` rolls the block back, and the command prints the reason and exits 2.
- **A test.** A service unit's tests (ADU-03's first) wrap each call in `with db.unit_of_work(db.engine_for(tmp_path)):` and read back in a second unit of work. A refusal is asserted with `pytest.raises(Refused)` around the block, which leaves it rolled back. No test sets the ContextVar itself; a test calls a service outside a unit of work only to assert `db.NoCurrentSession`.
```
# src/app/db.py gains (ADU-03, by amendment of ADU-01's module; layer 1, so every service, the API and the CLI reach it):
class NoCurrentSession(RuntimeError)
def current_session() -> Session                               # the current session; raises NoCurrentSession when none is
def use_session(session: Session) -> ContextManager[Session]    # current for the block, the previous one restored on exit; commits nothing
def unit_of_work(engine: Engine) -> ContextManager[Session]     # session_for(engine) made current; commits on return, rolls back on raise, closes
```
Invariants: one ContextVar, private to `src/app/db.py`. `use_session` restores the previous session with the token it set, so nested blocks and concurrent requests stay apart. `engine_for` and `session_for` do not change. The transfer (ADU-05) and the Notifier (ADU-09) write in the same current session, so a decision, its transfer and its notifications commit together (R-swaps-04).
~~~

#### E-6b.2 · design/INTERFACES.md:93
replace exactly (within the line):
~~~text
# implements MemberDirectory (above), and:
~~~
with:
~~~text
# implements MemberDirectory (above), and the operations below — every method in db.current_session() (D-p3):
~~~

#### E-6b.3 · design/INTERFACES.md:94
Under (b) the constructor takes no session, so the fragment goes; the class line above says where the session comes from.
replace exactly (within the line):
~~~text
 the request's session: Q-p1;
~~~
with:
~~~text
~~~

#### E-6b.4 · design/INTERFACES.md:112
replace exactly (within the line):
~~~text
| MemberDirectory | the six methods above over identity's own rows:
~~~
with:
~~~text
| MemberDirectory | the six methods above over identity's own rows, read in the current session (with none current, each raises db.NoCurrentSession; D-p3):
~~~

#### E-6b.5 · design/ARCHITECTURE.md:42
replace exactly (within the line):
~~~text
compute first (rules, overlap checks), then write; never hold the write across a computation.
~~~
with:
~~~text
compute first (rules, overlap checks), then write; never hold the write across a computation. That session is current for the whole request (D-p3). The async dependency `deps.get_session` makes it current; every service and port implementation reads and writes in `db.current_session()` and never opens, commits or closes one; and the API layer commits a write before it answers, never in the dependency's exit, which runs after the response is sent. The operator's command and the tests run in `db.unit_of_work(engine)`; with no session current a service raises `db.NoCurrentSession`.
~~~

#### E-6b.6 · ADU-PLAN.md:153
Why: ADU-03's roster must hold the two modules it edits (hard rule 6). Both are `files` of completed units, not tests, so the guard honours the `amends` without a grant (Part A-2, `scripts/adu.mjs:692–693`; rehearsed in B-4.3). ADU-01 and ADU-02 are already in ADU-03's `depends`, so the derived order does not change. The lines cite Q-07, since the plan may carry no provisional id.
replace exactly:
~~~text
  - { unit: ADU-16, file: src/app/identity/null_directory.py, assertion: "deleted (retires MK-04)", q: none }
~~~
with:
~~~text
  - { unit: ADU-01, file: src/app/db.py, assertion: "gains the current session of design/INTERFACES.md (Domain services): NoCurrentSession, current_session() (raises it when no session is current), use_session(session) and unit_of_work(engine) (commits on return, rolls back on raise, restores the previous session, closes); engine_for and session_for unchanged, and tests/test_models.py and tests/test_synthetic.py stay green unchanged", q: Q-07 }
  - { unit: ADU-02, file: src/app/api/deps.py, assertion: "get_session becomes an async generator dependency that opens the request's session, makes it current with db.use_session for the whole request, and on exit restores the previous one and closes it, rolling back what was not committed; require_caller depends on it, so caller_for_token reads the request's session; ProblemError, problem_response and engine_of unchanged; the session-sharing test of tests/api/test_contract_conformance.py stays green unchanged", q: Q-07 }
  - { unit: ADU-16, file: src/app/identity/null_directory.py, assertion: "deleted (retires MK-04)", q: none }
~~~

#### E-6b.7 · VERSIONS.md:123
replace exactly (within the line):
~~~text
the four retirement arms rewritten so they can be met;
~~~
with:
~~~text
ADU-03 amends src/app/db.py and src/app/api/deps.py (the request's current session, D-p3); the four retirement arms rewritten so they can be met;
~~~

#### E-6b.8 · DECISIONS.md:18
The DECISIONS blocks of E-6–E-9 share this anchor, the end of D-p2's row, and are applied E-9's first, so the rows stand D-p3, D-p4, D-p5, D-p6.
replace exactly (within the line):
~~~text
design/INTERFACES.md §Refused |
~~~
with:
~~~text
design/INTERFACES.md §Refused |
| D-p3 | **The request's session is the current session: every service and every port implementation reads and writes in `db.current_session()` and never opens, commits or closes one; with none current it raises `db.NoCurrentSession` and never opens one quietly.** A request makes its one session current in the async dependency `deps.get_session` (`db.use_session`), on which `require_caller` depends. The API layer commits a write after the service returns and before it answers. The operator's command and the tests run in `db.unit_of_work(engine)` (commit on return, rollback on raise). ADU-03 adds `NoCurrentSession`, `current_session`, `use_session` and `unit_of_work` to `src/app/db.py` (ADU-01's module) and rewrites `get_session` in `src/app/api/deps.py` (ADU-02's), both by declared amendment. The transfer (ADU-05) and the Notifier (ADU-09) write in the same session. | <apply-date>, operator: Q-p1 option (b), Part E-6 of docs/PACK-q07-retire-amends.md v1.2. It is the one mechanism that also serves the Notifier's and the transfer's writes in the caller's transaction (R-swaps-04; design/INTERFACES.md §SchedulingPort, §Notifier). Measured on fastapi 0.162.0 with the repository's engine: a ContextVar set in a sync dependency is not visible to the endpoint. Set in an async generator dependency, it is seen by sync dependencies and the endpoint, kept apart across concurrent requests and reset cleanly on exit. That exit runs after the response is sent (a raise there still answers 200), hence the commit before the answer. design/INTERFACES.md §Domain services; design/ARCHITECTURE.md §Persistence and concurrency rules |
~~~

#### E-6b.9 · OPEN-QUESTIONS.md:65
replace exactly:
~~~text
**Recommendation:** (b), ruled once for all four services: it is the only option that also serves the Notifier's and the transfer's atomic writes.
**Resolution:** none yet.
~~~
with:
~~~text
**Recommendation:** (b), ruled once for all four services: it is the only option that also serves the Notifier's and the transfer's atomic writes.
**Resolution:** option (b), the operator, <apply-date>, on Part E-6 of docs/PACK-q07-retire-amends.md v1.2 (verified in docs/VERIFICATION-<id>.md): the request's session is the current session. The async `deps.get_session` makes it current for a request, and `db.unit_of_work` for the operator's command and the tests. Every service reads it through `db.current_session()`, which raises `db.NoCurrentSession` when none is current. The API layer commits a write before it answers. It lives in D-p3, design/INTERFACES.md §Domain services (the request's session) and §IdentityService, design/ARCHITECTURE.md §Persistence and concurrency rules, and ADU-03's amends of src/app/db.py and src/app/api/deps.py (ADU-PLAN v1.3).
~~~

#### E-6b.10 · ADU-PLAN.md:161
Why: R1 N-1. E-6b.6's db.py and deps.py lines need an ADU-03 arm that fails when they are wired wrong. This is R1's clause, appended before the arm's closing quote. Its "under D-p3" is written as "under the request's current session of design/INTERFACES.md (Domain services)", because the plan may carry no provisional id (B-3; plugin scripts/lib/plan.mjs:160). The arm's file stays as E-10 rules it.
replace exactly (within the line):
~~~text
imports app.identity.null_directory; the contract unit's tests and tests/test_nulls.py pass in the gate after exactly the edits this entry's amends declare on them, each made under the operator's grant (Q-07)
~~~
with:
~~~text
imports app.identity.null_directory; the contract unit's tests and tests/test_nulls.py pass in the gate after exactly the edits this entry's amends declare on them, each made under the operator's grant (Q-07); under the request's current session of design/INTERFACES.md (Domain services), with the identity service bound by create_app(workspace=tmp_path), a request to a stubbed operation answers 501 not_built with Bearer <a token sign_in issued in that workspace> and 401 unauthenticated with Bearer garbage (require_caller reads the request's current session), and an IdentityService method called with no session current raises db.NoCurrentSession
~~~

#### E-6a.1 · design/INTERFACES.md:88
replace exactly (within the line):
~~~text
A point the arms, the domain spec and the contract do not settle is marked open with its question, never filled in.
~~~
with:
~~~text
A point the arms, the domain spec and the contract do not settle is marked open with its question, never filled in.

**The request's session (D-p3).** Every IdentityService operation takes the session it runs in as its first parameter after `self` (`session: Session`). It writes only in that session and never commits:
- The API layer passes the request's one session from `deps.get_session` and commits a write after the service returns and before it answers.
- The operator's command (ADU-11) opens `db.session_for(db.engine_for(app.state.workspace))` and passes it to `seed_admin`. It commits and prints the id; on `Refused("team_not_empty")` it rolls back, prints the reason and exits 2.
- A test passes a session it opened on `db.engine_for(tmp_path)`.

The MemberDirectory methods, whose signatures `src/app/ports.py` pins without a session (tests/test_ports.py:21), each open a short session of their own on `engine()`. They see committed state only, never the caller's uncommitted writes. There is no current session, so none can be missing. This does not serve the Notifier's and the transfer's writes in the caller's transaction (§SchedulingPort, §Notifier): ADU-09 and ADU-05 each settle their mechanism in a design-change loop before they open.
~~~

#### E-6a.2 · design/INTERFACES.md:93
replace exactly (within the line):
~~~text
# implements MemberDirectory (above), and:
~~~
with:
~~~text
# implements MemberDirectory (above; each method on a short session of its own, D-p3), and:
~~~

#### E-6a.3 · design/INTERFACES.md:94
The replacement starts with a line break: the fence's first line is empty.
replace exactly (within the line):
~~~text
 the request's session: Q-p1;
~~~
with:
~~~text

        engine: Callable[[], Engine],           # the workspace's engine, for the MemberDirectory methods' own short sessions
                                                #   (D-p3); main.py passes one that creates the engine once, as deps.engine_of does
~~~

#### E-6a.4 · design/INTERFACES.md:95
replace exactly:
~~~text
    def seed_admin(self, name: str, email: str, passcode: str) -> int
    def add_member(self, caller: Caller, name: str, email: str, role: str | None, passcode: str) -> MemberValue
    def change_role(self, caller: Caller, member_id: int, role: str | None) -> MemberValue
    def deactivate(self, caller: Caller, member_id: int) -> MemberValue
    def sign_in(self, email: str, passcode: str | None) -> SignInValue
    def list_members(self, caller: Caller) -> list[MemberSummary]
~~~
with:
~~~text
    def seed_admin(self, session: Session, name: str, email: str, passcode: str) -> int
    def add_member(self, session: Session, caller: Caller, name: str, email: str, role: str | None, passcode: str) -> MemberValue
    def change_role(self, session: Session, caller: Caller, member_id: int, role: str | None) -> MemberValue
    def deactivate(self, session: Session, caller: Caller, member_id: int) -> MemberValue
    def sign_in(self, session: Session, email: str, passcode: str | None) -> SignInValue
    def list_members(self, session: Session, caller: Caller) -> list[MemberSummary]
~~~

#### E-6a.5 · design/INTERFACES.md:112
replace exactly (within the line):
~~~text
| MemberDirectory | the six methods above over identity's own rows:
~~~
with:
~~~text
| MemberDirectory | the six methods above over identity's own rows, each read in a short session of its own on engine() (committed state only; D-p3):
~~~

#### E-6a.6 · design/ARCHITECTURE.md:42
replace exactly (within the line):
~~~text
compute first (rules, overlap checks), then write; never hold the write across a computation.
~~~
with:
~~~text
compute first (rules, overlap checks), then write; never hold the write across a computation. The IdentityService's operations take that session as a parameter, and the API layer commits a write before it answers. The MemberDirectory's reads are the one exception to one session per request: each runs in a short session of its own that sees committed state only (D-p3).
~~~

#### E-6a.7 · DECISIONS.md:18
replace exactly (within the line):
~~~text
design/INTERFACES.md §Refused |
~~~
with:
~~~text
design/INTERFACES.md §Refused |
| D-p3 | **Every IdentityService operation takes the session it runs in as its first parameter and never commits; the MemberDirectory methods, whose signatures the ports pin without a session (tests/test_ports.py:21), each read in a short session of their own on the workspace's engine and see committed state only.** The API layer passes the request's session from `deps.get_session` and commits a write before it answers; the operator's command and the tests pass a session they opened. The Notifier's and the transfer's writes in the caller's transaction are not served: ADU-09 and ADU-05 each settle theirs in a design-change loop before they open. | <apply-date>, operator: Q-p1 option (a), Part E-6 of docs/PACK-q07-retire-amends.md v1.2. No change to the ports, `src/app/api/deps.py` or `src/app/db.py`. The directory's reads are the one exception to one session per request (design/ARCHITECTURE.md §Persistence and concurrency rules); design/INTERFACES.md §Domain services |
~~~

#### E-6a.8 · OPEN-QUESTIONS.md:65
replace exactly:
~~~text
**Recommendation:** (b), ruled once for all four services: it is the only option that also serves the Notifier's and the transfer's atomic writes.
**Resolution:** none yet.
~~~
with:
~~~text
**Recommendation:** (b), ruled once for all four services: it is the only option that also serves the Notifier's and the transfer's atomic writes.
**Resolution:** option (a), the operator, <apply-date>, on Part E-6 of docs/PACK-q07-retire-amends.md v1.2 (verified in docs/VERIFICATION-<id>.md): every IdentityService operation takes its session as the first parameter, and the MemberDirectory methods read in short sessions of their own (committed state only). The Notifier's and the transfer's writes in the caller's transaction are left to ADU-09's and ADU-05's own loops. It lives in D-p3, design/INTERFACES.md §Domain services and §IdentityService, and design/ARCHITECTURE.md §Persistence and concurrency rules.
~~~

#### E-6a.9 · ADU-PLAN.md:161
Why: under (a) too, no gate test sends a token through the composition root's own directory before ADU-04 (R1 §5, N-1, last point). The clause is (a)'s form of E-6b.10's.
replace exactly (within the line):
~~~text
imports app.identity.null_directory; the contract unit's tests and tests/test_nulls.py pass in the gate after exactly the edits this entry's amends declare on them, each made under the operator's grant (Q-07)
~~~
with:
~~~text
imports app.identity.null_directory; the contract unit's tests and tests/test_nulls.py pass in the gate after exactly the edits this entry's amends declare on them, each made under the operator's grant (Q-07); with the identity service bound by create_app(workspace=tmp_path), a request to a stubbed operation answers 501 not_built with Bearer <a token sign_in issued in that workspace> and 401 unauthenticated with Bearer garbage (caller_for_token reads in a short session of its own on the workspace's engine)
~~~

**7. How the IdentityService receives its collaborators (Q-p2).** B-2.7 states the question in full. The arms name a clock, a SchedulingPort and a Notifier. Identity consumes scheduling (IR-05) and notifications (IR-10), and each of those consumes MemberDirectory (IR-06, IR-04): two cycles at the service level. Both design/ARCHITECTURE.md:18 ("two cycles (identity ↔ scheduling, scheduling ↔ swaps)") and design/INTERFACES.md:92 (post-B :129) omit identity ↔ notifications, so each option amends both (E-7a.5–.6, E-7b.4–.5, the same text in each). Each option's blocks also write the constructor's collaborator lines, D-p4 and Q-p2's resolution.
[(a) constructor values, `IdentityService(clock, scheduling, notifier, …)` — blocks E-7a.1–E-7a.6. ADU-09 and ADU-05 construct their services with the identity service and then set `identity.notifier` and `identity.scheduling` in main.py. The consequence is two attribute sets after construction, a seam that design/INTERFACES.md:82 ("each provider unit replaces its own line by amendment") does not describe; E-7a.4 names it in that heading (post-B :117)
| (b) recommended: the composition root's bindings, read at call time — `IdentityService(bound, …)`, where `bound` is a zero-argument callable answering an object with `.clock`, `.scheduling` and `.notifier` (`main.Ports`, read structurally), and main.py binds `IdentityService(lambda: app.state.ports, …)` — blocks E-7b.1–E-7b.5. Each provider still replaces only its own line, and no setter exists. v1.0 put this as "receives the composition root's `Ports` container". The container cannot be passed itself, because the service is built inside the container's own constructor (src/app/main.py:52–58); a callable answering it is the nearest form that keeps one line per port. Ruling (b) also rules the constructors of ADU-09's, ADU-05's and ADU-07's services: D-p4 says "Every later service is built the same way", which goes beyond Q-p2 as worded (the IdentityService alone)
| (c) the collaborators passed with each call — no text: every API call site would carry them, the arms do not suggest it, and ADU-04's and ADU-11's call shapes would change with it; choosing it stops the apply]

#### E-7b.1 · design/INTERFACES.md:94
The constructor is written across three fragments of this one line, E-7's, E-6's and E-8's; any option of each composes with any option of the others (B-4.3 composes all 16).
replace exactly (within the line):
~~~text
def __init__(self, ...)                     # collaborators the arms name: a Clock, a SchedulingPort (IR-05), a Notifier (IR-10); how they are given: Q-p2;
~~~
with:
~~~text
def __init__(
        self,
        bound: Callable[[], Bindings],          # the composition root's bindings, read at call time (D-p4): .clock (Clock),
                                                #   .scheduling (SchedulingPort, IR-05), .notifier (Notifier, IR-10); Bindings is a Protocol of those
                                                #   three in src/app/identity/service.py, which main.Ports satisfies, so identity never imports main;
                                                #   main.py binds IdentityService(lambda: app.state.ports, …); a test passes
                                                #   lambda: SimpleNamespace(clock=FixedClock(…), scheduling=FakeSchedulingPort(), notifier=SpyNotifier())
~~~

#### E-7b.2 · DECISIONS.md:18
replace exactly (within the line):
~~~text
design/INTERFACES.md §Refused |
~~~
with:
~~~text
design/INTERFACES.md §Refused |
| D-p4 | **A domain service receives the composition root's bindings, not its collaborators one by one: `IdentityService(bound, …)` takes a zero-argument callable answering an object with `.clock`, `.scheduling` and `.notifier` (`Bindings`, a Protocol in identity's service module that `main.Ports` satisfies, so identity never imports main), and reads them at call time.** The composition root binds `IdentityService(lambda: app.state.ports, …)`; a test passes `lambda: SimpleNamespace(clock=…, scheduling=…, notifier=…)` holding the doubles. Every later service is built the same way, so each provider unit still replaces only its own line in `src/app/main.py` and no cycle needs a setter. | <apply-date>, operator: Q-p2 option (b), Part E-7 of docs/PACK-q07-retire-amends.md v1.2. The service-level cycles identity ↔ scheduling (IR-05 / IR-06) and identity ↔ notifications (IR-10 / IR-04) are closed by reading the bindings at call time, not by construction order. design/INTERFACES.md §Composition root bindings ("each provider unit replaces its own line by amendment") and §IdentityService |
~~~

#### E-7b.3 · OPEN-QUESTIONS.md:72
replace exactly:
~~~text
**Recommendation:** (b).
**Resolution:** none yet.
~~~
with:
~~~text
**Recommendation:** (b).
**Resolution:** option (b), the operator, <apply-date>, on Part E-7 of docs/PACK-q07-retire-amends.md v1.2 (verified in docs/VERIFICATION-<id>.md): `IdentityService(bound, …)` takes a zero-argument callable answering the composition root's bindings (`.clock`, `.scheduling`, `.notifier`) and reads them at call time; main.py binds `IdentityService(lambda: app.state.ports, …)`. It lives in D-p4 and design/INTERFACES.md §IdentityService.
~~~

#### E-7b.4 · design/INTERFACES.md:129
replace exactly (within the line):
~~~text
identity ↔ scheduling (IR-05 / IR-06) and scheduling ↔ swaps (IR-01, IR-02 / IR-07) are cycles at the service level.
~~~
with:
~~~text
identity ↔ scheduling (IR-05 / IR-06), identity ↔ notifications (IR-10 / IR-04) and scheduling ↔ swaps (IR-01, IR-02 / IR-07) are cycles at the service level.
~~~

#### E-7b.5 · design/ARCHITECTURE.md:18
replace exactly (within the line):
~~~text
The service graph has two cycles (identity ↔ scheduling, scheduling ↔ swaps);
~~~
with:
~~~text
The service graph has three cycles (identity ↔ scheduling, identity ↔ notifications, scheduling ↔ swaps);
~~~

#### E-7a.1 · design/INTERFACES.md:94
replace exactly (within the line):
~~~text
def __init__(self, ...)                     # collaborators the arms name: a Clock, a SchedulingPort (IR-05), a Notifier (IR-10); how they are given: Q-p2;
~~~
with:
~~~text
def __init__(
        self,
        clock: Clock,                           # constructor values (D-p4): main.py passes the bound clock, SchedulingPort
        scheduling: SchedulingPort,             #   (IR-05) and Notifier (IR-10), a test the doubles; ADU-09 and ADU-05, whose services
        notifier: Notifier,                     #   consume MemberDirectory, then set identity.notifier / identity.scheduling in main.py
~~~

#### E-7a.2 · DECISIONS.md:18
replace exactly (within the line):
~~~text
design/INTERFACES.md §Refused |
~~~
with:
~~~text
design/INTERFACES.md §Refused |
| D-p4 | **`IdentityService(clock, scheduling, notifier, …)` receives its collaborators as constructor values.** The composition root passes the bound clock, SchedulingPort and Notifier; a test passes the doubles. ADU-09 and ADU-05, whose services consume MemberDirectory while identity consumes theirs, construct their service with the identity service and then set `identity.notifier` / `identity.scheduling` in `src/app/main.py`, each by its own `main.py` amendment. | <apply-date>, operator: Q-p2 option (a), Part E-7 of docs/PACK-q07-retire-amends.md v1.2. The cycles identity ↔ notifications (IR-10 / IR-04) and identity ↔ scheduling (IR-05 / IR-06) are closed by setting an attribute after construction, a seam design/INTERFACES.md §Composition root bindings names beside "each provider unit replaces its own line"; design/INTERFACES.md §IdentityService |
~~~

#### E-7a.3 · OPEN-QUESTIONS.md:72
replace exactly:
~~~text
**Recommendation:** (b).
**Resolution:** none yet.
~~~
with:
~~~text
**Recommendation:** (b).
**Resolution:** option (a), the operator, <apply-date>, on Part E-7 of docs/PACK-q07-retire-amends.md v1.2 (verified in docs/VERIFICATION-<id>.md): the clock, the SchedulingPort and the Notifier are constructor values; ADU-09 and ADU-05 set `identity.notifier` and `identity.scheduling` after construction in main.py. It lives in D-p4 and design/INTERFACES.md §IdentityService.
~~~

#### E-7a.4 · design/INTERFACES.md:117
replace exactly (within the line):
~~~text
each provider unit replaces its own line by amendment)
~~~
with:
~~~text
each provider unit replaces its own line by amendment; ADU-09 and ADU-05 also set `identity.notifier` and `identity.scheduling` on the identity service after constructing their own, D-p4)
~~~

#### E-7a.5 · design/INTERFACES.md:129
replace exactly (within the line):
~~~text
identity ↔ scheduling (IR-05 / IR-06) and scheduling ↔ swaps (IR-01, IR-02 / IR-07) are cycles at the service level.
~~~
with:
~~~text
identity ↔ scheduling (IR-05 / IR-06), identity ↔ notifications (IR-10 / IR-04) and scheduling ↔ swaps (IR-01, IR-02 / IR-07) are cycles at the service level.
~~~

#### E-7a.6 · design/ARCHITECTURE.md:18
replace exactly (within the line):
~~~text
The service graph has two cycles (identity ↔ scheduling, scheduling ↔ swaps);
~~~
with:
~~~text
The service graph has three cycles (identity ↔ scheduling, identity ↔ notifications, scheduling ↔ swaps);
~~~

**8. Where a salt and a bearer token come from (Q-p3).** B-2.7 states the question in full. Each option's blocks write the constructor's source line, amend design/ARCHITECTURE.md:45, write D-p5 and Q-p3's resolution.
[(a) recommended: a `TokenSource` passed to the IdentityService — blocks E-8a.1–E-8a.4. The product's `SecretsSource` draws from the standard library's `secrets` (`token_urlsafe(32)`, `token_hex(8)`), and a test passes a deterministic source. There is no new dependency. ARCHITECTURE.md:45 gains the one exception. v1.0's wording, "never `random`", is narrowed to "a credential never comes from `random`", because `src/app/synthetic.py`, which is product code at layer 1, rightly takes a `random.Random(seed)`
| (b) a `random.Random` passed in, the synthetic generator's pattern; the composition root passes `random.Random()` (seeded from the OS), a test a seeded one — blocks E-8b.1–E-8b.4. The consequence: Python's Mersenne Twister state can be recovered from enough of its outputs (624 32-bit words), so a member who collects their own tokens can predict other members' tokens. That is unacceptable for a credential. The adapter's opt-in determinism scan (plugin `adapters/python-fastapi-uv/determinism_scan.py`) is not enabled (`adu.toml` `[adapter]` has only `name`). Enabled, it would fail on `random` in the package under (b), but also today, on src/app/synthetic.py:70, so it does not tell (b) from the rest
| (c) a salt derived from the email and a token derived by HMAC from a configured secret — no text: it needs an operator-held secret the design does not have (where it is configured, who holds it, how it is rotated), which is the operator's to define, not a mechanism this pack can write; choosing it stops the apply]

#### E-8a.1 · design/INTERFACES.md:94
The replacement starts with a line break: the fence's first line is empty.
replace exactly (within the line):
~~~text
 the token and salt source: Q-p3 (all open)
~~~
with:
~~~text

        source: TokenSource,                    # the token and the salt (D-p5): TokenSource is a Protocol in src/app/identity/service.py,
                                                #   token() -> str and salt() -> str; the product's SecretsSource (same module) answers
                                                #   secrets.token_urlsafe(32) and secrets.token_hex(8); main.py passes SecretsSource(), a test a
                                                #   deterministic source; seed_admin and add_member store models.hash_passcode(passcode, source.salt());
                                                #   sign_in stores source.token() as the member's one token and checks a passcode by recomputing
                                                #   models.hash_passcode with the stored salt (the text before '$'), compared with hmac.compare_digest
    ) -> None
~~~

#### E-8a.2 · design/ARCHITECTURE.md:45
replace exactly (within the line):
~~~text
No randomness in the product;
~~~
with:
~~~text
No randomness in the product except identity's token and salt source: the composition root passes the IdentityService a `TokenSource`, and the product's (`SecretsSource`) draws from the standard library's `secrets` (D-p5); a credential never comes from `random`;
~~~

#### E-8a.3 · DECISIONS.md:18
replace exactly (within the line):
~~~text
design/INTERFACES.md §Refused |
~~~
with:
~~~text
design/INTERFACES.md §Refused |
| D-p5 | **Identity's bearer tokens and passcode salts come from a source passed to the IdentityService; the product's draws from the standard library's `secrets`.** `IdentityService(…, source)` takes a `TokenSource` (`token() -> str`, `salt() -> str`). The composition root passes `SecretsSource()` (`secrets.token_urlsafe(32)`, `secrets.token_hex(8)`, in `src/app/identity/service.py`), and a test passes a deterministic source. It is the one exception to "no randomness in the product" (design/ARCHITECTURE.md §Persistence and concurrency rules); a credential never comes from `random`. | <apply-date>, operator: Q-p3 option (a), Part E-8 of docs/PACK-q07-retire-amends.md v1.2. No new dependency (D-03; D-04: the salted SHA-256 from the standard library). CLAUDE.md hard rule 5 ("randomness only through a passed generator where the adapter says so"): the source is passed, and the adapter names no other source (its determinism scan is opt-in and not enabled: `adu.toml` `[adapter]` has only `name`). A seeded generator's tokens are predictable (Q-p3 (b)). design/INTERFACES.md §IdentityService |
~~~

#### E-8a.4 · OPEN-QUESTIONS.md:78
The block starts at the Options line: the Recommendation and Resolution lines of Q-p3 and Q-p4 are identical, so only the Options line makes the text unique.
replace exactly:
~~~text
**Options:** (a) the service takes a token-and-salt source in its constructor; the composition root passes one built on the standard library's `secrets` (no new dependency), tests pass a deterministic one, and a DECISIONS row amends ARCHITECTURE.md:45 to "no randomness in the product except the injected token and salt source (`secrets`); never `random`". (b) a seeded `random.Random` passed in, the synthetic generator's pattern. Consequence: reproducible, but a bearer token becomes guessable from the seed, which is unacceptable for a credential. (c) a deterministic salt (from the email) and a token derived by HMAC from a configured secret. Consequence: no randomness, but the secret is an operator-held configuration the design does not mention.
**Recommendation:** (a).
**Resolution:** none yet.
~~~
with:
~~~text
**Options:** (a) the service takes a token-and-salt source in its constructor; the composition root passes one built on the standard library's `secrets` (no new dependency), tests pass a deterministic one, and a DECISIONS row amends ARCHITECTURE.md:45 to "no randomness in the product except the injected token and salt source (`secrets`); never `random`". (b) a seeded `random.Random` passed in, the synthetic generator's pattern. Consequence: reproducible, but a bearer token becomes guessable from the seed, which is unacceptable for a credential. (c) a deterministic salt (from the email) and a token derived by HMAC from a configured secret. Consequence: no randomness, but the secret is an operator-held configuration the design does not mention.
**Recommendation:** (a).
**Resolution:** option (a), the operator, <apply-date>, on Part E-8 of docs/PACK-q07-retire-amends.md v1.2 (verified in docs/VERIFICATION-<id>.md): a `TokenSource` passed to the IdentityService. The product's `SecretsSource` draws from the standard library's `secrets`, and tests pass a deterministic source. It lives in D-p5, design/INTERFACES.md §IdentityService and design/ARCHITECTURE.md §Persistence and concurrency rules (the one exception to "no randomness in the product").
~~~

#### E-8b.1 · design/INTERFACES.md:94
The replacement starts with a line break: the fence's first line is empty.
replace exactly (within the line):
~~~text
 the token and salt source: Q-p3 (all open)
~~~
with:
~~~text

        rng: random.Random,                     # the token and the salt (D-p5): salt f"{rng.randrange(16**8):08x}" (the fixture's shape),
                                                #   token f"tok_{rng.randrange(16**32):032x}"; main.py passes random.Random() (seeded from the OS),
                                                #   a test random.Random(<seed>); seed_admin and add_member store models.hash_passcode(passcode, salt);
                                                #   sign_in stores the token as the member's one token and checks a passcode by recomputing
                                                #   models.hash_passcode with the stored salt (the text before '$'), compared with hmac.compare_digest
    ) -> None
~~~

#### E-8b.2 · design/ARCHITECTURE.md:45
replace exactly (within the line):
~~~text
No randomness in the product;
~~~
with:
~~~text
No randomness in the product except the `random.Random` the composition root passes the IdentityService for its tokens and salts (D-p5);
~~~

#### E-8b.3 · DECISIONS.md:18
replace exactly (within the line):
~~~text
design/INTERFACES.md §Refused |
~~~
with:
~~~text
design/INTERFACES.md §Refused |
| D-p5 | **Identity's bearer tokens and passcode salts come from a `random.Random` passed to the IdentityService.** The composition root passes `random.Random()` (seeded from the OS), and a test passes `random.Random(<seed>)`. A salt is eight hex digits, as the fixture's are, and a token is `tok_` and 32 hex digits. It is the one exception to "no randomness in the product" (design/ARCHITECTURE.md §Persistence and concurrency rules). | <apply-date>, operator: Q-p3 option (b), Part E-8 of docs/PACK-q07-retire-amends.md v1.2. It follows the synthetic generator's pattern and needs no new dependency. Accepted with its consequence: the generator's state can be recovered from enough of its outputs, so tokens are predictable to a member who collects their own. design/INTERFACES.md §IdentityService |
~~~

#### E-8b.4 · OPEN-QUESTIONS.md:78
replace exactly:
~~~text
**Options:** (a) the service takes a token-and-salt source in its constructor; the composition root passes one built on the standard library's `secrets` (no new dependency), tests pass a deterministic one, and a DECISIONS row amends ARCHITECTURE.md:45 to "no randomness in the product except the injected token and salt source (`secrets`); never `random`". (b) a seeded `random.Random` passed in, the synthetic generator's pattern. Consequence: reproducible, but a bearer token becomes guessable from the seed, which is unacceptable for a credential. (c) a deterministic salt (from the email) and a token derived by HMAC from a configured secret. Consequence: no randomness, but the secret is an operator-held configuration the design does not mention.
**Recommendation:** (a).
**Resolution:** none yet.
~~~
with:
~~~text
**Options:** (a) the service takes a token-and-salt source in its constructor; the composition root passes one built on the standard library's `secrets` (no new dependency), tests pass a deterministic one, and a DECISIONS row amends ARCHITECTURE.md:45 to "no randomness in the product except the injected token and salt source (`secrets`); never `random`". (b) a seeded `random.Random` passed in, the synthetic generator's pattern. Consequence: reproducible, but a bearer token becomes guessable from the seed, which is unacceptable for a credential. (c) a deterministic salt (from the email) and a token derived by HMAC from a configured secret. Consequence: no randomness, but the secret is an operator-held configuration the design does not mention.
**Recommendation:** (a).
**Resolution:** option (b), the operator, <apply-date>, on Part E-8 of docs/PACK-q07-retire-amends.md v1.2 (verified in docs/VERIFICATION-<id>.md): a `random.Random` passed to the IdentityService, `random.Random()` in the product and a seeded one in tests, accepted with the predictability its consequence states. It lives in D-p5, design/INTERFACES.md §IdentityService and design/ARCHITECTURE.md §Persistence and concurrency rules.
~~~

**9. What the IdentityService answers, and where the values live (Q-p4).** B-2.7 states the question in full. One more fact belongs with it: design/PRODUCT-DESIGN.md:18 was added by DESIGN-REVIEW-7 finding 9 (design/DESIGN-REVIEW-7.md:36, which calls it line 17) so that the contract would read the write answers rather than invent them. The contract, cut afterwards, answers `Member` with the email (contracts/openapi.yaml:104, :144, :178). Only an admin calls the three writes (R-identity-08), and sign-in answers the signed-in member's own row, so the email reaches nobody the team list hides it from (R-identity-09). Each option's blocks complete the values comment of §IdentityService and write D-p6 and Q-p4's resolution.
[(a) recommended: the contract wins, and the values are frozen dataclasses in src/app/identity/service.py — `MemberValue` (the contract's Member) from add_member, change_role and deactivate; `SignInValue` (token, member) from sign_in; `MemberSummary` from list_members — blocks E-9a.1–E-9a.3. The names are those B-2.3 already uses
| (b) the design wins: the writes answer MemberSummary and the contract's three Member responses lose `email` — no text: it is a breaking contract change (D-07), which needs a design-change loop of its own and a regenerated golden, and this pack changes no pin; choosing it stops the apply
| (c) the contract wins, and the values are plain dicts with exactly the contract's keys (`MemberValue` and the rest are aliases of `dict[str, object]`), answered by the API unchanged — blocks E-9c.1–E-9c.3. The consequence: no type checks a key, so a missing or misspelt one shows only in ADU-04's conformance check, and every other in-process value of this product is a frozen dataclass (src/app/ports.py)]

**The editorial note on design/PRODUCT-DESIGN.md:18, under (a) or (c).** It is the pm-lead's edit, not the architect's and not the apply's. The pm-lead owns PRODUCT-DESIGN (D-02), and D-p6 records that the contract supersedes the line until the edit is made. It is not in this apply: the release manager does not apply E-9.P. It aligns the sentence with what the contract, pinned by the golden, already answers, but it also changes what the design text says a write answers. That may make it a requirement change, a minor bump to v1.8 by VERSIONS.md:4, rather than an editorial v1.7.1; which one is the pm-lead's call. The pm-lead may word it otherwise, as long as it says what D-p6 says. It blocks nothing: ADU-03 and ADU-04 follow D-p6.

#### E-9a.1 · design/INTERFACES.md:102
replace exactly (within the line):
~~~text
Their names, types and home: Q-p4 (open).
~~~
with:
~~~text
All three are frozen dataclasses (`@dataclass(frozen=True)`) defined in src/app/identity/service.py beside the service; no other domain consumes them in process (D-05), and the API layer maps them onto the contract's Member, Token and MemberSummary (D-p6).
~~~

#### E-9a.2 · DECISIONS.md:18
replace exactly (within the line):
~~~text
design/INTERFACES.md §Refused |
~~~
with:
~~~text
design/INTERFACES.md §Refused |
| D-p6 | **The IdentityService answers the contract's shapes as frozen values defined in `src/app/identity/service.py`: `MemberValue` (id, name, email, role, active — the contract's Member) from add_member, change_role and deactivate; `SignInValue` (token, member: MemberValue — the contract's Token) from sign_in; `MemberSummary` (id, name, role, active) from list_members; seed_admin answers the new id.** The API layer maps them onto the contract's schemas; no other domain consumes them in process (D-05). design/PRODUCT-DESIGN.md:18, "a member as the team list shows it", is superseded by the contract's Member: a write answers the member's row with the email (the contract comes before the design in CLAUDE.md's document authority, 6 before 7). The pm-lead rewords that line in a patch of PRODUCT-DESIGN, outside this apply. | <apply-date>, operator: Q-p4 option (a), Part E-9 of docs/PACK-q07-retire-amends.md v1.2. The contract wins because ADU-02's golden pins it (contracts/openapi.yaml:104, :144, :178 answer Member, and :44 Token; D-07: a breaking change is a design-change loop). Only an admin calls the three writes, and sign-in answers the caller's own row, so no email reaches anyone the team list hides it from (R-identity-08, R-identity-09). design/INTERFACES.md §IdentityService |
~~~

#### E-9a.3 · OPEN-QUESTIONS.md:85
The block starts at the Options line, for the reason E-8a.4 gives.
replace exactly:
~~~text
**Options:** (a) the contract wins, since ADU-02's golden pins it: the service returns a frozen value with the contract Member's fields for the three writes, (token, that value) for sign_in, and MemberSummary for list_members, all defined in src/app/identity/service.py (no other domain consumes them in process, D-05); PRODUCT-DESIGN.md:18 is read as "the member's row", and the pm-lead rewords it editorially. (b) the design wins: the writes answer MemberSummary, and the contract's three Member responses lose `email`. Consequence: a breaking contract change (D-07), so a design-change loop and a regenerated golden.
**Recommendation:** (a).
**Resolution:** none yet.
~~~
with:
~~~text
**Options:** (a) the contract wins, since ADU-02's golden pins it: the service returns a frozen value with the contract Member's fields for the three writes, (token, that value) for sign_in, and MemberSummary for list_members, all defined in src/app/identity/service.py (no other domain consumes them in process, D-05); PRODUCT-DESIGN.md:18 is read as "the member's row", and the pm-lead rewords it editorially. (b) the design wins: the writes answer MemberSummary, and the contract's three Member responses lose `email`. Consequence: a breaking contract change (D-07), so a design-change loop and a regenerated golden.
**Recommendation:** (a).
**Resolution:** option (a), the operator, <apply-date>, on Part E-9 of docs/PACK-q07-retire-amends.md v1.2 (verified in docs/VERIFICATION-<id>.md): the contract wins. The values are `MemberValue` (the contract's Member) from the three writes, `SignInValue` (token, member) from sign_in and `MemberSummary` from list_members, all frozen dataclasses in src/app/identity/service.py. It lives in D-p6 and design/INTERFACES.md §IdentityService. PRODUCT-DESIGN.md:18 is superseded, as D-p6 says, until the pm-lead's patch (E-9.P of the pack), which is not part of this apply.
~~~

#### E-9c.1 · design/INTERFACES.md:102
replace exactly (within the line):
~~~text
Their names, types and home: Q-p4 (open).
~~~
with:
~~~text
All three are plain dicts with exactly those keys, the contract's JSON names (aliases of dict[str, object] in src/app/identity/service.py); the API layer answers them unchanged (D-p6).
~~~

#### E-9c.2 · DECISIONS.md:18
replace exactly (within the line):
~~~text
design/INTERFACES.md §Refused |
~~~
with:
~~~text
design/INTERFACES.md §Refused |
| D-p6 | **The IdentityService answers the contract's shapes as plain dicts with exactly the contract's keys: `MemberValue` ({id, name, email, role, active}) from add_member, change_role and deactivate; `SignInValue` ({token, member}) from sign_in; `MemberSummary` ({id, name, role, active}) from list_members — aliases of `dict[str, object]` in `src/app/identity/service.py`; seed_admin answers the new id.** The API layer answers them unchanged. design/PRODUCT-DESIGN.md:18 is superseded by the contract's Member: a write answers the member's row with the email (the contract comes before the design in CLAUDE.md's document authority, 6 before 7). The pm-lead rewords that line in a patch of PRODUCT-DESIGN, outside this apply. | <apply-date>, operator: Q-p4 option (c), Part E-9 of docs/PACK-q07-retire-amends.md v1.2. The contract wins, as in option (a). No type checks a key, so a missing or misspelt one shows only in ADU-04's conformance check; every other in-process value of this product is a frozen dataclass (src/app/ports.py). design/INTERFACES.md §IdentityService |
~~~

#### E-9c.3 · OPEN-QUESTIONS.md:85
replace exactly:
~~~text
**Options:** (a) the contract wins, since ADU-02's golden pins it: the service returns a frozen value with the contract Member's fields for the three writes, (token, that value) for sign_in, and MemberSummary for list_members, all defined in src/app/identity/service.py (no other domain consumes them in process, D-05); PRODUCT-DESIGN.md:18 is read as "the member's row", and the pm-lead rewords it editorially. (b) the design wins: the writes answer MemberSummary, and the contract's three Member responses lose `email`. Consequence: a breaking contract change (D-07), so a design-change loop and a regenerated golden.
**Recommendation:** (a).
**Resolution:** none yet.
~~~
with:
~~~text
**Options:** (a) the contract wins, since ADU-02's golden pins it: the service returns a frozen value with the contract Member's fields for the three writes, (token, that value) for sign_in, and MemberSummary for list_members, all defined in src/app/identity/service.py (no other domain consumes them in process, D-05); PRODUCT-DESIGN.md:18 is read as "the member's row", and the pm-lead rewords it editorially. (b) the design wins: the writes answer MemberSummary, and the contract's three Member responses lose `email`. Consequence: a breaking contract change (D-07), so a design-change loop and a regenerated golden.
**Recommendation:** (a).
**Resolution:** option (c), the operator, <apply-date>, on Part E-9 of docs/PACK-q07-retire-amends.md v1.2 (verified in docs/VERIFICATION-<id>.md): the contract wins, and the values are plain dicts with exactly the contract's keys. It lives in D-p6 and design/INTERFACES.md §IdentityService. PRODUCT-DESIGN.md:18 is superseded, as D-p6 says, until the pm-lead's patch (E-9.P of the pack), which is not part of this apply.
~~~

#### E-9.P · design/PRODUCT-DESIGN.md:18 (the pm-lead's text; not applied by this apply)
Proposed wording for the pm-lead's patch of PRODUCT-DESIGN (v1.7.1 if editorial, v1.8 if a requirement changed: the pm-lead's call), under E-9 (a) or (c).
replace exactly (within the line):
~~~text
a member as the team list shows it (the same-role no-op answers the unchanged row, 200)
~~~
with:
~~~text
a member as the contract's Member gives it — the team list's fields and the email, which only the admin who made the change receives (the same-role no-op answers the unchanged row, 200)
~~~

**10. The four service units' test files of one basename (Q-p6; plugin FB-33).** Found by verification R1 (docs/VERIFICATION-R1.md §6), outside v1.1's text; B-2.7 enters the question in full. ADU-03, ADU-09, ADU-05 and ADU-07 each place a test file at `tests/<domain>/test_service.py` (ADU-PLAN.md:149, :180, :206, :238). tests/ holds no `__init__.py`, and pyproject.toml sets no import mode. Measured in B-4.3 on the 7d1e7d4 tree, with one stand-in test in each of the four files: as planned, 3 errors ("import file mismatch"); under (a), 50 passed; under (b), 50 passed; under (c), set in pyproject.toml as its block writes it, 50 passed. ADU-09 is the first to meet it. E-10 is ruled with every apply, whatever E-5 says. Each option's blocks write its plan text, its VERSIONS fragments and Q-p6's resolution (or, under (d), its ruling); (a), (b) and (c) also write D-p7. D-p7 shares the DECISIONS anchor of E-6–E-9 and goes first, so it stands last.
[(a) recommended: unique basenames — `tests/identity/test_identity_service.py`, `tests/notifications/test_notifications_service.py`, `tests/scheduling/test_scheduling_service.py`, `tests/swaps/test_swaps_service.py` — blocks E-10a.1–E-10a.34. The `tests:` line and every arm's `file` of the four entries are renamed (E-10a.1–.28); nothing else in the plan changes
| (b) packages: each of the four units' `files:` gains `tests/<domain>/__init__.py`, so pytest imports the files as `identity.test_service`, `notifications.test_service` and so on — blocks E-10b.1–E-10b.11. E-10b.1 applies without E-2 (b); with it, E-10b.2 adds the file after `src/app/refusals.py`
| (c) the import mode: ADU-03 amends ADU-00's pyproject.toml so `[tool.pytest.ini_options]` gains `addopts = "--import-mode=importlib"`, and ADU-03's `depends` gains ADU-00 — blocks E-10c.1–E-10c.8. Plan check derives `depends` from the `amends` (plugin scripts/lib/plan.mjs:181); under E-2 (b), E-2b.1 already adds ADU-00, so E-10c.1 applies only without it
| (d) deferred: Q-p6 stays open and non-blocking. An Owed row O-p2 due ADU-09 (E-10d.1) and a pointer under ADU-09's entry (E-10d.2) carry the duty to rule it in a design-change loop before ADU-09 opens (plugin FB-32) — blocks E-10d.1–E-10d.6]
Not offered: the plugin's own fix (FB-33: a plan-check rule on basenames, a naming rule in cut-adus, or importlib in the scaffold). It changes the plugin, not this repository, and the four paths would still need one of (a)–(c).

What each option changes:

| | (a) rename | (b) `__init__.py` | (c) importlib | (d) defer |
|---|---|---|---|---|
| `tests:` lines | ADU-03, ADU-09, ADU-05, ADU-07: the service file renamed (4 lines) | unchanged | unchanged | unchanged |
| arms' `file:` | 24 arms renamed: ADU-03 7, ADU-09 4, ADU-05 7, ADU-07 6 | unchanged | unchanged | unchanged |
| `files:`, `depends`, `amends` | unchanged | each `files:` gains `tests/<domain>/__init__.py` (ADU-09, size S, reaches its cap of 3) | ADU-03's `amends` gains pyproject.toml, its `depends` ADU-00 | unchanged |
| other plan lines | none | none | none | ADU-09's pointer (E-10d.2) |
| T-blocks (B-2.T) | unchanged: they edit only the conformance test and test_nulls.py | unchanged | unchanged | unchanged |
| a completed unit's file | none | none | ADU-00's pyproject.toml, by a declared amendment | none now; a later rename would edit ADU-03's completed test |
| a protected path | none | none | none (adu.toml `[protected]`: adu.toml, PINS.lock, .claude/settings.json, CLAUDE.md, src/app/ledger.py) | none |
| a grant | none | none | none: pyproject.toml is not a test, and the guard honours `amends` on a non-test file (plugin scripts/adu.mjs:692–693; asked in B-4.3) | none now; one later, if that loop renames ADU-03's file |
| the derived order | unchanged | unchanged | unchanged (ADU-00 is first) | unchanged |
| the 46 completed tests | untouched | untouched (none sits in the new packages) | all imported in importlib mode from ADU-03 on (measured: 46 passed) | untouched |
| plugin FB-33's proposed check (two `tests:` paths of one basename fail plan check) | passes | fails, unless the check learns packages | passes, by its import-mode exception | fails |

**Recommendation: (a).**
1. It edits plan text only, of four units not yet built. It touches no completed unit's file, no protected path and no existing test, and needs no grant. (b) is as light, but (c) amends ADU-00's pyproject.toml, and (d) leaves a rename of a completed test for later.
2. Unique basenames collect under every import mode: pytest's default, importlib, with packages or without. They pass the check plugin FB-33 proposes and follow its naming (`test_<domain>_<role>.py`). Under (b) and (c), four files keep one basename, which that check would refuse unless it learns their exception; (d) meets the error at ADU-09.
3. It is cheapest now. Before ADU-03 opens, none of the four files exists. Once ADU-03 is ✅, renaming its file is an edit of a completed unit's test (hard rule 1, a grant), and that is what (d) defers into.
4. (c) changes how all 46 completed tests are imported. They pass in importlib mode today (measured), but every later unit inherits the mode, and in it test modules cannot import one another. (b) makes four top-level packages named identity, notifications, scheduling and swaps importable from tests/ (pyproject.toml's `pythonpath`), beside tests/api's modules, which stay outside any package.

The cost of (a) is 28 plan fragments, one per `tests:` line and per arm, and the Part C chase. Rehearsed (B-4.3): with all four stages applied, four stand-in tests under (a)'s names collect together and the gate is green; the same four under `test_service.py` fail collection with 3 errors.

#### E-10a.1 · ADU-PLAN.md:149
replace exactly:
~~~text
tests: ["tests/identity/test_service.py"]
~~~
with:
~~~text
tests: ["tests/identity/test_identity_service.py"]
~~~

#### E-10a.2 · ADU-PLAN.md:161 (within the line; it runs on into line 162)
replace exactly (within the line):
~~~text
file: tests/identity/test_service.py, kind: deterministic }
  - { arm: "seed_admin on an empty team
~~~
with:
~~~text
file: tests/identity/test_identity_service.py, kind: deterministic }
  - { arm: "seed_admin on an empty team
~~~

#### E-10a.3 · ADU-PLAN.md:162
replace exactly (within the line):
~~~text
team it raises Refused(team_not_empty)", file: tests/identity/test_service.py
~~~
with:
~~~text
team it raises Refused(team_not_empty)", file: tests/identity/test_identity_service.py
~~~

#### E-10a.4 · ADU-PLAN.md:163
replace exactly (within the line):
~~~text
Refused with those reasons", file: tests/identity/test_service.py
~~~
with:
~~~text
Refused with those reasons", file: tests/identity/test_identity_service.py
~~~

#### E-10a.5 · ADU-PLAN.md:164
replace exactly (within the line):
~~~text
last_admin, invalid_role, not_found, forbidden", file: tests/identity/test_service.py
~~~
with:
~~~text
last_admin, invalid_role, not_found, forbidden", file: tests/identity/test_identity_service.py
~~~

#### E-10a.6 · ADU-PLAN.md:165
replace exactly (within the line):
~~~text
(nothing emitted); not_found; forbidden", file: tests/identity/test_service.py
~~~
with:
~~~text
(nothing emitted); not_found; forbidden", file: tests/identity/test_identity_service.py
~~~

#### E-10a.7 · ADU-PLAN.md:166
replace exactly (within the line):
~~~text
for an inactive member", file: tests/identity/test_service.py
~~~
with:
~~~text
for an inactive member", file: tests/identity/test_identity_service.py
~~~

#### E-10a.8 · ADU-PLAN.md:167
replace exactly (within the line):
~~~text
name (case-insensitively) then id", file: tests/identity/test_service.py
~~~
with:
~~~text
name (case-insensitively) then id", file: tests/identity/test_identity_service.py
~~~

#### E-10a.9 · ADU-PLAN.md:182
replace exactly:
~~~text
tests: ["tests/notifications/test_service.py"]
~~~
with:
~~~text
tests: ["tests/notifications/test_notifications_service.py"]
~~~

#### E-10a.10 · ADU-PLAN.md:191
replace exactly (within the line):
~~~text
double) stay green unchanged", file: tests/notifications/test_service.py
~~~
with:
~~~text
double) stay green unchanged", file: tests/notifications/test_notifications_service.py
~~~

#### E-10a.11 · ADU-PLAN.md:192
replace exactly (within the line):
~~~text
skipped except for MemberDeactivated", file: tests/notifications/test_service.py
~~~
with:
~~~text
skipped except for MemberDeactivated", file: tests/notifications/test_notifications_service.py
~~~

#### E-10a.12 · ADU-PLAN.md:193
replace exactly (within the line):
~~~text
for an unknown id", file: tests/notifications/test_service.py
~~~
with:
~~~text
for an unknown id", file: tests/notifications/test_notifications_service.py
~~~

#### E-10a.13 · ADU-PLAN.md:194
replace exactly (within the line):
~~~text
one assertion per event", file: tests/notifications/test_service.py
~~~
with:
~~~text
one assertion per event", file: tests/notifications/test_notifications_service.py
~~~

#### E-10a.14 · ADU-PLAN.md:209
replace exactly:
~~~text
tests: ["tests/scheduling/test_service.py", "tests/scheduling/test_board_timing.py"]
~~~
with:
~~~text
tests: ["tests/scheduling/test_scheduling_service.py", "tests/scheduling/test_board_timing.py"]
~~~

#### E-10a.15 · ADU-PLAN.md:220
replace exactly (within the line):
~~~text
double) stay green unchanged", file: tests/scheduling/test_service.py
~~~
with:
~~~text
double) stay green unchanged", file: tests/scheduling/test_scheduling_service.py
~~~

#### E-10a.16 · ADU-PLAN.md:221
replace exactly (within the line):
~~~text
shift with its holder-rows", file: tests/scheduling/test_service.py
~~~
with:
~~~text
shift with its holder-rows", file: tests/scheduling/test_scheduling_service.py
~~~

#### E-10a.17 · ADU-PLAN.md:222
replace exactly (within the line):
~~~text
refuses week_published and not_found", file: tests/scheduling/test_service.py
~~~
with:
~~~text
refuses week_published and not_found", file: tests/scheduling/test_scheduling_service.py
~~~

#### E-10a.18 · ADU-PLAN.md:223
replace exactly (within the line):
~~~text
through the SpyNotifier double", file: tests/scheduling/test_service.py
~~~
with:
~~~text
through the SpyNotifier double", file: tests/scheduling/test_scheduling_service.py
~~~

#### E-10a.19 · ADU-PLAN.md:224
replace exactly (within the line):
~~~text
the clock or null", file: tests/scheduling/test_service.py
~~~
with:
~~~text
the clock or null", file: tests/scheduling/test_scheduling_service.py
~~~

#### E-10a.20 · ADU-PLAN.md:225
replace exactly (within the line):
~~~text
draft and published weeks", file: tests/scheduling/test_service.py
~~~
with:
~~~text
draft and published weeks", file: tests/scheduling/test_scheduling_service.py
~~~

#### E-10a.21 · ADU-PLAN.md:227
replace exactly (within the line):
~~~text
without an open request", file: tests/scheduling/test_service.py
~~~
with:
~~~text
without an open request", file: tests/scheduling/test_scheduling_service.py
~~~

#### E-10a.22 · ADU-PLAN.md:242
replace exactly:
~~~text
tests: ["tests/swaps/test_service.py", "tests/swaps/test_decide.py"]
~~~
with:
~~~text
tests: ["tests/swaps/test_swaps_service.py", "tests/swaps/test_decide.py"]
~~~

#### E-10a.23 · ADU-PLAN.md:251
replace exactly (within the line):
~~~text
double) stay green unchanged", file: tests/swaps/test_service.py
~~~
with:
~~~text
double) stay green unchanged", file: tests/swaps/test_swaps_service.py
~~~

#### E-10a.24 · ADU-PLAN.md:252
replace exactly (within the line):
~~~text
→ reason_required → invalid_reason", file: tests/swaps/test_service.py
~~~
with:
~~~text
→ reason_required → invalid_reason", file: tests/swaps/test_swaps_service.py
~~~

#### E-10a.25 · ADU-PLAN.md:253
replace exactly (within the line):
~~~text
reason sent with accept)", file: tests/swaps/test_service.py
~~~
with:
~~~text
reason sent with accept)", file: tests/swaps/test_swaps_service.py
~~~

#### E-10a.26 · ADU-PLAN.md:257
replace exactly (within the line):
~~~text
other party still listed", file: tests/swaps/test_service.py
~~~
with:
~~~text
other party still listed", file: tests/swaps/test_swaps_service.py
~~~

#### E-10a.27 · ADU-PLAN.md:258
replace exactly (within the line):
~~~text
planner; forbidden for members", file: tests/swaps/test_service.py
~~~
with:
~~~text
planner; forbidden for members", file: tests/swaps/test_swaps_service.py
~~~

#### E-10a.28 · ADU-PLAN.md:259
replace exactly (within the line):
~~~text
deadline) without reading scheduling", file: tests/swaps/test_service.py
~~~
with:
~~~text
deadline) without reading scheduling", file: tests/swaps/test_swaps_service.py
~~~

#### E-10a.29 · DECISIONS.md:18
replace exactly (within the line):
~~~text
design/INTERFACES.md §Refused |
~~~
with:
~~~text
design/INTERFACES.md §Refused |
| D-p7 | **A service unit's test file is named for its domain, `tests/<domain>/test_<domain>_service.py`, so no two test files share a basename.** ADU-03, ADU-09, ADU-05 and ADU-07 place their service tests at `tests/identity/test_identity_service.py`, `tests/notifications/test_notifications_service.py`, `tests/scheduling/test_scheduling_service.py` and `tests/swaps/test_swaps_service.py`. pytest's default import mode imports a test file under its basename, and tests/ holds no package, so two `test_service.py` fail collection. | <apply-date>, operator: Q-p6 option (a), Part E-10 of docs/PACK-q07-retire-amends.md v1.2. A plan edit of four units not yet built: no completed unit's file, no protected path, no grant. Unique basenames collect under every import mode and follow the naming plugin FB-33 proposes. Measured: four stand-in tests under these names collect with the gate green, and under one name fail with 3 errors. ADU-PLAN.md, the four entries |
~~~

#### E-10a.30 · OPEN-QUESTIONS.md:59
replace exactly (within the line):
~~~text
found by verification R1, are Q-p6.
~~~
with:
~~~text
found by verification R1, are Q-p6, resolved by this apply (D-p7).
~~~

#### E-10a.31 · OPEN-QUESTIONS.md:96
replace exactly:
~~~text
### Q-p6 · 2026-11-08 · verification R1 (the plan's test paths) · open
~~~
with:
~~~text
### Q-p6 · 2026-11-08 · verification R1 (the plan's test paths) · resolved → D-p7
~~~

#### E-10a.32 · OPEN-QUESTIONS.md:100
replace exactly:
~~~text
**Recommendation:** (a), ruled in this loop (docs/PACK-q07-retire-amends.md, Part E-10): it edits plan text only, and it is cheapest before ADU-03 opens.
**Resolution:** none yet.
~~~
with:
~~~text
**Recommendation:** (a), ruled in this loop (docs/PACK-q07-retire-amends.md, Part E-10): it edits plan text only, and it is cheapest before ADU-03 opens.
**Resolution:** option (a), the operator, <apply-date>, on Part E-10 of docs/PACK-q07-retire-amends.md v1.2 (verified in docs/VERIFICATION-<id>.md): the four service test files are named `tests/<domain>/test_<domain>_service.py`. It lives in D-p7 and ADU-PLAN v1.3 (the `tests:` lines and arm files of ADU-03, ADU-09, ADU-05 and ADU-07).
~~~

#### E-10a.33 · VERSIONS.md:120
replace exactly (within the line):
~~~text
the service units' test files (Q-p6)
~~~
with:
~~~text
the service units' test files (Q-p6 → D-p7)
~~~

#### E-10a.34 · VERSIONS.md:123
replace exactly (within the line):
~~~text
the service units' test files: Q-p6;
~~~
with:
~~~text
the four service units' test files renamed tests/<domain>/test_<domain>_service.py (Q-p6, D-p7);
~~~

#### E-10b.1 · ADU-PLAN.md:148 (without E-2 (b))
replace exactly:
~~~text
files: ["src/app/identity/service.py", "src/app/identity/repo.py"]
~~~
with:
~~~text
files: ["src/app/identity/service.py", "src/app/identity/repo.py", "tests/identity/__init__.py"]
~~~

#### E-10b.2 · ADU-PLAN.md:148 (with E-2 (b); on the text E-2b.2 writes)
replace exactly (within the line):
~~~text
"src/app/refusals.py"]
~~~
with:
~~~text
"src/app/refusals.py", "tests/identity/__init__.py"]
~~~

#### E-10b.3 · ADU-PLAN.md:181
replace exactly:
~~~text
files: ["src/app/notifications/service.py", "src/app/notifications/repo.py"]
~~~
with:
~~~text
files: ["src/app/notifications/service.py", "src/app/notifications/repo.py", "tests/notifications/__init__.py"]
~~~

#### E-10b.4 · ADU-PLAN.md:208
replace exactly:
~~~text
files: ["src/app/scheduling/service.py", "src/app/scheduling/repo.py", "src/app/scheduling/rules.py"]
~~~
with:
~~~text
files: ["src/app/scheduling/service.py", "src/app/scheduling/repo.py", "src/app/scheduling/rules.py", "tests/scheduling/__init__.py"]
~~~

#### E-10b.5 · ADU-PLAN.md:241
replace exactly:
~~~text
files: ["src/app/swaps/service.py", "src/app/swaps/repo.py", "src/app/swaps/rules.py"]
~~~
with:
~~~text
files: ["src/app/swaps/service.py", "src/app/swaps/repo.py", "src/app/swaps/rules.py", "tests/swaps/__init__.py"]
~~~

#### E-10b.6 · DECISIONS.md:18
replace exactly (within the line):
~~~text
design/INTERFACES.md §Refused |
~~~
with:
~~~text
design/INTERFACES.md §Refused |
| D-p7 | **Each service unit's test folder is a package: ADU-03, ADU-09, ADU-05 and ADU-07 each add `tests/<domain>/__init__.py` to their `files`, so pytest imports their `test_service.py` as `<domain>.test_service` and the four collect together.** No other test folder becomes a package. | <apply-date>, operator: Q-p6 option (b), Part E-10 of docs/PACK-q07-retire-amends.md v1.2. The test paths and arms stay as cut. Accepted with its consequences: four top-level packages named identity, notifications, scheduling and swaps are importable from tests/ (pyproject.toml's `pythonpath`), and four test files still share one basename, which the plan check plugin FB-33 proposes would refuse. ADU-PLAN.md, the four entries |
~~~

#### E-10b.7 · OPEN-QUESTIONS.md:59
replace exactly (within the line):
~~~text
found by verification R1, are Q-p6.
~~~
with:
~~~text
found by verification R1, are Q-p6, resolved by this apply (D-p7).
~~~

#### E-10b.8 · OPEN-QUESTIONS.md:96
replace exactly:
~~~text
### Q-p6 · 2026-11-08 · verification R1 (the plan's test paths) · open
~~~
with:
~~~text
### Q-p6 · 2026-11-08 · verification R1 (the plan's test paths) · resolved → D-p7
~~~

#### E-10b.9 · OPEN-QUESTIONS.md:100
replace exactly:
~~~text
**Recommendation:** (a), ruled in this loop (docs/PACK-q07-retire-amends.md, Part E-10): it edits plan text only, and it is cheapest before ADU-03 opens.
**Resolution:** none yet.
~~~
with:
~~~text
**Recommendation:** (a), ruled in this loop (docs/PACK-q07-retire-amends.md, Part E-10): it edits plan text only, and it is cheapest before ADU-03 opens.
**Resolution:** option (b), the operator, <apply-date>, on Part E-10 of docs/PACK-q07-retire-amends.md v1.2 (verified in docs/VERIFICATION-<id>.md): each service unit's `files:` gains `tests/<domain>/__init__.py`. It lives in D-p7 and ADU-PLAN v1.3 (the `files:` of ADU-03, ADU-09, ADU-05 and ADU-07).
~~~

#### E-10b.10 · VERSIONS.md:120
replace exactly (within the line):
~~~text
the service units' test files (Q-p6)
~~~
with:
~~~text
the service units' test files (Q-p6 → D-p7)
~~~

#### E-10b.11 · VERSIONS.md:123
replace exactly (within the line):
~~~text
the service units' test files: Q-p6;
~~~
with:
~~~text
each service unit's files gain tests/<domain>/__init__.py (Q-p6, D-p7);
~~~

#### E-10c.1 · ADU-PLAN.md:147 (without E-2 (b))
replace exactly:
~~~text
depends: [ADU-01, ADU-02, ADU-16]
~~~
with:
~~~text
depends: [ADU-00, ADU-01, ADU-02, ADU-16]
~~~

#### E-10c.2 · ADU-PLAN.md:156
The amends line goes last in ADU-03's `amends`, before its `mocks:`.
replace exactly:
~~~text
mocks:
  - { id: MK-01, interface: SchedulingPort, kind: in-process, provider: ADU-05, stub: src/app/scheduling/null_port.py }
~~~
with:
~~~text
  - { unit: ADU-00, file: pyproject.toml, assertion: "[tool.pytest.ini_options] gains addopts set to --import-mode=importlib, so test files of one basename in different folders collect together; nothing else in the file changes, and every completed unit's test stays green unchanged", q: Q-07 }
mocks:
  - { id: MK-01, interface: SchedulingPort, kind: in-process, provider: ADU-05, stub: src/app/scheduling/null_port.py }
~~~

#### E-10c.3 · DECISIONS.md:18
replace exactly (within the line):
~~~text
design/INTERFACES.md §Refused |
~~~
with:
~~~text
design/INTERFACES.md §Refused |
| D-p7 | **The test suite is collected in pytest's importlib import mode: ADU-03 amends ADU-00's pyproject.toml so `[tool.pytest.ini_options]` gains `addopts = "--import-mode=importlib"`, and test files of one basename in different folders collect together.** ADU-03's `depends` gains ADU-00. | <apply-date>, operator: Q-p6 option (c), Part E-10 of docs/PACK-q07-retire-amends.md v1.2. One line, and it serves every later test file too. Accepted with its consequences: every completed unit's test is imported in the new mode from ADU-03 on (measured: the 46 pass), and test modules cannot import one another; pyproject.toml's `pythonpath` keeps `support` and `layering_scan` importable. pyproject.toml is neither pinned nor protected, and an `amends` of a non-test file needs no grant. ADU-PLAN.md, ADU-03's entry |
~~~

#### E-10c.4 · OPEN-QUESTIONS.md:59
replace exactly (within the line):
~~~text
found by verification R1, are Q-p6.
~~~
with:
~~~text
found by verification R1, are Q-p6, resolved by this apply (D-p7).
~~~

#### E-10c.5 · OPEN-QUESTIONS.md:96
replace exactly:
~~~text
### Q-p6 · 2026-11-08 · verification R1 (the plan's test paths) · open
~~~
with:
~~~text
### Q-p6 · 2026-11-08 · verification R1 (the plan's test paths) · resolved → D-p7
~~~

#### E-10c.6 · OPEN-QUESTIONS.md:100
replace exactly:
~~~text
**Recommendation:** (a), ruled in this loop (docs/PACK-q07-retire-amends.md, Part E-10): it edits plan text only, and it is cheapest before ADU-03 opens.
**Resolution:** none yet.
~~~
with:
~~~text
**Recommendation:** (a), ruled in this loop (docs/PACK-q07-retire-amends.md, Part E-10): it edits plan text only, and it is cheapest before ADU-03 opens.
**Resolution:** option (c), the operator, <apply-date>, on Part E-10 of docs/PACK-q07-retire-amends.md v1.2 (verified in docs/VERIFICATION-<id>.md): ADU-03 amends ADU-00's pyproject.toml with `addopts = "--import-mode=importlib"`. It lives in D-p7 and ADU-PLAN v1.3 (ADU-03's `amends` and `depends`).
~~~

#### E-10c.7 · VERSIONS.md:120
replace exactly (within the line):
~~~text
the service units' test files (Q-p6)
~~~
with:
~~~text
the service units' test files (Q-p6 → D-p7)
~~~

#### E-10c.8 · VERSIONS.md:123
replace exactly (within the line):
~~~text
the service units' test files: Q-p6;
~~~
with:
~~~text
ADU-03 amends ADU-00's pyproject.toml (--import-mode=importlib) and depends on ADU-00 (Q-p6, D-p7);
~~~

#### E-10d.1 · STATUS.md:31
The second Owed row. It shares E-5's anchor and goes first, so it stands after O-p1.
replace exactly (within the line):
~~~text
| operator, 2026-11-07 17:37, release M1: "0-01 approved" | open |
~~~
with:
~~~text
| operator, 2026-11-07 17:37, release M1: "0-01 approved" | open |
| O-p2 | ADU-09 | Q-p6: the four service units' test files share the basename test_service.py and fail pytest collection together from ADU-09 on (plugin FB-33); ruled in a design-change loop before ADU-09 opens (ADU-PLAN.md, ADU-09's pointer); once ADU-03 is ✅, renaming tests/identity/test_service.py is an edit of a completed unit's test (hard rule 1, a grant) | operator, <apply-date>: the ruling of E-10 (d) on docs/PACK-q07-retire-amends.md v1.2 (Q-p6 deferred, entered non-blocking because `adu status` reads `**Blocking:** yes` as a stop for every unit, plugin FB-32) | open |
~~~

#### E-10d.2 · ADU-PLAN.md:197
The block starts with the blank line before ADU-05's heading, so the pointer follows ADU-09's yaml block directly.
replace exactly:
~~~text

### ADU-05 — Scheduling service
~~~
with:
~~~text
**Owed before this unit opens (Q-07's design-change loop).** Four service units' test files share the basename `test_service.py` (this unit's, ADU-03's, ADU-05's and ADU-07's), and pytest's default import mode fails the second one at collection (plugin FB-33). The fix is outside this unit's roster: unique names, `__init__.py` packages, or an import-mode change in ADU-00's pyproject.toml. A design-change loop rules it before this unit's hand-over, and an Owed row due at this unit in STATUS.md carries the duty (plugin FB-32). Once ADU-03 is ✅, renaming its test file is an edit of a completed unit's test (hard rule 1).

### ADU-05 — Scheduling service
~~~

#### E-10d.3 · OPEN-QUESTIONS.md:59
replace exactly (within the line):
~~~text
found by verification R1, are Q-p6.
~~~
with:
~~~text
found by verification R1, are Q-p6, entered open and non-blocking and owed before ADU-09 (O-p2).
~~~

#### E-10d.4 · OPEN-QUESTIONS.md:100
Q-p6 stays open; the ruling is recorded as Q-07's was.
replace exactly:
~~~text
**Recommendation:** (a), ruled in this loop (docs/PACK-q07-retire-amends.md, Part E-10): it edits plan text only, and it is cheapest before ADU-03 opens.
**Resolution:** none yet.
~~~
with:
~~~text
**Recommendation:** (a), ruled in this loop (docs/PACK-q07-retire-amends.md, Part E-10): it edits plan text only, and it is cheapest before ADU-03 opens.
**Ruling:** deferred, the operator, <apply-date>, on Part E-10 (d) of docs/PACK-q07-retire-amends.md v1.2 (verified in docs/VERIFICATION-<id>.md): a design-change loop rules it before ADU-09 opens. The Owed row O-p2 (STATUS.md, due ADU-09) and ADU-09's entry carry the duty (plugin FB-32).
**Resolution:** none yet.
~~~

#### E-10d.5 · VERSIONS.md:120
replace exactly (within the line):
~~~text
the service units' test files (Q-p6)
~~~
with:
~~~text
the service units' test files (Q-p6, deferred: O-p2)
~~~

#### E-10d.6 · VERSIONS.md:123
replace exactly (within the line):
~~~text
the service units' test files: Q-p6;
~~~
with:
~~~text
ADU-09's entry points to the Owed row of Q-p6 (O-p2);
~~~
