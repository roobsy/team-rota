# PRODUCT-DESIGN — Team Rota
v1.4 · owned by the pm-lead (`/adu-lifecycle:design-product`); checked by `adu design check`; reviewed by the architect and the developer (`/adu-lifecycle:review-design`) before stories are written. Everything here serves the North Star in `design/PRODUCT-BRIEF.md`: the roster tells each person the truth about their week, plainly, even when unwelcome. v1.1 applied `design/DESIGN-REVIEW-1.md` (56 findings); v1.2 `design/DESIGN-REVIEW-2.md` (52); v1.3 `design/DESIGN-REVIEW-3.md` (22, two blocking); v1.4 `design/DESIGN-REVIEW-4.md` (28, four blocking): the caller resolved once, refusal shape and precedence, not_found, the typed Notifier events, "open" defined once, the answer fields, list members and list weeks, the badge per holder, tiebreaks, ids on every entity.

## Personas
| Persona | Role | Goal | Pain today |
|---|---|---|---|
| Pat | planner | publish a fair, complete week early and settle swaps without chasing | the spreadsheet is one message behind the chat |
| Mo | member | see the week early and hand over a shift without a phone tree | a swap agreed in chat is forgotten by the roster |
| Avi | admin | keep members and roles right; nobody decides their own swap | no record of who agreed to what |

## Cross-cutting rules (apply to every journey)
- **The caller.** Every operation except sign-in and the operator's seed command carries a bearer token issued by identity at sign-in. The API layer resolves the token once per request into the caller {member_id, name, role, active} (IR-11) and passes that value into every domain operation; the domain enforces forbidden, own and party on it. A missing or unknown token, or a token of an inactive member, is refused with reason `unauthenticated`. A new sign-in replaces the member's token.
- **The forbidden rule.** An action by a role the Permissions table denies is refused with reason `forbidden`; an action on something that is not the caller's own, where the table says `own`, is refused with the reason the story names.
- **Refusals.** A refusal is {reason, detail, and the extra fields a story names}; it changes nothing. An identifier that names nothing is refused with reason `not_found` (except sign-in, where an unknown email is `invalid_credentials`, and credentials are verified before the active check so that `member_inactive` is only ever answered to a correct passcode). When several checks fail, the first in this order names the reason: unauthenticated → forbidden → not_found → own/party → state → deadline → validation. Within the state bucket, a refusal about the target's own state (the week is published; the request is not in the right state) precedes refusals about the input or the counterpart, whichever story names it; after that, within a bucket, checks run in the order the story's arms list them. A body that fails shape or enum validation is refused with reason `invalid_request`. The HTTP status follows the bucket: unauthenticated 401 · forbidden and own/party 403 · not_found 404 · state and deadline 409 · validation 422 (the Reason codes table below lists every code with its bucket). An operation that changed state never answers with a refusal: approval whose transfer was refused succeeds and returns the recorded decision.
- **The clock.** Every action reads `now` from an injected clock; tests set it. Times are naive local times of the team (one team, one timezone, a fixed deployment setting). A shift's start instant is its date plus its start time. A deadline is half-open: an action is allowed while now < deadline and refused at or after it.
- **Lists and ties.** Every list names its sort key and breaks ties by id: ascending for oldest-first lists, descending for newest-first; the board sorts by date, start, then shift id.
- **Ids.** Every entity's id is an integer assigned by the store in creation order; Week is keyed by its start_date.
- **Nothing pending looks done.** States are shown as they are; a derived display state (`expired`) is computed on read and never stored. A request is **open** when its stored state is requested or accepted and now < its deadline; only open requests carry a badge, show answer or decide controls, or count as pending.

