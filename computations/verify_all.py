#!/usr/bin/env python3
"""Run all algebra certificates. Artin reconstruction is an ordinary proof, not a rank test."""
from pathlib import Path
import subprocess,sys,json,platform
import sympy,networkx
root=Path(__file__).resolve().parent
checks=['verify_envelope_family.py','verify_normal_form.py','verify_smooth_witness.py','verify_tangent_quotient.py','verify_integrated_lift.py','verify_cubic_obstruction.py','verify_universal_cubic_syzygies.py','verify_second_order_incidence.py','verify_rains_central_formula.py','verify_central_multivariate_lift.py','verify_potential_recovery.py','verify_algebraic_boundary.py','verify_boundary_graph.py']
completed=[]
for name in checks:
    subprocess.run([sys.executable,str(root/name)],check=True,cwd=root)
    completed.append({'script':name,'status':'PASS'})
result={'date':'2026-11-17','version':'triangle-component-v11','status':'PASS',
        'python':platform.python_version(),'sympy':sympy.__version__,'networkx':networkx.__version__,
        'completed':completed,
        'separate_mathematical_inputs':['fixed-finite-order H3 recognition/openness','Sklyanin boundary and CY/PBW theorems','Hochschild local-to-global and categorical obstruction theory','De Deken--Lowen Theorem 4.5 and perfect-object lifting for Artin injectivity'],
        'not_certified_by_this_run':['global H3 algebraic-stack construction','all-boundary component classification','relative quadratic-envelope AS4 recognition','independent peer review','novelty','GitHub or Library saving']}
(root/'validation.json').write_text(json.dumps(result,indent=2)+'\n')
print('ALL CURRENT EXACT CHECKS PASS')
