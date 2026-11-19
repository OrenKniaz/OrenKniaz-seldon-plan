Design task, read-only: no edits, no tests. Output one design document. Read in this order: CHARTER.md (v1.3; note I9, C20, I1, I2, I7, I10, and the core-idea reference to GenAI-Final-Project's run_turn loop); ~/codex-harness/work/ladder/CLEAN-CORE-DECISION.md; ~/codex-harness/work/ladder/design-review/what-the-code-does.md; ~/codex-harness/work/ladder/design-review/should-it-exist-audit.md; ~/codex-harness/work/fight-1/r27-diagnosis.md through r33-diagnosis.md.

The owner decided to stop patching the 32k-line core and build charter v1.3 as a clean, Omarchy-style new core: opinionated, one way to do each thing, in Python, stdlib plus the approved MCP SDK, one plain pip install.

Design it so that a real LLM can take "a page with a Play button that shows Hello, world!" from dream to approved C, then ShelfLife, with the rest of the charter added afterward on the same shape.

The document must contain:
1. THE LOOP in one page: one state machine, its states, and for each state: the question asked, its strict schema, what CODE validates, what is saved, and the next state, including what happens on refusal, on an inconclusive judge, and on provider failure. Every path has a next step; no holds.
2. MODULE LIST for milestone 1: each module, its single job, charter clause, target lines. Prefer about ten modules. State the honest line total for milestone 1 and for the full charter, and say where you disagree with the inventory's 19-22k and why.
3. DATA: the minimum store and record kinds. One canonical plan. How approvals and reviews bind to its meaning. How a question gets bounded facts.
4. REPAIR as one mechanism before and after B: typed edits, with CODE binding provenance.
5. TESTS FIRST and verification for products with no server, with a browser, and with no browser available, keeping C14 honest: failing because the product is missing is the right RED; say exactly what a labelled "couldn't verify" means at C.
6. STUB TESTING: how the whole loop runs offline from A to C in about a minute with scripted LLM replies per state, and how recorded real answers from actual runs replay as regression. This is the main test.
7. REUSE: exact list of old files or functions worth lifting, each with why. Default is rewrite. Reuse must be cheaper than rewriting and must not import old concepts.
8. BUILD ORDER: milestones small enough to verify, starting with a stubbed A-to-C on day one. Where the new code lives in this repo, how the old core gets removed, and when.
9. WHAT THE CHARTER REQUIRES LATER (waves, research, brownfield, recovery, and so on) and the one extension point for each, so none forces a redesign.
10. The three biggest risks of this plan and how we would see them early.

Be concrete and short: at most about 400 lines. Decide; do not list options. Name anything that needs the owner.
