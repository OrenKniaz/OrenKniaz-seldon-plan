# Fable consult 2026-11-13: dream literals lost after ALIGN (T-130)

TRIAGE: DESIGN. The vision is a lossy LLM rewrite, yet it is the only carrier of the user's words past ALIGN.

RULE: the user's words are the root agreed text. The vision adds to them and never replaces them, so every planning and plan-review question carries them verbatim, and a value they leave open is a recorded decision shown at B, never a missing fact.

(1) Both, verbatim as the guarantee: a "User's words" fact on ARCHITECT, ARCH-REVIEW, DETAIL and REVIEW (today only ALIGN gets it, run.py:129; everything after reads the vision). ALIGN carries literals best effort (prompt line). WORK and JUDGE do NOT get the words; DETAIL/ARCHITECT copy literals into requirement and contract text, REVIEW (which sees the words) flags drops. R2: existing 64 KB bounded_unit covers it; per-area excerpts only when a real dream needs it. T-119: the user's words are the first agreed-text source.

(2) neededFacts never ends a run; no re-ask machinery. With the words in the brief, anything still missing is something nobody said = a decision. ARCHITECT records it in `decisions` (already in schema and shown at B). DETAIL: cross-area value -> existing contract_gap; local value is its own. User questions already have ALIGN `unknowns` shown at A. Remove the `uncertain` answer shape from ALIGN/ARCHITECT/DETAIL.

(3) Changes:
- questions.py new user_words(store): the "Dream" and "Requested change" facts of the question behind cursor.vision (answer -> attempt -> question); no new record kind.
- questions.architect_brief(words): add "User's words"; caller run.py step ~148.
- questions.detail_brief: add "User's words": user_words(store).
- plan_review.py ~33 and ~44: same fact beside "Approved vision".
- AGREED_LITERALS: add "The user's words are agreed text; an exact value they state appears verbatim in the commitment, contract or requirement that owns it."
- PROMPTS["ALIGN"]: add "Keep every exact value the user stated verbatim in the scopeIn item it belongs to; improving never paraphrases an exact value."
- PROMPTS["ARCHITECT"]: add "Copy exact values from the user's words into contract text or the owning commitment; a value they leave open is yours to choose — record it in decisions."
- schema.answer_schema (~124-126): `uncertain` only for judge and review kinds; ALIGN and ARCHITECT get (payload,); DETAIL gets (payload, DETAIL_SPLIT, DETAIL_GAP).
Delete: `uncertain` for ALIGN/ARCHITECT/DETAIL; narrow inference.py:82-83 to kinds that can still answer uncertain (keep MissingFacts class: units.py catches it for WORK/JUDGE). No dream-specific handling anywhere.

Journey twin (test_journey.py or test_architect.py): dream contains `GET /api/items -> 200`, a CSV header line, and "imported N, skipped M"; stub ALIGN returns a condensed vision; stub ARCHITECT/DETAIL build contract/requirement text ONLY from literals found in the question's facts (so the test fails if the words are not passed). Assert outcome: run reaches B and the B plan's contract or requirement text contains the three literals. Fault twin: stub ARCHITECT answers `uncertain` -> rejected as invalid, ordinary re-ask, reaches B with a decisions entry; no MissingFacts, no INCOMPLETE.

Siblings: ARCH-REVIEW/REVIEW judged scope from the condensed vision only; ALIGN on a second revise loses the first revise's words (user_words should eventually return all revise words of the run); B-revise words same path.
