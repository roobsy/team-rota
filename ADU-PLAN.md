# ADU-PLAN — Team Rota
v1.0 · cut by the architect (`/adu-lifecycle:cut-adus`) on 2026-11-07 from stories v1.1, contracts/openapi.yaml v1.0, design/INTERFACES.md v1.0 and design/ARCHITECTURE.md v1.0; nothing is cut from prose alone. Each entry's `yaml adu` block is normative; the prose lines under it are rendered from the block (`adu derived render`) and never edited by hand. The order is derived (`adu plan order`), never typed; ids are stable and allocated with `adu next-id ADU`; an inserted unit gets a new id, never a letter.

The entry format and its rules are documented in the plugin's `templates/plan/adu-entry.md`. `adu plan check` enforces them: every session opens with it, and ADU-00's method guard runs it as a test.

**Shape of the cut.** Foundations (ADU-00 method guard · ADU-01 data model · ADU-02 contract unit) then, per domain, a layer-3 service unit and a layer-4 API unit (identity, scheduling, swaps, notifications), the operator's seed command (layer 6), three UI units (layer 5) and the end-to-end vertical path with packaging (layer 6). Every cross-domain call goes through a protocol in `src/app/ports.py` whose `Null<Interface>` the contract unit creates at the provider's future path; a consumer built before its provider declares that stub as an in-process mock (MK-nn) and the provider's acceptance retires it. The API units move their operations out of `src/app/api/contract_stubs.py` (declared `amends`), so the served contract — pinned byte for byte by ADU-02's golden — never changes shape while handlers fill in. HTTP mocks (Prism over the contract's examples) are the UI's development server, not an ordering device: in the derived order every API unit precedes every UI unit, so no `http` mock is declared.

## Milestones
<!-- contiguous slices of `adu plan order`; each ends in a usable vertical path -->
| Milestone | Title | Units | Usable path at close |
|---|---|---|---|
| M1 | Foundations | ADU-00, ADU-01, ADU-02 | the served contract equals the golden; every operation answers 501 not_built; the Prism mock serves the examples |
| M2 | The four services | ADU-03, ADU-09, ADU-05, ADU-07 | the brief's §6 path (seed → members → week → request → accept → decide, every party notified, the board correct) runs end to end through the services in the test harness; every in-process mock retired |
| M3 | The API and the operator's command | ADU-04, ADU-10, ADU-06, ADU-08, ADU-11 | the same path for real personas through the API (generated client or curl): the operator seeds an admin, the admin adds members, a planner publishes a week, a member swaps a shift |
| M4 | The browser | ADU-12, ADU-13, ADU-14, ADU-15 | the same path in the browser; the E2E test runs on every commit; `app serve` packages it |

**Deviation recorded (rule 17).** The first path a persona can use end to end closes M3, not M2. The derived order's primary tie-break (rule 10: lower layer first) places all four layer-3 services before any layer-4 API, so no contiguous slice ending at M2 can contain an API. The alternative — mocking MemberDirectory and SchedulingPort in every consumer so that identity's API could precede scheduling's service — would add four in-process mocks for ordering alone, which rule 12 warns against. M2's "usable path" is therefore the §6 path through the services under a fixed clock, asserted by ADU-07's tests. Reported to the package as feedback (rule 10's tie-break and rule 17 pull against each other for a multi-domain product).

## Mocks
<!-- derived: plan mocks -->
Mock | interface | kind | consumer | provider | status
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
files: ["pyproject.toml","src/app/__init__.py","tests/conftest.py","tests/layering_scan.py","tests/layering.json"]
tests: ["tests/test_method.py","tests/test_layering.py","tests/test_tiers.py"]
amends: []
mocks: []
size: M
acceptance:
  - { arm: "the bootstrap manifest and its invariants hold (adu init --check exits 0)", file: tests/test_method.py, kind: deterministic }
  - { arm: "a planted wrong pin in a temporary copy makes adu pins check exit 2 (guard on the guard)", file: tests/test_method.py, kind: deterministic }
  - { arm: "a duplicated '## Now:' line in a temporary copy makes adu ledger lint exit 2", file: tests/test_method.py, kind: deterministic }
  - { arm: "adu plan check exits 0 on the committed plan and 2 on a temporary copy with a planted dependency cycle", file: tests/test_method.py, kind: deterministic }
  - { arm: "the real tree has no forbidden layer crossing and matches the committed baseline", file: tests/test_layering.py, kind: deterministic }
  - { arm: "a planted forbidden import in a scratch package is caught by the scan (exit 1, the edge named)", file: tests/test_layering.py, kind: deterministic }
  - { arm: "the baseline fails both ways: a new frozen edge and a baseline edge no longer in the code", file: tests/test_layering.py, kind: deterministic }
  - { arm: "every test is in the gate or the timing tier and not both; timing implies calibration; no tier pattern is stale", file: tests/test_tiers.py, kind: deterministic }
