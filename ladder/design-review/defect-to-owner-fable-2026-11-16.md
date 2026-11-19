# Defect found in another unit's files reaches its owner (Fable, 2026-11-16)

Read-only. Basis: thin core `src/seldon` at 1f2d6df; stores f03, m01, m05 (mode=ro). No tests run; line counts are estimates.

## Cause: the worker already hands the defect over, and Seldon files it away
In all three runs the worker did the right thing with the tool it has: `discoveries: [{owner, correction}]`.
f03 guide, first WORK answer (r205): `outcome: done`, owner `u002`, the exact bug (`event.currentTarget` after `await` in web/app.js).
- `units.py:79-81` stores it as "pending check-in". Nothing reads that record again. This is the dropped hand-off.
- `units.py:113,137` then proves the finder's own check locally; it fails on the owner's bug; `units.py:179` charges the finder.
  Second failure = ASKED (`recovery.py:23,27`). f03 r214 -> r231 -> user.
- `fixups.py:22-23` forces every failing check back to the check's writer, so even WAVE-VERIFY cannot send it to the owner.
- Nothing tells the worker or COACH that a path exists: WORK prompt is silent on discoveries (`questions.py:67-72`),
  `questions.py:265` lists only dependencies as owners, `schema.py:68` leaves `owner` free text ("u001 / u002", "u003 / UI owner").
  COACH invents "Return the defect to u002" (r256, r282, m01 r323); `units.py:74` turns that advice into a counted failure of the finder.
- m01 last step: the worker gives up and edits `web/favicon.ico`; `gitwork.py:157` refuses without saying what to do instead.
The old sending half (`fixups.handoff`, 45 lines of cases) was deleted in 5182ada; its receiving half is still there, dead:
`states.py:32` `wait-owner`, `store.py:66,99` + `scheduler.py:27,41` + `decisions.py:24` `waitingFor`.

## The one rule
**A worker that names another unit as the owner of a defect is done. Its checks are then proven on the integrated product,
and a check that fails there goes to the owner its writer named, with the writer's correction.**
This is the wave rule thin already has ("a check that needs a peer fails here, return done, Seldon comes back only if it fails
integrated"), extended from "peer's files are absent" to "peer's files are wrong". No new state, no new question, no judge of
the discovery: the integrated check is the fact. If it passes (m01's favicon was intermittent), nothing happens.

## Design
1. `plan.execution`: each unit gets `handed = {owner: correction}` from its latest WORK report (discoveries naming another unit).
   `plan.assigned(local=True)` leaves out a unit with `handed`, exactly as it leaves out wave units. Derived, never stored;
   the next report without a discovery clears it.
2. `units.work`: keep discoveries inside the `worker_checks` record; a question that names another owner is treated as done
   (the answer is always yes). `run_unit`: a handed unit adds no gap checks at integration. It reaches DONE with its patch in.
3. `proof.gaps`: `units = list(handed of the check's writer) or [writer]`; correction = writer's correction + the observation.
   `fixups.py:22-23` deleted. The owner's fixup already carries the failing check as its integration check (`units.py:118-121`),
   so the owner proves the finder's real check before it is DONE.
4. Chain, unchanged counting: recovery key becomes per check and owner (`fixups.py:63` adds `":" + ref`), so the owner gets its
   one recovery even when the writer spent one on the same check (m01, m05). Second failure for that owner = user question (R15).
5. Coaching words, one shared sentence in the WORK and COACH prompts: "A defect in a file outside your write scope is its
   owner's to fix: leave the file alone, keep your check honest, name the owner and the correction in discoveries and return
   done. Seldon delivers it and reruns your checks on the integrated product." Fact "Correction owners" = every unit with its
   scope; `owner` in the schema is a choice of unit names. `gitwork.py:157` message ends with the same instruction.

## Removes
`wait-owner` and `waitingFor` (dead), the forced writer routing (`fixups.py:22-23`), the `seen`/charged bookkeeping in
`fixups.apply`, the write-only `discovery` record and its false "pending check-in" label, free-text owners, and the COACH
detour for "may the owner fix it?". Estimate: src +14 / -14, net about 0.

## Honest limits
- f03 becomes fully autonomous. m01/m05: their first user question came earlier, from the two-failure chain on an intermittent
  check before the worker had named anyone; this design removes the dead end after it. The favicon line removed that trigger.
- Wrong owner named, or the owner hands it back: the same check fails again for that owner and the chain ends at the user.
- Note for the lead, not this lane: R15 says "two recoveries", `recovery.py:23` asks on the second failure (one recovery).

## Lane brief (Sol medium, one lane, shared files: units/plan/proof/fixups/questions/schema)
Files: `src/seldon/{plan,units,proof,fixups,questions,schema,gitwork,states,store,scheduler,decisions}.py`, `tests/seldon/test_journey.py`.
Change: items 1-5 above and the removals. No new module, no new state, no new question kind. Report src lines before/after.
Proof, golden/journey only (stub provider, real git, real checks):
- Fault twin `test_defect_reaches_owner_journey`: two units; unit B's file has a defect that B's own check does not see; unit
  A's check fails on it. A's scripted worker returns done with `discoveries: [{owner: B, correction}]`. Assert outcomes only:
  B gets one `unit_fixup` whose gap is A's check, B's file changes, A's files do not, no UNIT decision request is recorded,
  the run reaches scripted C. Variant in the same test: A answers `outcome: question` with the same discovery; same outcome.
- Twin of the twin: B's scripted fix does not work; the run ends WAITING on one UNIT question for B, resumable; A stays DONE.
- Existing goldens stay green; `test_journey.py:378` (free-text owner "future check-in") changes to a unit name.
- One real Terra ShelfLife run after landing; no unit test, no timing assertion, one gate.
