# Chopin Research 101 — Waltz Op.69 No.1 / WN47 — witness-aware generative grammar (PARTIAL 1/3)
Date: 2026-11-25 JST. **Cumulative count 1/3** (repository history checked: Op.10 Nos.1–12, Op.25 Nos.1–12, Op.18, Op.34 Nos.1–3, Op.42, Op.64 Nos.1–3 already covered; no earlier Op.69 No.1 record found in the research/chopin directory listing). This is a repository-based count, not proof about all external activity.

## Evidence / provenance
1. Fryderyk Chopin Institute manuscript catalogue, https://chopin.nifc.pl/en/chopin/rekopis/226 : A-flat major Waltz WN47, presentation autograph dedicated to Maria Wodzińska, dated Dresden September 1835; original lost, preserved through photograph printed in Binental (1930). **Catalogue inspected; actual notation image NOT inspected.**
2. IMSLP https://imslp.org/wiki/Waltzes%2C_Op.69_%28Chopin%2C_Fr%C3%A9d%C3%A9ric%29 : 1855 French first printed appearance of No.1 (Meissonnier, plate J.M.3526, scan #400818), posthumous. Catalogue entry inspected, score image NOT inspected.
3. Henle scholarly preface https://www.henle.de/media/d3/d6/59/1690886042/0131-1690886042-sync.pdf : Fontana's posthumous editions need not coincide closely with surviving autograph versions. Secondary critical editorial source, not a primary score.
4. Chopin Online Annotated Catalogue https://chopin-os.kdl.kcl.ac.uk/aco/ : methodological bibliography for editions, not a note-level witness.
**No bar-specific pitches, chords, ties, formal boundaries, or ornament readings are asserted as verified original facts.** The word 'autograph' must not be conflated with the 1855 posthumous edition.

## Existing research audit and nonduplication
Read Op.10 No.2 studies 07/08 and study 100, plus `research/chopin/code/waltz_event_audit.py`. The old Op.10 generator's three-note cells, missing contextual NCT test, and missing two-bar sequence are documented shortcomings. Study 100 adds a synthetic event/tie/meter validator but does not establish Chopin's score readings or a complete NCT taxonomy. Do not repeat its eight tests as evidence for this work. No new code executed in this run.

## Transferable algorithm proposal (original composition only; NOT transcribed Chopin)
Represent a composition as `Witness -> Section -> Phrase -> 2-bar motive -> voice events -> harmonic spans`. Witness identity is mandatory: `autograph_photo_1835`, `fontana_print_1855`, `editorial_reconstruction` must never be silently merged. Every extracted event needs `source_id, image_page, measure, voice, onset, duration, pitch_spelling, uncertainty`; unknown fields stay UNKNOWN.

**Generative rules:**
- First design a phrase graph with arrival/departure, cadence strength, bass goal and upper melodic high point. Specify independently a melody skeleton, harmonic bass and inner-voice response; ornamentation is a later pass, not the form generator.
- For each two-bar unit encode `contour, salient-onset pattern, goal-degree, harmonic function, voice-role`. For its next unit preserve at least one musically meaningful invariant and alter a *different* dimension (e.g. rhythmic displacement plus harmonic goal). Require a genuine cadence-oriented continuation over 4–8 bars; a changed five-tuple alone is not evidence of motivic coherence.
- Place 3/4 bass and chord attacks as **optional grammar**, not a factual transcription of this piece. Keep bass and upper melodic clocks independent. When a melodic note crosses a harmony boundary, split **assessment intervals**, not the original note attack.
- Ornament choices: passing, neighbor, anticipation, appoggiatura, suspension, escape, chromatic approach, or UNKNOWN. For passing/neighbor demand stepwise approach and departure, for appoggiatura an accented dissonance and directed resolution, for suspension same-pitch preparation and tie/continuation plus downward/upward context-dependent resolution. Permit exceptions only with explicit documented reason and source context. Extended harmony must be specified; pitch-class membership alone cannot prove consonance or dissonance.
- Audit every independent voice for exact rational duration, rest gaps, ties, range, rhythmic accent, and voice crossing. Reject UNKNOWN NCT classifications in strict mode, but preserve uncertainty in source-critical mode. Separate invented compositional examples from source-derived observations.

## Test plan (NOT executed)
A. Witness-isolation: no note event from one source appears in another without explicit concordance; reject unknown source IDs.
B. Synthetic 3/4 events: check ties, gaps, held note across harmonic boundaries, repeated attacks, explicit rests, no overfill.
C. NCT positive and negative fixtures for accented appoggiatura, unaccented passing, prepared suspension, chromatic neighbor, ambiguous altered chord tones; false-positive rejection required.
D. Two-bar transformation: reject pure copy falsely labeled development; require structural invariant, controlled change, and phrase-level harmonic destination.
E. Compare same selected passage in autograph photograph and 1855 first print *only after visual access*, recording disagreements without privileging Fontana automatically.

## Critical self-audit and handoff
**PARTIAL / fails primary-score and executable-test quality gates.** Catalogue-level identification of primary witnesses is real, but original score images were not directly inspected; no note-by-note collation, no verified original harmony or formal analysis, no Python integration or executed regression, and no independent validation of user-preferred research was performed. The rules above are proposed engineering specifications, not evidence of Chopin's exact technique. Next permitted run: Op.69 No.1 **2/3**, prioritize actual primary-score image and at least one source-specific, bar-located comparison before claiming score-grounded analysis. Maximum 3 runs, then move on regardless of completion.
