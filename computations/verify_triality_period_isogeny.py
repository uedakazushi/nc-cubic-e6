#!/usr/bin/env python3
"""Exact algebra for triality periods, the degree-three G2 map and hidden dynamics.

Topological homology actions, the Hodge-extension comparison and entropy use
ordinary proofs and cited results; the finite checks below are not substitutes.
"""
from pathlib import Path
from itertools import product
from collections import Counter
from math import gcd
import json
import sympy as s

a,b,u,v,w,h,lam=s.symbols('a b u v w h lambda', nonzero=True)
A,B,C=s.symbols('A B C')
vars=(u,v,w)
W=u*v*w-(u*u+v*v+w*w)/2-A*u-B*v-C*w
Ws=W.subs({A:lam,B:lam,C:lam})
B1=(u,2*u*v-w-2*lam,v)
B2=(w,v,2*v*w-u-2*lam)
def compose(f,g):
    return tuple(s.expand(z.subs(dict(zip(vars,g)), simultaneous=True)) for z in f)
for F in (B1,B2):
    assert s.expand(Ws.subs(dict(zip(vars,F)),simultaneous=True)-Ws)==0
    assert s.Matrix(F).jacobian(vars).det()==1
assert compose(B1,B2)==(w,u,v)
points=[(1,-1,-1),(-1,1,-1),(-1,-1,1),(1,1,1),(0,0,0)]
perms=[]
for F in (B1,B2):
    images=[]
    for p in points:
        d={**dict(zip(vars,p)),lam:0}
        images.append(points.index(tuple(z.subs(d) for z in F)))
    perms.append(images)
assert perms==[[0,2,1,3,4],[2,1,0,3,4]]
G=-2*s.eye(5)
for i in range(4):G[i,4]=G[4,i]=1
delta=s.Matrix([1,1,1,1,2])
for p in perms:
    P=s.Matrix.hstack(*[s.eye(5)[:,j] for j in p])
    assert P.T*G*P==G and P*delta==delta

# K basis (c,o1,o2,o3). Fixed c,sum(o_i) vs coinvariant c,o.
GK=s.Matrix([[-2,1,1,1],[1,-2,0,0],[1,0,-2,0],[1,0,0,-2]])
fixed=s.Matrix([[1,0],[0,1],[0,1],[0,1]])
coinv=s.Matrix([[1,0,0,0],[0,1,1,1]])
assert fixed.T*GK*fixed==s.Matrix([[-2,3],[3,-6]])
assert coinv*fixed==s.diag(1,3)
roots=[]
for vec in product(range(-3,4),repeat=4):
    col=s.Matrix(vec)
    if (col.T*GK*col)[0]==-2:roots.append(vec)
assert len(roots)==24
positive=[r for r in roots if all(x>=0 for x in r)]
restricted=Counter((r[0],sum(r[1:])) for r in positive)
assert restricted=={(1,0):1,(0,1):3,(1,1):3,(1,2):3,(1,3):1,(2,3):1}

short=(b,a*b,a*b*b)
long=(a,a*b**3,a*a*b**3)
S=sum(x+1/x for x in short)
L=sum(x+1/x for x in long)
la=(S+2)/4; hh=(L+3*S+4)/8
z=(-a*b*b,-a*b,-b,s.Integer(-1))
ui=[(zz+1/zz)/2 for zz in z]
N=(u*u+2*la*u+2*hh)*(u*u-1)+2*la**2*(1+u)
assert s.factor(N-s.prod(u-root for root in ui))==0
assert [s.factor(z[0]/z[1]),s.factor(z[1]/z[2]),s.factor(z[2]/z[3]),s.factor(z[2]*z[3])]==[b,a,b,b]
# A line section w=m, v=k*u+ell disjoint from the first three chosen components.
k=z[0]; m=(k+1/k)/2; ell=-(b+1)*(a*b+1)/2
assert s.factor(Ws.subs({v:k*u+ell,w:m,lam:la},simultaneous=True)-hh)==0
inc=[]
for zi,root in zip(z[:3],ui[:3]):
    ki=-2*la*zi/(zi-1)
    inc.append(s.factor(m-zi*(k*root+ell)-ki))
assert all(t!=0 for t in inc)
qsection=s.factor(-k+ell+m)
assert s.factor(qsection*qsection+2*la*qsection+1-2*la+2*hh)==0
# The two components above u=-1 are w+v=-lambda +/- sqrt(...).
assert s.factor((2*la)**2-((1-ui[0])*(1-ui[1])*(1-ui[2])*(1-ui[3])))==0

# Weyl reflections on the period torus; fixed-lattice restriction is (a,b^3).
r1={a:1/a,b:a*b}
r2={a:a*b**3,b:1/b}
for rr in (r1,r2):
    assert s.factor(S.subs(rr,simultaneous=True)-S)==0
    assert s.factor(L.subs(rr,simultaneous=True)-L)==0
