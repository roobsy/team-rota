# ADU-PLAN — Team Rota
v1.1 · cut by the architect (`/adu-lifecycle:cut-adus`) on 2026-11-07 from stories v1.7 (D-02), contracts/openapi.yaml v1.1, design/INTERFACES.md v1.0.1 and design/ARCHITECTURE.md v1.1; recut after the developer's buildability read (docs/PLAN-REVIEW-1.md, 23 findings, all accepted). Nothing is cut from prose alone. Each entry's `yaml adu` block is normative; the prose lines under it are rendered from the block (`adu derived render`) and never edited by hand. The order is derived (`adu plan order`), never typed; ids are stable and allocated with `adu next-id ADU`; an inserted unit gets a new id, never a letter (ADU-16 and ADU-17 were inserted by the recut and take their derived places).

The entry format and its rules are documented in the plugin's `templates/plan/adu-entry.md`. `adu plan check` enforces them: every session opens with it, and ADU-00's method guard runs it as a test.

**Shape of the cut.** Foundations: ADU-00 method guard · ADU-01 data model and the seeded fixture · ADU-16 the five ports, their Null implementations and the permanent test doubles · ADU-02 the contract unit (the served contract pinned byte for byte, every operation a 501 placeholder until its router lands). Then per domain a layer-3 service unit and a layer-4 API unit (identity, scheduling, swaps, notifications), the browser (the Vite scaffold, the generated client and sign-in, the Team and Week board screens, the swap and notification screens), the operator's seed command and the end-to-end path with packaging. Every cross-domain call goes through a protocol in `src/app/ports.py`; a consumer built before its provider declares the provider's Null as an in-process mock (MK-nn) and tests itself with the doubles in `tests/support/doubles.py`, which no unit deletes; the provider's acceptance retires the mock by rebinding `src/app/main.py` and deleting the Null and its stub test — both declared as `amends`, because they are other units' files. The API units move their operations out of `src/app/api/contract_stubs.py` (declared `amends`), so the served contract — pinned by ADU-02's golden — never changes shape while handlers fill in. Prism is the operator's smoke (`adu.toml [commands] mock`), never a gate test: the gate checks the contract's examples in process. HTTP mocks are the UI's development server, not an ordering device.

## Milestones
<!-- contiguous slices of `adu plan order`; each ends in a usable vertical path -->
| Milestone | Title | Units | Usable path at close |
|---|---|---|---|
| M1 | Foundations | ADU-00, ADU-01, ADU-16, ADU-02 | the served contract equals the golden; every operation answers 501 not_built; the ports exist with Nulls and doubles; the seeded fixture reproduces byte for byte |
| M2 | The four services | ADU-03, ADU-09, ADU-05, ADU-07 | the brief's §6 path (members → week → request → accept → decide, every party notified, the board correct) runs end to end through the four real services under a fixed clock, asserted by ADU-07's tests; every in-process mock retired |
| M3 | The API | ADU-04, ADU-06, ADU-10, ADU-08 | the same path for real personas through the API with curl or the test client, signed in as the seeded fixture's members (the fixture of ADU-01 is the operator's first team until the seed command of M4) |
| M4 | The browser and the operator's command | ADU-12, ADU-17, ADU-13, ADU-14, ADU-11, ADU-15 | the same path in the browser; the operator seeds a real first admin; the E2E test runs on every commit; `app serve` packages it |

**Deviation recorded (rule 17).** The first path a persona can use end to end closes M3, not M2: the derived order's primary tie-break (rule 10, lower layer first) places all four layer-3 services before any layer-4 API, so no contiguous slice ending at M2 can contain an API. Reported to the plugin's feedback ledger. M4 is six units, the cap.

## Mocks
<!-- derived: plan mocks -->
Mock | interface | kind | consumer | provider | status
MK-04 | MemberDirectory | in-process | ADU-02 | ADU-03 | active (provider not built)
MK-01 | SchedulingPort | in-process | ADU-03 | ADU-05 | active (provider not built)
MK-02 | Notifier | in-process | ADU-03 | ADU-09 | active (provider not built)
MK-03 | SwapsPort | in-process | ADU-05 | ADU-07 | active (provider not built)
<!-- /derived -->

## Units
### ADU-00 — Scaffold and method guard
```yaml adu
id: ADU-00
title: Scaffold and method guard
layer: 0
domain: platform
stories: []
provides: [method.guard]
consumes: []
depends: []
files: ["pyproject.toml","src/app/__init__.py","tests/conftest.py","tests/layering_scan.py","tests/layering.json","tests/layering_baseline.json"]
tests: ["tests/test_method.py","tests/test_layering.py","tests/test_tiers.py"]
amends: []
mocks: []
size: M
acceptance:
  - { arm: "the bootstrap manifest and its invariants hold (adu init --check exits 0)", file: tests/test_method.py, kind: deterministic }
  - { arm: "a planted wrong pin in a temporary copy makes adu pins check exit 2 (guard on the guard)", file: tests/test_method.py, kind: deterministic }
  - { arm: "a duplicated '## Now:' line in a temporary copy makes adu ledger lint exit 2", file: tests/test_method.py, kind: deterministic }
  - { arm: "adu plan check exits 0 on the committed plan and 2 on a temporary copy with a planted dependency cycle", file: tests/test_method.py, kind: deterministic }
  - { arm: "the real tree has no forbidden layer crossing and matches the committed baseline (tests/layering.json: frozen is empty — services and the API may import the model, as the architecture allows; only private reaches are frozen; app.cli and app.serve are the root layer)", file: tests/test_layering.py, kind: deterministic }
  - { arm: "a planted forbidden import in a scratch package is caught by the scan (exit 1, the edge named)", file: tests/test_layering.py, kind: deterministic }
  - { arm: "the baseline fails both ways: a new frozen edge and a baseline edge no longer in the code", file: tests/test_layering.py, kind: deterministic }
  - { arm: "every test is in the gate or the timing tier and not both; timing implies calibration; no tier pattern is stale (TIMING_NODES is empty until ADU-05 registers its arm by amendment)", file: tests/test_tiers.py, kind: deterministic }
owed: []
```
The adapter's `pyproject.toml.tmpl` (plus `[project.scripts] app = "app.cli:main"` for ADU-11 and ADU-15), `conftest.py.tmpl`, `test_layering.py.tmpl` and `test_tiers.py.tmpl` are the starting text; the layering scan, its configuration and the baseline generated on the empty tree were committed in the architecture phase and are this unit's to keep current.

