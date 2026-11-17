#!/usr/bin/env python3
"""Exact algebra for the two boundary cusps, conductor and torus-link model.

The all-n parametrization, analytic normalization, topological link theorem,
DHKK estimates, and Casals' construction have ordinary proofs in the paper.
This verifier uses only rational/integer/symbolic computations, no samples
as substitutes for proofs and no floating-point root classification.
"""
from pathlib import Path
from math import gcd
import json
import sympy as s

u,v,w,A,B,C,h,k,r,z=s.symbols('u v w A B C h k r z')
U,V,W=u,v,w
# g^{-1}=i_w i_u i_w i_v: start at the rightmost letter.
V=2*U*W-V-2*B
W=2*U*V-W-2*C
U=2*V*W-U-2*A
W=2*U*V-W-2*C
invg=[s.expand(t) for t in (U,V,W)]
# Initial branch: u=1/t, v=k, w=r/t+O(1).
# Substitution u=z, w=r*z records the exact leading Laurent terms.
lead=[]
for f,deg,coef in zip(invg,(5,2,7),(16*r**2,2*r,64*r**3)):
    poly=s.Poly(s.expand(f.subs({u:z,v:k,w:r*z})),z)
    assert poly.degree()==deg
    assert s.expand(poly.LC()-coef)==0
    lead.append({'pole':deg,'coefficient':str(coef)})
# Check the complete ambient relation is preserved, not merely its leading part.
H=u*v*w-(u*u+v*v+w*w)/2-A*u-B*v-C*w-h
for var,other,co in ((u,(v,w),A),(v,(w,u),B),(w,(u,v),C)):
    assert s.expand(H.subs(var,2*other[0]*other[1]-var-2*co)-H)==0

# Uniform induction: pole orders (c,b,c+b), r-exponents (b,a,a+b).
a,b,c=s.symbols('a b c', integer=True)
poles=[c,b,c+b]
r_exp=[b,a,a+b]
two_exp=[c-1,b-1,c+b-1]
steps=[1,2,0,2]
for i in steps:
    j,l=[x for x in range(3) if x!=i]
    poles[i]=s.expand(poles[j]+poles[l])
    r_exp[i]=s.expand(r_exp[j]+r_exp[l])
    two_exp[i]=s.expand(1+two_exp[j]+two_exp[l])
assert poles==[2*b+5*c,b+2*c,3*b+7*c]
assert r_exp==[2*a+5*b,a+2*b,3*a+7*b]
assert [s.expand(two_exp[i]-poles[i]+1) for i in range(3)]==[0]*3
# c=a+2b makes r-exponents the entries of the next Pell matrix.
assert s.expand((2*a+5*b)-(b+2*c)).subs(c,a+2*b)==0

records=[]
M=s.Matrix([[1,-2],[-2,5]])
for n in range(1,25):
    T=M**n
    an,bn,cn=int(T[0,0]),-int(T[0,1]),int(T[1,1])
    dn=bn+cn
    assert cn==an+2*bn and an*cn-bn*bn==1
    assert gcd(bn,cn)==1 and bn%2==0 and cn%2==1
    # x_n=2^{-b} r^{-a} t^b, y_n=2^{-c} r^{-b} t^c.
    assert -bn*bn+an*cn==1
    branch_delta=(bn-1)*(cn-1)//2
    intersection=bn*cn
    delta=2*branch_delta+intersection
    mu=(2*bn-1)*(2*cn-1)
    assert delta==1+2*bn*cn-dn
    assert mu==2*delta-1
    assert gcd(bn+cn,2*bn*cn)==1
    # Conductor exponent of either branch = its Milnor number + other intersection.
    conductor=(bn-1)*(cn-1)+bn*cn
    assert conductor==delta
    # Equal-parity Chebyshev extrema lie on the zero level.
    nodes=bn*cn+(bn-1)*(cn-1)
    extrema=bn*(cn-1)+(bn-1)*cn
    assert nodes==delta and extrema==delta-1 and nodes+extrema==mu
    if n<=4:
        records.append({'n':n,'a':an,'b':bn,'c':cn,'degree':2*dn,
                        'branch_delta':branch_delta,'branch_intersection':intersection,
                        'delta':delta,'Milnor_number':mu,'Milnor_fiber_genus':delta-1,
                        'homological_monodromy_order':2*bn*cn,'conductor_each':conductor,
                        'Chebyshev_nodes':nodes,'Chebyshev_other_critical_points':extrema})

