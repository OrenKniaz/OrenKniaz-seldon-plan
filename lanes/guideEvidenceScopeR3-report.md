TRIAGE: DESIGN — guide coaching did not preserve the supplied external evidence directory for checks and local probes; sibling generated evidence belongs there too.
Changed guide instructions to use the supplied directory without overriding it; no ownership permissions changed.
Focused PowerShell delivery: 4 passed in 27.83s; missing approved runtime remained unverified at C.
Added product-local evidence rejection through normal scoped snapshots: affected case passed in 5.06s.
Separately invalid `checks/** excluding checks/kit/**` is owned by scopeExpression, not this fix.
Source +3/-1; focused test +10/-1; patch: lanes/guideEvidenceScopeR3.patch.
No real provider run or gate; coordinator owns real Quiet Bench exit and acceptance.