### ADU-01 — Data model and the seeded fixture
```yaml adu
id: ADU-01
title: Data model and the seeded fixture
layer: 1
domain: platform
stories: []
provides: [data.model, data.synthetic]
consumes: []
depends: []
files: ["src/app/models.py","src/app/db.py","src/app/synthetic.py","tests/fixtures/seeded_week_20261107.json"]
tests: ["tests/test_models.py","tests/test_synthetic.py"]
amends: []
mocks: []
size: M
acceptance:
  - { arm: "the stored entities of PRODUCT-DESIGN §Entities exist as tables with the key fields (Member, Week keyed by start_date, Shift, Assignment, SwapRequest, Decision, Notification; Role is an enumeration in Member.role), and a fresh SQLite file per workspace path is created on first use (pathlib, tmp_path in tests; never a shared in-memory engine)", file: tests/test_models.py, kind: deterministic }
  - { arm: "the constraints hold at the database: email unique case-insensitively, slots >= 1, role in {admin, planner, member}, week state in {draft, published}, request state in {requested, accepted, declined, approved, refused}; one open request per assignment is the service's rule (documented)", file: tests/test_models.py, kind: deterministic }
  - { arm: "every timestamp column is a naive local datetime and every date a date; ids are integers assigned in creation order; nothing in the model calls the system clock", file: tests/test_models.py, kind: deterministic }
  - { arm: "seeded_week(seed) implements R-scheduling-09 exactly (clock 2026-11-05 09:00; start_date 2026-11-09; 7 days x 08–12, 12–16, 16–20 x 2 slots; member 1 admin, 2–3 planners, 4–12 members, round-robin over all 12 in id order with slots walked by date, start, slot index; the week published; requests on assignments 1–5 in states requested, accepted, requested, accepted, requested, reason other; names, emails under example.test, passcodes and counterparts drawn by the seeded generator) and seeded_week(20261107) reproduces tests/fixtures/seeded_week_20261107.json byte for byte on a second run", file: tests/test_synthetic.py, kind: deterministic }
  - { arm: "a different seed produces different bytes in names and counterparts (the reproduction test can fail)", file: tests/test_synthetic.py, kind: deterministic }
  - { arm: "the fixture file carries the SYNTHETIC header, exposes the passcodes and the admin's token for later units' tests, and no row resembles a real person", file: tests/test_synthetic.py, kind: deterministic }
owed: []
```

### ADU-16 — Ports, Null implementations and test doubles
```yaml adu
id: ADU-16
title: Ports, Null implementations and test doubles
layer: 2
domain: platform
stories: []
provides: [Clock, test.doubles]
consumes: []
depends: []
files: ["src/app/ports.py","src/app/identity/null_directory.py","src/app/scheduling/null_port.py","src/app/swaps/null_port.py","src/app/notifications/null_notifier.py","tests/support/doubles.py"]
tests: ["tests/test_ports.py","tests/test_nulls.py"]
amends: []
mocks: []
size: M
acceptance:
  - { arm: "the five protocols of design/INTERFACES.md (Clock, MemberDirectory, SchedulingPort, SwapsPort, Notifier) exist in ports.py with the stated signatures, the Caller, AssignmentInfo and AssignmentView values and the nine frozen event dataclasses; FixedClock and SystemClock satisfy Clock", file: tests/test_ports.py, kind: deterministic }
  - { arm: "tests/support/doubles.py provides SpyNotifier (records every event), FakeSchedulingPort (settable assignment info, has_assignment_after, holds_intersecting_shift and transfer outcome), FakeSwapsPort (settable view) and FakeMemberDirectory (settable members, callers and deciders), each satisfying its protocol; consumer units test against these, never against a Null", file: tests/test_ports.py, kind: deterministic }
  - { arm: "each Null<Interface> satisfies its protocol, does nothing observable (NullDirectory resolves tok_<id> to an active member for the contract unit's auth; the others answer the empty value) and carries the docstring 'replaced by ADU-nn, class not shape' naming its provider", file: tests/test_nulls.py, kind: deterministic }
  - { arm: "test_nulls.py is one test per Null, each deleted together with its Null by the retiring unit (declared in that unit's amends); the file as a whole is removed with the last Null", file: tests/test_nulls.py, kind: deterministic }
  - { arm: "no port module imports a domain service, the API or the model (the layering scan asserts it)", file: tests/test_ports.py, kind: deterministic }
  - { arm: "a double that round-trips its own input is labelled vacuous in doubles.py and is not used as an oracle by any consumer arm (rule 13)", file: tests/test_ports.py, kind: deterministic }
owed: []
```
Cut out of the contract unit by the developer's read (PLAN-REVIEW-1 findings 1, 16, 18): the doubles must outlive the Nulls, and the contract unit was over the Size L file cap with both.

### ADU-02 — Contract unit: served contract, golden pin, composition root
```yaml adu
id: ADU-02
title: Contract unit — served contract, golden pin, composition root
layer: 2
domain: platform
stories: []
provides: [contract.app, contract.golden]
consumes: [data.model, Clock, MemberDirectory]
depends: [ADU-01, ADU-16]
files: ["src/app/main.py","src/app/api/schemas.py","src/app/api/deps.py","src/app/api/contract_stubs.py","contracts/openapi.golden.json"]
tests: ["tests/api/test_openapi_golden.py","tests/api/test_metadata.py","tests/api/test_contract_conformance.py"]
amends: []
mocks:
  - { id: MK-04, interface: MemberDirectory, kind: in-process, provider: ADU-03, stub: src/app/identity/null_directory.py }
size: M
acceptance:
  - { arm: "the served contract equals contracts/openapi.golden.json byte for byte under the canonical serialisation (sorted keys, no whitespace, ASCII, one line, no trailing newline)", file: tests/api/test_openapi_golden.py, kind: pin, can_fail: "test_an_added_route_breaks_the_equality" }
  - { arm: "an added route and a changed description each break the equality; two builds in one process serve identical bytes; the regeneration command reproduces the committed bytes", file: tests/api/test_openapi_golden.py, kind: deterministic }
  - { arm: "every operation of contracts/openapi.yaml is served with the same operationId, method, path, declared response codes and x-roles, and nothing the contract does not declare is served — except the 501 not_built placeholder every stub answers, which is deliberately outside the contract (absent from the served document, exempt from the conformance helper) and gone once the last router lands (ADU-08)", file: tests/api/test_contract_conformance.py, kind: deterministic }
  - { arm: "a request without a bearer token answers 401 unauthenticated on every served operation except sign-in (deps.py resolves the caller once per request through MemberDirectory — the Null until ADU-03 — and reads body, path and query leniently so that the refusal order holds)", file: tests/api/test_contract_conformance.py, kind: deterministic }
  - { arm: "every x-synthetic example of the contract validates in process against the pydantic schema of api/schemas.py for its operation and code (the contract's examples are the mock; Prism is the operator's smoke through adu.toml [commands] mock, never a gate test — no network at test time)", file: tests/api/test_contract_conformance.py, kind: deterministic }
  - { arm: "the served document passes the field-metadata lint (title, description, example on every property; x-when-to-use on numeric and enum) and the lint fires on a bare property", file: tests/api/test_metadata.py, kind: deterministic }
  - { arm: "the composition root binds an implementation of each protocol (the Null until its provider lands) and the system clock; create_app(clock=FixedClock(...)) injects a test clock; one session per request is opened in deps.py and shared by every service", file: tests/api/test_contract_conformance.py, kind: deterministic }
  - { arm: "the golden is regenerated by `uv run python tests/api/test_openapi_golden.py` and committed in the same change as any contract change admitted by a DECISIONS row", file: tests/api/test_openapi_golden.py, kind: deterministic }
owed: []
```
The golden test file is the adapter's `test_openapi_golden.py.tmpl`; the metadata lint is the adapter's `metadata_lint.py.tmpl` placed inside `tests/api/test_metadata.py`.

