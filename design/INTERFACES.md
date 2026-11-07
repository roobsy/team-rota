# INTERFACES — Team Rota
v1.0.1 (design v1.7, D-02) · owned by the architect (`/adu-lifecycle:design-contract`). Every in-process interface one domain offers another, defined before either side exists; HTTP operations live in `contracts/openapi.yaml` and are listed here only in the traceability table. All protocols live in one module of layer 2 (`src/app/ports.py`), each with a `Null<Interface>` in the contract unit at the provider's future path; the composition root (`src/app/main.py`) binds the real class when its unit lands — class replaced, shape kept.

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

## Build order (the cycles, accepted explicitly — DESIGN-REVIEW-2 A18/D17)
identity ↔ scheduling (IR-05 / IR-06) and scheduling ↔ swaps (IR-01, IR-02 / IR-07) are cycles at the service level. They are broken by the ports above: the contract unit (ADU-02) ships every protocol with a Null implementation; the plan's derived order builds identity (Null scheduling for IR-05, Null notifier), notifications, scheduling (Null swaps for IR-07), then swaps; each provider's acceptance retires the Null it replaces, and `adu release check` fails on a Null that outlives its provider.

## CLI entry points (not operations)
| Command | Story | Rule |
|---|---|---|
| `app seed-admin --name --email --passcode` | US-identity-005 | R-identity-07: refused with team_not_empty once any member exists |

## Traceability — story action → operation or protocol
<!-- a row with no operation stays empty: a finding for the design, never an invented operation -->
| Story | Action | Operation (operationId) or protocol |
|---|---|---|
| US-identity-005 | seed the first admin | CLI `app seed-admin` |
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
