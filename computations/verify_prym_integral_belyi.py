#!/usr/bin/env python3
"""Exact cyclic-cover arithmetic and X411/Belyi invariants.

Full-ramification injectivity, theta norm, Prym polarization type,
Kodaira classification and Shioda--Tate remain ordinary proofs.
"""
from pathlib import Path
from math import gcd, lcm
import json
import sympy as s

M=s.Matrix([[1,-2],[-2,5]])
records=[]
for n in range(1,11):
    A=M**n;b=-int(A[0,1]);c=int(A[1,1]);m=b//2;d=b*c
    assert b%2==0 and c%2==1 and gcd(b,c)==gcd(m,c)==1
    assert lcm(2*c,2*m)==d and lcm(4*c,4*m)==2*d
    # q' cyclic generator of order bc: a and y phases (1/2c,1/2m).
    for i,j in ((4*c,0),(0,4*m),(2*c,2*m),(-c,m),(-2*c,0)):
        assert (s.Rational(i,2*c)+s.Rational(j,2*m)).q==1
    # q cyclic generator of order 2bc, y phase h/(4m) with h=3 mod4.
    h=next(j for j in range(3,8*m+4,4) if gcd(j,4*m)==1)
    for i,j in ((4*c,0),(0,4*m),(2*c,2*m),(-2*c,2*m),(-3*c,m)):
        assert (s.Rational(i,4*c)+s.Rational(h*j,4*m)).q==1
    # q' ramification: 4 fully ramified; 2 points with inertia m;
    # 2 points with inertia c. Riemann--Hurwitz checks the genus.
    ram=4*(d-1)+2*(d-2*c)+2*(d-b)
    gC=2*d-b-c;gT=4*d-b-2*c-1
    assert ram==2*gT-2 and (gT-gC)==gC+b-1
    assert lcm(d,m,c)==d # maximal etale quotient of q has degree 2
    records.append({'n':n,'b':b,'c':c,'degree_cyclic_qprime':d,
      'degree_cyclic_q':2*d,'Prym_dimension':gT-gC,
      'elliptic_theta_degree':d,'Prym_theta_type':f'(1^{b-1},2^{gC})',
      'qprime_ramification':'4*(bc); 2 fibers with 2c points of index m; 2 with b points of index c'})

k,t=s.symbols('kappa t')
a2=-2*k;a4=s.Integer(1)
c4=s.expand(16*(a2*a2-3*a4))
Delta=s.expand(16*a4*a4*(a2*a2-4*a4))
j=s.factor(c4**3/Delta)
assert Delta==64*(k*k-1) and c4==16*(4*k*k-3)
assert s.factor(j-1728-64*k*k*(8*k*k-9)**2/(k*k-1))==0
assert s.factor(s.diff(j,k)-128*k*(4*k*k-3)**2*(8*k*k-9)/(k*k-1)**2)==0
c4inf=s.expand(16*((-2*t)**2-3*t**4))
Dinf=s.expand(16*t**8*((-2*t)**2-4*t**4))
assert s.expand(c4inf-16*t*t*(4-3*t*t))==0
assert s.expand(Dinf-64*t**10*(1-t*t))==0
# Belyi passport and Shioda--Tate rank of X411.
assert 2*3==3*2==4+1+1==6
assert 10-2-8==0

# Monodromy of the degree-six Belyi cover: all transitive branch triples
# of passport (3,3), (2,2,2), (4,1,1) generate the same order-24 group.
from itertools import permutations
from sympy.combinatorics import Permutation, PermutationGroup
g_inf=Permutation(0,1,2,3,size=6)
compatible=[]
for tup in permutations(range(6)):
    g_zero=Permutation(list(tup))
    if sorted(len(cyc) for cyc in g_zero.cyclic_form)!=[3,3]:continue
    g_1728=(g_zero*g_inf)**-1
    if sorted(len(cyc) for cyc in g_1728.cyclic_form)!=[2,2,2]:continue
    G=PermutationGroup([g_zero,g_1728])
    if G.is_transitive():
        assert G.order()==24
        assert G.derived_subgroup().order()==12
        assert G.derived_subgroup().derived_subgroup().order()==4
        compatible.append([g_zero.cyclic_form,g_1728.cyclic_form])
assert len(compatible)==4

cert={'date':'2026-11-18','version':'e6-connections-v31','status':'PASS',
 'arithmetic':'exact rational polynomials and integer congruences',
 'records':records[:6],'instances_checked':len(records),
 'full_cyclic_cover_degree':'2bc','maximal_etale_degree':2,
 'qprime_cyclic_cover_degree':'bc','four_total_ramification_points':True,
 'kernel_q_pullback':'<[(0,0)-O]> of order 2',
 'theta_degree_on_embedded_D':'bc',
 'elliptic_j':'64*(4*kappa^2-3)^3/(kappa^2-1)',
 'kodaira':'I1, I1, I4*','Miranda_Persson':'X411, Mordell-Weil Z/2',
 'belyi_passport':{'0':[3,3],'1728':[2,2,2],'infinity':[4,1,1]},
 'belyi_monodromy':'S4, faithful degree-six coset action on S4/C4',
 'compatible_transitive_branch_triples_fixed_infinity':len(compatible),
 'ordinary_inputs_not_computationally_certified':[
   'cyclic covering function fields and local ramification indices',
   'totally ramified pullback on Jacobians is injective',
   'div(z)=2(0,0)-2O and the associated etale double cover',
   'theta pullback and ramified Prym polarization',
   'Tate Kodaira fiber criterion and Miranda-Persson classification'],
 'not_claimed':['integral splitting of the whole Prym',
   'an MF equivalence from a two-isogeny','analytically deformed Prym sector','novelty']}
Path(__file__).with_name('prym_integral_belyi_certificate.json').write_text(
 json.dumps(cert,indent=2)+'\n')
print('PRYM CYCLIC COVER / THETA DEGREE / X411 BELYS: EXACT CHECKS PASS')
for row in records[:3]:
    print('n=',row['n'],'(b,c)=',row['b'],row['c'], 'theta=',row['elliptic_theta_degree'])
