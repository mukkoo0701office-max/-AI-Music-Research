# Passing Chords 007 (3/3): practical 8-bar comparison
# Full runnable version created locally as build_passing007.py; study specification below.
# 4/4, 72 BPM, melody E5 E5 F5 E5 E5 E5 F5 E5, one whole-note per bar.
# Stable bars: Cmaj9 Am9 Dm9 Cmaj9 Cmaj9 Cmaj9/E Dm9 Cmaj9.
routes={
 0:{},
 1:{0:['E7b9'],2:['Db9'],4:['Fm6'],6:['G13']},
 2:{0:['Bm7b5','E7b9'],2:['Ab7','Db9'],4:['Fmaj7','Fm6'],6:['Dm9','G13']}
}
# For 1 detour, approach on beat 4; for 2 detours, beats 3 and 4.
# Melody held unchanged; bass + four-note LH, pedal CC64 reset at every change.
# XML parts: melody, voicings, bass. Acoustic grand piano soundfont TimGM6mb.sf2.
# Audit: 8 bars each part, 16 divisions per bar (4/4), 48/68/88 MIDI notes,
# 24/32/40 CC64 events, 8/12/16 chord events, all variants generated and rendered.
# Limitation: independent nonchord-tone resolution audit and musical listening
# evaluation NOT performed. Static long-note melody intentionally exposes
# clashes that should be assessed, not automatically called successful.
