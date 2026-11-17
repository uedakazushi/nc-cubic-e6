#!/usr/bin/env python3
"""Construct the simultaneous eight-variable central-incidence jet modulo the cube of the maximal ideal, and verify centrality again in rebuilt original relations. No all-order or intrinsic-coverage claim."""
import sys,json,itertools,time
from pathlib import Path
from verify_tangent_quotient import *
start=time.time();dirs=[];current=dm(gauge)
for vec in family:
 trial=dm(gauge+dirs+[vec])
 if trial.rank()>current.rank():dirs.append(vec);current=trial
assert len(dirs)==7;dirs.append(extra);assert dm(gauge+dirs).rank()==22
P=K.poly_ring(*sp.symbols('h0:8'));u=P.gens;oneP=P.one;zeroP=P.zero
pc=lambda c:P.convert(c,K)
def trunc(p):return P.ring.from_dict({m:c for m,c in p.items() if sum(m)<=2})
def hom(p,n):return P.ring.from_dict({m:c for m,c in p.items() if sum(m)==n})
ph={w:pc(c) for w,c in phi.items()}
for j,w in enumerate(PHIS):ph[w]=ph.get(w,zeroP)+sum((u[a]*pc(dirs[a][j]) for a in range(8)),zeroP)
raw=[]
for g in range(3):
 out={}
 for w,c in ph.items():
  for j,x in enumerate(w):
   if x==g:
    v=w[j+1:]+w[:j];out[v]=out.get(v,zeroP)+c
 raw.append(out)
inv=[(1,0),(2,0),(2,1)];normal=sum((words(n) for n in range(3)),[])
A0=DomainMatrix([[p.get(w,zeroP).get((0,)*8,K.zero) for w in inv] for p in raw],(3,3),K).inv().to_list()
A1=[[hom(p.get(w,zeroP),1) for w in inv] for p in raw]
C0=[[hom(p.get(w,zeroP),0) for w in normal] for p in raw];C1=[[hom(p.get(w,zeroP),1) for w in normal] for p in raw]
def matmul(a,b):return [[sum((pc(x)*y if not hasattr(x,'ring') else x*y for x,y in zip(row,col)),zeroP) for col in zip(*b)] for row in a]
B0=[[-x for x in row] for row in matmul(A0,C0)];AB=matmul(A1,B0)
B1=[[-x for x in row] for row in matmul(A0,[[x+y for x,y in zip(a,b)] for a,b in zip(C1,AB)])]
B2=[[-x for x in row] for row in matmul(A0,matmul(A1,B1))]
rr={w:[{v:c for v,c in zip(normal,mat[j]) if c} for mat in [B0,B1,B2]] for j,w in enumerate(inv)}
@lru_cache(None)
def nfh(w,n):
 for j in range(len(w)-1):
  if w[j:j+2] in rr:
   out={}
   for d in range(n+1):
    for v,c in rr[w[j:j+2]][d].items():
     for z,b in nfh(w[:j]+v+w[j+2:],n-d).items():out[z]=out.get(z,zeroP)+c*b
   return {v:c for v,c in out.items() if c}
 return {w:oneP} if n==0 else {}
Gp={w:pc(c) for w,c in G.items()}
for j,w in enumerate(BASIS):Gp[w]=Gp.get(w,zeroP)+sum((u[a]*pc(dirs[a][20+j]) for a in range(8)),zeroP)
pairs=list(itertools.combinations_with_replacement(range(8),2));exps=[]
for a,b in pairs:
 e=[0]*8;e[a]+=1;e[b]+=1;exps.append(tuple(e))
columns=[[K.zero]*105 for _ in pairs]
for g in range(3):
 for n in [1,2]:
  out={}
  for w,c in Gp.items():
   for d in range(min(n,1)+1):
    cc=hom(c,d)
    if not cc:continue
    for ww,sign in [(w+(g,),1),((g,)+w,-1)]:
     for v,b in nfh(ww,n-d).items():out[v]=out.get(v,zeroP)+sign*cc*b
  out={w:c for w,c in out.items() if c}
  if n==1:assert not out,('first order',g)
  else:
   for j,(gg,w) in enumerate(ROWS):
    if gg==g:
     for k,e in enumerate(exps):columns[k][j]=out.get(w,zeroP).get(e,K.zero)
 print('normal residual',g,'seconds',time.time()-start,flush=True)
