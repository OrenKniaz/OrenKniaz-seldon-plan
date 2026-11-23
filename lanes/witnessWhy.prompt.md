# Lane witnessWhy (Terra 6.1 medium): analysis only, no code changes
Question (Oren 11-22): why do the Lead builder's proof files (checks, try-it guide, lifecycle logs) break while the product feature works? We now carry such gaps (BLUEPRINT-LEAD v0.5). We want to learn the cause and coach it out of the builder brief.
Evidence:
- Control repairs: C:/seldon/tests/m1/shelf-coord4b-34d9378-csb01..05. Many repairs changed only guide/check files.
- Carried gaps: C:/seldon/tests/m1/shelf-witnesscarry4-*-w401..w405 and shelf-witnesscarry-*.
- Each slot's calls/ directory has the WORK brief, the receipt, guard verdicts and must-fix findings. product/ has the code.
For every witness-only must-fix or carry, record: slot, B line, what was broken (quoted), and the cause class. Use classes such as: witness never run by the builder; witness omits the actual invocation; guide step does not match the real command; environment/path assumption (Windows, ports, browser kit); brief asked for something ambiguous; witness asserts the wrong thing; other.
Then count per class and name the top 2 causes with quotes. For each, propose one sentence for the builder brief that would prevent it. It must be a coaching sentence, not a new rule or check.
Write C:/seldon/tests/witnessWhy-0/REPORT.md, max 25 lines. Do not edit any repo. Temp files only under C:/seldon/tests/witnessWhy-0. Never read C:/seldon/sealed/. Never open desktop windows.
