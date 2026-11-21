// Op.10 No.3 generative architecture, study 01. This is a structural test, not a transcription.
const form=[["A",1,21],["B",22,61],["A'",62,77]];
const motifs=[
 {name:"song",section:"A",layers:["cantabile","oscillating-sixteenths","syncopated-bass"],tension:1},
 {name:"transition",section:"B",layers:["chromatic-inner","bass","motivic-fragment"],tension:3},
 {name:"diminished-chain",section:"B",layers:["diminished-harmony","contrary-motion"],tension:4},
 {name:"double-sixths",section:"B",layers:["mirrored-sixths","bass"],tension:5},
 {name:"return",section:"A'",layers:["cantabile","oscillating-sixteenths","syncopated-bass"],tension:1}
];
function assign(bar){
 if(bar<1||bar>77)throw Error("bar out of range");
 const section=form.find(x=>bar>=x[1]&&bar<=x[2])[0];
 const type=bar>=46&&bar<=53?"double-sixths":bar>=38&&bar<=41?"diminished-chain":section==="A"?"song":section==="A'"?"return":"transition";
 return {bar,section,type,template:motifs.find(x=>x.name===type)};
}
function validate(){
 const bars=Array.from({length:77},(_,i)=>assign(i+1));
 if(bars.length!==77||form.reduce((n,s)=>n+s[2]-s[1]+1,0)!==77)throw Error("form");
 if(bars[20].section!=="A"||bars[21].section!=="B"||bars[60].section!=="B"||bars[61].section!=="A'")throw Error("boundaries");
 if(bars.slice(45,53).some(x=>x.type!=="double-sixths"))throw Error("sixths");
 if(bars.slice(37,41).some(x=>x.type!=="diminished-chain"))throw Error("diminished");
 if(!bars.every(x=>x.template.layers.length>=2))throw Error("texture");
 // A' is a transformed return, not literal pitch copy.
 if(bars[0].template===bars[61].template)throw Error("return must be a transformation");
 return {bars:bars.length,sections:form.map(x=>x[2]-x[1]+1),diminished:[38,41],sixths:[46,53],status:"PASS"};
}
if(typeof console!=="undefined")console.log(JSON.stringify(validate()));
