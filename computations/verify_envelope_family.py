#!/usr/bin/env python3
"""Universal PBW and full affine center checks for the seven-dimensional family.
Exact polynomial arithmetic in Q(q)[a,b,c], no finite sampling.
"""
import sympy as s,json,itertools
from functools import lru_cache
from pathlib import Path
from central_tangent import K,q as q0
A,B,C=s.symbols('a b c');P=K.poly_ring(A,B,C);a,b,c=P.gens;q=P.convert(q0,K);zero,one=P.zero,P.one
pars=(a,b,c)
def cv(v):return P.convert(v)
def add(*ps):
    out={}
    for p in ps:
        for w,v in p.items():
            out[w]=out.get(w,zero)+v
            if not out[w]:del out[w]
    return out
def sc(p,v):
    v=cv(v);return {w:c*v for w,c in p.items() if c*v}
def mon(w,v=1):return {tuple(w):cv(v)} if v else {}
rules={(1,0):{(0,1):q*q,(2,):-q*q,():-q*q*c},(2,0):{(0,2):q,(1,):one,():b},(2,1):{(1,2):q*q,(0,):-q*q,():-q*q*a}}
@lru_cache(None)
def nf(w):
    for i in range(len(w)-1):
        if w[i:i+2] in rules:return add(*(sc(nf(w[:i]+v+w[i+2:]),c) for v,c in rules[w[i:i+2]].items()))
    return mon(w)
def mul(p,r):return add(*(sc(nf(w+v),c*d) for w,c in p.items() for v,d in r.items()))
gs=[mon((i,)) for i in range(3)]
lhs=add(*(sc(nf(w+(0,)),v) for w,v in rules[(2,1)].items()));rhs=add(*(sc(nf((2,)+w),v) for w,v in rules[(1,0)].items()));assert lhs==rhs
f=(1-q)*cv(s.Rational(1,3));e=-(2*q+1)*cv(s.Rational(1,9));d=-(q+2)*cv(s.Rational(1,3))
cs=[add(mon((i,i,i)),sc(gs[i],q*q)) for i in range(3)];X,Y,Z=cs
om=add(mon((0,1,2)),mon((0,0),(q-1)*cv(s.Rational(1,3))),mon((2,2),(q-1)*cv(s.Rational(1,3))),mon((1,1),(q+2)*cv(s.Rational(1,3))),sc(gs[0],d*a),sc(gs[1],q*d*b),sc(gs[2],d*c))
for cent in [*cs,om]:
    for g in gs:assert mul(cent,g)==mul(g,cent)
ell=[((2*q+1)*pars[i]**3+2*(q-1)*pars[i]+3*q*pars[(i+1)%3]*pars[(i+2)%3])*cv(s.Rational(1,9)) for i in range(3)]
kappa=((q+1)*(a*a+b*b+c*c)+(q+2)*a*b*c)*cv(s.Rational(1,3))
nu=((1-q)*(a*a*b*b+a*a*c*c+b*b*c*c)+(q+2)*(a*a+b*b+c*c))*cv(s.Rational(1,9))
relation=add(mul(mul(om,om),om),sc(mul(om,om),f),sc(mul(mul(X,Y),Z),-1),*(sc(mul(v,v),e) for v in cs),*(sc(mul(v,om),-p) for v,p in zip(cs,pars)),*(sc(v,l) for v,l in zip(cs,ell)),sc(om,kappa),mon((),nu))
assert not relation
out={'date':'2026-11-17','version':'triangle-component-v2','status':'PASS','coefficient_ring':'Q(q)[a,b,c], q^2+q+1=0','parameter_sampling':False,'PBW_overlap':'zyx checked','central_commutators':12,'full_degree9_center_relation':True,'scope':'universal algebra identities; H3 recognition and finite-order openness are separate geometric inputs'}
Path(__file__).with_name('envelope_family_certificate.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
