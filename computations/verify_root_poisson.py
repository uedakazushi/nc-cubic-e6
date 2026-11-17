#!/usr/bin/env python3
"""Exact first-order root-of-unity Poisson bracket; no numeric samples."""
from functools import lru_cache
from pathlib import Path
import json
import sympy as s
from sympy.polys.rings import ring

Q, a0,b0,c0 = s.symbols('Q a b c')
# All PBW operations take place over Q(Q)[a,b,c].
R,a,b,c=ring('a,b,c',s.QQ.frac_field(Q))
Qv=R.from_expr(Q)
I=R.one
@lru_cache(None)
def nf(word):
    for i in range(len(word)-1):
        pair=word[i:i+2]
        if pair=='yx': ts=((1/Qv,'xy'),(-1/Qv,'z'),(-c/Qv,''))
        elif pair=='zx': ts=((Qv,'xz'),(I,'y'),(b,''))
        elif pair=='zy': ts=((1/Qv,'yz'),(-1/Qv,'x'),(-a/Qv,''))
        else:continue
        out={}
        for cf,r in ts:
            for w,k in nf(word[:i]+r+word[i+2:]).items():
                out[w]=out.get(w,R.zero)+cf*k
        return {w:cf for w,cf in out.items() if cf}
    return {word:I}
def add(*terms):
    out={}
    for p in terms:
        for w,cf in p.items():out[w]=out.get(w,R.zero)+cf
    return {w:cf for w,cf in out.items() if cf}
def scale(p,cf):return {w:v*cf for w,v in p.items() if v*cf}
def mul(p,r):
    out={}
    for w,v in p.items():
        for z,u in r.items():
            for t,cf in nf(w+z).items():out[t]=out.get(t,R.zero)+v*u*cf
    return {w:cf for w,cf in out.items() if cf}
def comm(p,r):return add(mul(p,r),scale(mul(r,p),-I))
def power(p,n):
    out={'':I}
    for _ in range(n):out=mul(out,p)
    return out
x,y,z=({'x':I},{'y':I},{'z':I})
Omega={'xyz':I,'xx':1/(Qv**2-1),'yy':Qv**2/(Qv**2-1),'zz':1/(Qv**2-1),
       'x':a/(Qv-1),'y':Qv*b/(Qv-1),'z':c/(Qv-1)}
for label,g in zip('xyz',(x,y,z)):
    rem=comm(Omega,g)
    assert not rem,(label,rem)
print('Generic Casimir: PASS',flush=True)
# q is exact algebraic: q=(-1+sqrt(-3))/2.
q=(-1+s.sqrt(-3))/2
K=s.QQ.algebraic_field(s.sqrt(-3))
S,aa,bb,cc=ring('a,b,c',K)
def at_root(cf,derivative=False):
    """Evaluate cf, or Q*d(cf)/dQ, exactly at Q=q."""
    out=S.zero
    for mon,coef in cf.items():
        expr=coef.as_expr()
        if derivative:expr=Q*s.diff(expr,Q)
        val=K.from_sympy(expr.subs(Q,q))
        if val:out+=S.from_dict({mon:val})
    return out

def specialize(p,derivative=False):
    out={w:at_root(cf,derivative) for w,cf in p.items()}
    return {w:cf for w,cf in out.items() if cf}

def special_add(*p):
    out={}
    for d in p:
        for w,cf in d.items():out[w]=out.get(w,S.zero)+cf
    return {w:cf for w,cf in out.items() if cf}

def special_scale(p,v):return {w:v*cf for w,cf in p.items() if v*cf}
O=specialize(Omega)
centers=[add(power(t,3),scale(t,Qv**2)) for t in (x,y,z)]
for i,A in enumerate(centers):
    for j,t in enumerate((x,y,z)):
        assert not specialize(comm(A,t)),(i,j,'not central')
coef_e=at_root(-(2*Qv+1)/9)
params=(aa,bb,cc)
ells=[at_root(((2*Qv+1)*u**3+2*(Qv-1)*u+3*Qv*v*w)/9)
      for u,v,w in ((a,b,c),(b,c,a),(c,a,b))]
checked=[]
for i,j,k in ((0,1,2),(1,2,0),(2,0,1)):
    C=comm(centers[i],centers[j])
    assert not specialize(C),'zeroth-order commutator nonzero'
    bracket=specialize(C,True)
    rhs=special_add(specialize(mul(centers[i],centers[j])),
          special_scale(specialize(centers[k]),-2*coef_e),
          special_scale(O,params[k]),{'':-ells[k]})
    residual=special_add(bracket,special_scale(rhs,-9))
    assert not residual,(i,j,residual)
    checked.append({'pair':['X','Y','Z'][i]+['X','Y','Z'][j],
                    'nonzero_PBW_coefficients':len(bracket),'status':'PASS'})
print('All three first-order central brackets: PASS',flush=True)
# Direct check of the sole critical overlap, not merely finite degree ranks.
left=mul({'z':I},nf('yx'))
right=mul(nf('zy'),{'x':I})
assert not add(left,scale(right,-I))
certificate={
 'date':'2026-11-17','version':'e6-connections-v15','status':'PASS',
 'coefficient_ring':'Q(Q)[a,b,c], specialized exactly in Q(sqrt(-3))[a,b,c]',
 'parameter':'Q=q exp(h); first derivative = Q d/dQ at Q=q',
 'q_relation':'q^2+q+1=0',
 'generic_Casimir':'xyz+(x^2+Q^2*y^2+z^2)/(Q^2-1)+(a*x+Q*b*y+c*z)/(Q-1)',
 'PBW_zyx_overlap':'identically zero for indeterminate Q,a,b,c',
 'generic_Casimir_commutators':'all three identically zero',
 'root_center_commutators':'all nine zero',
 'central_Poisson_brackets':'{X,Y}=9*(X*Y-2*e*Z+c*Omega-ell_c), cyclic',
 'Fricke_normalization':'{u,v}=9*(2*w+u*v+C), cyclic',
 'checks':checked,
 'not_certified':['global H3 admissibility','whole-center equality after arbitrary central quotient',
                  'skein/DAHA Morita equivalence','novelty','categorical extension of Vieta']}
Path(__file__).with_name('root_poisson_certificate.json').write_text(json.dumps(certificate,indent=2)+'\n')
print('ROOT POISSON / GOLDMAN: PASS')
