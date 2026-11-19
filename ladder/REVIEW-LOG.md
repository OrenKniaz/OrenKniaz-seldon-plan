# Periodic review log (Oren 11-08: one useful read-only review every ~12h; skip if none)
Checked whenever CC wakes; if the last entry is >12h old, launch one review or log a skip.

| When (JST) | Type | Why now | Output | Yield |
|---|---|---|---|---|
| 2026-11-07 19:00 | Implicit state machines | fix17 host race; recurring same-shape stalls | design-review/state-machines-audit.md | fix17 root cause (closed judgment offered); 2e ownership map; 3 small bugs |
| 2026-11-07 19:10 | Duplicate sources of truth | same | design-review/truth-dupes-audit.md | review-credit authority hole; recovered-job rejection; r16/r17 explained |
| 2026-11-07 19:10 | Compensating code | size target 27-30k | design-review/compensating-code-audit.md | 2.2-2.5k deletable; 27k not substantiated |
| 2026-11-07 22:30 | Recovery flake diagnosis | 4 gates failed same journey | design-review/recovery-flake-diagnosis.md | recov1: prelaunch-failure product bug |
| 2026-11-08 00:30 | Golden meaning + redundancy | gate speed blocking landings | design-review/golden-meaning-audit.md | 131s deliberate silence movable; 4 weak assertions; speed plan post-2e |
| 2026-11-08 ~02:00 | Packet sufficiency + simplicity (inside 2e independent review) | 2e principal risk; PROD only −45 net (+1,130/−1,175) | lanes/stage-2e-reviewH.md | 2 P1 packet gaps (build judge no implementation content; steering no recovery subject); r18 proof incomplete; 2e = protocol rewrite, only 50-100 more lines cuttable |
| 2026-11-08 07:40 | Partial publication (one fact, 2+ writes) | 5 host reds share shape (recov1 x4 + 2e delivery KeyError); lead-dont-follow trigger | design-review/partial-publication-audit.md | DESIGN: 11 split facts; one rule (owner publishes one terminal outcome last; everyone reads it); 5 product gaps incl. interrupted revalidation never consumed; -40..-100 lines → lane pub1 after r19 |
| 2026-11-08 eve | Should-it-exist (subsystem vs charter vs provider-native) | Owner: are we fixing things that should not exist; no real run at B since v1.2; Astra (important deep review) | design-review/should-it-exist-audit.md | Verdict (b) thin A-to-Z path in repo then delete displaced code; est 12-16k lines removable (unvalidated); no charter clause needs all kinds before B; old-run migration has no value; awaiting Oren decisions (thin path, C5 collapse, no cross-version migration) |
| 2026-11-09 11:15 | Skipped: r26 Sol diagnosis covers this window | No review would beat fixing the path that blocks the first real run | - | - |
| 2026-11-09 23:40 | Clean-core scaling and patch audit (Astra) | Owner: do not patch bad design; run 09 failed intermittently; last review >12h | design-review/clean-core-scaling-audit.md | Patch list; code must own evidence applicability; repairs routed by cause; workers check own work; one scoped work unit |
