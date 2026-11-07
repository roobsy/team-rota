# PRODUCT-DESIGN — Team Rota
v1.1 · owned by the pm-lead (`/adu-lifecycle:design-product`); checked by `adu design check`; reviewed by the architect and the developer (`/adu-lifecycle:review-design`) before stories are written. Everything here serves the North Star in `design/PRODUCT-BRIEF.md`: the roster tells each person the truth about their week, plainly, even when unwelcome. v1.1 applies the dispositions of `design/DESIGN-REVIEW-1.md` (56 findings): sign-in and the first admin, implicit Monday weeks, the clock, atomic approval, derived expiry, the decider rule, the forbidden rule, the notifications read path and account-change events.

## Personas
| Persona | Role | Goal | Pain today |
|---|---|---|---|
| Pat | planner | publish a fair, complete week early and settle swaps without chasing | the spreadsheet is one message behind the chat |
| Mo | member | see the week early and hand over a shift without a phone tree | a swap agreed in chat is forgotten by the roster |
| Avi | admin | keep members and roles right; nobody decides their own swap | no record of who agreed to what |

## Cross-cutting rules (apply to every journey)
- **The caller.** Every operation except sign-in and the operator's seed command carries a bearer token issued by identity at sign-in; the acting member is the one the token identifies. A missing or invalid token is refused with reason `unauthenticated`.
- **The forbidden rule.** An action by a role the Permissions table denies is refused with reason `forbidden`; an action on something that is not the caller's own, where the table says `own`, is refused with the reason the story names.
- **The clock.** Every action reads `now` from an injected clock; tests set it. Times are naive local times of the team (one team, one timezone, a fixed deployment setting). A shift's start instant is its date plus its start time; a week is "future" when its start_date is after the clock's today.
- **Nothing pending looks done.** States are shown as they are; a derived display state (`expired`) is computed on read and never stored.

## Journeys
### J-01 — Admin sets up the team
Persona: Avi. Outcome: the team exists with one admin, every member has one role, a passcode and can sign in, and is told of changes to their account.
1. [identity] the operator seeds the first admin with a command outside the API, once, on an empty team
2. [identity] Avi adds a member with a name, an email, a role and a passcode
3. [identity] Avi changes a member's role
4. [identity] Avi deactivates a member, who keeps their history but can no longer be assigned or sign in
5. [identity] a member signs in with email and passcode and receives the token every later operation carries
6. [notifications] the member is told when they are added, when their role changes and when they are deactivated

### J-02 — Planner publishes a week
Persona: Pat. Outcome: the week is visible to every member, who were all told.
1. [scheduling] Pat creates the shifts of a week (date, start, end, slots); the week is named by its Monday and comes into being with its first shift
2. [scheduling] Pat assigns active members to shifts, no member twice in one shift and no overlapping shifts for one member, and removes a mistaken assignment while the week is a draft
3. [scheduling] Pat publishes the week; a published week changes only through an approved swap
4. [notifications] every active member is notified that the week is published

### J-03 — Member views the week
Persona: Mo. Outcome: Mo knows who holds every shift and what is pending.
1. [scheduling] Mo opens the week board and sees every shift with its holders and the state of any open swap on it
2. [scheduling] Mo filters the board to their own shifts

### J-04 — Member hands over a shift
Persona: Mo. Outcome: a counterpart holds Mo's shift, a planner or admin who is not a party approved it, everyone concerned was told.
1. [swaps] Mo requests a swap of one of their assignments on a published week, naming a counterpart and a reason code, before the shift's deadline
2. [notifications] the counterpart is notified of the request
3. [swaps] the counterpart accepts or declines the request
4. [notifications] the requester and every member eligible to decide the request are notified of the counterpart's answer
5. [swaps] a planner or admin who is not a party approves or refuses the accepted request with a reason code; approval transfers the assignment first and records the decision second, atomically
6. [scheduling] on transfer the assignment moves to the counterpart and the board shows it
7. [notifications] both members are notified of the outcome, with the reason when refused

