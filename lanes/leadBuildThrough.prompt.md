# Lane leadBuildThrough (Sol 6.2 medium), Lead only: TRIAL, off by default — build the whole accepted scope through, prove at check-ins and the end
Repo: this lane dir is main c4cf3fd plus the gated leadHonestLimits. Binding: CHARTER-LEAD.md and BLUEPRINT-LEAD.md v0.5. This trial is OFF by default (SELDON_ON=leadBuildThrough), because a default change needs Oren's word.
Evidence (blind walk C:/seldon/tests/m2walk-0/REPORT.md, M2 Spoke & Sprocket, 24 workflows; works/partly/broken/missing):
- Seldon Lead: ~5 milestones, 63 calls (WORK 28, JUDGE 21), stopped before the end. Result 7/5/1/11, maintainability 5/10. It never reached stock, finance, import, audit or reports.
- Plain Codex told to "continue" each turn (13 turns, 76 min): 20/4/0/0, maintainability 7/10.
- Inferred: proving every milestone (a guard walk plus repairs) consumed the run.
Design (lead, Claude). Keep everything that works: planning (ALIGN asks real questions, REVIEW, B), the thin owner-first brief, keepBuilding continuations, resume after a kill, and the owner-words plausible guard.
Change only the rhythm, behind the switch:
- After B, one builder session builds the WHOLE accepted scope, milestone by milestone in order. Seldon says "continue with the next milestone: <its promises>" at each return. Each milestone still has its spec and B lines, and the builder keeps its regression checks green as it goes. Seldon may run the builder's checks between milestones: cheap, deterministic.
- The guard walks only (a) at an owner check-in the person asked for, and (b) once at the end, over all promises (cumulative), with one complete walk, one repair list and one scoped re-walk, as leadGuardOnce does today.
- Milestone records and receipts stay, so memory, resume and hand-off are unchanged.
Tests: golden/journey only. Add one journey: a 3-milestone dream under the switch, with one builder session, no guard between milestones, one final walk, and C. The default path must be unchanged (existing journeys pass). Run the journeys you touch plus cold imports. Do not run gate.sh or cohorts.
Report C:/seldon/tests/leadBuildThrough-0/REPORT.md, max 10 lines: what changed (file:line), net src, and the exact command for one M2 run with SELDON_ON=leadBuildThrough. Leave the diff, do not push. Temp files only under C:/seldon/tests/leadBuildThrough-0. Never open desktop windows. Never read C:/seldon/sealed/.
