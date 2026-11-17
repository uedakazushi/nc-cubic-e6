#!/usr/bin/env python3
"""All four homogeneous cubic overlaps for the 20 first-order cyclic-potential directions. This is a degree-three check, not all-order intrinsic versality."""
import itertools,json
from functools import lru_cache
from pathlib import Path
from central_tangent import K,q,zero,one,cv,add,scale,mon,PHIS
rules={(1,0):{(0,1):q*q,(2,3):-q*q},(2,0):{(0,2):q,(1,3):one},(2,1):{(1,2):q*q,(0,3):-q*q},**{(3,j):{(j,3):one} for j in range(3)}}
@lru_cache(None)
def nf(w):
 for j in range(len(w)-1):
  if w[j:j+2] in rules:
   return add(*(scale(nf(w[:j]+v+w[j+2:]),c) for v,c in rules[w[j:j+2]].items()))
 return mon(w)
critical=[(c,b,a) for a,b,c in itertools.combinations(range(4),3)]
checks=0
for phi in PHIS:
 dr=[]
 for g in range(3):
  dr.append(add(*(mon(phi[j+1:]+phi[:j]+(3,)*(3-len(phi))) for j,h in enumerate(phi) if h==g)))
 delta={(2,1):scale(dr[0],q*q),(2,0):scale(dr[1],-1),(1,0):scale(dr[2],q*q)}
 @lru_cache(None)
 def dn(w):
  for j in range(len(w)-1):
   p=w[j:j+2]
   if p in rules:
    return add(*(scale(dn(w[:j]+v+w[j+2:]),c) for v,c in rules[p].items()),*(scale(nf(w[:j]+v+w[j+2:]),c) for v,c in delta.get(p,{}).items()))
  return {}
 for w in critical:
  left=add(*(scale(dn(v+w[2:]),c) for v,c in rules[w[:2]].items()),*(scale(nf(v+w[2:]),c) for v,c in delta.get(w[:2],{}).items()))
  right=add(*(scale(dn(w[:1]+v),c) for v,c in rules[w[1:]].items()),*(scale(nf(w[:1]+v),c) for v,c in delta.get(w[1:],{}).items()))
  assert not add(left,scale(right,-1)),(phi,w)
  checks+=1
out={'status':'PASS','field':'Q(q), q^2+q+1=0','homogeneous_variables':['x','y','z','t'],'cyclic_directions':len(PHIS),'critical_words':critical,'exact_first_order_overlap_checks':checks,'cubic_obstruction_matrix_shape':[80,20],'cubic_obstruction_matrix_is_zero':True,'not_claimed':['all-order flatness for arbitrary potential parameters','all intrinsic deformation directions covered','global component classification']}
Path(__file__).with_name('cubic_obstruction_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
