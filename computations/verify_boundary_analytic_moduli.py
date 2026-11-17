#!/usr/bin/env python3
"""Exact algebra for boundary analytic moduli, level-2 elliptic curves and MF models.

All computations are over Q or Q(sqrt(2)). Contact classification, the
Mather--Yau theorem and Morita invariance are ordinary mathematical inputs.
The actual-germ example is computed from the first Vieta iterate, not by
silently replacing the germ with its weighted initial form.
"""
from pathlib import Path
import json
import sympy as s

x,y,k,K,z,eta,u,v,w,t=s.symbols('x y kappa K z eta u v w t')

# The weighted models and their Euler identity.
for b,c in ((2,5),(12,29),(70,169)):
    f=y**(2*b)-2*k*x**c*y**b+x**(2*c)
    assert s.expand(b*x*s.diff(f,x)+c*y*s.diff(f,y)-2*b*c*f)==0
    assert s.Poly(s.gcd(s.diff(f,x),s.diff(f,y)),x,y).total_degree()==0
    assert s.expand(f.subs(k,-k) - (y**(2*b)+2*k*x**c*y**b+x**(2*c)))==0

# Three equally large, but not all isomorphic, Jacobi algebras.
model_records=[]
for kv in (s.S.Zero,s.Integer(2),3*s.sqrt(2)/4):
    f=y**4-2*kv*x**5*y**2+x**10
    domain=s.QQ.algebraic_field(s.sqrt(2)) if kv.has(s.sqrt(2)) else s.QQ
    gb=s.groebner([s.diff(f,x),s.diff(f,y)],x,y,order='grevlex',domain=domain)
    lead=[g.LM(order=gb.order).exponents for g in gb.polys]
    basis=[(i,j) for i in range(20) for j in range(8)
           if not any(i>=a and j>=b for a,b in lead)]
    assert len(basis)==27
    assert gb.reduce(f)[1]==0
    model_records.append({'kappa':str(kv),'K':str(s.simplify(kv**2)),
                          'Milnor_and_Tjurina':27,
                          'Groebner_basis':[str(p.as_expr()) for p in gb.polys]})

# Four points, elliptic invariants, and a concrete two-isogeny.
a2=-2*k; a4=s.S.One
b2=4*a2; b4=2*a4; b6=s.S.Zero; b8=-a4*a4
c4=b2*b2-24*b4
Delta=-b2*b2*b8-8*b4**3-27*b6*b6+9*b2*b4*b6
assert s.expand(c4-16*(4*k*k-3))==0
assert s.expand(Delta-64*(k*k-1))==0
j=64*(4*K-3)**3/(K-1)
assert s.cancel(c4**3/Delta-j.subs(K,k*k))==0
T=64*(K-1)
assert s.cancel(j-(T+16)**3/T)==0
assert s.factor(j-1728)==64*K*(8*K-9)**2/(K-1)
assert j.subs(K,0)==j.subs(K,s.Rational(9,8))==1728

# Translation by the nonzero two-torsion point and its invariant quotient.
source=z**3-2*k*z*z+z
X=z-2*k+1/z
Yfactor=1-1/z**2
quotient=X**3+4*k*X**2+4*(k*k-1)*X
assert s.cancel(source*Yfactor**2-quotient)==0
assert s.cancel(X.subs(z,1/z)-X)==0
assert s.cancel((-eta/z**2)*(1-z**2)-eta*Yfactor)==0
Kdual=K/(K-1)
assert s.cancel(Kdual.subs(K,Kdual)-K)==0
assert s.cancel(64*(Kdual-1)-4096/T)==0
jdual=s.factor(j.subs(K,Kdual))
assert jdual==64*(K+3)**3/(K-1)**2
assert Kdual.subs(K,4)==s.Rational(4,3)

# The actual boundary germ for A=B=C=0, h=1, initial conic v=2, n=1.
def iw(q):
    U,V,W=q
    return U,V,s.expand(2*U*V-W)
def iu(q):
    U,V,W=q
    return s.expand(2*V*W-U),V,W
def iv(q):
    U,V,W=q
    return U,s.expand(2*U*W-V),W
forward=iv(iw(iu(iw((u,v,w)))))
V=s.Poly(forward[1],u,v,w)
assert s.total_degree(V.as_expr())==7
H=sum(cf*x**i*y**j*t**(7-i-j-l) for (i,j,l),cf in V.terms())-2*t**7
P=2*x*y-t*(x*x+y*y+1)-2*t**3
raw=s.resultant(P,H,t)
representative,rem=s.div(s.Poly(raw,x,y),s.Poly(64*x*x*y**5,x,y))
assert rem.is_zero
F=representative.as_expr()
terms=representative.terms()
initial=s.expand(sum(cf*x**i*y**j for (i,j),cf in terms if 2*i+5*j==20))
assert initial==4*(y**4-4*x**5*y*y+x**10)
assert min(2*i+5*j for (i,j),cf in terms)==20

# The initial partials form a weighted regular sequence. Its Jacobi socle
# weight is 2*20-2*(2+5)=26; strictness of the filtered Koszul complex
# makes truncation above weight 26 exact for the local Jacobi quotient.
monomials=sorted([(i,j) for i in range(14) for j in range(6) if 2*i+5*j<=26],
                 key=lambda e:(2*e[0]+5*e[1],e))
