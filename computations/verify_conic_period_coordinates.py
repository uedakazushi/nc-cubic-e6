#!/usr/bin/env python3
"""Exact checks for conic-marked D4 periods and rational splitting examples.

The contraction, line-bundle gluing, Friedman period comparison and mixed
Hodge splitting argument are ordinary proofs, not proved by this program.
"""
from pathlib import Path
from itertools import combinations, product
import json
import sympy as s
from sympy.matrices.normalforms import smith_normal_form

u,A,B,C,h,z=s.symbols('u A B C h z')
N=(u*u+2*A*u+2*h)*(u*u-1)+B*B+C*C+2*u*B*C
Q=s.Matrix([[-1,u,-B],[u,-1,-C],[-B,-C,-u*u-2*A*u-2*h]])
assert s.expand(Q.det()-N)==0
assert s.expand(N.subs(u,1)-(B+C)**2)==0
assert s.expand(N.subs(u,-1)-(B-C)**2)==0
coefficient_map=s.Matrix([2*A,2*h-1,2*B*C-2*A,B*B+C*C-2*h])
coef_det=s.factor(coefficient_map.jacobian((A,B,C,h)).det())
assert s.expand(coef_det-16*(C*C-B*B))==0
assert s.factor(s.diff((z+1/z)/2,z)*z-(z-1/z)/2)==0

# Picard(F1 blown up at five points), basis section, fiber, E1,...,E5.
G=s.diag(-1,0,-1,-1,-1,-1,-1)
G[0,1]=G[1,0]=1
v=[s.eye(7)[:,i] for i in range(7)]
S,F=v[:2]; E=v[2:]
D=s.Matrix.hstack(2*S+2*F-sum(E,s.zeros(7,1)),E[4],F-E[4])
roots=s.Matrix.hstack(E[0]-E[1],E[1]-E[2],E[2]-E[3],E[2]+E[3]-F)
cartan=s.Matrix([[-2,1,0,0],[1,-2,1,1],[0,1,-2,0],[0,1,0,-2]])
assert D.T*G*roots==s.zeros(3,4)
assert roots.T*G*roots==cartan
assert cartan.det()==4
assert D.T*G*D==s.Matrix([[-1,1,1],[1,-1,1],[1,1,-1]])
exp=s.Matrix([[1,-1,0,0],[0,1,-1,0],[0,0,1,-1],[0,0,1,1]])
assert exp.det()==2
assert -exp*exp.T==cartan
snf=smith_normal_form(exp,domain=s.ZZ)
assert sorted(abs(int(snf[i,i])) for i in range(4))==[1,1,1,2]

# Root characters and the conic discriminant factorization.
z1,z2,z3,z4=s.symbols('z1 z2 z3 z4', nonzero=True)
zz=(z1,z2,z3,z4)
ui=[(x+1/x)/2 for x in zz]
for i,j in combinations(range(4),2):
    assert s.factor(ui[i]-ui[j]-(zz[i]-zz[j])*(zz[i]*zz[j]-1)/(2*zz[i]*zz[j]))==0
root_vectors=[]
for i,j in combinations(range(4),2):
    for a,b in product((-1,1),repeat=2):
        vec=[0]*4;vec[i]=a;vec[j]=b
        root_vectors.append(vec)
assert len(root_vectors)==24
# One-pair identity proves the Vandermonde factorization in the manuscript.

# Smooth rational split example: N=(2u+1)(8u^3-6u+1)/16.
split={A:s.Rational(1,4),B:s.Rational(1,2),C:s.Rational(1,4),h:s.Rational(1,8)}
Ns=s.Poly(N.subs(split),u)
assert s.factor(Ns.as_expr()-(2*u+1)*(8*u**3-6*u+1)/16)==0
assert s.gcd(Ns,Ns.diff()).degree()==0
assert Ns.eval(1)==s.Rational(9,16) and Ns.eval(-1)==s.Rational(1,16)
# z^8*? N((z+1/z)/2) has precisely all nontrivial ninth roots.
cyclotomic_identity=s.factor(16*z**4*Ns.as_expr().subs(u,(z+1/z)/2))
assert s.expand(cyclotomic_identity-sum(z**i for i in range(9)))==0
assert s.factor(cyclotomic_identity-(z*z+z+1)*(z**6+z**3+1))==0

# Smooth rational nonsplit example from z=(2,3,4,6).
nums=list(map(s.Rational,[2,3,4,6]))
uv=[(x+1/x)/2 for x in nums]
Nn=s.Poly(s.prod(u-x for x in uv),u)
cm=Nn.all_coeffs()
An=cm[1]/2; hn=(cm[2]+1)/2
# The chosen square roots of N(1), N(-1) fix B and C.
sumBC=s.prod(x-1 for x in nums)/(4*s.sqrt(s.prod(nums)))
diffBC=s.prod(x+1 for x in nums)/(4*s.sqrt(s.prod(nums)))
Bn=s.simplify((sumBC+diffBC)/2); Cn=s.simplify((sumBC-diffBC)/2)
non={A:An,B:Bn,C:Cn,h:hn}
assert s.Poly(s.expand(N.subs(non)-Nn.as_expr()),u).is_zero
assert s.gcd(Nn,Nn.diff()).degree()==0 and Nn.eval(1)!=0 and Nn.eval(-1)!=0
assert all(v.is_Rational for v in non.values())
# All sheet choices are 2^+-1,3^+-1,4^+-1,6^+-1, never roots of unity.
assert all(x>1 for x in nums)

certificate={
 'date':'2026-11-17','version':'e6-connections-v23','status':'PASS',
 'field':'Q, integral lattices and formal Laurent identities',
 'conic_discriminant':'(u^2+2Au+2h)(u^2-1)+B^2+C^2+2uBC',
 'coefficient_jacobian':str(coef_det),
 'root_basis_Gram':cartan.tolist(),
 'period_exponent_matrix':exp.tolist(),'period_exponent_determinant':2,
 'four_periods':['z1/z2','z2/z3','z3/z4','z3*z4'],
 'D4_roots_count':len(root_vectors),
 'pair_identity':'ui-uj=(zi-zj)(zi*zj-1)/(2zi*zj)',
 'discriminant_factor':'Disc(N)=prod_{i<j}(zi-zj)^2(zi*zj-1)^2/(2^12*(z1*z2*z3*z4)^6)',
 'split_rational_parameters':{str(k):str(v) for k,v in split.items()},
 'split_polynomial':str(Ns.as_expr()),
 'split_cyclotomic_identity':'16*z^4*N((z+z^-1)/2)=(z^9-1)/(z-1)',
 'nonsplit_rational_parameters':{str(k):str(v) for k,v in non.items()},
 'nonsplit_conic_sheet_coordinates':['2','3','4','6'],
 'ordinary_proof_inputs':['conic bundle contraction to F1',
  'gluing of multidegree-zero line bundles on a boundary triangle',
  'Friedman Proposition 3.12: exponential integral period equals restriction',
  'mixed Hodge weights and rational splitting criterion'],
 'not_computer_certified':['geometric existence of a compatible marking',
  'algebraic de Rham connection matrices','global H3 admissibility',
  'mirror or Fukaya equivalence','novelty','whole manuscript compilation']}
Path(__file__).with_name('conic_period_coordinates_certificate.json').write_text(
 json.dumps(certificate,indent=2,default=int)+'\n')
print('CONIC / FOUR D4 PERIODS / CYCLOTOMIC MHS: EXACT CHECKS PASS')
print('split:',split)
print('nonsplit:',non)
