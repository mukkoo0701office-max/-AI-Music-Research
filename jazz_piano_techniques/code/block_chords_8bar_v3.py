"""Block chord final study: guide-tone constrained four-way close candidate selection."""
from itertools import combinations
CHORDS = [
 ('Dm9', {2,5,9,0,4}, {5,0}, 4),
 ('G13b9', {7,11,2,5,8,4}, {11,5}, 9),
 ('Cmaj9', {0,4,7,11,2}, {4,11}, 2),
 ('A7alt', {9,1,7,10,5,8}, {1,7}, 10),
 ('Dm9', {2,5,9,0,4}, {5,0}, 4),
 ('G7b9', {7,11,2,5,8}, {11,5}, 8),
 ('Cmaj9', {0,4,7,11,2}, {4,11}, 2),
 ('C6/9', {0,4,7,9,2}, {4,9}, 2),
]
def candidates(pcs, guides, top):
    pool = [n for n in range(top-11,top) if n%12 in pcs]
    for triple in combinations(pool,3):
        notes=(*triple,top)
        if len(set(n%12 for n in notes))!=4: continue
        if not guides.issubset({n%12 for n in notes}): continue
        if notes[0]<48: continue
        if any(b-a==1 and a<60 for a,b in zip(notes,notes[1:])):continue
        yield notes
def cost(a,b):
    return sum(abs(x-y) for x,y in zip(a,b)) + 3*sum(abs(x-y)>7 for x,y in zip(a,b))
voicings=[]
for name,pcs,guides,top_pc in CHORDS:
    top=top_pc+72 if top_pc<5 else top_pc+60
    opts=list(candidates(pcs,guides,top))
    assert opts, (name,top)
    selected=min(opts,key=lambda n:cost(voicings[-1],n) if voicings else sum(n))
    voicings.append(selected)
    assert selected[-1]%12==top_pc and guides.issubset({x%12 for x in selected})
    assert selected[-1]-selected[0]<12
for i,(chord,notes) in enumerate(zip(CHORDS,voicings),1):
    print(f'{i}: {chord[0]:8} {notes} pcs={tuple(x%12 for x in notes)}')
print('PASS 8 chords; top melody, guide tones, unique pitch classes, close spacing, low semitone filter')
print('total voice motion:',sum(cost(a,b) for a,b in zip(voicings,voicings[1:])))
