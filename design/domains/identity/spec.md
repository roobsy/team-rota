# identity — domain spec
v1.0 · owned by pm-lead. The business rules of this domain, each testable, each naming the story it serves.

## Rules
| Rule | Statement | Serves | Testable as |
|---|---|---|---|
| R-identity-01 | One role per member; roles are admin, planner, member | US-identity-001 | the role field accepts exactly the three names |
| R-identity-02 | An email is unique on the team | US-identity-001 | duplicate_email refusal |
| R-identity-03 | The team always keeps at least one admin | US-identity-002 | last_admin refusal |
| R-identity-04 | An inactive member keeps history and cannot be assigned | US-identity-003 | member_inactive refusal |
| R-identity-05 | A member with assignments in a published future week cannot be deactivated | US-identity-003 | future_assignments refusal |

## Interfaces this domain needs from others
