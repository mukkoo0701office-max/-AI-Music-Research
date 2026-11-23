# Chopin Research 066 — Op.25 No.9, study 2/3: attack-event and NCT boundary audit

Date: 2026-11-23. **PARTIAL / score-note verification NOT PASSED**. Cumulative Op.25 No.9 research **2/3**: study 065 was 1/3; this is 2/3. At most one further run, then move to Op.25 No.10 regardless of completion.

## Source provenance and limitations
- Primary-score inventory: IMSLP https://imslp.org/wiki/%C3%89tudes,_Op.25_(Chopin,_Fr%C3%A9d%C3%A9ric) (consulted 2026-11-23); includes original score editions. This run accessed the catalogue, **not a readable original-score page**. No particular measure, note, octave placement, articulation or chord is certified.
- Online Chopin Variorum Edition, source collection: https://chopinonline.ac.uk/ocve/browse/acview/8d87e14df522ef5e57678d651abc97b4/ (catalogue lead from study 065; not visually checked here).
- Repository studies 07 and 08 were **directly read**. Study 07 established three independent layers and acknowledged missing vertical NCT checking. Study 08 implemented 3-note cell repetition and target-note membership only; it explicitly lacked NCT, cross-voice, and 2-bar sequence checks. `research/chopin/code/chromatic_engine_v4.py` was **directly read**: 32-step lines, 8 groups of 4 directions, chord-tone anchors sampled at group starts, no per-event NCT, no explicit rhythmic rests/articulation, no independent bass generation. This is a code inspection, not a runtime validation of v4. Study 065 was directly read and its phrase/attack proposal retained.
- User-approved exemplar scores were not inspected; do not claim style validation.

## Original algorithm proposal (NOT a transcription or confirmed rule of Op.25 No.9)
### Event and phrase layers
A phrase plan stores harmonic windows, cadence target, 2-bar motivic relationships, register trajectory and independent bass arrivals. An attack event stores `onset: Fraction`, `notated_duration: Fraction`, `sounding_release`, `pitches: tuple[SpelledPitch]`, `voice_id`, `articulation`, `accent`, `tie_id`, `motif_id`. Simultaneous octave/chord tones are one event with two pitches, never falsely serialized. A rest has an explicit duration and no pitches. Articulation changes release, not the notated rhythmic sum. Phrase grammar operates on groups of attacks; pitch realization is subordinate to harmonic and contrapuntal goals.

### NCT / harmony audit
At **every onset and harmonic boundary**, inspect sounding active events using half-open intervals `[onset, release)`. Determine chord membership using spelled pitch and chord spelling; pitch-class equality alone is insufficient for enharmonic/function analysis. Propose `PASSING` only with same-voice stepwise entry and exit in a coherent direction; `NEIGHBOR` only with return to structural pitch; `SUSPENSION` only with prior consonant preparation, tie across boundary and subsequent resolution; `APPOGGIATURA` only when accent and resolution conditions hold. Without surrounding events return `UNKNOWN`, not PASS. An unresolved accent requires `REVIEW`; exceptions require explicit reason and release deadline. Check all simultaneous voices and bass, not merely sampled anchors. Chromatic embellishments may be expressive and intentionally dissonant: automatic flags are review triggers, not blanket prohibitions.

### Two-bar development, not three-note looping
Let `A` and `B` be 2-bar phrase units with attack-group signatures, accent topology, interval endpoints, register peaks, bass goals and cadence roles. Require at least one invariant (rhythmic silhouette, articulation contrast or interval endpoint) and at least two meaningful changes (register apex, accent placement, harmonic arrival, bass response, density, contour). Reject exact/transposition-only copies as **development failure** when variation was requested; allow deliberate literal reprise when phrase plan marks `REPRISE`. Test variation at 4–8 bar context to prevent local diversity from destroying thematic identity. No fixed 4-bar period or octave-group count is attributed to Chopin.

### Independent bass / voice-leading
Bass arrival schedule is generated separately from upper event groups. Track each genuine voice through overlaps, ties and handoffs. An octave chord doubling is not automatically two contrapuntal voices; assess perfect-interval parallels only for actual independent strands. Preserve structural bass destination even when upper attack density changes.

## Executed independent synthetic Python tests
Executed with Python `fractions.Fraction` in this run (not repository v4):
1. An event ending exactly at a chord boundary is NOT sounding at the boundary.
2. A held event crossing a boundary IS sounding.
3. Sixteen 1/16 events sum to one whole note.
4. Thirty-two 1/32 events sum to one whole note.
5. A true octave pitch pair is recognized.
6. A non-octave pitch pair is rejected.
7. A dissonance without neighbor context returns UNKNOWN.
8. An unaccented stepwise candidate is distinguished from an accented unresolved candidate (REVIEW).
All eight assertions passed. These are **small synthetic invariants**, not proof of a Chopin-style generator, not original-score verification, and not production integration.

## Negative tests still required
- Passing vs neighbor must inspect motion direction and structural return, not merely step size (the executed synthetic classifier is deliberately too permissive).
- Suspensions must verify preparation, explicit tie and delayed step resolution across changing harmony; attack-only scanning is inadequate.
- Exact meter sums must be per voice with rests, tuplets, ties and grace-note exceptions.
- Real two-bar phrase transformations require test fixtures with changing harmonic boundaries and bass goals; no implemented full phrase generator exists.
- Compare against a readable first-edition witness before asserting any score-specific harmonic or motivic fact.

## Quality gate and handoff
**Incomplete.** Primary score images were not obtained/read; no original measure pitches or harmonies verified. No full generator code edited; no approved-example regression. The independent Python test suite passed 8 narrow assertions but does not resolve musical correctness. Next and final No.9 run **3/3**: prioritize first-edition note image access, explicit page/bar provenance, genuinely adversarial phrase/NCT tests, and record unresolved defects. After 3/3 move to Op.25 No.10 even if these remain unresolved. No fingering, practice advice, audio, MusicXML or user PDF production.
