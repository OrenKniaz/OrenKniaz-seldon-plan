Base: f8c8081, snapshot labelled "base 050f3e8 golden-only"; no commit.
8 files, +210/-48, net +162: src/seldon/{schema,plan,architecture,plan_review,questions}.py; tests/seldon/{test_architect,test_fixups,test_journey}.py.
Signatures: def owner(document, check_ref): returns one unit ref; def assigned(document): returns per-unit checks plus None for wave checks.
Journeys passed: own-only declared wave, two-unit and legacy level promotion, file ownership despite sibling argv, valid WORK owner and one prose-owner re-ask; agreed/missing-contract twins reach B.
13 retained PNGs under checkPaths add 2690 JUDGE bytes; binary names/counts retained, source text unchanged.
REVIEW same-area bytes 1 vs 50 units: 5582 / 5582; ARCHITECT/DETAIL also flat.
Gate: bash scripts/gate.sh cown-5, venv first on PATH; 60.21s, 13 passed/1 failed, 14 collected vs 14 at base.
BLOCKER: owner-emitting blocked WORK validates, then forbidden src/seldon/fixups.py:64 raises KeyError('target'); later owner-only lane must consume owner. Golden is RED; later golden/replay cases were not reached.
Changed questions use the existing inference recorder; raw replay JSON unchanged. Inline synthetic checks now have worker-written owned files; one golden call line added.
Patch: git diff --binary; diff whitespace and reverse-apply checks pass. No dependencies, real providers, publication, forbidden source edits or charter/blueprint edits.
