# PACK — q07-retire-amends
v1.0 · 2026-11-08 · snapshot: 7d1e7d4 · status: unapplied — verification pending (round R1)
Input to the loop, not a replacement for it: every proposal below is in the documents' own vocabulary, for a verifier to check first and the release-manager to apply second. Every identifier here is provisional (D-p1, D-p2, Q-p1 … Q-p5) until the apply step allocates it with `adu next-id`; `<apply-date>` is the apply step's date. Drafted by the architect (`/adu-lifecycle:change-design Q-07`, stage 1); the operator's ruling is written here, not re-opened.

**How to read the replacement blocks.** Each block is headed `#### <id> · <file>:<line>` and gives `replace exactly:` and `with:` as fenced `text` blocks; the fence content is the text, character for character, with line endings normalised (the Windows working tree is CRLF, the blobs LF). "(within the line)" means the text is a fragment of that line, with no line ending of its own. An empty `with:` block removes the lines, line endings included. A block's line is where its text starts. B-blocks are numbered against 7d1e7d4, and E-blocks against the file as B leaves it. T-blocks are numbered against the file as the previous retirement leaves it: 7d1e7d4 for ADU-03. Within a file, blocks are applied from the bottom up, so every stated line stays valid. Every block was matched and applied by the script in B-4.3; its outputs are pasted there.

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
| plugin `scripts/adu.mjs:687` (plugin HEAD 4b63bb0) | a path in a completed unit's `tests:` is denied unless granted; `amends` is not consulted | every edit of a completed unit's test needs the operator's grant, with or without an `amends` line (plugin FB-28, plugin FEEDBACK.md:33, open) |
| plugin `scripts/adu.mjs:692–693` | the Now unit's roster is `files` + `tests` + `amends` files | `amends` is honoured for non-test files (main.py, a Null, ports.py, doubles.py, layering.json); no grant is needed there |
| plugin `scripts/adu.mjs:704` | the bash guard refuses `rm` only of the ledgers | removing `tests/test_nulls.py` at ADU-07 is not seen by any guard; the grant and the journal are its only record |
| src/app/ports.py:28–41 | `MemberNotFound`, `AssignmentNotFound`, `TransferRefused(reason)` with `.reason` | the cross-domain exceptions already live in the layer-2 module; `TransferRefused` is the precedent shape for `Refused` |
| tests/test_ports.py:21, :38, :66, :117–118 | the pinned signatures (`caller_for_token(self, token)`, `notify(self, event)`), `not hasattr(ports, "FixedClock")`, and "ports imports nothing of the product" | adding `Refused` to ports.py breaks none of them (rehearsed: B-4.3) |
| tests/layering.json, `forbidden` | `["scheduling","identity"]`, `["swaps","identity"]`, `["notifications","identity"]` and every other cross-domain pair | a `Refused` defined in identity's own module could not be imported by any later service |
| tests/layering_scan.py:46–57, :101–104 | `layer_of` returns None for a module in no layer, and no edge from or to such a module is ever flagged | a new module outside `tests/layering.json`'s layers would escape the ratchet |
| design/INTERFACES.md (whole file) | five protocols, doubles, bindings, build order, CLI, traceability; no IdentityService and no Refused | the two gaps the ruling names |
| ADU-PLAN.md:160–165 | arms 2–7 name seed_admin, add_member, change_role, deactivate, sign_in, caller_for_token, list_members and MemberSummary, and raise `Refused(<reason>)` | the sources of the IdentityService section (B-2.3) |

### A-3 What a correct mechanism must do, and must never do
**Must:** let each provider retire its Null in one session, together with every completed test that names that Null, edited exactly where it names it and nowhere else. Keep every assertion ADU-02's and ADU-16's arms require: the served operations' identity; 401 without a token and with an unknown one; 501 not_built with a resolved caller; every example validates; an implementation of each protocol bound; the injectable clock; one session per request. Keep hard rule 1 in the operator's hands: one grant per file, per session, recorded in that session's journal. Leave the other Nulls' tests untouched until their own provider. Define `Refused` and IdentityService before ADU-03 implements them, with every point the sources do not settle left visibly open.
**Must never:** skip, xfail or delete an assertion that is not about the Null. Weaken the 501 check (to "not 401", say). Bring the Null back under another name as the default binding. Let a later unit's edit ride on ADU-03's grant. Invent a signature the arms, the identity spec and the contract do not settle.

## Part B — the proposal

### B-1 DECISIONS rows (provisional)
| ID | Decision | Rationale / status |
|---|---|---|
| D-p1 | **Retiring a Null edits the completed tests that name it. Each such test is declared in the retiring unit's `amends` and edited only under the operator's grant.** The import goes, a class check becomes a protocol check, and a test that needs a resolved caller injects a double through `create_app(member_directory=…)`. Nothing else in the test changes. The edit guard does not honour `amends` on a completed unit's test (plugin FB-28), so the retiring session obtains the grant (`adu grant add <session> <file> "<reason>"`) before its first edit and records it in its journal block. | Q-07 option 1, ruled by the operator 2026-11-07, verbatim "Add both tests to ADU-03's amends". ADU-02's arms pin a protocol, not a class (ADU-PLAN.md:129, :132). Applies to ADU-03, ADU-09, ADU-05, ADU-07 |
| D-p2 | **`Refused(reason, detail="", **extra)` in `src/app/ports.py` is the one domain refusal.** Every service raises it for a refusal a story names. `reason` is a code of the Reason codes table, `detail` the plain sentence, `extra` the fields a story names. It carries no HTTP status: the API layer maps the bucket per operation (D-07), and the seed command exits 2. ADU-03 adds it to ADU-16's module by a declared amendment. | Part E-2, E-3. ports.py already holds the cross-domain exceptions and imports nothing of the product, so every service, the API and the CLI reach it without a forbidden edge. `TransferRefused` is the precedent shape |

