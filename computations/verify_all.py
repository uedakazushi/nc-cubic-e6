#!/usr/bin/env python3
"""Run exact arithmetic validators and record the actual execution and sources.

The current manifest is replaced, not appended. A failed execution overwrites
a previous PASS. Geometric and categorical arguments are separate inputs.
"""
from pathlib import Path
from datetime import datetime, timezone
from zoneinfo import ZoneInfo
import subprocess, sys, json, platform, hashlib
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
    'verify_logarithmic_periods.py', 'verify_conic_period_coordinates.py',
    'verify_triality_period_isogeny.py', 'verify_boundary_pell_dynamics.py',
    'verify_localization_entropy.py', 'verify_boundary_torus_links.py',
    'verify_boundary_thresholds.py', 'verify_boundary_analytic_moduli.py',
    'verify_boundary_prym.py',
    'verify_prym_integral_belyi.py',
]
SEPARATE_MATHEMATICAL_INPUTS = [
        'fixed-finite-order H3 recognition/openness',
        'fixed-envelope dual criterion for nodal-center H3',
        'Terwilliger universal AW Casimir and PSL2Z action',
        'Goldman Fricke trace cubic',
        'Schock--Naruki D4 lattice and period torus of a tritangent cubic',
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
        'Goldman--Neumann topology, homology action and boundary plumbing',
        'Deligne weight spectral sequence',
        'Boalch--Paluba component, triality and Hurwitz formulas and Klein orbit',
        'configuration spaces and the braid fundamental group',
        'primitive boundary torus and analytic Cauchy residue integral',
        'conic matching sphere construction and analytic period continuation',
        'Friedman Proposition 3.12 and Looijenga algebraic period comparison',
        'compatible conic component contraction to F1',
        'boundary line-bundle gluing and rational MHS splitting criterion',
        'integer Hodge extension classification and rational companion comparison',
        'Weyl invariant ring of the triality fixed period torus',
        'Cantat--Loray entropy and dynamical-degree theorem',
        'Jang general tropical Markov linearization',
        'boundary monomial valuations and Vieta invariance',
        'all-n leading-term proof and associated graded minimal degree',
        'pole-divisor comparison with projective pullback',
        'irrational eigenrays and finite-boundary-blowup nonregularization',
        'minimal corner extraction by the Euclidean algorithm',
        'DHKK fixed-generator proof and saturated complexity comparison',
        'pole filtration from categorical localization',
        'normalization genus, adjunction and proper cohomology estimates',
        'mixed-complex HKR and periodic cyclic/de Rham comparison',
        'all-n inverse branch parametrization and plane-curve Puiseux topology',
        'conductor formula and Milnor--Orlik monodromy formula',
        'normalization defect and vector-bundle estimates on P1',
        'Casals real-morsification Weinstein construction',
        'Newton toric log resolution and multiplier ideals',
        'analytic coordinate comparison of two weighted branches',
        'Dyckerhoff Hochschild algebra and minimal A-infinity models',
        'Mather--Yau contact reconstruction for isolated hypersurfaces',
        'strict filtered Koszul lemma for weighted regular initial sequences',
        'elliptic curves with a marked nonzero two-torsion point',
        'connected Kummer covers and Riemann-Hurwitz',
        'Prym norm and pullback, Ciani Jacobian isogeny decomposition',
        'cyclic Milnor cover with total ramification and theta polarization',
        'Miranda--Persson X411 classification, Kodaira and Shioda--Tate',
        'Gauss-Manin compatibility of finite curve maps',
        'Hua--Keller Theorem 5.9 for ordinary Z-graded dg singularity categories',
    ]
NOT_CERTIFIED = [
        'global H3 algebraic-stack construction',
        'all-boundary component classification',
        'relative quadratic-envelope AS4 recognition',
        'all-Casimir-value Azumaya or finite global dimension',
        'derived Vieta extension or heart mutation',
        'H3 status without the existing fixed-envelope criterion',
        'full branch divisor classification',
        'choice-independent global Milnor-Picard splitting',
        'mirror or Fukaya-Seidel equivalence',
        'equivariant uniform filtration comparison for the specific automorphism',
        'G2 quantum algebra or group-level isogeny comparison',
        'full rank-five algebraic Gauss-Manin connection matrices',
        'unmarked global companion variation of Hodge structures',
        'algebraic or categorical equivalence of companion surfaces',
        'non-archimedean SYZ model or good-reduction verification',
        'nonregularization on all unrelated compactifications',
        'categorical relation to nearly Kahler geometry',
        'noncommutative H3 functor realizing the affine automorphism',
        'a proper exact functor realizing the sequence of curve closures',
        'general strictly two-periodic MF reconstruction for higher-weight germs',
        'elliptic isogeny inducing an MF equivalence or categorical summand',
        'the Kummer-Prym construction for the actual non-quasihomogeneous germ',
        'integral direct-product splitting of the full Prym polarization',
        'complete comparison between relative periodic and absolute dg Hochschild theory',
        'functors or exact cobordisms between different local Weinstein models',
        'independent peer review', 'novelty', 'GitHub or Library saving',
    ]

def utc_now():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_snapshot():
    names = checks + ["central_tangent.py", "integrate_via_rains.py",
                      "verify_all.py", "requirements.txt"]
    return {name: sha256(root / name) for name in sorted(set(names))}


def write_manifest(completed, before, *, started_at=None, failed=None,
                   record_origin="direct execution", executed_runner_sha256=None):
    """Record only a completed execution; source hashes bind the stated scope."""
    now = datetime.now(timezone.utc)
    changed = [name for name, digest in before.items()
               if sha256(root / name) != digest]
    if changed:
        failed = {"source_changed_during_run": changed}
    status = "PASS" if failed is None and completed == checks else "FAIL"
    result = {
        "schema_version": 2,
        "date": now.astimezone(ZoneInfo("Asia/Tokyo")).date().isoformat(),
        "completed_at_utc": now.isoformat(timespec="seconds"),
        "status": status,
        "scope": "Execution of the 36 exact arithmetic validators listed below; not an independent audit of mathematical proofs.",
        "record_origin": record_origin,
        "python": platform.python_version(), "sympy": sympy.__version__,
        "networkx": networkx.__version__,
        "runner_sha256": executed_runner_sha256 or before["verify_all.py"],
        "support_source_sha256": {name: before[name] for name in
            ("central_tangent.py", "integrate_via_rains.py", "requirements.txt")},
        "completed": [{"script": name, "status": "PASS",
                       "source_sha256": before[name]} for name in completed],
        "source_integrity": "unchanged" if not changed else "changed",
        "separate_mathematical_inputs": SEPARATE_MATHEMATICAL_INPUTS,
        "not_certified_by_this_run": NOT_CERTIFIED,
    }
    if started_at is not None:
        result["started_at_utc"] = started_at
    if failed is not None:
        result["failure"] = failed
    (root / "validation.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    return status


def main():
    before = source_snapshot()
    started = utc_now()
    completed = []
    for i, name in enumerate(checks, 1):
        print(f"[{i}/{len(checks)}] {name}", flush=True)
        try:
            subprocess.run([sys.executable, str(root / name)], check=True, cwd=root)
        except subprocess.CalledProcessError as exc:
            write_manifest(completed, before, started_at=started,
                           failed={"script": name, "returncode": exc.returncode})
            return exc.returncode or 1
        completed.append(name)
    status = write_manifest(completed, before, started_at=started)
    if status != "PASS":
        print("SOURCE INTEGRITY FAILED", file=sys.stderr)
        return 1
    print("ALL CURRENT EXACT CHECKS PASS (arithmetic scope only)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
