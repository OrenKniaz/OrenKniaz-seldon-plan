# Lane leadHumanGuide (Sol 6.2 medium), Lead only: the proof process must not become a second product
Repo: this lane dir = main d822514. Binding: CHARTER-LEAD.md, BLUEPRINT-LEAD.md v0.5. Read the Astra macro review first: ~/codex-harness/work/ladder/design-review/astra62-macro-2026-11-23.md, the section "The proof process became a second product".
Facts:
- ShelfLife asked for a short README. Lead's delivered try-it guide opens with Node, a browser kit and an evidence directory before telling a householder how to start the pantry. Example: C:/seldon/tests/m1/shelf-raceCtl-620d540-rc01/product/docs/try-it.md.
- 4 of 5 morning repairs touched only guide or check files.
- An earlier "lean builder" trial failed only because B still demanded a runnable guide check and a lifecycle log while WORK said to skip them. Both builders named that conflict and replanned: C:/seldon/tests/m1/shelf-raceLean-b80c799-rl01/calls/call-659061d6cc1c4d66a5fd77532419f88f/question.json.
Design (lead, Claude):
- The builder delivers the product, real executable regression checks it judges useful (tests a future change could break), and a short human guide: how a person starts and uses the product, in the person's terms.
- No universal machine-readable lifecycle or proof-history requirement, and no evidence dirs or browser kits in the human guide.
- Seldon's guard walks the product itself and records its own walk (v0.4/v0.5). It may run the builder's checks.
- Make B, the plan templates, the WORK brief and the receipt agree. No instruction anywhere may demand an artifact another instruction drops. Find every place that asks for lifecycle logs, guide-walkthrough checks, evidence dirs or kit setup in the guide, and remove the requirement at the source, without adding a rule on top.
- This applies at every size, not only micro.
- If the guard's input currently depends on those artifacts, hand it the guide path and the check paths only. Do not change guard judging logic; another session owns it.
- Switch: SELDON_OFF=leadHumanGuide restores today. Net src should go DOWN: you are deleting a requirement.
Tests: golden/journey only. No gate, no cohorts. Run the journeys you touch plus cold imports. One journey: a run whose B and WORK carry no lifecycle/walkthrough demand reaches verified C from the guard walk plus the builder's regression checks.
Report C:/seldon/tests/leadHumanGuide-0/REPORT.md (max 12 lines): every requirement removed (file:line, quoted), net src, and the ShelfLife ×3 + S1-doorcount ×1 cohort commands. Leave the diff, do not push. Temp files only under C:/seldon/tests/leadHumanGuide-0. Never open desktop windows. Never read C:/seldon/sealed/.
