// Chromatic engine v3: constrained two-bar search; original study, NOT Chopin transcription.
// Run: node chromatic_engine_v3.js (tests only; no score or audio output).
const HARMONY=[
 {name:"Am", pcs:[9,0,4], bass:45},
 {name:"E7",pcs:[4,8,11,2],bass:40},
 {name:"Fmaj7",pcs:[5,9,0,4],bass:41},
 {name:"G7",pcs:[7,11,2,5],bass:43},
 {name:"Am",pcs:[9,0,4],bass:45},
 {name:"E7b9",pcs:[4,8,11,2,5],bass:40},
 {name:"E7",pcs:[4,8,11,2],bass:40},
 {name:"Am",pcs:[9,0,4],bass:45}
];
const pc=n=>((n%12)+12)%12;
function chromaticBeat(start,dir){return Array.from({length:4},(_,k)=>start+dir*k)}
function classify(line,j,chord){
 const p=pc(line[j]), isChord=chord.pcs.includes(p);
 if(isChord)return "chord";
 const prev=j?line[j-1]:null,next=j+1<line.length?line[j+1]:null;
 if(prev!==null&&next!==null&&Math.abs(line[j]-prev)===1&&Math.abs(next-line[j])===1){
  if(next===prev)return "neighbor";
  if(Math.sign(line[j]-prev)===Math.sign(next-line[j]))return "passing";
 }
 return "unresolved";
}
function generatePair(pair, seed=70){
 const chords=HARMONY.slice(pair*2,pair*2+2);
 const patterns=[];
 // All 8-beat contour choices (256), each beat has exactly 4 chromatic 16ths.
 for(let mask=0;mask<256;mask++){
  let line=[],pitch=seed,dirs=[];
  for(let b=0;b<8;b++){
   const dir=(mask&(1<<b))?1:-1;dirs.push(dir);
   line.push(...chromaticBeat(pitch,dir));
   pitch+=dir*4;
  }
  const classifications=line.map((p,j)=>classify(line,j,chords[Math.floor(j/16)]));
  const strong=[0,4,8,12,16,20,24,28];
  const onChord=strong.filter(j=>chords[Math.floor(j/16)].pcs.includes(pc(line[j]))).length;
  const range=Math.max(...line)-Math.min(...line);
  const outOfRange=line.filter(p=>p<60||p>90).length;
  const unresolved=classifications.filter((v,j)=>v==="unresolved"&&j%4!==0).length;
  // Phrase-level control: reward contour reversals but penalize perpetual zigzag.
  const turns=dirs.slice(1).filter((d,j)=>d!==dirs[j]).length;
  const score=onChord*12-outOfRange*25-Math.max(0,range-18)*3-unresolved*2-Math.abs(turns-3)*2;
  patterns.push({score,line,dirs,onChord,range,unresolved,turns,mask});
 }
 patterns.sort((a,b)=>b.score-a.score||a.mask-b.mask);
 return {chords:chords.map(x=>x.name),...patterns[0]};
}
function audit(result){
 const r=[];
 for(let i=0;i<4;i++){
  const pair=generatePair(i,70);
  if(pair.line.length!==32)throw Error("length");
  if(pair.line.some((p,j)=>j&&Math.abs(p-pair.line[j-1])!==1))throw Error("chromatic continuity");
  if(pair.line.some(p=>p<60||p>90))throw Error("register");
  if(pair.onChord<1)throw Error("harmonic anchors");
  r.push({pair:i+1,chords:pair.chords,mask:pair.mask,score:pair.score,onChord:pair.onChord,range:pair.range,turns:pair.turns,unresolved:pair.unresolved});
 }
 return r;
}
const result=audit();
if(typeof console!=="undefined")console.log(JSON.stringify(result,null,2));
