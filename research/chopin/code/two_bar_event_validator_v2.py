"""Synthetic two-bar event grammar validator; NOT a Chopin transcription."""
from dataclasses import dataclass
from fractions import Fraction as F
from collections import defaultdict

@dataclass(frozen=True)
class Event:
    voice: str
    onset: F
    duration: F
    pitch: int | None
    chord_group: str | None = None
    tie_in: bool = False
    tie_out: bool = False

def validate(events, meter=(3,4), bars=2):
    span=F(meter[0]*4,meter[1])*bars
    if not events: raise ValueError('empty')
    by_voice=defaultdict(list)
    for e in events:
        if e.duration<=0 or e.onset<0 or e.onset+e.duration>span: raise ValueError('bounds')
        by_voice[e.voice].append(e)
    for voice, seq in by_voice.items():
        groups=defaultdict(list)
        for e in seq: groups[(e.onset,e.duration,e.chord_group)].append(e)
        blocks=[]
        for (onset,duration,gid), notes in groups.items():
            if len(notes)>1 and (gid is None or any(n.pitch is None for n in notes)):
                raise ValueError('invalid chord group')
            blocks.append((onset,duration,notes))
        blocks.sort(key=lambda b:b[0])
        cursor=F(0)
        for i,(onset,duration,notes) in enumerate(blocks):
            if onset!=cursor: raise ValueError('gap/overlap')
            prev=blocks[i-1][2] if i else []
            for n in notes:
                matching=[p for p in prev if p.pitch==n.pitch and p.tie_out]
                if n.tie_in != bool(matching): raise ValueError('tie reciprocity')
                if n.tie_out and (n.pitch is None or i==len(blocks)-1): raise ValueError('dangling tie')
            if prev:
                for p in prev:
                    if p.tie_out and not any(n.tie_in and n.pitch==p.pitch for n in notes):
                        raise ValueError('unresolved tie')
            cursor=onset+duration
        if cursor!=span: raise ValueError('endpoint')
    return True

def classify_motif(a,b,voice, meter=(3,4)):
    validate(a,meter);validate(b,meter)
    def notes(seq):
        return sorted((n for n in seq if n.voice==voice and n.pitch is not None and not n.tie_in),key=lambda n:(n.onset,n.pitch))
    x,y=notes(a),notes(b)
    if len(x)<3 or len(x)!=len(y): return 'UNCLASSIFIED'
    if any((u.onset,u.duration)!=(v.onset,v.duration) for u,v in zip(x,y)):
        return 'UNCLASSIFIED'
    offsets=[v.pitch-u.pitch for u,v in zip(x,y)]
    if all(d==0 for d in offsets):return 'EXACT'
    if len(set(offsets))==1:return 'CHROMATIC_TRANSPOSITION'
    return 'UNCLASSIFIED' # diatonic sequence needs spelling, key, harmonic evidence

def tests():
    a=[Event('s',F(i),F(1),p) for i,p in enumerate([60,62,64,63,65,67])]
    b=[Event('s',F(i),F(1),p+2) for i,p in enumerate([60,62,64,63,65,67])]
    c=[Event('s',F(i),F(1),p) for i,p in enumerate([60,62,65,64,66,69])]
    assert classify_motif(a,a,'s')=='EXACT'
    assert classify_motif(a,b,'s')=='CHROMATIC_TRANSPOSITION'
    assert classify_motif(a,c,'s')=='UNCLASSIFIED'
    chord=[Event('s',F(0),F(3),60,'c'),Event('s',F(0),F(3),64,'c'),Event('s',F(3),F(3),67)]
    assert validate(chord)
    assert validate([Event('s',F(i,2),F(1,2),60+i) for i in range(6)],(3,8))
    tie=[Event('s',F(0),F(3),60,tie_out=True),Event('s',F(3),F(3),60,tie_in=True)]
    assert validate(tie)
    for bad in ([Event('s',F(0),F(2),60),Event('s',F(3),F(3),61)],
                [Event('s',F(0),F(3),60),Event('s',F(0),F(3),64),Event('s',F(3),F(3),67)],
                [Event('s',F(0),F(3),60,tie_out=True),Event('s',F(3),F(3),61,tie_in=True)]):
        try:validate(bad)
        except ValueError:pass
        else:raise AssertionError('invalid accepted')
    print('PASS: 9 synthetic regression cases; NO Chopin score verification')
if __name__=='__main__': tests()
