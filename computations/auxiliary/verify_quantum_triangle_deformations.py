#!/usr/bin/env python3
"""Exact checks for the three transverse q-so(3) envelope parameters.

Coefficient ring: QQ[q,a,b,c]/(q^2+q+1).  This verifies universal identities,
not sampled numerical ranks.  The geometric H3-open theorem is a separate
input, explicitly recorded in the companion manuscript and certificate.
Run from any directory with Python 3 and SymPy.
"""
from __future__ import annotations
import itertools
import json
from collections import defaultdict
from functools import lru_cache
from pathlib import Path
import sympy as s
from sympy.polys.matrices import DomainMatrix

q,a,b,c=s.symbols('q a b c')
PARAMS=(a,b,c)
MINPOLY=s.Poly(q*q+q+1,q)

def red(value):
    return s.Poly(s.expand(value),q).rem(MINPOLY).as_expr().expand()

def clean(poly):
    out={}
    for word,value in poly.items():
        value=red(value)
        if value!=0: out[word]=value
    return out

def add(*polys):
    result=defaultdict(lambda:s.Integer(0))
    for poly in polys:
        for word,value in poly.items(): result[word]+=value
    return clean(result)

def scale(poly,value):
    return clean({word:coefficient*value for word,coefficient in poly.items()})

def mono(word,value=1):
    return {tuple(word):s.sympify(value)}

# t=1; homogenization restores t^(total degree - word length).
RULES={
    (1,0):{(0,1):q*q,(2,):-q*q,():-q*q*c},
    (2,0):{(0,2):q,(1,):1,():b},
    (2,1):{(1,2):q*q,(0,):-q*q,():-q*q*a},
}

@lru_cache(None)
def normal(word):
    for i in range(len(word)-1):
        pair=word[i:i+2]
        if pair in RULES:
            return add(*(scale(normal(word[:i]+w+word[i+2:]),v)
                         for w,v in RULES[pair].items()))
    return mono(word)

def mul(left,right):
    return add(*(scale(normal(w+v),u*z)
                 for w,u in left.items() for v,z in right.items()))

def comm(left,right):
    return add(mul(left,right),scale(mul(right,left),-1))

def check_zero(poly,description):
    if poly: raise AssertionError(f'{description}: {poly}')

def transform(poly,signs,permutation):
    substitutions={PARAMS[i]:signs[i]*PARAMS[permutation[i]] for i in range(3)}
    result=[]
    for word,value in poly.items():
        sign=s.prod(signs[i] for i in word)
        transformed_word=tuple(permutation[i] for i in word)
        result.append(scale(normal(transformed_word),sign*value.xreplace(substitutions)))
    return add(*result)

