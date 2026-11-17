#!/usr/bin/env python3
"""Run all exact certificates; geometric and categorical arguments are separate.

validation.json is written only after all checks succeed. Merely changing
this runner is not a run, and individual certificates state their scope.
"""
from pathlib import Path
import subprocess, sys, json, platform
import sympy, networkx

root = Path(__file__).resolve().parent
checks = [
    'verify_envelope_family.py', 'verify_normal_form.py',
    'verify_smooth_witness.py', 'verify_tangent_quotient.py',
    'verify_integrated_lift.py', 'verify_cubic_obstruction.py',
    'verify_universal_cubic_syzygies.py', 'verify_second_order_incidence.py',
    'verify_rains_central_formula.py', 'verify_central_multivariate_lift.py',
    'verify_potential_recovery.py', 'verify_algebraic_boundary.py',
    'verify_boundary_graph.py', 'verify_nodal_cuts.py',
    'verify_character_node_cover.py', 'verify_daha_character.py',
    'verify_daha_braid.py', 'verify_d4_lattice.py',
    'verify_root_poisson.py', 'verify_poisson_cut_obstruction.py',
    'verify_casimir_poisson_leaves.py', 'verify_relative_poisson_cover.py',
    'verify_companion_s5.py', 'verify_cayley_lg_connections.py',
    'verify_lg_picard_g2.py', 'verify_g2_braids_periods.py',
    'verify_logarithmic_periods.py',
]
completed = []
for name in checks:
    subprocess.run([sys.executable, str(root / name)], check=True, cwd=root)
    completed.append({'script': name, 'status': 'PASS'})
result = {
    'date': '2026-11-17', 'version': 'e6-connections-v22', 'status': 'PASS',
    'python': platform.python_version(), 'sympy': sympy.__version__,
    'networkx': networkx.__version__, 'completed': completed,
    'separate_mathematical_inputs': [
        'fixed-finite-order H3 recognition/openness',
        'fixed-envelope dual criterion for nodal-center H3',
        'Terwilliger universal AW Casimir and PSL2Z action',
        'Goldman Fricke trace cubic',
        'Schock--Naruki D4 lattice of a tritangent cubic',
        'Sklyanin boundary and CY/PBW theorems',
        'Hochschild local-to-global and categorical obstruction theory',
        'De Deken--Lowen Theorem 4.5 and perfect-object lifting',
        'Brown--Gordon Poisson orders and Theorem 4.2',
        'flat-ideal intersection and pointed H3 reconstruction',
        'Cayley invariant-ring identification with torus characters',
        'D4 analytic right-equivalence and infinitesimal versality',
        'strict concavity on the real elliptope',
        'cohomology exact sequence and Poincare duality',
        'ADE Milnor lattice, unimodular gluing, outer triality',
        'Goldman--Neumann topology and boundary plumbing',
        'Deligne weight spectral sequence',
        'Boalch--Paluba component and Hurwitz formulas and Klein orbit',
        'configuration spaces and the braid fundamental group',
        'primitive boundary torus and analytic Cauchy residue integral',
        'conic matching sphere construction and analytic period continuation',
        'Friedman Proposition 3.12 and Looijenga algebraic period comparison',
        'rational mixed Hodge nonsplitting criterion using normalized periods',
    ],
    'not_certified_by_this_run': [
        'global H3 algebraic-stack construction',
        'all-boundary component classification',
        'relative quadratic-envelope AS4 recognition',
        'all-Casimir-value Azumaya or finite global dimension',
        'derived Vieta extension or heart mutation',
        'H3 status without the existing fixed-envelope criterion',
        'full branch divisor classification',
        'choice-independent global Milnor-Picard splitting',
        'mirror or Fukaya-Seidel equivalence',
        'G2 quantum algebra comparison',
        'full rank-five Gauss-Manin connection or simultaneous integral D4 period basis',
        'splitting criterion for the entire family of mixed Hodge structures',
        'non-archimedean SYZ model or good-reduction verification',
        'categorical relation to nearly Kahler geometry',
        'independent peer review', 'novelty', 'GitHub or Library saving',
    ],
}
(root / 'validation.json').write_text(json.dumps(result, indent=2) + '\n')
print('ALL CURRENT EXACT CHECKS PASS')
