# PRODUCT-DESIGN — Team Rota
v1.0 · owned by the pm-lead (`/adu-lifecycle:design-product`); checked by `adu design check`; reviewed by the architect and the developer (`/adu-lifecycle:review-design`) before stories are written. Everything here serves the North Star in `design/PRODUCT-BRIEF.md`: the roster tells each person the truth about their week, plainly, even when unwelcome.

## Personas
| Persona | Role | Goal | Pain today |
|---|---|---|---|
| Pat | planner | publish a fair, complete week early and settle swaps without chasing | the spreadsheet is one message behind the chat |
| Mo | member | see the week early and hand over a shift without a phone tree | a swap agreed in chat is forgotten by the roster |
| Avi | admin | keep members and roles right; nobody approves their own swap | no record of who agreed to what |

## Journeys
### J-01 — Admin sets up the team
Persona: Avi. Outcome: every member exists with one role and can sign in.
1. [identity] Avi adds a member with a name, an email and a role
2. [identity] Avi changes a member's role
3. [identity] Avi deactivates a member, who keeps their history but can no longer be assigned

### J-02 — Planner publishes a week
Persona: Pat. Outcome: the week is visible to every member, who were all told.
1. [scheduling] Pat creates the shifts of a week (date, start, end, slots)
2. [scheduling] Pat assigns active members to shifts, no member twice in one shift and no overlapping shifts for one member
3. [scheduling] Pat publishes the week; a published week is read-only except through swaps
4. [notifications] every active member is notified that the week is published

### J-03 — Member views the week
Persona: Mo. Outcome: Mo knows who holds every shift and what is pending.
1. [scheduling] Mo opens the week board and sees every shift with its holders and any pending swap on it
2. [scheduling] Mo filters the board to their own shifts

### J-04 — Member hands over a shift
Persona: Mo. Outcome: a counterpart holds Mo's shift, the planner approved it, everyone concerned was told.
1. [swaps] Mo requests a swap of one of their assignments, naming a counterpart and a reason code, before the shift's deadline
2. [notifications] the counterpart is notified of the request
3. [swaps] the counterpart accepts or declines the request
4. [notifications] the requester and the planner are notified of the counterpart's answer
5. [swaps] the planner approves or refuses the accepted request with a reason code; a planner never approves a swap they are party to
6. [scheduling] on approval the assignment moves to the counterpart and the board shows it
7. [notifications] both members are notified of the outcome, with the reason when refused

### J-05 — Anyone reads what is pending
Persona: Mo, Pat. Outcome: nothing pending is hidden, nothing pending looks done.
1. [swaps] Mo sees their open requests with their current state and who is holding them up
2. [swaps] Pat sees every accepted request awaiting approval, oldest first

## Screens
| Screen | Journey steps | Anchors |
|---|---|---|
| Team | J-01#1, J-01#2, J-01#3 | team-list, member-add, member-role, member-deactivate |
| Week board | J-02#1, J-02#2, J-02#3, J-03#1, J-03#2, J-04#6 | week-board, week-picker, shift-create, shift-assign, week-publish, board-filter-mine, shift-pending-badge |
| Swap request | J-04#1 | swap-request-form, swap-counterpart, swap-reason, swap-submit |
| Swap inbox | J-04#3, J-04#5, J-05#1, J-05#2 | swap-inbox, swap-accept, swap-decline, swap-approve, swap-refuse, swap-state |
| Notifications | J-02#4, J-04#2, J-04#4, J-04#7 | notification-list, notification-item |

## Domains
| Domain | Owner PM | Purpose |
|---|---|---|
| identity | pm-lead | members, roles, who may do what |
| scheduling | pm-lead | weeks, shifts, assignments, the board |
| swaps | pm-lead | swap requests, acceptances, approvals, their reasons |
| notifications | pm-lead | telling the people affected what changed, never overstating |

## Entities
| Entity | Domain | Description | Key fields |
|---|---|---|---|
| Member | identity | a person on the team | id, name, email, role, active |
| Role | identity | admin, planner or member | name |
| Week | scheduling | seven days with a publication state | start_date, state (draft, published) |
| Shift | scheduling | a slot on a day of a week | week, date, start, end, slots |
| Assignment | scheduling | a member holding a shift | shift, member |
| SwapRequest | swaps | a request to hand an assignment to a counterpart | assignment, requester, counterpart, reason, state (requested, accepted, declined, approved, refused, expired) |
| Approval | swaps | the planner's decision on an accepted request | request, decider, outcome, reason |
| Notification | notifications | a message to one member about one event | recipient, event, text, read |

## Roles
| Role | Description |
|---|---|
| admin | manages members and roles; approves swaps a planner is party to |
| planner | creates, assigns and publishes weeks; approves swaps |
| member | views the board, requests and accepts swaps for their own assignments |

## Permissions
| Action | admin | planner | member |
|---|---|---|---|
| manage members and roles | allowed | denied | denied |
| create shifts, assign, publish a week | allowed | allowed | denied |
| view the week board | allowed | allowed | allowed |
| request a swap | own | own | own |
| accept or decline a swap | own | own | own |
| approve or refuse a swap | allowed (not own) | allowed (not own) | denied |
| read notifications | own | own | own |

## Open design questions
| Q | Question | Recommendation | Ruling |
|---|---|---|---|
| Q-01 | Who approves a swap in which the planner is a party? | the admin (segregation of duties: R-swaps-05) | ruled 2026-11-07: the admin; recorded in design/domains/swaps/spec.md |
