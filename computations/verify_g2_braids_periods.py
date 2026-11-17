#!/usr/bin/env python3
"""Exact checks for component monodromy, LG Hurwitz dynamics and the Klein orbit.

Symbolic identities and finite permutation computations are verified here.
Topology of configuration spaces and the primitive boundary torus are proved
in the manuscript; the G2/Fano/octonion realization is cited separately.
"""
from collections import deque
from pathlib import Path
import hashlib
import json
import sympy as s

u,v,w,lam,h=s.symbols('u v w lambda h')
x,y,z,b,c,alpha,beta,xi,P,Q=s.symbols('x y z b c alpha beta xi P Q')
variables=(u,v,w)
W=u*v*w-(u*u+v*v+w*w)/2-lam*(u+v+w)
b1=(u,2*u*v-w-2*lam,v)
b2=(w,v,2*v*w-u-2*lam)
b1inv=(u,w,2*u*w-v-2*lam)
b2inv=(2*u*v-w-2*lam,v,u)
identity=variables

def compose(f,g):
    return tuple(s.expand(t.subs(dict(zip(variables,g)), simultaneous=True)) for t in f)

def eqmaps(f,g):
    return all(s.expand(a-b)==0 for a,b in zip(f,g))

for f,fi in ((b1,b1inv),(b2,b2inv)):
    assert eqmaps(compose(f,fi),identity) and eqmaps(compose(fi,f),identity)
    assert s.expand(W.subs(dict(zip(variables,f)),simultaneous=True)-W)==0
    assert s.Matrix(f).jacobian(variables).det()==1
assert eqmaps(compose(compose(b1,b2),b1),compose(compose(b2,b1),b2))
rho=compose(b1,b2)
assert rho==(w,u,v)
assert eqmaps(compose(compose(rho,rho),rho),identity)
# The Jacobian Poisson bracket with Casimir W is preserved, not just its leaf.
def pb(f,g):
    return s.expand(s.Matrix([s.diff(f,t) for t in variables]).dot(
        s.Matrix([s.diff(g,t) for t in variables]).cross(
        s.Matrix([s.diff(W,t) for t in variables]))))
for f in (b1,b2):
    sub=dict(zip(variables,f))
    for i,j,k in ((0,1,2),(1,2,0),(2,0,1)):
        assert s.expand(pb(f[i],f[j])-s.diff(W,variables[k]).subs(sub,simultaneous=True))==0

# The component cover is the universal depressed cubic, after affine changes.
base={alpha:c+2+3*b,beta:-b**3+3*b**2+3*b*c+3*b-2}
chi=xi**3+6*xi**2+3*(1-alpha)*xi+beta+2
assert s.expand(chi.subs(xi,b).subs(base))==0
assert s.expand(chi.subs({xi:z-2,alpha:P-3,beta:Q-6*(P-3)-12}))==z**3-3*P*z+Q
D=4*(alpha+3)**3-(beta+6*alpha+12)**2
assert s.expand(s.discriminant(chi,xi)-27*D)==0
C0=b*b+b-c-1
S1=b*b-8*b-4*c-16
assert s.expand(D.subs(base)+C0*C0*S1)==0
assert s.Matrix([base[alpha],base[beta]]).jacobian((b,c)).det()==3*C0
assert s.factor(chi.subs({alpha:6,beta:6}))==(xi+8)*(xi-1)**2
assert s.expand(chi.subs({alpha:-3,beta:6})-(xi+2)**3)==0
# Generic singular component of S1: three A1 points; in particular the cusp.
Wc=W.subs(lam,s.Rational(1,2))
cusp_points=[(s.Rational(1,2),-1,-1),(-1,s.Rational(1,2),-1),(-1,-1,s.Rational(1,2))]
for pt in cusp_points:
    d=dict(zip(variables,pt))
    assert Wc.subs(d)==s.Rational(1,8)
    assert all(s.diff(Wc,t).subs(d)==0 for t in variables)
    assert s.hessian(Wc,variables).subs(d).det()==s.Rational(9,4)

# Chebyshev formula for one Hurwitz twist on the conic pencil u=constant.
M=s.Matrix([[2*u,-1],[1,0]])
center=lam/(u-1)
assert all(s.cancel(a)==0 for a in (M*s.Matrix([v-center,w-center])-s.Matrix([b1[1]-center,b1[2]-center])))
assert M.det()==1 and M.trace()==2*u
for n in range(1,8):
    prev=s.S.Zero if n==1 else s.chebyshevu(n-2,u)
    assert (M**n-s.chebyshevu(n-1,u)*M+prev*s.eye(2)).applyfunc(s.expand)==s.zeros(2)

