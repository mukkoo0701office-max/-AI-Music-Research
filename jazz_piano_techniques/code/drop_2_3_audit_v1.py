"""Original drop-2/drop-3 structural audit; not an extracted score."""
def close_for_top(pcs,top):
    below=[]
    for pc in pcs:
        n=max(x for x in range(top-11,top+1) if x%12==pc%12)
        if n!=top:below.append(n)
    return tuple(sorted(below+[top]))
def drop(close,k):
    a=list(close);a[-k]-=12;return tuple(sorted(a))
examples={'Dm9':([2,5,9,0],74),'G13':([11,5,9,4],83),'Cmaj9':([0,4,7,11],84)}
for name,(pcs,top) in examples.items():
    cl=close_for_top(pcs,top)
    assert len(set(cl))==4 and max(cl)-min(cl)<12
    d2,d3=drop(cl,2),drop(cl,3)
    assert set(n%12 for n in d2)==set(pcs)
    assert set(n%12 for n in d3)==set(pcs)
    assert max(d2)==max(d3)==top
    print(name,'close',cl,'drop2',d2,'drop3',d3)
print('PASS')