beta=sum(x**3+x**-3 for x in short)
assert s.factor(beta-(S**3-3*S*L-9*S-6*L-12))==0
bc=-S-2; cc=L+3*S+4
assert s.factor(cc+2+3*bc-L)==0
assert s.factor(-bc**3+3*bc**2+3*bc*cc+3*bc-2-beta)==0
# The target G2 short variables can be a and a*b^3.
y1=a; y2=a*b**3
alpha_target=y1+1/y1+y2+1/y2+y1*y2+1/(y1*y2)
beta_target=y1/y2+y2/y1+y1*y1*y2+1/(y1*y1*y2)+y1*y2*y2+1/(y1*y2*y2)
assert s.factor(alpha_target-L)==0 and s.factor(beta_target-beta)==0
zeta=s.symbols('zeta')
for f in (L,beta):
    num,den=s.fraction(s.factor(f.subs(b,zeta*b)-f))
    assert s.rem(s.Poly(num,zeta),s.Poly(zeta*zeta+zeta+1,zeta)).is_zero

# Cyclotomic Klein example and its two companion components.
t=s.symbols('t')
phi=s.Poly(s.cyclotomic_poly(21,t),t,domain=s.QQ)
def cyc(expr):
    num,den=s.fraction(s.cancel(expr))
    n=s.Poly(num,t,domain=s.QQ).rem(phi)
    d=s.Poly(den,t,domain=s.QQ).rem(phi)
    return (n*s.invert(d,phi)).rem(phi).as_expr()
components=[]
bs=[]
for j in range(3):
    sub={a:t**3,b:t**(3+7*j)}
    Sj=cyc(S.subs(sub,simultaneous=True)); Lj=cyc(L.subs(sub,simultaneous=True))
    bj=cyc(-Sj-2); cj=cyc(Lj+3*Sj+4)
    assert Lj==-1 and cyc(beta.subs(sub,simultaneous=True))==-1
    assert cyc((bj+1)*(bj*bj+5*bj+1))==0
    for p,q in restricted:
        assert cyc((a**p*b**q-1).subs(sub,simultaneous=True))!=0
    assert cyc(((1+b)*(1+a*b)*(1+a*b*b)).subs(sub,simultaneous=True))!=0
    order=s.ilcm(7,21//gcd(21,3+7*j))
    assert int(order)==(7 if j==0 else 21)
    bs.append(bj)
    components.append({'j':j,'period_exponents_mod21':[3,3+7*j],
                       'Fricke_b':str(bj),'Fricke_c':str(cj),
                       'integral_extension_order':int(order)})
assert bs[0]==-1 and cyc(bs[1]+bs[2])==-5 and cyc(bs[1]*bs[2])==1
assert 4*(-1+3)**3-(-1+6*(-1)+12)**2==7
assert (-1)**2-4*(-1)-12==-7

# A homologically trivial word with hyperbolic modular matrix.
TL=s.Matrix([[1,0],[-1,1]]); TU=s.Matrix([[1,1],[0,1]])
Mg=TL**2*TU**-2
assert Mg==s.Matrix([[1,-2],[-2,5]]) and Mg.det()==1
assert all(x%2==y for x,y in zip(Mg,s.eye(2)))
qvar=s.symbols('qvar')
assert Mg.charpoly(qvar).as_expr()==qvar*qvar-6*qvar+1
Vieta=[(2*v*w-u-2*A,v,w),(u,2*u*w-v-2*B,w),(u,v,2*u*v-w-2*C)]
for F in Vieta:
    assert s.expand(W.subs(dict(zip(vars,F)),simultaneous=True)-W)==0
    assert s.Matrix(F).jacobian(vars).det()==-1

cert={
 'date':'2026-11-17','version':'e6-connections-v24','status':'PASS',
 'field':'Q Laurent identities, integer lattices, Q(zeta_21)',
 'Hurwitz_permutations_on_affine_D4':[p for p in perms],
 'fixed_lattice_Gram':[[-2,3],[3,-6]],'invariant_to_coinvariant':[[1,0],[0,3]],
 'positive_D4_restriction_multiplicities':{str(k):v for k,v in sorted(restricted.items())},
 'symmetric_periods':['b','a','b','b'],
 'symmetric_conic_lifts':['-a*b^2','-a*b','-b','-1'],
 'line_section_disjointness':[str(x) for x in inc],
 'coefficient_formula':['lambda=(S+2)/4','h=(L+3S+4)/8'],
 'isogeny':'(a,b)->(a,b^3), kernel mu3',
 'G2_base_formula':['alpha=L','beta=S^3-3SL-9S-6L-12'],
 'Fricke_base_formula':['b_F=-S-2','c_F=L+3S+4'],
 'Klein_components':components,
 'entropy_word':'B1^2 B2^(-2)=iota_v iota_w iota_u iota_w',
 'modular_matrix':[[1,-2],[-2,5]],'spectral_radius':'3+2*sqrt(2)',
 'ordinary_proof_inputs':['Goldman--Neumann homology theorem and local-system transport',
  'conic component contraction and Friedman period comparison',
  'Weyl invariant ring and quotient isogeny argument',
  'Hodge extension classification by period logarithms',
  'Boalch--Paluba G2 component interpretation',
  'Cantat--Loray dynamical-degree/entropy theorem'],
 'not_certified':['independent audit of older E6 classification or S5xS5',
  'canonical unmarked identification of all components',
  'isomorphism of algebraic surfaces or derived/Fukaya categories',
  'novelty or entire Gauss-Manin connection']}
Path(__file__).with_name('triality_period_isogeny_certificate.json').write_text(json.dumps(cert,ensure_ascii=False,indent=2)+'\n')
print('TRIALITY / PERIOD ISOGENY / KLEIN 7-21 / HIDDEN DYNAMICS: EXACT CHECKS PASS')