### ADU-03 — Identity service
```yaml adu
id: ADU-03
title: Identity service
layer: 3
domain: identity
stories: [US-identity-001, US-identity-002, US-identity-003, US-identity-004, US-identity-005, US-notifications-006]
provides: [MemberDirectory, IdentityService]
consumes: [data.model, Clock, SchedulingPort, Notifier, test.doubles]
depends: [ADU-01, ADU-02, ADU-16]
files: ["src/app/identity/service.py", "src/app/identity/repo.py"]
tests: ["tests/identity/test_service.py"]
amends:
  - { unit: ADU-02, file: src/app/main.py, assertion: "the composition root binds the real IdentityService as MemberDirectory; test_contract_conformance.py still passes", q: none }
  - { unit: ADU-16, file: src/app/identity/null_directory.py, assertion: "deleted (retires MK-04)", q: none }
  - { unit: ADU-16, file: tests/test_nulls.py, assertion: "the NullDirectory test is deleted with its stub", q: none }
mocks:
  - { id: MK-01, interface: SchedulingPort, kind: in-process, provider: ADU-05, stub: src/app/scheduling/null_port.py }
  - { id: MK-02, interface: Notifier, kind: in-process, provider: ADU-09, stub: src/app/notifications/null_notifier.py }
size: M
acceptance:
  - { arm: "retires MK-04: MemberDirectory is bound to the identity service; src/app/identity/null_directory.py and its test_nulls test are deleted; the contract unit's tests stay green unchanged", file: tests/identity/test_service.py, kind: deterministic }
  - { arm: "seed_admin on an empty team creates one active admin (passcode stored as a salted SHA-256) and returns its id, emitting nothing; on a non-empty team it raises Refused(team_not_empty)", file: tests/identity/test_service.py, kind: deterministic }
  - { arm: "add_member creates an active member and notifies them (MemberAdded through the SpyNotifier double); duplicate_email (case-insensitive), invalid_role and forbidden (caller not admin) are raised as Refused with those reasons", file: tests/identity/test_service.py, kind: deterministic }
  - { arm: "change_role changes the role and notifies (RoleChanged); the same role is a no-op that emits nothing; an inactive member's role may change and nobody is notified; last_admin, invalid_role, not_found, forbidden", file: tests/identity/test_service.py, kind: deterministic }
  - { arm: "deactivate sets active false, keeps the row, notifies (MemberDeactivated); future_assignments is raised when the FakeSchedulingPort's has_assignment_after(member, now) is set true; last_admin; member_inactive on a repeat (nothing emitted); not_found; forbidden", file: tests/identity/test_service.py, kind: deterministic }
  - { arm: "sign_in with email (case-insensitive) and passcode issues a token (replacing the earlier one) and returns the member; credentials are verified before the active check; caller_for_token resolves it to a Caller and to None for an unknown token or an inactive member (IR-11); invalid_credentials for a wrong passcode and for an unknown email alike; member_inactive for an inactive member", file: tests/identity/test_service.py, kind: deterministic }
  - { arm: "MemberDirectory is implemented: caller_for_token, is_active (None for an unknown id), role_of (MemberNotFound), name_of, active_member_ids, decider_ids (active admins and planners); list_members returns MemberSummary rows (id, name, role, active — never email, passcode or token), by name (case-insensitively) then id", file: tests/identity/test_service.py, kind: deterministic }
owed: []
```

### ADU-09 — Notifications service
```yaml adu
id: ADU-09
title: Notifications service
layer: 3
domain: notifications
stories: [US-notifications-001, US-notifications-002, US-notifications-003, US-notifications-004, US-notifications-005, US-notifications-006]
provides: [Notifier, NotificationsService]
consumes: [data.model, Clock, MemberDirectory, test.doubles]
depends: [ADU-01, ADU-02, ADU-03, ADU-16]
files: ["src/app/notifications/service.py", "src/app/notifications/repo.py"]
tests: ["tests/notifications/test_service.py"]
amends:
  - { unit: ADU-02, file: src/app/main.py, assertion: "the composition root binds the real Notifier", q: none }
  - { unit: ADU-16, file: src/app/notifications/null_notifier.py, assertion: "deleted (retires MK-02)", q: none }
  - { unit: ADU-16, file: tests/test_nulls.py, assertion: "the NullNotifier test is deleted with its stub", q: none }
mocks: []
size: S
acceptance:
  - { arm: "retires MK-02: Notifier is bound to the notifications service; src/app/notifications/null_notifier.py and its test_nulls test are deleted; the identity tests (which use the SpyNotifier double) stay green unchanged", file: tests/notifications/test_service.py, kind: deterministic }
  - { arm: "notify writes one Notification per recipient of the event with its event code (one of nine), text composed from the payload alone, created_at from the clock and read false, in the caller's session; duplicate recipients are written once; an inactive recipient (FakeMemberDirectory) is skipped except for MemberDeactivated", file: tests/notifications/test_service.py, kind: deterministic }
  - { arm: "list returns only the caller's notifications newest first by created_at then id desc; mark_read sets read, succeeds unchanged on a repeat, refuses not_recipient for someone else's and not_found for an unknown id", file: tests/notifications/test_service.py, kind: deterministic }
  - { arm: "the text for each of the nine events carries the payload fields the stories name (date and start, names, role, reason) and names the state as it is — one assertion per event", file: tests/notifications/test_service.py, kind: deterministic }
owed: []
```

