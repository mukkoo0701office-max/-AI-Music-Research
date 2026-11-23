# Chopin Research 079 — Waltz Op.18, final study 3/3: variant-aware structural generation and harmony audit

Date 2026-11-24. **Cumulative Op.18 research: 3/3** (077, 078, 079). **CLOSED** regardless of incomplete verification. Next eligible work: Op.34 No.1, subject to checking existing study counts. No fourth Op.18 study.

## Evidence and provenance

Read GitHub studies 077 and 078 directly. Both report missing direct score-image pitch verification and generator integration. Their proposals are not silently promoted to verified Chopin facts. Historical studies 07/08 and Python generator were NOT fetched in this run; user-approved reference examples NOT accessed. Repository code-search for Op.18 returned no results, so no global claim of absence is justified.

**Critical editorial source checked directly 2026-11-24:** Jan Ekier / Paweł Kamiński, National Edition Waltzes performance and abridged source commentary, https://www.chopin-nationaledition.com/wp-content/uploads/2022/06/waltzes_commentaries.pdf , PDF pp.1,3–4. This is an authoritative *editorial report on primary witnesses*, not direct examination of the handwritten/engraved score. Original witness image and note-by-note transcription remain **UNVERIFIED**.

### Source-specific facts reported by the critical edition (not independent score reading)

- Earlier autograph AI groups what became final-version bars 5–68, 69–116, 117–164 as separately numbered waltzes and lacks a coda; AII also lacks a coda. Final autograph A was the basis for FE1, corrected by Chopin. FE2 includes further authorial corrections. The editors choose FE2 as their principal basis compared against A and AII (source commentary pp.3–4).
- **Bar 28 L.H.**: A and its descendant early prints have a quarter-note A-flat (editorial typography must be checked in facsimile for octave); the editors instead adopt the longer rhythmic value from analogous bars 60 (A) and 212 (FE2 proofs). This is a **source-dependent duration decision**, not an instruction to lengthen all basses (p.4).
- **Bars 12, 36, 44, 165, 167, 169 L.H.**: bass-related slurs derive from annotated pupils' copies FED' and, in 165–169, FEX. Editors warn that a slur at bar 66 might be mistaken for a tie (p.4). **Slur != tie**; sustained sounding pitch must not be inferred solely from phrasing.
- **Bar 224 L.H. second quarter**: FE2 proof correction changes a chord tone from E-flat to D-flat as reported by editors (PDF extraction omits some accidentals; do not assert exact pitch spelling until facsimile verified). **Bar 274 L.H. beats 2–3**: revisions to chord membership in A and FE1/FE2 demonstrate that accompaniment voicing can change while rhythmic function persists (p.4). Pitch classes and octaves unverified here.
- **Bar 304** was inserted in A but omitted by engraver and restored at FE1 final proof; GE and EE omit it (p.4). This is a **bar-index alignment hazard**, not an instruction to insert a bar in any score without witness metadata.
- **Bars 165–172**: the edition's performance commentary describes alternating two-bar expressive pairs; this is editorial interpretation, not proof of precise harmonic alternation (p.1).
- **Bar 118 and analogues**: grace-note timing may be anticipatory or on the beat; the anchor and accompaniment beat grid remain fixed (p.1).

## New reusable algorithmic contribution (original proposal; NOT a transcription)

### 1. Witness-aware graph and alignment

Store each source as `Witness(id, lineage, date, authority, bar_map, event_variants)`. Do not collapse FE1/FE2/GE1/EE1 into a generic 'first edition'. An event stores `witness_id, local_bar, canonical_section, voice, onset_fraction, duration_fraction, pitch_spelling, evidence_type, confidence`. Map each witness's bar sequence onto section identities via explicit edit operations (INSERT, DELETE, REPLACE, ALIGN). At bar 304, a missing GE/EE bar must produce an alignment gap, not a spurious chromatic or formal change. Preserve original bar numbers in every cited fact.

### 2. Form before texture

Construct an episode graph with nodes for thematic inventory, transitions, reprises, and coda. Different witnesses can instantiate different graphs; the algorithm must not treat early three-part numbering and final integrated work as identical formal structures. Generate long-range cadential destinations and motif genealogy first; generate accompaniment attacks only after the structural plan.

### 3. Voice-leading with witness-dependent harmony

Each harmonic window has a structural bass, chord-member inventory, tendency tones and cadential goal. Separate the **harmonic function** from **voicing** and from **notated duration**. The editorially documented bar 274 chord changes provide a concrete counterexample to assuming that the same recurring accompaniment rhythm implies fixed chord membership. For source-grounded classification, an unreadable pitch is UNKNOWN and blocks chord-tone/non-chord-tone assertions.

### 4. Non-chord-tone classification and boundary reevaluation

For each event overlapping harmonic window H, record structural voice role, metric accent, approach and resolution intervals, preparation/tie evidence, and spelling. Candidate PASSING requires stepwise connection in same direction between anchors; NEIGHBOR returns to anchor; SUSPENSION requires genuine sustained sounding pitch across harmony boundary and resolution; APPOGGIATURA requires accented dissonance with plausible resolution; otherwise UNKNOWN. Reevaluate every sounding event at each harmonic boundary. Phrasing slur alone cannot prove a suspension or bass hold. Flag rather than auto-correct unresolved chromatic notes or pedal conflicts.

### 5. Two-bar motif transformation

`Motif(id, contour_skeleton, rhythmic_anchors, cadence_target, bass_path, register, ornament_density, genealogy)`. Compare successive 2-bar units on at least two independent structural axes (e.g. bass goal + phrase apex), unless the passage is explicitly tagged reprise. Do not merely repeat a three-note cell. In an **original, invented example**, A uses ascending structural 3rd→7th→9th over tonic-to-predominant bass; B preserves the rhythmic signature but shifts apex and resolves over a dominant-to-tonic bass. This example is NOT an Op.18 transcription and is not validated against its exact harmony.

### 6. Duration and ornament integrity

Use integer ticks at common denominator 32 or rational fractions for 16ths/32nds; separate grace events from metrical durations. Validate each voice's bar occupancy and allow independent overlapping bass/chord voices. Alternative grace timing must not shift structural anchors. Require explicit tied-note evidence for notated sustains.

## Executed checks (limited, synthetic; NOT musical validation)

Six JavaScript assertions executed in the tool runtime: witness ordering representation; explicit FE1/GE1/EE1 bar-presence flag; independent bass overlap with chord attacks; detection of exact repeated three-note arrays; crossing of a harmony boundary by held event; 8 subdivisions of 1/8 = 1 quarter unit. **6/6 passed**, but these are trivial structural sanity checks, not tests of a Python generator, facsimile, exact source variants, harmony, or compositional quality. They do NOT validate the historical assertions.

## Critical self-audit / unresolved handoff

**PARTIAL / FAIL finished-quality gate.** No directly readable primary score image inspected; no original pitches or bar-by-bar harmonic analysis independently verified. Exact accidentals/registrations in editorial PDF text extraction are potentially degraded. Historical Python source, user-approved high-rated compositions, and integration/regression tests not retrieved. No claim of generator improvement or verified source-note transcription. Transfer general *witness-alignment*, *slur-vs-tie*, *harmonic membership revision*, *motif genealogy*, and *bar-occupancy* test requirements to next distinct work; **do not run Op.18 a fourth time**. No fingering, practice, MusicXML, PDF, or audio production.
