# VERSIONS — Team Rota
The authority on every governing document's version. On any disagreement between a document's own header line and this table, this table wins — which is why no document pins another's version in its text (a pointer that can disagree with the authority is a pointer that will).

Scheme: `vMAJOR.MINOR` — a requirement changed (design-change loop, operator decision). `vMAJOR.MINOR.PATCH` — editorial, no requirement changed. Only the release-manager session (or the apply step of a design-change loop) bumps a version, on `main`; everyone else proposes with a provisional version.

## Current
| Document | Version | Role |
|---|---|---|
| CLAUDE.md | 1.0 | constitution |
| design/PRODUCT-BRIEF.md | 1.0 | purpose (content-pinned, D-01) |
| design/PRODUCT-DESIGN.md | 1.7 | product design (agreed, D-02) |
| design/ARCHITECTURE.md | 1.1 | architecture contract |
| contracts/openapi.yaml | 1.1 | API contract |
| ADU-PLAN.md | 1.1 | the plan |

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

### 2026-11-07 — PRODUCT-DESIGN v1.4: DESIGN-REVIEW-4 — 28 findings (architect 13, developer 15; four distinct blocking) dispositioned, all accepted
| Document | From | To | What changed |
|---|---|---|---|
| design/PRODUCT-DESIGN.md | 1.3 | 1.4 | cross-story order in the state bucket; invalid_request; the internal codes row; a Permissions row for my requests; inbox reason anchors |
| stories/ | 22 (108 arms) | 22 (108 arms) | holder-row fields incl. requestable; counterpart check order; swap_refused recipients; one answer operation; the week-picker; mine rows; the E2E's clock; Data touched corrected |
| design/domains/*/spec.md | 1.3 | 1.4 | R-scheduling-05/09, R-swaps-03/06/07/08, R-notifications-01 |
| design/INTERFACE-REQUESTS.md | IR-07 | IR-07 widened | pending and requestable per assignment; the third cycle named |

### 2026-11-07 — PRODUCT-DESIGN v1.5: DESIGN-REVIEW-5 — 21 findings (architect 13, developer 8; three distinct blocking) dispositioned, all accepted; Q-02, Q-03 opened
| Document | From | To | What changed |
|---|---|---|---|
| design/PRODUCT-DESIGN.md | 1.4 | 1.5 | invalid_request narrowed; role and reason codes as strings enumerated by the domain; the state bucket's leading codes named exactly; status per operation; Role an enumeration |
| stories/ | 22 (108 arms) | 22 (108 arms) | the request row of R-swaps-09 everywhere; the assign order; unfilled rows; the timer boundary; email case at sign-in |
| design/domains/*/spec.md | 1.4 | 1.5 | R-swaps-03/06/09, R-scheduling-03/05/07/09, R-identity-06 |
| design/INTERFACE-REQUESTS.md | IR-07 | IR-07 restated | exact inputs and outputs; IR-06 without role; IR-01/IR-09 story columns complete |

### 2026-11-07 — PRODUCT-DESIGN v1.6: DESIGN-REVIEW-6 — 21 findings (architect 7, one blocking; developer 14, none, AGREED) dispositioned, all accepted
| Document | From | To | What changed |
|---|---|---|---|
| design/PRODUCT-DESIGN.md | 1.5 | 1.6 | lenient body read and invalid_request first within validation; the Reason codes table completed (repeated deactivation, counterpart_overlap at request, the seed's exit status) |
| stories/ | 22 (108 arms) | 22 (109 arms) | repeated deactivation; counterpart_overlap at request; anchors named in the sign-in and swap-form arms; stored state vs expiry; the board's shape |
| design/domains/*/spec.md | 1.5 | 1.6 | R-identity-04, R-scheduling-01/05, R-swaps-03/08/09, R-notifications-01/02 |
| design/INTERFACE-REQUESTS.md | IR-01/06/09 | restated | the shift's representation, the intersecting-shift check, absent ids → not_found |

### 2026-11-07 — PRODUCT-DESIGN v1.7: DESIGN-REVIEW-7 — both AGREED (D-02); the 16 cosmetic findings applied
| Document | From | To | What changed |
|---|---|---|---|
| design/PRODUCT-DESIGN.md | 1.6 | 1.7 | lenient read of path and query; sign-in's unreadable body; writes answer rows; Role an enumeration in the table; the header points at VERSIONS.md |
| stories/ | 22 (109 arms) | 22 (109 arms) | not_found named per operation; unfilled rows; the weeks list's shape; mark-read twice; the shift-create form carries the week |
| design/domains/*/spec.md | 1.6 | 1.7 | R-scheduling-03/06/09, R-notifications-04 |
| design/INTERFACE-REQUESTS.md | — | — | IR-06 story column; IR-09 'eligible' wording; the Build order pointer |

### 2026-11-07 — ARCHITECTURE v1.0: D-03..D-06 — layers, allowed edges, roster, persistence and transactions, the five ports, the layering baseline on the empty tree
| Document | From | To | What changed |
|---|---|---|---|
| design/ARCHITECTURE.md | 0.1 | 1.0 | written against design v1.5; the layering scan and baseline committed |

### 2026-11-07 — contracts/openapi.yaml v1.0, design/INTERFACES.md v1.0: D-07 — 18 operations, five protocols, the request row, examples as the mock
| Document | From | To | What changed |
|---|---|---|---|
| contracts/openapi.yaml | 0.1 | 1.0 | every story action an operation with operationId <domain>.<action>, x-story, x-roles, named synthetic examples, explicit refusals with enumerated reasons; Spectral clean; Prism serves every operation with zero validator errors (docs/CONTRACT-SMOKE.md) |
| design/INTERFACES.md | 0.1 | 1.0 | Clock, MemberDirectory, SchedulingPort, SwapsPort, Notifier with signatures, Null implementations and the build order; the traceability table |

### 2026-11-07 — ADU-PLAN v1.0: D-08 — 16 units in four milestones, three in-process mocks, the derived order
| Document | From | To | What changed |
|---|---|---|---|
| ADU-PLAN.md | 0.1 | 1.0 | cut by the twenty rules from stories v1.5, the contract and the interfaces; `adu plan check` green with no warnings |

### 2026-11-07 — ADU-PLAN v1.1, ARCHITECTURE v1.1, contract v1.1, INTERFACES v1.0.1: D-09, D-10 — the developer's buildability read (docs/PLAN-REVIEW-1.md, 23 findings, all accepted)
| Document | From | To | What changed |
|---|---|---|---|
| ADU-PLAN.md | 1.0 | 1.1 | 18 units: ADU-16 (ports, Nulls, doubles) and ADU-17 (client and sign-in) inserted; every retirement a declared amendment; the CLI at layer 6; Prism out of the gate; the §6 path asserted in ADU-07; milestones from the new order |
| design/ARCHITECTURE.md | 1.0 | 1.1 | D-09 frontend toolchain in the roster; contract_stubs and serve.py named; frozen edges removed from the layering law's configuration |
| contracts/openapi.yaml | 1.0 | 1.1 | MemberSummary for identity.list_members (additive; the golden is pinned by ADU-02) |
| design/INTERFACES.md | 1.0 | 1.0.1 | the doubles section; ADU-16 as the Nulls' creator; SwapsPort.view in the traceability |
