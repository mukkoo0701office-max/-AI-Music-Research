"""Synthetic 3/4 event audit v2; not a Chopin transcription."""
from dataclasses import dataclass
from fractions import Fraction as F

@dataclass(frozen=True)
class Event:
    witness: str
    voice: str
    onset: F
    duration: F
    pitch: int | None
    tie_prev: bool = False

@dataclass(frozen=True)
class Harmony:
    start: F
    end: F
    pcs: frozenset[int]

def audit(events, harmonies, start=F(0), end=F(3)):
    if not events or not harmonies or end <= start:
        raise ValueError('empty events/harmonies or invalid span')
    hs=sorted(harmonies,key=lambda h:h.start)
    cursor=start
    for h in hs:
        if h.start != cursor or h.end <= h.start or any(not 0<=p<12 for p in h.pcs):
            raise ValueError('harmony gap/overlap/invalid interval')
        cursor=h.end
    if cursor!=end: raise ValueError('harmony endpoint mismatch')
    by_voice={}
    for e in events:
        if not e.witness or not e.voice or e.duration<=0 or not start<=e.onset<end or e.onset+e.duration>end:
            raise ValueError('invalid event')
        by_voice.setdefault((e.witness,e.voice),[]).append(e)
    attacks=[]; segments=[]
    for key,seq in by_voice.items():
        seq.sort(key=lambda e:e.onset)
        cursor=start
        previous=None
        for e in seq:
            if e.onset!=cursor: raise ValueError('voice gap/overlap; explicit rests required')
            if e.tie_prev:
                if previous is None or e.pitch is None or previous.pitch!=e.pitch:
                    raise ValueError('invalid tie')
            elif e.pitch is not None:
                attacks.append((key,e.onset,e.pitch))
            if e.pitch is not None:
                for h in hs:
                    left=max(e.onset,h.start); right=min(e.onset+e.duration,h.end)
                    if left<right: segments.append((key,left,right,e.pitch%12 in h.pcs,e.tie_prev and left==e.onset))
            cursor=e.onset+e.duration
            previous=e
        if cursor!=end: raise ValueError('voice endpoint mismatch')
    return attacks,segments

def two_bar_transform(source,target,reprise=False):
    """Tuple fields: contour, accents, harmonic goal, bass goal, metadata."""
    if len(source)!=len(target) or len(source)!=5: raise ValueError('invalid motif')
    if source==target: return bool(reprise)
    if reprise: return False
    invariant=any(source[i]==target[i] for i in (0,1,2,3))
    substantial=sum(source[i]!=target[i] for i in (0,1,2,3))>=2
    return invariant and substantial

def tests():
    h=[Harmony(F(0),F(1),frozenset({0,4,7})),Harmony(F(1),F(3),frozenset({2,7,11}))]
    good=[Event('A','v',F(0),F(1),60),Event('A','v',F(1),F(2),60,True)]
    a,s=audit(good,h)
    assert len(a)==1 and len(s)==2 and s[0][3] and not s[1][3]
    bad=[(good,[Harmony(F(0),F(1),frozenset({0})),Harmony(F(2),F(3),frozenset({0}))]),
         ([Event('A','v',F(0),F(1),60),Event('A','v',F(1),F(2),61,True)],h),
         ([Event('A','v',F(0),F(2),60),Event('A','v',F(1),F(2),60)],h),
         ([Event('A','v',F(0),F(1),60),Event('A','v',F(2),F(1),60)],h),
         ([Event('A','v',F(0),F(3),None,True)],h),
         ([Event('', 'v',F(0),F(3),60)],h),
         ([Event('A','v',F(0),F(13,4),60)],h)]
    for ev,hs in bad:
        try: audit(ev,hs)
        except ValueError: pass
        else: raise AssertionError('invalid accepted')
    motif=((1,-1),'strong','I-V','open','editionA')
    assert not two_bar_transform(motif,((1,-1),'strong','I-V','open','editionB'))
    assert two_bar_transform(motif,((1,-1),'weak','ii-V','open','editionA'))
    assert not two_bar_transform(motif,motif)
    assert two_bar_transform(motif,motif,reprise=True)
    print('PASS: 12 synthetic cases; not source fidelity')
if __name__=='__main__': tests()