owed: []
```
The adapter's `pyproject.toml.tmpl`, `conftest.py.tmpl`, `test_layering.py.tmpl` and `test_tiers.py.tmpl` are the starting text; the layering scan and its baseline were generated on the empty tree in the architecture session.

### ADU-01 — Data model and synthetic generator
```yaml adu
id: ADU-01
title: Data model and synthetic generator
layer: 1
domain: platform
stories: []
provides: [data.model, data.synthetic]
consumes: []
depends: []
files: ["src/app/models.py","src/app/db.py","src/app/synthetic.py"]
tests: ["tests/test_models.py","tests/test_synthetic.py"]
amends: []
mocks: []
size: S
acceptance:
  - { arm: "the eight entities exist as tables with the key fields of PRODUCT-DESIGN §Entities, and a fresh SQLite file per workspace path is created on first use (pathlib, tmp_path in tests; never a shared in-memory engine)", file: tests/test_models.py, kind: deterministic }
  - { arm: "the constraints hold at the database: email unique, slots >= 1, role in {admin, planner, member}, week state in {draft, published}, request state in {requested, accepted, declined, approved, refused}, one open request per assignment is left to the service (documented)", file: tests/test_models.py, kind: deterministic }
  - { arm: "every timestamp column is a naive local datetime and every date a date; nothing in the model calls the system clock", file: tests/test_models.py, kind: deterministic }
  - { arm: "the synthetic generator with seed 20261107 produces the M2 board fixture (12 active members incl. 1 admin and 2 planners, one published week of 7 days x 3 shifts x 2 slots fully assigned, 5 open requests) and reproduces it byte for byte on a second run", file: tests/test_synthetic.py, kind: deterministic }
  - { arm: "a different seed produces different bytes (the reproduction test can fail)", file: tests/test_synthetic.py, kind: deterministic }
  - { arm: "the generated fixture file carries the SYNTHETIC header and no row resembles a real person (names from a fixed synthetic list, emails under example.test)", file: tests/test_synthetic.py, kind: deterministic }
owed: []
```

### ADU-02 — Contract unit: served contract, golden pin, ports and nulls
```yaml adu
id: ADU-02
title: Contract unit — served contract, golden pin, ports and nulls
layer: 2
domain: platform
stories: []
provides: [contract.app, contract.golden, Clock]
consumes: [data.model]
depends: [ADU-01]
files: ["src/app/ports.py","src/app/main.py","src/app/api/schemas.py","src/app/api/deps.py","src/app/api/contract_stubs.py","src/app/identity/null_directory.py","src/app/scheduling/null_port.py","src/app/swaps/null_port.py","src/app/notifications/null_notifier.py"]
tests: ["tests/api/test_openapi_golden.py","tests/api/test_metadata.py","tests/api/test_contract_conformance.py","tests/test_ports.py"]
amends: []
mocks: []
size: L
plan_first: true
acceptance:
  - { arm: "the served contract equals contracts/openapi.golden.json byte for byte under the canonical serialisation (sorted keys, no whitespace, ASCII, one line, no trailing newline)", file: tests/api/test_openapi_golden.py, kind: pin, can_fail: "test_an_added_route_breaks_the_equality" }
  - { arm: "an added route and a changed description each break the equality; two builds in one process serve identical bytes; the regeneration command reproduces the committed bytes", file: tests/api/test_openapi_golden.py, kind: deterministic }
  - { arm: "every operation of contracts/openapi.yaml is served with the same operationId, method, path, declared response codes and x-roles; nothing is served that the contract does not declare", file: tests/api/test_contract_conformance.py, kind: deterministic }
  - { arm: "every served operation answers 501 with a Problem whose reason is not_built until its unit lands, and a request without a bearer token answers 401 unauthenticated (deps.py resolves the caller through MemberDirectory)", file: tests/api/test_contract_conformance.py, kind: deterministic }
  - { arm: "the served document passes the field-metadata lint (title, description, example on every property; x-when-to-use on numeric and enum) and the lint fires on a bare property", file: tests/api/test_metadata.py, kind: deterministic }
  - { arm: "the five protocols of design/INTERFACES.md exist in ports.py with the stated signatures; FixedClock and SystemClock satisfy Clock; each Null<Interface> satisfies its protocol, does nothing observable except what its spy records, and carries the docstring 'replaced by ADU-nn, class not shape'", file: tests/test_ports.py, kind: deterministic }
  - { arm: "the composition root binds the four Null ports and the system clock, and create_app(clock=FixedClock(...)) injects a test clock", file: tests/test_ports.py, kind: deterministic }
  - { arm: "the Prism mock serves every operation from the contract's examples with zero validator errors (docs/CONTRACT-SMOKE.md regenerated by the session and compared)", file: tests/api/test_contract_conformance.py, kind: deterministic }