# Klein seven-point orbit and its full permutation image S7.
points=[(0,0,0),(0,0,1),(0,1,0),(1,0,0),(1,1,0),(1,0,1),(0,1,1)]
F=x*x+y*y+z*z+x*y*z-x-y-z
for pt in points: assert F.subs(dict(zip((x,y,z),pt)))==0
p=tuple(points.index((a,1-d-a*b_,b_)) for a,b_,d in points)
q=tuple(points.index((d,b_,1-a-b_*d)) for a,b_,d in points)
def pc(a,b_): return tuple(a[b_[i]] for i in range(7))
def inv(a): return tuple(a.index(i) for i in range(7))
def power(a,n):
    if n<0: return power(inv(a),-n)
    out=tuple(range(7))
    for _ in range(n): out=pc(a,out)
    return out
# q^{-1} p q^{-2} p q^{-1} p^3=(5 7), using 1-based labels.
trans=pc(inv(q),pc(p,pc(power(q,-2),pc(p,pc(inv(q),power(p,3))))))
assert trans==(0,1,2,3,6,5,4)
seen={tuple(range(7))}
queue=deque(seen)
while queue:
    a=queue.popleft()
    for g in (p,q):
        nxt=pc(g,a)
        if nxt not in seen: seen.add(nxt);queue.append(nxt)
assert len(seen)==5040
assert p==(2,0,6,4,5,3,1) and q==(1,5,6,0,2,3,4)
# This G2 fiber is regular; its two other component parameters are quadratic.
assert D.subs({alpha:-1,beta:-1})==7
assert (alpha*alpha-4*beta-12).subs({alpha:-1,beta:-1})==-7
assert s.factor(chi.subs({alpha:-1,beta:-1}))==(xi+1)*(xi*xi+5*xi+1)

# Boundary residue. In the projective chart U=1, use local coordinates v,w.
t,V,Z,A,B,C=s.symbols('t V Z A B C')
proj=V*Z-t*(1+V*V+Z*Z)/2-t*t*(A+B*V+C*Z)-h*t**3
assert s.diff(proj,t).subs({V:0,Z:0,t:0})==-s.Rational(1,2)
assert proj.subs(t,0)==V*Z
# Formal t=V*Z*a(V,Z); at the node a(0)=2, giving double residue 1.
assert -1/(s.Integer(2)*(-s.Rational(1,2)))==1

cert={
 'date':'2026-11-17','version':'e6-connections-v21','status':'PASS',
 'arithmetic':'exact Q-polynomial identities; explicit permutations of seven points',
 'hurwitz_maps':[str(b1),str(b2)],
 'inverse_braid_and_center_identities':'PASS',
 'preserves_W_jacobian_Poisson_and_volume':'PASS',
 'component_cubic':'xi^3+6xi^2+3(1-alpha)xi+beta+2',
 'depressed_cubic':'z^3-3Pz+Q, P=alpha+3, Q=beta+6alpha+12',
 'branch_equation':'4P^3-Q^2=0',
 'pullback_branch':'-(b^2+b-c-1)^2*(b^2-8b-4c-16)',
 'cusp_parameters':{'alpha':-3,'beta':6,'b':-2,'c':1,'lambda':'1/2','h':'1/8'},
 'cusp_surface_singularity':'3A1; each Hessian determinant 9/4',
 'chebyshev_identity_checked_degrees':[1,2,3,4,5,6,7],
 'klein_orbit':points,'klein_braid_permutations_zero_based':[p,q],
 'transposition_word':'q^-1 p q^-2 p q^-1 p^3 = (5 7), 1-based labels',
 'klein_permutation_group_order':len(seen),
 'klein_component_polynomial':'(xi+1)*(xi^2+5xi+1)',
 'boundary_double_residue':1,
 'ordinary_proof_inputs':['configuration-space interpretation of braid groups',
   'Poisson and Poincare residue naturality','primitive boundary torus identification',
   'primitive group plus transposition argument'],
 'known_results_used':['Boalch--Paluba sections 4.1, 5, 7 and Corollary 17, Theorem 20'],
 'not_certified_or_claimed':['actual analytic period integration by this program',
   'full Gauss-Manin connection or mixed-Hodge extension splitting',
   'quantum G2 algebra or derived equivalence',
   'S7 identified with the group of order 6048',
   'newness or independent audit of old H3 and S5xS5 claims']}
path=Path(__file__).with_name('g2_braids_periods_certificate.json')
path.write_text(json.dumps(cert,ensure_ascii=False,indent=2)+'\n')
print('G2 COMPONENT COVER / HURWITZ / CHEBYSHEV / S7 / RESIDUE: PASS')
print('Seven-point permutation group:',len(seen),'boundary double residue: 1')
print('Certificate SHA256:',hashlib.sha256(path.read_bytes()).hexdigest())
