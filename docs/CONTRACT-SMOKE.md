# CONTRACT-SMOKE — Team Rota
One request per operation against `npx --yes @stoplight/prism-cli mock contracts/openapi.yaml` (port 4010, loopback), 2026-11-07 06:42. Prism serves the contract's own examples (x-synthetic) and validates every response against its schema; a validator error in its log is a contract fault.

| operationId | request | status |
|---|---|---|
| identity.sign_in | POST /auth/sign-in | 200 |
| identity.list_members | GET /members | 200 |
| identity.add_member | POST /members | 201 |
| identity.change_role | PATCH /members/2/role | 200 |
| identity.deactivate | POST /members/4/deactivate | 200 |
| scheduling.create_shift | POST /weeks/2026-11-09/shifts | 201 |
| scheduling.assign | POST /shifts/11/assignments | 201 |
| scheduling.unassign | DELETE /assignments/101 | 204 |
| scheduling.publish | POST /weeks/2026-11-09/publish | 200 |
| scheduling.board | GET /weeks/2026-11-09/board?mine=true | 200 |
| swaps.request | POST /swaps | 201 |
| swaps.answer | POST /swaps/501/answer | 200 |
| swaps.decide | POST /swaps/501/decision | 200 |
| swaps.mine | GET /swaps/mine | 200 |
| swaps.pending | GET /swaps/pending | 200 |
| notifications.list | GET /notifications | 200 |
| notifications.mark_read | POST /notifications/9002/read | 200 |
| swaps.request (refusal example) | POST /swaps Prefer: code=409, example=past_deadline | 409 |

Validator errors in Prism's log: 0 (expected 0).
