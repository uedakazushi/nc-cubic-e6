#!/usr/bin/env python3
"""Exact checks for the two boundary branches of g^{-n}{v=kappa}.

All-n asymptotics, Puiseux classification, torus-link identification,
normalization, and multiplier ideals have ordinary proofs in the paper.
This script does not prove those statements by finite sampling.
"""
from __future__ import annotations
import json
from collections import Counter
from fractions import Fraction
from math import gcd
from pathlib import Path
import sympy as s

u,v,w,A,B,C,h,k,z,t,w0 = s.symbols('u v w A B C h kappa z t w0')
W=u*v*w-(u*u+v*v+w*w)/2-A*u-B*v-C*w
# Individual generators preserve the equation for arbitrary coefficients.
for var,expr in ((u,2*v*w-u-2*A),(v,2*u*w-v-2*B),(w,2*u*v-w-2*C)):
    assert s.expand(W.subs(var,expr)-W)==0

# g^{-1}=iota_w iota_u iota_w iota_v, applied from the right.
V1=2*u*w-v-2*B
W1=2*u*V1-w-2*C
U1=2*V1*W1-u-2*A
W2=2*U1*V1-W1-2*C
for expr,pole,coefficient in ((U1,5,16*z*z),(V1,2,2*z),(W2,7,64*z**3)):
    scaled=s.expand(t**pole*expr.subs({u:1/t,v:k,w:z/t+w0},simultaneous=True))
    polynomial=s.Poly(scaled,t)
    assert polynomial.coeff_monomial(1)==coefficient
    assert polynomial.degree()>=0

# Smoothness of the initial projective conic is the stated determinant.
G0=s.Matrix([[1,-k,A],[-k,1,C],[A,C,k*k+2*B*k+2*h]])
conic_det=(1-k*k)*(k*k+2*B*k+2*h)-A*A-C*C-2*k*A*C
assert s.expand(G0.det()-conic_det)==0
assert s.expand(s.discriminant(z*z-2*k*z+1,z)-4*(k-1)*(k+1))==0

# General induction of leading Laurent monomials.
aa,bb,cc=s.symbols('a b c', integer=True)
# Triples: pole order, exponent of 2, exponent of z.
leadU=s.Matrix([cc,cc-1,bb]);leadV=s.Matrix([bb,bb-1,aa]);leadW=s.Matrix([bb+cc,bb+cc-1,aa+bb])
mult2=s.Matrix([0,1,0])
newV=leadU+leadW+mult2
newW=leadU+newV+mult2
newU=newV+newW+mult2
newW=newU+newV+mult2
an=aa+2*bb;bn=2*cc+bb;cn=5*cc+2*bb
for actual,target in ((newU,s.Matrix([cn,cn-1,bn])),
                      (newV,s.Matrix([bn,bn-1,an])),
                      (newW,s.Matrix([bn+cn,bn+cn-1,an+bn]))):
    assert all(s.expand(q.subs(cc,aa+2*bb))==0 for q in actual-target)
# All candidate leading products dominate the terms subtracted: symbolic positive differences.
assert s.expand((cc+(cc+bb))-bb)==2*cc
assert s.expand((cc+(2*cc+bb))-(cc+bb))==2*cc
assert s.expand(((2*cc+bb)+(3*cc+bb))-cc)==4*cc+2*bb
assert s.expand(((5*cc+2*bb)+(2*cc+bb))-(3*cc+bb))==4*cc+2*bb

