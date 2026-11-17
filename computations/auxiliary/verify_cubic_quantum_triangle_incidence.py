"""Universal degree-three central resonance and tetrahedral coarse invariants."""
import sympy as s,json
from functools import lru_cache
from pathlib import Path
q=s.symbols('q');h=q*q-1;p=q*q+q+1
rules={(1,0):[(1/q,(0,1)),(-1/q,(2,))],(2,0):[(q,(0,2)),(1,(1,))],(2,1):[(1/q,(1,2)),(-1/q,(0,))]}
@lru_cache(None)
def nf(w):
 for j in range(len(w)-1):
  if w[j]>w[j+1]:
   out={}
   for a,v in rules[w[j:j+2]]:
    for u,c in nf(w[:j]+v+w[j+2:]).items():out[u]=s.cancel(out.get(u,0)+a*c)
   return {u:c for u,c in out.items() if c!=0}
 return {w:s.Integer(1)}
def add(f,g,a=1):
 out=dict(f)
 for w,c in g.items():out[w]=s.cancel(out.get(w,0)+a*c)
 return {w:c for w,c in out.items() if c!=0}
def mul(f,g):
 out={}
 for u,a in f.items():
  for v,b in g.items():
   for w,c in nf(u+v).items():out[w]=s.cancel(out.get(w,0)+a*b*c)
 return {w:c for w,c in out.items() if c!=0}
O={(0,1,2):1,(0,0):1/h,(1,1):q*q/h,(2,2):1/h}
for j in range(3):assert not add(mul(O,{(j,):1}),mul({(j,):1},O),-1)
for i in range(3):
 C={(i,i,i):1,(i,):-3*q/h**2}
 for j in range(3):
  comm=add(mul(C,{(j,):1}),mul({(j,):1},C),-1)
  for v in comm.values():
   num,den=s.cancel(v).as_numer_denom();assert s.rem(num,p,q)==0
# Odd variable permutation sends c3_i(q,t) to c3_perm(i)(q^-1,t').
assert s.cancel((q/h**2)*q*q-(1/q)/(q**-2-1)**2)==0
x,y,z=s.symbols('x y z');P=x*x+y*y+z*z;Q=x*y*z;R=x*x*y*y+y*y*z*z+z*z*x*x;J=(x*x-y*y)*(y*y-z*z)*(z*z-x*x)
Disc=P*P*R*R-4*R**3-4*P**3*Q*Q-27*Q**4+18*P*R*Q*Q
assert s.expand(J*J-Disc)==0
from itertools import product
for ep in product([1,-1],repeat=3):
 if ep[0]*ep[1]*ep[2]!=1:continue
 for k in range(3):
  vv=[x,y,z];sub={vv[i]:ep[i]*vv[(i+k)%3] for i in range(3)}
  for f in [P,Q,R,J]:assert s.expand(f.xreplace(sub)-f)==0
t=s.symbols('t')
Molien=(1/(1-t)**3+3/((1-t)*(1+t)**2)+8/(1-t**3))/12
assert s.cancel(Molien-(1-t**12)/((1-t**2)*(1-t**3)*(1-t**4)*(1-t**6)))==0
cert={'version':'classification-v61','universal_base':'q*(q-1)*(q+1) invertible','central_incidence_equations':['(q²+q+1) beta=0','(q²+q+1) gamma=0','(q²+q+1) delta=0'],'ordinary_proof':'Highest active degree kills all other coefficients by q-1 and q²-1 units; subtract Omega,c3x,c3y,c3z; all remaining central coefficients constant. Exact over nonreduced bases.','local_mixed_equations':'u beta=u gamma=u delta=0 at root3 pencil, components dimensions2 and4 meeting along dim1','tetrahedral_invariants':{'P':'x²+y²+z²','Q':'xyz','R':'x²y²+y²z²+z²x²','J':'(x²-y²)(y²-z²)(z²-x²)','relation':'J²=P²R²-4R³-4P³Q²-27Q⁴+18PRQ²'},'scope':'Universal centrality/divisibility and invariant identities exact; component and family interpretation are ordinary proofs, not global H3 moduli claims.'}
Path(__file__).with_name('cubic_quantum_triangle_incidence_certificate.json').write_text(json.dumps(cert,indent=2)+'\n')
print('PASS universal root3 central resonance, q-inversion and tetrahedral invariants')
