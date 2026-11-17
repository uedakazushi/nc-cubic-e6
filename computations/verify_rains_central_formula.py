#!/usr/bin/env python3
"""Verify the corrected EG/Rains Appendix 9.1 central formula in all original filtered relations over the full coefficient ring. All normal-form denominators are checked at the three-torsion base point."""
import itertools,json,time
from functools import lru_cache
from pathlib import Path
import sympy as S,networkx as nx
from sympy.polys.matrices import DomainMatrix
start=time.time();qs,ts=S.symbols('q t');K=S.QQ.frac_field(qs,ts);q,t=K.gens;P=K.poly_ring(*S.symbols('a b c aa bb cc'));a,b,c,aa,bb,cc=P.gens;zero=P.zero;one=P.one
# Explicit conversion is safer than relying on the different ring attributes.
def C(v):return P.ring.from_dict({(0,)*6:K.convert(v)})
def add(*ps):
 out={}
 for p in ps:
  for w,c in p.items():
   out[w]=out.get(w,zero)+c
   if not out[w]:del out[w]
 return out
def scale(p,v):return {w:c*v for w,c in p.items() if c*v}
def words(n):return [tuple([0]*i+[1]*j+[2]*(n-i-j)) for i in range(n+1) for j in range(n-i+1)]
rules={(1,0):{(0,1):C(1/q),(2,2):C(-t/q),(2,):c*C(1/q),():cc*C(1/q)},(2,0):{(0,2):C(q),(1,1):C(t),(1,):-b,():-bb},(2,1):{(1,2):C(1/q),(0,0):C(-t/q),(0,):a*C(1/q),():aa*C(1/q)}}
NF={}
for n in range(5):
 for w in words(n):NF[w]={w:one}
 rew={};graph=nx.DiGraph()
 for w in itertools.product(range(3),repeat=n):
  if w in NF:continue
  graph.add_node(w)
  for j in range(n-1):
   if w[j:j+2] in rules:
    rew[w]=add(*({w[:j]+v+w[j+2:]:c} for v,c in rules[w[j:j+2]].items()))
    for v in rew[w]:
     if len(v)==n and v not in NF:graph.add_edge(w,v)
    break
 cond=nx.condensation(graph)
 for comp in reversed(list(nx.topological_sort(cond))):
  ww=sorted(cond.nodes[comp]['members']);idx={w:i for i,w in enumerate(ww)}
  mat=[[K.one if i==j else K.zero for j in range(len(ww))] for i in range(len(ww))];rhs=[]
  for i,w in enumerate(ww):
   rr={}
   for v,c in rew[w].items():
    if v in idx:
     assert c.is_ground;mat[i][idx[v]]-=c.get((0,)*6,K.zero)
    else:rr=add(rr,scale(NF[v],c))
   rhs.append(rr)
  if len(ww)==1:NF[ww[0]]=scale(rhs[0],C(1/mat[0][0]));continue
  print('invert',n,len(ww),'sec',time.time()-start,flush=True)
  inv=DomainMatrix(mat,(len(ww),len(ww)),K).inv().to_list()
  for i,w in enumerate(ww):NF[w]=add(*(scale(rr,C(v)) for v,rr in zip(inv[i],rhs) if v))
 print('degree done',n,'sec',time.time()-start,flush=True)
rels=[]
for pair,row in rules.items():rels.append(add({pair:one},scale(row,-one)))
for rel in rels:
 for n in range(3):
  for nl in range(n+1):
   for l in itertools.product(range(3),repeat=nl):
    for r in itertools.product(range(3),repeat=n-nl):
     image=add(*(scale(NF[l+w+r],v) for w,v in rel.items()));assert not image
print('ALL ORIGINAL RELATION INSERTIONS PASS',time.time()-start,flush=True)
a,b,c,aa,bb,cc=P.gens
raw={}
def term(w,v):raw[w]=raw.get(w,zero)+v
term((1,1,1),C(t*t*(q+1)*(t**3+1)));term((1,2,0),C(t*(q+1)*(q**3-t**3)));term((2,1,0),C(-t*(q+1)*q*(t**3+1)));term((2,2,2),C(t*t*(q+1)*(q**3-t**3)))
term((1,1),-C(t*(q*q+q*t**3+q+2*t**3+1))*b);term((1,2),C(q*t**3-q*q)*a);term((2,0),C(t**3*(q+1))*b);term((2,1),C(q**3+q*t**3)*a);term((1,0),C(q*(q+1)*t**3)*c);term((2,2),C(t*(2*q*t**3+t**3-q**4-q**3-q*q))*c)
term((0,),-(C(q**3*t+2*q*q*t+q*t)*aa+C(q*q)*a*a+C(q*t*t)*b*c))
term((1,),-C(t)*(C(q**3+2*q*q+q*t**3+2*q+t**3+1)*bb+C(q*t)*a*c-C(t*t)*b*b))
term((2,),-C(t)*(C(q**4+2*q**3+2*q*q-q*t**3+q-t**3)*cc+C(q*t*t)*c*c+C(q*t)*a*b))
for g in range(3):
 image=add(*(scale(add(NF[w+(g,)],scale(NF[(g,)+w],-one)),v) for w,v in raw.items()))
 assert not image,('corrected formula fails',g)
 print('CENTRAL COMMUTATOR PASS',g,'sec',time.time()-start,flush=True)
printed_difference={(1,):-C(t*q**3)*bb*(bb-one)}
printed_comm=add(*(scale(add(NF[w+(0,)],scale(NF[(0,)+w],-one)),v) for w,v in printed_difference.items()))
assert printed_comm, 'printed b2 repetition must give a noncentral generic expression'
normal_center=add(*(scale(NF[w],v) for w,v in raw.items()))
# Every rational normal-form denominator is a unit at q^2+q+1=0,t=0.
E=S.QQ.alg_field_from_poly(S.Poly(S.Symbol('Q')**2+S.Symbol('Q')+1));q0=E.unit
seen=set()
for pol in list(normal_center.values())+[c for row in NF.values() for c in row.values()]:
 for rat in pol.values():
  den=rat.denom
  key=str(den)
  if key in seen:continue
  seen.add(key)
  value=sum((E.convert(v)*q0**a for (a,b),v in den.items() if b==0),E.zero)
  assert value,('denominator not a unit at quantum point',key)
result={'status':'PASS','coefficient_ring':'QQ(q,t)[a1,b1,c1,a2,b2,c2]','parameter_sampling':False,'original_relation_insertions':102,'central_commutators':3,'all_normal_form_denominators_are_units_at_q3_t0':True,'correction_to_arxiv_0709_3593_v4_page35':'remove the repeated b2 in q^3*b2 inside the coefficient multiplying b2*y','source_formula_independently_checked':True,'printed_formula_noncentral_over_full_coefficient_ring':True,'not_claimed':['all intrinsic deformation coverage','global component classification']}
Path(__file__).with_name('rains_central_formula_certificate.json').write_text(json.dumps(result,indent=2)+'\n')
print('UNIVERSAL CORRECTED RAINS FORMULA PASS',flush=True)
