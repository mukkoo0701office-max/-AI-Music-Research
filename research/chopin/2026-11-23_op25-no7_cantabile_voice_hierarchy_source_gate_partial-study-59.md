# Chopin Research 059 — Op.25 No.7 (1/3): cantabile voice hierarchy and source gate
Date: 2026-11-23. Status: PARTIAL / NOT SCORE-VERIFIED. **Cumulative count 1/3** (repository listing shows no earlier Op.25 No.7 study; 056–058 close No.6 at 3/3). Next No.7 2/3, no more than 3 total.

## Sources and provenance
- Primary witness **catalogued, not note-read**: Chopin Online OCVE, German first edition Breitkopf & Härtel, Zaleska-Rosengardt exemplar, pp.3 (bars 1–21), 4 (22–39), 5 (40–69): https://chopinonline.ac.uk/ocve/browse/pageview/78070/ . The page metadata and witness are visible, but the image of the score did not render as readable noteheads in the accessible text view. Thus NO bar-level pitch, harmony, slur or dynamic claims are certified.
- Chopin Online source overview, including autograph/copy pp.21–23 (bars 1–23, 24–46, 47–69), and English first edition pp.1–3 (bars 1–21, 22–39, 40–69): https://chopinonline.ac.uk/ocve/browse/acview/7512aa67f1e20e5434a2ec7329c379c4/ . These are catalogue metadata, not visual comparison.
- Contextual secondary overview: https://en.wikipedia.org/wiki/%C3%89tude_Op._25%2C_No._7_%28Chopin%29 ; C-sharp minor, slow lyrical texture with prominent lower-register melody. This is a contextual description, not proof of any specific note.
- Read repository research 07, 08 and 058. 07 proposes independent fast/mid/bass clocks; 08 acknowledges repeated three-note cells and missing NCT auditing; 058 specifies half-open harmony windows, independent voices, and candidate NCT labels. This study avoids repeating their test claims and makes no assertion that their code was executed here.
- User-approved compositions were not individually retrieved/verified; no fabricated exemplar attribution.

## Distinct composition-algorithm question
How to produce **slow, expressive contrapuntal melody plus answering upper voice** without equating melodic prominence with highest pitch, while keeping harmonic rhythm separate from surface attack density? This is an ORIGINAL transferable design hypothesis, **not a transcription of Chopin's specific bars**.

### Data model
Each event: `(onset: Fraction, duration: Fraction, pitch_spelling, midi, voice_id, role, phrase_id, harmonic_window_id, accent, tie, source_status)`.
Roles: `principal_cantabile`, `answer`, `harmonic_fill`, `bass_support`. Role is independent of staff and pitch rank. The principal line may be in a lower register. Keep at least two independent melodic continuities where the design calls for a dialogue.

### Generation rules
1. **Phrase skeleton first**: plan 2+2 or asymmetric phrase spans as configurable hypotheses, cadential goals, register/energy arcs, bass functional arrival points. Do not assign these proportions to the source piece without score evidence.
2. **Primary melody**: generate structural goal tones (3rd, 7th, expressive tension or prepared appoggiatura where harmonic syntax permits), then interpolate conjunct motion, chromatic approach, delayed resolutions. Every nonchord tone has a candidate type, entry condition, resolution deadline, and ambiguity flag.
3. **Answering voice**: respond to a preceding phrase gesture with offset entrances, contour complement, or delayed imitation; avoid simply doubling the primary melody at a fixed interval. Score melodic independence using distinct onset patterns, independent phrase peaks, and nonidentical contour.
4. **Harmonic fill**: minimize attacks under important melody notes; prefer common-tone retention and inner chromatic 6–flat6–5 only when supported by the chord trajectory. An arbitrary altered note without harmonic justification fails the gate.
5. **Bass**: choose structural arrivals based on harmonic function; keep bass rhythm independently parameterized. A bass note held across a change is reaudited in the new half-open harmonic window.
6. **Two-bar development**: preserve an identifiable melodic anchor while varying at least two of rhythm, contour, register, harmonic destination, voice exchange, or counterline; distinguish genuine motivic development from literal transposition or repeated three-note loops.
7. **Density**: represent 16ths/32nds exactly as fractions, but introduce rapid notes only when a local gesture needs them; density itself is not stylistic success.

### Validation contract and exceptions
- Verify exact per-voice time coverage, overlap, tie consistency, onset grid, and active notes at every harmonic boundary.
- Classify passing/neighbor/suspension/appoggiatura as **candidates** using spelling, meter, chord membership, preparation, attack and resolution. UNKNOWN on missing harmony or continuation; do not force a label.
- Structural-reduction audit: remove ornaments and test whether principal line, bass and counterline still articulate phrase/harmony. Reject outputs that only sound coherent because of busy figuration.
- Counterpoint audit on structural sonorities: unintended parallels, crossing, registral masking, unresolved accented dissonance; allow justified exceptions by human musical review, not automatic blanket bans.
- Phrase response audit: test that counterline has distinct onset/contour and a coherent goal; never assume independent register means independent musical function.
- All of the above are **specifications only**; no new Python tests or integration were run in this session. Prior 058's nine synthetic tests are not evidence of this algorithm's correctness.

## Critical self-audit and next action
Primary source catalogue accessed but notation was **not visually read**. No verified bar-level score reduction, harmonic analysis, source variant comparison, or NCT annotations. Consequently the quality gate FAILS for completed source-grounded study. The present deliverable is an explicitly provisional algorithm design and source ledger, not a verified extraction of Op.25 No.7. At 2/3, first inspect legible score images for bars 1–21 and 22–39 and compare at least two witnesses before assigning any original-music claims. Implement a minimal voice-role/NCT/phrase-goal test with both passing and failing synthetic cases, and record execution output. Do not exceed 3 studies; unresolved items transfer forward.
