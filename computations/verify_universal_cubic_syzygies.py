#!/usr/bin/env python3
"""Four exact universal degree-three syzygies for homogenized cyclic potentials. All polynomial coefficients, no parameter sampling. This certifies cubic flatness near the base point, not intrinsic coverage."""
import itertools,json
from pathlib import Path
from sympy.polys.matrices import DomainMatrix
from central_tangent import K,q,PHIS
# Coefficients are affine polynomials: index -1 is the constant term.
def plus(a,b,sign=1):
 out=dict(a)
 for j,c in b.items():
  out[j]=out.get(j,K.zero)+sign*c
  if not out[j]:del out[j]
 return out
def add(p,w,c):
 p[w]=plus(p.get(w,{}),c)
 if not p[w]:del p[w]
def cst(c):return {-1:K.convert(c)} if c else {}
phi={(0,1,2):cst(1),(0,2,1):cst(-q)}
for j in range(3):phi[(j,j,3)]=cst(-K.one/2)
for j,w in enumerate(PHIS):add(phi,w+(3,)*(3-len(w)),{j:K.one})
r=[]
for g in range(4):
 pol={}
 for w,c in phi.items():
  for j,x in enumerate(w):
   if x==g:add(pol,w[j+1:]+w[:j],c)
 r.append(pol)
rels=[{(3,j):cst(1),(j,3):cst(-1)} for j in range(3)]+r[:3]
# Coordinates (left-letter, relation) and (relation, right-letter).
S=[]
for g in range(3):
 syz={('L',3,3+g):cst(1),('R',3+g,3):cst(-1)}
 for (a,b),c in r[g].items():
  if a!=3:add(syz,('R',a,b),{j:-v for j,v in c.items()})
  if b!=3:add(syz,('L',a,b),{j:-v for j,v in c.items()})
 S.append(syz)
syz={}
for g in range(3):add(syz,('L',g,3+g),cst(1));add(syz,('R',3+g,g),cst(-1))
for (a,b),c in r[3].items():
 if a!=3:add(syz,('R',a,b),c)
 if b!=3:add(syz,('L',a,b),c)
S.append(syz)
# Products of affine coefficients can be quadratic; verify without SymPy expansion.
def mul(a,b):
 out={}
 for i,c in a.items():
  for j,d in b.items():
   key=tuple(sorted(x for x in (i,j) if x>=0));out[key]=out.get(key,K.zero)+c*d
   if not out[key]:del out[key]
 return out
def sumquad(a,b):
 out=dict(a)
 for j,c in b.items():
  out[j]=out.get(j,K.zero)+c
  if not out[j]:del out[j]
 return out
cols=[('L',v,j) for v in range(4) for j in range(6)]+[('R',j,v) for j in range(6) for v in range(4)]
ww=list(itertools.product(range(4),repeat=3));wi={w:i for i,w in enumerate(ww)}
for syz in S:
 image={}
 for (side,a,b),c in syz.items():
  j=b if side=='L' else a;v=a if side=='L' else b
  for w,d in rels[j].items():
   word=(v,)+w if side=='L' else w+(v,)
   image[word]=sumquad(image.get(word,{}),mul(c,d))
 assert not any(image.values())
D=[[K.zero]*48 for w in ww]
for j,(side,a,b) in enumerate(cols):
 rel=b if side=='L' else a;v=a if side=='L' else b
 for w,c in rels[rel].items():
  word=(v,)+w if side=='L' else w+(v,);D[wi[word]][j]+=c.get(-1,K.zero)
DM=DomainMatrix(D,(64,48),K);SM=DomainMatrix([[s.get(col,{}).get(-1,K.zero) for s in S] for col in cols],(48,4),K)
assert DM.rank()==44 and SM.rank()==4 and (DM*SM).is_zero_matrix
out={'status':'PASS','coefficient_ring':'Q(q)[e_1,...,e_20], q^2+q+1=0; no truncation','exact_universal_syzygies':4,'base_cubic_relation_matrix_shape':[64,48],'base_cubic_relation_rank':44,'base_syzygy_matrix_shape':[48,4],'base_syzygy_rank':4,'all_four_syzygies_hold_identically':True,'conclusion':'all four cubic syzygies lift over every Artin cyclic-potential deformation of this point; cubic envelope piece is free rank20','not_claimed':['all intrinsic deformations are cyclic-potential deformations','higher-degree flatness from this certificate alone','complete component classification']}
Path(__file__).with_name('universal_cubic_syzygies_certificate.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
