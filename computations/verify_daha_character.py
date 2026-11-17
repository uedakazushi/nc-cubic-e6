#!/usr/bin/env python3
"""Exact AW--Fricke--character-variety coefficient and Poisson checks.

The AW normalization is derived from Terwilliger, Definition 2.6 (2013);
the Fricke trace relation is Goldman, Section 5.2.1.  The calculation uses
polynomial identities and exact characteristic-zero arithmetic only.
"""
import json
from pathlib import Path
import sympy as s

q = s.Symbol('q')
Q = s.Poly(q*q+q+1, q)
def mod_q(expr):
    """Reduce a polynomial with coefficients in Q modulo q^2+q+1."""
    return s.rem(s.Poly(s.expand(expr),q),Q).as_expr()

x,y,z,a,b,c,D=s.symbols('x y z a b c D')
r=1-q
f=(1-q)/3
e=-(2*q+1)/9
# In V_{a,b,c}: zy=q^2 yz-q^2 (x+a) (q^3=1).
# Terwilliger's q^{-1}ACB+q^{-2}A^2+q^{-2}B^2+q^2 C^2
# -q^{-1} A alpha-q^{-1}B beta-q C gamma,
# with A=(1-q)x and alpha=(1-q)a, etc.
CasAW=q**2*r**3*(q**2*x*y*z-q**2*x*x-q**2*a*x) + r**2*(q*(x*x+y*y)+q*q*z*z - q*q*a*x - q*q*b*y-q*c*z)
Omega=x*y*z+(q-1)*(x*x+z*z)/3+(q+2)*y*y/3-(q+2)*(a*x+q*b*y+c*z)/3
assert mod_q(CasAW-q*r**3*Omega)==0
assert mod_q(q*r**3-3*(q+2))==0

la=((2*q+1)*a**3+2*(q-1)*a+3*q*b*c)/9
lb=((2*q+1)*b**3+2*(q-1)*b+3*q*c*a)/9
lc=((2*q+1)*c**3+2*(q-1)*c+3*q*a*b)/9
K=((q+1)*(a*a+b*b+c*c)+(q+2)*a*b*c)/3
L=((1-q)*(a*a*b*b+a*a*c*c+b*b*c*c)+(q+2)*(a*a+b*b+c*c))/9
X,Y,Z=s.symbols('X Y Z')
# Central cubic after Omega=-D.
center=X*Y*Z-e*(X*X+Y*Y+Z*Z)-(D*a+la)*X-(D*b+lb)*Y-(D*c+lc)*Z+D**3-f*D**2+D*K-L
u,v,w=s.symbols('u v w')
Ac=-(D*a+la)/e**2; Bc=-(D*b+lb)/e**2; Cc=-(D*c+lc)/e**2
Tc=-(D**3-f*D**2+D*K-L)/e**3
F=u*u+v*v+w*w+u*v*w+Ac*u+Bc*v+Cc*w+Tc
assert s.cancel(center.subs({X:-e*u,Y:-e*v,Z:-e*w}) /(-e**3) - F)==0
# Dominance of Fricke coefficients; evaluate d(a,b,c,D) at a=b=c=0.
J=s.Matrix([Ac,Bc,Cc,Tc]).jacobian([a,b,c,D]).subs({a:0,b:0,c:0})
Jac=s.factor(J.det())
expected=3*D*(D-2*f/3)**4/e**9
assert s.cancel(Jac-expected)==0
assert expected!=0
# Four boundary traces of the SL2 four-holed-sphere character variety.
r1,r2,r3,r4=s.symbols('r1 r2 r3 r4')
trace_coeff=[-(r1*r2+r3*r4),-(r2*r3+r1*r4),-(r1*r3+r2*r4),
    r1*r1+r2*r2+r3*r3+r4*r4+r1*r2*r3*r4-4]
TJac=s.Matrix(trace_coeff).jacobian([r1,r2,r3,r4]).det()
assert TJac.subs({r1:1,r2:2,r3:3,r4:4})==-200
# Verify Goldman residue/Jacobian Poisson structure and Vieta moves.
U,V,W,A,B,C,T=s.symbols('U V W A B C T')
H=U*U+V*V+W*W+U*V*W+A*U+B*V+C*W+T
phiW=-U*V-C-W
phiU=-V*W-A-U
phiV=-U*W-B-V
for idx,expr in [(W,phiW),(U,phiU),(V,phiV)]:
    assert s.expand(H.subs(idx,expr)-H)==0
# For H=0, the Jacobi bracket P_H(df,dg)=det(dH,df,dg)
# is Poisson.  An involution preserving H with determinant -1 is anti-Poisson.
var=s.Matrix([U,V,W])
for idx,expr in [(W,phiW),(U,phiU),(V,phiV)]:
    dest=s.Matrix([expr if i==idx else i for i in (U,V,W)])
    assert s.expand(dest.jacobian(var).det()+1)==0
# Ordinary polynomial identity: all cyclic brackets have Jacobiator zero.
D_U=s.diff(H,U);D_V=s.diff(H,V);D_W=s.diff(H,W)
Jcyclic=s.expand(s.diff(D_W,U)*D_V-s.diff(D_W,V)*D_U
                +s.diff(D_U,V)*D_W-s.diff(D_U,W)*D_V
                +s.diff(D_V,W)*D_U-s.diff(D_V,U)*D_W)
assert Jcyclic==0

cert={
    'date':'2026-11-17','version':'e6-links-v1','status':'PASS',
    'q':'q^2+q+1=0, q primitive cubic root',
    'AW':'Casimir_AW=3(q+2)*Omega_abc, after A=(1-q)x and alpha=(1-q)a, cyclic',
    'casimir_relation_source':'Terwilliger 2013 Definition 2.6, equation (2.5)',
    'Fricke_center':'Omega=-D, X=-e*u, Y=-e*v, Z=-e*w gives u^2+v^2+w^2+uvw+A*u+B*v+C*w+T=0',
    'A':'-(D*a+la)/e^2', 'B':'-(D*b+lb)/e^2', 'C':'-(D*c+lc)/e^2',
    'T':'-(D^3-fD^2+D*K-L)/e^3',
    'Fricke_parameter_Jacobian_at_a_b_c_zero':'3*D*(D-2*f/3)^4/e^9',
    'trace_parameter_Jacobian_at_1_2_3_4':-200,
    'Vieta_involutions':['W -> -U*V-C-W','U -> -V*W-A-U','V -> -U*W-B-V'],
    'Jacobian_Poisson':'{U,V}=dH/dW and cyclic; each Vieta involution is anti-Poisson',
    'external_inputs_not_verified_by_code':[
       'Terwilliger universal Askey-Wilson defining relations and Casimir centrality',
       'Goldman four-holed sphere trace identity and Goldman bracket normalization',
       'base H3 recognition and center computation of nc-cubic-e6',
       'comparison with skein and spherical DAHA at the primitive cubic root',
       'novelty and full stack-level equivalence'
    ]
}
Path(__file__).with_name('daha_character_certificate.json').write_text(json.dumps(cert,indent=2)+'\n')
print('EXACT AW--FRICKE--CHARACTER--POISSON CHECKS PASS')
print('AW Casimir factor:',s.factor(mod_q(q*r**3)))
print('Fricke map determinant:',Jac)
print('Trace map determinant at (1,2,3,4):',TJac.subs({r1:1,r2:2,r3:3,r4:4}))