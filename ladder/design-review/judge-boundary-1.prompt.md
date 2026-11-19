ASTRA JUDGE-BOUNDARY-1 — read-only audit. Read CHARTER.md (ratified v1.1; C1-C4, I1-I4, I6, I8) first.
Goal (Oren 11-04): every place Seldon decides something must be decided by the RIGHT kind of judge — code or LLM. Find every decision point and classify it.

THE TEST (apply to each decision point):
1. CODE decides when the answer is a function of structure alone: existence, IDs, links/referential integrity, coverage counts, schema validity of a record, ordering/phases, dependencies, file ownership/conflicts, timeouts/leases, revision binding, stale propagation, process exit codes, "test ran / failed / RED->GREEN observed", hashes/receipts.
2. LLM decides when the answer needs meaning: does X satisfy requirement Y, is this test meaningful for that requirement, does the plan cover the whole dream, is this a stub/mock/missing feature, quality/UX vs the Vision Lock bar, dream size, expansion, steering, research conclusions, amendment impact on intent.
3. HYBRID (the usual right answer for gates): code gathers evidence and flags candidates; an LLM judge issues a structured verdict record (C4: typed + rationale); code then enforces structurally that the verdict exists and is bound to the current revision/candidate. Code may BLOCK only on observed structural failure (I4). On meaning, code never blocks or passes by pattern-matching, keyword lists, AST heuristics, closed vocabularies or thresholds; unsure -> pending judgment (I2), never refuse.
4. Anti-pattern in the other direction: an LLM call doing a function's job (counting, linking, scheduling, choosing the next phase, checking a field exists) = WRONG (C2, C1).

Scope: src/codex_harness/core/*.py (semantic-v1 path first; legacy only where still live). Look at every refusal/raise with a code string, every gate/validator/admission check, every predicate feeding acceptance/C, every place an LLM is called (planner, judge, reviewer), and every place the planner LLM is asked to choose something deterministic.

Output (final message only, <=90 lines, open with the CHARTER line):
A. Table of MISALLOCATED points only: file:function | decides what | currently CODE/LLM | should be CODE/LLM/HYBRID | charter rule broken | which reset stage (astra-reset-1/2) fixes it, or NEW.
B. Count of correctly allocated points by category (no list).
C. The 3-5 shared rules/owners that would fix most of table A at once (I9: one rule, not patches), e.g. a single judge-verdict record + one "pending judgment" state.
D. Any decision you could not classify -> say why (that is a question for Oren).
No files changed.
