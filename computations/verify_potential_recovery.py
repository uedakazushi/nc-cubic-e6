#!/usr/bin/env python3
"""Exact rigidity ranks for recovering the potential and the central degree-one line at the quantum-so3 point. These ranks support a separate Artin induction proof."""
import itertools,json
from functools import lru_cache
from pathlib import Path
from sympy.polys.matrices import DomainMatrix
from central_tangent import K,q,PHIS,words,mon,add,scale,zero,one,cv
rules={(1,0):{(0,1):q*q,(2,):-q*q},(2,0):{(0,2):q,(1,):one},(2,1):{(1,2):q*q,(0,):-q*q}}
@lru_cache(None)
def nf(w):
 for i in range(len(w)-1):
  if w[i:i+2] in rules:return add(*(scale(nf(w[:i]+v+w[i+2:]),c) for v,c in rules[w[i:i+2]].items()))
 return mon(w)
basis=sum((words(n) for n in range(3)),[]);cols=[]
for w in PHIS:
 col=[]
 for g in range(3):
  dr=add(*(nf(w[j+1:]+w[:j]) for j,h in enumerate(w) if h==g));col.extend(dr.get(v,zero) for v in basis)
 cols.append(col)
D=DomainMatrix([[col[i] for col in cols] for i in range(30)],(30,20),K)
phi={ (0,1,2):one,(0,2,1):-q,**{(i,i):-one/cv(2) for i in range(3)}}
v=DomainMatrix([[phi.get(w,zero)] for w in PHIS],(20,1),K)
assert D.rank()==19 and (D*v).is_zero_matrix
hrels={(1,0):{(0,1):q*q,(2,3):-q*q},(2,0):{(0,2):q,(1,3):one},(2,1):{(1,2):q*q,(0,3):-q*q},**{(3,j):{(j,3):one} for j in range(3)}}
quad=list(itertools.combinations_with_replacement(range(4),2));qc=[]
for v in range(4):
 col=[]
 for g in range(4):
  row={}
  for w,sign in [((v,g),1),((g,v),-1)]:
   for z,c in hrels.get(w,{w:one}).items():row[z]=row.get(z,zero)+sign*c
  col.extend(row.get(w,zero) for w in quad)
 qc.append(col)
C=DomainMatrix([[col[i] for col in qc] for i in range(40)],(40,4),K)
assert C.rank()==3 and all(not x for x in qc[3])
out={'status':'PASS','field':'Q(q), q^2+q+1=0','potential_gradient_matrix_shape':[30,20],'potential_gradient_rank':19,'gradient_kernel':'span of Phi0=xyz-q*xzy-(x^2+y^2+z^2)/2','linear_center_matrix_shape':[40,4],'linear_center_rank':3,'linear_center_kernel':'span of central t','scope':'formal Artin potential recovery up to scalar and central line rigidity; proof of categorical recognition is separate'}
Path(__file__).with_name('potential_recovery_certificate.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