M=s.Matrix([[1,-2],[-2,5]])
records=[]
for n in range(1,25):
    Mn=M**n
    a=int(Mn[0,0]);b=-int(Mn[0,1]);c=int(Mn[1,1]);d=b+c
    assert a*c-b*b==1 and c==a+2*b and 0<a<b<c and gcd(b,c)==1
    # Local leading coefficients are x=2^-b z^-a t^b, y=2^-c z^-b t^c.
    assert -b*b+a*c==1  # y^b/x^c has leading coefficient z.
    branch_delta=(b-1)*(c-1)//2
    delta=2*branch_delta+b*c
    mu=(2*b-1)*(2*c-1)
    assert delta==1+2*b*c-b-c and mu==2*delta-1
    q,r=c,b;cf=[]
    while r:
        m,rem=divmod(q,r);cf.append(m);q,r=r,rem
    assert cf==[2]*(2*n) and sum(cf)==4*n
    lct=Fraction(b+c,2*b*c)
    # Lower bounds on all toric log discrepancy ratios are exact rational tests.
    if n<=3:
        for rr in range(1,31):
            for ss in range(1,31):
                value=Fraction(rr+ss,min(2*c*rr,2*b*ss))
                assert value>=lct
        semigroup={i*b+j*c for i in range(c) for j in range(b)}
        gaps=[i for i in range(b*c-b-c+1) if i not in semigroup]
        assert len(gaps)==branch_delta
        # Eigenvalue exponents of X^(2c)+Y^(2b) in Z/(2bc).
        period=2*b*c
        actual=Counter((c*i+b*j)%period for i in range(1,2*b) for j in range(1,2*c))
        expected={e:2+int(e==0)-int(e%b==0)-int(e%c==0) for e in range(period)}
        assert all(actual[e]==expected[e] for e in range(period))
        assert sum(actual.values())==mu
    if n<=5:
        records.append({'n':n,'b':b,'c':c,'link':[2*b,2*c],
                        'delta_each':branch_delta,'intersection':b*c,
                        'delta_total':delta,'Milnor_number':mu,
                        'Milnor_fiber_genus':delta-1,'corner_blowups':4*n,
                        'log_canonical_threshold':str(lct)})

# Entire reduced face polynomial and the first concrete monodromy polynomial.
x,y,T=s.symbols('x y T')
face=(y**2-z*x**5)*(y**2-x**5/z)
assert s.expand(face-(y**4-(z+1/z)*x**5*y**2+x**10))==0
chi_num=s.Poly((T**20-1)**2*(T-1),T)
chi_den=s.Poly((T**4-1)*(T**10-1),T)
quotient,remainder=s.div(chi_num,chi_den)
assert remainder.is_zero and quotient.degree()==27
assert s.rem(s.Poly(T**20-1,T),s.Poly(s.prod(p for p,m in s.factor_list(quotient)[1]),T)).is_zero

certificate={
 'date':'2026-11-17','version':'e6-connections-v28','status':'PASS',
 'arithmetic':'Q-polynomial identities, integer matrices and rational numbers',
 'inverse_word':'iota_w iota_u iota_w iota_v (right to left)',
 'parameter_conditions':'U smooth; kappa^2!=1; projective conic determinant!=0',
 'initial_inverse_Laurent_terms':['16*z^2*t^-5','2*z*t^-2','64*z^3*t^-7'],
 'general_branch_terms':['x=2^-b*z^-a*t^b*(1+O(t))','y=2^-c*z^-b*t^c*(1+O(t))'],
 'face':'y^(2b)-2*kappa*x^c*y^b+x^(2c)',
 'tested_matrix_indices':[1,24],
 'small_n_semigroups_and_eigenvalue_multisets':[1,2,3],
 'examples':records,
 'first_monodromy_polynomial':str(quotient.as_expr()),
 'separate_proof_inputs':['all-n Laurent induction and compactification',
   'Newton-Puiseux and nondegenerate equisingularity',
   'torus link identification and Milnor fibration',
   'toric log resolution and multiplier ideals',
   'normalization exact sequence and localization',
   'Dyckerhoff Corollary 6.5 and Morita invariance (not computer verified)'],
 'not_claimed':['analytic equivalence to a weighted homogeneous germ',
   'global Milnor fibration of U or iteration map',
   'repeated tests prove all-n geometric conclusions',
   'newness of general torus-link or Newton formulas',
   'full main-paper compilation or rerun of previous 32 scripts',
   'GitHub push']}
Path(__file__).with_name('boundary_thresholds_certificate.json').write_text(json.dumps(certificate,indent=2)+'\n')
print('BOUNDARY THRESHOLDS / LOCAL MF DIMENSIONS (EXACT FINITE ALGEBRA): EXACT CHECKS PASS')
for r in records[:3]:print(r)
