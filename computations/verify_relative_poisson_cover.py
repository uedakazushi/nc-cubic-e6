#!/usr/bin/env python3
"""Exact degree-15 origin fiber and S5 simple-fold computations.

Global flatness, finite etale splitting and Galois conclusions use the
independent algebraic proofs in the manuscript.
"""
import json
from pathlib import Path
import sympy as s

q=(-1+s.sqrt(-3))/2
K=s.QQ.algebraic_field(s.sqrt(-3))
X,Y,Z,O,t=s.symbols('X Y Z Omega t')
D=s.symbols('D')
u,v,w,Q=s.symbols('u v w Q')
a,b,c=s.symbols('a b c')
f=(1-q)/3
e=-(2*q+1)/9
assert K.from_sympy(s.expand(e**3+f**3/27))==K.zero

P=O**3+f*O**2-X*Y*Z+e*(X**2+Y**2+Z**2)
g=s.groebner([P,*[s.diff(P,z) for z in (X,Y,Z)]],
            X,Y,Z,O,domain=K,order='grevlex')
lead=[h.LM(order=g.order).exponents for h in g.polys]
std=[]
for n in range(8):
 for i in range(n+1):
  for j in range(n+1-i):
   for k in range(n+1-i-j):
    m=(i,j,k,n-i-j-k)
    if not any(all(m[d]>=z[d] for d in range(4)) for z in lead):
     std.append(m)
assert len(std)==15
vars=(X,Y,Z,O);ix={m:i for i,m in enumerate(std)}
mat=s.zeros(15,15)
for j,m in enumerate(std):
 mon=s.prod(z**power for z,power in zip(vars,m))
 for ex,cf in s.Poly(g.reduce(-O*mon)[1],*vars,domain=K).terms():
  mat[ix[ex],j]=cf
wanted=s.expand(D**2*(D-f)*(D+f/3)**4*(D-2*f/3)**8)
assert s.Poly(mat.charpoly(D).as_expr()-wanted,D,domain=K).is_zero

# Homogeneous projective critical equations near the X=1 infinity vertex.
la=((2*q+1)*a**3+2*(q-1)*a+3*q*b*c)/9
lb=((2*q+1)*b**3+2*(q-1)*b+3*q*c*a)/9
lc=((2*q+1)*c**3+2*(q-1)*c+3*q*a*b)/9
PX=-Y*Z+t*(2*e-a*O)+t*t*la
PY=-Z+t*(2*e*Y-b*O)+t*t*lb
PZ=-Y+t*(2*e*Z-c*O)+t*t*lc
jinf=s.Matrix([PX,PY,PZ]).jacobian([t,Z,Y]).det().subs(
      {Y:0,Z:0,O:0,t:0})
assert K.from_sympy(jinf)!=K.zero

r=1-q
jchar=s.Matrix([r*Y*Z-t-a*t*t,r*Z-Y*t-b*t*t,
                r*Y-Z*t-c*t*t]).jacobian([t,Z,Y]).det().subs(
                {Y:0,Z:0,t:0})
assert K.from_sympy(jchar)!=K.zero

# Five-sheet polynomial map, its simple fold and other three sheets.
F=[v*w-u,w*u-v,u*v-w]
J=s.Matrix(F).jacobian([u,v,w])
Jdet=s.factor(J.det())
assert Jdet==u*u+v*v+w*w+2*u*v*w-1
fold={u:s.Rational(1,2),v:s.Rational(1,2),w:s.Rational(1,2)}
assert [h.subs(fold) for h in F]==[-s.Rational(1,4)]*3
assert J.subs(fold).rank()==2
for point in [(s.Rational(5,4),-1,-1),
              (-1,s.Rational(5,4),-1),
              (-1,-1,s.Rational(5,4))]:
 subs=dict(zip((u,v,w),point))
 assert [h.subs(subs) for h in F]==[-s.Rational(1,4)]*3
 assert Jdet.subs(subs)==s.Rational(81,16)
h=s.symbols('h')
assert s.expand(h*h-h+s.Rational(1,4)-(h-s.Rational(1,2))**2)==0

# Universal one-dimensional Casimir and separation of five sheets.
rr=1-Q
xx=u/rr;yy=v/rr;zz=w/rr
av=(v*w-u)/rr;bv=(w*u-v)/rr;cv=(u*v-w)/rr
Om=xx*yy*zz+((Q-1)*(xx*xx+zz*zz)+(Q+2)*yy*yy)/3
Om-=(Q+2)*(av*xx+Q*bv*yy+cv*zz)/3
Om_expected=(1-Q)*(u*v*w-u*u-v*v-w*w)/9
num,den=s.fraction(s.cancel(Om-Om_expected))
assert s.rem(s.Poly(num,Q),s.Poly(Q*Q+Q+1,Q)).is_zero
sgn=[(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)]
Cas=f*(u*v*w-u*u-v*v-w*w)/3
for point in sgn:
 subs=dict(zip((u,v,w),point))
 assert [s.expand(s.diff(Cas,z).subs(subs)) for z in (u,v,w)]==[
  -f*s.Integer(t)/3 for t in point]
 assert J.subs(subs)*s.Matrix(point)==s.Matrix(point)

cert={
 'date':'2026-11-17','version':'e6-relative-poisson-v17','status':'PASS',
 'field':'Q(sqrt(-3))','critical_origin_length':15,
 'origin_critical_polynomial':'D^2*(D-2*f/3)^8*(D-f)*(D+f/3)^4',
 'node_quintic_at_origin':'D*(D-2*f/3)^4',
 'other_quintic_at_origin':'(D-f)*(D+f/3)^4',
 'origin_standard_monomials':[str(s.prod(z**p for z,p in zip(vars,m)))
                             for m in std],
 'infinity_critical_local':'3 vertices, each Omega^3',
 'infinity_character_local':'3 reduced vertices',
 'critical_infinity_Jacobian':str(s.simplify(jinf)),
 'character_infinity_Jacobian':str(s.simplify(jchar)),
 'character_map':'(v*w-u,w*u-v,u*v-w)',
 'character_map_jacobian':'u^2+v^2+w^2+2uvw-1',
 'simple_fold':'A=B=C=-1/4; (1/2,1/2,1/2) double, three others simple',
 'other_fiber_jacobian':'81/16',
 'character_Casimir':'(f/3)*(uvw-u^2-v^2-w^2)',
 'monodromy':'S5 by connected prime degree cover with a simple fold',
 'not_computer_certified':['relative projective Bezout/flatness',
     'etale splitting','global N5^2*M5 factorization','S5 group argument',
     'irreducibility of companion M5','all H3 conditions','novelty']}
Path(__file__).with_name('relative_poisson_cover_certificate.json').write_text(
 json.dumps(cert,indent=2)+'\n')
print('RELATIVE POISSON DEGREE-15 / S5: EXACT CHECKS PASS')
