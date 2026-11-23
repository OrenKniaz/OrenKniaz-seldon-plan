# Astra deep review (read-only): Seldon Lead, macro view

You are reviewing a product, not a patch. Take the widest view you can. Form your own conclusions from the evidence. Reasoning from first principles is welcome.

## What Seldon is
- Its goal, in plain words, is in ~/codex-harness/work/sprint-20261027/semantic-cc/CHARTER.md, CHARTER-LEAD.md and BLUEPRINT-LEAD.md (v0.5). Read these first.
- Lead mode is a planner only: Seldon expands and crystallizes a person's dream into specs. One builder agent builds, and Seldon proves the result.
- The owner's view:
  - "planner should be so thin... no concurrency handled by us. it's just a beautiful process of expanding and crystallizing a dream, breaking it down into SW specs that are best fit for agentic development."
  - "he still owns the results... mainly be a subjective semantic guard... he should walk the user path."
  - "no patching, always holistic macro view."

## Code
Lead code is at main, ~/codex-harness/work/lanes/land-wt (src/seldon). Entry is frontdoor → lead.

## Evidence (read the raw material, not only summaries)
- **Same brief, both arms.** ~/codex-harness/work/ladder/briefs/S/S1-doorcount.md:
  - Plain Codex: C:/seldon/tests/plainBase/S1-doorcount-1 (events.jsonl, product).
  - Seldon Lead: C:/seldon/tests/m1/s1b-doorcount-cfb3438-s1b01 (calls/ has every planner, builder and guard question and answer; product/).
  - Blind hands-on review of both: C:/seldon/tests/s1walk-0/REPORT.md. A = plain, B = Lead.
- **Plain baselines:** C:/seldon/tests/plainBase/BASELINE.md.
- **Lead ShelfLife runs today**, in C:/seldon/tests/m1/:
  - shelf-coord4b-*: morning
  - shelf-witnesscarry4-*
  - race*: the latest; also look for raceCtl/raceLean slot dirs
  - shelf-imp2-*-is01: lone
- **Analyses written today** (they may be biased; check them against the raw data):
  - C:/seldon/tests/leadJudgeTokens-0/REPORT2.md and REPORT4.md
  - C:/seldon/tests/timeWhy-0/REPORT.md
  - C:/seldon/tests/witnessWhy-0/REPORT.md
- **Earlier Astra reviews:** ~/codex-harness/work/ladder/design-review/astra62-lead-vs-plain-2026-11-22.md and astra62-patterns-2026-11-19.md.
- **Today's log:** ~/codex-harness/work/ladder/HANDOVER.md (tail).

## Questions
1. What does Seldon Lead actually add over a plain agent on these dreams today, and what does it cost? Judge quality from the products themselves, not from Seldon's own verdicts.
2. Where does Seldon's design fight its own goal? Name the design-level causes, not individual bugs. Is anything here that should not exist?
3. If you were designing Lead from scratch for this goal, knowing what these runs show, what would its simplest shape be? What would stay, what would go, and what is missing?
4. As dreams grow from minutes to weeks of work, which of Seldon's costs and benefits grow, and how fast? What would make Lead clearly better than plain on big dreams, which is where it is meant to matter?
5. What single experiment would most quickly tell us whether that shape is right?

## Output
Write ~/codex-harness/work/ladder/design-review/astra62-macro-2026-11-23.md, at most 120 lines. Plain words. Evidence pointers for every claim. Separate "observed" from "inferred".

## Rules
- Read-only: edit no repo.
- Temp files only under C:/seldon/tests/astraMacro-0.
- Never read C:/seldon/sealed/ or any .env file.
- Never open desktop windows.
