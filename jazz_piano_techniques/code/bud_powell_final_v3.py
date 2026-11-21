from dataclasses import dataclass
@dataclass(frozen=True)
class Note:
    onset:int
    duration:int
    pitch:int
    role:str
# Original 8-bar composition prototype; not a Bud Powell transcription.
roots=[2,7,0,5,2,7,0,0]
thirds=[5,11,4,9,5,11,4,4]
sevenths=[0,5,11,3,0,5,11,11]
patterns=[(0,2,3,5,7),(1,2,4,6),(0,1,3,4,7),(1,3,5,6),
          (0,2,4,5,7),(1,2,3,6),(0,1,4,6),(2,3,5)]
contours=[(-2,-1,0,2,0),(2,1,0,-1),(1,0,3,2,0),(-1,0,2,0),
          (2,1,0,3,0),(-2,-1,0,2),(1,0,-1,0),(-1,0,2)]
assert [len(x) for x in patterns]==[len(x) for x in contours]
rh=[]
for bar,(ons,shape) in enumerate(zip(patterns,contours)):
    base=60+thirds[bar]
    for t,d in zip(ons,shape):
        rh.append(Note(bar*8+t,1,base+d,'RH'))
left_onsets=[(2,),(0,5),(4,),(3,),(0,5),(2,),(2,),(5,)]
lh=[]
for bar,onsets in enumerate(left_onsets):
    for t in onsets:
        lh.append((bar*8+t,(36+roots[bar],48+sevenths[bar])))
assert all(0<=t<8 for pat in patterns for t in pat)
assert all(0<=t<8 for pat in left_onsets for t in pat)
assert all(len(set(x))==len(x) for x in patterns+left_onsets)
assert all(p[0]%12==roots[on//8] and p[1]%12==sevenths[on//8] for on,p in lh)
assert all(any(n.onset//8==bar and n.pitch%12==thirds[bar] for n in rh) for bar in range(8))
assert len(rh)==34 and len(lh)==10
rh_ticks={n.onset for n in rh}
synced=sum(on in rh_ticks for on,_ in lh)
assert synced==7
assert len(set(n.pitch for n in rh))>10
assert len(set(tuple(x) for x in patterns))==8
assert len({n.onset//8 for n in rh})==8
print({'bars':8,'RH_notes':len(rh),'LH_chord_attacks':len(lh),'simultaneous':synced,'simultaneous_ratio':round(synced/len(lh),3),'different_RH_rhythm_patterns':8,'status':'PASS'})
