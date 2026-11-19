LANE judge-level (ticket T-81). Worktree C:/Users/oren/codex-harness/work/lanes/judge-level-20261112 (Seldon main fb74470). Temp only under C:/seldon/tests/level-<n>. Do not commit. No new dependencies. Do not edit CHARTER.md or BLUEPRINT.md. Behaviour-only journeys. No real provider calls.

Read CHARTER.md (I2, I10, C14), BLUEPRINT.md (R2, R9, R11, R12), then src/seldon and tests/seldon.

FAILURE (real runs C:/seldon/tests/m1/foundation-fb74470-c01 and foundation-230667c-c02, both reached C but with plan repairs): REVIEW overturned the planner's `judgment: false` on a quality criterion in 2 of 2 runs (REPAIR + second REVIEW). In c01 REVIEW also asked for a "source review" the plan cannot express, so REPAIR wrote a cross-unit property ("each script touches only its own button") into n006, whose unit owns only tests/integration.cjs; its unit JUDGE then asked for sibling files. Calls: c01 call-b381e1c* (REVIEW), call-d675e2f* (REPAIR), call-4fc32a6* (JUDGE n006).

TRIAGE DESIGN. ONE RULE (decided by the lead; if a point is wrong, stop and say where): a property is judged at the level whose scope owns every file it speaks about; code supplies those files by trace; the plan never declares an evidence kind.
1. Delete the `judgment` flag (schema, plan.create, PLAN/REVIEW prompt clauses, the `code_quality` branch in judgment.step). Every quality criterion gets one PRODUCT question; code still records a gap without a call when a traced check failed.
2. Give PLAN and REVIEW one labelled fact (a facts section, not a prompt sentence) stating what each judge is handed: unit JUDGE = its own requirements, its checks, its T..P diff, outputs, screenshots; DEMO = one requirement with its traced checks, observations and the files of the units owning it; PRODUCT = one criterion with the same for the checks it traces to.
3. Code check at plan validation (and REVIEW sees it as a fact): for each criterion and requirement, the set of units reached by its trace; REVIEW judges whether that reaches every unit whose files the property speaks about, and a miss is a gap on the trace, not a request for a review step.
4. A unit JUDGE never gets sibling or whole-product files.
DO NOT: add a sourceReview or evidence-kind field; add source-reading tests; widen unit JUDGE; keep the flag with a smarter prompt or keyword guess; patch prompt text for this answer.
LEAD DECISIONS THAT MUST SURVIVE: timing asserts `scale_seconds < 90` and `seconds < 270` (T-77); owner constants ALIGN_DESIGN, CRAFT, JUDGMENT_LEEWAY word for word; one subject per judge question; DEMO-FACTS/PRODUCT-FACTS; one copy of each file per question (T-79) and the recorded-judgment size journey.

JOURNEYS (outcome only): a plan whose criterion trace misses the units it names gets a REVIEW gap on the trace, repaired, then C; every criterion is asked once at PRODUCT; 1-vs-50-unit size bound still holds. Suite under 3 minutes.

DELIVER in C:/Users/oren/codex-harness/work/lanes: judge-level.patch (git diff --binary vs base, with new files; use git add -N for untracked), judge-level-report.md at most 10 lines: lines before/after per changed module (aim net negative); what was removed; journeys and seconds; largest question bytes per kind at 1 and 50 units; anything in the rule you found wrong.
