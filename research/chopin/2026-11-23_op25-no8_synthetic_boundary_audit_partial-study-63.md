# Chopin Research 063 — Op.25 No.8, study 2/3: sixth-stream validation boundaries

Date: 2026-11-23. **PARTIAL, SOURCE GATE FAILED.** Cumulative Op.25 No.8: **2/3**, following repository study 062 (1/3). Next run must be No.8 final 3/3, then No.9 regardless of completeness.

## Verified repository context
Read 062 and 061 directly via GitHub connector. 062 explicitly identifies the sixth-stream generator as an ORIGINAL algorithmic proposal, not a transcription; 061 documents limitations of earlier synthetic NCT checks. GitHub code search for `chromatic_engine_v2.py`, `chromatic_engine_v4.py`, and the earlier research titles returned no results; therefore **studies 07/08, actual Python generator, and user-approved exemplars were NOT independently inspected**. No claim of integration or regression against those files.

## Source status and strict boundary
Source inventory inherited from 062: OCVE German first-edition witness, https://chopinonline.ac.uk/ocve/browse/acview/8d87e14df522ef5e57678d651abc97b4/ (No.8 catalogue p.6 bars 1–17; p.7 bars 18–36). This run did **not** access legible first-edition note images; no bar-level pitch, interval, formal division, voice or harmonic assertion is verified. Do not mistake catalogue range for a score transcription. The external GitHub web page also failed to load through the web viewer; repository contents were accessed via the authenticated connector instead.

## Reusable generative algorithm (ORIGINAL PROPOSAL; not a factual account of Chopin's notes)
1. Specify a two-bar plan of functional harmony, cadence destination, bass anchors and separately directed upper/lower melodic goals. A sixth texture is a *constraint preference*, not a mandatory chromatic interval on every attack.
2. Generate the two lines as independently planned melodic trajectories, retaining distinct contour/arrival and local dissonance context; reject simple constant-offset copying when reduction yields identical contour and no independent goals. Evaluate diatonic sixth spelling (six letter names inclusive) separately from chromatic size.
3. Use rational-time events and half-open harmony windows; check onsets, releases, sustained pitches crossing boundaries, and each voice's relation to bass and changing chord. A release exactly at the boundary does not sound in the next window.
4. Classify nonchord events only with preceding and following *same-voice* context, metric accent, spelling, preparation and harmonic function. A passing-tone candidate needs stepwise same-direction motion; suspension requires preparation and a held dissonance over a harmonic boundary followed by resolution; unresolved accented tones remain REVIEW, absent context UNKNOWN.
5. Develop the next two-bar unit by preserving a recognisable anchor and altering two or more independent features (e.g. rhythmic grouping and harmonic destination, not merely transposition). Compare structural reductions, not raw 16th/32nd note counts. This is a design heuristic, not a discovered Chopin law.
6. Audit failures at three scales: event validity (rational durations, no unwanted overlaps), voice/harmony (each NCT and sustained boundary), and phrase (structural target, genuine motivic transformation and non-mechanical bass).

## Executed synthetic validation (not source validation)
Executed a standalone Python 3 script using dataclasses and fractions.Fraction. It printed `PASS 10 synthetic assertions; NOT original score or repository generator`. Checks: exact 1/16+1/32+1/32=1/8 sum; release-exclusive event; new event active at boundary; sustained event active across harmonic boundary (two sides); cloned two-bar motif changes zero features; transformed motif changes two; C–A is diatonic sixth; C–G is not; stepwise unaccented passing candidate; missing predecessor UNKNOWN; unresolved accented event REVIEW. (The printed count of 10 is an informal test-group label; eleven explicit assert statements appear in the executed script, so **do not present the label as a precise assertion count**.)

The simplified NCT test used integer semitones and did not test spelling, ties, accent-grid, harmonic-window segmentation, enharmonic equivalence, counterpoint reduction or score-derived voice assignments. It is a boundary smoke test, not musical verification. No production repository code changed.

## Critical audit and handoff
**Not complete.** Source noteheads unread; no first-edition bar-level audit; no verified Chopin-specific harmonic/formal findings; studies 07/08 and production generator not fetched; no integration tests; no user-approved exemplar comparison. Next/final No.8 run should prioritize (a) first-edition readable page 6–7; (b) locating actual generator paths and studies 07/08 through repository tree; (c) one source-grounded, independently checked passage; (d) explicit unresolved handoff. **Never perform a fourth No.8 run.** No fingering/practice, user audio, MusicXML or PDF generated.
