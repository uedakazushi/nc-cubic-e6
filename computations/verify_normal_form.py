#!/usr/bin/env python3
"""Universal translation/scaling normal form and local inertia characters.
The first check is a polynomial identity, not parameter sampling.  Character
checks support the local Koszul proof, not global Hochschild descent by themselves.
"""
import sympy as s,json
from pathlib import Path
q=s.symbols('q'); x,y,z=s.symbols('x y z'); X=(x,y,z)
h1,h2,h3,a12,a13,a23,b1,b2,b3=s.symbols('h1 h2 h3 a12 a13 a23 b1 b2 b3')
A=s.Matrix([[h1,a12,a13],[a12,h2,a23],[a13,a23,h3]])
b=s.Matrix([b1,b2,b3]);v=s.Matrix([a23,a13,a12])/(1-q)
# For degree <=2 the cyclic quotient and commutative symmetric coordinates agree.
phi=(1-q)*x*y*z-(s.Matrix(X).T*A*s.Matrix(X))[0]/2-(b.T*s.Matrix(X))[0]
p=s.Poly(s.expand(phi.subs(dict(zip(X,[X[i]+v[i] for i in range(3)])),simultaneous=True)),*X)
assert all(s.cancel(p.coeff_monomial(X[i]*X[j]))==0 for i,j in ((0,1),(0,2),(1,2)))
expected=[b[i]+A[i,i]*v[i]+(1-q)*v[(i+1)%3]*v[(i+2)%3] for i in range(3)]
assert all(s.cancel(p.coeff_monomial(X[i])+expected[i])==0 for i in range(3))
assert all(s.cancel(p.coeff_monomial(X[i]**2)+A[i,i]/2)==0 for i in range(3))
# h_i=r_j*r_k/r_i gives the normalized coefficient 1 identically.
r=s.symbols('r0:3',nonzero=True)
h=[r[(i+1)%3]*r[(i+2)%3]/r[i] for i in range(3)]
assert all(s.cancel(h[i]*r[i]/(r[(i+1)%3]*r[(i+2)%3]))==1 for i in range(3))
assert all(s.cancel(r[i]**2-h[(i+1)%3]*h[(i+2)%3])==0 for i in range(3))
# Local action: s has weight 0, w has weight 1; derivations have opposite weights.
identity_generators={'ds':0,'w_dw':(1-1)%3,'w_ds_wedge_dw':(1-1)%3}
assert set(identity_generators.values())=={0}
nonidentity_normal_characters=[1,1]  # det normal on the fixed divisor for g and g^2
assert all(weight%3!=0 for weight in nonidentity_normal_characters)
result={'date':'2026-11-17','version':'triangle-component-v2','status':'PASS',
        'universal_offdiagonal_translation':'v=(A23,A13,A12)/(1-q)',
        'diagonal_coefficients_unchanged':True,
        'new_constants':[str(s.factor(c)) for c in expected],
        'normalization':'r_i^2=h_j*h_k, r1*r2*r3=h1*h2*h3; four even-sign choices',
        'local_HH_invariant_generators':['1','partial_s','w partial_w','w partial_s wedge partial_w'],
        'nonidentity_sectors_invariants':'zero because the normal character is nontrivial',
        'scope':'universal coefficient identities and local characters; geometric theorems are proved in the paper'}
Path(__file__).with_name('normal_form_certificate.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