owed: []
```
Size L: the session presents a plan first. The golden test file is the adapter's `test_openapi_golden.py.tmpl`; the metadata lint is the adapter's `metadata_lint.py.tmpl` placed inside `tests/api/test_metadata.py`.

### ADU-03 — Identity service
```yaml adu
id: ADU-03
title: Identity service
layer: 3
domain: identity
stories: [US-identity-001, US-identity-002, US-identity-003, US-identity-004, US-identity-005, US-notifications-006]
provides: [MemberDirectory, IdentityService]
consumes: [data.model, Clock, SchedulingPort, Notifier]
depends: [ADU-01, ADU-02]
files: ["src/app/identity/service.py","src/app/identity/repo.py"]
tests: ["tests/identity/test_service.py"]
amends: []
mocks:
  - { id: MK-01, interface: SchedulingPort, kind: in-process, provider: ADU-05, stub: src/app/scheduling/null_port.py }
  - { id: MK-02, interface: Notifier, kind: in-process, provider: ADU-09, stub: src/app/notifications/null_notifier.py }
size: M
acceptance:
  - { arm: "seed_admin on an empty team creates one active admin (passcode stored hashed) and returns its id; on a non-empty team it raises Refused(team_not_empty)", file: tests/identity/test_service.py, kind: deterministic }
  - { arm: "add_member creates an active member and notifies them (MemberAdded); duplicate_email (case-insensitive), invalid_role and forbidden (caller not admin) are raised as Refused with those reasons", file: tests/identity/test_service.py, kind: deterministic }
  - { arm: "change_role changes the role and notifies (RoleChanged); last_admin, invalid_role, forbidden", file: tests/identity/test_service.py, kind: deterministic }
  - { arm: "deactivate sets active false, keeps the row, notifies (MemberDeactivated); future_assignments is raised when SchedulingPort.has_assignment_after(member, now) is true; last_admin; member_inactive on a repeat (nothing emitted); forbidden", file: tests/identity/test_service.py, kind: deterministic }
  - { arm: "sign_in with email (case-insensitive) and passcode issues a token (replacing the earlier one) and returns the member; caller_for_token resolves it to a Caller and to None for an unknown token or an inactive member (IR-11); invalid_credentials for a wrong passcode and for an unknown email alike; member_inactive for an inactive member", file: tests/identity/test_service.py, kind: deterministic }
  - { arm: "MemberDirectory is implemented: caller_for_token, is_active (None for an unknown id), role_of (MemberNotFound), name_of, active_member_ids, decider_ids (active admins and planners); list_members returns id, name, role, active only, by name (case-insensitively) then id", file: tests/identity/test_service.py, kind: deterministic }
  - { arm: "the Notifier calls are asserted through the NullNotifier spy (recipients, event, text), never by reading notifications", file: tests/identity/test_service.py, kind: deterministic }
