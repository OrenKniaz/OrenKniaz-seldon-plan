# Fable bird's-eye 2026-11-13 (cohort #4 on 050f3e8, read-only)

Two rules cover all six failures; three evidence notes were misdiagnosed.

Store findings:
- Every area writes its own "integrated" check listing other areas' requirements. plan.assigned() infers level from requirement subset; plan.traced_units() infers gap owners from requirement intersection. Both guesses wrong by construction.
- x04: n011 (--integrated) lists only its own requirement, so assigned() made it LOCAL; unprovable in an isolated checkout.
- x01: gap n010 assigned to u001 AND u002; u001 had spent 2 recoveries on unit JUDGE gaps, so fixups.apply -> units.recover exhausted it instantly. u002 (real owner) was fine.
- x09: one failing wave check reopened ALL FOUR units; u001 fixed it, then failed proof because checks_for flipped its check to preserves (must pass on defective base). u002 prose target hit safe_path in handoff.
- x03/x06: a race, not debris. wave_verify runs checks in parallel threads in ONE checkout; each proof.observe ends with gitwork.unchanged and sees a sibling's transient .fixture- dir.
- x07: not unit size. Worker saved PNG/JSON evidence under checks/foundation/evidence/ (122 KB); judge_brief decodes check blobs (binaries not skipped); UnitTooLarge terminal with 0 recoveries.

RULE 1 (ownership by location, declared level): a check has a declared level (unit|wave; BLUEPRINT 3.1, missing from schema.py), exactly one owner (the unit whose checkPaths hold its file), and runs only where its inputs exist. Wave-level is proven/repaired only by its file owner, on the integrated candidate.
RULE 2 (hermetic, source-only): every check run gets its own disposable checkout of the exact commit, reset and cleaned by code; tree and briefs carry text source only; code never refuses on what a check or worker left behind.
Supporting (R12, normalise-not-refuse): structured EXECUTE fields the LLM fills are code-supplied enums.

Per failure: x04 R1; x01 R1 (single owner; fixup = fresh recovery budget); x09 R1 + enum target; x03/x06 R2; x07 R2 (size measured by code at PROVING/JUDGING, retryable). Cohort 3: z04/z05 T-118; z06 mostly R1.
Code owns: owner from path, where each level runs, checkout lifecycle, owner enum, size measure, normalising a check spanning two units to wave. LLM: level, check content, own vs named-owner defect.
Delete: assigned() subset inference; requirement-intersection branch of traced_units for ownership; checks_for mode flip; gitwork.unchanged after observe + disposable flag (keep as publication guard); safe_path lookup in handoff; retryable=False for UnitTooLarge.
T-118 keep, simplify to owner enum. T-119 keep the sentence, no code on it.
Lanes: A plan.py, schema.py, architecture.py, questions.py (level, assigned by level, plan.owner(check), enum target, judge_brief text-only). B proof.py, wave_verify.py, gitwork.py (worktree per observer, clean, gap owners = plan.owner). C fixups.py, units.py, flow_review.py (single owner, fixup resets recoveries, no mode flip, integrate reruns gap wave check, enum handoff, size retryable). Agree plan.owner signature first.
Risks: page unit draws unit-JUDGE gaps in 4/5 failed runs (judge strictness on largest unit); wave checks written blind on first pass (~one fixup round per run).
