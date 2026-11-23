# Chopin Research 060 — Op.25 No.7 (2/3): source boundary and executable voice-role audit
Date: 2026-11-23. **PARTIAL; NOT NOTE-VERIFIED. Cumulative research count 2/3.** Previous study 059 is 1/3; repository recent commit history checked. Next is final 3/3, then move to Op.25 No.8 regardless of completion.

## Source audit
Primary catalogue: Online Chopin Variorum Edition, Breitkopf & Härtel Zaleska-Rosengardt witness, p.3 bars 1–21, p.4 bars 22–39, p.5 bars 40–69: https://chopinonline.ac.uk/ocve/browse/pageview/78070/ . **Verified:** page metadata and bar ranges in live page text. **Not verified:** legible notation image, pitches, voice entrances, specific dissonances, cadences, or original slurs. No bar-level analytical claims are made. Earlier study 059 identifies other witnesses; their notation was not directly compared here.

Repository baseline: read study 059; it explicitly separates source facts from proposed voice-role algorithms and acknowledges unverified notation. Earlier research 07/08 and 058 are summarized there; their full source/code was not re-read in this run. No user-approved exemplar was verified.

## Distinct algorithmic advance (ORIGINAL PROPOSAL, NOT CLAIM ABOUT THE SCORE)
A lower-register principal melody can remain the perceptual foreground while an upper-register answer sounds above it. Represent voice role independently from pitch, staff and instrument register. Give each voice a phrase-level goal, an attack schedule, and a harmonic dependency graph.

### Executable contract
1. Event schema: (voice, onset: Fraction, duration: Fraction, pitch, harmonic_window, phrase, role). Intervals are half-open [onset, onset+duration). A sounding note is reevaluated at every harmony boundary.
2. Assign principal, answer, bass and harmonic-fill roles before note selection. Reject the trivial shortcut 'highest note = melody'. Enforce separate attack schedules for answer and principal, except deliberately synchronized cadences.
3. Plan a two-bar source motif as a contour/rhythm/goal abstraction. The successor must change at least two independent dimensions (e.g. rhythm and goal), while retaining one recognizable anchor. This is a **design heuristic**, not an asserted Chopin rule.
4. For each dissonant event, distinguish membership test from musical classification. A pitch-class outside the chord is an NCT **candidate**, not automatically a passing tone, suspension or appoggiatura. Full classification requires spelling, attack/accent, preparation, stepwise context, harmonic rhythm, resolution and voice identity. Missing context => UNKNOWN.
5. Bass/harmony boundaries are structural: any held pitch must be checked against the *new* chord. A dissonance can be justified by preparation/resolution; a generic chord-membership-only filter must not reject every expressive appoggiatura.
6. On reduction, suppress ornament attacks and check that principal, answer and bass still have distinguishable phrase goals; if not, reject the texture as superficial density.
7. Exceptions: a deliberately synchronized answer or a stationary counterline can be artistically legitimate; flag for review rather than categorical rejection. Unresolved accented NCTs require explicit rationale or fail.

## Executed synthetic micro-tests (not Chopin transcription)
A local Python 3 script with fractions.Fraction ran five assertions successfully: (1) three independent role labels; (2) staggered principal/answer onset; (3) half-open active-note boundary behavior; (4) nonchord candidate versus chord tone in a synthetic C-major triad; (5) two of four abstract motif features changed. Output: `PASS: 5 synthetic assertions; not source score verification`.
**Limitations:** these are five minimal synthetic assertions, not a full regression suite. They do not establish NCT taxonomy correctness, musical quality, score correspondence, or integration with repository Python implementation. No repository code was modified or executed.

## Critical audit / next handoff
The main quality gate remains **FAILED**: primary score notation not visually decoded; no independent original-bar harmonic reduction; no second-witness comparison; no real-piece NCT annotations; no integration test. At 3/3 prioritize legible notation, at least one bounded source passage with witness comparison, and negative synthetic cases (bad suspension, role conflation, boundary error). If blocked, close at 3/3 with explicit unresolved handoff; never run a fourth study.