def main():
    x,y,z=[mono((i,)) for i in range(3)]
    generators=(x,y,z)
    left=add(*(scale(normal(w+(0,)),v) for w,v in RULES[(2,1)].items()))
    right=add(*(scale(normal((2,)+w),v) for w,v in RULES[(1,0)].items()))
    check_zero(add(left,scale(right,-1)),'zyx overlap')

    f=(1-q)/3
    d=-(q+2)/3
    e=-(2*q+1)/9
    X,Y,Z=[add(mono((i,i,i)),scale(generators[i],q*q)) for i in range(3)]
    omega=add(mono((0,1,2)),scale(mono((0,0)),(q-1)/3),
              scale(mono((1,1)),(q+2)/3),scale(mono((2,2)),(q-1)/3),
              scale(x,d*a),scale(y,q*d*b),scale(z,d*c))
    centers=(X,Y,Z,omega)
    for i,central in enumerate(centers):
        for j,generator in enumerate(generators):
            check_zero(comm(central,generator),f'central commutator {i},{j}')

    # Full affine central hypersurface, with the original a=b=c=0 relation.
    ell=[((2*q+1)*PARAMS[i]**3+2*(q-1)*PARAMS[i]
          +3*q*PARAMS[(i+1)%3]*PARAMS[(i+2)%3])/9 for i in range(3)]
    squares=a*a+b*b+c*c
    pairs=a*a*b*b+a*a*c*c+b*b*c*c
    kappa=((q+1)*squares+(q+2)*a*b*c)/3
    nu=((1-q)*pairs+(q+2)*squares)/9
    relation=add(
        mul(mul(omega,omega),omega),scale(mul(omega,omega),f),
        scale(mul(mul(X,Y),Z),-1),
        *(scale(mul(C,C),e) for C in (X,Y,Z)),
        *(scale(mul(C,omega),-parameter) for C,parameter in zip((X,Y,Z),PARAMS)),
        *(scale(C,value) for C,value in zip((X,Y,Z),ell)),
        scale(omega,kappa),mono((),nu))
    check_zero(relation,'universal degree-nine central identity')

    # All twelve signed cyclic transformations preserve omega and transport X,Y,Z.
    action_checks=0
    for signs in itertools.product((-1,1),repeat=3):
        if s.prod(signs)!=1: continue
        for shift in range(3):
            permutation=tuple((i+shift)%3 for i in range(3))
            check_zero(add(transform(omega,signs,permutation),scale(omega,-1)),
                       'A4 Casimir covariance')
            for i,C in enumerate((X,Y,Z)):
                check_zero(add(transform(C,signs,permutation),
                               scale((X,Y,Z)[permutation[i]],-signs[i])),
                           'A4 Chebyshev covariance')
            action_checks+=1

    # Full infinitesimal affine-linear coordinate change after the intrinsic
    # unique central line kt has been preserved.  Relation-basis changes are
    # already factored out by reduction in the quadratic PBW quotient.
    M=s.symbols('m0:9'); v=s.symbols('v0:3'); r=s.symbols('r')
    da,db,dc=s.symbols('da db dc')
    changes=[add(*(scale(generators[j],M[3*i+j]) for j in range(3)),mono((),v[i]))
             for i in range(3)]
    equations=[]
    for i,ds in enumerate((da,db,dc)):
        j,k=(i+1)%3,(i+2)%3
        variation=add(mul(changes[j],generators[k]),mul(generators[j],changes[k]),
                      scale(mul(changes[k],generators[j]),-q),
                      scale(mul(generators[k],changes[j]),-q),
                      scale(changes[i],-1),scale(generators[i],-r),mono((),-ds))
        equations.extend(s.expand(u.subs({a:0,b:0,c:0})) for u in variation.values())
    unknowns=(*M,*v,r,da,db,dc)
    matrix,_=s.linear_eq_to_matrix(equations,unknowns)
    root=(-1+s.sqrt(-3))/2
    field=s.QQ.algebraic_field(s.sqrt(-3))
    exact=DomainMatrix.from_Matrix(matrix.subs(q,root)).convert_to(field)
    rank=exact.rank()
    assert rank==15,(matrix.shape,rank)
    scalar=s.Matrix([1 if i in (0,4,8) else 0 for i in range(9)]+[0,0,0,1,0,0,0])
    assert all(red(u)==0 for u in matrix*scalar)

    certificate={
        'date':'2026-11-17','version':'triangle-component-v1','status':'PASS',
        'coefficient_ring':'QQ[q,a,b,c]/(q^2+q+1)',
        'sampling':'none; identities hold polynomially in all a,b,c',
        'PBW_critical_overlap':'zyx: both reductions agree',
        'central_commutators_checked':12,
        'central_hypersurface_identity':'verified in original relations, total filtered degree 9',
        'finite_group_elements_checked':action_checks,
        'infinitesimal_coordinate_matrix_shape':list(matrix.shape),
        'infinitesimal_coordinate_matrix_rank':rank,
        'kernel':'one-dimensional: common degree scalar only; da=db=dc=0',
        'conclusion_of_algebra_checks':'three genuine integrable envelope directions, with five central cubics',
        'geometric_inputs_not_computer_proofs':[
            'PBW/CY and central-extension homological theorems',
            'fixed finite-order elliptic-boundary H3 openness, existing manuscript theorem',
            'intrinsic anticanonical reconstruction on H3 geometric objects'],
        'not_claimed':[
            'algebraicity of the entire intrinsic H3 stack',
            'the seven-dimensional chart is an irreducible component',
            'full versality or exact full tangent dimension',
            'independent re-audit of all earlier H3 proofs or literature novelty']
    }
    out=Path(__file__).with_name('quantum_triangle_deformations_certificate.json')
    out.write_text(json.dumps(certificate,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(certificate,ensure_ascii=False,indent=2))

if __name__=='__main__': main()
