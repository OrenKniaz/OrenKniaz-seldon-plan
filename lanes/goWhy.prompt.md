# Lane goWhy (Terra 6.1 medium): analysis only, no code changes
Seldon Lead's guard was changed to do one complete walk, one repair, then a scoped re-walk (leadGuardOnce). On ShelfLife it still took 13 and 16 calls, about 350k fresh tokens, and was not fully verified. The target is ≤1 repair cycle and ≤150k tokens.
Slots:
- C:/seldon/tests/m1/shelf-goR-6dc9a611-g01: ALIGN REVIEW WORK RECEIPT JUDGE MILESTONES REVIEW WORK JUDGE WORK JUDGE WORK JUDGE
- C:/seldon/tests/m1/shelf-goR-6dc9a611-g02: 16 calls, a similar sequence
Logs: C:/seldon/tests/goRshelf/g01.log and g02.log. Each calls/<id>/ has question.json and answer.txt.
Answer with quotes:
1. Why did MILESTONES and REVIEW (a re-plan) run after the first JUDGE? What did the guard say that triggered a plan revision, e.g. a B amendment?
2. For each later JUDGE: was it a full walk or a scoped re-walk, which new defects did it report, and were those defects in code the repair changed (a regression) or in old code the first walk missed?
3. What did each repair WORK change, and did the builder re-run its own checks?
4. The top 2 reasons the target was missed, and one design-level fix for each (not a patch).
Write C:/seldon/tests/goWhy-0/REPORT.md, max 20 lines. Do not edit any repo. Temp files only under C:/seldon/tests/goWhy-0. Never read C:/seldon/sealed/.
