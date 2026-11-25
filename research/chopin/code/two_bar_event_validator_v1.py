"""Synthetic two-bar event validator; NOT a Chopin transcription."""
from dataclasses import dataclass
from fractions import Fraction as F
@dataclass(frozen=True)
class Note:
    voice:str; onset:F; duration:F; pitch:int|None; tie_in:bool=False; tie_out:bool=False

def validate(notes,span=F(6)):
    voices={n.voice for n in notes}
    if not voices: raise ValueError('empty')
    for voice in voices:
        seq=sorted((n for n in notes if n.voice==voice),key=lambda n:n.onset)
        cursor=F(0)
        for i,n in enumerate(seq):
            if n.onset!=cursor or n.duration<=0:raise ValueError('gap/overlap')
            if n.tie_in != (i>0 and seq[i-1].tie_out):raise ValueError('tie reciprocity')
            if n.tie_in and (n.pitch is None or n.pitch!=seq[i-1].pitch):raise ValueError('tie pitch')
            if n.tie_out and (n.pitch is None or i==len(seq)-1):raise ValueError('dangling tie')
            cursor+=n.duration
        if cursor!=span:raise ValueError('endpoint')
    return True

def signature(notes):
    seq=sorted((n for n in notes if n.pitch is not None and not n.tie_in),key=lambda n:n.onset)
    return (tuple(n.onset for n in seq),tuple((b.pitch>a.pitch)-(b.pitch<a.pitch) for a,b in zip(seq,seq[1:])))

def transformed(a,b):
    validate(a);validate(b)
    sa,sb=signature(a),signature(b)
    pa=[n.pitch for n in sorted(a,key=lambda n:n.onset) if n.pitch is not None and not n.tie_in]
    pb=[n.pitch for n in sorted(b,key=lambda n:n.onset) if n.pitch is not None and not n.tie_in]
    return len(pa)>=3 and len(pa)==len(pb) and sa[1]==sb[1] and pa!=pb and (sa[0]!=sb[0] or any(x-y!=pa[0]-pb[0] for x,y in zip(pa,pb)))

def tests():
    a=[Note('v',F(i),F(1),p) for i,p in enumerate([60,62,64,63,65,67])]
    b=[Note('v',F(i),F(1),p) for i,p in enumerate([60,62,65,64,66,69])]
    assert transformed(a,b)
    assert not transformed(a,a)
    assert not transformed(a,[Note('v',F(i),F(1),p+2) for i,p in enumerate([60,62,64,63,65,67])])
    t=[Note('v',F(0),F(3),60,False,True),Note('v',F(3),F(3),60,True,False)]
    assert validate(t)
    for bad in ([Note('v',F(0),F(3),60),Note('v',F(3),F(3),60,True)], [Note('v',F(0),F(3),60,False,True),Note('v',F(3),F(3),61,True)], [Note('v',F(0),F(6),60,False,True)], [Note('v',F(0),F(2),60),Note('v',F(3),F(3),61)]):
        try:validate(bad)
        except ValueError:pass
        else:raise AssertionError('bad accepted')
    print('PASS 8 synthetic assertions; no Chopin score validation')
if __name__=='__main__':tests()
