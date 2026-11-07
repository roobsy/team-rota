# FEEDBACK — Team Rota
Defects, friction and ideas found by using or operating the product, triaged at each milestone close. A defect is fixed by a **Defect session** (`/adu-lifecycle:defect FB-nn`): a failing test shown red, the minimal fix, the test permanent and immutable. Ids come from `adu next-id FB`.

Entry format:
```
### FB-nn · YYYY-MM-DD · area (file, unit) · open | fixed YYYY-MM-DD | deferred → ADU-nn | wontfix
**Observation:** the one-line fault, how it was found, and why the tests missed it.
**Disposition:** added at triage — the defect session, the unit that absorbs it, or the reason it is not fixed.
```

## Defects

### FB-01 · 2026-11-07 · tests/layering_scan.py (committed at the architecture phase, 2ba56ac; guarded by ADU-00's arms in tests/test_layering.py) · open
**Observation:** the operator's first own gate run (M1 release; a fresh Windows PowerShell, cp1252 locale, `PYTHONUTF8` unset) — `uv run pytest tests/ -q -m "not timing"` → `2 failed, 40 passed, 1 warning in 19.79s`: `tests/test_layering.py::test_a_planted_forbidden_import_is_caught` and `::test_the_baseline_fails_both_ways`. The scan's child process dies with `UnicodeEncodeError: 'charmap' codec can't encode character '→'`: its messages carry `→` and `—` (lines 121, 156, 189–196) and its stdout is a pipe in the locale encoding. Reproduced by the release session in the project's own environment: `env -u PYTHONUTF8 uv run pytest tests/test_layering.py -q` → `2 failed, 1 passed`; with `PYTHONUTF8=1` → `3 passed`. Missed because every earlier gate ran in a Claude Code session whose launching shell had set `PYTHONUTF8=1` (M1's ✅s were session-run — the caveat of the record), and no test forces a non-UTF-8 child. Upstream: the plugin's FB-18 (the adapter's template carries the same fault).
**Disposition:** defect session now, before the M1 tag — `/adu-lifecycle:defect FB-01` in a fresh session launched from a shell where `PYTHONUTF8` is unset. M1 stays open until the fix is on `main` and the operator's gate is green in a default Windows PowerShell. Release manager, 2026-11-07.

## Friction

## Ideas

## Closed
