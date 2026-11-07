# VERSIONS — Team Rota
The authority on every governing document's version. On any disagreement between a document's own header line and this table, this table wins — which is why no document pins another's version in its text (a pointer that can disagree with the authority is a pointer that will).

Scheme: `vMAJOR.MINOR` — a requirement changed (design-change loop, operator decision). `vMAJOR.MINOR.PATCH` — editorial, no requirement changed. Only the release-manager session (or the apply step of a design-change loop) bumps a version, on `main`; everyone else proposes with a provisional version.

## Current
| Document | Version | Role |
|---|---|---|
| CLAUDE.md | 1.0 | constitution |
| design/PRODUCT-BRIEF.md | 1.0 | purpose (content-pinned, D-01) |
| design/PRODUCT-DESIGN.md | 1.0 | product design |
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
