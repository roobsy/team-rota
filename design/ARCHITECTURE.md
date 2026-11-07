# ARCHITECTURE — Team Rota
v1.1 · owned by the architect (`/adu-lifecycle:design-architecture`). The walls a unit may not cross, written so the layering ratchet (`tests/test_layering.py`) fails the build when one does. Rests on D-03..D-06 and D-09 (the frontend toolchain).

## Stack and adapter
Adapters: `python-fastapi-uv` (API) and `react-vite-vitest` (UI), see `adu.toml`. Runtime: Python 3.12, FastAPI, SQLAlchemy 2 over SQLite (one file per workspace, in-memory never shared across tests). UI: React 18 + Vite + TypeScript, calling the API only through the client generated from `contracts/openapi.yaml`. Auth in this version: sign-in by email and passcode (stored as a salted SHA-256 from the standard library — no new dependency) issuing one opaque bearer token per member; the API layer resolves it once per request into the `Caller` value every service receives (D-04, IR-11).

## Layers
| Layer | Name | Path prefixes | May import |
|---|---|---|---|
| 0 | scaffold | `pyproject.toml`, `src/app/__init__.py`, `tests/conftest.py` | — |
| 1 | data model | `src/app/models.py`, `src/app/db.py`, `src/app/synthetic.py` | nothing of the product |
| 2 | contract & stubs | `contracts/`, `src/app/api/contract_stubs.py` (the 501 placeholders, deleted with the last router), `src/app/ports.py`, `src/app/*/null_*.py`, `tests/support/doubles.py` | 1 |
| 3 | domain services | `src/app/identity/`, `src/app/scheduling/`, `src/app/swaps/`, `src/app/notifications/` (`service.py`, `repo.py`, `rules.py`) | 1, 2 (protocols only — `src/app/ports.py`), its own domain |
| 4 | API | `src/app/api/` (one router module per domain, `deps.py`) | 3, 1, 2 |
| 5 | UI | `frontend/src/` | the generated client only (`frontend/src/client/`) |
| 6 | cross-cutting / packaging | `src/app/main.py` (composition root), `src/app/cli.py` (the operator's commands), `src/app/serve.py` | everything |

A domain service imports another domain only through a protocol in `src/app/ports.py` (`MemberDirectory`, `SchedulingPort`, `SwapsPort`, `Notifier`, `Clock`) bound in the composition root — never the other domain's `service.py`. The service graph has two cycles (identity ↔ scheduling, scheduling ↔ swaps); they are legal only across these ports, and `tests/layering.json` forbids every direct cross-domain import.

## Allowed edges (the ratchet's configuration, `tests/layering.json`)
- 3 → 4, 3 → 5, 3 → 6, 1 → anything above, 2 → 3/4/6: forbidden (asserted zero).
- 3 → 3 across domains (`src/app/swaps/*` importing `src/app/scheduling/*` etc.): forbidden; the port is the only crossing.
- 4 → 4 across routers: forbidden; shared request plumbing lives in `src/app/api/deps.py`.
- Private reaches (`_name` across modules): frozen at the baseline, may only shrink. Nothing else is frozen: the model may be imported by every layer above it, so `tests/layering.json`'s `frozen` list is empty and the baseline on the empty tree holds no edges.
- `src/app/main.py` is the only module that imports the API, every service and the model together.

## Dependency roster
| Package | Layer | Admitted by |
|---|---|---|
| fastapi, uvicorn | 4, 6 | D-03 |
| sqlalchemy | 1 | D-03 |
| pydantic | 1, 4 | D-03 |
| pytest, httpx (test client), ruff | tests | D-03 |
| react, react-dom, vite, typescript, vitest, @testing-library/react | 5 | D-03 |
| openapi-typescript, openapi-fetch (the generated client, the only client) | 5 | D-03, D-09 |
| react-router-dom, jsdom, @testing-library/jest-dom, msw (handlers from the contract's examples) | 5 | D-09 |
| eslint, typescript-eslint, eslint-plugin-react-hooks, dependency-cruiser | 5 (lint) | D-09 |
| @playwright/test | 6 (the browser E2E) | D-09 |
Nothing else is installed by a unit (hard rule 2); a new package is a DECISIONS row first.

## Persistence and concurrency rules
- One session and one write transaction per request, opened by the API layer (`src/app/api/deps.py`) and shared by every service the request touches (the transfer, the decision and their notifications commit together, R-swaps-04); compute first (rules, overlap checks), then write; never hold the write across a computation.
- SQLite file per workspace under a `pathlib.Path`; tests get a fresh file in `tmp_path`, never a shared in-memory engine.
- The clock is injected (`Clock` protocol in `src/app/ports.py`); no service calls `datetime.now()` directly — the swap deadline (R-swaps-01) and expiry (R-swaps-06) are only testable with a controlled clock.
- No randomness in the product; the synthetic generator (`src/app/synthetic.py`) takes a `random.Random(seed)` and reproduces byte for byte.
- No non-loopback network at test time; the UI tests use the generated client against the mock server or MSW handlers built from the contract's examples.

## Protected paths
None beyond the method's own (`adu.toml`, `PINS.lock`, `.claude/settings.json`, `CLAUDE.md`). The adapter's default `src/app/ledger.py` does not exist in this product and is removed from `[protected].paths` on the operator's approval (D-06) — a protected path that names no file is a rule nobody can test.

## Decisions
D-03 (stack and roster) · D-04 (sign-in by email and passcode; one bearer token per member; the caller resolved once per request) · D-05 (the layering law and the five ports) · D-06 (protected paths) · D-09 (the frontend toolchain).
