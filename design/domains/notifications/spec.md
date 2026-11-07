# notifications — domain spec
v1.0 · owned by pm-lead. The business rules of this domain, each testable, each naming the story it serves.

## Rules
| Rule | Statement | Serves | Testable as |
|---|---|---|---|
| R-notifications-01 | Every state change notifies exactly the people affected, once | US-notifications-001..004 | one notification per recipient per event |
| R-notifications-02 | A notification never overstates: it names the state as it is | US-notifications-003, US-notifications-004 | the text carries the state and the reason |
| R-notifications-03 | Inactive members receive nothing | US-notifications-001 | none for inactive |

## Interfaces this domain needs from others
- identity: the active members and the planners (row 4).