### ADU-05 — Scheduling service
```yaml adu
id: ADU-05
title: Scheduling service
layer: 3
domain: scheduling
stories: [US-scheduling-001, US-scheduling-002, US-scheduling-003, US-scheduling-004, US-scheduling-005, US-scheduling-006, US-notifications-001]
provides: [SchedulingPort, SchedulingService]
consumes: [data.model, data.synthetic, Clock, MemberDirectory, SwapsPort, Notifier, test.doubles]
depends: [ADU-00, ADU-01, ADU-02, ADU-03, ADU-09, ADU-16]
files: ["src/app/scheduling/service.py", "src/app/scheduling/repo.py", "src/app/scheduling/rules.py"]
tests: ["tests/scheduling/test_service.py", "tests/scheduling/test_board_timing.py"]
amends:
  - { unit: ADU-02, file: src/app/main.py, assertion: "the composition root binds the real SchedulingService as SchedulingPort", q: none }
  - { unit: ADU-16, file: src/app/scheduling/null_port.py, assertion: "deleted (retires MK-01)", q: none }
  - { unit: ADU-16, file: tests/test_nulls.py, assertion: "the NullSchedulingPort test is deleted with its stub", q: none }
  - { unit: ADU-00, file: tests/conftest.py, assertion: "TIMING_NODES registers tests/scheduling/test_board_timing.py::test_board_p95 naming its deterministic sibling", q: none }
mocks:
  - { id: MK-03, interface: SwapsPort, kind: in-process, provider: ADU-07, stub: src/app/swaps/null_port.py }
size: M
acceptance:
  - { arm: "retires MK-01: SchedulingPort is bound to the scheduling service; src/app/scheduling/null_port.py and its test_nulls test are deleted; the identity tests (FakeSchedulingPort double) stay green unchanged", file: tests/scheduling/test_service.py, kind: deterministic }
  - { arm: "create_shift creates the week in draft on its first shift (Monday start_date) and refuses not_week_start, outside_week, invalid_interval (times of day, end after start, at most 23:59), invalid_slots, week_published, forbidden; the response is the shift with its holder-rows", file: tests/scheduling/test_service.py, kind: deterministic }
  - { arm: "assign holds a free slot and refuses, in the order of R-scheduling-07, week_published, already_assigned, overlapping_shift ([start, end) on the same date), shift_full, member_inactive (through MemberDirectory), with not_found for an unknown shift or member and forbidden for a member caller; unassign frees a slot in a draft week and refuses week_published and not_found", file: tests/scheduling/test_service.py, kind: deterministic }
  - { arm: "publish requires every slot filled (unfilled: one row per shift with an empty slot, in board order; an unknown start_date is not_found; a second publish is week_published and emits nothing) and notifies every active member of any role once (WeekPublished with MemberDirectory.active_member_ids, IR-12) through the SpyNotifier double", file: tests/scheduling/test_service.py, kind: deterministic }
  - { arm: "the board is {start_date, state, shifts: [{id, date, start, end, slots, holders}]} by date, start, then id, holder-rows by assignment id with assignment id, member id, name (an inactive holder still listed), pending and requestable from SwapsPort.view (the FakeSwapsPort double), honours mine (the caller's shifts with all holder-rows), refuses week_draft to members and not_found for an unknown week; list_weeks returns {weeks, current} newest first (members: published only) with the current week by the clock or null", file: tests/scheduling/test_service.py, kind: deterministic }
  - { arm: "SchedulingPort is implemented: assignment (AssignmentInfo with the shift's times, start_instant, holder_ids and week_state; AssignmentNotFound), holds_intersecting_shift, transfer inside the caller's session (TransferRefused counterpart_overlap — a slot on the same shift counts — or counterpart_inactive, the assignment unchanged; no operation performs it, asserted against the contract's operation ids and the layering scan), has_assignment_after(member, now) over draft and published weeks", file: tests/scheduling/test_service.py, kind: deterministic }
  - { arm: "p95 of the wall-clock duration around each call of the board operation over seeded_week(20261107)", file: tests/scheduling/test_board_timing.py, kind: quantitative, statistic: p95_ms, threshold: 300, n: 50, seed: 20261107, tolerance: "50 ms", tier: timing, measured_by: "uv run python tests/scheduling/test_board_timing.py --measure  (called by the fixture's start_date with mine unset as the fixture's admin; 5 untimed warm-ups; p95 by nearest rank; pass <= 300, 300–350 within tolerance and passes with a report line, > 350 red; reported never gating)" }
  - { arm: "the timing arm's deterministic sibling: the board over seeded_week(20261107) of R-scheduling-09 returns 21 shifts with 42 holder-rows of which 5 carry pending (3 requested, 2 accepted) and, for the fixture's admin as caller, requestable only on the admin's own rows without an open request", file: tests/scheduling/test_service.py, kind: deterministic }
owed: []
```

