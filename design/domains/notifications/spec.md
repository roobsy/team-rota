# notifications — domain spec
v1.1 · owned by pm-lead. The business rules of this domain, each testable, each naming the story it serves. v1.1 applies the dispositions of DESIGN-REVIEW-1.

## Rules
| Rule | Statement | Serves | Testable as |
|---|---|---|---|
| R-notifications-01 | These events notify exactly the people affected, once each: week published (every active member); swap requested (the counterpart); swap answered (on accept the requester and every eligible decider, on decline the requester); swap decided (both members); member added, role changed, deactivated (that member). No other event notifies; expiry is derived and never notifies | US-notifications-001..006 | one notification per recipient per event; none for any other event |
| R-notifications-02 | A notification never overstates: it names the state as it is and the reason when refused | US-notifications-003, US-notifications-004 | the text carries the state and the reason |
| R-notifications-03 | Inactive members receive nothing | US-notifications-001 | none for inactive |
| R-notifications-04 | A member reads only their own notifications, newest first by created_at, and marks only their own read | US-notifications-005 | not_recipient; the order; the empty state |

## Interfaces this domain needs from others
- identity: the active members, the admins and planners, and member names (IR-04)
