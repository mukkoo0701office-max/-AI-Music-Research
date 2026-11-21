"""Original structural tests of rootless minor iiø–V7alt–i, not a transcription."""
SOURCE=(62,65,69,73)  # Bø9 D F A C#
DOM=(62,65,68,72)     # E7(b9,b13) D F G# C
TONIC7=(60,64,67,71) # Am9 C E G B
TONIC6=(60,64,66,71) # Am6/9 C E F# B
def pcset(notes):return {n%12 for n in notes}
def valid(notes,root,required):
    pcs=pcset(notes)
    return len(notes)==4 and list(notes)==sorted(notes) and {(root+i)%12 for i in required}<=pcs and root%12 not in pcs
def move(a,b):return tuple(y-x for x,y in zip(a,b))
def cost(a,b):return sum(abs(x) for x in move(a,b))
def transpose(v,k):return tuple(n+k for n in v)
def run():
    for k in range(12):
        s,d,t7,t6=(transpose(v,k) for v in (SOURCE,DOM,TONIC7,TONIC6))
        assert valid(s,(11+k)%12,(3,10))
        assert valid(d,(4+k)%12,(4,10))
        assert valid(t7,(9+k)%12,(3,10))
        assert valid(t6,(9+k)%12,(3,9))
        assert move(s,d)==(0,0,-1,-1)
        assert move(d,t7)==(-2,-1,-1,-1)
        assert move(d,t6)==(-2,-1,-2,-1)
        assert cost(s,d)==2 and cost(d,t7)==5 and cost(d,t6)==6
    return {'keys':12,'ii_to_V':2,'V_to_minor9':5,'V_to_minor6_9':6,'status':'PASS'}
if __name__=='__main__':print(run())
