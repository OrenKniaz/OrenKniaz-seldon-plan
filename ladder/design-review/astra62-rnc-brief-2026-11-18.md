# Astra 6.2 job: write the big M3 test dream and its SEALED oracle (2026-11-18)

You are the separate reviewer for Seldon's held-out milestone dream (BLUEPRINT M3 exit, "held-out exit": the brief and oracle are written by a separate reviewer and kept sealed from builders and the lead). The lead (Claude) will never read the oracle. Write it so it is fair, strict on behaviour and silent about implementation.

## The owner's facts (verbatim intent, Oren 2026-11-18)
- No hardware is connected. Build around **recorded data from a demo car** (raw data, no NDA, may be read by any model): `C:/Tuning data/RNC/AKM HV Tesla Y/EU Model Y March 2024 - Ford/Day1/Tuning 1/Cal1` (93 MB, 76 files: `.mat`, `.dat`, JSON params/results, flash XML, SIL output logs zipped, a performance log).
- Goal in his words: "use it to build a simulation tool around it for NFxLMS / ML method for ANC or something."
- Channels: **rmic** = accelerometer reference channels, one axis each; **pmic** = physical error microphones (1-4 headliner, 5-12 headrest); **emic 1-8** = ear-position virtual microphones (the virtual-microphone technique maps pmic to emic for adaptation); **STF** = secondary path: a sine sweep from each speaker (9 speakers), recorded by all 20 microphones. **Fs = 3 kHz.**
- **Any language and any libraries** are allowed (Python with numpy/scipy, C, anything).
- **The front end is central (owner, 2026-11-18):** "make sure the big dream holds front end controlling simulations parameters for different testing, and plotting for viewing results." The operator screen must let him set and change simulation parameters (algorithm, step size, filter length, regularisation, channel selection, band ranges, data span and similar) to run different tests, and must plot the results (e.g. attenuation per mic and band, time/frequency curves, secondary-path responses, convergence, before/after spectra, and comparisons between runs). The dream text must say this in his voice; the oracle must check it on the real screen (parameters change a run's results; plots exist and reflect the run's data).
- He can answer questions about the file structure, but expects the builder to figure it out.

## Deliverable 1 — the dream (what builders get)
Write `C:/Users/oren/codex-harness/work/ladder/briefs/L3/5-rnc.json` in the same shape as `work/ladder/briefs/L3/repair-cafe.json` and `4-quietbench.json` (read both). Rules:
- `message`: the owner's dream **in his voice**, the way a real engineer would write it: what he wants to be able to do with this data and why, his quality bar (measured not assumed, safe outputs, sessions reloadable, results compared and explained). **Do not dictate waves, units, file layouts, endpoints or an interface spec.** Seldon must size and stage it. Include the data path and the channel facts above. It should be clearly a large product (several areas: data import/parsing, secondary-path estimation from STF sweeps, virtual-microphone mapping, multichannel NFxLMS simulation on recorded reference/error data, an ML method and its comparison, attenuation per mic/band reporting, session storage/browse/reload, an operator screen, optionally parameter export), but let the owner say it in plain words.
- `profile` / `scriptedUser` / `interrupt`: a persona with one private preference and one exclusion, a mid-run kill, and check-in behaviour like Quiet Bench (one realistic steer, then "don't stop again"). Use the grow-loop persona shape from `repair-cafe.json`.
- **Do NOT put the oracle, checks or hidden expectations in this file.** If the oracle needs a fixed command to start the product, have the dream ask for a documented way to run it (the oracle will follow the product's own docs, like the Quiet Bench guide check).

## Deliverable 2 — the sealed oracle (what nobody on the build side sees)
Write into `C:/seldon/sealed/rnc/`: `oracle.py` (black box: `python oracle.py <product-dir> <evidence-dir>`), `README.md` (how to run, what each check proves), and any held-out data or answer keys. Rules:
- Test **behaviour a user would require from the dream text**, never wording, status codes or file names the dream does not state. Follow the product's own documentation to run it.
- Ground truth from evidence already in the folder where possible (e.g. the tool's own `EstimationErrorResult.json`, sweep results, performance log) and from independent recomputation (your own reference secondary-path estimate and an independent FxLMS/NFxLMS reference implementation on the same data). Hold back part of the data (a channel subset or time span) that the dream does not point to, if useful.
- Checks should include, at least: data actually parsed (channel counts, Fs, lengths match the files); secondary-path estimates close to an independent estimate (tolerance you justify); the virtual-mic mapping exists and is used for adaptation; simulated attenuation per error/virtual mic and band is plausible and close to an independent reference run; the algorithm is stable (no divergence on the recorded data; a limiter/safety behaviour exists if the dream asks for it); results are saved and reload identically; the operator screen shows a run and its results; a documented end-to-end run from a fresh copy works.
- Mark anything you cannot verify as `unverified` with the reason; never silently pass.
- Plain-model fairness: the oracle must be passable by a strong single-session builder that reads the same dream.

## Constraints
- Read the data files freely (they are not confidential). Do not modify anything in the data folder; copy what you need into `C:/seldon/sealed/rnc/`.
- Never read any `.env` file. Do not read or edit Seldon source. No calls to other models/providers.
- Do not write anything about the oracle into any file outside `C:/seldon/sealed/rnc/`.

## Reply (your final message, readable by the lead)
At most 12 lines: the dream's one-paragraph summary, the number of oracle checks by kind (no details), how long you expect a plain single-session build to take, and anything the owner should confirm about the data (e.g. a file you could not parse).
