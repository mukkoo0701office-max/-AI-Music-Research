# Chopin Research 075 — Op.25 No.12, study 2/3: witness priority, structural-tone extraction and falsifiable event audits
Date: 2026-11-24. **Cumulative study count: 2/3 (074,075).** Status **PARTIAL; quality gate NOT passed**.

## Existing work and provenance
Directly read research 074, Op.10 No.2 research 07/08. Research 074 identifies the 3-note modulo loop, missing two-bar transformation and NCT audit in the earlier Python generator. This study does **not** repeat its six synthetic assertions or claim to have patched that generator. The original code was not executed during this run. User-approved examples have not been directly retrieved.

## Primary witnesses and what was actually verified
1. Chopin Online OCVE, Op.25 autograph/copy Stichvorlage (A&C), No.12 p.39 bars 1–20, p.40 21–40, p.41 41–60, p.42 61–83: https://chopinonline.ac.uk/ocve/browse/acview/8d87e14df522ef5e57678d651abc97b4/ . **Catalogue text verified; facsimile pixels and notes NOT inspected.**
2. Chopin First Editions Online, French-first-edition collection, No.12 p.48 bars 1–14, p.49 15–29, p.50 30–44, p.51 45–59, p.52 60–71, p.53 72–83: https://chopin-os.kdl.kcl.ac.uk/cfeo/browse/acview/81463b2d142d5d52c8dbca2bd48fde76/ . **Catalogue verified; notes NOT inspected.**
3. Additional German first-edition witness in Chopin Online: https://chopinonline.ac.uk/cfeo/browse/acview/7512aa67f1e20e5434a2ec7329c379c4/ (No.12 p.24–30, bars 1–83). **Catalogue verified only.**
4. Secondary claim that French edition uses 4/4 while autograph and German editions use cut time: https://en.wikipedia.org/wiki/%C3%89tude_Op._25%2C_No._12_%28Chopin%29 . **Unconfirmed against score images**; therefore the timing engine must retain notated meter and beat-unit as separate witness-specific attributes, never silently normalize tempo or accents.

## New reusable algorithm specification (original design, NOT Chopin transcription)
**Separation of evidence layers**: WitnessReading(source_id, page, bar, image_checked, pitch_verified, meter_verified); ScoreEvent(bar, voice, onset:Fraction, duration:Fraction, spelled_pitch, tie_group, accent, articulation, witness_id); HarmonyHypothesis(interval, bass_anchor, root, quality, evidence_status); Motive2(bar_pair, contour_invariant, anchor_sequence, transformation, cadence_target).
A pitch/duration assertion about the original is valid only if image_checked=true and note position/accidental/tie have been independently logged. Otherwise UNKNOWN. A secondary analytical description is not a substitute.

**Structural extraction before decoration**: compress each voice to salient bass attacks, metrically accented structural tones, registral apexes and harmonic-boundary held tones; retain each extracted note's provenance and uncertainty. Only then infer harmonic candidates, and distinguish chord-membership from melodic function. Avoid a naive rule that all fast notes must be chord tones.

**Two-bar grammar**: for each pair choose a bass goal and an upper registral goal, preserve an invariant (directional sweep, attack grouping or structural interval) and transform at least two of harmonic target, apex location, contour turnaround, bass trajectory or voice assignment. Permit literal repetition only with a declared rhetorical purpose; compare at phrase level, not merely pitch-class histogram. Define recurrence distance across 2/4/8 bars so long-range development can be tested.

**NCT classification**: evaluate spelled pitch against harmonic candidates and same-voice neighbors. Passing requires two adjacent step motions in same direction and a weak/intermediate placement unless explicitly justified. Neighbor returns to the departure tone. Suspension requires preparation, held/tied dissonance across a harmonic boundary, and resolution. Appoggiatura requires accented arrival and contextual resolution. Anticipation occurs before a boundary and matches the succeeding harmony. Ambiguous harmony, unverified tie or missing neighbor => UNKNOWN, not PASS. A chromatic tone that is a legitimate altered chord member must not be forcibly labeled NCT.

**Independent voices**: overlapping chord attacks share onset but remain distinct events; an arpeggiated note is not a simultaneously sounding chord merely because it belongs to a harmony. Held tones are re-evaluated when the harmony changes even if no attack occurs. A pairwise dissonance is reported with metrical, harmonic and voice-leading context; no automatic prohibition of every dissonance.

**Exact rhythm and meter**: use Fraction for attack, duration and tuplets. Store notated meter separately from metrical interpretation and pulse; a 2/2 versus 4/4 witness difference cannot be erased in accent modeling. Verify occupancy per voice, no accidental event duplication, tie continuity, and that vertical simultaneity does not increase a voice's elapsed duration.

## Test design (specified, NOT executed in this run)
- T1: two distinct witnesses disagreeing in meter must preserve both readings, not overwrite one.
- T2: a held note crossing harmony at t=1/2 must trigger a second harmonic audit without a new attack.
- T3: chromatic altered chord tone must not be mislabeled passing solely for being chromatic.
- T4: 2-bar pair with identical modulo-3 cell and no structural change is flagged; a deliberate exact reprise tagged as such is exempt.
- T5: tied chord with 3 simultaneous pitches must count one onset time, three sounding pitches.
- T6: uninspected source pitch and unsupported harmonic function must remain UNKNOWN.
- T7: 32nd and tuplet durations sum exactly per independent voice; mixed meter interpretation remains explicit.
These are acceptance criteria, **not test results**.

## Adversarial audit / unresolved
**Quality gate failed**: first-edition and manuscript page images were not directly inspected; no verified original pitches, voice-leading, harmonic functions or exact phrase boundaries; no executed Python test, no generator integration, no comparison against user-approved high-rated compositions. This is an implementable *hypothesis specification*, not evidence of Chopin-specific compositional technique. Avoid using the term 'verified Chopin model'. The next and FINAL study of this work (3/3) should prioritize facsimile inspection of a bounded passage, direct witness comparison, and executable regression fixtures; after it, move to the next unstudied work regardless of remaining gaps. No fingering/practice research.
