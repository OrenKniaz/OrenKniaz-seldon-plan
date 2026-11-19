Read-only design question: no edits, no tests, no provider launches. Read CHARTER.md (v1.3, especially C6, C8, C10, C15, C16, I1, I2), C:/Users/oren/codex-harness/work/ladder/CLEAN-CORE-DECISION.md and C:/Users/oren/codex-harness/work/ladder/design-review/clean-core-scaling-audit.md.

Situation: the dream was "a tiny web page with one Play button; when I click Play the page shows Hello, world!; a single static HTML file; no server, accounts or dependencies". A worker, asked for craft, added an unrequested headline: "Good things start here." and a small label. The accepted scope-out said roughly "additional controls, pages or features".

The delivery lead flagged this as a line taste has to draw between craft and adding content. The owner disagrees and asked for an independent view, explicitly not to take his word for it. His position: a small unrequested improvement that serves the goal and does not touch a declared non-goal should be accepted; otherwise we will always fail on tiny shifts that are impossible to judge, and on big apps scope is harder still; this is an LLM, not code, so it needs leeway.

Give your honest judgment. You may disagree with either of them. Answer in at most 40 lines:
1. What is the right rule for unrequested additions, stated in one or two sentences? Who owns it (CODE, LLM, user)?
2. Where exactly is the line between acceptable leeway and scope creep? Apply your rule to: the headline; a screen-reader announcement promise; a settings page; an analytics snippet; a new dependency; a changed user-facing word in a required string.
3. Does this hold at a thousand times the size? What is the failure mode if leeway is too wide, and if too narrow?
4. How should a user see additions at C, if at all, so trust is kept without creating a gate?
5. What, specifically, should change in Seldon, smallest form, and what should not be built.
Decide; do not list options.
