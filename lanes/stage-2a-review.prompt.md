INDEPENDENT CODE REVIEW — Stage 2a (read-only; you are NOT the author). This folder = Seldon main efc4a25 + local commit a97ecf0 = exactly ../stage-2a.patch (SHA256 be14e8390cb0316d821fb164b970aee7a26fc9991fa913db48fbaee176ce41d6). Review `git diff HEAD~1`. Read CHARTER.md (C3, C4, C10, C11, I1, I2, I4, I5, I6) and ../stage-2a-report.md.
Why it's flagged: it changes AUTHORITY. That covers canonical review admission in PlanStore, finding membership and closure, and review-reuse credit on revision deltas.
Impact-only review. No style, naming or nitpicks. Find only defects that would:
1. grant approval or closure without a current, bound, positive judgment (e.g. a stale or reused verdict, a member closed by another member's verdict, an empty or malformed review counted as approval);
2. lose a finding or a gap (a finding dropped from membership, an unresolved member silently closed, a conflict resolved without a judgment);
3. block or deadlock on meaning instead of staying pending (I2/I4), or create a wait that never ends (I5);
4. create a second owner of the same truth (I6), or let code judge meaning by pattern (I1);
5. remove something a later charter piece needs, without a replacement.
For each finding: file:line, concrete failure scenario (inputs → wrong outcome), severity HIGH/MED, and the one fix. Cap at 8 findings. If none qualify, say "NO BLOCKING FINDINGS" and list the 3 riskiest spots you checked.
First line: `VERDICT: APPROVE | APPROVE-WITH-FOLLOWUPS | REJECT`. Output ≤45 lines. No files changed, no tests run.
