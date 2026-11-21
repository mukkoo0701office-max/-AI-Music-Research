from itertools import product
# Original ii-V-I prototype, NOT a Bud Powell transcription.
chords=[{'root':2,'third':5,'seventh':0},{'root':7,'third':11,'seventh':5},{'root':0,'third':4,'seventh':11}]
melody=[[65,69,72,74,76,74,72,71],[71,74,77,76,74,71,69,68],[76,79,83,81,79,76,74,72]]
def options(c):
    return [(r,t) for r in range(36,49) if r%12==c['root'] for t in range(48,65) if t%12 in (c['third'],c['seventh']) and 7<=t-r<=24]
def score(seq):
    movement=sum(abs(a[0]-b[0])+abs(a[1]-b[1]) for a,b in zip(seq,seq[1:]))
    collision=sum(1 for v in seq for bar in melody for m in bar if abs(v[1]-m)<=2)
    return movement+collision*2
choices=[options(c) for c in chords]
assert all(choices)
best=min(product(*choices),key=score)
assert all(v[0]%12==c['root'] and v[1]%12 in (c['third'],c['seventh']) for v,c in zip(best,chords))
assert all(len(bar)==8 for bar in melody)
onsets=[(0,), (0,), (0,)]
assert all(len(x)<=1 for x in onsets)
print({'candidates':[len(x) for x in choices],'best':best,'cost':score(best),'right_hand_notes':sum(map(len,melody)),'left_hand_hits':sum(map(len,onsets)),'status':'PASS'})
