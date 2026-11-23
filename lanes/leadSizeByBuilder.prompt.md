# Lane leadSizeByBuilder (Sol 6.2 medium), Lead only: split a dream by what one builder session does well
Repo: this lane dir = main 943def4. Binding: CHARTER-LEAD.md, BLUEPRINT-LEAD.md v0.5, BLUEPRINT R19 (size first), CHARTER C8 (check-ins may be waived in the person's words; scope changes always wait).
Evidence, S1-doorcount (~/codex-harness/work/ladder/briefs/S/S1-doorcount.md):
- Plain Codex built the whole brief in one call, 4.1 min, 224 lines.
- Lead split it into 3 milestones: 11 calls, 17 min, 240k tokens (plain 21k). The extra was 4 builds plus 4 guard walks re-proving earlier promises.
- The brief estimated 3-4.5k lines in human-days terms. The real product was about 120-220 lines.
- ShelfLife-size dreams already run as one milestone (leadPlanOne).
Design (lead, Claude):
- The milestone is the unit one builder session can deliver well, not a human-days slice. The planner decides the count in meaning: "how many separate builder sessions does this need, and why?" Reasons that earn an extra milestone: the work genuinely exceeds one session's context or reliability (many seams, large surface, long-running research); the person asked to see and steer an intermediate slice (a check-in they want); or a later part depends on a decision only the earlier slice can inform. "It's a natural first slice" alone is not a reason.
- Default for anything a single session can build: one milestone. The person still sees A and B, and growth (R18) still offers later milestones as next steps after C.
- Keep the multi-milestone machinery for dreams that do need it. Only the default and the planner's guidance change. If the planner returns one milestone, the leadPlanOne micro path (spec in ALIGN, no MILESTONES call) applies.
- Find where the size router or ALIGN decides milestone count today, and change the guidance and the schema field (a short reason per extra milestone). Code normalises: no reason means one milestone.
- Switch: SELDON_OFF=leadSizeByBuilder restores today's sizing.
Coordination: another session owns guard/prove code (lead.py prove paths, judgment.py, proof.py). Stay in planning, size routing and planning prompts.
Tests: golden/journey only, no gate, no cohorts. Add one journey: a multi-feature brief with no check-in request gets one milestone; a brief whose person asks to review a first slice gets two.
Report C:/seldon/tests/leadSizeByBuilder-0/REPORT.md (max 12 lines): what decides the milestone count now (quote the prompt text), net src lines, files touched, and the cohort command for S1-doorcount ×1 plus S2-rehearsalkeys ×1 (DREAM=.../briefs/S/<name>.md). Leave the diff, do not push. Temp files only under C:/seldon/tests/leadSizeByBuilder-0. Never open desktop windows. Never read C:/seldon/sealed/.
