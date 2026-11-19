CHARTER: serves C1/C4/C9/C16 — violates no I#; preserves I1/I10 and REV1 confinement.
TRIAGE: DESIGN — r21/r22 asked the LLM to preserve canonical membership while permitting impossible references. Siblings: omitted nodes/targets/scenarios, partial corrections treated as deletion, invalid parent kinds, paths in codeRefs/testRefs/resultRefs.
SIMPLEST: CODE retains outline membership and proposed edits in existing judgment diagnostics, merges supplied sections, and binds IDs/revisions. First answer and repair share edits[{ref, section, value}], rationale, reply. C4 remains two exact-fix retries, then existing steering; repair admits only the refusal's named sections. No new store/state machine.

Owner surfaces: run_schemas/run_questions/run_content and the shared schema decoder. Spine exports its existing scenario-kind tuple for reuse. Publication/recovery source is untouched. The patch is relative to the supplied clean stage-trace1 checkout, including PUB1 + REV1B; no commits, pushes, lane-local commit identities, actual-provider launches or shared installs.

| Question field | LLM-or-CODE | Reason / tradeoff |
|---|---|---|
| edits | CODE retains membership; LLM supplies changes | Omission preserves content; missing initial semantics receive a named refusal. |
| edits[].ref | CODE allocates/enumerates; LLM selects | Additions use the existing outline; trace answers cannot invent identities or delete members. |
| edits[].section | CODE enumerates; LLM selects meaning to change | One typed shape; repair authority comes only from the recorded refusal. |
| edits[].value | LLM semantics; CODE types, eligible handles and merge | Parents use ALLOWED_PARENTS; trace/baseline links use TRACE_LINKS; scenarios share SCENARIO_LINKS. Other reference enums follow existing dependsOn/lessons/sourceRef/targetRefs, expansion and action-target contracts. Existing non-reference semantic subfields remain domain-open. |
| rationale | LLM | Explain WHY; never grants authority. |
| reply | LLM | User explanation; never substitutes for state or consent. |

Files without code nodes: leave codeRefs empty until a canonical code node exists. Filenames remain ownedFiles/launch paths. This avoids fabricating code evidence or adding a filename allocator. With no eligible handles, reference arrays admit only empty values (plus existing optional nulls).

Deleted surfaces: full trace response envelope, exact-membership copying check, trace removal authority, separate repair-envelope reconstruction/comparison, arbitrary-handle precheck and redundant scenario handle checks. The existing repair control/retry path remains. Schema-invalid edits also retain the other proposed sections. Enum-compatible schema branches now give exact fixes naming the actual node/section instead of a shorter unrelated branch error.

Evidence: read charter/instructions, r21/r22 diagnoses, retained capability audit and requested DB events 86–111/160–187 using read-only immutable SQLite. GO appeared 2026-11-08 14:55:06 local; polled every 60s with a 60-minute bound. No tests ran before GO. Runtime temp files are under C:/seldon/tests/trace1.

Existing r18 journey replays omitted targets/scenarios, invalid parents and server.py codeRefs through the fake-provider boundary. It requires partial exact fixes, correctly named refusals, confined cycle/testRoots repair, B, retained membership, reciprocal links, stale-credit rejection and preserved brownfield provenance. It adds no cases. The final CLI also exercises Copilot planning/Claude decoding, archived-producer recovery, real local RED/GREEN/delivery/C and post-C control paths. Fake providers supply meaning, not completion evidence.

GATE: RED — exactly one invocation: bash C:/Users/oren/codex-harness/work/lanes/golden-gate.sh C:/Users/oren/codex-harness/work/lanes/stage-trace1 trace1. Exit 1; 1 failed/10 passed in 537.42s; web 1 skipped/5.68s; wall 546.447s. Raw: golden-trace1.log beside this report.
TRIAGE: BUG — the fake provider emitted edits to the archived producer, whose advertised schema still requires its original envelope; siblings are retained baseline-producer journeys. Fixed in the fixture by following that schema. Production gains no legacy branch. Exact-fix diagnostic correction and this fixture fix followed the frozen gate; no source changed during it and no second full gate ran.

Final affected verification: CLI golden + suite budget + module size guards, 3 passed in 769.74s (C:/seldon/tests/trace1/final-focus.log). r18 36.73s, trace/brownfield 0.80s, mixed-provider 9.64s. These are composed results, not a fresh green full gate.
TRIAGE: DESIGN — final selected CLI runtime exceeds 600s; five serial admission-interruption journeys take 388.73s. Owner/next action: golden scheduling/runtime must preserve coverage and deliver a green full gate within 600s. No baseline runtime attribution, timer/cap change or recovery edit. Intermediate focus also returned one OperationalError; its SQLite cause remains unestablished and is recorded in the discovery ledger.

Delta vs supplied tree: src +87/-89 = -2 lines; tests +53/-34 = +19; discovery ledger +4. Zero new cases; suite/source ceilings unchanged. Whitespace and patch reverse-apply checks PASS. Last proven product outcome: partial trace authoring/repair reaches B and final fake-provider CLI reaches C. Next unproven step: CC's integrated full gate and authorized real-provider r22 replay. Browser/full-vision acceptance remains unverified.

Patch SHA-256: c1628d7a403be973683f8a8001a0f757a9d6c4d83108e0beb94652c88b4b720c
