#!/usr/bin/env python3
"""Exact first-order cyclic-potential/central-cubic incidence at q^3=1.
No smoothness/versality assertion is inferred from the rank alone.
"""
from __future__ import annotations
import itertools,json
from functools import lru_cache
from pathlib import Path
import sympy as sp
from sympy.polys.matrices import DomainMatrix

K=sp.QQ.alg_field_from_poly(sp.Poly(sp.Symbol('Q')**2+sp.Symbol('Q')+1))
q=K.unit
zero,one=K.zero,K.one
# K.unit is the primitive element Q.
def cv(x): return K.convert(x)
def add(*ps):
    d={}
    for p in ps:
        for w,c in p.items():
            d[w]=d.get(w,zero)+c
            if not d[w]: del d[w]
    return d
def scale(p,c):
    c=cv(c)
    return {w:a*c for w,a in p.items() if a*c}
def mon(w,c=1):
    c=cv(c)
    return {tuple(w):c} if c else {}
def words(n): return [tuple([0]*i+[1]*j+[2]*(n-i-j)) for i in range(n+1) for j in range(n-i+1)]
def necklace(w): return min(w[i:]+w[:i] for i in range(len(w)))
PHIS=sorted({necklace(w) for n in (1,2,3) for w in itertools.product(range(3),repeat=n)},key=lambda w:(len(w),w))
BASIS=sum((words(n) for n in range(4)),[])
ROWS=[(i,w) for i in range(3) for n in range(5) for w in words(n)]

def compute(a=0,b=0,c=0,cut=(2,1,2,3,5)):
    a,b,c=map(cv,(a,b,c))
    rules={(1,0):{(0,1):q*q,(2,):-q*q,():-q*q*c},
           (2,0):{(0,2):q,(1,):one,():b},
           (2,1):{(1,2):q*q,(0,):-q*q,():-q*q*a}}
    rules={w:{v:k for v,k in p.items() if k} for w,p in rules.items()}
    @lru_cache(None)
    def nf(w):
        for i in range(len(w)-1):
            if w[i:i+2] in rules:
                return add(*(scale(nf(w[:i]+v+w[i+2:]),k) for v,k in rules[w[i:i+2]].items()))
        return mon(w)
    def normalize(p): return add(*(scale(nf(w),c) for w,c in p.items()))
    def mul(p,r): return add(*(scale(nf(w+v),c*d) for w,c in p.items() for v,d in r.items()))
    def comm(p,r): return add(mul(p,r),scale(mul(r,p),-1))
    gs=[mon((i,)) for i in range(3)]
    d=-(q+cv(2))/cv(3)
    om=add(mon((0,1,2)),mon((0,0),(q-one)/cv(3)),mon((2,2),(q-one)/cv(3)),
           mon((1,1),(q+cv(2))/cv(3)),scale(gs[0],d*a),scale(gs[1],q*d*b),scale(gs[2],d*c))
    cs=[add(mon((i,i,i)),scale(gs[i],q*q)) for i in range(3)]
    G=add(scale(om,cut[0]),*(scale(p,k) for p,k in zip(cs,cut[1:4])),mon((),cut[4]))
    assert all(not comm(G,g) for g in gs)
    def column(polys): return [polys[i].get(w,zero) for i,w in ROWS]
    columns=[]
    overlap_columns=[]
    for phi in PHIS:
        dr=[]
        for i in range(3):
            dr.append(normalize(add(*(mon(phi[j+1:]+phi[:j]) for j,x in enumerate(phi) if x==i))))
        delta={(2,1):scale(dr[0],q*q),(2,0):scale(dr[1],-1),(1,0):scale(dr[2],q*q)}
        @lru_cache(None)
        def dn(w):
            for i in range(len(w)-1):
                p=w[i:i+2]
                if p in rules:
                    old=add(*(scale(dn(w[:i]+v+w[i+2:]),c) for v,c in rules[p].items()))
                    new=add(*(scale(nf(w[:i]+v+w[i+2:]),c) for v,c in delta[p].items()))
                    return add(old,new)
            return {}
        comms=[]
        for i in range(3):
            comms.append(add(*(scale(add(dn(w+(i,)),scale(dn((i,)+w),-1)),c) for w,c in G.items())))
        columns.append(column(comms))
        # First-order Diamond overlap for the perturbed quadratic presentation.
        lhs=add(*(scale(dn(w+(0,)),v) for w,v in rules[(2,1)].items()),
                *(scale(nf(w+(0,)),v) for w,v in delta[(2,1)].items()))
        rhs=add(*(scale(dn((2,)+w),v) for w,v in rules[(1,0)].items()),
                *(scale(nf((2,)+w),v) for w,v in delta[(1,0)].items()))
        overlap_columns.append(add(lhs,scale(rhs,-1)))
    for w in BASIS: columns.append(column([comm(mon(w),g) for g in gs]))
    data=[[columns[j][i] for j in range(len(columns))] for i in range(len(ROWS))]
    M=DomainMatrix(data,(len(ROWS),len(columns)),K)
    N=M.nullspace().to_Matrix()
    # leading cyclic potential restriction of kernel
    cubic_indices=[i for i,w in enumerate(PHIS) if len(w)==3]
    proj=N[:,cubic_indices]
    projection_rank=DomainMatrix.from_Matrix(proj).convert_to(K).rank()
    print('basis',PHIS,'G_basis',BASIS,flush=True)
    print('rank',M.rank(),'nullity',N.rows,'leading_projection',projection_rank,flush=True)
    # Show simple kernel vectors having diagonal cubic monomials in potential.
    extra=[]
    ids=[PHIS.index((i,i,i)) for i in range(3)]
    for row in N.tolist():
        if any(row[i]!=0 for i in ids):
            extra.append({''.join('xyz'[j] for j in PHIS[i]):str(row[i]) for i in range(len(PHIS)) if row[i]!=0})
    result={'field':'Q(q), q^2+q+1=0','base_constants':[str(K.to_sympy(v)) for v in (a,b,c)],
            'cut':list(cut),'matrix_shape':list(M.shape),'rank':M.rank(),'nullity':N.rows,
            'potential_basis':[''.join('xyz'[i] for i in w) for w in PHIS],
            'central_basis':[''.join('xyz'[i] for i in w) or '1' for w in BASIS],
            'leading_projection_rank':projection_rank,'extra_potential_directions':extra,
            'first_order_overlap_all_zero':all(not p for p in overlap_columns),
            'not_claimed':['full H3 tangent space','integration of all tangent directions','component dimension from this rank alone']}
    Path(__file__).with_name('central_tangent_certificate.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    return M,N,result

if __name__=='__main__':
    M,N,result=compute()
    print(json.dumps(result,ensure_ascii=False,indent=2))
