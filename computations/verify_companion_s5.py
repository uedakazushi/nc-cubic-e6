#!/usr/bin/env python3
"""Exact finite-field Frobenius certificates for the companion quintic.

Reconstruct two good-reduction characteristic polynomials directly from
the critical algebra and independently from the five scalar characters.
The geometric S5 x S5 consequence additionally uses the proof in the paper.
SymPy only: no random sampling, floating point or numpy.
"""
from pathlib import Path
import json
import sympy as s

X,Y,Z,O,D=s.symbols('X Y Z Omega D')
u,v,w=s.symbols('u v w')

def standard_monomials(g, variables, expected, bound=12):
    leading=[h.LM(order=g.order).exponents for h in g.polys]
    dim=len(variables)
    result=[]
    def rec(j,left,prefix):
        if j==dim-1:
            exps=(*prefix,left)
            if not any(all(exps[i]>=lm[i] for i in range(dim)) for lm in leading):
                result.append(exps)
        else:
            for m in range(left+1):
                rec(j+1,left-m,(*prefix,m))
    for n in range(bound):
        rec(0,n,())
    assert len(result)==expected,(len(result),expected)
    return result

def multiplication_charpoly(g,variables,monoms,multiplier,p):
    n=len(monoms)
    index={m:i for i,m in enumerate(monoms)}
    matrix=[[0]*n for _ in range(n)]
    for j,exps in enumerate(monoms):
        word=s.prod(var**power for var,power in zip(variables,exps))
        rem=g.reduce(multiplier*word)[1]
        for mon,coeff in s.Poly(rem,*variables,modulus=p).terms():
            matrix[index[mon]][j]=int(coeff)%p
    inv=lambda a:pow(int(a),-1,p)
    char=[1]
    traces=[0]
    power=[row[:] for row in matrix]
    for k in range(1,n+1):
        traces.append(sum(power[i][i] for i in range(n))%p)
        char.append(-sum(char[k-i]*traces[i] for i in range(1,k+1))*inv(k)%p)
        if k<n:
            new=[[0]*n for _ in range(n)]
            for i in range(n):
                for h in range(n):
                    if not power[i][h]:
                        continue
                    for j in range(n):
                        new[i][j]=(new[i][j]+power[i][h]*matrix[h][j])%p
            power=new
    return s.Poly(sum(char[i]*D**(n-i) for i in range(n+1)),D,modulus=p)

def finite_field_certificate(p):
    assert s.isprime(p) and (p-1)%3==0
    q=pow(s.primitive_root(p),(p-1)//3,p)
    assert (q*q+q+1)%p==0
    a,b,c=30,19,29
    inv=lambda d:pow(int(d)%p,-1,p)
    f=(1-q)*inv(3)%p
    e=-(2*q+1)*inv(9)%p
    ell=lambda a,b,c:((2*q+1)*a**3+2*(q-1)*a+3*q*b*c)*inv(9)%p
    la,lb,lc=ell(a,b,c),ell(b,c,a),ell(c,a,b)
    K=((q+1)*(a*a+b*b+c*c)+(q+2)*a*b*c)*inv(3)%p
    L=((1-q)*(a*a*b*b+a*a*c*c+b*b*c*c)+(q+2)*(a*a+b*b+c*c))*inv(9)%p
    P=(O**3+f*O**2-X*Y*Z+e*(X**2+Y**2+Z**2)
       -(a*X+b*Y+c*Z)*O+la*X+lb*Y+lc*Z+K*O+L)
    g=s.groebner([P,*[s.diff(P,z) for z in (X,Y,Z)]],
                 X,Y,Z,O,modulus=p,order='grevlex')
    basis=standard_monomials(g,(X,Y,Z,O),15)
    Delta=multiplication_charpoly(g,(X,Y,Z,O),basis,-O,p)

    A,B,C=[(1-q)*d%p for d in (a,b,c)]
    gE=s.groebner([v*w-u-A,w*u-v-B,u*v-w-C],
                  u,v,w,modulus=p,order='grevlex')
    basisE=standard_monomials(gE,(u,v,w),5)
    OmegaE=f*inv(3)*(u*v*w-u*u-v*v-w*w)
    N=multiplication_charpoly(gE,(u,v,w),basisE,-OmegaE,p)
    assert N.degree()==5 and N.is_irreducible
    M,remainder=s.div(Delta,N**2,domain=s.GF(p))
    assert remainder.is_zero and M.degree()==5
    M=M.monic()
    facs=s.factor_list(M,modulus=p)[1]
    cycle=sorted([factor.degree() for factor,multiplicity in facs
                  for _ in range(multiplicity)])
    assert all(factor.is_irreducible for factor,mult in facs)
    assert s.gcd(M,N).degree()==0
    assert s.gcd(M,M.diff()).degree()==0
    assert s.gcd(N,N.diff()).degree()==0
    assert cycle==([5] if p==1009 else [2,3])
    return {
        'p':p,'q':int(q),
        'parameters':[a,b,c],
        'critical_algebra_rank':len(basis),
        'character_algebra_rank':len(basisE),
        'N5':str(N.as_expr()),
        'M5':str(M.as_expr()),
        'N5_cycle_type':[5],
        'M5_cycle_type':cycle,
        'M5_factors':[{'degree':z.degree(),'multiplicity':m,'polynomial':str(z.as_expr())}
                      for z,m in facs],
        'N5_irreducible':True,
        'Delta15_equals_N5sq_M5':'PASS',
        'N5_M5_coprime_and_squarefree':'PASS',
    }

def main():
    records=[finite_field_certificate(p) for p in (1009,1069)]
    proof={
        'date':'2026-11-17',
        'version':'e6-relative-poisson-v18',
        'status':'PASS',
        'number_field':'Q(q), q^2+q+1=0',
        'specialized_parameters':[30,19,29],
        'finite_field_certificates':records,
        'arithmetic_Galois_M5':'S5 from Frobenius types (5) and (2,3)',
        'arithmetic_joint_Galois':'S5xS5 by Goursat and mismatched signs at p=1069',
        'geometric_joint_Galois':'S5xS5 via common rational totally split etale fiber at a=b=c=0',
        'ordinary_proof_inputs':[
            'global finite flat degree15 critical and degree5 character schemes',
            'Delta15=N5^2*M5 monic factorization',
            'residual finite etale degree5 cover near coefficient origin',
            'five distinct Q(q)-rational residual points and five character points above origin',
            'Frobenius factorization at good split primes',
            'Stacks Project Tag 0BTX and rational-point section',
            'Goursat lemma and normal subgroups of S5',
        ],
        'not_certified_by_computation':[
            'geometric etale pi1 argument',
            'newness of the arithmetic/geometric results',
            'global H3 admissibility',
            'spherical DAHA Morita comparison',
        ]
    }
    dest=Path(__file__).with_name('companion_s5_certificate.json')
    dest.write_text(json.dumps(proof,indent=2)+'\n')
    for rec in records:
        print('p=',rec['p'],'q=',rec['q'],
              'N5 degrees',rec['N5_cycle_type'],'M5 degrees',rec['M5_cycle_type'])
    print('COMPANION PAIR FROBENIUS CERTIFICATES: PASS')

if __name__=='__main__':
    main()