### ADU-07 — Swaps service
```yaml adu
id: ADU-07
title: Swaps service
layer: 3
domain: swaps
stories: [US-swaps-001, US-swaps-002, US-swaps-003, US-swaps-004, US-swaps-005, US-notifications-002, US-notifications-003, US-notifications-004]
provides: [SwapsPort, SwapsService]
consumes: [data.model, data.synthetic, Clock, SchedulingPort, MemberDirectory, Notifier, IdentityService, SchedulingService, NotificationsService, test.doubles]
depends: [ADU-01, ADU-02, ADU-03, ADU-05, ADU-09, ADU-16]
files: ["src/app/swaps/service.py", "src/app/swaps/repo.py", "src/app/swaps/rules.py"]
tests: ["tests/swaps/test_service.py", "tests/swaps/test_decide.py"]
amends:
  - { unit: ADU-02, file: src/app/main.py, assertion: "the composition root binds the real SwapsService as SwapsPort", q: none }
  - { unit: ADU-16, file: src/app/swaps/null_port.py, assertion: "deleted (retires MK-03)", q: none }
  - { unit: ADU-16, file: tests/test_nulls.py, assertion: "the NullSwapsPort test is deleted with its stub; the file is removed with this last Null", q: none }
mocks: []
size: M
acceptance:
  - { arm: "retires MK-03: SwapsPort is bound to the swaps service; src/app/swaps/null_port.py and its test_nulls test are deleted (test_nulls.py removed with the last Null); the scheduling tests (FakeSwapsPort double) stay green unchanged", file: tests/swaps/test_service.py, kind: deterministic }
  - { arm: "request records state requested with created_at from the clock, answers the request row of R-swaps-09 and notifies the counterpart (SwapRequested); refuses in the design's order not_found (assignment, counterpart) → not_holder → week_draft → request_open → counterpart_self → counterpart_inactive → counterpart_on_shift → counterpart_overlap → past_deadline → reason_required → invalid_reason", file: tests/swaps/test_service.py, kind: deterministic }
  - { arm: "answer is one operation with an outcome: accept sets answered_at and notifies the requester and every eligible decider once each (SwapAccepted; parties removed per R-swaps-05); decline requires answer_reason, sets answered_at and notifies the requester only (SwapDeclined); refuses not_found, not_counterpart, wrong_state (stored state), past_deadline, reason_required, invalid_reason (including a reason sent with accept)", file: tests/swaps/test_service.py, kind: deterministic }
  - { arm: "decide approve calls SchedulingPort.transfer first and then records one Decision (approved) and mirrors the state; refuse records the Decision with the reason; both notify both members less an inactive one (SwapApproved / SwapRefused); a reason with approve, or a system code, is invalid_reason; the response is the request row with the decision embedded", file: tests/swaps/test_decide.py, kind: deterministic }
  - { arm: "decide refuses not_found, party_to_swap for the requester or the counterpart whatever their role, forbidden for a member, wrong_state (stored state), past_deadline, reason_required, invalid_reason; an admin who is not a party decides a request a planner is party to", file: tests/swaps/test_decide.py, kind: deterministic }
  - { arm: "when transfer raises TransferRefused the operation succeeds: the Decision is recorded refused with that reason, the decider is the attempting member, the state mirrors refused, the requester and (if active) the counterpart are notified with the reason", file: tests/swaps/test_decide.py, kind: deterministic }
  - { arm: "mine lists every request the member is party to, every state, newest first by created_at then id desc, as request rows (shift date and start, both names, answer_reason, decision, party true, display state with expired derived from the clock — nothing stored, nobody notified — and awaiting); an inactive other party still listed", file: tests/swaps/test_service.py, kind: deterministic }
  - { arm: "pending lists open accepted requests oldest first by answered_at then id asc as request rows with party per viewer (an accepted request past its deadline is absent), the same for any admin or planner; forbidden for members", file: tests/swaps/test_service.py, kind: deterministic }
  - { arm: "SwapsPort.view takes the caller, the week state and each assignment with its holder and start instant, and returns per assignment pending (the open request state or none) and requestable (own row, published, no open request, now < deadline) without reading scheduling", file: tests/swaps/test_service.py, kind: deterministic }
  - { arm: "the brief's §6 path through the four real services under a FixedClock, from seeded_week(20261107): a member requests, the counterpart accepts, a non-party planner approves; every party's notifications are exactly those of R-notifications-01 and the board shows the new holder (M2's usable path)", file: tests/swaps/test_decide.py, kind: deterministic }
owed: []
```
IdentityService, SchedulingService and NotificationsService are consumed by the §6 arm only, through the composition root; the swaps service itself reaches other domains through the ports alone (the layering scan asserts it).

### ADU-04 — Identity API
```yaml adu
id: ADU-04
title: Identity API
layer: 4
domain: identity
stories: [US-identity-001, US-identity-002, US-identity-003, US-identity-004]
provides: [identity.sign_in, identity.list_members, identity.add_member, identity.change_role, identity.deactivate]
consumes: [contract.app, IdentityService]
depends: [ADU-02, ADU-03]
files: ["src/app/api/identity.py"]
tests: ["tests/api/test_identity.py"]
amends:
  - { unit: ADU-02, file: src/app/api/contract_stubs.py, assertion: "the five identity operations move out of the stubs module; the served contract is unchanged (golden still equal)", q: none }
mocks: []
size: M
acceptance:
  - { arm: "POST /auth/sign-in answers 200 with the token and member for the contract's example, 422 invalid_request for an unreadable body, 401 invalid_credentials (a missing passcode counts), 403 member_inactive", file: tests/api/test_identity.py, kind: deterministic }
  - { arm: "the bearer token resolves the caller for every operation; a missing, unknown or inactive member's token answers 401 unauthenticated", file: tests/api/test_identity.py, kind: deterministic }
  - { arm: "GET /members answers MemberSummary rows (id, name, role, active) by name then id; POST /members (201 the member row; 409 duplicate_email; 422 invalid_role; 403 forbidden), PATCH role (200, 409 last_admin, 422, 403, 404), POST deactivate (200, 409 future_assignments, 409 last_admin, 409 member_inactive, 403, 404) answer the contract's codes and Problem reasons", file: tests/api/test_identity.py, kind: deterministic }
  - { arm: "the served contract still equals the golden after the move (the golden test runs in this unit's gate)", file: tests/api/test_identity.py, kind: deterministic }
  - { arm: "every response body validates against the contract schema for its code (the conformance helper from ADU-02)", file: tests/api/test_identity.py, kind: deterministic }
  - { arm: "the forbidden rule: a planner or member calling add, change role or deactivate answers 403 forbidden", file: tests/api/test_identity.py, kind: deterministic }
owed: []
```

### ADU-06 — Scheduling API
```yaml adu
id: ADU-06
title: Scheduling API
layer: 4
domain: scheduling
stories: [US-scheduling-001, US-scheduling-002, US-scheduling-003, US-scheduling-004, US-scheduling-005]
provides: [scheduling.create_shift, scheduling.assign, scheduling.unassign, scheduling.publish, scheduling.board, scheduling.list_weeks]
consumes: [contract.app, SchedulingService]
depends: [ADU-02, ADU-05]
files: ["src/app/api/scheduling.py"]
tests: ["tests/api/test_scheduling.py"]
amends:
  - { unit: ADU-02, file: src/app/api/contract_stubs.py, assertion: "the six scheduling operations move out of the stubs module; golden unchanged", q: none }
mocks: []
size: M
acceptance:
  - { arm: "POST shifts (201 the shift with holder-rows; 422 not_week_start, outside_week, invalid_interval, invalid_slots; 409 week_published; 403), POST assignments (201; 409 week_published, already_assigned, overlapping_shift, shift_full, member_inactive in that order; 404; 403), DELETE assignment (204; 409 week_published; 404; 403) answer the contract's codes and reasons", file: tests/api/test_scheduling.py, kind: deterministic }
  - { arm: "POST publish answers 200 the week, 409 with the PublishProblem (unfilled rows; week_published on a repeat) and 404 for an unknown start_date", file: tests/api/test_scheduling.py, kind: deterministic }
  - { arm: "GET board answers the Board shape with holder-rows carrying pending and requestable, honours mine, 403 week_draft for a member, 404 for an unknown week; GET weeks answers {weeks, current}", file: tests/api/test_scheduling.py, kind: deterministic }
  - { arm: "the served contract still equals the golden after the move", file: tests/api/test_scheduling.py, kind: deterministic }
  - { arm: "every response body validates against the contract schema for its code", file: tests/api/test_scheduling.py, kind: deterministic }
  - { arm: "the forbidden rule: a member calling create, assign, unassign or publish answers 403 forbidden", file: tests/api/test_scheduling.py, kind: deterministic }
owed: []
```

