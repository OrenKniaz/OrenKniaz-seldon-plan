# Lane leadLeanBuilder (Sol 6.2 medium), Lead only: let the planned builder be fast
Repo: this lane dir is main 441c0d2 plus leadPlanOne (gate pending). Binding: CHARTER-LEAD.md, BLUEPRINT-LEAD.md v0.5 (witness carry: the guard's walk is the witness when it observed the promise).
Oren 11-22: "I would think our builder needs less thinking (plan ready) so he would be fast." Data:
- ShelfLife Lead WORK is ~232 s, equal to plain's whole run (233 s).
- In Lead first builds, 33 of 49 shell calls touched check/guide/lifecycle paths; plain had 0 of 31 (C:/seldon/tests/leadJudgeTokens-0/REPORT2.md).
- So the plan likely does save thinking, but we spend the saving, and more, on proof artifacts the guard then re-walks anyway (C:/seldon/tests/timeWhy-0/REPORT.md).
Lead's design (Claude), as a TRIAL behind switch leadLeanBuilder (default ON in the lane, SELDON_OFF=leadLeanBuilder restores today):
- For a single-milestone (micro) dream, the builder delivers the product plus a short human try-it guide: what to run, what you should see. The guide stays a deliverable for the person.
- It writes no lifecycle log, no browser walkthrough script, and no per-promise check files, unless B explicitly promises a test suite to the person.
- The builder may still run whatever it likes to check its own work. It just doesn't have to retain it as Seldon evidence.
- Seldon's guard walks every B promise itself, starting from the try-it guide (v0.4 walk). Its recorded walk is the retained witness (v0.5).
- Multi-milestone dreams: unchanged for now. Retained builder witnesses matter for regression there, and the guard's recorded walk replay is a later step.
- Remove the receipt fields and validation that only exist for the dropped artifacts on the micro path. Net src lines should go down.
Coordination: the guard/prove logic belongs to another session. You may change what the builder is asked for and what the receipt must contain on the micro path. If the guard needs a different input, change only its input facts (which files or paths it's handed), not its judging logic. Say exactly what you touched there.
Tests: golden/journey only; no gate, no cohorts. Run the journeys you touch plus cold imports. Add one journey: a micro run in which the builder returns no checks, the guard walks, and C is verified.
Report C:/seldon/tests/leadLeanBuilder-0/REPORT.md, max 12 lines: net src, files touched, what the builder brief and receipt drop, and the exact cohort command for ShelfLife ×5. Leave the diff; do not push. Temp files only under C:/seldon/tests/leadLeanBuilder-0. Never open desktop windows. Never read C:/seldon/sealed/.
