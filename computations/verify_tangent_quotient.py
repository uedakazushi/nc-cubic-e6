#!/usr/bin/env python3
"""Exact gauge quotient and the seven known plus one transverse directions.
This is the cyclic-potential/central-cubic incidence, not a proof of full
intrinsic H3 versality. Every rank is over Q(q), q^2+q+1=0.
"""
from central_tangent import *
M,N,result=compute()
rules={(1,0):{(0,1):q*q,(2,):-q*q},(2,0):{(0,2):q,(1,):one},(2,1):{(1,2):q*q,(0,):-q*q}}
@lru_cache(None)
def nf(w):
    for i in range(len(w)-1):
        if w[i:i+2] in rules:
            return add(*(scale(nf(w[:i]+v+w[i+2:]),c) for v,c in rules[w[i:i+2]].items()))
    return mon(w)
def norm(poly): return add(*(scale(nf(w),c) for w,c in poly.items()))
def cyclic(poly):
    out={}
    for w,c in poly.items():
        if not w: continue
        v=necklace(w); out[v]=out.get(v,zero)+c
        if not out[v]: del out[v]
    return out
phi=add(mon((0,1,2)),mon((0,2,1),-q),*(mon((i,i),-cv(1)/cv(2)) for i in range(3)))
om=add(mon((0,1,2)),mon((0,0),(q-one)/cv(3)),mon((2,2),(q-one)/cv(3)),mon((1,1),(q+cv(2))/cv(3)))
cs=[add(mon((i,i,i)),mon((i,),q*q)) for i in range(3)]
G=add(scale(om,2),scale(cs[0],1),scale(cs[1],2),scale(cs[2],3),mon((),5))
def vector(dp,dg):
    dp=cyclic(dp); dg=norm(dg)
    return [dp.get(w,zero) for w in PHIS]+[dg.get(w,zero) for w in BASIS]
def derivative(poly,i,replacement):
    return add(*(scale(mon(w[:j]+replacement+w[j+1:]),c) for w,c in poly.items() for j,l in enumerate(w) if l==i))
gauge=[]
for i in range(3):
    for replacement in [(),(0,),(1,),(2,)]:
        gauge.append(vector(derivative(phi,i,replacement),derivative(G,i,replacement)))
gauge.append(vector(phi,{}))
gauge.append(vector({},G))
def dm(cols):
    return DomainMatrix([[col[i] for col in cols] for i in range(40)],(40,len(cols)),K)
A=dm(gauge)
assert (M*A).is_zero_matrix
assert A.rank()==14
# three envelope constants and all five central cut directions (one projective redundancy).
d=-(q+cv(2))/cv(3)
family=[vector(mon((i,),-1),mon((i,),2*d*(q if i==1 else one))) for i in range(3)]
family += [vector({},C) for C in [om,*cs,mon(())]]
F=dm(gauge+family)
assert (M*F).is_zero_matrix
assert F.rank()==21
# Construct the central correction to the explicit leading deformation by an exact linear solve.
pvec=[zero]*20
for w,v in [((0,0,0),1),((1,1,1),2),((2,2,2),3),((0,1,2),2)]: pvec[PHIS.index(w)]=cv(v)
D=M.extract(range(105),range(20,40)); P=M.extract(range(105),range(20))
rhs=-(P*DomainMatrix([[v] for v in pvec],(20,1),K))
rr,pivots=D.hstack(rhs).rref(); assert 20 not in pivots
vals=[zero]*20
for row,pivot in zip(rr.to_list(),pivots): vals[pivot]=row[20]
extra=pvec+vals
Full=dm(gauge+family+[extra])
assert (M*Full).is_zero_matrix
assert Full.rank()==22==N.rows
out={'date':'2026-11-17','version':'triangle-component-v2','status':'PASS',
     'field':'Q(q), q^2+q+1=0','base_constants':[0,0,0],'cut':[2,1,2,3,5],
     'incidence_matrix_shape':list(M.shape),'incidence_rank':M.rank(),'incidence_kernel_dimension':N.rows,
     'gauge_columns':14,'gauge_rank':A.rank(),'kernel_contains_gauge':True,
     'known_family_plus_gauge_rank':F.rank(),'known_family_mod_gauge_dimension':7,
     'with_transverse_rank':Full.rank(),'incidence_mod_gauge_dimension':8,
     'span_is_entire_kernel':True,
     'explicit_delta_Phi':'x^3+2y^3+3z^3+2xyz',
     'explicit_delta_G':{''.join('xyz'[i] for i in w) or '1':str(K.to_sympy(v).subs(K.ext.as_expr(),sp.Symbol('q'))) for w,v in zip(BASIS,vals) if v},
     'not_claimed':['global irreducible-component classification','all intrinsic H3 deformation functors identified with this incidence']}
Path(__file__).with_name('tangent_quotient_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