### ADU-10 — Notifications API
```yaml adu
id: ADU-10
title: Notifications API
layer: 4
domain: notifications
stories: [US-notifications-005]
provides: [notifications.list, notifications.mark_read]
consumes: [contract.app, NotificationsService]
depends: [ADU-02, ADU-09]
files: ["src/app/api/notifications.py"]
tests: ["tests/api/test_notifications.py"]
amends:
  - { unit: ADU-02, file: src/app/api/contract_stubs.py, assertion: "the two notifications operations move out of the stubs module; golden unchanged", q: none }
mocks: []
size: S
acceptance:
  - { arm: "GET /notifications answers the caller's list newest first (and [] for none); POST read answers 200 the item (unchanged on a repeat), 403 not_recipient, 404", file: tests/api/test_notifications.py, kind: deterministic }
  - { arm: "the served contract still equals the golden after the move", file: tests/api/test_notifications.py, kind: deterministic }
  - { arm: "every response body validates against the contract schema for its code", file: tests/api/test_notifications.py, kind: deterministic }
  - { arm: "the forbidden rule and the own rule: another member's notification is not listed and cannot be marked", file: tests/api/test_notifications.py, kind: deterministic }
owed: []
```

### ADU-08 — Swaps API
```yaml adu
id: ADU-08
title: Swaps API
layer: 4
domain: swaps
stories: [US-swaps-001, US-swaps-002, US-swaps-003, US-swaps-004, US-swaps-005]
provides: [swaps.request, swaps.answer, swaps.decide, swaps.mine, swaps.pending]
consumes: [contract.app, SwapsService]
depends: [ADU-02, ADU-07]
files: ["src/app/api/swaps.py"]
tests: ["tests/api/test_swaps.py"]
amends:
  - { unit: ADU-02, file: src/app/api/contract_stubs.py, assertion: "the five swaps operations move out; the stubs module is now empty and deleted (this is the last API unit in the derived order); every operation of the contract is served by a domain router", q: none }
mocks: []
size: M
acceptance:
  - { arm: "POST /swaps answers 201 the request row and each contract refusal (404; 403 not_holder; 409 week_draft, request_open, counterpart_self, counterpart_inactive, counterpart_on_shift, counterpart_overlap, past_deadline; 422 reason_required, invalid_reason, invalid_request)", file: tests/api/test_swaps.py, kind: deterministic }
  - { arm: "POST answer answers 200 accepted/declined rows, 404, 403 not_counterpart, 409 wrong_state/past_deadline, 422", file: tests/api/test_swaps.py, kind: deterministic }
  - { arm: "POST decision answers 200 approved/refused/transfer_refused rows, 404, 403 forbidden/party_to_swap, 409, 422", file: tests/api/test_swaps.py, kind: deterministic }
  - { arm: "GET mine and GET pending answer request rows in the contract's order; pending 403 for a member", file: tests/api/test_swaps.py, kind: deterministic }
  - { arm: "the stubs module is gone, every operation of the contract is served by a domain router, the 501 placeholder no longer exists, and the served contract still equals the golden", file: tests/api/test_swaps.py, kind: deterministic }
  - { arm: "every response body validates against the contract schema for its code; adu release check reports zero active mocks (every Null deleted)", file: tests/api/test_swaps.py, kind: deterministic }
owed: []
```

### ADU-11 — Operator command: seed the first admin
```yaml adu
id: ADU-11
title: Operator command — seed the first admin
layer: 6
domain: identity
stories: [US-identity-005]
provides: [cli.seed_admin]
consumes: [IdentityService, contract.app]
depends: [ADU-02, ADU-03]
files: ["src/app/cli.py"]
tests: ["tests/test_cli.py"]
amends: []
mocks: []
size: S
acceptance:
  - { arm: "app seed-admin --workspace <path> --name --email --passcode on an empty workspace creates the admin through the composition root and prints its id (exit 0), emitting nothing", file: tests/test_cli.py, kind: deterministic }
  - { arm: "on a non-empty team it exits 2 and prints team_not_empty", file: tests/test_cli.py, kind: deterministic }
  - { arm: "the seeded admin's stored passcode hash verifies the given passcode and nothing else", file: tests/test_cli.py, kind: deterministic }
  - { arm: "the command takes the workspace path as a pathlib argument, is the `app` script of pyproject (ADU-00), lives in the root layer (app.cli may import the composition root; the layering scan asserts nothing imports it) and never touches the network", file: tests/test_cli.py, kind: deterministic }
owed: []
```
Layer 6 (the root): the command composes the application like `app serve` will (ADU-15 adds the serve subcommand here by amendment). Its derived place is in M4; until then the operator's first team is the seeded fixture of ADU-01.

