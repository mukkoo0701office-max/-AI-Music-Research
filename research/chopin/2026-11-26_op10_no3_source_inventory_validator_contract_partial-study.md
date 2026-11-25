# Chopin Op.10 No.3 — source inventory and event-grammar quality gate (PARTIAL)
Date: 2026-11-26 JST. Priority: Op.10/25 before waltzes/nocturnes. No fingering or practice research.

## Count / eligibility
Op.10 No.2 is explicitly closed (>=3 runs). Prior study records 122–124 close WN28/B.21 at 3/3. GitHub code-search returned no matches even for known files, so a complete repository-wide Op.10 No.3 historical count **could not be established**. This is a **provisional Op.10 No.3 study, count not certified**; do not automatically label it 1/3 or authorize another run without a reliable inventory. Historical commit and deleted-file audits remain outstanding.

## Primary witnesses located, but NOT note-transcribed
- Chopin Online / OCVE Etudes Op.10 source index: https://chopin-os.kdl.kcl.ac.uk/ocve/browse/acview/9fe4d060d86d8603533171e2c9b682f6/ lists an autograph 10/3-A (p.1 bars 0–40; p.2 bars 41–77) and an autograph Stichvorlage 10/3,5-12-A-Stichvorlage (four pages covering bars 0–77). This is *catalogue-level direct inspection*, not examination of the actual notation.
- Fryderyk Chopin Institute facsimile catalogue: https://sklep.nifc.pl/en/produkt/77084-etudes-op-10-autograph-stichvorlage-fryderyk-chopin-museum-warsaw confirms the E-major Op.10 No.3 engraver's manuscript in Warsaw and the scholarly commentary by Irena Poniatowska.
- Morgan Library manuscript record: https://www.themorgan.org/music-manuscripts-and-printed-music/114339 describes a complete autograph sketch dated 25 August 1832, separate from the engraver's copy. Do not conflate sketch, autograph, engraver's copy, and first edition.
- A later album-leaf transcription https://www.themorgan.org/music-manuscripts-and-printed-music/115472 is explicitly in Gertrude Peppercorn's hand (1900), **not Chopin's autograph**; exclude from primary composer-event training.

## Previously implemented validator: directly inspected
Read `research/chopin/code/two_bar_event_validator_v1.py` and study 124. V1's `signature` merges voices, drops duration, compares contour signs only; `transformed` deliberately rejects constant transposition, hence cannot classify a valid transposed sequence. `validate` assumes six quarter units for two bars and disallows chord simultaneities. It also treats rest events as pitch=None but does not distinguish chord groups and tied notes crossing harmony changes. These are *code observations*, not Op.10 No.3 observations.

## ORIGINAL transferable compositional grammar (not claimed to be Chopin's exact notes)
1. Form graph: distinguish source measure IDs, performed repeat expansion, thematic anchors, cadence targets and witness variants. Compare phrase-level recurrence before generating surface density. A two-bar motif must preserve >=2 structural anchor events and a declared transformation; a three-note repeated cell alone is insufficient.
2. Voices: each event carries witness_id, page, bar, voice_id, chord_group_id, pitch spelling, MIDI pitch, rational onset and duration, tie flags, source confidence. Vertical chord simultaneity is legal across voices/chord groups; monophonic overlap within a voice requires explicit chord membership.
3. Harmonic plan: annotate intervals with source-specific harmonic function and bass goal; do not infer a key change from one chromatic note. Harmonies crossing a sustained note trigger a new dissonance inspection without inventing a fresh attack.
4. Transformation: EXACT if all voice-specific attacks/durations/pitches/anchors agree; CHROMATIC_TRANSPOSITION if a constant semitone offset with preserved rhythms; DIATONIC_SEQUENCE requires spelled scale-step invariance plus compatible harmonic motion; ORNAMENTED_RETURN requires ordered anchor matching despite additional subordinate notes. Similar contour alone => UNCLASSIFIED.
5. NCT: passing/neighbor require stepwise before-and-after context; suspension requires preparation, continuation across harmony change and resolution; appoggiatura requires new accented attack. If harmony, metrical strength or voice continuity is unknown, return UNKNOWN. Distinguish chord-tone status at attack from held-note status at harmony boundaries.
6. Rhythmic expansion: use Fraction; sixteenth = 1/4 and thirty-second = 1/8 quarter units. Validate each bar and voice separately, including rests and ties. Density expansion must preserve structural anchors and re-run harmonic/counterpoint checks.
7. Counterpoint: preserve independent bass and inner voice streams, evaluate intervals at union of attack/release/harmony boundaries, flag parallels and accented unresolved dissonance for review, not blanket rejection.

## Proposed adversarial regression cases (NOT executed)
- Multi-voice simultaneous chord accepted; same-voice overlapping independent events rejected.
- A constant +2 semitone transposition classified as transposition, not rejected; contour-preserving but unequal interval shifts rejected as sequence.
- Two-bar 3/8 and 3/4 spans handled without hardcoded six-unit default.
- A tied note at harmony boundary reclassified for consonance without reattack.
- Unknown harmony yields UNKNOWN NCT rather than false passing/suspension.
- Chord tones and rests distinguished from missing data; editorial conjectures excluded from observed-composer corpus.

## Critical quality audit and handoff
**PARTIAL / NOT VERIFIED AS CHOPIN-SPECIFIC ANALYSIS.** No primary score image was read note by note; no actual pitches, harmonies, phrase divisions or original nonharmonic notes asserted. No code modified or Python executed. Existing high-rated user works were not located in this run; compatibility remains unverified. Source-index evidence is sufficient to define a source-reconciliation plan, **not** to claim an extracted Chopin technique. The next run must first reliably inventory historical Op.10 No.3 studies and stop at 3 cumulative; then directly inspect score images and execute adversarial tests before claiming musical validation.
