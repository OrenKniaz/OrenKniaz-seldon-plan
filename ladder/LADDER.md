# Blocker-clearance ladder (Oren 11-04, binding)

Seldon climbs one level at a time. **Never run the next level until the current one is clean.**
Every blocker gets a triage call (`TRIAGE: BUG|DESIGN — why — sibling cases`) before its fix lane; DESIGN = one shared rule at one owner, never a patch (FAST-LANE-RULES.md).

| Level | What | Briefs | Target wall/run | Exit (clean) |
|---|---|---|---|---|
| L0 Ultra | one-file CLI, trivial behavior | 5 new: hello ("hello world, I'm Seldon"), greet NAME, shout (stdin upper-case), add A B, countdown N | ≤ 6 min | 2 consecutive cohorts, 5/5 verified each |
| L1 Fast | small CLI tools with edge cases | the 14 existing farm CLI briefs | ≤ 12 min | 12 consecutive verified runs |
| L2 Medium | small web / HTTP | the 6 existing farm web briefs + 2 new stdlib JSON HTTP APIs (notes API with file store; counter API with concurrent increments) | ≤ 20 min | 12 consecutive verified runs |
| L3 Large | full-stack: server + storage + UI + importer | ShelfLife (fight-1 brief) + 2 new (kanban: SQLite + UI + CSV export; booking: slots API + UI + conflict rule) | ≤ 40 min | 3/3 verified, and ShelfLife oracle ≥ plain Codex (36/40) |

**Clean** = every run in the window is ACCEPTED-VERIFIED or DELIVERED-VERIFIED by verify.py / the oracle. Codex usage-limit errors are reruns, not results.

**Loop**
1. `farm.py ladder` runs cohorts at the current level on the installed Seldon SHA.
2. On the first non-clean run it stops that level, writes `ladder/BLOCKERS.md` (run id, level, refusal code, last planner message, receipts path) and keeps re-running only the remaining briefs of that level (no promotion).
3. CC triages each blocker into BUG or DESIGN. Independent clusters get parallel fast lanes (separate files only); same-shape clusters go to one DESIGN lane.
4. After publish the loop reinstalls the new SHA and **restarts the level's clean window from zero**.
5. Exit met → `ladder/STATE.json` promotes to the next level; CC tells Oren.
6. A fix that regresses a lower level (golden gate or an L(n-1) spot run) is rejected.

**Lane 2 — Astra design review (continuous):** gpt-6-astra, read-only, design-only. It walks the code along the user journey and lists design faults that will block runs we haven't seen yet. Findings go to `ladder/design-review/` and feed the DESIGN lanes. First one: ASTRA-DESIGN-1.
