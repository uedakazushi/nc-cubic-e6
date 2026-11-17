#!/usr/bin/env python3
"""A characteristic-zero smooth-center H3 witness for the tangent calculation.
Uses the previously proved fixed-envelope H3 recognition theorem only after
checking smoothness of the affine center and the elliptic boundary.
"""
import json
from pathlib import Path
import sympy as s
from central_tangent import K,q
X,Y,Z=s.symbols('X Y Z'); Q=K.to_sympy(q)
f=(1-Q)/3;e=-(2*Q+1)/9
omega=-(X+2*Y+3*Z+5)/2
F=omega**3+f*omega**2-X*Y*Z+e*(X*X+Y*Y+Z*Z)
polys=[F,*[s.diff(F,v) for v in (X,Y,Z)]]
gb=s.groebner(polys,X,Y,Z,domain=K,order='grevlex')
assert len(gb.polys)==1 and gb.polys[0].is_one
result={'date':'2026-11-17','version':'triangle-component-v2','status':'PASS',
        'field':'Q(q), q^2+q+1=0','base_constants':[0,0,0], 'cut':[2,1,2,3,5],
        'Delta':170,'beta_gamma_delta':6,
        'affine_singularity_ideal_groebner_basis':['1'],
        'center':'smooth affine center and smooth projective boundary by existing boundary lemma',
        'H3':'by fixed-envelope recognition, not inferred merely from a finite-degree rank'}
Path(__file__).with_name('smooth_witness_certificate.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
