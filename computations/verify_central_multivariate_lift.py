#!/usr/bin/env python3
"""Verify the exact multivariable three-torsion limit of the corrected central formula. The double vanishing proves a regular rational all-order lift, not merely a finite jet."""
import sys,json
from pathlib import Path
from verify_rains_central_formula import *
ks,ys,zs,las,lbs,lcs=S.symbols('kappa eta zeta a b c');R=E.frac_field(ks,ys,zs,las,lbs,lcs);kap,eta,zeta,la,lb,lc=R.gens
RC=lambda v:R.field.ground_new(v)
monoms=[(0,0),(1,0),(0,1),(2,0),(1,1),(0,2)]
def jetpoly(p):
 out={m:E.zero for m in monoms}
 for (a,b),v in p.items():
  if b>2:continue
  for j in range(min(a,2-b)+1):out[j,b]+=E.convert(v)*E.convert(S.binomial(a,j))*q0**(a-j)
 return out
def jet(rat):
 n,d=jetpoly(rat.numer),jetpoly(rat.denom);assert d[0,0];o={}
 for a,b in monoms:
  v=n[a,b]
  for (h,k),dd in d.items():
   if h+k and h<=a and k<=b:v-=dd*o[a-h,b-k]
  o[a,b]=v/d[0,0]
 return o
subs=[-eta*zeta,-zeta/eta,-eta/zeta,-eta*zeta*la,-zeta*lb,-eta*lc];dq=-RC(q0)*kap;dt=-3*eta*zeta;lead={}
for word,pol in normal_center.items():
 if not word:continue
 value=R.zero
 for m,rat in pol.items():
  jj=jet(rat);assert not any(jj[x] for x in [(0,0),(1,0),(0,1)]),(word,m)
  v=RC(jj[2,0])*dq*dq+RC(jj[1,1])*dq*dt+RC(jj[0,2])*dt*dt
  for a,b in zip(subs,m):v*=a**b
  value+=v
 value*=eta**word.count(1)*zeta**word.count(2)
 if value:lead[word]=value
print('ALL NONCONSTANT COEFFICIENTS VANISH TO ORDER TWO',flush=True)
coef=lead[(0,0,0)];assert coef
print('leading x3 coefficient',S.factor(R.to_sympy(coef)),flush=True)
lead={w:c/coef for w,c in lead.items()};qR=RC(q0);d=-(qR+2)/3
expected={(0,0,0):R.one,(1,1,1):eta**3,(2,2,2):zeta**3,(0,1,2):kap,(0,0):kap*(qR-1)/3,(1,1):kap*(qR+2)/3,(2,2):kap*(qR-1)/3,(0,):qR*qR+kap*d*la,(1,):eta**3*qR*qR+kap*qR*d*lb,(2,):zeta**3*qR*qR+kap*d*lc}
diff={w:lead.get(w,R.zero)-expected.get(w,R.zero) for w in lead.keys()|expected.keys()};diff={w:v for w,v in diff.items() if v}
print('limit differences',{str(w):str(R.to_sympy(v)) for w,v in diff.items()},flush=True);assert not diff
Path(__file__).with_name('central_multivariate_lift_certificate.json').write_text(json.dumps({'status':'PASS','all_nonconstant_coefficients_vanish_to_order_two':True,'normalized_limit':'kappa*Omega(a,b,c)+X+eta^3*Y+zeta^3*Z','formal_parameters':['lambda','kappa','eta','zeta','a','b','c','D'],'potential':'(1+kappa*lambda)*xyz-q0*xzy+lambda*(x^3+eta^3*y^3+zeta^3*z^3)-(x^2+y^2+z^2)/2-a*x-b*y-c*z','substitution':{'q':'q0/(1+kappa*lambda)','t':'-3*lambda*eta*zeta/(1+kappa*lambda)','a1':'-eta*zeta/(1+kappa*lambda)','b1':'-zeta/(eta*(1+kappa*lambda))','c1':'-eta/(zeta*(1+kappa*lambda))','a2':'-eta*zeta*a/(1+kappa*lambda)','b2':'-zeta*b/(1+kappa*lambda)','c2':'-eta*c/(1+kappa*lambda)'},'leading_x3_coefficient':'9*eta^2*zeta^2*(1+q0)','normalized_cut':'(N-N_constant)/N_x3+D, after X=x,Y=eta*y,Z=zeta*z; cancel common lambda^2','not_claimed':['all intrinsic deformation coverage','relative H3 algebraicity','complete global component classification']},indent=2)+'\n')
