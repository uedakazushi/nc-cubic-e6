#!/usr/bin/env python3
"""Exact singular-locus certificates for five nodal H3 cuts of quantum so(3).

The algebraic verification is over Q(sqrt(-3)), using one of two conjugate
primitive cubic roots.  The H3 conclusion separately uses the fixed-envelope
recognition theorem (thm:quantum-triangle-full-H3); this script checks its
finite algebraic hypotheses, not categorical finite global dimension itself.
"""
import json
from pathlib import Path
import sympy as sp

X, Y, Z, O = sp.symbols('X Y Z O')
q = (-1 + sp.sqrt(-3)) / 2
K = sp.QQ.algebraic_field(sp.sqrt(-3))
f, e = (1-q)/3, -(2*q+1)/9
P = O**3 + f*O**2 - X*Y*Z + e*(X**2+Y**2+Z**2)
xyz = (X, Y, Z)
node_signs = [(0, 0, 0), (1, 1, 1), (1, -1, -1),
              (-1, 1, -1), (-1, -1, 1)]
results = []

for signs in node_signs:
    if signs == (0, 0, 0):
        point = {X: sp.S.Zero, Y: sp.S.Zero, Z: sp.S.Zero, O: sp.S.Zero}
        label = 'origin'
    else:
        point = {X: 2*e*signs[0], Y: 2*e*signs[1],
                 Z: 2*e*signs[2], O: -2*f/3}
        label = ''.join('+' if x == 1 else '-' for x in signs)
    D = sp.expand(-(2*point[O] + point[X] + 2*point[Y] + 3*point[Z]))
    F = sp.expand(P.subs(O, -(X+2*Y+3*Z+D)/2))
    ideal_generators = [F] + [sp.diff(F, v) for v in xyz]
    gb = sp.groebner(ideal_generators, *xyz, order='grevlex', domain=K)
    # Containment I <= m_p follows by direct substitution.
    assert all(K.from_sympy(sp.expand(g.subs(point))) == K.zero
               for g in ideal_generators)
    # The reverse containment m_p <= I is verified by exact division.
    assert len(gb.polys) == 3
    assert all(gb.reduce(v-point[v])[1] == 0 for v in xyz)
    # A nondegenerate quadratic tangent cone makes this exactly an A1 node.
    hess = sp.hessian(F, xyz).subs({v: point[v] for v in xyz})
    hdet = sp.expand(hess.det())
    assert K.from_sympy(hdet) != K.zero
    results.append({
        'label': label,
        'D': str(sp.simplify(D)),
        'node_xyz': [str(sp.simplify(point[v])) for v in xyz],
        'jacobian_ideal': 'maximal ideal of the indicated node',
        'groebner_basis': [str(sp.simplify(h.as_expr())) for h in gb.polys],
        'restricted_hessian_det': str(sp.simplify(hdet)),
        'status': 'PASS',
    })

assert len({z['D'] for z in results}) == 5
assert 2**3 + 27*1*2*3 == 170
certificate = {
    'date': '2026-11-17',
    'version': 'e6-nodal-v1',
    'status': 'PASS',
    'base_field': 'Q(sqrt(-3)), q=(-1+sqrt(-3))/2',
    'envelope': 'a=b=c=0',
    'cut': '[alpha:beta:gamma:delta:epsilon]=[2:1:2:3:D]',
    'boundary_Delta': 170,
    'method': 'groebner(F_D,dF_D/dX,dF_D/dY,dF_D/dZ) equals the node maximal ideal; Hessian is nonsingular',
    'nodal_fibers': results,
    'categorical_input_not_checked_by_script': 'fixed-order H3 criterion: Delta!=0 and hyperplane outside projective dual',
}
Path(__file__).with_name('nodal_cuts_certificate.json').write_text(
    json.dumps(certificate, ensure_ascii=False, indent=2) + '\n')
print('FIVE NODAL CUTS: PASS')
for entry in results:
    print(entry['label'], entry['D'], entry['restricted_hessian_det'])
