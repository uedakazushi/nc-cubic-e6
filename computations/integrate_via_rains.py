#!/usr/bin/env python3
"""Specialize Etingof--Ginzburg Appendix 9.1 and take the 3-torsion limit.
The all-order centrality input is the cited published formula.  This script
checks its rational PBW specialization and limit, not the full H3 condition.
"""
from central_tangent import K,q,words
import sympy as s,itertools,json,networkx as nx
from pathlib import Path
from sympy.polys.matrices import DomainMatrix
u=s.Symbol('u'); F=K.frac_field(u); U=F.gens[0]; Q0=F.convert(q,K); O,Z=F.one,F.zero
p=1+2*U; Q=Q0/p; T=-18*U/p
A=-6/p; B=-s.Rational(3,2)/p; C=-s.Rational(2,3)/p
# Original x,y,z variables, with X=x,Y=2y,Z=3z in the formula.
scales=[1,2,3]
def add(*ps):
    out={}
    for po in ps:
        for w,c in po.items():
            out[w]=out.get(w,Z)+c
            if not out[w]:del out[w]
    return out
def scale(po,c):return {w:v*c for w,v in po.items() if v*c}
def term(w,c):return {w:F.convert(c)*s.prod(scales[i] for i in w)}
raw=add(
    term((1,1,1),T*T*(Q+1)*(T**3+1)),
    term((1,2,0),T*(Q+1)*(Q**3-T**3)),
    term((2,1,0),-T*(Q+1)*Q*(T**3+1)),
    term((2,2,2),T*T*(Q+1)*(Q**3-T**3)),
    term((1,1),-T*(Q**2+Q*T**3+Q+2*T**3+1)*B),
    term((1,2),(Q*T**3-Q**2)*A),
    term((2,0),T**3*(Q+1)*B),
    term((2,1),(Q**3+Q*T**3)*A),
    term((1,0),Q*(Q+1)*T**3*C),
    term((2,2),T*(2*Q*T**3+T**3-Q**4-Q**3-Q**2)*C),
    term((0,),-(Q**2*A*A+Q*T*T*B*C)),
    term((1,),-T*(Q*T*A*C-T*T*B*B)),
    term((2,),-T*(Q*T*T*C*C+Q*T*A*B)))
rules={(2,1):{(1,2):p/Q0,(0,0):3*U/Q0,(0,):-1/Q0},
       (2,0):{(0,2):Q0/p,(1,1):-24*U/p,(1,):1/p},
       (1,0):{(0,1):p/Q0,(2,2):81*U/Q0,(2,):-1/Q0}}
NF={}
for n in range(4):
    for w in words(n):NF[w]={w:O}
    rew={};graph=nx.DiGraph()
    for w in itertools.product(range(3),repeat=n):
        if w in NF:continue
        graph.add_node(w)
        for i in range(n-1):
            if w[i:i+2] in rules:
                rew[w]=add(*({w[:i]+v+w[i+2:]:c} for v,c in rules[w[i:i+2]].items()))
                for v in rew[w]:
                    if v not in NF:graph.add_edge(w,v)
                break
    cond=nx.condensation(graph)
    for comp in reversed(list(nx.topological_sort(cond))):
        ww=sorted(cond.nodes[comp]['members']);idx={w:i for i,w in enumerate(ww)}
        mat=[[O if i==j else Z for j in range(len(ww))] for i in range(len(ww))];rhs=[]
        for i,w in enumerate(ww):
            r={}
            for v,c in rew[w].items():
                if v in idx:mat[i][idx[v]]-=c
                else:r=add(r,scale(NF[v],c))
            rhs.append(r)
        ob=sorted(set().union(*(r.keys() for r in rhs)))
        if len(ww)==1:NF[ww[0]]=scale(rhs[0],1/mat[0][0]);continue
        cm=DomainMatrix(mat,(len(ww),len(ww)),F)
        rm=DomainMatrix([[r.get(w,Z) for w in ob] for r in rhs],(len(ww),len(ob)),F)
        sol=cm.inv()*rm
        for w,row in zip(ww,sol.to_list()):NF[w]={v:c for v,c in zip(ob,row) if c}
normal=add(*(scale(NF[w],c) for w,c in raw.items()))
# normalize x^3 coefficient to 1; free scalar central constant = 5
normal=scale(normal,1/normal[(0,0,0)]);normal[()]=F.convert(5)
Qs=s.Symbol('q')
def show(v):return str(F.to_sympy(v).subs(K.ext.as_expr(),Qs))
def at0(v):
    num=v.numer.get((0,),K.zero);den=v.denom.get((0,),K.zero)
    assert den
    return num/den
lim={w:at0(v) for w,v in normal.items() if at0(v)}
print('limit', {''.join('xyz'[i] for i in w) or '1':str(K.to_sympy(v).subs(K.ext.as_expr(),Qs)) for w,v in lim.items()})
out={'date':'2026-11-17','version':'triangle-component-v2','status':'PASS',
     'potential':'(1+2u)xyz-qxzy+u(x^3+8y^3+27z^3)-(x^2+y^2+z^2)/2',
     'published_central_formula':'Etingof--Ginzburg arXiv:0709.3593v4 Appendix 9.1',
     'scaling':'X=x,Y=2y,Z=3z; q_R=q/(1+2u), t_R=-18u/(1+2u)',
     'coefficients':{''.join('xyz'[i] for i in w) or '1':show(v) for w,v in normal.items()},
     'limit':{''.join('xyz'[i] for i in w) or '1':str(K.to_sympy(v).subs(K.ext.as_expr(),Qs)) for w,v in lim.items()},
     'not_claimed':['full independent re-verification of the published universal central formula','H3 preservation across varying translation order']}
Path(__file__).with_name('transverse_rains_lift_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS rational central formula specialization and regular limit')