## Reason codes (every refusal a story names, its bucket and its status)
| Bucket | Status | Codes |
|---|---|---|
| unauthenticated | 401 | unauthenticated; invalid_credentials (sign-in) |
| forbidden / own / party | 403 | forbidden; member_inactive (sign-in); not_holder; not_counterpart; party_to_swap; not_recipient; week_draft (board of a draft week, members) |
| not_found | 404 | not_found |
| state | 409 | team_not_empty; duplicate_email; last_admin; future_assignments; week_published; already_assigned; overlapping_shift; shift_full; member_inactive (assign); unfilled_slots; request_open; week_draft (request on a draft week); counterpart_inactive; counterpart_on_shift; counterpart_self; wrong_state |
| deadline | 409 | past_deadline |
| validation | 422 | invalid_request (a body that fails shape or enum validation); invalid_role; not_week_start; outside_week; invalid_interval; invalid_slots; reason_required; invalid_reason |
| internal, never an HTTP refusal | — | counterpart_overlap; counterpart_inactive (the transfer's refusals, surfaced only as Decision.reason and in the swap_refused payload) |

## Journeys
### J-01 — Admin sets up the team
Persona: Avi. Outcome: the team exists with one admin, every member has one role, a passcode and can sign in, and is told of changes to their account.
1. [identity] the operator seeds the first admin with a command outside the API, once, on an empty team
2. [identity] Avi adds a member with a name, an email, a role and a passcode, and sees the team list
3. [identity] Avi changes a member's role
4. [identity] Avi deactivates a member, who keeps their row and history but can no longer be assigned, sign in or act on a token
5. [identity] a member signs in with email and passcode and receives the token every later operation carries, with who they are
6. [notifications] the member is told when they are added, when their role changes and when they are deactivated

### J-02 — Planner publishes a week
Persona: Pat. Outcome: the week is visible to every member, who were all told.
1. [scheduling] Pat creates the shifts of a week (date, start, end, slots); the week is named by its Monday and comes into being with its first shift
2. [scheduling] Pat assigns active members to shifts, no member twice in one shift and no overlapping shifts for one member, and removes a mistaken assignment while the week is a draft
3. [scheduling] Pat publishes the week; a published week changes only through an approved swap
4. [notifications] every active member of any role is notified that the week is published

### J-03 — Member views the week
Persona: Mo. Outcome: Mo knows who holds every shift and what is pending.
1. [scheduling] Mo opens the week board — the current week by default, any listed week from the picker — and sees every shift with its holder-rows, the open request on each, and a request control on their own rows where a request is allowed now
2. [scheduling] Mo filters the board to their own shifts

### J-04 — Member hands over a shift
Persona: Mo. Outcome: a counterpart holds Mo's shift, a planner or admin who is not a party approved it, everyone concerned was told.
1. [swaps] Mo requests a swap of one of their assignments on a published week, naming an eligible counterpart and a reason code, before the shift's deadline
2. [notifications] the counterpart is notified of the request
3. [swaps] the counterpart accepts or declines the request, with a reason when declining
4. [notifications] on accept the requester and every eligible decider are notified; on decline the requester, with the reason
5. [swaps] a planner or admin who is not a party approves or refuses the accepted request with a reason code; approval transfers the assignment first and records the decision second, in one transaction
6. [scheduling] on transfer the assignment moves to the counterpart and the board shows it
7. [notifications] both members are notified of the outcome, with the reason when refused

### J-05 — Anyone reads what is pending
Persona: Mo, Pat. Outcome: nothing pending is hidden, nothing pending looks done.
1. [swaps] Mo sees every request they are party to, with its state and whose action is awaited
2. [swaps] Pat sees every open accepted request awaiting a decision, oldest first, those Pat is party to marked
3. [notifications] Mo reads their notifications, newest first, and marks one read

## Screens
| Screen | Journey steps | Anchors |
|---|---|---|
| Sign in | J-01#5 | sign-in-form, sign-in-email, sign-in-passcode, sign-in-submit |
| Team | J-01#2, J-01#3, J-01#4 | team-list, member-add, member-role, member-deactivate |
| Week board | J-02#1, J-02#2, J-02#3, J-03#1, J-03#2, J-04#6 | week-board, week-picker, board-draft, board-none, shift-create, shift-assign, shift-unassign, week-publish, board-filter-mine, board-empty-mine, holder-row, holder-pending-badge, holder-request-swap |
| Swap request | J-04#1 | swap-request-form, swap-counterpart, swap-reason, swap-submit |
| Swap inbox | J-04#3, J-04#5, J-05#1, J-05#2 | swap-inbox, swap-accept, swap-decline, swap-decline-reason, swap-approve, swap-refuse, swap-refuse-reason, swap-state, swap-awaiting, swap-party, swap-decision |
| Notifications | J-01#6, J-02#4, J-04#2, J-04#4, J-04#7, J-05#3 | notification-list, notification-item, notification-mark-read, notification-empty |

## Domains
| Domain | Owner PM | Purpose |
|---|---|---|
| identity | pm-lead | members, roles, passcodes and tokens, who the caller is |
| scheduling | pm-lead | weeks, shifts, assignments, the board, the transfer |
| swaps | pm-swaps | swap requests, answers, decisions and their reasons |
| notifications | pm-lead | telling the people affected what changed, never overstating |

## Entities
| Entity | Domain | Description | Key fields |
|---|---|---|---|
| Member | identity | a person on the team | id, name, email (unique, compared case-insensitively), role, active, passcode_hash, token (one; replaced by each sign-in) |
| Role | identity | admin, planner or member | name |
| Week | scheduling | the seven days from a Monday, keyed by that date; comes into being with its first shift | start_date (a Monday, the key), state (draft, published) |
| Shift | scheduling | a set of slots on one day of a week; immutable once created in this version | id, week_start, date, start, end (times of day on that date; end after start; never crossing midnight), slots (≥ 1) |
| Assignment | scheduling | a member holding one slot of a shift | id, shift_id, member_id |
| SwapRequest | swaps | a request to hand an assignment to a counterpart, with the counterpart's answer | id, assignment_id, requester_id, counterpart_id, reason (the requester's), state (requested, accepted, declined, approved, refused), created_at, answered_at, answer_reason (the counterpart's, on decline); `expired` is derived on read (requested or accepted, deadline passed), never stored |
| Decision | swaps | the decision on an accepted request, approved or refused, with the reason | id, request_id, decider_id, outcome (approved, refused), reason (absent on approved; on refused one of the four caller codes, or counterpart_overlap / counterpart_inactive set only by the system), decided_at |
| Notification | notifications | a message to one member about one event | id, recipient_id, event (one of the nine event codes of R-notifications-01), text, created_at, read |

## Roles
| Role | Description |
|---|---|
| admin | manages members and roles; creates, assigns and publishes weeks; decides any swap they are not party to |
| planner | creates, assigns and publishes weeks; decides any swap they are not party to |
| member | views the board, requests and answers swaps for their own assignments, reads their own notifications |

## Permissions
Every cell presumes the caller resolved from the bearer token (cross-cutting rules). `own` = only for assignments, requests or notifications where the caller is the holder, a party or the recipient.
| Action | admin | planner | member |
|---|---|---|---|
| seed the first admin (operator command, outside the API) | — | — | — |
| sign in | allowed | allowed | allowed |
| list members (id, name, role, active; never passcode or token) | allowed | allowed | allowed |
| manage members and roles | allowed | denied | denied |
| list weeks (members: published only) | allowed | allowed | allowed |
| create shifts, assign, unassign, publish a week | allowed | allowed | denied |
| view the week board (draft weeks: planners and admins only) | allowed | allowed | allowed |
| request a swap | own | own | own |
| accept or decline a swap | own | own | own |
| approve or refuse a swap | allowed (not party) | allowed (not party) | denied |
| list my requests (requester or counterpart) | own | own | own |
| see pending decisions | allowed | allowed | denied |
| read and mark notifications | own | own | own |

## Open design questions
| Q | Question | Recommendation | Ruling |
|---|---|---|---|
| Q-01 | Who approves a swap in which the planner is a party? | the admin (segregation of duties: R-swaps-05) | ruled 2026-11-07: the admin; generalised by DESIGN-REVIEW-1 (A7): any admin or planner who is not a party decides, a party never does |
