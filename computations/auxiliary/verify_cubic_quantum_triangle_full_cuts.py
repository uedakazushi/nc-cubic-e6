exec(open('computations/verify_cubic_quantum_triangle.py').read().split('# The only')[0])
b,c,d=s.symbols('b c d');v={(0,):b,(1,):c,(2,):d}
O={(0,1,2):s.Integer(1),(0,0):(q-1)/3,(1,1):(q+2)/3,(2,2):(q-1)/3}
XYZ=[{(i,i,i):s.Integer(1),(i,):red(q*q)} for i in range(3)]
N={}
for z,coef in zip(XYZ,[b**3,c**3,d**3]):N=add(N,z,coef)
N=add(N,O,-3*q*b*c*d)
F=add(add(mul(mul(v,v),v),v,q*q*(b*b+c*c+d*d)),N,-1)
assert not F,F
print('PASS universal root3 linear reduced norm characteristic identity')
# Norm-image cubic and rational compact centre.
a=s.symbols('a');alpha=-3*q*b*c*d;beta=b**3;gamma=c**3;delta=d**3
assert red(alpha**3+27*beta*gamma*delta)==0
S,U,V,W,T=s.symbols('S U V W T');F=2*U*V*W-T*(U*U+V*V+W*W)+3*T*S*S+2*S**3
from itertools import product,combinations
nodes=[[0,0,0,0,1]]+[[-1,*eps,1] for eps in product([1,-1],repeat=3) if eps[0]*eps[1]*eps[2]==1]
coords=[S,U,V,W,T];Fa=F.subs(T,1);Ha=s.hessian(Fa,[S,U,V,W]);aa,bb,cc,dd=s.symbols('A B C E');cov=s.Matrix([aa,bb,cc,dd])
for p in nodes:
 point=dict(zip(coords,p));assert F.subs(point)==0 and all(s.diff(F,x).subs(point)==0 for x in coords)
 H=Ha.subs(point);assert H.det()!=0
 if p[0]==0:assert s.expand(6*(cov.T*H.inv()*cov)[0]-(aa*aa-3*(bb*bb+cc*cc+dd*dd)))==0
 else:
  ep=p[1:4];quad=-2*aa*aa-3*(bb*bb+cc*cc+dd*dd)+3*(ep[0]*bb+ep[1]*cc+ep[2]*dd)**2
  assert s.expand(12*(cov.T*H.inv()*cov)[0]-quad)==0
for pp in combinations(nodes,4):assert s.Matrix(pp).rank()==4
# Casimir pencil regular tangencies: one origin branch and four sign branches.
assert s.factor(Fa.subs({U:0,V:0,W:0}))==S*S*(2*S+3)
assert s.factor(Fa.subs({U:1,V:1,W:1}))==(S+1)**2*(2*S-1)
import json
from pathlib import Path
cert={'version':'classification-v60','norm_image':'alpha^3+27 beta gamma delta=0 in P4[alpha,beta,gamma,delta,epsilon]','linear_norm':'Nrd(a t+b x+c y+d z)=b³X+c³Y+d³Z-3q bcd Omega+(a³+q²a(b²+c²+d²))t³','compact_centre':'F=2UVW-T(U²+V²+W²)+3TS²+2S³ in P4','five_nodes':nodes,'no_four_nodes_coplanar':True,'node_normal_quadric':'Hessian inverse covector, exact formulas verified','Casimir_pencil_regular_tangencies':['rho=3/2 (one point)','rho=-1/2 (four points)'],'scope':'Exact universal PBW cubic norm identity, norm-image equation, compact nodes/ranks/Hessians and pencil tangency identities. Full-cut H3 proof is ordinary geometry/order/McKay argument.'}
Path(__file__).with_name('cubic_quantum_triangle_full_cuts_certificate.json').write_text(json.dumps(cert,indent=2)+'\n')
print('PASS full root3 norm hypersurface, five-node centre, normal quadrics and pencil compatibility')
# Exact examples in each nontrivial inertia stratum; no regular tangencies.
lam,inv=s.symbols('lam inv')
examples=[('A4',[1,0,0,0,0]),('C2',[1,1,0,0,0]),('C3',[0,1,1,1,0])]
for label,co in examples:
 A,B,C,E,K=co;linear=A*S+B*U+C*V+E*W+K
 eqs=[Fa,linear]+[s.diff(Fa,x)-lam*y for x,y in zip([S,U,V,W],co[:4])]+[lam*inv-1]
 gg=s.groebner(eqs,inv,lam,S,U,V,W);assert list(gg)==[1],(label,gg)
 cv=s.Matrix(co[:4])
 for p in nodes:
  if sum(x*y for x,y in zip(p,co))==0:assert (cv.T*Ha.subs(dict(zip(coords,p))).inv()*cv)[0]!=0
# All signed cyclic matrices, and stabilizer sizes on the examples.
from itertools import product
signs=[p for p in product([1,-1],repeat=3) if p[0]*p[1]*p[2]==1]
def stab(co):
 count=0
 for ep in signs:
  for shift in range(3):
   out=[co[0],*[ep[i]*co[1+(i+shift)%3] for i in range(3)],co[4]]
   if s.Matrix([co,out]).rank()==1:count+=1
 return count
assert [stab(co) for _,co in examples]==[12,2,3]
assert stab([1,2,3,5,7])==1
# Nontrivial projective eigenpoints of an order3 cycle are node-tangent.
assert red(1+q**2+q**4)==0
cert.update({'exact_good_inertia_examples':examples,'stabilizer_orders':[12,2,3],'regular_tangency_ideals':'unit ideals, exact Groebner','generic_stabilizer_example_order':1})
Path(__file__).with_name('cubic_quantum_triangle_full_cuts_certificate.json').write_text(json.dumps(cert,indent=2)+'\n')
print('PASS full-cut exact good A4/C2/C3 examples and stabilizer enumeration')
