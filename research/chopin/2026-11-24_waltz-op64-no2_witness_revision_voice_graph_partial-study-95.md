# Chopin Research 095 — Waltz Op.64 No.2: witness-sensitive revision and voice-event grammar (1/3)
Date: 2026-11-24 JST. **Cumulative count: 1/3 for Op.64 No.2**. Repo directory inspection found no earlier Op.64 No.2 study; Op.64 No.1 studies 092–094 explicitly closed at 3/3. This count is based on repository filenames and recent handoff, not an exhaustive audit of all historic execution logs. Étude priority remains globally higher; the established running sequence has reached the waltzes.

## Source hierarchy / what was actually checked
1. Chopin Online OCVE work catalogue, https://chopin-os.kdl.kcl.ac.uk/ocve/browse/acview/cc73ab49cc447fb5e57d010fadb5cd32/ : explicitly lists **64/2–A-sk** autograph sketch (p.[1], bars 1–96), **64/2–A-presentation** (p.[1], bars 1–128), and an opus-level engraving autograph. These are catalogue *bar-span metadata*, not proof of the final performance order or full work length. The public HTML view did not yield legible musical notation.
2. Henle critical comments (editorial secondary witness analysis, inspected directly): https://www.henle.de/media/cd/c4/c0/1697725757/0348-1697725756-sync.pdf (PDF comments p.108, lines corresponding to web-extracted 23–37). Sources A1 Paris, A2 Basel, F Brandus plate 4743, D Breitkopf & Härtel plate 7716. Editor reports A1 nearer draft, A2 engraving model for F, with A2+F as editorial basis. **This is an editor's report, not independent image verification**.
3. Chopin Online first-edition provenance overview: https://www.chopin.pl/first_editions.en.html . The French, German and English editions are not automatically independent witnesses; opus 63–65 have special dependency relationships.
4. Facsimile publisher's description (secondary): https://www.omifacsimiles.com/brochures/chop_wal64%2C2.html describes a Rothschild presentation autograph and Basel engraver's copy, and differences in upbeat, middle section and recapitulation. Claims require direct comparison before being coded as note-level fact.

## Concrete edition-sensitive issues from Henle comments (NOT direct score reading)
- Bar 3 and analogues: grace-note slurs inconsistently present in F, absent A1/A2/D. Algorithm must store **ornament attachment as witness-specific**, not assert an invariant slur.
- Bars 27–28 (also 155–156): C-sharp2-to-C-sharp2 tie reported in A1 but not A2; do not confuse tie (one sounding onset) with repeated pitch (two onsets).
- Bars 42, 45: lower-staff chord tones differ among editions, and A1/A2 legibility is uncertain; mark as variant/ambiguous, do not choose notes by presumed tonal plausibility.
- Bars 66–67 and analogues: E2-to-E2 tie reported in D but absent A1/A2/F. Timing of note onsets depends on witness.
- Bar 92: poco ritenuto reported only in F. This is a *source-specific performance marking*, not a universal formal boundary.
- Bars 8–12 and 136–140: phrasing reportedly inconsistent across witnesses; a phrase generator should represent uncertain segmentation rather than invent a definitive cadence.
These bar/pitch statements are **attributions to the inspected Henle critical commentary**, not verified readings of autograph or first-edition images.

## Reusable compositional grammar — original proposal, not a Chopin transcription
**Data model**: Witness(id, lineage, certainty); Event(voice, onset:Fraction, duration:Fraction, spelled_pitch, event_type, tie_id, source_anchor); Harmony(start,end,function,spelling); Motif(2-bar structural anchors, rhythm profile, interval contour, cadence_goal); Form(section, return_of, variant_transform). Use exact rational clock: 3/4 bar = 3 quarter units, 12 sixteenths or 24 thirty-seconds. A grace event must specify timing policy (pre-beat / on-beat / unspecified) and not silently add duration.

