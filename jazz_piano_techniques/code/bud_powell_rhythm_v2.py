from dataclasses import dataclass
@dataclass(frozen=True)
class Event:
    tick:int
    pitch:int
    role:str
# Original 8-bar test, NOT a transcription. Eighth-note grid.
roots=[2,7,0,5,11,4,9,7]
thirds=[5,11,4,9,3,8,0,11]
right=[]
for bar,third in enumerate(thirds):
    target=60+third
    pitches=[target+2,target+1,target-1,target,target+2,target+4,target+2,target]
    right.extend(Event(bar*8+t,p,'RH') for t,p in enumerate(pitches))
patterns=[(2,),(1,5),(4,),(3,),(0,5),(2,),(1,),(5,)]
left=[Event(bar*8+t,48+thirds[bar],'LH') for bar,pat in enumerate(patterns) for t in pat]
assert len(right)==64 and len(left)==10
assert all(right[bar*8+3].pitch%12==thirds[bar] for bar in range(8))
assert all(right[bar*8+2].pitch==right[bar*8+3].pitch-1 for bar in range(8))
assert all(right[bar*8+1].pitch==right[bar*8+3].pitch+1 for bar in range(8))
assert all(0<=t<8 for pat in patterns for t in pat)
assert len(set(e.tick for e in left))==len(left)
assert len(set(e.tick for e in right))==64
onbeat=sum(e.tick%2==0 for e in left)
offbeat=len(left)-onbeat
coincidence=sum(e.tick in {x.tick for x in right} for e in left)
assert coincidence==10
assert offbeat==6 and onbeat==4
assert sum(0 in pat for pat in patterns)==1
print({'bars':8,'RH_notes':64,'LH_attacks':10,'LH_onbeat':onbeat,'LH_offbeat':offbeat,'LH_on_downbeat':1,'RH_LH_simultaneous':coincidence,'status':'PASS'})
