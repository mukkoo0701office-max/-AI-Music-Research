# Chopin Research 102 — Waltz Op.69 No.1 / WN47: provenance-aware NCT and phrase audit (PARTIAL 2/3)
Date: 2026-11-25 JST. **Cumulative 2/3**: preceding repository study 101 establishes 1/3; this is the second. Do not run more than one further study on this work.

## Source verification and evidence ceiling
- IMSLP catalogue https://imslp.org/wiki/Waltzes,_Op.69_(Chopin,_Fr%C3%A9d%C3%A9ric) lists the 1855 French first edition of Op.69 No.1, Meissonnier plate J.M.3526, scan #400818, 12 pages. **Catalogue checked in this run; individual notation pages not opened.** This is a posthumous print, not the 1835 autograph.
- Fryderyk Chopin Institute manuscript catalogue https://chopin.nifc.pl/en/chopin/rekopis/226 is JavaScript-only in the available reader; the earlier study 101 reports a 1835 presentation autograph preserved photographically, but the manuscript photograph was **not directly inspected here**.
- Prior repository study 101 and `research/chopin/code/waltz_event_audit.py` were read directly. The latter implements exact Fraction onset/duration, tied attacks, harmony-span membership and a five-field two-bar transformation predicate. It is **not** a complete NCT classifier. No Python execution in this run.
- Consequently **no source-specific measure, pitch, ornament, formal boundary, or harmonic function is asserted**. Historical/source assertions must remain distinct from original algorithm examples.

## Specific defects found in existing code
1. `audit` accepts a harmony list that may contain overlapping spans or holes; it merely checks that each note intersects at least one span. This can mask unmapped portions of a sustained event. Require sorted, nonoverlapping, gapless harmony intervals for the entire audited musical span, or explicit UNKNOWN intervals.
2. The membership test `pitch%12 in h.pcs` cannot distinguish prepared suspension from chord extension, anticipation, accented appoggiatura or chromatic passing note. Enharmonic spelling and local harmonic function are absent. Therefore never call membership a non-chord-tone classification.
3. `two_bar_transform` accepts any shared field and any changed field, including trivial metadata differences; it does not enforce a two-bar event window, invariant identity, contour resemblance, phrase destination, or cadence progression.
4. `audit` requires the first event of each voice to start at a bar boundary; an inner voice entering after a rest must be represented with explicit rest events, but `pitch=None` is not independently typed as rest and a tied rest is not explicitly forbidden.
5. `assert` statements can be disabled by optimized Python execution; production validators should raise typed exceptions explicitly.

## Proposed implementable rules (original-composition grammar, NOT Chopin transcription)
**Witness graph**: `Witness(id, source_kind, edition_date, score_page, measure, uncertainty)`. Every extracted note has exactly one witness and optional explicit concordance edges; conflicting witnesses are preserved, not averaged.

**Harmonic segmentation**: split *analysis intervals* at every chord change, without creating new attacks. For a sustained note spanning harmonies H1 and H2, store `[(onset,H1,status1),(boundary,H2,status2)]` and mark the second segment as continuation, not reattack. The harmony coverage union must equal the event's full sounding interval.

**NCT classification** (requires previous and next sounding note in same voice, harmonic root/quality, metric accent, preparation and resolution):
- passing: nonstructural stepwise motion between distinct structural tones, consistent directional contour; chromatic spelling checked.
- neighbor: step away from and step back to a structural pitch; avoid false positive on repeated harmonic reinterpretation.
- suspension: same-pitch consonant preparation followed by dissonant continuation across boundary, then contextually directed resolution; tied or demonstrably held, never merely repeated attacks.
- appoggiatura: accented dissonance followed by resolution; do not infer merely from membership failure.
- anticipation: next-harmony structural pitch sounded before its boundary, then retained or repeated into the next harmony.
- unresolved or ambiguous: UNKNOWN with reason, not a forced label. Distinguish ninth/eleventh/thirteenth chord tones according to explicit harmony vocabulary.
In strict generation mode reject unexplained UNKNOWN; in source-critical mode retain it.

**Two-bar development**: `M=(rhythm_skeleton, contour, salient_intervals, harmonic_trajectory, cadence_goal, voice_role)`. Generate `M'` by keeping at least two *musical* invariants (e.g. accented rhythm and contour) while altering a controlled dimension (register, interval expansion, displacement, harmonic destination). Evaluate across at least four bars, not merely pairwise feature equality. A literal reprise is permitted only if form explicitly requests reprise; a transposition is not sufficient evidence of developmental purpose.

**Phrase graph**: define a 4–8 bar target with tonicization/cadence strength and bass arrival, then select two-bar transformations backwards from the goal. Do not infer these bar lengths or goals as facts about Op.69 No.1 until its score is inspected.

## Negative and positive regression fixtures to implement (NOT EXECUTED)
A. Sustain C over C-major then G-major: one attack, two harmonic assessments, second may be a chord extension or NCT depending on vocabulary.
B. Repeated C at the boundary: two attacks, must not be suspension solely because pitch is repeated.
C. D–E–F over C harmony: candidate passing E only if metric/harmonic conditions fit; E is actually chord tone in C major, so reject automatic passing label.
D. D–E-flat–D over C-major: chromatic neighbor candidate; check spelling and harmonic interpretation.
E. Phrase transform with identical musical tuple but changed source metadata: reject as development.
F. Harmony spans [0,1] and [2,3] with held note [0,3]: reject uncovered interval.
G. A late-entry voice with explicit initial rest: accept if total duration is exact; reject silent unencoded gap.
H. Prepared held note across chord boundary and stepwise resolution: suspension candidate only after checking dissonance and metric position.

## Quality gate and handoff
**PARTIAL; primary-score fidelity gate FAILED.** Actual autograph-photo and 1855 first-edition notation images not directly read; no bar-located primary-source collation; no code executed, no repository code patched, no real-score NCT test. This note is an engineering defect audit and test specification, not a verified analysis of Chopin's individual notes. The only remaining permitted run for Op.69 No.1 is **3/3**. Prioritize primary score page inspection, then source-grounded example and executable tests. If unavailable, record the block and advance to next piece after 3/3.
