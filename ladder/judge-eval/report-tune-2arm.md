# Judge eval tune replay

The paired replay uses the current Seldon renderer at main commit `21b638118f9ad549d542a083ca81b7b441f3bcac` (tree `a8c2f54ce2db65dd5409c372239a90205d7b4f68`). Both arms use gpt-6.1-terra at medium effort. Each arm is configured for one pass over 23 distinct recorded questions, covering 25 tune cases. Two folded records each cover two scored cases. The source facts, answer schema and attachments are common to both arms. Answer keys and independent oracle results stay outside the judge input.

The extension adds 3 MUST_CATCH, 3 CONTROL, 3 EVIDENCE_GAP and 1 CODE_QUALITY case. Six join tune. Four (40%) go to the sealed 19-case holdout. The split is by run, and holdout was neither rendered nor scored.

| Arm | MUST_CATCH recall | CONTROL false alarms | EVIDENCE_GAP | CODE_QUALITY catch | MUST_NOT_FLAG alarms | Validated calls |
|---|---:|---:|---:|---:|---:|---:|
| control | 0/6 | 0/13 | 1 | 0/1 | 0/4 | 23/23 |
| prompts2 | 0/6 | 1/13 | 1 | 0/1 | 0/3 | 22/23 |

Each arm attempted 23 calls. The prompts2 provider timed out on historical MUST_NOT_FLAG case `e57b218-z11/call-17f8809bb6e74581b5ba63437a12ec6f` after 300 seconds. Cleanup was verified. The invocation was not retried, and all cases contributing to the requested recall, CONTROL and code-quality rates returned usable answers.

The prompts2 CONTROL alarm is `cf88f0d-g01/call-6191a1443af14ca0b5d971941ab6bc4d`. It escalated missing full-journey offline proof to must-fix because the reported external request block covers only the browser reload. The recorded acceptance sentence does ask for the entire fresh-folder check with network access unavailable, so this is a defensible proof objection and exposes a weak historical CONTROL label. It remains an alarm against the frozen key. All new CONTROL cases in tune passed in both arms.

## Scoring

MUST_CATCH recall requires a must-fix finding that identifies the keyed defect by meaning. A similar symptom or a different defect on the same subject receives no credit. A must-fix finding on a CONTROL case counts as a false alarm in its scored scope. The four original MUST_NOT_FLAG rows are reported separately. CODE_QUALITY is scored separately for a specific, actionable observation about the readability or maintainability of the delivered source, with severity retained. EVIDENCE_GAP rows are excluded from both rate denominators.

## Semantic adjudication

| Tune case | Control | prompts2 |
|---|---|---|
| Three historical SQLite lifetime cases | Asked for startup diagnostics or successful endpoint checks. No connection-closure finding. | Asked for startup or integration evidence. No connection-closure finding. |
| Quiet Bench Stop | Flagged uncancellable signal preparation before the run starts. Missed the stale Stop response and terminal save failure. | Also flagged unhandled worker failures that can leave a session running. This partially addresses the outcome, but misses the Stop-specific race and durable stopped state with the actual count. |
| ShelfLife favicon | Missed the visible 404s. | Missed the visible 404s, while flagging a separate oversized-quantity issue. |
| ShelfLife SQLite connection lifetime | Missed the unclosed handles in the delivered source. | Missed the unclosed handles in the delivered source. |
| Quiet Bench code quality | Accepted the real implementation and checks without a readability finding. | Proposed lifecycle changes for cancellation and terminal failures. Missed the densely chained numerical code and single-line HTML. |
| Quiet Bench guide evidence gap | Flagged a missing walkthrough screenshot. | Flagged divergence between the walkthrough and guide and a missing second run in the comparison instructions. No replay arm had a recorded shell-argument observation. |

## Evidence limits

- The Quiet Bench Stop source exposes a stale acknowledgement and an unhandled final-save failure path. The independent server log confirms `os.replace` failed with WinError 5 for the stopped session and left its terminal data in `.tmp`. The judge packet contains the code, but its walkthrough polls for eventual completion and supplies no such exception.
- The Quiet Bench guide contains all four CLI examples. The oracle parser skips the assignment-prefixed `run` line. An offline probe ran all four commands in PowerShell 7.5.4 default mode. Legacy native-argument mode failed while passing the JSON to `run`. The recorded Python walkthrough bypasses that shell boundary. The guide case measures the missing shell-specific observation.
- ShelfLife's favicon 404 is in the delivered server stderr. Its unclosed SQLite connection is visible in source. The oracle's later WinError 32 does not identify which process held the file. A separate heading oracle matched literal `Expiring soon` and stopped before testing the behavior of the existing `Use these soon` region.

## Replay records

Raw calls are under `C:/seldon/tests/judgeEval2-2` (control) and `C:/seldon/tests/judgeEval2-3` (prompts2). Per-case semantic grades are under `C:/seldon/tests/judgeEval2-1`. SHA-256 of `tune.jsonl` is `2e50b71898d4c73d67cd9c2a1604f3f68308ae04b86a2d9052f6c8affbeb4b35`. The Stop key's explanation was updated from the independent server log after the control batch started and before inspecting the Stop response. The question, split, and scoring target stayed the same.

Native artifacts confirmed the same question JSON, schema and image bytes in each pair, with a different rendered prompt for all 23 pairs. Each recorded invocation selected Terra medium and disabled shell tools. All 46 calls have verified cleanup receipts.
