# Lane leadThinBrief (Sol 6.2 medium), Lead only: the builder brief is the product
Repo: this lane dir = main e4802dc. Binding: CHARTER-LEAD.md, BLUEPRINT-LEAD.md v0.5. Memory rule (Oren 11-19, "prompts are the product"): a JSON-first builder brief that lacked the user's words produced worse code than plain.
Evidence, three blind DoorCount walks with the same brief and the same model (Terra 6.1 medium):
- Plain Codex, fed only Mara's brief plus a short constraints paragraph, scored 7/10 on maintainability every time.
- Seldon Lead's builder scored 4.5, 4 and 4/10. Its code mixes routing, validation and SQL in one nested handler; some error paths return HTTP 200; it holds one shared connection.
- It also broke night-identity rules that plain got right: the cross-night retry, and a delayed close shutting the replacement night.
- Reports: C:/seldon/tests/s1walk-0, s1walk2-0, s1walk3-0 (REPORT.md). Key files: s1walk3-key.txt, s1walk2-key.txt.
- Lead's WORK question is ~26 KB; Mara's brief is 2.2 KB. Read one: C:/seldon/tests/m1/door-4f71-6dc9a611-d01/calls/<the WORK call>/question.json and prompt.txt. Plain's whole prompt: C:/seldon/tests/plainBase/run-one.ps1 plus the brief.
Hypothesis to test, not assume: the builder's attention goes to Seldon's machinery (schema, receipt, proof rules, bookkeeping facts) instead of the product, and that costs design quality.
Design (lead, Claude):
- The WORK prompt opens with the owner's own words, verbatim and first, then the approved spec in plain words, then a short "how we work" section. That section, at most ~12 lines, says: build the whole milestone; write the regression checks you would want; keep code readable for the next developer; return when done.
- The receipt schema and example go at the end, as small as possible.
- Move every fact the builder does not need to act on out of the prompt, especially bookkeeping ids, revision refs and internal states. Seldon keeps them itself.
- Add one sentence of senior-engineer coaching: "Design the data model around the real-world identities in the owner's story (for example, which night a tap belongs to) before writing handlers."
- Switch: SELDON_OFF=leadThinBrief.
Prove offline first:
- Render the old and new WORK prompts for the recorded DoorCount and ShelfLife WORK questions. Report sizes.
- Then run 2 real builder sessions per arm on DoorCount (Terra 6.1 medium, `codex exec` with the rendered prompt in a disposable copy of the candidate base), arms old vs new.
- Then a blind Sol-free Terra judge (or plain-language comparison) scores maintainability and the two night-identity cases (old-night retry, delayed close) on each product.
- Report the scores.
Tests: journeys you touch plus cold imports; no gate, no cohorts. Report C:/seldon/tests/leadThinBrief-0/REPORT.md (max 15 lines). Leave the diff, do not push. Temp files only under C:/seldon/tests/leadThinBrief-0. Never open desktop windows. Never read C:/seldon/sealed/.
