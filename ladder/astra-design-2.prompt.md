ASTRA-DESIGN-2 — read-only. Seldon main (this folder). Do not edit, do not run tests. Your previous review (D1-D9) is at C:/Users/oren/codex-harness/work/ladder/design-review/astra-design-1.md — read it first.
Owner's CORE (Oren, 11-04, verbatim intent) — this is the spec Seldon must be:
- everything runs in a loop
- everything that can be structured with tools/functions/classes for determinism is
- everything that can be a tool/function rather than LLM reasoning is
- the LLM creates and judges semantics determinism can't
- we help users improve their "dream", break it down and get their acceptance
- we work like a high-quality SW team (e.g. A-SPICE): dream -> features -> user stories -> requirements -> tests, all connected so the WHY is preserved (traceability)
- more LLM reviewers make outcomes more deterministic
- beads allow concurrent implementation (slow high-end planning, fast execution)
- we validate/force validation that the actual dream is built in the end — not stubs, not missing features
- the planner reviews progress and helps steer
- waves for large tasks: after wave 1, resync on vision and plan beads for wave 2
CC's boundary rule from today's blockers: deterministic code owns STRUCTURE (trace graph links/coverage, phases, beads/waves scheduling, budgets, running things, observed RED/GREEN, receipts); the LLM owns SEMANTICS (is this test meaningful, does this scenario express the requirement, is this the dream, is this a stub). When deterministic code cannot decide a semantic question it routes it to an LLM judge with a recorded verdict — it never refuses and never pattern-matches semantics.
Task: map the current code onto the core. For each core piece: which modules implement it today, approx lines, and verdict KEEP (sound) / RESHAPE (right job, wrong boundary — e.g. determinism doing semantics) / DELETE (overreach not in the core) / MISSING (core piece absent or weak — e.g. waves, real-dream validation, trace graph). Then: (1) the minimal core — module list + rough line budget vs today; (2) what is deletable and its size; (3) where the boundary rule is violated (determinism judging semantics, closed vocabularies, refusals instead of LLM-judge routing), with file:function; (4) whether D1-D9 lanes A/B/C as you proposed still fit or should change; (5) a sequenced reset plan of lane-sized steps (disjoint files per parallel step, each net-deleting, each provable on a ladder level L0 hello-CLI -> L1 small CLI -> L2 web/HTTP -> L3 full-stack). Be concrete and skeptical; say where unsure. Final message only, <=80 lines.
