# INTERFACE-REQUESTS — Team Rota
Cross-domain needs, raised by a domain's PM as a row and resolved by the pm-lead with the architect into `design/INTERFACES.md` or the contract. Sub-PMs never negotiate with each other in chat; this table is the conversation.

The service graph has cycles (identity ↔ scheduling: IR-05/IR-06; scheduling ↔ swaps: IR-01, IR-02 / IR-07; identity ↔ notifications: IR-10 / IR-04). They are accepted explicitly: every cross-domain call goes through a protocol whose Null implementation the contract unit creates, and the plan names the build and retire order (INTERFACES.md, "Build order").

| ID | From | To | Need | Story | Status |
|---|---|---|---|---|---|
| IR-01 | swaps | scheduling | read an assignment: its holder, its shift (id, date, start instant, end, current holder ids) and its week's state | US-swaps-001, US-swaps-002, US-swaps-003, US-swaps-004, US-swaps-005 | open |
| IR-02 | swaps | scheduling | transfer an assignment to the counterpart inside the caller's transaction (commits nothing itself), refused with counterpart_overlap (a slot on the same shift counts) or counterpart_inactive | US-swaps-003 | open |
| IR-03 | swaps | notifications | emit swap_requested / swap_accepted / swap_declined / swap_approved / swap_refused with self-contained payloads, written in the same transaction | US-notifications-002, US-notifications-003, US-notifications-004 | open |
| IR-04 | notifications | identity | whether a recipient is active | US-notifications-001, US-notifications-006 | open |
| IR-05 | identity | scheduling | whether a member holds an assignment on a shift whose start instant is after now, in any week | US-identity-003 | open |
| IR-06 | scheduling | identity | whether a member is active, and their name (for holder-rows) | US-scheduling-002, US-scheduling-004 | open |
| IR-07 | scheduling | swaps | scheduling passes the caller's member_id and, per assignment, {assignment_id, holder_id, start_instant, week_state}; swaps returns per assignment {pending: requested, accepted or none; requestable: holder_id == caller and week_state == published and no open request and now < start_instant − 24 h}; no re-entrant read | US-scheduling-004 | open |
| IR-08 | scheduling | notifications | emit week_published with the recipients, written in the same transaction | US-notifications-001 | open |
| IR-09 | swaps | identity | whether the counterpart is active; the eligible deciders (active admins and planners); member names for payloads and for the request row | US-swaps-001, US-swaps-002, US-swaps-003, US-swaps-004, US-swaps-005, US-notifications-002, US-notifications-003 | open |
| IR-10 | identity | notifications | emit member_added / role_changed / member_deactivated, written in the same transaction | US-notifications-006 | open |
| IR-11 | the API layer (every domain) | identity | resolve a bearer token to the caller {member_id, name, role, active}; unknown or inactive refused unauthenticated; resolved once per request | US-identity-004 and every story | open |
| IR-12 | scheduling | identity | the ids of every active Member of any role, for week_published's recipients | US-notifications-001 | open |
