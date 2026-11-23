# Lane leadResumeKilled (Sol 6.2 medium), Lead only: a killed run resumes where it stopped
Repo: this lane dir = main e4802dc. Binding: CHARTER-LEAD.md, BLUEPRINT-LEAD.md v0.5. Oren 11-13: "a run NEVER fails: steer, ask user, or pause on usage/auth and resume". Lead's whole value at medium/big size is continuity across sessions and interruptions.
Fault (FAULT SELDON, BUG or DESIGN, you decide):
- Lead M2 (4 milestones done; 26 calls) was killed mid-WORK by an external process kill, from our test watchdog.
- Reopening with `tests/seldon/real_hello.py <slot> --reopen --dream-file ...` printed state BUILD and "No terminal outcome recorded", then exited at once without doing any work. Log: C:/seldon/tests/m2v2/k01-reopen.log.
- A disposable copy of the slot is at C:/seldon/tests/m2-killed-copy. Work ONLY on copies. Never touch /c/seldon/tests/m1/m2-4f71-6dc9a611-k01 itself.
Find why an interrupted BUILD (a builder call started but never recorded as finished) is not resumed, and fix it at the root.
- The rule: on reopen, Seldon finds the in-flight step and continues it. For WORK that means resuming the same builder session if its thread id is recorded, with the milestone's promises and "you were interrupted; continue". Otherwise it starts the step again on the current candidate.
- No question goes to the person.
- Same rule for any interrupted call kind: JUDGE reruns the walk, planning calls are re-asked.
- Normalise; never refuse.
Prove it:
- a journey that kills a run mid-WORK and reopens it to verified C;
- and a real reopen of a FRESH copy of m2-killed-copy from this lane's src, to show it continues building. Let it run 2-3 calls, then stop it and report.
Switch: none needed; this is a bug fix.
Tests: journeys you touch plus cold imports; no gate, no cohorts. Report C:/seldon/tests/leadResumeKilled-0/REPORT.md (max 12 lines): root cause (file:line), fix, net src, and the exact reopen command. Leave the diff, do not push. Temp files only under C:/seldon/tests/leadResumeKilled-0. Never open desktop windows. Never read C:/seldon/sealed/.