### B-2 Document amendments
The two rows above become B-2.1. The rest: design/INTERFACES.md (B-2.2–B-2.5), OPEN-QUESTIONS.md (B-2.6–B-2.7), VERSIONS.md (B-2.8–B-2.9). No change to design/ARCHITECTURE.md, the contract, the golden, PINS.lock, adu.toml or any test.

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
Why: D-p2 (Refused), and the IdentityService section the ruling asks for. Signatures come only from ADU-03's arms (ADU-PLAN.md:159–165), R-identity-01..09 (design/domains/identity/spec.md:7–15) and contracts/openapi.yaml. Each point those sources do not settle is marked open with its question (B-5).
replace exactly:
~~~text
## Test doubles (ADU-16, permanent — never deleted)
~~~
with:
~~~text
### Refused (every domain → the API layer and the operator's command)
Provider: ADU-03, in `src/app/ports.py` beside `MemberNotFound`, `AssignmentNotFound` and `TransferRefused` (D-p2; ADU-03 amends ADU-16's module). Consumers: every service raises it; the API units map it to a Problem; the seed command (ADU-11) maps `team_not_empty` to exit status 2.
```
class Refused(Exception):
    def __init__(self, reason: str, detail: str = "", **extra: object) -> None   # .reason, .detail, .extra
```
Invariants: `reason` is a code of PRODUCT-DESIGN's Reason codes table (the values of the contract's `Problem.reason` and `PublishProblem.reason`, and `team_not_empty`); `detail` is the refusal's plain sentence and `extra` the fields a story names (`unfilled` for publish), because a refusal is {reason, detail, and the extra fields a story names} (PRODUCT-DESIGN, cross-cutting rules); `Refused` carries no HTTP status — the API layer maps the reason to its bucket's status per operation (D-07); a refusal changes nothing (services check before they write); tests assert `.reason`, never `.detail`; `TransferRefused` stays the transfer's own signal (IR-02) and is never re-raised as `Refused` (an approval whose transfer was refused succeeds).

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
**Resolution:** option 1, as ruled. Applied <apply-date> from docs/PACK-q07-retire-amends.md (verified in docs/VERIFICATION-<id>.md): D-p1 (the retirement edits, each under the operator's grant) and D-p2 (Refused); ADU-PLAN v1.3 (the amends and retirement arms of ADU-03, ADU-09, ADU-05 and ADU-07; ADU-03 amends src/app/ports.py); design/INTERFACES.md v1.1 (§Refused, §Domain services with IdentityService, the retirement paragraph). The IdentityService section's open points are Q-p1–Q-p4; the same wall at the API units is Q-p5.

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
**Conflict:** tests/api/test_contract_conformance.py:58–73 expects every operation except sign-in to answer `501 not_built` with a resolved caller, and sign-in to answer 501 (:66–67). ADU-04, ADU-06, ADU-10 and ADU-08 move their operations out of the stubs (ADU-PLAN.md:273, :299, :325, :349), after which those operations answer their real codes. ADU-08 deletes `src/app/api/contract_stubs.py`, which the test imports (line 22) for `example_path`, `example_body`, `validate_example`, `resolve` and `SESSION_DEP` (:63–64, :83, :86, :92, :99, :127); ADU-04's arm (ADU-PLAN.md:281) also uses "the conformance helper from ADU-02", which is `contract_stubs.validate_example` (src/app/api/contract_stubs.py:46). None of the four API entries declares the conformance test in its `amends`. This is Q-07's wall again, one milestone later.
**Blocking:** yes for ADU-04 (derived position 9); not for ADU-03, ADU-09, ADU-05 or ADU-07.
**Options:** (a) the D-p1 pattern: each API unit's `amends` gains the conformance test under a grant; the 501 loop leaves out the operations its router now serves (sign-in leaves at ADU-04); ADU-08 moves the helpers to a surviving module and repoints the imports. Consequence: four more edits of a completed test. (b) one re-cut before ADU-04: the helpers move to a permanent module (e.g. tests/support/contract.py), and the 501 assertion iterates the operations contract_stubs still registers, so no later unit edits the test again. Consequence: one hard-rule-1 edit, made by ADU-04 or by a contract-maintenance unit.
**Recommendation:** (b), decided in a design-change loop before ADU-04 opens.
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

### <apply-date> — ADU-PLAN v1.3, INTERFACES v1.1: Q-07, D-p1, D-p2 — the retirement edits under grants, Refused, IdentityService
| Document | From | To | What changed |
|---|---|---|---|
| ADU-PLAN.md | 1.2 | 1.3 | ADU-03, ADU-09, ADU-05, ADU-07: amends gain tests/api/test_contract_conformance.py and widen tests/test_nulls.py, each edited under the operator's grant (D-p1); ADU-03 amends src/app/ports.py (Refused, D-p2); the four retirement arms rewritten so they can be met; the Shape-of-the-cut sentence on retirement: a requirement changed, hence the minor bump |
| design/INTERFACES.md | 1.0.1 | 1.1 | §Refused; §Domain services with IdentityService (signatures from ADU-03's arms, R-identity-01..09 and the contract; open points Q-p1–Q-p4); the retirement paragraph under the composition-root bindings; US-identity-005's trace names IdentityService.seed_admin; first row in Current |
~~~

### B-2.T The edits the retiring sessions make under their grants (normative content; not applied by the apply step)
Each block below is what the corresponding `amends` line in B-3 declares. The unit session makes these edits, only after the operator's grant for that file in that session. The apply step does not make them. They were applied stage by stage to the scratch export (B-4.3). Each stage also ran the gate and the lint there, with stand-in services in place of the real ones.

**ADU-03 — tests/api/test_contract_conformance.py** (at 7d1e7d4; T-03.1 and T-03.5 are E-4 option (a))

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
    directory = FakeMemberDirectory()  # resolves tok_1 as the retired NullDirectory did (Q-07)
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
Every `amends` line the pattern needs, and every retirement arm rewritten so it can be met. The plan text cites `Q-07` only, because `adu plan check` rejects a provisional id anywhere in the plan (plugin `scripts/lib/plan.mjs`, `findProvisionalIds`). No `files`, `tests`, `depends`, size or arm count changes. Each new `amends` line names a unit already in the entry's `amends` (ADU-02, ADU-16), so the derived `depends` and the order are unchanged.

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
  - { unit: ADU-02, file: tests/api/test_contract_conformance.py, assertion: "a completed unit's test, edited under the operator's grant (hard rule 1, Q-07): the NullDirectory import goes; the class check isinstance(p.member_directory, NullDirectory) becomes isinstance(p.member_directory, ports.MemberDirectory); the 401/501 test builds its app with create_app(workspace=tmp_path, member_directory=directory), directory a FakeMemberDirectory holding member 1 ('Member 1', member, active) with token tok_1, so Bearer tok_1 still answers 501 not_built; the composition-root test is renamed test_the_composition_root_binds_an_implementation_per_port_and_an_injectable_clock and the module docstring reads 'binds an implementation of each port (the Null until its provider lands)'; no other assertion changes", q: Q-07 }
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

#### B-3.15 The plan after the change, checked on a scratch copy
`git archive 7d1e7d4` exported to the scratchpad (outside the repository), B-3.1–B-3.14 applied by the B-4.3 script, then `adu plan check` and `adu plan order` with the working directory inside the copy:

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

The order is the one `adu plan order` gives at 7d1e7d4 (18 units, ADU-03 at 5, ADU-09 at 6, ADU-05 at 7, ADU-07 at 8). Two copies, the pristine export and this one, also check the guard. The grants are still needed after the apply; each message is cut at 150 characters by the script:

~~~text
guard edit tests/test_nulls.py --role developer (at 7d1e7d4) -> exit 2: adu guard: refused to edit tests/test_nulls.py: tests/test_nulls.py is a test file of completed unit ADU-16: tests of completed ADUs are immutable (ha
guard edit tests/api/test_contract_conformance.py --role developer (at 7d1e7d4) -> exit 2: adu guard: refused to edit tests/api/test_contract_conformance.py: tests/api/test_contract_conformance.py is a test file of completed unit ADU-02: tes
guard edit src/app/ports.py --role developer (at 7d1e7d4) -> exit 2: adu guard: refused to edit src/app/ports.py: src/app/ports.py is outside ADU-03's roster (files, tests, amends). Stay inside this unit's specified fil
guard edit tests/test_nulls.py --role developer (with B-3 applied) -> exit 2: adu guard: refused to edit tests/test_nulls.py: tests/test_nulls.py is a test file of completed unit ADU-16: tests of completed ADUs are immutable (ha
guard edit tests/api/test_contract_conformance.py --role developer (with B-3 applied) -> exit 2: adu guard: refused to edit tests/api/test_contract_conformance.py: tests/api/test_contract_conformance.py is a test file of completed unit ADU-02: tes
guard edit src/app/ports.py --role developer (with B-3 applied) -> exit 0: allow src/app/ports.py
~~~

### B-4 Criteria
#### B-4.1 Quantitative criteria and pins
None proposed. Every arm this pack rewrites is deterministic. No pin changes: the contract, `contracts/openapi.golden.json` and PINS.lock are untouched, so no golden is regenerated and no twin is owed. With no stochastic arm there is no false-failure rate to state.

#### B-4.2 Can each rewritten arm fail?
- ADU-03 arm 1 (B-3.5) fails if `create_app()` still binds the Null or anything that does not satisfy `ports.MemberDirectory`; if `src/app/identity/null_directory.py` exists; if any file under src/ or tests/ imports it (as main.py:18, the conformance test :23 and test_nulls.py :11 do at 7d1e7d4); or if either edited test is red in the gate. The rewrite narrows nothing ADU-02's arms require: 401 without a token and with `garbage`, 501 with `tok_1`, an implementation of each protocol bound, the clock, one session per request. Each is still asserted by the unchanged lines.
- ADU-09, ADU-05 and ADU-07 arm 1 (B-3.8, B-3.11, B-3.14) fail the same way for their own Null. ADU-07's also fails if tests/test_nulls.py or any Null module survives.
- Twins, rehearsed (B-4.3): at stage ADU-03 the unedited conformance test fails at collection once the Null is deleted, and with only the import and class-check edits (no injected directory) the 401/501 test fails with 401. Each part of T-03 is therefore needed.

#### B-4.3 The rehearsal (reproducible; scratch only)
The script below, `pack_rehearse.py`, was run with the project's venv interpreter (`C:\dev\team-rota-data\.venv\Scripts\python.exe -I`) as `pack_rehearse.py C:\dev\team-rota docs\PACK-q07-retire-amends.md <scratchpad>\rehearsal`. It parses this pack. It checks every B-block against the 7d1e7d4 blob: the text unique in its file, starting at the stated line. It applies B-3 to an export, runs the plan and guard checks, and then runs the four stages in the derived order. Each stage deletes the Null and binds a stand-in "real" service that satisfies the protocol: identity's resolves no token, the worst case for line 70. It applies the stage's T-blocks (each also unique, at its stated line), then runs the gate and the lint. ADU-03's stage also adds the illustrative `Refused` (the D-p2 shape) to ports.py and runs the twins first. The E-blocks are checked against the text as B leaves it. E-2 (b) gets its own plan check. The stand-ins, the main.py rebinding and the illustrative `Refused` are scaffolding for the rehearsal, not proposed text: each session writes its own implementation.

The full output of the run:
~~~text
pack: C:\dev\team-rota\docs\PACK-q07-retire-amends.md · 58 replace blocks · 1 file deletions · snapshot 7d1e7d4
B-2.1    DECISIONS.md:16   occurrences=1 starts-at=16 OK (against the 7d1e7d4 blob)
B-2.5    design/INTERFACES.md:103  occurrences=1 starts-at=103 OK (against the 7d1e7d4 blob)
B-2.4    design/INTERFACES.md:91   occurrences=1 starts-at=91 OK (against the 7d1e7d4 blob)
B-2.3    design/INTERFACES.md:79   occurrences=1 starts-at=79 OK (against the 7d1e7d4 blob)
B-2.2    design/INTERFACES.md:2    occurrences=1 starts-at=2 OK (against the 7d1e7d4 blob)
B-2.7    OPEN-QUESTIONS.md:59   occurrences=1 starts-at=59 OK (against the 7d1e7d4 blob)
B-2.6    OPEN-QUESTIONS.md:53   occurrences=1 starts-at=53 OK (against the 7d1e7d4 blob)
B-2.9    VERSIONS.md:117  occurrences=1 starts-at=117 OK (against the 7d1e7d4 blob)
B-2.8    VERSIONS.md:14   occurrences=1 starts-at=14 OK (against the 7d1e7d4 blob)
B-3.14   ADU-PLAN.md:246  occurrences=1 starts-at=246 OK (against the 7d1e7d4 blob)
B-3.13   ADU-PLAN.md:242  occurrences=1 starts-at=242 OK (against the 7d1e7d4 blob)
B-3.12   ADU-PLAN.md:240  occurrences=1 starts-at=240 OK (against the 7d1e7d4 blob)
B-3.11   ADU-PLAN.md:216  occurrences=1 starts-at=216 OK (against the 7d1e7d4 blob)
B-3.10   ADU-PLAN.md:210  occurrences=1 starts-at=210 OK (against the 7d1e7d4 blob)
B-3.9    ADU-PLAN.md:208  occurrences=1 starts-at=208 OK (against the 7d1e7d4 blob)
B-3.8    ADU-PLAN.md:188  occurrences=1 starts-at=188 OK (against the 7d1e7d4 blob)
B-3.7    ADU-PLAN.md:184  occurrences=1 starts-at=184 OK (against the 7d1e7d4 blob)
B-3.6    ADU-PLAN.md:182  occurrences=1 starts-at=182 OK (against the 7d1e7d4 blob)
B-3.5    ADU-PLAN.md:159  occurrences=1 starts-at=159 OK (against the 7d1e7d4 blob)
B-3.4    ADU-PLAN.md:153  occurrences=1 starts-at=153 OK (against the 7d1e7d4 blob)
B-3.3    ADU-PLAN.md:151  occurrences=1 starts-at=151 OK (against the 7d1e7d4 blob)
B-3.2    ADU-PLAN.md:6    occurrences=1 starts-at=6 OK (against the 7d1e7d4 blob)
B-3.1    ADU-PLAN.md:2    occurrences=1 starts-at=2 OK (against the 7d1e7d4 blob)
E-2b.3   ADU-PLAN.md:155  occurrences=1 starts-at=155 OK (E-2b on post-B)
E-2b.2   ADU-PLAN.md:148  occurrences=1 starts-at=148 OK (E-2b on post-B)
E-2b.1   ADU-PLAN.md:147  occurrences=1 starts-at=147 OK (E-2b on post-B)
E-2b.4   design/ARCHITECTURE.md:12   occurrences=1 starts-at=12 OK (E-2b on post-B)
E-2b.5   design/INTERFACES.md:80   occurrences=1 starts-at=80 OK (E-2b on post-B)
E-2b.6   DECISIONS.md:18   occurrences=1 starts-at=18 OK (E-2b on post-B)
E-2b.7   DECISIONS.md:18   occurrences=1 starts-at=18 OK (E-2b on post-B)
E-3b.1   DECISIONS.md:18   occurrences=1 starts-at=18 OK (E-3b on post-B)
E-3b.2   DECISIONS.md:18   occurrences=1 starts-at=18 OK (E-3b on post-B)
E-3b.4   design/INTERFACES.md:85   occurrences=1 starts-at=85 OK (E-3b on post-B)
E-3b.3   design/INTERFACES.md:83   occurrences=1 starts-at=83 OK (E-3b on post-B)
E-2b.3   ADU-PLAN.md:155  occurrences=1 starts-at=155 OK (E-2b + E-3b on post-B)
E-2b.2   ADU-PLAN.md:148  occurrences=1 starts-at=148 OK (E-2b + E-3b on post-B)
E-2b.1   ADU-PLAN.md:147  occurrences=1 starts-at=147 OK (E-2b + E-3b on post-B)
E-2b.4   design/ARCHITECTURE.md:12   occurrences=1 starts-at=12 OK (E-2b + E-3b on post-B)
E-3b.4   design/INTERFACES.md:85   occurrences=1 starts-at=85 OK (E-2b + E-3b on post-B)
E-3b.3   design/INTERFACES.md:83   occurrences=1 starts-at=83 OK (E-2b + E-3b on post-B)
E-2b.5   design/INTERFACES.md:80   occurrences=1 starts-at=80 OK (E-2b + E-3b on post-B)
E-2b.6   DECISIONS.md:18   occurrences=1 starts-at=18 OK (E-2b + E-3b on post-B)
E-2b.7   DECISIONS.md:18   occurrences=1 starts-at=18 OK (E-2b + E-3b on post-B)
E-3b.1   DECISIONS.md:18   occurrences=1 starts-at=18 OK (E-2b + E-3b on post-B)
E-3b.2   DECISIONS.md:18   occurrences=1 starts-at=18 OK (E-2b + E-3b on post-B)

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

(B-3 blocks applied: 14)
guard edit tests/test_nulls.py --role developer (at 7d1e7d4) -> exit 2: adu guard: refused to edit tests/test_nulls.py: tests/test_nulls.py is a test file of completed unit ADU-16: tests of completed ADUs are immutable (ha
guard edit tests/api/test_contract_conformance.py --role developer (at 7d1e7d4) -> exit 2: adu guard: refused to edit tests/api/test_contract_conformance.py: tests/api/test_contract_conformance.py is a test file of completed unit ADU-02: tes
guard edit src/app/ports.py --role developer (at 7d1e7d4) -> exit 2: adu guard: refused to edit src/app/ports.py: src/app/ports.py is outside ADU-03's roster (files, tests, amends). Stay inside this unit's specified fil
guard edit tests/test_nulls.py --role developer (with B-3 applied) -> exit 2: adu guard: refused to edit tests/test_nulls.py: tests/test_nulls.py is a test file of completed unit ADU-16: tests of completed ADUs are immutable (ha
guard edit tests/api/test_contract_conformance.py --role developer (with B-3 applied) -> exit 2: adu guard: refused to edit tests/api/test_contract_conformance.py: tests/api/test_contract_conformance.py is a test file of completed unit ADU-02: tes
guard edit src/app/ports.py --role developer (with B-3 applied) -> exit 0: allow src/app/ports.py

$ adu plan check   # scratch copy with B-3 and E-2 (b), exit 0
plan OK: 18 units, order ADU-00 → ADU-01 → ADU-16 → ADU-02 → ADU-03 → ADU-09 → ADU-05 → ADU-07 → ADU-04 → ADU-06 → ADU-10 → ADU-08 → ADU-12 → ADU-17 → ADU-13 → ADU-14 → ADU-11 → ADU-15

$ adu plan order   # scratch copy with B-3 and E-2 (b), exit 0
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

baseline (export A, B-3 applied, no stage yet): gate exit 0: 46 passed, 1 warning in 16.43s · lint exit 0: All checks passed!
twin 1 (Null deleted, conformance test unedited): exit 2: E   ModuleNotFoundError: No module named 'app.identity.null_directory' | 1 warning, 1 error in 0.91s
twin 2 (import and class check edited, no injected directory): exit 1: test_contract_conformance.py:70: AssertionError: ('identity.list_members', '{"type":"about:blank","title":"Not signed in","detail":"Sign in first.","reason":"unauthentica | 1 failed, 5 passed, 1 warning in 0.99s
T-03.6   tests/api/test_contract_conformance.py:105  occurrences=1 starts-at=105 OK (stage T-03)
T-03.5   tests/api/test_contract_conformance.py:102  occurrences=1 starts-at=102 OK (stage T-03)
T-03.4   tests/api/test_contract_conformance.py:61   occurrences=1 starts-at=61 OK (stage T-03)
T-03.3   tests/api/test_contract_conformance.py:23   occurrences=1 starts-at=23 OK (stage T-03)
T-03.2   tests/api/test_contract_conformance.py:19   occurrences=1 starts-at=19 OK (stage T-03)
T-03.1   tests/api/test_contract_conformance.py:1    occurrences=1 starts-at=1 OK (stage T-03)
T-03.10  tests/test_nulls.py:36   occurrences=1 starts-at=36 OK (stage T-03)
T-03.9   tests/test_nulls.py:28   occurrences=1 starts-at=28 OK (stage T-03)
T-03.8   tests/test_nulls.py:17   occurrences=1 starts-at=17 OK (stage T-03)
T-03.7   tests/test_nulls.py:11   occurrences=1 starts-at=11 OK (stage T-03)
after stage T-03: gate exit 0: 44 passed, 1 warning in 16.55s · lint exit 0: All checks passed!
T-09.2   tests/api/test_contract_conformance.py:110  occurrences=1 starts-at=110 OK (stage T-09)
T-09.1   tests/api/test_contract_conformance.py:24   occurrences=1 starts-at=24 OK (stage T-09)
T-09.6   tests/test_nulls.py:48   occurrences=1 starts-at=48 OK (stage T-09)
T-09.5   tests/test_nulls.py:28   occurrences=1 starts-at=28 OK (stage T-09)
T-09.4   tests/test_nulls.py:18   occurrences=1 starts-at=18 OK (stage T-09)
T-09.3   tests/test_nulls.py:11   occurrences=1 starts-at=11 OK (stage T-09)
after stage T-09: gate exit 0: 42 passed, 1 warning in 19.35s · lint exit 0: All checks passed!
T-05.2   tests/api/test_contract_conformance.py:108  occurrences=1 starts-at=108 OK (stage T-05)
T-05.1   tests/api/test_contract_conformance.py:24   occurrences=1 starts-at=24 OK (stage T-05)
T-05.6   tests/test_nulls.py:30   occurrences=1 starts-at=30 OK (stage T-05)
T-05.5   tests/test_nulls.py:24   occurrences=1 starts-at=24 OK (stage T-05)
T-05.4   tests/test_nulls.py:15   occurrences=1 starts-at=15 OK (stage T-05)
T-05.3   tests/test_nulls.py:11   occurrences=1 starts-at=11 OK (stage T-05)
after stage T-05: gate exit 0: 40 passed, 1 warning in 19.72s · lint exit 0: All checks passed!
T-07.2   tests/api/test_contract_conformance.py:108  occurrences=1 starts-at=108 OK (stage T-07)
T-07.1   tests/api/test_contract_conformance.py:24   occurrences=1 starts-at=24 OK (stage T-07)
T-07.3   tests/test_nulls.py deleted
after stage T-07: gate exit 0: 38 passed, 1 warning in 20.40s · lint exit 0: All checks passed!
after all four: Null modules left: none; tests/test_nulls.py exists: False; imports of a Null module under src/ and tests/: none

all blocks matched: True
~~~

The script (`pack_rehearse.py`):
~~~python
"""Re-runs the mechanical claims of docs/PACK-q07-retire-amends.md on scratch exports of its snapshot.

Never writes to the repository: blobs are read with `git show`, trees exported with `git archive`, and every
write lands under <scratch>. Run with the project's venv interpreter, isolated:
    python -I pack_rehearse.py <repo> <pack.md> <scratch> [<plugin-root>]
"""

from __future__ import annotations

import io
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
    r"^#### (?P<id>[BTE]-[\w.]+) · (?P<file>[^\s:]+):(?P<line>\d+)[^\n]*\n"
    r"(?:(?!#### |replace exactly)[^\n]*\n)*"
    r"replace exactly(?P<inline> \(within the line\))?:\n~~~text\n(?P<old>[\s\S]*?)~~~\n"
    r"with:\n~~~text\n(?P<new>[\s\S]*?)~~~\n",
    re.M,
)
DELETE = re.compile(r"^#### (?P<id>T-[\w.]+) · (?P<file>\S+) — delete the file$", re.M)


def blocks(text: str) -> list[dict]:
    out = []
    for m in BLOCK.finditer(text):
        old, new = m["old"], m["new"]
        if m["inline"]:
            old, new = old[:-1], (new[:-1] if new.endswith("\n") else new)
        out.append({"id": m["id"], "file": m["file"], "line": int(m["line"]), "old": old, "new": new,
                    "inline": bool(m["inline"])})
    return out


def locate(text: str, b: dict) -> tuple[int, int | None]:
    n = text.count(b["old"])
    if n != 1:
        return n, None
    pos = text.find(b["old"])
    if not b["inline"] and pos and text[pos - 1] != "\n":
        return n, -1  # matched mid-line
    return n, text.count("\n", 0, pos) + 1


def apply_group(texts: dict[str, str], group: list[dict], label: str, report: list[str]) -> bool:
    ok = True
    by_file: dict[str, list[dict]] = {}
    for b in group:
        by_file.setdefault(b["file"], []).append(b)
    for f, bs in by_file.items():
        text = texts[f]
        for b in sorted(bs, key=lambda x: x["line"], reverse=True):  # bottom-up: every stated line stays valid
            n, line = locate(text, b)
            good = n == 1 and line == b["line"]
            ok &= good
            report.append(f"{b['id']:8} {f}:{b['line']:<4} occurrences={n} starts-at={line} {'OK' if good else 'MISMATCH'}"
                          f" ({label})")
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


def gate(tree: Path) -> str:
    r = run([str(PY), "-m", "pytest", "tests/", "-q", "-m", "not timing", "-p", "no:cacheprovider"], tree)
    lint = run([str(RUFF), "check"], tree)
    return f"gate exit {r.returncode}: {last(r.stdout, r'passed|failed|error')} · lint exit {lint.returncode}: " \
           f"{last(lint.stdout + lint.stderr, r'.')}"


# ---- scaffolding for the rehearsal only: stand-ins for the real services, never proposed text
STAND_INS = {
    "src/app/identity/service.py": '''"""Rehearsal stand-in (scratch only, not the product): a MemberDirectory on an empty workspace."""

from __future__ import annotations

from app.ports import Caller, MemberNotFound, Role


class IdentityService:
    def caller_for_token(self, token: str) -> Caller | None:
        return None

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
STAGES = [  # (stage, Null module, stand-in, main.py rebinding)
    ("T-03", "src/app/identity/null_directory.py", "src/app/identity/service.py", [
        ("from app.identity.null_directory import NullDirectory\n", "from app.identity.service import IdentityService\n"),
        ("member_directory=member_directory or NullDirectory(),  # replaced by ADU-03",
         "member_directory=member_directory or IdentityService(),")]),
    ("T-09", "src/app/notifications/null_notifier.py", "src/app/notifications/service.py", [
        ("from app.notifications.null_notifier import NullNotifier\n",
         "from app.notifications.service import NotificationsService\n"),
        ("notifier=notifier or NullNotifier(),  # replaced by ADU-09", "notifier=notifier or NotificationsService(),")]),
    ("T-05", "src/app/scheduling/null_port.py", "src/app/scheduling/service.py", [
        ("from app.scheduling.null_port import NullSchedulingPort\n", "from app.scheduling.service import SchedulingService\n"),
        ("scheduling=scheduling or NullSchedulingPort(),  # replaced by ADU-05",
         "scheduling=scheduling or SchedulingService(),")]),
    ("T-07", "src/app/swaps/null_port.py", "src/app/swaps/service.py", [
        ("from app.swaps.null_port import NullSwapsPort\n", "from app.swaps.service import SwapsService\n"),
        ("swaps=swaps or NullSwapsPort(),  # replaced by ADU-07", "swaps=swaps or SwapsService(),")]),
]
REFUSED = ("        self.reason = reason\n",
           '        self.reason = reason\n\n\nclass Refused(Exception):\n'
           '    """Illustrative D-p2 shape (rehearsal only): a refusal a story names; no HTTP status."""\n\n'
           '    def __init__(self, reason: str, detail: str = "", **extra: object) -> None:\n'
           '        super().__init__(reason)\n'
           '        self.reason, self.detail, self.extra = reason, detail, extra\n')


def scaffold(tree: Path, null: str, stand_in: str, rebinding: list[tuple[str, str]], refused: bool) -> None:
    (tree / null).unlink()
    write(tree, stand_in, STAND_INS[stand_in])
    main = read(tree, "src/app/main.py")
    for old, new in rebinding:
        assert main.count(old) == 1, old
        main = main.replace(old, new)
    write(tree, "src/app/main.py", main)
    if refused:
        ports = read(tree, "src/app/ports.py")
        assert ports.count(REFUSED[0]) == 1
        write(tree, "src/app/ports.py", ports.replace(*REFUSED))


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8")  # adu prints "→"; a cp1252 console would die on it (FB-01's lesson)
    pack = PACK.read_text(encoding="utf-8").replace("\r\n", "\n")
    allb = blocks(pack)
    deletes = [m.groupdict() for m in DELETE.finditer(pack)]
    report: list[str] = []
    ok = True
    print(f"pack: {PACK} · {len(allb)} replace blocks · {len(deletes)} file deletions · snapshot {SNAP}")

    # 1. B-blocks against the snapshot's blobs; the post-B text of every document
    bgroup = [b for b in allb if b["id"].startswith("B-")]
    post = {f: git_show(f) for f in {b["file"] for b in bgroup}}
    ok &= apply_group(post, bgroup, "against the 7d1e7d4 blob", report)

    # 2. E-blocks against the text as B leaves it, each option alone and both (b)s together (disjointness)
    for label, prefixes in (("E-2b on post-B", ("E-2b",)), ("E-3b on post-B", ("E-3b",)),
                            ("E-2b + E-3b on post-B", ("E-2b", "E-3b"))):
        eg = [b for b in allb if b["id"].startswith(prefixes)]
        texts = dict(post)
        for f in {b["file"] for b in eg} - set(texts):
            texts[f] = git_show(f)
        ok &= apply_group(texts, eg, label, report)
    print("\n".join(report))

    # 3. export A: B-3 applied; plan check and order; guard at the snapshot (export H) and after B-3 (export A)
    a, h = export("A-plan-and-stages"), export("H-pristine")
    b3 = [b for b in bgroup if b["file"] == "ADU-PLAN.md"]
    write(a, "ADU-PLAN.md", post["ADU-PLAN.md"])
    for label, tree in (("scratch copy with B-3 applied", a),):
        for args in (("plan", "check"), ("plan", "order")):
            r = adu(tree, *args)
            print(f"\n$ adu {' '.join(args)}   # {label}, exit {r.returncode}\n{(r.stdout + r.stderr).rstrip()}")
    print(f"\n(B-3 blocks applied: {len(b3)})")
    for label, tree in (("at 7d1e7d4", h), ("with B-3 applied", a)):
        for p in ("tests/test_nulls.py", "tests/api/test_contract_conformance.py", "src/app/ports.py"):
            r = adu(tree, "guard", "edit", p, "--role", "developer")
            msg = (r.stdout + r.stderr).strip().replace("\n", " ")
            print(f"guard edit {p} --role developer ({label}) -> exit {r.returncode}: {msg[:150]}")

    # 4. export C: B-3 plus E-2b on the plan
    c = export("C-plan-E2b")
    e2b = {"ADU-PLAN.md": post["ADU-PLAN.md"]}
    apply_group(e2b, [b for b in allb if b["id"].startswith("E-2b") and b["file"] == "ADU-PLAN.md"], "E-2b", [])
    write(c, "ADU-PLAN.md", e2b["ADU-PLAN.md"])
    for args in (("plan", "check"), ("plan", "order")):
        r = adu(c, *args)
        print(f"\n$ adu {' '.join(args)}   # scratch copy with B-3 and E-2 (b), exit {r.returncode}\n"
              f"{(r.stdout + r.stderr).rstrip()}")

    # 5. the stages, in the derived order, on export A
    print(f"\nbaseline (export A, B-3 applied, no stage yet): {gate(a)}")
    for stage, null, stand_in, rebinding in STAGES:
        refused = stage == "T-03"
        scaffold(a, null, stand_in, rebinding, refused)
        if refused:  # the twins: each part of T-03 is needed
            r = run([str(PY), "-m", "pytest", "tests/api/test_contract_conformance.py", "-q", "-p", "no:cacheprovider"], a)
            print(f"twin 1 (Null deleted, conformance test unedited): exit {r.returncode}: "
                  f"{first(r.stdout, r'ModuleNotFoundError')} | {last(r.stdout, r'error|passed|failed')}")
            conf = {"tests/api/test_contract_conformance.py": read(a, "tests/api/test_contract_conformance.py")}
            partial = [b for b in allb if b["id"] in ("T-03.3", "T-03.6")]
            apply_group(conf, partial, "twin 2", [])
            write(a, "tests/api/test_contract_conformance.py", conf["tests/api/test_contract_conformance.py"])
            r = run([str(PY), "-m", "pytest", "tests/api/test_contract_conformance.py", "-q", "-p", "no:cacheprovider",
                     "--tb=line"], a)
            print(f"twin 2 (import and class check edited, no injected directory): exit {r.returncode}: "
                  f"{first(r.stdout, r'test_contract_conformance\.py:\d+: ').split('tests' + chr(92) + 'api' + chr(92))[-1][:170]} | {last(r.stdout, r'passed|failed')}")
            write(a, "tests/api/test_contract_conformance.py", git_show("tests/api/test_contract_conformance.py"))
        group = [b for b in allb if b["id"].startswith(stage + ".")]
        texts = {f: read(a, f) for f in {b["file"] for b in group}}
        srep: list[str] = []
        ok &= apply_group(texts, group, f"stage {stage}", srep)
        for f, t in texts.items():
            write(a, f, t)
        for d in deletes:
            if d["id"].startswith(stage + "."):
                (a / d["file"]).unlink()
                srep.append(f"{d['id']:8} {d['file']} deleted")
        print("\n".join(srep))
        print(f"after stage {stage}: {gate(a)}")
    left = [str(p.relative_to(a)) for p in (a / "src").rglob("null_*.py")]
    imports = run(["git", "grep", "--no-index", "-I", "-n", "-E", r"null_(directory|notifier|port)", "--", "src", "tests"], a)
    print(f"after all four: Null modules left: {left or 'none'}; tests/test_nulls.py exists: "
          f"{(a / 'tests/test_nulls.py').exists()}; imports of a Null module under src/ and tests/: "
          f"{imports.stdout.strip() or 'none'}")
    print(f"\nall blocks matched: {ok}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
~~~

### B-5 Questions (provisional)
Q-p1 … Q-p5, in full, are the text B-2.7 enters into OPEN-QUESTIONS.md (each with its allocated id). In short:
- **Q-p1 (blocking ADU-03):** how the IdentityService, bound once, reaches the request's session. Recommended (b): a request-scoped current session set by an async dependency, for all four services. Measured: a ContextVar set in a sync generator dependency is invisible to the endpoint; set in an async one, it is visible (the probe below).
- **Q-p2 (blocking ADU-03):** how it receives its collaborators across the identity ↔ scheduling cycle. Recommended (b): the composition root's `Ports` container, read at call time.
- **Q-p3 (blocking ADU-03):** the token and salt source against "No randomness in the product". Recommended (a): an injected `secrets`-based source and a DECISIONS row amending ARCHITECTURE.md:45.
- **Q-p4 (blocking ADU-03):** the returned values and their home. Recommended (a): the contract's Member fields, values defined in identity's service module; PRODUCT-DESIGN.md:18 reworded editorially.
- **Q-p5 (blocking ADU-04, not M2):** the API units' wall on the same test and the helpers in contract_stubs.py. Recommended (b): one re-cut before ADU-04.

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
| "the five protocols" | stays | ADU-PLAN.md:99, design/ARCHITECTURE.md:18, design/INTERFACES.md:4: `Refused` is an exception like `TransferRefused`, not a protocol |
| `test_the_composition_root_binds_a_null_per_port_and_an_injectable_clock` (E-4 a) | `test_the_composition_root_binds_an_implementation_per_port_and_an_injectable_clock` | tests/api/test_contract_conformance.py:102 only (`git grep` finds no other reference): renamed by ADU-03's session, not by the apply |
| design/INTERFACES.md v1.0.1 | v1.1 | INTERFACES.md:2 (B-2.2); VERSIONS.md Current has no INTERFACES row at 7d1e7d4 (B-2.8) |
| ADU-PLAN v1.2 | v1.3 | ADU-PLAN.md:2 (B-3.1); VERSIONS.md:14 (B-2.8) |
| Q-07 open, blocking | resolved → D-p1 | OPEN-QUESTIONS.md:53, :59 (B-2.6, B-2.7); `adu status` reads it from there |
| "each with a `Null<Interface>` in the contract unit" | stays (observed, not this change's term) | design/INTERFACES.md:2: stale since v1.0.1 moved the Nulls to ADU-16 (:14 says so); an editorial fix for the next INTERFACES patch, recorded here so it is not lost |
| the ADU-03 hand-over (`adu handover ADU-03`) | regenerated after the apply | it must list the `amends` files and the two grant steps (plugin FB-30 (1): C1 omits `amends`; plugin FB-28: no grant step) — the oversight session's D-0 check |

## Part D — prompts

### D-1 The verify prompt
For a fresh `claude --plugin-dir C:\dev\adu-lifecycle --agent adu-lifecycle:verifier`, started from a PowerShell inside `C:\dev\team-rota`:

~~~text
Verification round for Team Rota: /adu-lifecycle:verify docs/PACK-q07-retire-amends.md

You are a fresh verifier; you did not write this pack, and you change nothing in the repository except your report and your journal block.

1. `adu status`: expect Now: ADU-03 and Q-07 open and blocking (the pack answers Q-07; it does not open ADU-03). Before any `uv` or python command confirm `$env:UV_PROJECT_ENVIRONMENT` is `C:\dev\team-rota-data\.venv` (the User-level variable names another project's venv) and that `$env:PYTHONUTF8` is empty. `git status --short` is expected to show `?? uv.lock` (Q-05) and, if the operator has not committed the pack yet, `?? docs/PACK-q07-retire-amends.md`.
2. Snapshot gate: `adu snapshot check 7d1e7d4`. Exit 2 → the report is the command's output and `VERDICT: STOP — STALE`; nothing else is verified.
3. Read the pack in full; then OPEN-QUESTIONS.md:53–59 (Q-07), the SESSION-JOURNAL.md blocks of 2026-11-07 20:20 (the hand-over that raised Q-07) and of the pack's drafting session (2026-11-08), and any docs/VERIFICATION-*.md.
4. Claims, each CONFIRMED / WRONG / UNVERIFIABLE with file and line:
   a. every B-block (B-2.1–B-2.9, B-3.1–B-3.14) against the 7d1e7d4 blob (`git show 7d1e7d4:<file>`): text character for character with line endings normalised, unique in its file, starting at the stated line;
   b. every T-block (B-2.T) against the file as the previous T-stage leaves it, starting from 7d1e7d4 for T-03; each E-block against the text as B leaves it;
   c. Part A-2's table, row by row, including: FakeMemberDirectory resolves no token until `add(…, token=…)` (tests/support/doubles.py:95–112); the stubs answer 501 to any resolved caller (src/app/api/contract_stubs.py:82–84, :118–123); plugin scripts/adu.mjs:687, :692–693 and :704 say what the pack says (plugin at C:\dev\adu-lifecycle);
   d. the guard: at 7d1e7d4, `adu guard edit tests/test_nulls.py --role developer` and `adu guard edit tests/api/test_contract_conformance.py --role developer` refused as completed units' tests, `adu guard edit src/app/ports.py --role developer` refused as outside ADU-03's roster; on a scratch export with B-3 applied, the two tests still refused (FB-28) and ports.py allowed;
   e. every amendment names the file and the assertion it falsifies, in both directions (each B-3 `amends` line names its T-blocks; each T-block is named by a B-3 line);
   f. that no arm is weakened: compare each replaced arm with the arm it replaces and with ADU-02's arms (ADU-PLAN.md:126–133) and ADU-16's (:99–104); say how each rewritten arm can fail;
   g. that the IdentityService section (B-2.3) contains nothing the arms (ADU-PLAN.md:159–165), R-identity-01..09 (design/domains/identity/spec.md:7–15) and contracts/openapi.yaml do not settle, other than what it marks open (Q-p1–Q-p4).
5. Measurements, in your own scratchpad, never in the repository: (i) `git archive 7d1e7d4` into a scratch folder, apply B-3, run `adu plan check` and `adu plan order` with the working directory inside the copy; compare with B-3.15; repeat with E-2 (b)'s blocks on top; (ii) re-run the rehearsal of B-4.3 (the pack's script, or your own equivalent) and compare per stage the gate count, the lint, and the twins; (iii) re-run the ContextVar probe of B-5 and compare. Table: the pack's value · yours · verdict per cell.
6. Optional, once: `uv run pytest tests/ -q -m "not timing" -p no:cacheprovider` at HEAD, expect `46 passed`; `git status --short` unchanged afterwards.
7. The report: docs/VERIFICATION-<id>.md (`adu next-id V`) in the skill's report shape, the verdict as its last line and the token VERDICT nowhere else; `adu verdict check docs/VERIFICATION-<id>.md` passes; then your journal block. Write nothing else.
~~~

### D-2 The apply prompt
For a fresh `claude --plugin-dir C:\dev\adu-lifecycle --agent adu-lifecycle:release-manager`, started from a PowerShell inside `C:\dev\team-rota`, after the verifier's report and the operator's rulings on Part E:

~~~text
Design-change loop, stage 4 (apply) for Team Rota: /adu-lifecycle:change-design apply docs/PACK-q07-retire-amends.md

Preconditions — stop and tell me if any fails: docs/VERIFICATION-<id>.md for this pack ends `VERDICT: READY` or `VERDICT: READY WITH MECHANICAL ADAPTATIONS`; my rulings on Part E (E-1 … E-5) are pasted at the end of this prompt, verbatim; `adu snapshot check 7d1e7d4` exits 0; `$env:UV_PROJECT_ENVIRONMENT` is `C:\dev\team-rota-data\.venv` and `$env:PYTHONUTF8` is empty.

1. First: re-derive every provisional identifier against HEAD and record the mapping in docs/APPLICATION-REPORT-q07-retire-amends.md (from the plugin's templates/reports/APPLICATION-REPORT.md): D-p1 and D-p2 with `adu next-id D` (D-12 and D-13 if main took none), Q-p1 … Q-p5 with `adu next-id Q` (Q-08 … Q-12 if main took none). Replace every provisional id, every `<apply-date>` and `docs/VERIFICATION-<id>.md` in the text you apply. Never renumber to dodge a number main took.
2. Apply B-2.1–B-2.9 and B-3.1–B-3.14 block by block, bottom-up within each file, each `replace exactly` matching character for character with line endings normalised; a miss is a stop, not a guess. For each Part E bracket apply the text of the option I ruled (its E-blocks on top of B); a ruled option whose text is not in the pack stops the apply. Do not apply B-2.T: those edits belong to the retiring units' sessions, each under its own grant.
3. Chase every row of Part C with `adu chase "<old>" "<new>"`; change each hit or record in the application report why it stays.
4. Make the verification report's mechanical adaptations in the governing documents (never in the pack). Then `adu derived render`; `adu plan check` (expect `plan OK: 18 units` and the order of B-3.15); `adu derived check`; `adu ledger lint`; `adu pins check` (no pinned file changes).
5. Versions as B-2 writes them: ADU-PLAN 1.2 → 1.3, design/INTERFACES.md 1.0.1 → 1.1 (it gains the Current row it lacked). Q-07 resolved as B-2.6–B-2.7 write it; Q-p1 … Q-p5 entered with their allocated ids.
6. Run the gate once: `uv run pytest tests/ -q -m "not timing"`; expect `46 passed` (STATUS.md:40; this loop changes no test). Any other count is a stop. Then your journal block and a STATUS Log line ending `backward: n/a (documents only)`. I commit: `docs: apply pack q07-retire-amends (ADU-PLAN v1.3, INTERFACES v1.1)`.
7. NEXT in your journal block: if E-5 (a) was ruled, ADU-03 still does not open — I rule the allocated Q-p1 … Q-p4 first. When ADU-03 is handed over, its prompt says "design updated: ADU-PLAN v1.3 (ADU-03's amends and arm 1; the same pattern in ADU-09, ADU-05, ADU-07), INTERFACES v1.1 (§Refused, §Domain services — IdentityService, the retirement paragraph)", and its first section names the two grants the session asks me for (`tests/api/test_contract_conformance.py`, `tests/test_nulls.py`), since the guard does not honour amends on a completed unit's test (plugin FB-28).

My rulings on Part E:
<paste here>
~~~

## Part E — the operator's decisions
Each bracket's options have their text in this pack. An option without text stops the apply, and E-1 (c) is such an option.

**1. Which double answers `Bearer tok_1` in the 401/501 test.** No existing double resolves `tok_1` as constructed (Part A-2).
[(a) recommended: `FakeMemberDirectory`, configured in the test with `add(1, "Member 1", "member", token="tok_1")`, the same Caller the Null gave; nothing but the test changes (T-03.2, T-03.4, B-3.3, B-2.4)
| (b) a new double `TokenDirectory` in tests/support/doubles.py that resolves any `tok_<id>` as the Null did; ADU-03 gains `{ unit: ADU-16, file: tests/support/doubles.py, assertion: "gains TokenDirectory, a MemberDirectory double that resolves tok_<id> to an active member 'Member <id>' of role member, as the retired NullDirectory did; nothing else in the module changes", q: Q-07 }` (a `files` path, so no grant); T-03.2 reads `from support.doubles import FixedClock, TokenDirectory  # noqa: E402`; T-03.4's three lines become `    client = TestClient(create_app(workspace=tmp_path, member_directory=TokenDirectory()))`, so the later conformance lines move up by 2 (T-09.2 :108, T-05.2 :106, T-07.2 :106; with E-4 (b) as well, by 4); in B-3.3 and B-2.4 "FakeMemberDirectory holding member 1 ('Member 1', member, active) with token tok_1" becomes "TokenDirectory" — consequence: the Null's behaviour lives on under another name, and tests/test_ports.py does not cover the new double
| (c) the real IdentityService with an admin seeded in tmp_path and the token sign_in issues — no text in this pack: the edit depends on Q-p1–Q-p4; choosing it stops the apply]

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
If (b) is ruled, B-3.4's ports.py line reads "gains Refused(reason, **extra)" in place of "gains Refused(reason, detail, **extra)". If E-2 (b) is also ruled, that line is gone. The Invariants clause "tests assert `.reason`, never `.detail`" reads "tests assert `.reason`" (design/INTERFACES.md:85, within the line).

**4. The composition-root test's name and the module docstring, which say "binds a Null per port".** Both are false from ADU-03 on.
[(a) recommended: ADU-03 renames the test to `test_the_composition_root_binds_an_implementation_per_port_and_an_injectable_clock` and rewords the docstring (T-03.5, T-03.1). The new name holds in every state, Nulls included, so no later unit renames again. `git grep` finds no other reference to the old name
| (b) both unchanged: drop T-03.1 and T-03.5; in B-3.3's conformance line delete the clause "; the composition-root test is renamed test_the_composition_root_binds_an_implementation_per_port_and_an_injectable_clock and the module docstring reads 'binds an implementation of each port (the Null until its provider lands)'"; the later conformance lines move up by 2 (T-09.2 :108, T-05.2 :106, T-07.2 :106; with E-1 (b) as well, by 4) — consequence: a test whose name states what is no longer true]

**5. The status of the questions this loop raises (B-5).**
[(a) recommended: Q-p1–Q-p4 enter OPEN-QUESTIONS as open and blocking ADU-03, and Q-p5 as open and blocking ADU-04. Q-07 is resolved by this apply, but ADU-03 opens only after you rule Q-p1–Q-p4 (in the oversight session, as Q-07 was), and their text is written by the next design-change loop
| (b) Q-p1–Q-p4 non-blocking: in B-2.7 each `**Blocking:** yes — for ADU-03 …` line reads `**Blocking:** no — ADU-03's session proceeds on the recommended option, stated in its journal block as the assumption (Q-02's pattern).` Consequence: ADU-03 opens at once, but ADU-04, ADU-09 and ADU-05 inherit four choices made by a unit session rather than by you]
