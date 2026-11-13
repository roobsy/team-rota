# INTERFACES — Team Rota
v1.1 (design v1.7, D-02; Q-07: D-12–D-17) · owned by the architect (`/adu-lifecycle:design-contract`). Every in-process interface one domain offers another, defined before either side exists; HTTP operations live in `contracts/openapi.yaml` and are listed here only in the traceability table. All protocols live in one module of layer 2 (`src/app/ports.py`), each with a `Null<Interface>` in the contract unit at the provider's future path; the composition root (`src/app/main.py`) binds the real class when its unit lands — class replaced, shape kept.

## Protocols
### Clock
Provider: ADU-02 (the contract unit; `SystemClock` is trivial and ships with the port). Consumers: every service; tests pass a `FixedClock`. Null implementation: none (FixedClock in tests/support/doubles.py is the test double, SystemClock the product's).
```
class Clock(Protocol):
    def now(self) -> datetime            # naive local time of the team
```
Invariants: no service calls datetime.now(); the deadline, expiry, created_at, accepted_at, decided_at and "future week" all read this clock.

### MemberDirectory (identity → scheduling, swaps, notifications)
Provider: ADU-03 (identity service). Consumers: scheduling (IR-06, IR-12: active_member_ids for WeekPublished), swaps (IR-09), notifications (IR-04), the API layer (IR-11). Null implementation: `src/app/identity/null_directory.py` (created by ADU-16, deleted by ADU-03).
```
@dataclass(frozen=True)
class Caller:
    member_id: int; name: str; role: Role; active: bool

class MemberDirectory(Protocol):
    def caller_for_token(self, token: str) -> Caller | None       # IR-11: None for unknown; an inactive member's token resolves to None too
    def is_active(self, member_id: int) -> bool | None            # None for an id that names no member: the consumer answers not_found (IR-06, IR-09)
    def role_of(self, member_id: int) -> Role                     # raises MemberNotFound
    def name_of(self, member_id: int) -> str
    def active_member_ids(self) -> list[int]
    def decider_ids(self) -> list[int]                            # active admins and planners
```
Invariants: an unknown id raises `MemberNotFound`; the API layer calls `caller_for_token` once per request (`deps.py`) and passes the `Caller` into every service call. The Null resolves any token of the form `tok_<id>` to an active member of role member named "Member <id>" (`tok_admin` → an admin), returns active=True, role=member, name="Member <id>", and empty lists.

### SchedulingPort (scheduling → swaps, identity)
Provider: ADU-05 (scheduling service). Consumers: swaps (IR-01, IR-02), identity (IR-05). Null implementation: `src/app/scheduling/null_port.py`.
```
@dataclass(frozen=True)
class AssignmentInfo:
    assignment_id: int; holder_id: int; shift_id: int; shift_date: date; start: time; end: time; start_at: datetime
    week_start: date; week_state: str; holder_ids: tuple[int, ...]       # IR-01

class SchedulingPort(Protocol):
    def assignment(self, assignment_id: int) -> AssignmentInfo               # raises AssignmentNotFound
    def holds_intersecting_shift(self, member_id: int, shift_id: int) -> bool   # IR-01: a slot on a shift of the same date whose [start, end) intersects (counterpart_overlap at request time)
    def transfer(self, assignment_id: int, to_member_id: int) -> None       # IR-02; raises TransferRefused(reason), reason in {counterpart_overlap, counterpart_inactive}
    def has_assignment_after(self, member_id: int, now: datetime) -> bool   # IR-05: any week, draft or published, shift start instant after now
```
Invariants: `transfer` runs inside the caller's transaction and commits nothing itself (one session per request, opened by the API layer; swaps and scheduling write in it; the Notifier writes in it); a slot on the same shift counts as an overlap; `TransferRefused.reason` is one of the two enumerated codes and nothing else.

### SwapsPort (swaps → scheduling)
Provider: ADU-07 (swaps service). Consumers: scheduling, for the badge (IR-07). Null implementation: `src/app/swaps/null_port.py`.
```
@dataclass(frozen=True)
class AssignmentView:
    pending: str | None        # "requested" | "accepted" | None — the open request's state
    requestable: bool          # the caller may request a swap on it now: own row, published week, no open request, now < deadline

class SwapsPort(Protocol):
    def view(self, caller_id: int, week_published: bool, assignments: Iterable[tuple[int, int, datetime]]) -> dict[int, AssignmentView]   # IR-07: (assignment_id, holder_id, start_at) → per assignment
```
Invariants: scheduling passes each assignment's id, holder and start instant; swaps applies R-swaps-01/02/06 to those (no re-entrant read of scheduling); the Null returns pending=None, requestable=False for every id.

### Notifier (notifications → identity, scheduling, swaps)
Provider: ADU-09 (notifications service). Consumers: identity (IR-10), scheduling (IR-08), swaps (IR-03). Null implementation: `src/app/notifications/null_notifier.py`.
```
# one frozen dataclass per event, each self-contained (R-notifications-01); recipients are member ids named by the emitter
class WeekPublished:    start_date: date; recipient_ids: tuple[int, ...]
class SwapRequested:    request_id: int; shift_date: date; shift_start: time; requester_name: str; reason: str; recipient_id: int
class SwapAccepted:     request_id: int; shift_date: date; shift_start: time; counterpart_name: str; recipient_ids: tuple[int, ...]
class SwapDeclined:     request_id: int; shift_date: date; shift_start: time; counterpart_name: str; reason: str; recipient_id: int
class SwapApproved:     request_id: int; shift_date: date; shift_start: time; new_holder_name: str; recipient_ids: tuple[int, ...]
class SwapRefused:      request_id: int; shift_date: date; shift_start: time; reason: str; recipient_ids: tuple[int, ...]
class MemberAdded:      member_id: int; role: str
class RoleChanged:      member_id: int; role: str
class MemberDeactivated: member_id: int
Event = WeekPublished | SwapRequested | SwapAccepted | SwapDeclined | SwapApproved | SwapRefused | MemberAdded | RoleChanged | MemberDeactivated

class Notifier(Protocol):
    def notify(self, event: Event) -> None
```
Invariants: one notification per recipient per event, written in the caller's transaction; the Notifier composes the text from the payload alone and never reads another domain; recipients are deduplicated; inactive recipients are skipped except for MemberDeactivated (IR-04). The Null records every event in a list (`sent`) a spy can assert and writes nothing.

## Refused (every domain → the API layer and the operator's command; an exception, not a protocol)
Provider: ADU-03, in `src/app/ports.py` beside `MemberNotFound`, `AssignmentNotFound` and `TransferRefused` (D-13; ADU-03 amends ADU-16's module). Consumers: every service raises it; the API units map it to a Problem; the seed command (ADU-11) maps `team_not_empty` to exit status 2.
```
class Refused(Exception):
    def __init__(self, reason: str, detail: str = "", **extra: object) -> None   # .reason, .detail, .extra
```
Invariants: `reason` is a code of PRODUCT-DESIGN's Reason codes table (the values of the contract's `Problem.reason` and `PublishProblem.reason`, and `team_not_empty`); `detail` is the refusal's plain sentence and `extra` the fields a story names (`unfilled` for publish), because a refusal is {reason, detail, and the extra fields a story names} (PRODUCT-DESIGN, cross-cutting rules); `Refused` carries no HTTP status — the API layer maps the reason to its bucket's status per operation (D-07); a refusal changes nothing (services check before they write); tests assert `.reason`, never `.detail` (the contract's `Problem.reason`: "x-when-to-use: assert the code, never the detail text", contracts/openapi.yaml:646); `TransferRefused` stays the transfer's own signal (IR-02) and is never re-raised as `Refused` (an approval whose transfer was refused succeeds).

## Domain services (called by the API layer and the operator's command; not ports)
A service is called only from the layers above it — the API, the composition root, the CLI; another domain reaches it only through the ports above (D-05). Every operation a signed-in member performs takes the `Caller` that `deps.py` resolved (R-identity-06, IR-11); every refusal is `Refused(<reason>)`. A point the arms, the domain spec and the contract do not settle is marked open with its question, never filled in.

**The request's session (D-14).** Every service, and every port implementation `src/app/main.py` binds, reads and writes in the current session, `db.current_session()`, and never opens, commits or closes one. With no session current, `db.current_session()` raises `db.NoCurrentSession`; a service method lets it propagate and never opens a session quietly. Exactly three owners make a session current:
- **A request.** `deps.get_session` is an async generator dependency. It opens the request's one session on `engine_of(request)`, makes it current with `db.use_session(session)` for the whole request, and yields it. On the way out it restores the previous current session and closes this one, which rolls back whatever was not committed. It is async because a ContextVar set in a sync dependency is not visible to the endpoint. `require_caller` depends on it, so `caller_for_token` reads the request's session. The API layer commits a write after the service returns and before it answers, never in the dependency's exit: FastAPI runs that exit after the response is sent, so a failure there would leave a 200 standing. Both behaviours are measured in docs/PACK-q07-retire-amends.md, Part E-6.
- **The operator's command.** `app seed-admin` (ADU-11) builds the app with `create_app(workspace)` and calls `seed_admin` on the identity service that app binds as `Ports.member_directory` (ADU-03 arm 1), inside `with db.unit_of_work(db.engine_for(app.state.workspace)):`. Whether the command reaches it there or through another binding is Q-12's first point, ruled before ADU-04 opens and so before ADU-11. The block commits when `seed_admin` returns, and the command then prints the id (exit 0). `Refused("team_not_empty")` rolls the block back, and the command prints the reason and exits 2.
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
class IdentityService:                          # implements MemberDirectory (above), and the operations below — every method in db.current_session() (D-14):
    def __init__(
        self,
        bound: Callable[[], Bindings],          # the composition root's bindings, read at call time (D-15): .clock (Clock),
                                                #   .scheduling (SchedulingPort, IR-05), .notifier (Notifier, IR-10); Bindings is a Protocol of those
                                                #   three in src/app/identity/service.py, which main.Ports satisfies, so identity never imports main;
                                                #   main.py binds IdentityService(lambda: app.state.ports, …); a test passes
                                                #   lambda: SimpleNamespace(clock=FixedClock(…), scheduling=FakeSchedulingPort(), notifier=SpyNotifier())
        source: TokenSource,                    # the token and the salt (D-16): TokenSource is a Protocol in src/app/identity/service.py,
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
# MemberSummary: id, name, role, active (ADU-03 arm 7). All three are frozen dataclasses (`@dataclass(frozen=True)`) defined in src/app/identity/service.py beside the service; no other domain consumes them in process (D-05), and the API layer maps them onto the contract's Member, Token and MemberSummary (D-17).
```
| Operation | Rule (source) | Emits | Refused with, by bucket (R-identity-08: forbidden → not_found → state → validation) |
|---|---|---|---|
| seed_admin | an empty team gets one active admin; the passcode stored as a salted SHA-256; answers the new id; no caller — an operator command outside the API (R-identity-07; ADU-03 arm 2) | nothing | state: team_not_empty |
| add_member | an active member with the role; the email unique, compared case-insensitively; a role that is missing or not admin, planner or member is invalid_role (R-identity-01, -02; the contract's MemberCreate.role is optional and "checked by identity") | MemberAdded(member_id, role) | forbidden (the caller is not an admin) · state: duplicate_email · validation: invalid_role |
| change_role | the same role is a no-op that answers the unchanged member and emits nothing; an inactive member's role may change and nobody is notified; the team keeps an active admin (R-identity-01, -03) | RoleChanged(member_id, role), except for the no-op and an inactive member | forbidden · not_found · state: last_admin · validation: invalid_role |
| deactivate | active false, the row kept; refused while `scheduling.has_assignment_after(member_id, clock.now())` (R-identity-03, -04, -05) | MemberDeactivated(member_id) | forbidden · not_found · state: future_assignments, last_admin, member_inactive (a repeat; nothing emitted) — their order within the bucket is US-identity-003's (PRODUCT-DESIGN, cross-cutting rules) |
| sign_in | the email matched case-insensitively and the passcode verified before the active check; a missing passcode counts as wrong; the new token replaces the member's earlier one; no caller (R-identity-06; the contract's 401 for identity.sign_in) | nothing | unauthenticated bucket: invalid_credentials (wrong or missing passcode, unknown email) · forbidden bucket: member_inactive (only after a correct passcode) |
| list_members | every member, active and inactive, as MemberSummary — never email, passcode or token — by name compared case-insensitively, then id (R-identity-09) | nothing | none: any signed-in caller |
| MemberDirectory | the six methods above over identity's own rows, read in the current session (with none current, each raises db.NoCurrentSession; D-14): caller_for_token is None for an unknown token and for an inactive member's (IR-11); is_active is None for an unknown id; role_of and name_of raise MemberNotFound; active_member_ids (IR-12); decider_ids the active admins and planners | — | none: no caller |

## Test doubles (ADU-16, permanent — never deleted)
`tests/support/doubles.py`: `SpyNotifier` (records every event), `FakeSchedulingPort` (settable AssignmentInfo, has_assignment_after, holds_intersecting_shift and transfer outcome), `FakeSwapsPort` (settable view), `FakeMemberDirectory` (settable members, callers, deciders). Consumer units test against these, never against a Null; a double that round-trips its input is labelled vacuous and is no oracle (rule 13).

## Composition root bindings (ADU-16 creates the Nulls, ADU-02 binds them; each provider unit replaces its own line by amendment)
| Port | Null (contract unit) | Real (provider unit) |
|---|---|---|
| Clock | SystemClock / FixedClock in tests | — |
| MemberDirectory | identity/null_directory.py | ADU-03 |
| SchedulingPort | scheduling/null_port.py | ADU-05 |
| SwapsPort | swaps/null_port.py | ADU-07 |
| Notifier | notifications/null_notifier.py | ADU-09 |

**Retiring a Null (D-12).** The provider unit rebinds its line in `src/app/main.py`, deletes the Null, and edits every completed test that names the Null by class: the import goes; a class check becomes a protocol check (`isinstance(x, ports.<Interface>)`); a test that needs a resolved caller injects `FakeMemberDirectory` through `create_app(member_directory=…)`, holding the member and token it needs. Each such test is a declared `amends` line of the provider and a hard-rule-1 edit: the session asks the operator for the grant (`adu grant add <session> <file> "<reason>"`) before its first edit, because the edit guard does not honour `amends` on a completed unit's test (plugin FB-28), and records the grant in its journal block. In this plan: ADU-03 (NullDirectory), ADU-09 (NullNotifier), ADU-05 (NullSchedulingPort) and ADU-07 (NullSwapsPort; `tests/test_nulls.py` removed with it), each editing `tests/api/test_contract_conformance.py` and `tests/test_nulls.py`.

## Build order (the cycles, accepted explicitly — DESIGN-REVIEW-2 A18/D17)
identity ↔ scheduling (IR-05 / IR-06), identity ↔ notifications (IR-10 / IR-04) and scheduling ↔ swaps (IR-01, IR-02 / IR-07) are cycles at the service level. They are broken by the ports above: the contract unit (ADU-02) ships every protocol with a Null implementation; the plan's derived order builds identity (Null scheduling for IR-05, Null notifier), notifications, scheduling (Null swaps for IR-07), then swaps; each provider's acceptance retires the Null it replaces, and `adu release check` fails on a Null that outlives its provider.

## CLI entry points (not operations)
| Command | Story | Rule |
|---|---|---|
| `app seed-admin --name --email --passcode` | US-identity-005 | R-identity-07: refused with team_not_empty once any member exists |

## Traceability — story action → operation or protocol
<!-- a row with no operation stays empty: a finding for the design, never an invented operation -->
| Story | Action | Operation (operationId) or protocol |
|---|---|---|
| US-identity-005 | seed the first admin | CLI `app seed-admin` (IdentityService.seed_admin) |
| US-identity-001 | add a member; list the members | identity.add_member; identity.list_members |
| US-identity-002 | change a role | identity.change_role |
| US-identity-003 | deactivate | identity.deactivate (reads SchedulingPort.has_assignment_after) |
| US-identity-004 | sign in; carry the token; land on the current week | identity.sign_in; bearer security on every other operation (MemberDirectory.caller_for_token in deps.py); scheduling.list_weeks |
| US-notifications-006 | account-change notifications | Notifier.notify from identity (MemberAdded, RoleChanged, MemberDeactivated) |
| US-scheduling-001 | create a shift (and its week) | scheduling.create_shift |
| US-scheduling-002 | assign; unassign | scheduling.assign; scheduling.unassign |
| US-scheduling-003 | publish | scheduling.publish |
| US-notifications-001 | week published | Notifier.notify from scheduling (WeekPublished) |
| US-scheduling-004 | the board; the badge per holder-row; the request control on own rows; the weeks and the current week | scheduling.board (reads SwapsPort.view with the caller, the week state and each assignment's holder and start instant); scheduling.list_weeks |
| US-scheduling-005 | filter mine | scheduling.board?mine=true |
| US-swaps-001 | request a swap; the eligible counterparts | swaps.request (reads SchedulingPort.assignment — holder_ids answer counterpart_on_shift; MemberDirectory.is_active); the form composes candidates from identity.list_members and the board |
| US-notifications-002 | counterpart told | Notifier.notify from swaps (SwapRequested) |
| US-swaps-002 | accept or decline | swaps.answer |
| US-notifications-003 | answer told | Notifier.notify from swaps (SwapAccepted with MemberDirectory.decider_ids; SwapDeclined) |
| US-swaps-003 | approve or refuse | swaps.decide (calls SchedulingPort.transfer first) |
| US-scheduling-006 | the transfer | SchedulingPort.transfer (no operation, by R-scheduling-08) |
| US-notifications-004 | outcome told | Notifier.notify from swaps (SwapApproved, SwapRefused) |
| US-swaps-004 | my requests (with shift and names) | swaps.mine (reads SchedulingPort.assignment, MemberDirectory.name_of) |
| US-swaps-005 | pending decisions (with shift and names) | swaps.pending (reads SchedulingPort.assignment, MemberDirectory.name_of) |
| US-notifications-005 | read notifications; mark read | notifications.list; notifications.mark_read |