**Voice graph**: independently schedule bass, accompaniment and melody. Chord attack times, bass roots and melodic upbeats are not forced onto one onset grid. Create a sounding-interval index; at each harmonic boundary inspect held notes even when no new note is struck. Store tie semantics separately from phrase slurs and portato. A tied note cannot be treated as a new melodic attack; a phrase slur cannot be treated as prolonging duration.

**Two-bar transformation**: generate phrase skeleton before ornamentation: anchors A=(role,scale_degree,metric_weight), B=transform(A, preserve=[cadential_goal or contour], change=[rhythm/register/harmonic-route]). Reject four identical 3-note cells unless explicitly reprise. Distinguish **sequence** (transposition plus functional reinterpretation) from literal repetition; check target scale-degree relative to local harmony, not just MIDI semitone distance. A and B here are hypothetical *original* objects, not verified Chopin sections.

**Dissonance**: every note carries proposed label chord-tone/passing/neighbor/appoggiatura/suspension/anticipation/unknown. Passing: stepwise movement between structural anchors in one direction, checked with diatonic spelling; neighbor: depart and return; suspension: consonant preparation, tied retention into a new harmony and stepwise resolution; appoggiatura: accented nonchord event and plausible resolution. Exception: unclassifiable but intentionally colored dissonance remains UNKNOWN pending human review, not auto-PASS. Split held notes at harmony changes for vertical audit, retaining single onset and identity.

**Form/revision**: represent each source as its own form graph. Do not merge the Rothschild presentation copy and Basel engraver's copy into one imagined 'original'. Generate alternate developmental paths by varying length, reprise and accompaniment density while preserving cadential targets; only claim a Chopin-specific revision pattern after image-to-image score comparison.

## Existing implementation audit
Directly fetched and read `research/chopin/code/chromatic_engine_v2.py`, `chromatic_engine_v4.py`, research 07/08 and `feedback/USER_PREFERENCES.md`.
- v2: `make_line` explicitly repeats a three-note [anchor,anchor+approach,anchor] cell four times; only final target pitch class, duration and adjacent leap are checked. No dissonance, phrase, edition or bar-boundary audit.
- v4: `contour` expands each +/-1 direction into four steps, choosing an 8-direction sequence by a crude anchor/turn score. Two-bar timing exists but **does not constitute validated motif sequence**; no spelled-pitch nonchord-tone classifier. Its `contour` uses an `extend` generator referring to the last element dynamically; test behavior before relying on this as a fixed four-step motif transformation.
- Feedback: prefer natural functional progressions, common-tone and chromatic inner-line resolutions, distinct density arcs, and avoidance of gratuitous chromatic clashes. These are user preference constraints for **future original generation**, not Chopin historical facts.

## Falsifiable validation plan (NOT EXECUTED in this study)
1. For each witness, independently transcribe an image-anchored small passage, preserve image coordinates/page and uncertain readings.
2. A/B test tied-vs-rearticulated C-sharp at 27–28 and E at 66–67 using a source-labelled onset list; compare event counts, not just sounding pitch.
3. Synthetic negative fixtures: a phrase slur mistaken for a tie; sustained dissonance across a harmony boundary; neighbor mislabeled as passing; repeated 3-note cell passed off as sequence; 32nd-note bar totaling >3 quarters.
4. Require independent score comparison and manual musical review before declaring the algorithm Chopin-grounded.

## Quality gate and handoff
**PARTIAL — source-image and execution gates FAILED / not attempted.** Primary catalogue and scholarly editorial comments were inspected; **no legible primary score image was directly compared**. No actual musical event was transcribed. No Python code was run, no generator integration or music-quality test performed; do not count this as a passed implementation. The major new finding is that witness-specific *ties and ornaments alter the event graph*, so the algorithm must not flatten variants into a single note stream. Future pass 2/3: obtain legible A2/F images and implement/test witness-specific tie semantics. Future pass 3/3: independent verification or explicit unresolved handoff, then close this work permanently. No score, XML or audio deliverables.
