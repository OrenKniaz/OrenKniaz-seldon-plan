TRIAGE FAULT SELDON + DESIGN — T-245. q05 r105 showed a one-wave example and an empty remaining horizon. The CSV direction appeared in general history while User check-in was null.
q05 r106/r109, q01 r175/r178 and q04 r220/r223 returned empty wave lists. The merge restored the closed wave, then the wave-2 check refused it.
ARCHITECT now gets the direction tied to the completed wave and commit, the next wave number and a follow-on example. It still uses the existing scope and correction paths.
Golden RED reproduced the recorded refusal on base. GREEN reached wave 2 DETAIL on the first reply, retaining the completed wave, Git candidate, owners, plan nodes and observations.
The sole bare gate passed 144 cases, one more than base, in 487.98 s (489.18 s wall). All 28 cold imports passed.
nextWave.patch targets launch 6292effdf245bfa8797766e51a28b3b2e3577558 (snapshot 396b082), applies with plannerBrief and changes source by +30/-1 lines.
T-246 covers the separate DETAIL subset-scope collision in q05 r125/r133. The companion brief records the full-scope reply that reused the existing writer and reached REVIEW.
An authorized Quiet Bench rerun must establish whether native ARCHITECT plans CSV on its first continuation reply. Executed wave 2 and native acceptance remain open.
