# leadThin (T-249)
Patch verified against Seldon `513de6a` (lane snapshot `9bc4d93` has the same Git tree).
Scripted hello reaches C with one milestone and one builder session. Reopening at B keeps Lead after the selector changes. B precedes every builder assignment and product commit.
The two-milestone journey replays the first approved command, catches the broken greeting despite the weakened builder test, and resumes the second builder with the exact failure. The repair reaches scripted C.
Source +490/−14. 29 Python modules and 2 CommonJS modules cold-imported. 96 Orchestrator prompt and instruction pairs match the base byte for byte.
Sole default `bash scripts/gate.sh leadThin` passed 151 cases vs 149 on base in 609.16 s (611.17 s wall). The suite exceeded the 600 s target by 9.16 s.
Lane 2 covers native provider delegation, skill and workspace confinement qualification, deeper crash and scope-change recovery, rendered memory and the read-only board. C evidence here is scripted.
Start the MCP server from the repo root in Git Bash with `SELDON_MODE=lead PYTHONPATH=src /c/Users/oren/codex-harness/.venv/Scripts/python.exe -m seldon.frontdoor mcp`.
Call its `start` tool with `{"dream":"Build a CLI that prints Hello, Ada!","folder":"C:/seldon/tests/leadThin-8/hello"}`.
