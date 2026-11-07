# OPEN-QUESTIONS — Team Rota
Not a to-do list. A `Q-nn` is a conflict, gap or ambiguity between the documents and what a session must do; it is raised by the session that meets it and ruled by the operator, usually through the design-change loop (`/adu-lifecycle:change-design`). Product behaviour belongs in FEEDBACK.md instead. Ids come from `adu next-id Q`; a question raised off this tree (in a pack or a verification report) is numbered provisionally (`Q-p<n>`) until the apply step allocates it; a provisional id never enters this file.

Entry format:
```
### Q-nn · YYYY-MM-DD · ADU-nn (or the phase) · open | resolved → vX.Y | resolved → D-nn | withdrawn
**Conflict:** what disagrees with what, quoted with file and line.
**Blocking:** yes | no — a blocking question stops the unit; a non-blocking one lets it proceed with the assumption stated in the journal.
**Options:** two or three, each with its consequence; the raiser recommends one.
**Resolution:** the ruling, who made it, the date, and the document it now lives in.
```

### Q-01 · 2026-11-07 · design-product (pm-lead) · resolved → PRODUCT-DESIGN v1.0
**Conflict:** the permissions matrix lets a planner approve swaps and lets a planner request swaps of their own assignments; nothing said who approves a swap the planner is party to.
**Blocking:** no — relevant at the swaps stories.
**Options:** (1) the admin approves such swaps (segregation of duties); (2) a second planner, if any; (3) the planner may approve their own.
**Resolution:** option 1, the operator, 2026-11-07; the rule lives in design/domains/swaps/spec.md (R-swaps-05) and the permissions matrix ("allowed (not party)" (generalised by DESIGN-REVIEW-1 A7)).

### Q-02 · 2026-11-07 · review-design (DESIGN-REVIEW-5 A13) · open
**Question:** should deactivation end a member's open requests as counterpart?
**Blocking:** no — the design as written is consistent; the build proceeds with the dead end shown as the truth.
**Conflict:** a counterpart deactivated while a request is in state requested (allowed by R-identity-05, since they hold no future assignment) can neither sign in nor answer; nobody else may answer (not_counterpart); deciders may not act (wrong_state); the requester cannot withdraw (out of scope) nor re-request (request_open) until expiry, and after expiry past_deadline bars a new request — the shift cannot be handed over at all. The design shows the truth as it is (brief §4), so no contract guess is needed, but the outcome is a dead end the operator may not want.
**Options:** (a) leave it: the truth is shown; the member works the shift or the roster is wrong; (b) deactivation declines that member's open requests as counterpart with a system reason (one more event: swap_declined with reason counterpart_inactive, to the requester); (c) allow withdrawal by the requester (a design change: a withdraw transition from requested).
**Resolution:** none yet — the raiser recommends (b), smallest and honest; it is a change of scope (one more event), so it is the operator's call in the design-change loop, not a session's.

### Q-03 · 2026-11-07 · review-design (DESIGN-REVIEW-5 A13) · open
**Question:** should an accepted request with no eligible decider be refused by the system?
**Blocking:** no.
**Conflict:** when every active admin and planner is a party to the swap, swap_accepted finds an empty decider set and the request shows "awaiting decider" with nobody able to decide until it expires.
**Options:** (a) leave it (truthful, and rare on a team with one admin and two planners); (b) the system refuses it at acceptance with a new reason no_decider; (c) seeding a second admin is an operator practice recorded in the runbook.
**Resolution:** none yet — the raiser recommends (a) now and (c) in the runbook; revisit with the first real team.

### Q-04 · 2026-11-07 · ADU-00 (hand-over) · resolved → adu.toml (operator's grant recorded in the journal)
**Conflict:** `adu.toml [commands].gate` is `uv run pytest tests/ -q -m "not timing" && npm --prefix frontend run test -- --run` (the two adapters joined at scaffold), but no `frontend/` exists until ADU-12 (UI foundation) — the gate for ADU-00..11 fails on the npm half before any test runs, so no unit before ADU-12 can close under the gate as written. Seen in the ADU-00 hand-over (section C2).
**Blocking:** yes — for the closure of every unit before ADU-12.
**Options:** (1) the operator edits the protected `adu.toml` so gate, fast and lint are the python commands until ADU-12, and ADU-12's entry amends `adu.toml` back to the combined commands under a recorded grant; (2) ADU-00 scaffolds a minimal frontend with one passing test — outside its roster and its stories; (3) the gate wraps the npm half in a directory test — hides a missing frontend forever.
**Resolution:** option 1, 2026-11-07. The operator's grant for this protected edit is the standing instruction for the example run (the operator asked for ADU-00..02 to be executed in this run); recorded in this session's journal as a grant paragraph. Package feedback: a combined-adapter scaffold must not produce a gate that cannot pass before the second adapter's first unit.
