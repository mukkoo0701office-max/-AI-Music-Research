# Chopin Research 048 — Op.25 No.3: rhythmic-source conflict and executable synthetic audits (2/3)
Date: 2026-11-22. **PARTIAL: no directly verified original score image.** Cumulative count: **2/3**, based on repository research 047 and current research/chopin directory inspection; no additional No.3 entries observed. Next maximum 3/3, then Op.25 No.4 regardless of quality.

## Source hierarchy / critical evidence
- OCVE A&C composite source index: https://chopinonline.ac.uk/ocve/browse/acview/887542e8785ef984d8321af5ed9640f3/ ; research 047 records No.3 at p.8 bars 0–20, p.9 bars 21–40, p.10 bars 41–72. **Index metadata only; the score images were not read.**
- French first edition catalogue: https://chopin-os.kdl.kcl.ac.uk/cfeo/browse/acview/81463b2d142d5d52c8dbca2bd48fde76/ ; 047 reports p.9–12. Again not direct notation evidence.
- PTNA https://enc.piano.or.jp/en/musics/20786 identifies F major, **4/4**, Allegro, Lombard/inverted dotted rhythms, distinct right/left rhythmic patterns and right-hand sixteenth-note appoggiaturas. **Secondary commentary, not a primary reading.**
- Conflicting online derivative descriptions: https://noctavepiano.com/en/free-library/chopin-etude-in-f-major-op-25-no-3/ and https://opusmotif.com/frederic-chopin-etudes/etude-op-25-no-3-f-major/ both claim **3/4**, while PTNA says **4/4**. **Meter must remain UNRESOLVED until an identified original score page is visually checked**; do not silently select one.
- https://www.ourchopin.com/analysis/etude25.html describes differing rhythmic notation between two later editions; without original edition comparison, neither is established as Chopin's definitive reading.
- A scanned early-20th-century pedagogical edition is accessible at https://s9.imslp.org/files/imglnks/usimg/a/a4/IMSLP390196-PMLP631380-breithaupt_prakt_2.pdf , but its page attribution in searchable extraction is inconsistent (contents list Op.25 No.1 where search index labels No.3). **Do not cite this as verified primary Op.25 No.3 notation.**

## Earlier repository context
Read 047, 07 and 08. 07 demonstrates independent clocks; 08 introduced target pitch validation but repeats 3-note cells, with no full nonharmonic or cross-voice audit. 047 proposed accent-mask grammar and rational timing but marked tests NOT EXECUTED. This study **tests only a small independent validation prototype** and does not claim engine integration or analysis of Chopin's actual pitches. Existing v4 integration remains pending.

## Synthetic generative model (NOT a transcription)
1. Input `meter` is a **required explicit source-tagged parameter**, not inferred from unverified commentary. Reject missing meter.
2. Independently plan harmonic windows, bass function, melody anchors, inner-voice guide tones, and surface rhythm; accent positions are `Fraction` offsets within a bar. Attach source provenance to every proposed motif.
3. Construct two-bar successor with at least two descriptor changes among accent phase, density, contour, register, and one preserved structural anchor. This is a minimum novelty gate, not proof of musical development. Prohibit pure literal three-note-cell cycling unless independently justified by form.
4. Before accepting any chromatic ornament, check previous/current/next note in same voice and active harmony. Passing = step in same direction both sides; neighbor = step out and return; accented step-resolution = *appoggiatura candidate* only, requiring further harmonic/accent checks. Suspension requires preparation, tied continuation over an actual harmonic change, and step resolution. Unknown contexts remain UNKNOWN, not PASS.
5. Vertical sonority audit must evaluate actual overlapping sounding intervals at each onset and each harmonic boundary, with context-specific exceptions logged. A fast layer cannot erase melodic anchor continuity.
6. Require explicit `source_status=synthetic` on examples; never label their notes as Op.25 No.3.

## Actually executed independent Python checks (7 assertions PASS)
Executed using Python `fractions.Fraction`:
- PASSING example 60–61–62; NEIGHBOR example 60–61–60; missing predecessor yields UNKNOWN.
- Fractional durations 1/16 + 3/16 within a bar accepted; an event at 15/16 lasting 1/8 rejected.
- Two-bar descriptor successor with changed accent phase and register and same anchor accepted; only density changed rejected.
- These are **7 individual assertions** (not 7 comprehensive music-analysis tests). The prototype was executed in the analysis runtime, **not committed as a Python module and not integrated into v4**.
- Important counterexample: a 60–61–62 chromatic passing classification is only a *candidate* if 61 is dissonant in the actual sounding harmony. A note classifier must not infer dissonance from contour alone.

## Critical quality audit
Verified: existence and content of 047/07/08; source-index references and secondary-source **contradiction**; execution of seven synthetic assertions.
Unverified: actual 1837 first-edition or composer-authorised-copy notation, meter, bar-specific accents/pitches/voice count, harmonic reductions, original-score nonharmonic classifications, full-engine integration, musical quality.
**Source-grounded quality gate NOT MET.** Next permitted No.3 study (3/3): visually inspect p.8 A&C or p.9 French first edition and log source identifier, image/page, bar range, meter and one precisely checked rhythmic event; then run an integration test with verified provenance. If inaccessible, record the failure and advance to Op.25 No.4 without a fourth No.3 run.