owed: []
```

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
  - { unit: ADU-02, file: src/app/main.py, assertion: "the composition root binds the real IdentityService/MemberDirectory; null_directory.py is deleted; test_ports.py still passes", q: none }
mocks: []
size: M
acceptance:
  - { arm: "retires the null directory: MemberDirectory is bound to the identity service; src/app/identity/null_directory.py is deleted; consumer tests of ADU-02 unchanged and green", file: tests/api/test_identity.py, kind: deterministic }
  - { arm: "POST /auth/sign-in answers 200 with the token and member for the contract's example, 401 invalid_credentials, 403 member_inactive", file: tests/api/test_identity.py, kind: deterministic }
  - { arm: "the bearer token resolves the caller for every other operation; a missing token answers 401 unauthenticated", file: tests/api/test_identity.py, kind: deterministic }
  - { arm: "GET /members, POST /members (201, 409 duplicate_email, 422 invalid_role, 403 forbidden), PATCH role (200, 409 last_admin, 422, 403, 404), POST deactivate (200, 409 future_assignments, 409 last_admin, 403, 404) answer the contract's codes and Problem reasons", file: tests/api/test_identity.py, kind: deterministic }
  - { arm: "the served contract still equals the golden after the move (the golden test is run in this unit's gate)", file: tests/api/test_identity.py, kind: deterministic }
  - { arm: "every response body validates against the contract schema for its code (the conformance helper from ADU-02)", file: tests/api/test_identity.py, kind: deterministic }
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
consumes: [data.model, Clock, MemberDirectory, SwapsPort, Notifier]
depends: [ADU-01, ADU-02, ADU-03, ADU-09]
files: ["src/app/scheduling/service.py","src/app/scheduling/repo.py","src/app/scheduling/rules.py"]
tests: ["tests/scheduling/test_service.py","tests/scheduling/test_board_timing.py"]
amends: []
mocks:
  - { id: MK-03, interface: SwapsPort, kind: in-process, provider: ADU-07, stub: src/app/swaps/null_port.py }
size: M
acceptance:
  - { arm: "retires MK-01: SchedulingPort is bound to the scheduling service; src/app/scheduling/null_port.py is deleted; the identity tests stay green unchanged", file: tests/scheduling/test_service.py, kind: deterministic }
  - { arm: "create_shift creates the week in draft on its first shift (Monday start_date) and refuses not_week_start, outside_week, invalid_interval (times of day, end after start), invalid_slots, week_published, forbidden", file: tests/scheduling/test_service.py, kind: deterministic }
  - { arm: "assign holds a free slot and refuses already_assigned, overlapping_shift ([start, end) on the same date), shift_full, member_inactive (through MemberDirectory), week_published, forbidden; unassign frees a slot in a draft week and refuses week_published", file: tests/scheduling/test_service.py, kind: deterministic }
  - { arm: "publish requires every slot filled (unfilled_slots lists shift id, date, start, unfilled; an unknown start_date is not_found; a second publish is week_published and emits nothing) and notifies every active member of any role once (WeekPublished with MemberDirectory.active_member_ids, IR-12) through the Notifier spy", file: tests/scheduling/test_service.py, kind: deterministic }
  - { arm: "the board lists shifts by date, start, then id with holder-rows (member id, name — an inactive holder still listed) ordered by assignment id, each carrying pending and requestable from SwapsPort.view, honours mine (the caller's shifts with all holder-rows), refuses week_draft to members; list_weeks returns the weeks newest first (members: published only) and the current week by the clock or null", file: tests/scheduling/test_service.py, kind: deterministic }
  - { arm: "SchedulingPort is implemented: assignment (AssignmentInfo with holder_ids and week_state; AssignmentNotFound), holds_intersecting_shift, transfer inside the caller's session (TransferRefused counterpart_overlap — a slot on the same shift counts — or counterpart_inactive, the assignment unchanged; no HTTP route performs it), has_assignment_after(member, now) over draft and published weeks", file: tests/scheduling/test_service.py, kind: deterministic }
  - { arm: "p95 server-side time of the board over the seeded M2 fixture", file: tests/scheduling/test_board_timing.py, kind: quantitative, statistic: p95_ms, threshold: 300, n: 50, seed: 20261107, tolerance: "50 ms", tier: timing, measured_by: "uv run python tests/scheduling/test_board_timing.py --measure  (5 untimed warm-ups, p95 by nearest rank; pass <= 300, 300-350 within tolerance, > 350 red; reported never gating)" }
  - { arm: "the timing arm's deterministic sibling: the board over seeded_week(20261107) of R-scheduling-09 returns 21 shifts with 42 holder-rows of which 5 carry pending (3 requested, 2 accepted) and, for the fixture's admin as caller, requestable only on the admin's own rows without an open request", file: tests/scheduling/test_service.py, kind: deterministic }
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
  - { unit: ADU-02, file: src/app/api/contract_stubs.py, assertion: "the five scheduling operations move out of the stubs module; golden unchanged", q: none }
  - { unit: ADU-02, file: src/app/main.py, assertion: "the composition root binds the real SchedulingService", q: none }
mocks: []
size: M
acceptance:
  - { arm: "POST shifts (201; 422 not_week_start, outside_week, invalid_interval, invalid_slots; 409 week_published; 403), POST assignments (201; 409 x5; 403; 404), DELETE assignment (204; 409; 403; 404) answer the contract's codes and reasons", file: tests/api/test_scheduling.py, kind: deterministic }
  - { arm: "POST publish answers 200, 409 with the PublishProblem (unfilled rows) and 404 for an unknown start_date", file: tests/api/test_scheduling.py, kind: deterministic }
  - { arm: "GET board answers the Board shape with holder-rows and their open_request, honours mine, 403 week_draft for a member, 404 for an unknown week; GET weeks answers the list newest first (members: published only) and the current week or null", file: tests/api/test_scheduling.py, kind: deterministic }
  - { arm: "the served contract still equals the golden after the move", file: tests/api/test_scheduling.py, kind: deterministic }
  - { arm: "every response body validates against the contract schema for its code", file: tests/api/test_scheduling.py, kind: deterministic }
  - { arm: "the forbidden rule: a member calling create, assign, unassign or publish answers 403 forbidden", file: tests/api/test_scheduling.py, kind: deterministic }
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
consumes: [data.model, Clock, SchedulingPort, MemberDirectory, Notifier]
depends: [ADU-01, ADU-02, ADU-03, ADU-05, ADU-09]
files: ["src/app/swaps/service.py","src/app/swaps/repo.py","src/app/swaps/rules.py"]
tests: ["tests/swaps/test_service.py","tests/swaps/test_decide.py"]
amends: []
mocks: []
size: M
acceptance:
  - { arm: "retires MK-03: SwapsPort is bound to the swaps service; src/app/swaps/null_port.py is deleted; the scheduling tests stay green unchanged", file: tests/swaps/test_service.py, kind: deterministic }
  - { arm: "request records state requested with created_at from the clock and notifies the counterpart (SwapRequested); refuses not_holder, week_draft, past_deadline (24 h before start by the clock), request_open, then counterpart_self, counterpart_inactive, counterpart_on_shift, counterpart_overlap in that order (not_found for an unknown counterpart), reason_required, invalid_reason", file: tests/swaps/test_service.py, kind: deterministic }
  - { arm: "answer: accept sets answered_at and notifies the requester and every eligible decider once each (SwapAccepted); decline sets answer_reason and answered_at and notifies the requester only (SwapDeclined); refuses not_counterpart, wrong_state (incl. not open), past_deadline, reason_required, invalid_reason", file: tests/swaps/test_service.py, kind: deterministic }
  - { arm: "decide approve calls SchedulingPort.transfer first and then records one Decision (approved) and mirrors the state; refuse records the Decision with the reason; both notify both members less an inactive one (SwapApproved / SwapRefused); a reason with approve, or a system code, is invalid_reason; the response is the request with the decision embedded", file: tests/swaps/test_decide.py, kind: deterministic }
  - { arm: "decide refuses party_to_swap for the requester or the counterpart whatever their role, forbidden for a member, wrong_state, past_deadline, reason_required, invalid_reason; an admin who is not a party decides a request a planner is party to", file: tests/swaps/test_decide.py, kind: deterministic }
  - { arm: "when transfer raises TransferRefused the operation succeeds: the Decision is recorded refused with that reason, the decider is the attempting member, the state mirrors refused, both members are notified with the reason", file: tests/swaps/test_decide.py, kind: deterministic }
  - { arm: "mine lists every request the member is party to, every state, newest first by created_at then id desc, with answer_reason and decision embedded, display_state (expired derived from the clock, nothing stored, nobody notified) and awaiting (counterpart | decider | none); an inactive other party still listed", file: tests/swaps/test_service.py, kind: deterministic }
  - { arm: "pending lists open accepted requests oldest first by answered_at then id asc (an accepted request past its deadline is absent), the same for any admin or planner, with party marked; forbidden for members", file: tests/swaps/test_service.py, kind: deterministic }
  - { arm: "SwapsPort.view takes the caller, the week state and each assignment with its holder and start instant, and returns per assignment pending (the open request state or none) and requestable (own row, published, no open request, now < deadline) without reading scheduling", file: tests/swaps/test_service.py, kind: deterministic }
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
  - { unit: ADU-02, file: src/app/api/contract_stubs.py, assertion: "the five swaps operations move out of the stubs module; golden unchanged", q: none }
  - { unit: ADU-02, file: src/app/main.py, assertion: "the composition root binds the real SwapsService", q: none }
mocks: []
size: M
acceptance:
  - { arm: "POST /swaps answers 201 and each contract refusal (403 not_holder; 409 past_deadline, request_open, week_draft, counterpart_*; 422 reason_required, invalid_reason)", file: tests/api/test_swaps.py, kind: deterministic }
  - { arm: "POST answer answers 200 accepted/declined, 403 not_counterpart, 409 wrong_state/past_deadline, 422", file: tests/api/test_swaps.py, kind: deterministic }
  - { arm: "POST decision answers 200 approved/refused/transfer_refused, 403 forbidden/party_to_swap, 409, 422", file: tests/api/test_swaps.py, kind: deterministic }
  - { arm: "GET mine and GET pending answer the contract's shapes and order; pending 403 for a member", file: tests/api/test_swaps.py, kind: deterministic }
  - { arm: "the served contract still equals the golden after the move", file: tests/api/test_swaps.py, kind: deterministic }
  - { arm: "every response body validates against the contract schema for its code", file: tests/api/test_swaps.py, kind: deterministic }
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
consumes: [data.model, Clock, MemberDirectory]
depends: [ADU-01, ADU-02, ADU-03]
files: ["src/app/notifications/service.py","src/app/notifications/repo.py"]
tests: ["tests/notifications/test_service.py"]
amends: []
mocks: []
size: S
acceptance:
  - { arm: "retires MK-02: Notifier is bound to the notifications service; src/app/notifications/null_notifier.py is deleted; the identity tests stay green unchanged", file: tests/notifications/test_service.py, kind: deterministic }
  - { arm: "notify writes one Notification per recipient of the event with its event code, text composed from the payload alone, created_at from the clock and read false, in the caller's transaction; duplicate recipients are written once; an inactive recipient is skipped except for MemberDeactivated", file: tests/notifications/test_service.py, kind: deterministic }
  - { arm: "list returns only the caller's notifications newest first by created_at then id desc; mark_read sets read and refuses not_recipient for someone else's and not_found for an unknown id", file: tests/notifications/test_service.py, kind: deterministic }
  - { arm: "the text for each of the nine events carries the payload fields the stories name (date and start, names, role, reason) and names the state as it is — one assertion per event", file: tests/notifications/test_service.py, kind: deterministic }
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
  - { unit: ADU-02, file: src/app/api/contract_stubs.py, assertion: "the two notifications operations move out of the stubs module, which is now empty and deleted; golden unchanged", q: none }
  - { unit: ADU-02, file: src/app/main.py, assertion: "the composition root binds the real NotificationsService and no Null remains", q: none }
mocks: []
size: S
acceptance:
  - { arm: "GET /notifications answers the caller's list newest first (and [] for none); POST read answers 200, 403 not_recipient, 404", file: tests/api/test_notifications.py, kind: deterministic }
  - { arm: "the stubs module is gone and every operation of the contract is served by a domain router; the golden still equals", file: tests/api/test_notifications.py, kind: deterministic }
  - { arm: "every response body validates against the contract schema for its code", file: tests/api/test_notifications.py, kind: deterministic }
  - { arm: "adu release check reports zero active mocks (every Null deleted)", file: tests/api/test_notifications.py, kind: deterministic }
owed: []
```