# A concrete n=1 weighted initial germ with rational branch parametrizations.
x,y=s.symbols('x y')
b1,c1=2,5
f0=(y**b1-4*x**c1)*(y**b1-s.Rational(1,4)*x**c1)
g=s.groebner([s.diff(f0,x),s.diff(f0,y)],x,y,order='grevlex')
lms=[p.LM(order=g.order).exponents for p in g.polys]
standard=[]
for i in range(30):
    for j in range(30):
        if not any(i>=p and j>=q for p,q in lms):standard.append((i,j))
assert len(standard)==27
# Normalized branches x=t^2, y=2 t^5 and x=t^2, y=t^5/2.
# Modulo t^14 on both branches, each weight contributes rank min(2,#monomials).
conductor=14
ranks=[]
for weight in range(conductor+max(b1,c1)+1):
    reps=[j for j in range(weight//c1+1) if (weight-c1*j)%b1==0]
    mat=s.Matrix([[s.Integer(2)**j for j in reps],
                  [s.Rational(1,2)**j for j in reps]]) if reps else s.zeros(2,0)
    rank=mat.rank()
    assert rank==min(2,len(reps))
    ranks.append(rank)
assert sum(ranks[:conductor])==14
assert ranks[conductor-1]==1 and all(rank==2 for rank in ranks[conductor:])
# Characteristic polynomial from the weighted homogeneous Milnor formula.
T=s.symbols('T')
p,q=2*c1,2*b1
L=2*b1*c1
char=s.div(s.Poly((T**L-1)**2*(T-1),T),s.Poly((T**p-1)*(T**q-1),T))
assert char[1].is_zero and char[0].degree()==27
assert char[0].rem(s.Poly(s.cyclotomic_poly(L,T),T)).is_zero
assert s.div(char[0],s.Poly(T-1,T))[1].is_zero
# All monodromy factors divide T^L-1 (possibly with multiplicity).
sqfree=s.Poly(s.sqf_part(char[0].as_expr()),T)
assert s.rem(s.Poly(T**L-1,T),sqfree).is_zero

# Chebyshev real morsification, checked algebraically for p=10 and q=4.
zeta=s.symbols('zeta')
critical_values=[]
for d in (p,q):
    cheb=s.chebyshevt(d,x)
    der=s.diff(cheb,x)
    assert s.gcd(s.Poly(der,x),s.Poly(s.diff(der,x),x)).degree()==0
    res=s.Poly(s.resultant(der,cheb-zeta,x),zeta).monic()
    expected=s.Poly((zeta-1)**(d//2-1)*(zeta+1)**(d//2),zeta)
    assert s.expand(res.as_expr()-expected.as_expr())==0
    critical_values.append({'degree':d,'resultant_monic':str(res.as_expr())})

certificate={
 'date':'2026-11-17','version':'e6-connections-v27','status':'PASS',
 'field':'Q and Z; exact symbolic arithmetic',
 'new_curve_condition':'kappa^2!=1 and N_v(kappa)!=0; smooth ambient cubic',
 'inverse_first_leading':lead,
 'all_n_boundary_orders':'(b_n,c_n), gcd=1; inverse poles=(c_n,b_n,b_n+c_n)',
 'leading_ratio':'y^b_n/x^c_n = r, r+r^-1=2*kappa',
 'weighted_initial':'y^(2b)-2*kappa*x^c*y^b+x^(2c)',
 'link':'T(2b_n,2c_n), two T(b_n,c_n) components, linking b_n*c_n',
 'checked_integer_iterations':24,
 'examples':records,
 'n1_Jacobi_dimension':27,
 'n1_conductor_truncated_normalization_dimension':28,
 'n1_conductor_quotient_dimension':14,
 'n1_monodromy_charpoly':str(char[0].as_expr()),
 'Chebyshev_critical_value_resultants':critical_values,
 'ordinary_proof_inputs':['normalization and local Puiseux topology',
     'plane-curve conductor formula and Milnor monodromy',
     'all-n leading-term induction',
     'DHKK smooth proper comparison',
     'Casals Theorem 1.1 real-morsification construction'],
 'not_computer_certified':['analytic equivalence to the weighted homogeneous model',
     'global wrapped equivalence or equivariant mirror construction',
     'categorical entropy of a new endofunctor',
     'full old verification suite','novelty']}
Path(__file__).with_name('boundary_torus_links_certificate.json').write_text(
 json.dumps(certificate,ensure_ascii=False,indent=2)+'\n')
print('BOUNDARY TWO-BRANCH / TORUS LINK / CONDUCTOR / CHEBYSHEV: PASS')
for row in records:
    print(row)
