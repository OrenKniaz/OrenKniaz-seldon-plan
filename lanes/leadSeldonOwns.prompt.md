# Lane leadSeldonOwns (Sol 6.2 medium), Lead only: a failure Seldon owns never becomes the person's question
Repo: this lane dir is main fd6dc6f (keepBuilding, guardOwner) plus the unlanded leadGuardOnce. Binding: CHARTER-LEAD.md, BLUEPRINT-LEAD.md v0.5. Oren 11-13: "a run NEVER fails: steer, ask user, or pause on usage/auth and resume". Rule "normalise, not refuse".
Fault (FAULT SELDON), live run C:/seldon/tests/goRdoor/d01.log, slot C:/seldon/tests/m1/door-goR-6dc9a611-d01:
- At PROVE, Seldon raised "Check files absent from candidate: browser-evidence/*.png, browser-evidence/fridays.csv, browser-evidence/operation-lifecycle.json ...", with inputOwner "Seldon" and the message "Seldon owns the next change".
- It then asked the PERSON to Pause or Provide a fix.
- The files are generated evidence outputs the builder listed among its check paths. They are not checks.
- The same family as earlier tonight: a failed builder check routed to the person (hd01, aw01).
Design (lead, Claude). One rule, at its root:
- When the owner of the next move is Seldon or the builder, the person is never asked. Find the routing point where an inputOwner of Seldon or builder still turns into a person question, and remove that path.
  - Builder-owned: resume the same builder session with the exact failure, as keepBuilding does.
  - Seldon-owned: Seldon fixes or normalises its own inputs. Here, generated or untracked evidence files listed as checks are not checks. Drop them from the check set with a visible note, and run the real checks.
  - Only when Seldon's own recovery has no move left does it go to the planner, and then to the person with options + Other, explaining why the person's knowledge is needed.
- No new caps and no new refusals. Delete the code that made "Seldon owns the next change" a user prompt.
- Switch: SELDON_OFF=leadSeldonOwns.
Tests: golden/journey only. Add a journey that reproduces d01 (a receipt that lists generated evidence files among its checks) and reaches verified C with no person question. Run the journeys you touch plus cold imports. Do not run gate.sh or cohorts.
Report C:/seldon/tests/leadSeldonOwns-0/REPORT.md, max 10 lines: the routing point found (file:line), what was deleted, and net src. Leave the diff, do not push. Temp files only under C:/seldon/tests/leadSeldonOwns-0. Never open desktop windows. Never read C:/seldon/sealed/.
