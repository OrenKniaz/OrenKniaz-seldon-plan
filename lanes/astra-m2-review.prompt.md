Read-only design review for the Seldon lead (Opus 5.5). Do not edit or run anything that writes. At most 30 lines, plain words.

Binding: CHARTER.md v1.6 and BLUEPRINT.md v1.4 in ~/codex-harness/work/sprint-20261027/semantic-cc (read section 3, R1-R14, section 6 M2 row: "In this order: Area, Contract, Decision records and the skeleton wave; then WAVE-VERIFY with flow review (replacing the M1 DEMO/PRODUCT judgment) and fixup units; then ARCHITECT, per-area DETAIL and a bounded per-area REVIEW"). Current main core: src/seldon (~2.8k lines).

Two M2 draft lanes were built earlier WITHOUT a lead brief and are frozen, never landed: ~/codex-harness/work/lanes/m2-flow-20261111 (commit abfd4a5) and ~/codex-harness/work/lanes/m2-area-20261111 (commit 6733da7). Compare each against main (git diff against its base, and read the new modules).

Answer:
1. For each draft: what it builds, in one paragraph; which parts match blueprint v1.4 M2 and which contradict it (especially anything that re-reads source after integration, reviewer-selected walkthroughs/inspections, evidence-reuse hashes, or product-sized questions, all now forbidden).
2. Reuse list: specific modules/functions worth porting to the M2 lane, with file paths, and what to drop.
3. A proposed M2 slice plan: 3-5 lanes in blueprint order, each with its files and exit, marking which lanes can run concurrently (disjoint files) and which must be sequential.
4. Risks the lead should put in the M2 brief.
