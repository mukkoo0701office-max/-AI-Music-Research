"""Passing/approach chord study 007 v2: tested 0/1/2 detours, four-voice DP."""
from itertools import combinations
spec={'Cmaj9':({0,2,4,7,11},{4,11}),'Bm7b5':({11,2,5,9},{2,9}),'E7b9':({4,8,11,2,5},{8,2}),'Am9':({9,0,4,7,11},{0,7}),'Dm9':({2,5,9,0,4},{5,0}),'Ab13':({8,0,3,6,5},{0,6}),'Db13':({1,5,8,11,3},{5,11}),'Fm6':({5,8,0,2},{8,2}),'Fmaj9':({5,9,0,4,7},{9,4}),'Cmaj9/E':({0,2,4,7,11},{4,11})}
def candidates(name):
 pcs,guide=spec[name]
 for ns in combinations((n for n in range(52,73) if n%12 in pcs),4):
  if len({n%12 for n in ns})!=4 or not guide.issubset({n%12 for n in ns}) or ns[-1]-ns[0]>16:continue
  if any(b-a==1 and a<60 for a,b in zip(ns,ns[1:])):continue
  yield ns
def transition(a,b):
 return sum(abs(x-y)+3*(abs(x-y)>5) for x,y in zip(a,b))
def solve(names):
 dp={v:(0,[v]) for v in candidates(names[0])}
 for name in names[1:]:
  nxt={}
  for v in candidates(name):
   u=min(dp,key=lambda u:dp[u][0]+transition(u,v))
   nxt[v]=(dp[u][0]+transition(u,v),dp[u][1]+[v])
  assert nxt,name
  dp=nxt
 return min(dp.values(),key=lambda pair:pair[0])
tests={'A0':['Cmaj9','Am9'],'A1':['Cmaj9','E7b9','Am9'],'A2':['Cmaj9','Bm7b5','E7b9','Am9'],'B0':['Dm9','Cmaj9'],'B1':['Dm9','Db13','Cmaj9'],'B2':['Dm9','Ab13','Db13','Cmaj9'],'C0':['Cmaj9','Cmaj9/E'],'C1':['Cmaj9','Fm6','Cmaj9/E'],'C2':['Cmaj9','Fmaj9','Fm6','Cmaj9/E']}
for label,names in tests.items():
 score,notes=solve(names)
 assert len(notes)==len(names)
 for name,voicing in zip(names,notes):
  assert all(n%12 in spec[name][0] for n in voicing)
 print(label,score,list(zip(names,notes)))
print('PASS 9 sequences; voice-leading cost only; melody/bass/pedal not yet audited')
