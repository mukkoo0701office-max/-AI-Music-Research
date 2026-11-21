"""Drop2/3 and chromatic/diminished approach audit; original illustrative material."""
close=(60,64,67,71)  # C4 E4 G4 B4
drop2=tuple(sorted((close[0],close[1],close[2]-12,close[3])))
drop3=tuple(sorted((close[0],close[1]-12,close[2],close[3])))
chrom=tuple(n-1 for n in drop2)
dim=(59,62,65,68)  # B3 D4 F4 Ab4 = G7(b9) without root
assert drop2==(55,60,64,71) and drop3==(52,60,67,71)
assert {n%12 for n in drop2}=={n%12 for n in close}
assert {n%12 for n in drop3}=={n%12 for n in close}
assert all(b-a==1 for a,b in zip(chrom,drop2))
assert {n%12 for n in dim}=={11,2,5,8}
def displacement(a,b):return tuple(y-x for x,y in zip(a,b))
assert displacement(dim,drop2)==(-4,-2,-1,3)
# Eight illustrative bars, 2 harmonies/bar; intentionally held target Cmaj7,
# NOT an ii-V-I realization or a finished composition.
plan=[('chrom' if i%2==0 else 'dim',chrom if i%2==0 else dim,drop2) for i in range(8)]
assert len(plan)==8 and sum(len((a,b)) for _,a,b in plan)==16
print({'close':close,'drop2':drop2,'drop3':drop3,'chromatic_displacement':displacement(chrom,drop2),'diminished_displacement':displacement(dim,drop2),'bars':len(plan),'sonorities':16,'status':'PASS'})