### J-05 — Anyone reads what is pending
Persona: Mo, Pat. Outcome: nothing pending is hidden, nothing pending looks done.
1. [swaps] Mo sees every request they are party to, with its state and whose action is awaited
2. [swaps] Pat sees every accepted request awaiting a decision, oldest first, those Pat is party to marked
3. [notifications] Mo reads their notifications, newest first, and marks one read

## Screens
| Screen | Journey steps | Anchors |
|---|---|---|
| Sign in | J-01#5 | sign-in-form, sign-in-email, sign-in-passcode, sign-in-submit |
| Team | J-01#2, J-01#3, J-01#4 | team-list, member-add, member-role, member-deactivate |
| Week board | J-02#1, J-02#2, J-02#3, J-03#1, J-03#2, J-04#6 | week-board, week-picker, shift-create, shift-assign, shift-unassign, week-publish, board-filter-mine, board-empty-mine, shift-pending-badge |
| Swap request | J-04#1 | swap-request-form, swap-counterpart, swap-reason, swap-submit |
| Swap inbox | J-04#3, J-04#5, J-05#1, J-05#2 | swap-inbox, swap-accept, swap-decline, swap-approve, swap-refuse, swap-state, swap-awaiting, swap-party |
| Notifications | J-01#6, J-02#4, J-04#2, J-04#4, J-04#7, J-05#3 | notification-list, notification-item, notification-empty |

## Domains
| Domain | Owner PM | Purpose |
|---|---|---|
| identity | pm-lead | members, roles, passcodes and tokens, who may do what |
| scheduling | pm-lead | weeks, shifts, assignments, the board, the transfer |
| swaps | pm-swaps | swap requests, answers, decisions and their reasons |
| notifications | pm-lead | telling the people affected what changed, never overstating |

## Entities
| Entity | Domain | Description | Key fields |
|---|---|---|---|
| Member | identity | a person on the team | id, name, email, role, active, passcode_hash, token |
| Role | identity | admin, planner or member | name |
| Week | scheduling | the seven days from a Monday, with a publication state; comes into being with its first shift | start_date (a Monday), state (draft, published) |
| Shift | scheduling | a set of slots on one day of a week; immutable once created in this version | week, date, start, end (times of day on that date; end after start; never crossing midnight), slots (≥ 1) |
| Assignment | scheduling | a member holding one slot of a shift | shift, member |
| SwapRequest | swaps | a request to hand an assignment to a counterpart | assignment, requester, counterpart, reason, state (requested, accepted, declined, approved, refused), created_at, accepted_at; `expired` is derived on read (deadline passed, no decision), never stored |
| Decision | swaps | the decision on an accepted request, approved or refused, with the reason | request, decider, outcome (approved, refused), reason, decided_at |
| Notification | notifications | a message to one member about one event | recipient, event, text, created_at, read |

## Roles
| Role | Description |
|---|---|
| admin | manages members and roles; creates, assigns and publishes weeks; decides any swap they are not party to |
| planner | creates, assigns and publishes weeks; decides any swap they are not party to |
| member | views the board, requests and answers swaps for their own assignments, reads their own notifications |

## Permissions
Every cell presumes the caller identified by the bearer token (cross-cutting rules). `own` = only for assignments, requests or notifications where the caller is the holder, a party or the recipient.
| Action | admin | planner | member |
|---|---|---|---|
| seed the first admin (operator command, outside the API) | — | — | — |
| sign in | allowed | allowed | allowed |
| manage members and roles | allowed | denied | denied |
| create shifts, assign, unassign, publish a week | allowed | allowed | denied |
| view the week board (draft weeks: planners and admins only) | allowed | allowed | allowed |
| request a swap | own | own | own |
| accept or decline a swap | own | own | own |
| approve or refuse a swap | allowed (not party) | allowed (not party) | denied |
| see pending decisions | allowed | allowed | denied |
| read and mark notifications | own | own | own |

## Open design questions
| Q | Question | Recommendation | Ruling |
|---|---|---|---|
| Q-01 | Who approves a swap in which the planner is a party? | the admin (segregation of duties: R-swaps-05) | ruled 2026-11-07: the admin; generalised by DESIGN-REVIEW-1 (A7): any admin or planner who is not a party decides, a party never does |
