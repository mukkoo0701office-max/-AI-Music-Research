from itertools import product
# Original eight-bar test; not a transcription.
bars=[('Dm7',(2,5,9,0),74,2),('G7',(7,11,2,5),77,7),('Cmaj7',(0,4,7,11),79,0),('Am7',(9,0,4,7),76,9),('Dm7',(2,5,9,0),74,2),('G7',(7,11,2,5),77,7),('Cmaj7',(0,4,7,11),79,0),('Cmaj7',(0,4,7,11),76,0)]
def close(pcs,top):
    assert top%12 in pcs
    notes=[max(n for n in range(top-11,top) if n%12==pc) for pc in pcs if pc!=top%12]
    return tuple(sorted(notes+[top]))
def drop(v,k):
    a=list(v);a[-k]-=12;return tuple(sorted(a))
def cost(a,b):return sum(abs(x-y) for x,y in zip(a,b))
result=[]
for name,pcs,top,root in bars:
    c=close(pcs,top)
    variants={'close':c,'drop2':drop(c,2),'drop3':drop(c,3)}
    assert all({x%12 for x in v}==set(pcs) and v[-1]==top for v in variants.values())
    result.append((name,root,variants))
states=[(0,[],None)]
for name,root,variants in result:
    next_states=[]
    for score,sequence,previous in states:
        for kind,v in variants.items():
            penalty=(max(0,48-v[0])*2)+(2 if kind=='close' else 0)
            next_states.append((score+(cost(previous,v) if previous else 0)+penalty,sequence+[(name,kind,v)],v))
    states=[min((s for s in next_states if s[1][-1][1]==k),key=lambda s:s[0]) for k in variants]
best=min(states,key=lambda s:s[0]);seq=best[1]
last=seq[-1][2];chrom=tuple(n-1 for n in last)
assert all(b-a==1 for a,b in zip(chrom,last))
dim=(59,62,65,68)
assert {n%12 for n in dim}=={11,2,5,8}
assert len(seq)==8 and [s[0] for s in seq]==[x[0] for x in bars]
print('cost',best[0]);print(*seq,sep='\n');print('chrom',chrom,'->',last,'dim',dim,'->',last)
