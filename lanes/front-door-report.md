Four allowed files on base 8961a898: +414/-2, net +412; binary patch includes both new files and reverse-apply checks.
frontdoor.py is 237 lines (exceeds the ~150 target); all new code lines are at most 110 characters.
Commands: seldon mcp, seldon status <run>; hidden internal drive. Tools: start, state, answer, pause, resume, stop.
SDK API variance: installed mcp 2.3.0 has MCPServer, no FastMCP; factory uses MCPServer and deliberate ToolError refusals.
MCP journey: 30.77s; revision/new request, stale refusal, words-only A/B/check-in/C, pause kills worker, DONE worker runs once, accepted/non-scripted outcome, stop/status, decline.
Gate: bash scripts/gate.sh fdoor-3 with gate venv first on PATH: 15 passed in 335.62s (14 existing + 1 new); golden and recorded replays untouched and green.
Earlier gates: fdoor-1 13 passed/2 failed, 369.84s (SDK refusal fixed; unchanged golden 291.42s >270); fdoor-2 14 passed/1 failed, 127.50s (Git commondir admission recovery violated hermetic zero-recovery assertion).
Cold: C:/seldon/tests/fdoor-3/cold/smoke.py; fresh venv, plain pip install ., resolved mcp 2.3.0; 82.44s total.
Cold help/import and SDK stdio initialize/list passed, exactly six tools; exit 0 within 0.094s after closure; installed seldon status equals MCP state for the stopped run.
Existing core risks remain: pause spends a WORKING recovery; revise/decline beyond A/B ends the run. Earlier runtime failures recorded under T-77/T-91; no root-cause fix claimed.
Not done: main landing, real providers or human/L3 acceptance, read-only page, reprioritization, other worker providers; scripted journeys are not M4 acceptance.
No core file changed or wanted changing; no commit, .env read, global registration/settings change or real provider call. T-21/T-22 remain in progress pending lead landing/owner use.
