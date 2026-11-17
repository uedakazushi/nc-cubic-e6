#!/usr/bin/env python3
"""Exact audit: ten Poisson-zero points and four singular Casimir fibers.

A1 type and singularities of the total center are verified algebraically.
The equivalence with strong H3 relies separately on the existing
fixed-envelope H3 hyperplane criterion, not on this computation alone.
"""
import json
from pathlib import Path
import sympy as s
q=s.symbols('q')
X,Y,Z,O=s.symbols('X Y Z Omega')
f=(1-q)/3
E=-(2*q+1)/9
s3=s.Poly(q*q+q+1,q)
def red(expr):
    t=s.cancel(expr)
    num,den=s.fraction(t)
    n=s.rem(s.Poly(num,q),s3).as_expr()
    d=s.rem(s.Poly(den,q),s3).as_expr()
    return s.cancel(n/d)
assert red(E**3+f**3/27)==0
P=O**3+f*O**2-X*Y*Z+E*(X**2+Y**2+Z**2)
P_g=[s.diff(P,v) for v in (X,Y,Z)]
P_O=s.diff(P,O)
H=s.hessian(P,(X,Y,Z))
H4=s.hessian(P,(X,Y,Z,O))
assert red((O**3+f*O**2+4*E**3) - (O-f/3)*(O+2*f/3)**2)==0
D=s.symbols('D')
assert red(((-D)**3+f*(-D)**2) - D**2*(f-D))==0
assert red(((-D)**3+f*(-D)**2+4*E**3) + (D+f/3)*(D-2*f/3)**2)==0
cases=[('node_origin',0,(0,0,0),True),
       ('tangent_origin',-f,(0,0,0),False)]
signs=[(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)]
for signs3 in signs:
    assert signs3[0]*signs3[1]*signs3[2]==1
    cases.extend([(f'node_{signs3}',-2*f/3,signs3,True),
                  (f'tangent_{signs3}',f/3,signs3,False)])
records=[]
for label,w,eps,is_node in cases:
    C={X:2*E*eps[0],Y:2*E*eps[1],Z:2*E*eps[2],O:w}
    assert red(P.subs(C))==0,label
    assert all(red(t.subs(C))==0 for t in P_g),label
    assert (red(P_O.subs(C))==0)==is_node,label
    det=red(H.subs(C).det())
    assert det!=0,label
    expected=8*E**3 if eps==(0,0,0) else -32*E**3
    assert red(det-expected)==0,label
    if not is_node: assert red(P_O.subs(C)-f*f)==0,label
    else: assert red(H4.subs(C).det())!=0,label
    records.append({'label':label,'Omega':str(s.expand(w)),
                    'center_singular':is_node,'A1_hessian_det':str(det)})
assert len(records)==10
# Check the five 1D characters at a=b=c=0 and their central values.
for eps in [(0,0,0),*signs]:
    x0,y0,z0=[s.Integer(t)/(1-q) for t in eps]
    assert all(red((1-q)*v*w-u)==0 for u,v,w in ((x0,y0,z0),(y0,z0,x0),(z0,x0,y0)))
    central=[v**3+q*q*v for v in (x0,y0,z0)]
    assert all(red(central[i]-2*E*eps[i])==0 for i in range(3))
    o0=x0*y0*z0+(q-1)*(x0*x0+z0*z0)/3+(q+2)*y0*y0/3
    assert red(o0-(0 if eps==(0,0,0) else -2*f/3))==0
# D=-Omega: H3 status below is taken from a separate existing theorem.
byD=[{'D':'0','nodes':1,'total_center_singular':True,'H3_via_existing_criterion':True},
     {'D':'2f/3','nodes':4,'total_center_singular':True,'H3_via_existing_criterion':True},
     {'D':'f','nodes':1,'total_center_singular':False,'H3_via_existing_criterion':False},
     {'D':'-f/3','nodes':4,'total_center_singular':False,'H3_via_existing_criterion':False}]
cert={'date':'2026-11-17','version':'triangle-component-v16','status':'PASS',
      'base_field':'Q(q), q^2+q+1=0','identity':'e^3=-f^3/27',
      'critical_equations':'YZ=2eX, ZX=2eY, XY=2eZ',
      'zero_poisson_points':len(records), 'singular_total_center_points':5,
      'smooth_total_center_poisson_zeros':5,
      'roots_at_sign_points':'(Omega-f/3)(Omega+2f/3)^2',
      'formal_smoothing_origin':'D^2*(f-D)',
      'formal_smoothing_sign':'-(D+f/3)*(D-2*f/3)^2',
      'critical_points':records,'casimir_fibers':byD,
      'one_dimensional_characters':'five, exactly the five singular points of the total center',
      'limits':['H3 status uses the fixed-envelope classification theorem',
                'numerical symmetry is not a proof of newness',
                'Poisson-zero set classification is geometric support, not scheme multiplicity',
                'no categorical equivalence or Azumaya conclusion']}
path=Path(__file__).with_name('casimir_poisson_leaves_certificate.json')
path.write_text(json.dumps(cert,indent=2)+'\n')
print('CASIMIR POISSON CRITICAL POINTS: PASS')
print('total center singular / smooth Poisson zeros:',5,5)
for c in byD:print(c)
