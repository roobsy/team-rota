# INTERFACE-REQUESTS — Team Rota
Cross-domain needs, raised by a domain's PM as a row and resolved by the pm-lead with the architect into `design/INTERFACES.md` or the contract. Sub-PMs never negotiate with each other in chat; this table is the conversation.

| ID | From | To | Need | Story | Status |
|---|---|---|---|---|---|
| IR-01 | swaps | scheduling | read an assignment's holder and its shift's start instant (for the deadline) | US-swaps-001 | open |
| IR-02 | swaps | scheduling | transfer an assignment to the counterpart, refused with counterpart_overlap or counterpart_inactive | US-swaps-003 | open |
| IR-03 | swaps | notifications | emit request / answer / outcome events through a Notifier | US-notifications-002, US-notifications-003, US-notifications-004 | open |
| IR-04 | notifications | identity | list active members, the admins and planners, and member names | US-notifications-001, US-notifications-003 | open |
| IR-05 | identity | scheduling | whether a member holds an assignment in a published week after the clock's today | US-identity-003 | open |
| IR-06 | scheduling | identity | whether a member is active, and their role | US-scheduling-002, US-scheduling-004 | open |
| IR-07 | scheduling | swaps | the open requests (requested, accepted) per shift of a week, for the badge | US-scheduling-004 | open |
| IR-08 | scheduling | notifications | emit the week-published event through the Notifier | US-notifications-001 | open |
| IR-09 | swaps | identity | whether the counterpart is active; member names for notification text | US-swaps-001, US-notifications-002 | open |
| IR-10 | identity | notifications | emit member added / role changed / deactivated events through the Notifier | US-notifications-006 | open |
