# ARCHITECTURE — Team Rota
v0.1 · draft · owned by the architect (`/adu-lifecycle:design-architecture`). The walls a unit may not cross, written so the layering ratchet (`tests/test_layering.*`) fails the build when one does.

## Stack and adapter
Adapter: `python-fastapi-uv,react-vite-vitest` (see `adu.toml`). Runtime: … Storage: … UI: …

## Layers
| Layer | Name | Path prefixes | May import |
|---|---|---|---|
| 0 | scaffold | project files | — |
| 1 | data model | `src/app/models.*`, `src/app/db.*` | nothing of the product |
| 2 | contract & stubs | `contracts/`, `src/app/*/null_*.py` | 1 |
| 3 | domain services | `src/app/<domain>/service.*`, `src/app/core/**` | 1, 2 (protocols only) |
| 4 | API | `src/app/api/**` | 3, 1 |
| 5 | UI | `frontend/src/**` | the generated client only |
| 6 | cross-cutting / packaging | `src/app/cli.*`, `src/app/main.*` (composition root) | everything |

## Allowed edges (the ratchet's configuration)
<!-- forbidden crossings are asserted zero; tolerated edges are frozen in tests/layering_baseline.json and may only shrink -->
- 3 → 4, 3 → 5, 1 → anything above: forbidden.
- Private reaches (`_name` across modules): frozen at the baseline.
- The composition root is the only module that imports the API, the services and the model together.

## Dependency roster
| Package | Layer | Admitted by |
|---|---|---|

## Persistence and concurrency rules
- One write transaction per request; compute first, then write (never hold the write lock across a computation).
- No in-memory database shared by concurrent sessions in tests; file-backed workspaces for contention tests.
- Every path through the platform's path library; no non-loopback network at test time.

## Protected paths
<!-- security-critical modules, mirrored in adu.toml [protected] -->

## Decisions
<!-- the D-nn rows this document rests on -->
