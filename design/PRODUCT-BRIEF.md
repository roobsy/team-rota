# PRODUCT-BRIEF — Team Rota
v1.0 · approved by the operator on 2026-11-07 · content-pinned (`PINS.lock`), recorded as D-01. A change here is a change of purpose: the operator's explicit decision, recorded as a new version, never an editorial patch.

## 1. Purpose
Team Rota is a shift roster for one small team. A planner publishes the week's shifts, members see who holds what, and a member who cannot make a shift hands it to a willing counterpart through a swap that the planner approves. It replaces a spreadsheet and a group chat with one place where the week, the swaps and their reasons are visible to everyone concerned.

## 2. Who it is for
- **Planner** — builds and publishes the week; wants a fair, complete roster without chasing people. Pain today: the spreadsheet is always one message behind the chat.
- **Member** — works the shifts; wants to see the week early and hand over a shift without a phone tree. Pain today: a swap arranged in chat is forgotten by the roster.
- **Admin** — keeps the team's membership and roles right; wants nobody to approve their own swap. Pain today: no record of who agreed to what.

## 3. North Star
**The roster tells each person the truth about their week — who holds every shift, what is still pending, and why a request was refused — plainly, even when the truth is unwelcome.** Clarity over reassurance: a refused swap shows its reason; an unapproved swap never looks approved.

## 4. What it must never become
- A scheduling optimiser that assigns people to shifts for the planner; the planner decides, the product records and shows.
- A chat: no free-text threads, no reactions; a swap carries a reason code, not a conversation.
- A silent system: no state changes without a notification to the people affected, and no notification that overstates (a "pending" is never shown as "done").
- A multi-team or multi-tenant product in this version.

## 5. Non-goals (this version)
Time tracking and pay; recurring templates; mobile apps (the web UI must work on a phone's browser, nothing more); integrations with calendars or messengers; more than one team.

## 6. What would count as success
Before any unit exists: a planner can publish a week of shifts; every member can see it the same minute; a member can request a swap, a counterpart accept it, the planner approve or refuse it with a reason, and the roster and the notifications reflect each step — end to end, in the browser, with no step hidden. The one number: a swap's full path (request → accept → approve) completes with every party notified and the board correct, in a test that runs on every commit.

## 7. Open purpose questions
None at approval. (Whether a planner may approve a swap in which they are the counterpart is a rule of the swaps domain — segregation of duties — not a purpose question; it is decided in the design.)
