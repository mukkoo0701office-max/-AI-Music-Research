# Chopin Research 106 — Waltz Op.69 No.2 / WN19 — FINAL PARTIAL 3/3
Date: 2026-11-25 JST. **Cumulative work-specific run 3/3**: 104=1/3; 105=2/3; 106=3/3. Do not study this work a fourth time; move to next unstudied work after checking history.

## Evidence ledger and primary-score access
- Directly revisited IMSLP Op.69 catalogue (https://imslp.org/wiki/Waltzes,_Op.69_(Chopin,_Fr%C3%A9d%C3%A9ric)): No.2 composed 1829; 1855 Meissonnier first joint Op.69 issue, but No.2 already printed by Wildt in 1852. IMSLP lists French first-edition scan #400818, later Kullak 1880 #82860, and a modern transcription purportedly based on the Jagiellonian manuscript copy. Catalogue claims are **metadata**, not verified score readings.
- Directly read scholarly early-edition heading (https://chopinonline.ac.uk/media/documents/Op.69.heading_IG2hTjM.pdf): Wildt from 1852, Wessel 1853–60, Ewer from 1854, Meissonnier 1855–April 1856, Schlesinger 1855–64. Date ranges describe publications/states; no inference that their musical text is identical.
- Attempted to open IMSLP first-edition #400818 notation through its file link on 2026-11-25. Redirected to IMSLP anti-bot verification instead of PDF; **no notation page was seen**. Accordingly there are **zero directly verified bar-specific pitches, harmonies, voice-leading facts or manuscript variants** in this run. No unsupported Chopin-specific structural claim is made.
- Research 104 and 105 and existing `research/chopin/code/waltz_event_audit.py` directly read. Prior code uses `assert` (disabled under `python -O`), only checks harmonic intersections, and treats pitch-class membership as a proxy for consonance; `two_bar_transform` can pass a superficial one-field change. This final report does not claim those defects were patched in the repository.

## Generative architecture (ORIGINAL proposal, not an extracted Op.69 No.2 fact)
1. Build a source-independent `PhrasePlan` with phrase length, harmonic regions, bass goals, melody anchor contour, contrapuntal role and cadence target. Select a 2-bar motivic unit at phrase level rather than recycling a three-note cell.
2. A `Transform` specifies musical invariants (e.g. metrical accents and contour) and a substantive change (e.g. interval profile or harmonic goal). A literal reprise requires an explicit reprise flag; edition/witness metadata changes never count as development. Validate phrase-level goal attainment and audible rhythmic/contour relationships, not only metadata equality.
3. Realize bass and inner voices as independent rational-time partitions. Split selected structural intervals into 16th/32nd-note neighbor/passing/anticipation figures only with explicit source/target anchor and exact duration conservation. Do not indiscriminately subdivide.
4. NCT classification operates on *sounding segments* split at harmony boundaries, including ties without new attack. For each candidate store spelled pitch, local harmonic vocabulary (including extensions), accent, preceding/following voice events, preparation and resolution, and `UNKNOWN` where harmony or notation is not established. A pitch-class mismatch alone does not establish passing tone, suspension, or dissonance; a chordal ninth is not automatically an NCT.
5. Source-conditioned analysis must store witness, edition state, image/page/bar and verification status per reading. Manuscript *copies* are not autographs. Never combine editions into a single asserted Chopin text.

## Actually executed standalone regression (NOT merged into repository)
Executed Python 3 locally using `fractions.Fraction`, `ValueError` and exact partitions; **8 synthetic cases passed** (1 accepted, 7 rejected): valid contiguous harmony and same-pitch tie; rejected harmony gap; harmony overlap; changed-pitch tie; rest tie; voice gap; absent witness ID; incomplete harmony endpoint. This tests temporal integrity only, not harmonic classification, motif quality or Chopin source fidelity. Core pseudocode:
```python
if not harmonies or harmonies[0].start != 0 or harmonies[-1].end != window_end:
    raise ValueError("harmony coverage")
for left, right in zip(harmonies, harmonies[1:]):
    if left.end != right.start: raise ValueError("harmony gap or overlap")
for witness_voice in voices:
    t = 0
    for event in witness_voice:
        if event.onset != t or event.duration <= 0: raise ValueError("voice partition")
        if event.tie_prev and (event.pitch is None or previous is None or previous.pitch != event.pitch):
            raise ValueError("invalid tie")
        t = event.onset + event.duration
    if t != window_end: raise ValueError("voice endpoint")
```
The full test code was run in the working runtime, **not committed**, and the snippets above are illustrative rather than a tested copy-paste implementation.

## Critical audit and terminal handoff
**PARTIAL / primary-score quality gate FAILED.** The source catalogues were checked but original notation was inaccessible through the attempted route; no Chopin-specific note or formal discovery is certified. The isolated synthetic tests were executed, but integration with the repository generator, 2-bar musical-quality regression, NCT adversarial cases and score-based validation remain **NOT DONE**. The original request to improve the existing implementation is therefore not complete. Do not inflate the test result into a successful composition algorithm. Under the hard cumulative cap, **Op.69 No.2 is now closed at 3/3 even though incomplete**. Carry forward the *general* implementation backlog to the next work without returning to this work for a fourth study. Do not alter hourly schedule; no audio, MusicXML, user PDF, or fingering research.
