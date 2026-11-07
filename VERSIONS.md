# VERSIONS — Team Rota
The authority on every governing document's version. On any disagreement between a document's own header line and this table, this table wins — which is why no document pins another's version in its text (a pointer that can disagree with the authority is a pointer that will).

Scheme: `vMAJOR.MINOR` — a requirement changed (design-change loop, operator decision). `vMAJOR.MINOR.PATCH` — editorial, no requirement changed. Only the release-manager session (or the apply step of a design-change loop) bumps a version, on `main`; everyone else proposes with a provisional version.

## Current
| Document | Version | Role |
|---|---|---|
| CLAUDE.md | 1.0 | constitution |
| design/PRODUCT-BRIEF.md | 1.0 | purpose (content-pinned, D-01) |
| design/PRODUCT-DESIGN.md | 1.3 | product design |
| design/ARCHITECTURE.md | 0.1 | architecture contract |
| contracts/openapi.yaml | 0.1 | API contract |
| ADU-PLAN.md | 0.1 | the plan |

## History
<!-- ### YYYY-MM-DD — DOC vX / DOC vY: <ID> — <summary>, then a table | Document | From | To | What changed | -->

### 2026-11-07 — PRODUCT-BRIEF v1.0: D-01 — the brief approved and pinned
| Document | From | To | What changed |
|---|---|---|---|
| design/PRODUCT-BRIEF.md | 0.1 | 1.0 | purpose, personas, North Star, never-becomes, non-goals, success written in the operator's terms and approved |


### 2026-11-07 — PRODUCT-DESIGN v1.0: Q-01 — personas, five journeys (18 steps), five screens, four domains, eight entities, three roles, the permissions matrix
| Document | From | To | What changed |
|---|---|---|---|
| design/PRODUCT-DESIGN.md | 0.1 | 1.0 | the design written; Q-01 ruled (the admin approves a swap the planner is party to) |

### 2026-11-07 — PRODUCT-DESIGN v1.1: DESIGN-REVIEW-1 — 56 findings (architect 25, developer 31) dispositioned, all accepted
| Document | From | To | What changed |
|---|---|---|---|
| design/PRODUCT-DESIGN.md | 1.0 | 1.1 | cross-cutting rules (caller, forbidden, clock, derived states); J-01 gains seed, sign-in and account-change steps; J-05 gains the notifications read; Sign-in screen; Week implicit from a Monday; Shift times of day; SwapRequest timestamps, expired derived; Approval renamed Decision; deciders = any non-party admin or planner |
| stories/ | 18 | 22 | US-identity-004/005, US-notifications-005/006 added; every story's arms made falsifiable (reason codes, fixtures, anchors); 5 UI arms; forbidden arms |
| design/domains/*/spec.md | 1.0 | 1.1 | identity 5→8 rules, scheduling 6→8, swaps 7→9, notifications 3→4; every "needs from others" section filled against IR-01..IR-10 |

### 2026-11-07 — PRODUCT-DESIGN v1.2: DESIGN-REVIEW-2 — 52 findings (architect 25, developer 27; 14 blocking each) dispositioned, all accepted
| Document | From | To | What changed |
|---|---|---|---|
| design/PRODUCT-DESIGN.md | 1.1 | 1.2 | the caller resolved once (IR-11), refusal shape and precedence, not_found, half-open deadlines, tiebreaks, "open" defined once; list members and list weeks with the current week; badge per holder-row; SwapRequest answered_at/answer_reason; ids on every entity; board-draft/board-none anchors |
| stories/ | 22 (86 arms) | 22 (107 arms) | UI arms on every screen story; token lifecycle; the §6 end-to-end arm on US-swaps-003; the quantitative arm with its predicate and fixture; identity no longer asserts other domains' lists |
| design/domains/*/spec.md | 1.1 | 1.2 | the nine typed Notifier events with payloads (R-notifications-01); R-scheduling-09 fixture; R-identity-09 list; transactions and the internal transfer stated |
| design/INTERFACE-REQUESTS.md | IR-01..10 | IR-01..11 | rows widened to what the rules need; the service cycles accepted explicitly |

### 2026-11-07 — PRODUCT-DESIGN v1.3: DESIGN-REVIEW-3 — 22 findings (architect 11, developer 11; one blocking each) dispositioned, all accepted
| Document | From | To | What changed |
|---|---|---|---|
| design/PRODUCT-DESIGN.md | 1.2 | 1.3 | the Reason codes table (bucket and HTTP status for every code); order within a bucket; ids in creation order; holder-request-swap and notification-mark-read anchors; Decision.reason values |
| stories/ | 22 (107 arms) | 22 (108 arms) | publishing twice refused; the seed emits nothing; same-role change a no-op; lists carry shift and names; the timing arm's call; the transfer arm's predicate |
| design/domains/*/spec.md | 1.2 | 1.3 | R-scheduling-04/08/09, R-identity-01/06/07/09, R-swaps-04/07/09, R-notifications-01 reworded as the dispositions say |
| design/INTERFACE-REQUESTS.md | IR-01..11 | IR-01..12 | IR-12 (active member ids for week_published); IR-07 no longer re-entrant |
