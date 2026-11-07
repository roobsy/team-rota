# identity — domain spec
v1.1 · owned by pm-lead. The business rules of this domain, each testable, each naming the story it serves. v1.1 applies the dispositions of DESIGN-REVIEW-1.

## Rules
| Rule | Statement | Serves | Testable as |
|---|---|---|---|
| R-identity-01 | One role per member; roles are admin, planner, member; any other name is refused | US-identity-001, US-identity-002 | invalid_role |
| R-identity-02 | An email is unique on the team | US-identity-001 | duplicate_email |
| R-identity-03 | The team always keeps at least one active admin | US-identity-002, US-identity-003 | last_admin on role change and on deactivation |
| R-identity-04 | An inactive member keeps history (stays listed with active false; assignments and requests remain), cannot sign in and cannot be assigned | US-identity-003, US-identity-004 | member_inactive at sign-in; scheduling enforces member_inactive at assignment (R-scheduling-02) |
| R-identity-05 | A member who holds an assignment in a published week whose start_date is after the clock's today cannot be deactivated | US-identity-003 | future_assignments (reads scheduling, IR-05) |
| R-identity-06 | Sign-in is email plus passcode (stored hashed); it issues the bearer token every other operation carries; the caller is the member the token identifies; no token means unauthenticated | US-identity-004 | invalid_credentials (one reason for wrong passcode and unknown email), unauthenticated |
| R-identity-07 | An empty team is seeded with one admin by an operator command outside the API, exactly once | US-identity-005 | team_not_empty |
| R-identity-08 | An action by a role the Permissions table denies is refused with reason forbidden (the cross-cutting rule, enforced by every domain) | US-identity-001..003, US-scheduling-001..003, US-swaps-003, US-swaps-005 | forbidden |

## Interfaces this domain needs from others
- scheduling: whether a member holds an assignment in a published future week (IR-05)
- notifications: emit member added / role changed / deactivated events (IR-10)
