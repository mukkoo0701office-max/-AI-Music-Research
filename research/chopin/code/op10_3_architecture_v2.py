"""Original structural composition model, not transcription of Chopin Op.10 No.3."""
from dataclasses import dataclass
@dataclass(frozen=True)
class Section:
    name:str
    start:int
    end:int
    density:int
    cantabile:bool
SECTIONS=(Section('A',1,21,2,True),Section('B',22,61,5,False),Section('A_prime',62,77,2,True))
def bar_plan(bar):
    assert 1<=bar<=77
    s=next(s for s in SECTIONS if s.start<=bar<=s.end)
    mode='theme' if s.name=='A' else 'development' if s.name=='B' else 'transformed_return'
    if bar==8:mode='phrase_breath'
    if 38<=bar<=41:mode='chromatic_dim7_tension'
    if 46<=bar<=53:mode='double_note_chromatic_development'
    if 54<=bar<=61:mode='dominant_preparation_hypothesis'
    return dict(bar=bar,section=s.name,texture=mode,density=s.density,cantabile=s.cantabile)
def audit():
    bars=[bar_plan(i) for i in range(1,78)]
    assert len(bars)==77
    assert [s.end-s.start+1 for s in SECTIONS]==[21,40,16]
    assert bars[7]['texture']=='phrase_breath'
    assert all(x['texture']=='chromatic_dim7_tension' for x in bars[37:41])
    assert all(x['texture']=='double_note_chromatic_development' for x in bars[45:53])
    assert all(x['texture']=='dominant_preparation_hypothesis' for x in bars[53:61])
    assert all(x['texture']=='transformed_return' for x in bars[61:])
    assert bars[0]['texture']!=bars[61]['texture']
    return {'total_bars':77,'section_lengths':[21,40,16],'final_section':'transformed_return','status':'PASS'}
if __name__=='__main__':print(audit())
