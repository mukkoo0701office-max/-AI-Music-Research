// Chopin Op.10 No.2 formal constraints (not a transcription).
// Source-backed landmarks and explicitly separate hypothetical realization.
const FACTS={
  totalBars:49,
  sections:[{name:"A",from:1,to:18},{name:"B",from:19,to:35},{name:"A'",from:36,to:49}],
  neapolitanBar:15,
  dominantPedal:{from:32,to:35,pc:4},
  middleRisingSequence:[{from:19,to:20,rootPc:5},{from:21,to:22,rootPc:7},{from:23,to:24,rootPc:9}],
  middleClimaxBar:25,
  picardyEnding:true
};
const pc=x=>((x%12)+12)%12;
function validateForm(f){
 const errors=[];
 if(f.totalBars!==49)errors.push("bar count");
 let cursor=1;
 for(const s of f.sections){if(s.from!==cursor||s.to<s.from)errors.push("section gap");cursor=s.to+1}
 if(cursor!==50)errors.push("final boundary");
 if(f.dominantPedal.from<19||f.dominantPedal.to>35||f.dominantPedal.pc!==4)errors.push("dominant pedal");
 if(f.middleClimaxBar!==25)errors.push("climax");
 const seq=f.middleRisingSequence;
 if(seq.length!==3||seq.some((s,i)=>s.to!==s.from+1||(i&&s.from!==seq[i-1].to+1)))errors.push("sequence timing");
 if(seq.length===3&&(pc(seq[1].rootPc-seq[0].rootPc)!==2||pc(seq[2].rootPc-seq[1].rootPc)!==2))errors.push("sequence pitch");
 if(f.neapolitanBar!==15||!f.picardyEnding)errors.push("landmarks");
 return errors;
}
function buildConstraintGrid(f=FACTS){
 if(validateForm(f).length)throw Error(validateForm(f).join(","));
 const bars=Array.from({length:f.totalBars},(_,i)=>({bar:i+1,section:f.sections.find(s=>i+1>=s.from&&i+1<=s.to).name,confirmed:[],hypothesis:[]}));
 bars[f.neapolitanBar-1].confirmed.push("Neapolitan chord reported by secondary analytical source");
 for(const s of f.middleRisingSequence)for(let b=s.from;b<=s.to;b++)bars[b-1].hypothesis.push("rising two-bar sequence root pitch class "+s.rootPc);
 for(let b=f.dominantPedal.from;b<=f.dominantPedal.to;b++)bars[b-1].confirmed.push("E bass pedal reported from bar 32");
 bars[f.middleClimaxBar-1].confirmed.push("central climax reported by secondary analytical source");
 bars[48].confirmed.push("Picardy ending reported by secondary analytical source");
 return bars;
}
function tests(){
 if(validateForm(FACTS).length)throw Error("valid form rejected");
 const invalid=JSON.parse(JSON.stringify(FACTS));invalid.sections[1].from=20;
 if(!validateForm(invalid).includes("section gap"))throw Error("missing gap detector");
 const grid=buildConstraintGrid();
 if(grid.length!==49||grid[31].confirmed.length!==1||grid[14].confirmed.length!==1)throw Error("landmark");
 if(grid[18].hypothesis.length!==1||grid[24].confirmed.length!==1)throw Error("sequence/climax");
 return {bars:grid.length,sectionLengths:FACTS.sections.map(s=>s.to-s.from+1),pedalBars:[32,33,34,35],hypothesizedSequenceBars:[19,20,21,22,23,24],tests:"PASS"};
}
if(typeof console!=="undefined")console.log(JSON.stringify(tests()));
