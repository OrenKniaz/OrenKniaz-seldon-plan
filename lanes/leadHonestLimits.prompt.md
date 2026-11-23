# Lane leadHonestLimits (Sol 6.2 medium), Lead only: an honest "can't verify here" is not unfinished work
Repo: this lane dir is main 989c515 plus the gated leadPlausibleGuard. Binding: BLUEPRINT-LEAD.md line 45: "A missing device or inaccessible environment gets an explicit unverified observation with a reason." Oren: "a run NEVER fails".
Live fault, run C:/seldon/tests/plausDoor/d01.log, slot C:/seldon/tests/m1/door-plaus-*-d01:
- Calls: ALIGN, REVIEW, WORK, WORK, COACH, WORK, COACH. The runner then exited with code 1, state BUILD, and no C.
- The builder had built DoorCount. Its clean-copy walkthrough and its phone-sized browser tap both passed.
- It refused to claim the physical-phone-over-Wi-Fi check, which is impossible in this environment.
- leadKeepBuilding treated that honest limitation as "not done" and kept resuming. COACH told it to report the limitation, and the loop repeated.
Triage first: why exactly did the runner end with exit 1 in BUILD? Name the file and line, and say BUG or DESIGN.
Then fix at the root:
- The builder receipt has one way to say "built; these promises are verified; these checks cannot run in this environment, because <reason>". Seldon records each of those as an explicit unverified observation with its reason and moves to PROVE. That is not unfinished work and does not trigger a continuation.
- keepBuilding resumes only when the builder says product work remains.
- The guard and C show the limit to the owner. A promise that can only be verified on a physical device is disclosed at C, not blocked.
- Whatever made the runner exit 1: a run never ends that way. It steers, asks, or pauses resumably.
Switch: none, this is a bug fix. Delete any code that made "limitation" equal "not done".
Tests: a journey where the builder reports an environment limit and the run reaches C with the limit disclosed, plus journeys you touch and cold imports. Do not run gate.sh or cohorts.
Report C:/seldon/tests/leadHonestLimits-0/REPORT.md, max 10 lines: root cause (file:line), fix, net src. Leave the diff, do not push. Temp files only under C:/seldon/tests/leadHonestLimits-0. Never open desktop windows. Never read C:/seldon/sealed/.
