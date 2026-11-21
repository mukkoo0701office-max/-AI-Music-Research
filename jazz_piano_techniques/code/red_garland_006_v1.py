"""Original schematic Red Garland block-chord generator and collision audit."""
CHORDS=[('Fm9',(56,60,63,67),[84,86,87]),('Bb13',(56,60,62,67),[86,87,89]),('Ebmaj9',(55,58,62,65),[87,89,91])]
# LH rootless: Fm9 Ab C Eb G; Bb13 Ab C D G; Ebmaj9 G Bb D F
assert all(len(v)==4 and len(set(n%12 for n in v))==4 for _,v,_ in CHORDS)
rows=[]
for name,lh,melody in CHORDS:
 for top in melody:
  rh=(top-12,top-5,top) # octave + perfect fifth above lower octave
  assert rh[2]-rh[0]==12 and rh[1]-rh[0]==7
  assert max(lh)<rh[0]
  pcs={n%12 for n in lh}
  clash=any(abs(x-y)==1 for x in lh for y in rh)
  rows.append((name,lh,rh,clash))
print('PASS',len(rows),'attacks; octave+fifth RH, four distinct LH pitch classes, hands separated')
print('chromatic near-collisions:',sum(r[3] for r in rows))
for row in rows: print(row)
