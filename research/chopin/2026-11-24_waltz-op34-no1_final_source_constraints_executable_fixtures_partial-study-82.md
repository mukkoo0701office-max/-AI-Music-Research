# Chopin Research 082 — Waltz Op.34 No.1 final (3/3): source-variant constraints and tested synthetic fixtures

Date: 2026-11-24. **Cumulative work-specific count: 3/3 (080, 081, 082). HARD STOP: no fourth study.** Status: **PARTIAL — original score facsimile not note-verified**.

## Provenance and evidence boundaries
- Directly fetched and read repository studies 080 and 081, which establish witness inventory, notation ambiguity and prior unexecuted test specifications. 080 says historical Python was checked; 081 reports a 404 for a purported code path. Therefore no claim of current generator inspection/integration.
- Directly inspected **page image** of the *National Edition Waltzes, Source Commentary / Abridged*, printed p.6 (PDF p.5), and extracted performance/source commentary text from PDF pp.1,4–5. This is **editorial source commentary**, not the original autograph or first-edition score image. https://www.chopin-nationaledition.com/wp-content/uploads/2022/06/waltzes_commentaries.pdf
- The printed p.6 page shows Op.34/1 editorial remarks on bars 262/264: chromatic melody independent of harmony, FE primary text and A variant; bars 272–273 FE lineage omission of a tie; bars 303–304 autograph's deleted intermediate bars and printing confusion. These are source-*commentary* observations, **not a note-by-note independent reading**.
- The commentary's performance section p.1 notes that bars 67–68 and analogues admit timing ambiguity for runs; at bars 163–164 and 167–168 optional variants have distinct rhythmic realizations. Treat metrical anchor and realization as separate representations. The commentary also discusses bars 300–305 sustained harmony/pedaling; this is NOT evidence for automatically sustaining all chord tones in the composed score.
- No unverified pitch spelling or functional-harmony Roman numerals are asserted as original-score facts. User-approved reference scores not retrieved this run.

## Transferable generative grammar (original proposal, not Chopin transcription)
**Form graph:** Episode -> phrase pair -> harmonic destination -> bass trajectory -> voice-leading skeleton -> ornament layer. Reprise links may preserve a melodic/rhythmic identity while changing the harmonic destination; revision-deleted bars remain archival metadata, not active event nodes.

**Witness graph:** `Witness -> Version -> BarMap -> Event`; editorial substitutions and errors must be labeled by source and editorial status. Bar-number analogues are not proof of pitch-identical passages. A source note is verified only with direct legible original score evidence.

**Two-bar transformation:** Each unit stores `cadence_target, bass_plan, accent_grid, contour, register_envelope, rhythmic_signature`. Require at least one retained salient invariant and one consequential variation unless marked as intentional exact reprise. A three-note pattern repeated with no harmonic/formal purpose is flagged, not auto-prohibited.

**Harmony / dissonance:** Assign harmonic spans and independent sustained voices first; check all sounding notes at every onset and harmony change. `PASSING` requires directional stepwise approach/departure, `NEIGHBOR` return, `SUSPENSION` documented prior consonance and actual sustain across harmony change plus resolution, `APPOGGIATURA` accent and context. Simple classifiers return CANDIDATE, never certify these from pitch alone. A melodic chromaticism independent of accompaniment is allowed and must not be silently diatonically repaired. Slurs, ties, pedal and ornaments are distinct tokens.

**Ornament / exact time:** use rational onset/duration; unmeasured grace notes have explicit anchor and performance policy, and do not consume the notated metrical sum. 3/4 allows 6 eighths, 12 sixteenths, or 24 thirty-seconds per bar, with concurrent independent voices. A trill is not automatically interchangeable with a mordent. Accent position and source-specific grace-note placement require separate fields.

## Actually executed checks — 2026-11-24
Executed a standalone Python `fractions.Fraction` script in the working runtime. **8 assertions passed**: exact 3/4 occupancy with 6 eighths, 12 sixteenths, 24 thirty-seconds (3); passing candidate, neighbor candidate, sustain-based suspension candidate, unresolved dissonance (4); two-bar rhythm identity with changed cadence goal (1). All pitches and phrases in these fixtures are **synthetic original examples**; they do not validate Op.34/1's notes, actual chord progressions, original notation or any existing repository generator. This isolated classifier is intentionally weaker than the complete musical audit: suspension must also check preparation and harmonic boundary; passing requires metrically contextual confirmation.

## Critical self-audit
**Failed final quality gate:** no direct original facsimile note-by-note reading; no verified original-score harmony/voice-event transcription; no existing generator integration; no user-approved output comparison. Source commentary image inspection is NOT primary score-image inspection. The eight tests prove only local arithmetic and classification predicates, not musical quality or source fidelity. Prior reports contain an inconsistent account of the historical Python path; resolve as a cross-cutting tooling task, **not a fourth Op.34 No.1 study**.

## Handoff
Stop Op.34 No.1 at **3/3** regardless of incomplete work. Next: **Waltz Op.34 No.2 (1/3)** after checking history. Carry forward reusable source-variant schema, witness-qualified tie/slur distinctions, exact-time scheduler and contextual non-chord-tone audit; do not reopen Op.34 No.1 as its own research target. Existing hourly schedule unchanged.
