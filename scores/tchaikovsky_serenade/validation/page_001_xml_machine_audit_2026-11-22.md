# Page 1 checkpoint — machine audit of existing MusicXML (2026-11-22)

## What was actually checked
Read the existing local file `serenade_page1_working_excerpt.musicxml` as XML. It contains **only one part (Violin I)** and **four measures (1–4)**. Each measure sums to 30240 MusicXML divisions (6/8 at divisions=10080) when chord notes are not double-counted.

## Existing draft pitch data (NOT visually verified)
- m1: C6 dotted quarter; [C5,B5] dotted quarter
- m2: [C5,A5] dotted quarter; [C5,G5] eighth; [C5,A5] eighth; C6 eighth
- m3: [G4,G5] dotted quarter tied to [G4,G5] quarter; F5 eighth
- m4: [B4,E5] dotted quarter; [D4,F5] eighth; [D4,F5] eighth; [B4,A5] eighth

## Unresolved blockers
Prior GitHub audit notes contradict each other about m1 pitch and tempo unit. Passing a duration check is NOT evidence that the notes match the source. The existing excerpt has no Violin II, Viola, Violoncello or Double Bass; the PDF page has 20 measures and five parts. It also lacks the page's full expression marks. Therefore **0/20 measures fully verified**. Do not release this draft as a finished page.

## Progress accounting
- Drafted: 4/20 measures of Violin I only (20% of one part, approximately 4% of 100 part-measures).
- Fully source-verified: 0/20 complete measures.
- Next action: calibrate staff positions and verify m1 pitches on all five staves, with a rendered MusicXML comparison.
