#!/usr/bin/env python3
"""Independently verify the specialized all-order central lift in original relations.
The normal-form substitutions are exact consequences of the defining relations;
no numerical samples or use of published centrality is needed for the checks.
"""
from integrate_via_rains import *
import time
start=time.time();n=4
for w in words(n): NF[w]={w:O}
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
cond=nx.condensation(graph);blocks=[]
for comp in reversed(list(nx.topological_sort(cond))):
    ww=sorted(cond.nodes[comp]['members']);idx={w:i for i,w in enumerate(ww)};blocks.append(len(ww))
    mat=[[O if i==j else Z for j in range(len(ww))] for i in range(len(ww))];rhs=[]
    for i,w in enumerate(ww):
        r={}
        for v,c in rew[w].items():
            if v in idx:mat[i][idx[v]]-=c
            else:r=add(r,scale(NF[v],c))
        rhs.append(r)
    ob=sorted(set().union(*(r.keys() for r in rhs)))
    if len(ww)==1:NF[ww[0]]=scale(rhs[0],1/mat[0][0]);continue
    print('degree4 exact block',len(ww),'elapsed',round(time.time()-start,2),flush=True)
    cm=DomainMatrix(mat,(len(ww),len(ww)),F)
    rm=DomainMatrix([[r.get(w,Z) for w in ob] for r in rhs],(len(ww),len(ob)),F)
    cden,cp=cm.clear_denoms(convert=True);rden,rp=rm.clear_denoms(convert=True)
    ci,di=cp.inv_den(method='rref')
    fac=F.convert(cden.element,cden.domain)/F.convert(rden.element*di,rden.domain)
    sol=ci.matmul(rp).convert_to(F).scalarmul(fac)
    for w,row in zip(ww,sol.to_list()):NF[w]={v:c for v,c in zip(ob,row) if c}
for i in range(3):
    comm=add(*(scale(add(NF[w+(i,)],scale(NF[(i,)+w],-O)),c) for w,c in normal.items()))
    assert not comm,comm
    print('central commutator',i,'PASS',round(time.time()-start,2),flush=True)
result={'date':'2026-11-17','version':'triangle-component-v2','status':'PASS',
        'field':'Q(q)(u), q^2+q+1=0','parameter_sampling':False,
        'central_commutators_in_original_relations':3,'max_exact_rewrite_block':max(blocks),
        'regular_limit':'2 Omega + X + 8Y + 27Z + 5',
        'potential':'(1+2u)xyz-qxzy+u(x^3+8y^3+27z^3)-(x^2+y^2+z^2)/2',
        'proved_algebraically':'genuine rational all-order central-cubic lift, regular at u=0',
        'not_claimed':['H3 openness when translation order varies','global component equality']}
Path(__file__).with_name('transverse_integrated_certificate.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2),flush=True)
