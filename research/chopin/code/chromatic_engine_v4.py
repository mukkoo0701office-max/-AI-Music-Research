"""Original compositional laboratory, not a Chopin transcription. No score/audio output."""
from dataclasses import dataclass
from itertools import product
PC=lambda n:n%12
@dataclass(frozen=True)
class Harmony:
    label:str
    pcs:frozenset
    bass:int
PROGRESSION=[Harmony('Am',frozenset((9,0,4)),45),Harmony('E7',frozenset((4,8,11,2)),40),Harmony('F',frozenset((5,9,0)),41),Harmony('Gm7',frozenset((7,10,2,5)),43),Harmony('Am',frozenset((9,0,4)),45),Harmony('E7b9',frozenset((4,8,11,2,5)),40),Harmony('E7',frozenset((4,8,11,2)),40),Harmony('Am',frozenset((9,0,4)),45)]
def contour(start,directions):
    out=[start]
    for direction in directions:
        out.extend(out[-1]+direction for _ in range(4))
    return out[:32]
def generate_pair(harmonies,start=69):
    best=None
    for dirs in product((-1,1),repeat=8):
        line=contour(start,dirs)
        if min(line)<60 or max(line)>90:continue
        beats=[line[k*4] for k in range(8)]
        anchor=sum(PC(p) in harmonies[k//4].pcs for k,p in enumerate(beats))
        turns=sum(a!=b for a,b in zip(dirs,dirs[1:]))
        score=12*anchor-2*abs(turns-3)-max(line)+min(line)
        cand=(score,anchor,dirs,line)
        if best is None or cand[0]>best[0]:best=cand
    assert best is not None
    return best
def audit():
    pairs=[];next_start=69
    for i in range(0,len(PROGRESSION),2):
        score,anchor,dirs,line=generate_pair(PROGRESSION[i:i+2],start=next_start)
        assert len(line)==32
        assert all(abs(b-a)==1 for a,b in zip(line,line[1:]))
        next_start=line[-1]+dirs[-1]
        pairs.append(dict(pair=i//2+1,anchor=anchor,range=(min(line),max(line)),turns=sum(a!=b for a,b in zip(dirs,dirs[1:])),end=line[-1],start=line[0]))
    jumps=[pairs[i+1]['start']-pairs[i]['end'] for i in range(3)]
    assert all(abs(j)==1 for j in jumps),jumps
    return pairs,jumps
if __name__=='__main__':
    pairs,jumps=audit()
    print('TEST_PASS',pairs,'PAIR_BOUNDARY_JUMPS',jumps)
