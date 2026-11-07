# OPEN-QUESTIONS — Team Rota
Not a to-do list. A `Q-nn` is a conflict, gap or ambiguity between the documents and what a session must do; it is raised by the session that meets it and ruled by the operator, usually through the design-change loop (`/adu-lifecycle:change-design`). Product behaviour belongs in FEEDBACK.md instead. Ids come from `adu next-id Q`; a question raised off this tree (in a pack or a verification report) is numbered provisionally (`Q-p<n>`) until the apply step allocates it; a provisional id never enters this file.

Entry format:
```
### Q-nn · YYYY-MM-DD · ADU-nn (or the phase) · open | resolved → vX.Y | resolved → D-nn | withdrawn
**Conflict:** what disagrees with what, quoted with file and line.
**Blocking:** yes | no — a blocking question stops the unit; a non-blocking one lets it proceed with the assumption stated in the journal.
**Options:** two or three, each with its consequence; the raiser recommends one.
**Resolution:** the ruling, who made it, the date, and the document it now lives in.
```
