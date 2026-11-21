# Executed structural prototype; original notes, not a transcription.
C6={0,4,7,9}; DIM={2,5,8,11}
melody=[64,65,67,68,69,71,72,71,69,68,67,65,64,62,60,64,
        67,69,71,72,74,72,71,69,67,65,64,62,60,62,64,60]
def harmonize(top):
    pcs=C6 if top%12 in C6 else DIM if top%12 in DIM else None
    if pcs is None: return None
    lower=[max(n for n in range(top-11,top) if n%12==p) for p in pcs if p!=top%12]
    return tuple(sorted(lower+[top]))
chords=[harmonize(n) for n in melody]
assert len(chords)==32 and all(c is not None for c in chords)
assert all(len(c)==4 and c[-1]==m and c[-1]-c[0]<12 for c,m in zip(chords,melody))
assert all({n%12 for n in c}==(C6 if m%12 in C6 else DIM) for c,m in zip(chords,melody))
resolutions=[(i,melody[i],melody[i+1]) for i in range(31) if melody[i]%12 in DIM and melody[i+1]%12 in C6 and abs(melody[i+1]-melody[i])<=2]
assert len(resolutions)==13
chrom=tuple(n-1 for n in chords[0])
assert all(b-a==1 for a,b in zip(chrom,chords[0]))
locked=[(m-12,)+c for m,c in zip(melody,chords)]
assert all(x[0]<x[1] for x in locked)
print('PASS','bars',8,'events',len(chords),'dim',sum(m%12 in DIM for m in melody),'C6',sum(m%12 in C6 for m in melody),'immediate_dim_to_C6',len(resolutions),'chrom',chrom,'first',chords[0])
