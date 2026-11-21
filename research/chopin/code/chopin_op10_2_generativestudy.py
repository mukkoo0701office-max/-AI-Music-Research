"""Original Chopin Op.10-2-inspired three-layer generator; NOT a transcription."""
from xml.etree.ElementTree import Element, SubElement, ElementTree
CHROMATIC=['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
BARS=[('Am',45,[57,60,64]),('E7',47,[56,59,62]),('Am',48,[57,60,64]),('E7',46,[56,59,62]),('Fmaj7',50,[53,57,60]),('G7',52,[55,59,62]),('E7b9',49,[52,56,59]),('Am',45,[57,60,64])]
DIRECTIONS=[1,1,-1,-1,1,1,-1,-1]
ROOT={'Am':45,'E7':40,'Fmaj7':41,'G7':43,'E7b9':40}
def note(parent,midi,duration,voice,staff,beam=None):
 n=SubElement(parent,'note');p=SubElement(n,'pitch');pc=CHROMATIC[midi%12];SubElement(p,'step').text=pc[0]
 if len(pc)>1:SubElement(p,'alter').text='1'
 SubElement(p,'octave').text=str(midi//12-1)
 SubElement(n,'duration').text=str(duration);SubElement(n,'voice').text=str(voice);SubElement(n,'type').text={120:'16th',480:'quarter'}[duration];SubElement(n,'staff').text=str(staff)
 if beam:SubElement(n,'beam',number='1').text=beam
def backup(m):SubElement(SubElement(m,'backup'),'duration').text='1920'
root=Element('score-partwise',version='4.0');SubElement(root,'movement-title').text='Chromatic Layers — Original Study'
pl=SubElement(root,'part-list');sp=SubElement(pl,'score-part',id='P1');SubElement(sp,'part-name').text='Piano';part=SubElement(root,'part',id='P1')
for i,(h,start,tones) in enumerate(BARS):
 m=SubElement(part,'measure',number=str(i+1))
 if i==0:
  a=SubElement(m,'attributes');SubElement(a,'divisions').text='480';SubElement(a,'staves').text='2';t=SubElement(a,'time');SubElement(t,'beats').text='4';SubElement(t,'beat-type').text='4'
  for number,sign,line in [(1,'G',2),(2,'F',4)]:
   c=SubElement(a,'clef',number=str(number));SubElement(c,'sign').text=sign;SubElement(c,'line').text=str(line)
 d=SubElement(m,'direction');SubElement(SubElement(d,'direction-type'),'words').text=h
 for j in range(16):note(m,start+DIRECTIONS[i]*j,120,1,1,['begin','continue','continue','end'][j%4])
 backup(m)
 for j in range(4):note(m,tones[j%3],480,2,1)
 backup(m)
 for j in range(4):note(m,ROOT[h]+(7 if j%2 else 0),480,3,2)
ElementTree(root).write('chopin_op10_2_generativestudy.musicxml',encoding='utf-8',xml_declaration=True)
assert len(BARS)==8
print('8 bars; 128 chromatic 16ths; 32 harmonic quarter notes; 32 bass quarter notes')