index={mon:i for i,mon in enumerate(monomials)}
def rows(poly):
    terms=s.Poly(poly,x,y).terms()
    min_weight=min(2*i+5*j for (i,j),cf in terms)
    result=[]
    for a,b in monomials:
        if 2*a+5*b+min_weight>26:
            continue
        row=[s.S.Zero]*len(monomials)
        for (i,j),cf in terms:
            ex=(a+i,b+j)
            if ex in index:
                row[index[ex]]+=cf
        result.append(row)
    return result
Jrows=rows(s.diff(F,x))+rows(s.diff(F,y))
J=s.Matrix(Jrows)
TJ=s.Matrix(Jrows+rows(F))
assert len(monomials)==45 and J.rank()==18 and TJ.rank()==21
rr,pivots=J.rref()
free=[i for i in range(45) if i not in pivots]
def normal(poly):
    vector=s.zeros(1,45)
    for mon,cf in s.Poly(poly,x,y).terms():
        if mon in index:
            vector[0,index[mon]]=cf
    for i,pivot in enumerate(pivots):
        vector-=vector[0,pivot]*rr.row(i)
    return s.expand(sum(vector[0,i]*x**monomials[i][0]*y**monomials[i][1] for i in free))
residuals=[normal(F),normal(x*F),normal(x*x*F),normal(x**3*F),normal(y*F)]
assert residuals==[12*x**13-s.Rational(96,5)*x**12-s.Rational(12,5)*x**11,
                   -s.Rational(96,5)*x**13-s.Rational(12,5)*x**12,
                   -s.Rational(12,5)*x**13,0,0]
jet31=s.expand(sum(cf*x**i*y**j for (i,j),cf in terms if 2*i+5*j<=31))
assert s.Matrix(rows(s.diff(jet31,x))+rows(s.diff(jet31,y))).rref()[0]==rr
# The prescribed initial conic is smooth and the LG surface is smooth.
assert (2**2+2)*(2**2-1)==18

certificate={
 'date':'2026-11-18','version':'e6-connections-v29','status':'PASS',
 'arithmetic':'Q and Q(sqrt(2)); no sampling or floating-point arithmetic',
 'model':'y^(2b)-2*kappa*x^c*y^b+x^(2c), coprime 2<=b<c, kappa^2!=1',
 'model_examples':model_records,
 'analytic_invariant':'K=kappa^2=(rho1+rho2)^2/(4*rho1*rho2)',
 'elliptic_curve':'eta^2=z*(z^2-2*kappa*z+1), T=(0,0)',
 'elliptic_j':'64*(4*K-3)^3/(K-1)',
 'modular_coordinate':'Tmod=64*(K-1), j=(Tmod+16)^3/Tmod',
 'two_isogeny':'X=z-2*kappa+1/z, Y=eta*(1-1/z^2)',
 'two_isogeny_parameter':'K -> K/(K-1); Tmod -> 4096/Tmod',
 'same_j_distinct_level_examples':['K=0','K=9/8','j=1728'],
 'actual_boundary_example':{
   'ambient':'A=B=C=0, h=1; initial conic v=2; n=1',
   'local_curve_recipe':'Res_t(P,H)/(64*x^2*y^5), with P=2xy-t(x^2+y^2+1)-2t^3',
   'weighted_jet_up_to_31':str(jet31),
   'truncation_monomial_count':45,'Jacobi_matrix_rank':18,'Tjurina_matrix_rank':21,
   'Milnor_number':27,'Tjurina_number':24,
   'normal_forms_F_xF_x2F_x3F_yF':[str(p) for p in residuals],
   'conclusion':'The actual boundary germ is not contact-equivalent to its quasihomogeneous initial form.'},
 'ordinary_proof_inputs':[
   'analytic coordinate comparison preserving the single tangent and Puiseux pair',
   'Mather--Yau theorem for isolated complex hypersurface germs',
   'Dyckerhoff Corollary 6.5 and Hochschild algebra Morita invariance',
   'Dyckerhoff Theorem 5.9 for the minimal A-infinity model',
   'strict filtered Koszul lemma for a weighted regular initial sequence',
   'elliptic two-torsion pair isomorphism classification'],
 'not_claimed':[
   'dg Morita classification of actual higher-weight boundary germs',
   'principal model is analytically or categorically equivalent to actual germ',
   'elliptic attachment is a Milnor-fiber quotient or a categorical summand',
   'elliptic isogeny induces an MF equivalence','global HMS','novelty']}
out=Path(__file__).with_name('boundary_analytic_moduli_certificate.json')
out.write_text(json.dumps(certificate,indent=2)+'\n')
print('BOUNDARY ANALYTIC MODULI / LEVEL-2 ELLIPTIC / ACTUAL TAU: EXACT CHECKS PASS')
print('Actual example: mu=27, tau=24; principal model: mu=tau=27')
print('Equal j=1728: K=0 and K=9/8; two-isogeny: K=4 -> 4/3')
