#!/usr/bin/env python3
"""Exact Cayley, torus-Poisson, D4-unfolding and Jacobi-algebra checks.

All computations are symbolic over Q. Geometric identifications, analytic
right-equivalence, and claims about the real elliptope have ordinary proofs.
"""
import json
from pathlib import Path
import sympy as s

u, v, w, r, t = s.symbols('u v w r t')
x, y, ell, L, z = s.symbols('x y ell L z')
a, b, c = s.symbols('alpha beta gamma')
H = u*v*w - (u*u+v*v+w*w)/2
phi = s.Matrix([s.diff(H, j) for j in (u,v,w)])
J = phi.jacobian((u,v,w))
R = u*u+v*v+w*w+2*u*v*w-1
assert s.expand(J.det()-R)==0
nodes=[(-1,-1,-1),(-1,1,1),(1,-1,1),(1,1,-1)]
node_records=[]
for p in nodes:
    d=dict(zip((u,v,w),p))
    assert R.subs(d)==0
    assert all(s.diff(R,j).subs(d)==0 for j in (u,v,w))
    assert s.hessian(R,(u,v,w)).subs(d).det()==-32
    assert J.subs(d).rank()==1
    assert list(phi.subs(d))==[-2*j for j in p]
    other=dict(zip((u,v,w),[-2*j for j in p]))
    assert list(phi.subs(other))==[-2*j for j in p]
    assert J.subs(other).det()==27
    node_records.append({'node':p,'parameter':[-2*j for j in p],
                         'other_sheet':[-2*j for j in p]})

# Torus quotient and the exact Poisson normalization.
U=-(r+1/r)/2
V=-(t+1/t)/2
W=-(r*t+1/(r*t))/2
assert s.factor(R.subs({u:U,v:V,w:W}))==0
def torus_bracket(f,g):
    return s.factor(r*t*(s.diff(f,r)*s.diff(g,t)-s.diff(f,t)*s.diff(g,r)))
for f,g,k in ((U,V,w),(V,W,u),(W,U,v)):
    assert s.factor(torus_bracket(f,g)+s.diff(R,k).subs({u:U,v:V,w:W})/2)==0
# Trace commutator formula x^2+y^2+z^2-xyz-2=2.
assert s.expand((-2*u)**2+(-2*v)**2+(-2*w)**2-(-2*u)*(-2*v)*(-2*w)-4-4*R)==0

# Exact splitting at the corank-two point (-1,-1,-1), base (2,2,2).
Wabc=H-(2+a)*u-(2+b)*v-(2+c)*w
shift=s.expand(Wabc.subs({u:-1+x,v:-1+y,w:-1+ell-x-y}))
split=s.expand(shift.subs(ell,L+x*y-c))
local=-x*y*(x+y)+s.Rational(1,2)*x*x*y*y
constant=s.Rational(7,2)+a+b+c+c*c/2
expected=-L*L/2+local-c*x*y-(a-c)*x-(b-c)*y+constant
assert s.expand(split-expected)==0
# Saturate the two-variable Jacobi ideal away from its other critical point.
jac=[s.diff(local,x),s.diff(local,y)]
g=s.groebner([*jac,z*(y-3)-1],z,x,y,order='lex')
local_equations=[p.as_expr() for p in g.polys if not p.as_expr().has(z)]
g0=s.groebner(local_equations,x,y,order='lex')
for f in (x*x+2*x*y,y*y+2*x*y,x*x*y,x*y*y):
    assert g0.reduce(f)[1]==0
basis=[s.S.One,x,y,x*y]
coeff_mat=s.Matrix([[s.Poly(g0.reduce(bi)[1],x,y).coeff_monomial(mon)
                    for bi in basis] for mon in (1,x,y,y*y)])
assert coeff_mat.det()!=0
# Parameter classes span the nonconstant local Jacobi algebra.
parameter_classes=[-x,-y,x+y-x*y]
param=s.Matrix([[s.Poly(g0.reduce(f)[1],x,y).coeff_monomial(mon)
                 for f in parameter_classes] for mon in (x,y,y*y)])
assert param.det()!=0
# Cubic tangent cone has three distinct factors; cyclic tangent action order 3.
f3=-x*y*(x+y)
assert s.expand(f3.subs({x:y,y:-x-y},simultaneous=True)-f3)==0
T=s.Matrix([[0,1],[-1,-1]])
assert T**3==s.eye(2)

# Reference fiber (2,2,2) has total length five; one simple sheet at (2,2,2).
ge=s.groebner([v*w-u-2,w*u-v-2,u*v-w-2],u,v,w,order='grevlex')
leading=[p.LM(order=ge.order).exponents for p in ge.polys]
standard=[]
for n in range(7):
    for i in range(n+1):
        for j in range(n+1-i):
            ex=(i,j,n-i-j)
            if not any(all(ex[k]>=lm[k] for k in range(3)) for lm in leading):
                standard.append(ex)
assert len(standard)==5

# Origin: etale cover, even though the Casimir norm has a repeated root.
points=[(0,0,0),(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)]
B=[s.S.One,u,v,w,u*v*w]
E=s.Matrix([[h.subs(dict(zip((u,v,w),p))) for h in B] for p in points])
jacobians=[J.det().subs(dict(zip((u,v,w),p))) for p in points]
assert jacobians==[-1,4,4,4,4]
assert E.det()!=0
residue=E.T*s.diag(*[s.Rational(1,int(j)) for j in jacobians])*E
assert residue.det()!=0
omega_bar=u*v*w-u*u-v*v-w*w
values=[omega_bar.subs(dict(zip((u,v,w),p))) for p in points]
assert values==[0,-2,-2,-2,-2]
assert s.Matrix([[value**j for j in range(5)] for value in values]).det()==0
assert s.expand((-J).det()+R)==0

cert={
 'date':'2026-11-17','version':'e6-connections-v19','status':'PASS',
 'field':'Q; symbolic exact arithmetic',
 'gradient_map':'(vw-u,wu-v,uv-w)',
 'ramification_equation':'u^2+v^2+w^2+2uvw-1=0',
 'nodes_and_fibers':node_records,
 'torus_map':'u=-(r+r^-1)/2, v=-(t+t^-1)/2, w=-(rt+(rt)^-1)/2',
 'torus_Poisson':'{r,t}=rt gives {u,v}=-(1/2) R_w, cyclic',
 'D4_residual_germ':'-xy(x+y)+(x^2*y^2)/2',
 'local_Jacobi_dimension':4,
 'D4_unfolding':'-gamma*xy-(alpha-gamma)*x-(beta-gamma)*y, plus constant',
 'parameter_class_matrix_determinant':str(param.det()),
 'reference_fiber_length':5,
 'local_triality_tangent_matrix':[[0,1],[-1,-1]],
 'origin_evaluation_determinant':str(E.det()),
 'origin_residue_pairing_determinant':str(residue.det()),
 'origin_Casimir_values_divided_by_f_over_3':values,
 'caveat':'Repeated Casimir values do not imply ramification of the five-sheet cover.',
 'not_computer_certified':['invariant ring generation proof','analytic D4 right-equivalence',
   'infinitesimal versality criterion','real strict concavity proof',
   'global mirror/Fukaya equivalence','identification of distinct D4 lattices','novelty']}
Path(__file__).with_name('cayley_lg_connections_certificate.json').write_text(
 json.dumps(cert,indent=2,default=lambda x:int(x))+'\n')
print('CAYLEY / TORUS POISSON / D4 / JACOBI: ALL EXACT CHECKS PASS')
print('Local versality det:',param.det(),'residue pairing det:',residue.det())
