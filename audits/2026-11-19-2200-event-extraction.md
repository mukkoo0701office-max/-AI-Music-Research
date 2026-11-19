# 2026-11-19 22:00 MusicXML event extraction audit

Source: composition_db_update_20261119_2100.zip; original v1.1 ZIP not independently accessible.

- 13 synthetic MusicXML fixtures parsed; 52 note/rest events extracted.
- Fields: part, measure, raw onset/duration ticks, divisions, voice, pitch, rest, chord, tie tags.
- `backup`, `forward`, chord onset handled in structural extraction only.
- New original research recovered: 0; original scores directly verified: 0.
- Unrecovered per inherited index: Research 001–093 and 112–115 (97); not independently reverified.
- Limits: divisions changes not normalized, ties not merged, divisi identities not verified; no musical prohibition verdict.

Next: normalize beat positions, merge ties, validate divisi and simultaneous timelines against synthetic expected outcomes. Preserve original research IDs; do not infer missing originals.
