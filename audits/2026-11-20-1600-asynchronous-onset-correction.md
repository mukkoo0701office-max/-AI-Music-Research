# 16:00 asynchronous onset correction

The previous `staggered_onsets.musicxml` has simultaneous note onsets (0 and 1 quarter notes in both parts), so it did not test staggered attacks. A corrected synthetic fixture was constructed and parsed: P1 onsets 0, 1; P2 onsets 0.5, 1.5 quarter notes, using eighth rests and divisions=2. This confirms event timing only, not the full six-part parallel-fifths/eighths engine.

Recovered Research IDs: 0. Unrecovered 001–093 and 112–115 (97) is inherited and not independently checked. Original v1.1 ZIP and original scores not verified. Next: asynchronous pairwise event-overlap regression and integration with ties, divisi and Cb sounding pitches.
