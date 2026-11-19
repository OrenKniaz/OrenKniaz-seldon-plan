# L3 dream: the ANC system

Named by Oren on 2026-11-11 as the large dream for rung L3 (Blueprint P1). Written by Fable from his six points. Lines marked **(assumed)** are my guesses for Oren to correct; they do not block Seldon work before M3.

## The dream, as the user would give it to Seldon

Build an active noise cancellation (ANC) system that runs on this PC with the Andiamo audio interface connected.

1. **Inputs.** Accelerometers and microphones, many channels, as reference and error sensors.
2. **Hardware control.** Drivers and control for the interface and what is connected to it: channel routing, gains, sample rate, start and stop, health.
3. **Simulation.** Predict ANC performance before touching hardware: acoustic paths, the control algorithm, expected attenuation per frequency band.
4. **Data.** Record sensor and output signals with their settings. A storage server, on this machine for now as a demo, to keep, browse and reload sessions.
5. **Real ANC.** Run cancellation in real time on the PC. Measure the loop latency and the attenuation actually achieved.
6. **If the PC's latency is not good enough:** write the real-time code for the ADSP-21569 evaluation board, with the PC as controller and monitor.

## Quality bar (assumed, for the Vision Lock to confirm)

- Latency and attenuation are measured and recorded, never assumed.
- Measured results are compared with the simulation, and the gap is explained.
- Output is safe: a limiter and a kill switch, so a diverging filter cannot drive the speakers hard.
- Every claim in the demo is backed by a recorded session that can be reloaded.
- The operator's screen is clear enough to run a session without reading a manual.

## Why this is the right L3

| Blueprint need | In this dream |
|---|---|
| At least 3 areas | Device I/O, hardware control, DSP core, simulation, data server, operator UI, embedded target |
| At least 3 waves | Skeleton with simulated devices; real I/O and recording; real-time ANC; embedded path |
| Contracts that matter | Signal frame format, device control API, session storage schema, algorithm parameter set shared by simulation, PC and board |
| Research (C7) | Measure PC loop latency, then decide for or against the ADSP path |
| Open-loop work (C22) | Tune the controller toward an attenuation target with a stop condition |
| Real-path proof (C26) | Simulation and recorded-data replay without hardware; hardware-in-the-loop with the rig |

A single agent session is not expected to deliver this well. That is the point of the rung.

## Open points for Oren

- Which Andiamo model, and how the PC talks to it **(assumed: a multichannel audio interface reached through a standard low-latency driver)**.
- Channel counts, sample rate, and the sensors and speakers on the rig.
- The noise to cancel and the target band and attenuation.
- The control algorithm family **(assumed: adaptive feedforward, FxLMS family)**.
- Whether the ADSP-21569 board and its toolchain are available on this machine.
- What Seldon may do unattended with real hardware. Until you say otherwise, automated runs prove simulation and replay only, and anything that drives real outputs waits for you.
