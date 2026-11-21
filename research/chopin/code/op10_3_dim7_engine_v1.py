"""Original harmonic engine inspired by Op.10/3, not a transcription. No audio/score output."""
PC=lambda x:x%12
def dim7(root): return tuple(sorted({PC(root+3*i) for i in range(4)}))
def run():
    sets=[dim7(r) for r in range(12)]
    assert len(set(sets))==3
    assert all(len(s)==4 for s in sets)
    assert [dim7(x) for x in range(3)]==[(0,3,6,9),(1,4,7,10),(2,5,8,11)]
    chords=[[60+r+3*i for i in range(4)] for r in (0,1,2)]
    assert all(all(PC(x) in dim7(r) for x in chord) for r,chord in zip((0,1,2),chords))
    assert all(all(b-a==1 for a,b in zip(chords[i],chords[i+1])) for i in (0,1))
    assert PC(68)==8 and PC(69)==9 and PC(65)==5 and PC(64)==4
    return {'unique_dim7_pitch_class_sets':3,'chromatic_transpositions':2,'voice_motion_semitones':[1,1,1,1],'resolution_examples':['G#4->A4','F4->E4'],'status':'PASS'}
if __name__=='__main__':print(run())
