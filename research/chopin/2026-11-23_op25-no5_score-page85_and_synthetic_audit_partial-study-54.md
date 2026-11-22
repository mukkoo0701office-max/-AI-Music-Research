# Chopin Research 054 — Op.25 No.5 (2/3): directly inspected score and generative tests
Date: 2026-11-23. Cumulative count **2/3** (053 + this run). Next and final run 3/3; then Op.25 No.6. **PARTIAL: quality gate not passed**.

## Provenance and score observation
Directly viewed **printed page 85, PDF page index 20** of [PWM edition PDF](https://imslp.eu/files/imglnks/euimg/e/e5/IMSLP865891-PMLP1970-Chopin_Etude_Op_25_FR.pdf), screenshot from PDF. This is an edited printed score, **not the 1837 first edition or autograph**. [IMSLP Op.25 source catalogue](https://imslp.org/wiki/Etudes%2C_Op.25_%28Chopin%2C_Fr%C3%A9d%C3%A9ric%29) lists the Fontana copy of Nos.4–6 and 1837 French first edition. [Research 053](2026-11-23_op25-no5_source_form_and_dissonance_protocol_partial-study-53.md) established that their actual noteheads had not been inspected.

**Direct visual facts, limited to this edition and page**: At the bottom of p.85, a new section starts with printed bar number **45**, a four-sharp key signature and **Più lento**, dotted-quarter = 168, **leggiero**. The upper staff shows a continuous, beamed flowing figure with explicit triplet marking at the start; lower staff has a sustained lower line with **sostenuto** and pedal marks. At the preceding line (bar numbers beginning 40), upper and lower staves contain chromatic/contrapuntal figuration followed by a chordal punctuation and rests before the new section. **Do not infer exact harmony or every pitch from this visual inspection.** The four-sharp key signature is consistent with E major/C-sharp minor; tonal function requires separate analysis. The preceding outer texture and transition are visible, but full ABA/coda boundaries remain unverified.

## Transferable compositional model (original, not transcription)
1. **Section-specific event grammar**: A section may use short disruptive chordal attacks and adjacent tones; B section instead gives a sustained lower structural line and fast upper figuration. Generate a *voice-role map* first, then rhythms. This is a design proposal, not an assertion that every original bar follows this pattern.
2. **Contrasting density without loss of harmonic direction**: specify long-span bass/structural tones at half-note or longer spans; upper figurations can have triplet subdivisions but must aim at the next harmonic target. Keep exact rational time, and model simultaneous events separately.
3. **Dissonance evidence gate**: classify only when pitch, current harmony, metric accent, voice continuity and resolution evidence exist. A semitone alone is insufficient. Emit UNKNOWN instead of inventing appoggiatura/passing/neighbor labels. At harmony boundary, active notes satisfy onset <= t < onset+duration; re-evaluate chord membership without fabricating reattack.
4. **Two-bar motif transform**: represent (rhythm, contour, register, accent, cadence, bass trajectory). Retain at least one anchor (cadence or bass trajectory) while changing >=2 independent features. Reject transposition-only clones. This is a *candidate filter*, not a musical-quality proof.
5. **Section bridge**: prepare a pivot using diminished density, registral contraction, a cadential punctuation or rest, then switch foreground assignment. These are independent selectable strategies, not a claim of what Chopin specifically does.

## Actual Python execution — synthetic assertions only
Ran Python with fractions.Fraction; **5 assertions passed**:
- 1/16 + 1/32 + 1/32 == 1/8;
- a note active before its exclusive endpoint is inactive at endpoint;
- accented chromatic dissonance followed by semitone resolution returns APPOGGIATURA_CANDIDATE, not proven appoggiatura;
- missing resolution returns UNKNOWN;
- one-parameter motif change rejected, rhythm+contour change with retained cadence accepted as candidate.
No original Chopin notes were encoded or tested. No production generator was modified. These tests cover only simple fixtures, not complete musical or contrapuntal validity.

## Audit and unresolved
Read research 053 and research 08. Research 08's three-note-cell loops and lack of NCT audit remain deficiencies; the above proposal specifies alternative checks but does not integrate them into code. **Not yet done:** compare first-edition facsimile against edited p.85, verify exact opening wrong-note rhythm and pitch, check bar-level harmony/NCTs, independently inspect p.84 and p.86 onward, test multivoice tie/harmony boundaries on realistic data, read/execute production Python, confirm user-rated exemplar against algorithm. **Status: partial and unverified for those requirements.** On run 3/3 prioritize first-edition image comparison and real score-linked audit; then move to Op.25 No.6 even if incomplete.
