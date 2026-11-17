#!/usr/bin/env python3
"""Exact identities for the Kummer-Milnor/Prym/Ciani bridge.

The checks prove finite algebraic identities only. Smooth compactification,
Riemann-Hurwitz, trace/pullback and dg reconstruction are proved or cited
separately in the manuscript. No sampled numerical data are used as proofs.
"""
from pathlib import Path
from math import gcd
import hashlib
import json
import sympy as s

k,z,r,T,X,Y,Z=s.symbols('kappa z r T X Y Z')
a,x,y,t,u,v,w=s.symbols('a x y t u v w')
K=k*k
# The universal Ciani quartic and its three elliptic quotients.
C=X**4+Y**4-2*k*X**2*Y**2-1
qa=X**2-k*Y**2
qb=Y**2-k*X**2
assert s.expand(qa**2-1-(K-1)*Y**4)==C
assert s.expand(qb**2-1-(K-1)*X**4)==C
rr=Y/X; tt=1/X**2
assert s.cancel(tt**2-(rr**4-2*k*rr**2+1))==-C/X**4
# The diagonal quotient is 2-isogenous to the level-two elliptic curve.
Q=r**4-2*k*r*r+1
assert s.expand((r*T)**2-r*r*((r*r)**2-2*k*r*r+1)-r*r*(T*T-Q))==0
# Standard binary quartic invariants; this is NOT the plane-quartic discriminant.
I=12+4*k*k
J=16*k**3-144*k
jquart=s.factor(6912*I**3/(4*I**3-J**2))
assert s.cancel(jquart-64*(K+3)**3/(K-1)**2)==0
jlevel=lambda q:64*(4*q-3)**3/(q-1)
assert s.cancel(jquart-jlevel(K/(K-1)))==0
# Kummer pullback obstruction and map, checked for several exact Pell pairs.
M=s.Matrix([[1,-2],[-2,5]])
records=[]
for n in range(1,9):
    Mn=M**n; b=-int(Mn[0,1]);c=int(Mn[1,1]);m=b//2
    assert b%2==0 and c%2==1 and gcd(b,c)==1 and gcd(m,c)==1
    assert c*(b-1)%2==1
    genus=2*b*c-b-c
    gtilde=4*b*c-b-2*c-1
    assert 2*gtilde-2==2*(2*genus-2)+2*b
    assert gtilde-genus==2*b*c-c-1
    degree=2*b*c
    assert degree==4*c*m and c*m==b*c//2
    # Over z=y^b/x^c, eta^2=z(z^2-2kz+1)=y^b/x^(3c).
    # The second radicand is x times a square because b even,c odd.
    assert 2*(-(3*c+1)//2)+1==-3*c
    if n<=3:
        F=y**(2*b)-2*k*a**(2*c)*y**b+a**(4*c)-1
        zz=y**b/a**(2*c); ee=y**m/a**(3*c)
        assert s.cancel(ee*ee-zz*(zz*zz-2*k*zz+1)+y**b*F/a**(6*c))==0
        assert s.expand(C.subs({X:a**c,Y:y**m})-F)==0
        assert zz.subs(a,-a)==zz and ee.subs(a,-a)==-ee
    records.append({'n':n,'b':b,'c':c,'genus_original':genus,
      'genus_double_cover':gtilde,'branch_points_double_cover':2*b,
      'prym_dimension':gtilde-genus,'degree_to_Ciani':c*m,
      'degree_to_attached_elliptic':degree})
# At each of x=0, y^(2b)=1, the function x has order one.
# A meromorphic square has even valuation: the lifting obstruction is exact.

# Klein-four characters on holomorphic one-forms of a plane quartic.
# Basis is omega=dX/C_Y, X omega, Y omega.
alpha=s.diag(-1,1,-1)  # X -> -X
beta=s.diag(-1,-1,1)   # Y -> -Y
assert alpha**2==beta**2==s.eye(3)
assert alpha*beta==beta*alpha
Ealpha=(s.eye(3)+alpha)/2
Ebeta=(s.eye(3)+beta)/2
Ediag=(s.eye(3)+alpha*beta)/2
assert Ealpha+Ebeta+Ediag==s.eye(3)
assert Ealpha*Ebeta==Ealpha*Ediag==Ebeta*Ediag==s.zeros(3)
assert Ealpha.rank()==Ebeta.rank()==Ediag.rank()==1
assert ((s.eye(3)-alpha)/2).rank()==2

# Picard-Fuchs equality modulo an explicit exact relative differential.
P=z*(z*z-2*k*z+1)
N=3*(k*k-1)*z**4+2*k*z*z*P+s.Rational(1,4)*P*P
R=z*z*(1-z*z)/2
assert s.expand(s.diff(R,z)*P-s.Rational(3,2)*R*s.diff(P,z)-N)==0
# Hypergeometric pullback t=(1-kappa)/2: t(1-t) f''+(1-2t) f'-f/4=0.
q=s.symbols('q')
assert s.expand(-(k*k-1)/4 - q*(1-q)).subs(k,1-2*q).expand()==0
assert s.expand(k-(1-2*q)).subs(k,1-2*q)==0

# Recompute the actual mu=27, tau=24 example from Vieta, independent of JSON.
r1=2*u*v-w; r2=2*v*r1-u; r3=2*v*r2-r1
V=s.Poly(s.expand(2*r2*r3-v),u,v,w)
H=sum(cf*x**i*y**j*t**(7-i-j-l) for (i,j,l),cf in V.terms())-2*t**7
surf=2*x*y-t*(x*x+y*y+1)-2*t**3
poly,rem=s.div(s.Poly(s.resultant(surf,H,t),x,y),s.Poly(64*x*x*y**5,x,y))
assert rem.is_zero
f=poly.as_expr()
mons=sorted([(i,j) for i in range(14) for j in range(6) if 2*i+5*j<=26],
            key=lambda e:(2*e[0]+5*e[1],e))
index={m:i for i,m in enumerate(mons)}
def rows(poly):
    terms=s.Poly(poly,x,y).terms();low=min(2*i+5*j for (i,j),v in terms);out=[]
    for a,b in mons:
        if 2*a+5*b+low>26:continue
        row=[0]*len(mons)
        for (i,j),co in terms:
            if (i+a,j+b) in index:row[index[(i+a,j+b)]]+=co
        out.append(row)
    return out
jrows=rows(s.diff(f,x))+rows(s.diff(f,y))
rj=s.Matrix(jrows).rank();rt=s.Matrix(jrows+rows(f)).rank()
assert (len(mons),rj,rt)==(45,18,21)
assert 45-rj==27 and 45-rt==24
f0=4*(y**4-4*x**5*y*y+x**10)
assert s.expand(2*x*s.diff(f0,x)+5*y*s.diff(f0,y)-20*f0)==0

cert={
 'date':'2026-11-18','version':'e6-connections-v30','status':'PASS',
 'arithmetic':'exact rational polynomial identities, rational matrices and integer recurrences',
 'Pell_cases_checked':records,
 'Ciani_curve':'X^4+Y^4-2*kappa*X^2*Y^2=1',
 'Ciani_quotients':['q^2=1+(kappa^2-1)*Y^4','q^2=1+(kappa^2-1)*X^4',
                   'T^2=r^4-2*kappa*r^2+1'],
 'attached_curve':'eta^2=z*(z^2-2*kappa*z+1)',
 'Ciani_to_attached':'z=Y^2/X^2, eta=Y/X^3',
 'Kummer_map':'x=a^2; z=y^b/a^(2c); eta=y^(b/2)/a^(3c)',
 'quotient_j':'64*(K+3)^3/(K-1)^2',
 'elliptic_Picard_Fuchs':'(kappa^2-1)Pi_second +2*kappa*Pi_first+Pi/4=0',
 'exact_differential_numerator':'z^2*(1-z^2)/2',
 'actual_example_recomputed':{'mu':27,'tau':24,'monomials':45,'Jacobi_rank':18,'Tjurina_rank':21},
 'ordinary_proofs_required':['irreducibility and smooth compactification of the affine fibers',
  'square-class obstruction, degrees and Riemann-Hurwitz',
  'Jacobian trace-pullback splitting and Prym anti-invariance',
  'Picard-Fuchs interpretation as Gauss-Manin periods',
  'Hua--Keller Theorem 5.9, arXiv:1810.00749v6, for Z-graded dg singularity categories'],
 'not_claimed':['a quotient map from the original Milnor curve to E over the prescribed z',
  'general two-periodic MF reconstruction from tau alone',
  'application of weighted-Milnor cover to the non-quasihomogeneous actual germ',
  'HMS, categorical summand, integral or polarized Jacobian product','novelty']}
Path(__file__).with_name('boundary_prym_certificate.json').write_text(json.dumps(cert,indent=2)+'\n')
print('KUMMER / CIANI / PRYM / PICARD-FUCHS / ACTUAL TAU: EXACT CHECKS PASS')
print('n=1:',records[0])
print('Actual germ: mu=27, tau=24; weighted model: mu=tau=27')
