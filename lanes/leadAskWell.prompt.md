# Lane leadAskWell (Sol 6.2 medium), Lead only: ALIGN shapes the dream with the person
Repo: this lane dir = main d822514. Binding: CHARTER-LEAD.md; BLUEPRINT R17 (planner before user; every user question is options + Other) and R18 (grow-and-align: expand and improve, with multi-question rounds until the person says alignment is done).
Read first: Astra macro review ~/codex-harness/work/ladder/design-review/astra62-macro-2026-11-23.md, "Shape the dream with the person"; and C:/seldon/tests/alignQ-0/REPORT.md.
Fact: on 5 recent Lead runs (S1 doorcount ×4, S2 rehearsalkeys), ALIGN asked the person 0 product questions. The prompt says "Ask together only the choices whose answers materially change the proposed product", and its example shows `questions: []` with `done`. Missed example: Mara asks for "the last four Fridays", which could mean four Friday shifts or every shift between two dates. Both blind walks found exports that included a Wednesday or a Thursday.
Design (lead, Claude), coaching, not rules:
- Coach ALIGN as a thoughtful product partner. Find the few places where a reasonable builder could go two ways and the person would care: ambiguous numbers, time windows, who is allowed to do what, what happens on edge cases the person hinted at, and an improvement they did not think of. Ask those as options + Other. Usually 2-4 in the first round. Zero only when the dream is genuinely unambiguous, and then say why in one line.
- Fix the anchoring: the example must show a realistic first round with real questions, not an empty list.
- Each question carries a recommended option (the planner's best guess), so a person who just accepts gets a sensible product. Nothing blocks on an answer (R17 non-blocking answers).
- Do not add caps or validation. The planner decides.
Prove offline first (replay economy):
- Replay the recorded ALIGN questions old vs new on Terra 6.1 medium via codex exec: S1 doorcount (C:/seldon/tests/m1/s1b-doorcount-cfb3438-s1b01 and lsbb-S1-*), S2 (lsbb-S2-*), ShelfLife (shelf-raceCtl-*), and M1-repairnet if an ALIGN exists. Use one or two samples each.
- Report, per dream, the questions asked, whether they hit real ambiguities (quote them), and the planning tokens/seconds before vs after.
- Then a blind judgement by a second Terra session: "which ALIGN would a product owner rather answer?"
Switch: SELDON_OFF=leadAskWell. Stay in the ALIGN prompt and example (planning region). Another lane, leadHumanGuide, is editing B/plan templates in questions.py, so keep your diff to the ALIGN text.
Tests: journeys you touch, plus cold imports. No gate, no cohorts.
Report C:/seldon/tests/leadAskWell-0/REPORT.md (max 20 lines). Leave the diff, do not push. Temp files only under C:/seldon/tests/leadAskWell-0. Never read C:/seldon/sealed/. Never open desktop windows.
