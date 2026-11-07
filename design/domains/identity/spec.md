# identity — domain spec
v1.2 · owned by pm-lead. The business rules of this domain, each testable, each naming the story it serves. v1.2 applies the dispositions of DESIGN-REVIEW-2.

## Rules
| Rule | Statement | Serves | Testable as |
|---|---|---|---|
| R-identity-01 | One role per member; roles are admin, planner, member; any other name is refused | US-identity-001, US-identity-002 | invalid_role |
| R-identity-02 | An email is unique on the team, compared case-insensitively | US-identity-001 | duplicate_email |
| R-identity-03 | The team always keeps at least one active admin | US-identity-002, US-identity-003 | last_admin on role change and on deactivation |
| R-identity-04 | An inactive member keeps their row, cannot sign in, cannot act on a token issued earlier, and cannot be assigned or transferred to | US-identity-003, US-identity-004 | member_inactive at sign-in; unauthenticated on a stale token; scheduling enforces member_inactive and counterpart_inactive (R-scheduling-02) |
| R-identity-05 | A member who holds an assignment on any shift, in a draft or a published week, whose start instant is after now cannot be deactivated | US-identity-003 | future_assignments (reads scheduling, IR-05) |
| R-identity-06 | Sign-in is email plus passcode (stored hashed); it issues the one bearer token of the member (a new sign-in replaces it) and returns who they are; the API layer resolves the token once per request into the caller {member_id, name, role, active} (IR-11) and passes it to every domain operation; no token, an unknown token or an inactive member's token is unauthenticated — enforced by every operation, verified once by a test that walks the served route table | US-identity-004 and every story | invalid_credentials (one reason for wrong passcode and unknown email), unauthenticated |
| R-identity-07 | An empty team is seeded with one admin by an operator command outside the API, exactly once | US-identity-005 | team_not_empty |
| R-identity-08 | An action by a role the Permissions table denies is refused with reason forbidden; an id that names nothing is refused with reason not_found; checks apply in the cross-cutting order — enforced by every domain | every story | forbidden, not_found; each story's tests cover them for its own operations |
| R-identity-09 | Any signed-in caller lists the members with id, name, role and active only, ordered by name then id; passcode and token never leave identity | US-identity-001 | the list's fields and order |

## Interfaces this domain needs from others
- scheduling: whether a member holds an assignment on a shift whose start instant is after now, in any week (IR-05)
- notifications: emit member_added / role_changed / member_deactivated (IR-10)