### ADU-12 — UI foundation: the Vite scaffold, the shell and the anchor lint
```yaml adu
id: ADU-12
title: UI foundation — the Vite scaffold, the shell and the anchor lint
layer: 5
domain: platform
stories: [US-identity-004, US-scheduling-004]
provides: [ui.shell, ui.anchors]
consumes: []
depends: [ADU-00]
files: ["frontend/package.json","frontend/vite.config.ts","frontend/index.html","frontend/tsconfig.json","frontend/vitest.setup.ts","frontend/src/main.tsx","frontend/src/App.tsx","frontend/src/routes.ts","frontend/src/tour/anchors.json"]
tests: ["frontend/tests/tour-coverage.test.tsx","frontend/tests/shell.test.tsx"]
amends:
  - { unit: ADU-00, file: adu.toml, assertion: "gate, fast and lint regain the frontend commands (Q-04; a protected edit under the operator's grant recorded in the journal)", q: Q-04 }
  - { unit: ADU-00, file: CLAUDE.md, assertion: "the derived commands block is re-rendered by adu derived render (protected; same grant)", q: Q-04 }
mocks: []
size: L
plan_first: true
acceptance:
  - { arm: "npm run build, npm run lint (eslint with typescript-eslint and react-hooks, D-09) and npm run test -- --run succeed on the scaffold; the dependency set is exactly D-09's", file: frontend/tests/shell.test.tsx, kind: deterministic }
  - { arm: "the shell renders the navigation for the six screens of the design with placeholder routes in frontend/src/routes.ts; nothing but the router imports from pages/", file: frontend/tests/shell.test.tsx, kind: deterministic }
  - { arm: "frontend/src/tour/anchors.json lists every data-tour-id anchor of PRODUCT-DESIGN §Screens per route; the tour-coverage lint enumerates screens from the route table and asserts each anchor exists once its screen is built (placeholders carry their anchors as empty elements); the lint fails on a removed anchor", file: frontend/tests/tour-coverage.test.tsx, kind: deterministic }
  - { arm: "vitest runs under jsdom with testing-library's matchers and MSW handlers built from the contract's x-synthetic examples (the examples are the mock, D-09); nothing at test time reaches a non-loopback address", file: frontend/tests/shell.test.tsx, kind: deterministic }
  - { arm: "the dev server points the client at the Prism mock (VITE_API_BASE); the production build is served by app serve (ADU-15) from one port", file: frontend/tests/shell.test.tsx, kind: deterministic }
  - { arm: "adu.toml's gate, fast and lint are the combined commands again and CLAUDE.md's derived block is current (adu derived check green); the gate still passes", file: frontend/tests/shell.test.tsx, kind: deterministic }
owed: []
```
Size L, plan-first. Split from the former single UI foundation unit by PLAN-REVIEW-1 finding 7: the scaffold alone is nine files; the generated client and sign-in are ADU-17.

### ADU-17 — Generated client and sign-in
```yaml adu
id: ADU-17
title: Generated client and sign-in
layer: 5
domain: identity
stories: [US-identity-004]
provides: [ui.client, ui.sign_in]
consumes: [ui.shell, ui.anchors, identity.sign_in, scheduling.list_weeks]
depends: [ADU-04, ADU-06, ADU-12]
files: ["frontend/src/client/schema.d.ts","frontend/src/client/index.ts","frontend/src/hooks/useAuth.ts","frontend/src/pages/SignIn.tsx","frontend/.dependency-cruiser.cjs"]
tests: ["frontend/tests/sign-in.test.tsx","frontend/tests/client-rule.test.ts"]
amends:
  - { unit: ADU-12, file: frontend/src/routes.ts, assertion: "the sign-in route points at the real page; the week-board route remains a placeholder until ADU-13", q: none }
  - { unit: ADU-12, file: frontend/src/tour/anchors.json, assertion: "the Sign in screen's anchors are confirmed against the built page", q: none }
mocks: []
size: M
acceptance:
  - { arm: "frontend/src/client/schema.d.ts is generated from contracts/openapi.yaml by openapi-typescript and frontend/src/client/index.ts (openapi-fetch) is the only module that calls fetch; dependency-cruiser (D-09) forbids any other fetch and any component importing the client directly — hooks only", file: frontend/tests/client-rule.test.ts, kind: deterministic }
  - { arm: "the client sends the bearer token on every call once signed in and surfaces a Problem's reason code to the caller", file: frontend/tests/client-rule.test.ts, kind: deterministic }
  - { arm: "the sign-in-form's sign-in-email and sign-in-passcode submit via sign-in-submit through the client, store the token and the caller, and land on the week-board route for the current week from scheduling.list_weeks (a placeholder page until ADU-13); invalid_credentials and member_inactive are shown with their reason text", file: frontend/tests/sign-in.test.tsx, kind: deterministic }
  - { arm: "the tests use the MSW handlers of ADU-12 for identity.sign_in and scheduling.list_weeks from the contract's examples", file: frontend/tests/sign-in.test.tsx, kind: deterministic }
  - { arm: "every data-tour-id anchor of the Sign in screen exists (the coverage lint of ADU-12 passes)", file: frontend/tests/sign-in.test.tsx, kind: deterministic }
  - { arm: "npm run lint and npm run build stay clean", file: frontend/tests/sign-in.test.tsx, kind: deterministic }
owed: []
```

### ADU-13 — UI: Team and Week board
```yaml adu
id: ADU-13
title: UI — Team and Week board
layer: 5
domain: scheduling
stories: [US-identity-001, US-identity-002, US-identity-003, US-scheduling-001, US-scheduling-002, US-scheduling-003, US-scheduling-004, US-scheduling-005]
provides: [ui.team, ui.board]
consumes: [ui.client, ui.anchors, identity.list_members, identity.add_member, identity.change_role, identity.deactivate, scheduling.create_shift, scheduling.assign, scheduling.unassign, scheduling.publish, scheduling.board, scheduling.list_weeks]
depends: [ADU-04, ADU-06, ADU-12, ADU-17]
files: ["frontend/src/pages/Team.tsx","frontend/src/pages/WeekBoard.tsx","frontend/src/hooks/useTeam.ts","frontend/src/hooks/useBoard.ts"]
tests: ["frontend/tests/team.test.tsx","frontend/tests/board.test.tsx"]
amends:
  - { unit: ADU-12, file: frontend/src/routes.ts, assertion: "the Team and Week board routes point at the real pages", q: none }
  - { unit: ADU-12, file: frontend/src/tour/anchors.json, assertion: "the two screens' anchors are confirmed against the built pages", q: none }
mocks: []
size: M
acceptance:
  - { arm: "the Team screen lists members with role and active state; the member-add form creates one and shows it; member-role and member-deactivate show their refusals (duplicate_email, last_admin, future_assignments, member_inactive) as text with the reason; admin-only controls are hidden from planners and members", file: frontend/tests/team.test.tsx, kind: deterministic }
  - { arm: "the Team screen's anchors (team-list, member-add, member-role, member-deactivate) exist and the coverage lint passes", file: frontend/tests/team.test.tsx, kind: deterministic }
  - { arm: "the week board opens on the current week from scheduling.list_weeks (board-none for none, board-draft for a draft), renders shifts in order with holder-rows, holder-pending-badge with pending's text and nothing for null, holder-request-swap exactly on requestable rows, week-picker from the weeks list (selecting one shows its board), and the planner's shift-create (taking start_date so a new week begins from it), shift-assign, shift-unassign and week-publish controls", file: frontend/tests/board.test.tsx, kind: deterministic }
  - { arm: "board-filter-mine sets the mine parameter; board-empty-mine shows 'No shifts this week'", file: frontend/tests/board.test.tsx, kind: deterministic }
  - { arm: "the publish refusal lists the unfilled shifts from the PublishProblem; week_draft for a member shows the reason", file: frontend/tests/board.test.tsx, kind: deterministic }
  - { arm: "the tests use MSW handlers from the contract's examples; no component imports the client directly (dependency-cruiser)", file: frontend/tests/board.test.tsx, kind: deterministic }
owed: []
```

