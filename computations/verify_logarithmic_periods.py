#!/usr/bin/env python3
"""Exact algebra behind conic matching periods and a symmetric Picard--Fuchs slice.

Topological cycle constructions, integration and the period-map interpretation
are ordinary proofs in the manuscript, not finite symbolic verification.
"""
from pathlib import Path
import json
import sympy as s

u,v,w,A,B,C,h,z,a=s.symbols('u v w A B C h z a')
W=u*v*w-(u*u+v*v+w*w)/2-A*u-B*v-C*w
Delta=u*u-1
N=(u*u+2*A*u+2*h)*Delta+B*B+C*C+2*u*B*C
v0=(B+u*C)/Delta
w0=(C+u*B)/Delta
V,T=s.symbols('V T')
centered=s.factor((W-h).subs({v:v0+V,w:w0+T},simultaneous=True))
assert s.cancel(centered+(V*V-2*u*V*T+T*T)/2+N/(2*Delta))==0

# Rational uniformization of the double cover sqrt(u^2-1).
uz=(z+1/z)/2
sz=(z-1/z)/2
assert s.cancel(sz*sz-(uz*uz-1))==0
assert s.cancel(s.diff(uz,z)/sz-1/z)==0
Nz=s.factor(N.subs(u,uz))
bb=-Nz/(sz*sz*a)
Vz=(bb-a)/(2*sz)
Tz=(a+bb)/2+uz*Vz
vz=s.factor(v0.subs(u,uz)+Vz)
wz=s.factor(w0.subs(u,uz)+Tz)
assert s.cancel((W-h).subs({u:uz,v:vz,w:wz},simultaneous=True))==0
omega_coeff=s.cancel(s.diff(uz,z)*s.diff(vz,a)/(uz*vz-wz-C))
assert omega_coeff==1/(z*a)
# Inverse to the multiplicative coordinate used on the conic.
assert s.cancel((wz-w0.subs(u,uz))-(uz+sz)*(vz-v0.subs(u,uz))-a)==0

# Symmetric zero-coefficient real vanishing sphere, h=-r^2/2.
r,theta=s.symbols('r theta',positive=True)
amp=s.sqrt(r*r-u*u)
vr=amp*s.cos(theta)/s.sqrt(1-u*u)
wr=u*vr+amp*s.sin(theta)
assert s.trigsimp(s.expand((W-h).subs({A:0,B:0,C:0,h:-r*r/2,v:vr,w:wr},simultaneous=True)))==0
jac=s.trigsimp(s.diff(vr,theta)/(u*vr-wr))
assert s.simplify(jac-1/s.sqrt(1-u*u))==0

# Picard--Fuchs operator checked in r coordinates (h=-r^2/2).
y=s.asin(r)
D_h=lambda F:s.diff(F,r)/(-r)
PF=s.factor(2*(-r*r/2)*(1-r*r)*D_h(D_h(y))+(1-2*r*r)*D_h(y))
assert PF==0
# Exponentiated period and its algebraic quadratic equation.
cr=s.sqrt(1-r*r)
Q=(cr-s.I*r)**2
assert s.simplify(s.expand(Q*Q-(2-4*r*r)*Q+1))==0
assert s.simplify(s.diff(s.log(Q),r)+2*s.I/cr)==0
# Endpoint ratio in the general matching formula.
assert s.simplify((r+s.I*cr)/(-r+s.I*cr)-Q)==0

# A concrete nontorsion multiplicative period at h=-1/10.
Qtest=s.simplify(Q.subs(r,1/s.sqrt(5)))
assert s.expand(Qtest-(3-4*s.I)/5)==0
assert s.simplify(Qtest+1/Qtest)==s.Rational(6,5)
assert not s.Rational(6,5).is_integer

# Rank-two solution monodromy on (Pi_infinity,Pi_0)^T.
M0=s.Matrix([[1,0],[0,-1]])
M4=s.Matrix([[1,0],[-1,-1]])
I=s.eye(2)
assert M0**2==I and M4**2==I
Tmon=M4*M0
assert Tmon==s.Matrix([[1,0],[-1,1]])
assert (Tmon-I)**2==s.zeros(2)
# The constant solution has no common invariant complement.
beta=s.symbols('beta')
# A complementary solution Pi_0+beta Pi_infty would have eigenvalue -1
# under both involutions: first requires beta=0, second requires beta=1/2.
assert s.solve(2*beta,beta)==[0]
assert s.solve(2*beta-1,beta)==[s.Rational(1,2)]

certificate={
 'date':'2026-11-17','version':'e6-connections-v22','status':'PASS',
 'field':'Q and exact symbolic square roots',
 'conic_discriminant':'(u^2+2Au+2h)(u^2-1)+B^2+C^2+2uBC',
 'fiber_equation':'a*b=-N(u)/(u^2-1)',
 'uniformization':'u=(z+z^-1)/2; sqrt(u^2-1)=(z-z^-1)/2',
 'residue_form':'omega=dlog(z) wedge dlog(a)',
 'matching_period':'2*pi*i * integral_gamma du/sqrt(u^2-1)',
 'real_sphere_period':'Pi_0(h)=4*pi*asin(sqrt(-2h)), -1/2<h<0',
 'boundary_period':'Pi_infinity=(2*pi*i)^2',
 'Picard_Fuchs':'2h(1+2h)*y_ddot+(1+4h)*y_dot=0',
 'exponentiated_period':'Q+Q^-1=2+8h; Q=exp(Pi_0/(2*pi*i))',
 'nonsplit_Hodge_example':{'h':'-1/10','Q':'(3-4i)/5','Q_plus_inverse':'6/5'},
 'monodromy_at_0':M0.tolist(),
 'monodromy_at_minus_half':M4.tolist(),
 'unipotent_product':Tmon.tolist(),
 'not_computer_certified':[
   'matching sphere construction and orientation',
   'analytic integration and continuation',
   'Friedman period comparison theorem',
   'whole rank-five Gauss-Manin system or mixed-Hodge splitting',
   'root-pair spheres form an integral D4 basis',
   'mirror equivalence or non-archimedean model',
   'novelty'],
}
Path(__file__).with_name('logarithmic_periods_certificate.json').write_text(
 json.dumps(certificate,indent=2,default=lambda x:int(x))+'\n')
print('CONIC LOG PERIOD / MORSE SPHERE / PICARD-FUCHS / MONODROMY: EXACT CHECKS PASS')
