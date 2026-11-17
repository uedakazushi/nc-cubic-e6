#!/usr/bin/env python3
"""Exact identities for the E6/R(1,3) presentation comparison.

This checks cyclic-word linear algebra, derivatives and coefficient changes.
It does not establish AS regularity, H3 admissibility, global stack descent,
or the geometric component theorem without the manuscript's hypotheses.
"""
from collections import defaultdict
from itertools import permutations, product
from pathlib import Path
import hashlib
import json
import sympy as s

HERE = Path(__file__).resolve()
X = s.symbols('x y z')


def cyclic(word):
    return min(word[i:] + word[:i] for i in range(len(word))) if word else ()


def clean(poly):
    return {w: s.factor(c) for w, c in poly.items() if s.factor(c) != 0}


def add(*polys):
    result = defaultdict(lambda: s.S.Zero)
    for poly in polys:
        for word, coefficient in poly.items():
            result[word] += coefficient
    return clean(result)


def scale(poly, coefficient):
    return clean({word: coefficient * c for word, c in poly.items()})


def symmetrize(poly, quotient=False):
    result = defaultdict(lambda: s.S.Zero)
    for exponents, coefficient in s.Poly(poly, *X).terms():
        words = set(permutations(tuple(i for i, n in enumerate(exponents) for _ in range(n))))
        for word in words:
            result[cyclic(word) if quotient else word] += coefficient / len(words)
    return clean(result)


def derivative(poly, index):
    result = defaultdict(lambda: s.S.Zero)
    for word, coefficient in poly.items():
        for j, letter in enumerate(word):
            if letter == index:
                result[word[j + 1:] + word[:j]] += coefficient
    return clean(result)


def exponents_of_degree(n):
    return [(a, b, n-a-b) for a in range(n+1) for b in range(n-a+1)]


def monomial(exponents):
    return s.prod(x**e for x, e in zip(X, exponents))


def main():
    cubic_words = sorted({cyclic(word) for word in product(range(3), repeat=3)})
    assert len(cubic_words) == 11
    alt = {(0, 1, 2): s.S.One, (0, 2, 1): -s.S.One}
    symmetric = [symmetrize(monomial(e), True) for e in exponents_of_degree(3)]
    matrix = s.Matrix([[p.get(w, 0) for p in symmetric + [alt]] for w in cubic_words])
    assert matrix.rank() == 11
    assert len(symmetric) == 10
    derivative_checks = 0
    for n in (1, 2, 3):
        for exponents in exponents_of_degree(n):
            m = monomial(exponents)
            for i in range(3):
                assert derivative(symmetrize(m, True), i) == symmetrize(s.diff(m, X[i]))
                derivative_checks += 1
    assert derivative_checks == 57
    for i in range(3):
        j, k = (i+1) % 3, (i+2) % 3
        assert derivative(alt, i) == {(j, k): 1, (k, j): -1}

    lam, kap, eta, zet, a, b, c, q = s.symbols('lambda kappa eta zeta a b c q')
    x, y, z = X
    p = 1 + kap * lam
    alpha = (p + q) / 2
    symmetric_part = ((p-q)*x*y*z + lam*(x**3 + eta**3*y**3 + zet**3*z**3)
                      - (x**2+y**2+z**2)/2 - a*x-b*y-c*z)
    f = -symmetric_part / alpha
    original = add({(0,1,2): p, (0,2,1): -q},
                   symmetrize(symmetric_part - (p-q)*x*y*z, True))
    normalized = add(alt, scale(symmetrize(f, True), -1))
    assert add(scale(original, 1/alpha), scale(normalized, -1)) == {}
    for i in range(3):
        assert add(derivative(normalized, i), scale(derivative(alt, i), -1),
                   symmetrize(s.diff(f, X[i]))) == {}

    A, B, C, L = s.symbols('A B C L')
    hesse = A*x**3+B*y**3+C*z**3+L*x*y*z
    gradient = [s.diff(hesse, u) for u in X]
    # Whole-coefficient consequence of the gradient equations (not sampling).
    obstruction = (L**3+27*A*B*C)*x**2*y**2*z**2
    combination = (gradient[0]*(3*B*y**2)*(3*C*z**2)
                   - L*y*z*gradient[1]*(3*C*z**2)
                   + L**2*y*z*x*z*gradient[2])
    assert s.expand(combination - obstruction) == 0
    delta = (p-q)**3 + 27*lam**3*eta**3*zet**3
    assert s.expand((L**3+27*A*B*C).subs({A:lam,B:lam*eta**3,C:lam*zet**3,L:p-q})) == s.expand(delta)
    phi3 = s.Poly(q*q+q+1, q)
    units = [s.Poly((p+q).subs(lam, 0), q), s.Poly(delta.subs(lam, 0), q)]
    assert all(s.gcd(v, phi3).degree() == 0 for v in units)
    boundary_f = s.cancel(f.subs(lam, 0))
    homogeneous_three = sum(coef*monomial(e) for e,coef in s.Poly(boundary_f,*X).terms() if sum(e)==3)
    assert s.cancel(homogeneous_three + 2*(1-q)/(1+q)*x*y*z) == 0

    result = {
        'status': 'PASS',
        'source_sha256': hashlib.sha256(HERE.read_bytes()).hexdigest(),
        'field': 'exact rational functions; q^2+q+1 for special-point units',
        'cyclic_degree3_dimension': 11,
        'symmetric_degree3_dimension': 10,
        'symmetrization_derivative_checks': derivative_checks,
        'coefficient_change': 'alpha=(1+kappa*lambda+q)/2; f=-symmetric_part/alpha',
        'hesse_discriminant': str(delta),
        'special_f3': '-2*(1-q)/(1+q)*x*y*z',
        'checked': ['cyclic basis and commutator derivatives', 'all 57 monomial derivative identities',
                    'eight-parameter potential and all three relations',
                    'Hesse gradient consequence and discriminant substitution',
                    'nonvanishing special-point denominators'],
        'not_claimed': ['AS4 or H3 from finite identities alone', 'global intrinsic component identification',
                        'AOU/AS recognition', 'independent audit of prior 36 validators']
    }
    target = HERE.with_name('r13_comparison_certificate.json')
    target.write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
