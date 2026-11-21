"""Op.10-2-inspired compositional model, not a transcription. No audio generation."""
from dataclasses import dataclass
@dataclass(frozen=True)
class Bar:
    chord:str
    root:int
    tones:tuple[int,...]
    target:int
    approach:int
PLAN=[
Bar('Am9',45,(60,64,67,71),76,-1),
Bar('E7(b9)',40,(56,62,65,71),77,1),
Bar('Am9',45,(60,64,67,71),76,1),
Bar('E7(b13)',40,(56,62,65,72),72,-1),
Bar('Fmaj9',41,(57,60,64,67),79,-1),
Bar('Dm9',38,(53,57,60,64),77,1),
Bar('E7(b9)',40,(56,62,65,71),77,-1),
Bar('Am9',45,(60,64,67,71),76,1),
]
def make_line(b):
    t=b.target; out=[]
    for k in range(4):
        anchor=t+(k%2)*2-2
        out += [anchor,anchor+b.approach,anchor]
    out += [t-3*b.approach,t-2*b.approach,t-b.approach,t]
    assert len(out)==16 and out[-1]==t
    assert t%12 in {p%12 for p in b.tones}
    return out
def analyze(plan=PLAN):
    result=[]
    for i,b in enumerate(plan):
        line=make_line(b)
        upper=[(j*120,120,p) for j,p in enumerate(line)]
        harmony=[(j*480,480,b.tones[j%len(b.tones)]) for j in range(4)]
        bass=[(0,1920,b.root)]
        for layer in (upper,harmony,bass):
            assert sum(d for _,d,_ in layer)==1920
        assert all(abs(y-x)<=3 for x,y in zip(line,line[1:]))
        result.append(dict(bar=i+1,chord=b.chord,upper=upper,harmony=harmony,bass=bass))
    assert len(result)==8 and sum(len(x['upper']) for x in result)==128
    return result
if __name__=='__main__':
    analyze()
    print('PASS: 8 bars, 128 sixteenths, voice durations, harmonic targets, melodic leaps')