Qmat=DomainMatrix([[col[j] for col in columns] for j in range(105)],(105,36),K)
aug=M.hstack(-Qmat);rref,piv=aug.rref();consistent=all(j<40 for j in piv)
assert consistent,'second-order obstruction; no jet has been constructed'
print('SECOND ORDER',consistent,'ranks',M.rank(),aug.rank(),flush=True)
result={'status':'PASS' if consistent else 'OBSTRUCTION','base':[2,1,2,3,5],'directions':8,'quadratic_monomials':36,'linear_rank':M.rank(),'augmented_rank':aug.rank(),'all_second_order_obstruction_classes_zero':consistent}
Path(__file__).with_name('second_order_incidence_certificate.json').write_text(json.dumps(result,indent=2)+'\n')
if consistent:
 vals=[[K.zero]*36 for _ in range(40)]
 for row,pivot in zip(rref.to_list(),piv):vals[pivot]=row[40:]
 assert (M*DomainMatrix(vals,(40,36),K)+Qmat).is_zero_matrix
 result['second_order_corrections']=[{'variable':j,'coefficients':{str(pair):str(K.to_sympy(c).subs(K.ext.as_expr(),sp.Symbol('q'))) for pair,c in zip(pairs,row) if c}} for j,row in enumerate(vals) if any(row)]
 Path(__file__).with_name('second_order_incidence_certificate.json').write_text(json.dumps(result,indent=2)+'\n')
 # Rebuild the actual quadratic relations and cut to order two, then check all commutators again.
 second=[sum((P.ring.from_dict({e:vals[j][k]}) for k,e in enumerate(exps)),zeroP) for j in range(40)]
 for j,w in enumerate(PHIS):ph[w]+=second[j]
 raw=[]
 for g in range(3):
  out={}
  for w,c in ph.items():
   for j,x in enumerate(w):
    if x==g:
     v=w[j+1:]+w[:j];out[v]=out.get(v,zeroP)+c
  raw.append(out)
 A2=[[hom(p.get(w,zeroP),2) for w in inv] for p in raw];C2=[[hom(p.get(w,zeroP),2) for w in normal] for p in raw]
 AB1=matmul(A1,B1);AB2=matmul(A2,B0)
 B2=[[-x for x in row] for row in matmul(A0,[[a+b+c for a,b,c in zip(x,y,z)] for x,y,z in zip(C2,AB1,AB2)])]
 rr={w:[{v:c for v,c in zip(normal,mat[j]) if c} for mat in [B0,B1,B2]] for j,w in enumerate(inv)};nfh.cache_clear()
 for j,w in enumerate(BASIS):Gp[w]+=second[20+j]
 for g in range(3):
  for n in range(3):
   out={}
   for w,c in Gp.items():
    for d in range(n+1):
     cc=hom(c,d)
     if not cc:continue
     for ww,sign in [(w+(g,),1),((g,)+w,-1)]:
      for v,b in nfh(ww,n-d).items():out[v]=out.get(v,zeroP)+sign*cc*b
   assert not any(out.values()),('rebuilt commutator',g,n)
 result['rebuilt_original_relation_centrality_through_degree_two']=True
 result['base_ring']='Q(q)[h0,...,h7]/(h0,...,h7)^3'
 result['linear_directions']=[{str(j):str(K.to_sympy(v).subs(K.ext.as_expr(),sp.Symbol('q'))) for j,v in enumerate(row) if v} for row in dirs]
 result['not_claimed']=['all-order formal central lift','H3 family recognition over arbitrary bases','all intrinsic deformation coverage','complete component classification']
 Path(__file__).with_name('second_order_incidence_certificate.json').write_text(json.dumps(result,indent=2)+'\n')
 print('REBUILT SECOND-ORDER CENTRALITY PASS',time.time()-start,flush=True)
