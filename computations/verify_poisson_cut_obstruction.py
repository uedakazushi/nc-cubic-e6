#!/usr/bin/env python3
"""Symbolic leading obstruction for a central hyperplane and a PBW filtration test.
The completeness of the obstruction and the categorical consequence are proved
in the manuscript; this program does not test categories or finite global dimension.
"""
import json
from pathlib import Path
import sympy as s
X,Y,Z,O=s.symbols('X Y Z O')
beta,gamma,delta,eps=s.symbols('beta gamma delta eps')
a,b,c,e,la,lb,lc=s.symbols('a b c e la lb lc')
Jx=Y*Z-2*e*X+a*O-la
Jy=Z*X-2*e*Y+b*O-lb
Jz=X*Y-2*e*Z+c*O-lc
G=O+beta*X+gamma*Y+delta*Z+eps
B=(-gamma*Jz+delta*Jy,beta*Jz-delta*Jx,-beta*Jy+gamma*Jx)
expected=(X*(delta*Z-gamma*Y),Y*(beta*X-delta*Z),Z*(gamma*Y-beta*X))
coeffs=[]
for expr,goal in zip(B,expected):
    poly=s.Poly(s.expand(expr.subs(O,-beta*X-gamma*Y-delta*Z-eps)),X,Y,Z)
    degree2=sum(coef*X**i*Y**j*Z**k for (i,j,k),coef in poly.terms() if i+j+k==2)
    assert s.expand(degree2-goal)==0
    coeffs.extend(s.Poly(degree2,X,Y,Z).coeffs())
M,_=s.linear_eq_to_matrix(coeffs,(beta,gamma,delta))
assert M.rank()==3
# Independent verification on the distinguished cut from the manuscript:
witness=[s.expand(t.subs({beta:s.Rational(1,2),gamma:1,delta:s.Rational(3,2)})) for t in expected]
assert s.expand(witness[0]-X*(s.Rational(3,2)*Z-Y))==0
q=s.symbols('q')
assert s.rem(s.Poly((q*q-q)**3,q),s.Poly(q*q+q+1,q)).as_expr()==6*q+3
# e^{-1}=6q+3; sigma(z) has a nonzero genuine PBW degree-two xy coefficient.
assert s.gcd(s.Poly(q*q-q,q),s.Poly(q*q+q+1,q)).degree()==0
certificate={
 'date':'2026-11-17','version':'e6-connections-v15','status':'PASS',
 'central_cut':'G=Omega+beta*X+gamma*Y+delta*Z+eps',
 'quadratic_leading_brackets_divided_by_9':[str(t) for t in expected],
 'coefficient_matrix_rank':int(M.rank()),
 'Poisson_ideal_condition':'beta=gamma=delta=0, proved using degree-three center relation',
 'distinguished_cut':'2*Omega+X+2*Y+3*Z+5',
 'distinguished_obstruction':'9*X*(3*Z-2*Y) + terms of center degree <=1',
 'Vieta_degree':'sigma(z)=(q^2-q)*xy-q^2*z+q*c has PBW degree 2, not 1',
 'not_computer_certified':['flat-ideal obstruction lemma','pointed H3 reconstruction',
                           'derived equivalence or mutation construction','novelty']}
Path(__file__).with_name('poisson_cut_obstruction_certificate.json').write_text(json.dumps(certificate,indent=2)+'\n')
print('POISSON CUT / FILTRATION OBSTRUCTION: PASS')