### ADU-11 — Operator command: seed the first admin
```yaml adu
id: ADU-11
title: Operator command — seed the first admin
layer: 4
domain: identity
stories: [US-identity-005]
provides: [cli.seed_admin]
consumes: [IdentityService]
depends: [ADU-03]
files: ["src/app/api/cli.py"]
tests: ["tests/test_cli.py"]
amends: []
mocks: []
size: S
acceptance:
  - { arm: "app seed-admin --name --email --passcode on an empty workspace creates the admin and prints its id (exit 0)", file: tests/test_cli.py, kind: deterministic }
  - { arm: "on a non-empty team it exits 2 and prints team_not_empty", file: tests/test_cli.py, kind: deterministic }
  - { arm: "the seeded admin signs in through IdentityService with the given credentials", file: tests/test_cli.py, kind: deterministic }
  - { arm: "the command takes the workspace path as a pathlib argument and never touches the network", file: tests/test_cli.py, kind: deterministic }
owed: []
```

### ADU-12 — UI foundation: shell, generated client, sign-in
```yaml adu
id: ADU-12
title: UI foundation — shell, generated client, sign-in
layer: 5
domain: identity
stories: [US-identity-004]
provides: [ui.shell, ui.sign_in]
consumes: [identity.sign_in]
depends: [ADU-04]
files: ["frontend/package.json","frontend/vite.config.ts","frontend/src/client/index.ts","frontend/src/App.tsx","frontend/src/pages/SignIn.tsx","frontend/src/routes.ts"]
tests: ["frontend/tests/sign-in.test.tsx","frontend/tests/tour-coverage.test.tsx"]
amends: []
mocks: []
size: M
acceptance:
  - { arm: "the client is generated from contracts/openapi.yaml (openapi-typescript) and is the only module that calls fetch (dependency-cruiser rule)", file: frontend/tests/tour-coverage.test.tsx, kind: deterministic }
  - { arm: "every data-tour-id anchor the design names for the Sign in screen exists; the coverage lint fails on a removed anchor", file: frontend/tests/tour-coverage.test.tsx, kind: deterministic }
  - { arm: "the sign-in form submits email and passcode through the client, stores the token, and lands on the week board; invalid_credentials and member_inactive are shown with their reason text", file: frontend/tests/sign-in.test.tsx, kind: deterministic }
  - { arm: "the shell renders the navigation for the five screens and sends the bearer token on every call", file: frontend/tests/sign-in.test.tsx, kind: deterministic }
  - { arm: "the dev server points the client at the Prism mock (VITE_API_BASE) and the tests use handlers built from the contract's examples; nothing reaches a non-loopback address", file: frontend/tests/sign-in.test.tsx, kind: deterministic }
  - { arm: "npm run build succeeds and npm run lint is clean", file: frontend/tests/sign-in.test.tsx, kind: deterministic }
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
consumes: [ui.shell, identity.list_members, identity.add_member, identity.change_role, identity.deactivate, scheduling.create_shift, scheduling.assign, scheduling.unassign, scheduling.publish, scheduling.board]
depends: [ADU-04, ADU-06, ADU-12]
files: ["frontend/src/pages/Team.tsx","frontend/src/pages/WeekBoard.tsx","frontend/src/hooks/useTeam.ts","frontend/src/hooks/useBoard.ts"]
tests: ["frontend/tests/team.test.tsx","frontend/tests/board.test.tsx"]
amends: []
mocks: []
size: M
acceptance:
  - { arm: "the Team screen lists members with role and active state; the add form creates one and shows it; role change and deactivate show their refusals (duplicate_email, last_admin, future_assignments) as text with the reason", file: frontend/tests/team.test.tsx, kind: deterministic }
  - { arm: "the Team screen's anchors (team-list, member-add, member-role, member-deactivate) exist; admin-only controls are hidden from planners and members", file: frontend/tests/team.test.tsx, kind: deterministic }
  - { arm: "the week board opens on the current week from the API (board-none for none, board-draft for a draft), renders shifts in order with holder-rows, the holder-pending-badge with pending's text and nothing for null, holder-request-swap exactly on requestable rows, the week-picker from the weeks list (selecting one shows its board), and the planner's create/assign/unassign/publish controls", file: frontend/tests/board.test.tsx, kind: deterministic }
  - { arm: "the mine filter shows only the caller's shifts; the empty state board-empty-mine shows 'No shifts this week'", file: frontend/tests/board.test.tsx, kind: deterministic }
  - { arm: "the publish refusal lists the unfilled shifts from the PublishProblem; week_draft for a member shows the reason", file: frontend/tests/board.test.tsx, kind: deterministic }
  - { arm: "every data-tour-id anchor of the Team and Week board screens exists (the coverage lint extends to both)", file: frontend/tests/board.test.tsx, kind: deterministic }
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
consumes: [ui.shell, swaps.request, swaps.answer, swaps.decide, swaps.mine, swaps.pending, notifications.list, notifications.mark_read]
depends: [ADU-08, ADU-10, ADU-12]
files: ["frontend/src/pages/SwapRequest.tsx","frontend/src/pages/SwapInbox.tsx","frontend/src/pages/Notifications.tsx","frontend/src/hooks/useSwaps.ts","frontend/src/hooks/useNotifications.ts"]
tests: ["frontend/tests/swaps.test.tsx","frontend/tests/notifications.test.tsx"]
amends: []
mocks: []
size: M
acceptance:
  - { arm: "the request form offers the eligible counterparts by name (composed from the members list and the board), submits assignment, counterpart and reason through the client, and the inbox shows the new request with swap-state requested; every refusal is shown with its reason code", file: frontend/tests/swaps.test.tsx, kind: deterministic }
  - { arm: "the inbox shows swap-state, swap-awaiting and swap-decision per request, expired as expired, accept/decline only to the counterpart while open in requested, approve/refuse only to a non-party admin or planner while open in accepted, and the outcome with the reason after a decision", file: frontend/tests/swaps.test.tsx, kind: deterministic }
  - { arm: "the pending list shows accepted requests oldest first with the party mark and no decide controls on marked rows", file: frontend/tests/swaps.test.tsx, kind: deterministic }
  - { arm: "the Notifications screen lists notification-item rows newest first under notification-list, marks one read, and shows notification-empty with 'Nothing yet'", file: frontend/tests/notifications.test.tsx, kind: deterministic }
  - { arm: "every data-tour-id anchor of the three screens exists (coverage lint)", file: frontend/tests/notifications.test.tsx, kind: deterministic }
  - { arm: "no component imports the client directly; only hooks do (dependency-cruiser)", file: frontend/tests/swaps.test.tsx, kind: deterministic }
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
consumes: [cli.seed_admin, ui.swaps, ui.board, identity.add_member, scheduling.publish, swaps.decide, notifications.list]
depends: [ADU-04, ADU-06, ADU-08, ADU-10, ADU-11, ADU-13, ADU-14]
files: ["src/app/serve.py","frontend/playwright.config.ts","docs/RUNBOOK.md"]
tests: ["tests/test_e2e_api.py","frontend/tests/e2e/vertical-path.spec.ts"]
amends:
  - { unit: ADU-11, file: src/app/api/cli.py, assertion: "cli gains the serve subcommand (uvicorn on 127.0.0.1 only); seed-admin unchanged", q: none }
mocks: []
size: M
acceptance:
  - { arm: "the brief's §6 path through the API with the real app and a FixedClock: seed admin, add members, create and publish a week, request, accept, approve; every party's notifications are exactly those of R-notifications-01 and the board shows the new holder", file: tests/test_e2e_api.py, kind: deterministic }
  - { arm: "the same path with a refused transfer (counterpart_overlap): the decision is refused with that reason and both members are told", file: tests/test_e2e_api.py, kind: deterministic }
  - { arm: "the same path in the browser (Playwright against app serve on loopback and the built frontend): sign in as three members, the board and the inbox show every step", file: frontend/tests/e2e/vertical-path.spec.ts, kind: deterministic }
  - { arm: "app serve binds 127.0.0.1 only and serves the built frontend and the API from one port; docs/RUNBOOK.md's commands are executed by the test", file: tests/test_e2e_api.py, kind: deterministic }
  - { arm: "the gate finishes under the budget in adu.toml on the operator's machine (reported, never gating)", file: tests/test_e2e_api.py, kind: quantitative, statistic: wall_clock_s, threshold: 300, n: 1, seed: 0, tolerance: "60 s", tier: timing, measured_by: "time uv run pytest tests/ -q -m \"not timing\"" }
  - { arm: "adu release check is green: every mock retired, pins match, the plan derived blocks current", file: tests/test_e2e_api.py, kind: deterministic }
owed: []
```
