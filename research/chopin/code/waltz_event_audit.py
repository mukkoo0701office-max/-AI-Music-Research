"""Synthetic 3/4 polyphonic-event audit, not a Chopin transcription."""
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

def audit(events, harmonies, bar_length=F(3)):
    assert events and harmonies
    assert all(e.witness and e.voice and e.duration > 0 and e.onset >= 0 for e in events)
    by_voice = {}
    for e in events:
        by_voice.setdefault((e.witness, e.voice), []).append(e)
    attacks, assessments = [], []
    for key, seq in by_voice.items():
        seq.sort(key=lambda e: e.onset)
        for i,e in enumerate(seq):
            if i:
                prev=seq[i-1]
                assert prev.onset+prev.duration <= e.onset, 'voice overlap'
            if e.tie_prev:
                assert i and seq[i-1].pitch == e.pitch and e.pitch is not None
                assert seq[i-1].onset+seq[i-1].duration == e.onset, 'broken tie'
            elif e.pitch is not None:
                attacks.append((key,e.onset,e.pitch))
            if e.pitch is not None:
                overlaps=[h for h in harmonies if h.start < e.onset+e.duration and e.onset < h.end]
                assert overlaps, 'unmapped harmony'
                for h in overlaps:
                    assessments.append((key,e.onset,h.start,(e.pitch%12 in h.pcs)))
        assert seq[0].onset % bar_length == 0
        assert (seq[-1].onset+seq[-1].duration) % bar_length == 0
        assert all(a.onset+a.duration==b.onset for a,b in zip(seq,seq[1:])), 'gap requires rest'
    return attacks,assessments

def two_bar_transform(source, target, reprise=False):
    assert len(source)==len(target)==5
    if source==target:
        return bool(reprise)
    return any(a==b for a,b in zip(source,target)) and any(a!=b for a,b in zip(source,target))

def run_tests():
    h=[Harmony(F(0),F(1),frozenset({0,4,7})),Harmony(F(1),F(3),frozenset({2,7,11}))]
    e=[Event('edition-A','v1',F(0),F(1),60),Event('edition-A','v1',F(1),F(2),60,True)]
    a,ass=audit(e,h)
    assert len(a)==1 and len(ass)==2 and ass[0][-1] and not ass[1][-1]
    a,_=audit([Event('A','v',F(0),F(1),60),Event('A','v',F(1),F(2),60)],h)
    assert len(a)==2
    for invalid in [
        [Event('A','v',F(0),F(1),60),Event('A','v',F(1),F(2),61,True)],
        [Event('A','v',F(0),F(2),60),Event('A','v',F(1),F(2),60)],
        [Event('A','v',F(0),F(13,4),60)],
        [Event('A','v',F(0),F(1),60),Event('A','v',F(2),F(1),60)],
    ]:
        try: audit(invalid,h)
        except AssertionError: pass
        else: raise AssertionError('invalid event accepted')
    m=((1,-1),'strong','I-V','open','upper')
    assert two_bar_transform(m,((1,-1),'strong','ii-V','open','upper'))
    assert not two_bar_transform(m,m)
    assert two_bar_transform(m,m,reprise=True)
    print('PASS: 8 synthetic assertions/groups; no score fidelity implied')

if __name__=='__main__': run_tests()
