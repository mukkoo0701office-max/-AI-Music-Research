# Chopin Research 076 — Op.25 No.12 final 3/3: evidence gate, audit fixture and handoff
Date: 2026-11-24. **Cumulative count: 3/3 (074, 075, 076). CLOSED; do not study Op.25 No.12 a fourth time.**
**Result: PARTIAL / quality gate FAILED; not a verified Chopin-specific generator.**

## Directly checked existing repository material
- 074 and 075: source-catalogue maps, proposed structural-tone / two-bar grammar, witness-aware meter, NCT and event audit.
- `research/chopin/2026-11-21_op10-no2_algorithm-study-07.md` and `...-08.md`: three-layer generation and target-tone correction; study 08 explicitly identifies mechanical 3-note-cell repetitions, unverified NCT handling and missing two-bar sequence.
- `research/chopin/code/chopin_op10_2_generativestudy.py`: `tones[j%3]` cycles inner harmony, outer voice walks a fixed 16-note chromatic line, bass alternates root/fifth; only `len(BARS)==8` is asserted. These are *code facts*, not Op.25 No.12 score facts. The code was read, not patched or executed.
- User-approved composition examples were not independently retrieved or verified.

## Source access: precise limitations
- OCVE: https://chopinonline.ac.uk/ocve/browse/acview/8d87e14df522ef5e57678d651abc97b4/
- CFEO: https://chopin-os.kdl.kcl.ac.uk/cfeo/browse/acview/81463b2d142d5d52c8dbca2bd48fde76/
Both URLs were opened on 2026-11-24; the accessible text presented a general source-browser interface, **not legible facsimile page images**. Earlier catalogue page/bar ranges in 074/075 remain metadata-only and were not independently confirmed here. No pitches, harmonies, bars, meter differences or voice leading are asserted as directly score-verified. A 2/2 versus 4/4 claim remains unverified.

## Reusable ORIGINAL compositional algorithm (not Chopin transcription)
**Input**: source-aware `Witness`, independently voiced `Event(onset:Fraction,duration:Fraction,pitch_spelling,voice,tie_id)`, `HarmonyWindow`, `PhraseGoal`.
1. Choose 4–8-bar phrase goal (bass harmonic destination, upper structural apex, cadential arrival), then decompose into 2-bar units. This avoids local repetition masquerading as development.
2. For each 2-bar unit specify a named invariant (attack grouping, contour family, or structural interval) and transform at least two of bass destination, harmonic function, register apex, turnaround position, density or voice allocation. Exact reprise requires an explicit formal reason.
3. Generate separate attack streams for structural upper voice, inner voice and bass; insert 16th/32nd figuration *after* defining anchor pitches. A three-note modulo cell without structural change is flagged, not automatically called stylistic.
4. Audit each sounding pitch at its onset **and** every harmony-window boundary that occurs during its sustain. Candidate passing note: stepwise approach and exit in same direction; neighbor: step away and return; suspension: prepared dissonance held across boundary then resolved; appoggiatura: accented dissonance with contextual resolution. Check chord spelling and altered members first. Missing harmony, tie, neighbor or score evidence => UNKNOWN, never PASS.
5. Preserve simultaneity: chord tones sharing onset are separate sounding pitches, not serial rhythmic durations. Maintain exact rational timing, including tuplets; check voice-wise measure occupancy, ties and cross-voice clashes with harmonic context.
6. Output provenance and confidence for each assertion. The structural grammar is a *testable design hypothesis*, not an inferred rule of Op.25 No.12 until facsimile and counterexamples are checked.

## Executed internal synthetic checks (2026-11-24)
An independent Python 3 `fractions.Fraction` script was **actually run** in the working runtime, with 10 assertions passing:
1. 16 sixteenths sum to one whole-note bar; 2. 32 thirty-seconds sum likewise; 3. six exact sixth-note fractions sum to one; 4. a held note is still active at the midpoint; 5. chromatic 60–61–62 is only a *passing candidate*; 6. 60–67–69 is not passing; 7. 60–61–60 is neighbor candidate; 8. missing harmony yields UNKNOWN; 9. unmodified 2-bar motive is flagged; 10. formally tagged reprise is exempt.
**Caution**: this tiny test is not a production parser, does not validate chord spelling, meter-witness disagreement, suspension, real-score pitches or any Chopin-specific stylistic claim. It does not execute or integrate the repository's existing generator. Its sixth-note fraction test represents a synthetic duration, not a verified notation in Op.25 No.12.

## Adversarial quality audit
**FAIL**: no readable primary score images; no note-level source-to-source comparison; no source-grounded harmonic, contrapuntal, motivic or formal analysis; no validated score fixtures; no generator patch/integration or regression against user-approved musical results. Therefore neither the research nor the algorithm should be described as completed/verified. Do not fabricate first-edition notes or convert secondary claims into score facts.

## Mandatory handoff
Op.25 No.12 is closed at **3/3 regardless of incompleteness**. Preserve outstanding tasks as generic infrastructure backlog, **not a fourth study of this piece**: obtain independently legible first-edition images for the *next* work, annotate a bounded excerpt with source/page/bar/pitch/voice, test chord-spelling and NCT boundary conditions against it, implement 2-bar phrase transformation and verify against user-approved outputs. After the Op.10 and Op.25 sequences, move to waltzes, then nocturnes. No fingering/practice research; no user-facing audio/XML/PDF.