### ADU-14 — UI: Swap request, Swap inbox, Notifications
```yaml adu
id: ADU-14
title: UI — Swap request, Swap inbox, Notifications
layer: 5
domain: swaps
stories: [US-swaps-001, US-swaps-002, US-swaps-003, US-swaps-004, US-swaps-005, US-notifications-005]
provides: [ui.swaps, ui.notifications]
consumes: [ui.client, ui.anchors, ui.board, swaps.request, swaps.answer, swaps.decide, swaps.mine, swaps.pending, notifications.list, notifications.mark_read, identity.list_members, scheduling.board]
depends: [ADU-04, ADU-06, ADU-08, ADU-10, ADU-12, ADU-13, ADU-17]
files: ["frontend/src/pages/SwapRequest.tsx","frontend/src/pages/SwapInbox.tsx","frontend/src/pages/Notifications.tsx","frontend/src/hooks/useSwaps.ts","frontend/src/hooks/useNotifications.ts"]
tests: ["frontend/tests/swaps.test.tsx","frontend/tests/notifications.test.tsx"]
amends:
  - { unit: ADU-12, file: frontend/src/routes.ts, assertion: "the Swap request, Swap inbox and Notifications routes point at the real pages", q: none }
  - { unit: ADU-12, file: frontend/src/tour/anchors.json, assertion: "the three screens' anchors are confirmed against the built pages", q: none }
mocks: []
size: M
acceptance:
  - { arm: "holder-request-swap on the member's own requestable row opens swap-request-form for that assignment; swap-counterpart offers the eligible members by name (composed from identity.list_members and the board: active, not the requester, not on that shift or an intersecting one that day), swap-reason and swap-submit submit through the client, and swap-inbox shows the new request with swap-state requested; every refusal is shown with its reason code", file: frontend/tests/swaps.test.tsx, kind: deterministic }
  - { arm: "the inbox shows swap-state, swap-awaiting and swap-decision per request row, expired as expired, swap-accept / swap-decline / swap-decline-reason only to the counterpart while open in requested, swap-approve / swap-refuse / swap-refuse-reason only to a non-party admin or planner while open in accepted, and the outcome with the reason after a decision", file: frontend/tests/swaps.test.tsx, kind: deterministic }
  - { arm: "the pending list shows open accepted requests oldest first with swap-party on rows where party is true and no decide controls on them", file: frontend/tests/swaps.test.tsx, kind: deterministic }
  - { arm: "the Notifications screen lists notification-item rows newest first under notification-list, notification-mark-read marks one read, and notification-empty shows 'Nothing yet'", file: frontend/tests/notifications.test.tsx, kind: deterministic }
  - { arm: "every data-tour-id anchor of the three screens exists (coverage lint)", file: frontend/tests/notifications.test.tsx, kind: deterministic }
  - { arm: "the tests use MSW handlers from the contract's examples; no component imports the client directly (dependency-cruiser)", file: frontend/tests/swaps.test.tsx, kind: deterministic }
owed: []
```

### ADU-15 — End-to-end vertical path and packaging
```yaml adu
id: ADU-15
title: End-to-end vertical path and packaging
layer: 6
domain: platform
stories: [US-swaps-001, US-swaps-002, US-swaps-003, US-scheduling-006, US-notifications-001, US-notifications-002, US-notifications-003, US-notifications-004]
provides: [e2e.vertical_path, app.serve]
consumes: [cli.seed_admin, ui.sign_in, ui.board, ui.swaps, identity.add_member, scheduling.publish, swaps.decide, notifications.list, contract.app]
depends: [ADU-00, ADU-02, ADU-04, ADU-06, ADU-08, ADU-10, ADU-11, ADU-12, ADU-13, ADU-14, ADU-17]
files: ["src/app/serve.py","frontend/playwright.config.ts","docs/RUNBOOK.md"]
tests: ["tests/test_e2e_api.py","frontend/tests/e2e/vertical-path.spec.ts"]
amends:
  - { unit: ADU-11, file: src/app/cli.py, assertion: "cli gains the serve subcommand (uvicorn on 127.0.0.1 only, serving the built frontend and the API from one port); seed-admin unchanged", q: none }
  - { unit: ADU-12, file: frontend/vite.config.ts, assertion: "vitest excludes tests/e2e so the Playwright spec is not collected by the unit gate", q: none }
  - { unit: ADU-12, file: frontend/package.json, assertion: "gains the test:e2e script and @playwright/test (D-09)", q: none }
  - { unit: ADU-00, file: tests/conftest.py, assertion: "TIMING_NODES registers tests/test_e2e_api.py::test_gate_budget naming its deterministic sibling", q: none }
  - { unit: ADU-00, file: adu.toml, assertion: "the gate gains `npm --prefix frontend run test:e2e` (protected; the operator's grant) so the E2E runs on every commit", q: none }
mocks: []
size: M
acceptance:
  - { arm: "the brief's §6 path through the API with the real app and a FixedClock: seed admin, add members, create and publish a week, request, accept, approve; every party's notifications are exactly those of R-notifications-01 and the board shows the new holder", file: tests/test_e2e_api.py, kind: deterministic }
  - { arm: "the same path with a refused transfer (counterpart_overlap): the decision is refused with that reason and both members are told", file: tests/test_e2e_api.py, kind: deterministic }
  - { arm: "the same path in the browser (Playwright, D-09, against app serve on loopback and the built frontend, under the product's real clock: the test creates and publishes a week at least two Mondays ahead and reaches it through week-picker): sign in as three members, the board and the inbox show every step; run by `npm --prefix frontend run test:e2e`", file: frontend/tests/e2e/vertical-path.spec.ts, kind: deterministic }
  - { arm: "app serve binds 127.0.0.1 only and serves the built frontend and the API from one port; docs/RUNBOOK.md's commands are executed by the test", file: tests/test_e2e_api.py, kind: deterministic }
  - { arm: "the gate finishes under the budget in adu.toml on the operator's machine", file: tests/test_e2e_api.py, kind: quantitative, statistic: wall_clock_s, threshold: 300, n: 1, seed: 0, tolerance: "60 s", tier: timing, measured_by: "time uv run pytest tests/ -q -m \"not timing\"  (reported, never gating)" }
  - { arm: "adu release check is green: every mock retired, pins match, the plan's derived blocks current", file: tests/test_e2e_api.py, kind: deterministic }
owed: []
```
