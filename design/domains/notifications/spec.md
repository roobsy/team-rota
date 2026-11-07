# notifications — domain spec
v1.5 · owned by pm-lead. The business rules of this domain, each testable, each naming the story it serves. v1.3 applied DESIGN-REVIEW-3; v1.4 DESIGN-REVIEW-4; v1.5 applies DESIGN-REVIEW-5.

## Rules
| Rule | Statement | Serves | Testable as |
|---|---|---|---|
| R-notifications-01 | Nine events notify exactly the people the emitting domain names in the payload, once each; the Notifier never reads the event's data back — every payload is self-contained; its one lookup is IR-04 (R-notifications-03): week_published{start_date; recipients: every active Member of any role} · swap_requested{request_id, shift_date, shift_start, requester_name, reason; recipient: the counterpart} · swap_accepted{request_id, shift_date, shift_start, counterpart_name; recipients: the requester and every eligible decider} · swap_declined{request_id, shift_date, shift_start, counterpart_name, reason; recipient: the requester} · swap_approved{request_id, shift_date, shift_start, new_holder_name; recipients: both members} · swap_refused{request_id, shift_date, shift_start, reason; recipients: both members, less any inactive one (R-notifications-03) — with counterpart_inactive only the requester} · member_added{member_id, role} · role_changed{member_id, role} · member_deactivated{member_id}. No other event notifies; expiry is derived and never notifies | US-notifications-001..006 | one notification per recipient per event, its event code one of the nine; none for any other event |
| R-notifications-02 | A notification's text is composed from the payload alone and never overstates: it names the state as it is and the reason when refused | US-notifications-002, US-notifications-003, US-notifications-004 | for each event the payload fields appear in the text |
| R-notifications-03 | Inactive members receive nothing, except member_deactivated, whose recipient is the member being deactivated; the Notifier asks identity whether a recipient is active (IR-04) | US-notifications-001, US-notifications-006 | none for inactive; the one exception |
| R-notifications-04 | A member reads only their own notifications, newest first by created_at then id descending, and marks only their own read; notifications are written in the same transaction as the event that caused them | US-notifications-005 | not_recipient; the order; the empty state |

## Interfaces this domain needs from others
- identity: whether a recipient is active (IR-04)
