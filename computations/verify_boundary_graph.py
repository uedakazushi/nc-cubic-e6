#!/usr/bin/env python3
"""Check both determinant projections and a non-three-periodic boundary orbit. One exact orbit disproves a generic identity; it does not certify all fibers."""
import json,itertools,sympy as S
from pathlib import Path
from central_tangent import K,q,zero,one,cv
l,k,e,z,x,y,w,Q=S.symbols('lambda kappa eta zeta x y z Q');p=1+k*l
C=k+k*k*l+(k**3/S.Integer(3)+9*e**3*z**3)*l*l;F=Q*p*(x**3+e**3*y**3+z**3*w**3)+C*x*y*w
MR=S.Matrix([[3*l*x,p*w,-Q*y],[-Q*w,3*l*e**3*y,p*x],[p*y,-Q*x,3*l*z**3*w]])
red=lambda f:S.Poly(S.expand(f),Q).rem(S.Poly(Q*Q+Q+1,Q)).as_expr()
assert red(MR.det()-3*l*F)==0
assert all(red(v)==0 for v in MR.subs(l,0)*S.Matrix([x,Q*Q*y,Q*w]))
minor=[MR.subs(l,0).extract(a,b).det() for a in itertools.combinations(range(3),2) for b in itertools.combinations(range(3),2)]
for var in [x,y,w]:
 gb=S.groebner([Q*Q+Q+1,*[f.subs(var,1) for f in minor]],*[v for v in [x,y,w] if v!=var],Q,domain=S.QQ)
 assert len(gb.polys)==1 and gb.polys[0].is_one
# lambda=1/2,kappa=2,eta=zeta=1: p=2,C=83/12.
def matrix(v):
 x,y,z=v;h=cv(S.Rational(3,2));p=cv(2)
 return [[h*x,-q*z,p*y],[p*z,h*y,-q*x],[-q*y,p*x,h*z]]
def cross(a,b):return [a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]]
def normalize(v):
 pivot=next(c for c in v if c);return [c/pivot for c in v]
def step(v):
 rows=matrix(v)
 for a,b in itertools.combinations(rows,2):
  ans=cross(a,b)
  if any(ans):break
 else:raise AssertionError('rank below two along orbit')
 ans=normalize(ans);assert all(sum((a*b for a,b in zip(row,ans)),zero)==zero for row in rows)
 return ans
def equation(v):
 x,y,z=v;return q*cv(2)*(x**3+y**3+z**3)+cv(S.Rational(83,12))*x*y*z
orbit=[[zero,one,-one]]
for _ in range(3):orbit.append(step(orbit[-1]))
assert all(not equation(v) for v in orbit);assert orbit[3][0]
show=lambda c:str(K.to_sympy(c).subs(K.ext.as_expr(),S.Symbol('q0')))
out={'status':'PASS','right_projection_determinant':'det(Mright)=3*lambda*F','right_base_graph':'diag(1,q0^2,q0)','right_rank_two_projective_patches':3,'orbit_parameters':{'lambda':'1/2','kappa':2,'eta':1,'zeta':1},'orbit':[[show(c) for c in v] for v in orbit],'all_four_orbit_points_lie_on_F':True,'sigma_cubed_is_not_identity_at_generic_point':True,'scope':'exact rational example disproves generic three-periodicity; global relative graph is proved by properness and rank-two openness, not by sampling'}
Path(__file__).with_name('boundary_graph_certificate.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
