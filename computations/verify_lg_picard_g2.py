#!/usr/bin/env python3
"""Exact finite algebra underlying the LG--Picard--G2 comparison.

The topological sequence, Milnor-lattice theorem, mixed Hodge theory and
Boalch--Paluba character-variety identification are separate cited proofs.
"""
import json
from pathlib import Path
import sympy as s
from sympy.matrices.normalforms import smith_normal_form

u,v,w,A,B,C,h,t,lam=s.symbols('u v w A B C h t lambda')
x,y,z,b,c,alpha,beta=s.symbols('x y z b c alpha beta')
W=u*v*w-(u*u+v*v+w*w)/2-A*u-B*v-C*w
F=x*x+y*y+z*z+x*y*z-4*A*x-4*B*y-4*C*z+8*h
assert s.expand(F.subs({x:-2*u,y:-2*v,z:-2*w})+8*(W-h))==0
Ws=W.subs({A:lam,B:lam,C:lam})
assert Ws.subs({u:-1,v:-1,w:-1,lam:2})==s.Rational(7,2)
assert Ws.subs({u:2,v:2,w:2,lam:2})==-10
assert Ws.subs({u:s.Rational(1,2),v:s.Rational(1,2),w:s.Rational(1,2),lam:-s.Rational(1,4)})==s.Rational(1,8)
assert s.expand(Ws.subs({u:s.Rational(1,2)+t,v:s.Rational(1,2)+t,w:s.Rational(1,2)+t,lam:-s.Rational(1,4)})-s.Rational(1,8)-t**3)==0
assert s.hessian(W,(u,v,w)).subs({u:s.Rational(1,2),v:s.Rational(1,2),w:s.Rational(1,2)}).rank()==2

# Picard lattice of Bl_6(P2), with H,E1,...,E6.
Q=s.diag(1,-1,-1,-1,-1,-1,-1)
bas=[s.eye(7)[:,i] for i in range(7)]
H=bas[0]; Es=bas[1:]
D=s.Matrix.hstack(*[H-Es[2*i]-Es[2*i+1] for i in range(3)])
roots=s.Matrix.hstack(H-Es[0]-Es[2]-Es[4],Es[0]-Es[1],Es[2]-Es[3],Es[4]-Es[5])
GD=D.T*Q*D; GK=roots.T*Q*roots
assert GD==s.Matrix([[-1,1,1],[1,-1,1],[1,1,-1]])
assert GK==s.Matrix([[-2,1,1,1],[1,-2,0,0],[1,0,-2,0],[1,0,0,-2]])
assert D.T*Q*roots==s.zeros(3,4)
assert abs(GD.det())==abs(GK.det())==4
assert D.T*Q*s.Matrix.hstack(Es[0],Es[2],Es[4])==s.eye(3)
assert abs(s.Matrix.hstack(D,roots).det())==4
# Discriminant nonzero representatives in the boundary lattice.
reps=[s.Matrix([s.Rational(1,2),s.Rational(1,2),0]),
      s.Matrix([0,s.Rational(1,2),s.Rational(1,2)]),
      s.Matrix([s.Rational(1,2),0,s.Rational(1,2)])]
rot=s.Matrix([[0,0,1],[1,0,0],[0,1,0]])
assert rot.T*GD*rot==GD
for i,r in enumerate(reps):
    assert all(a.q==1 for a in GD*r)
    assert rot*r==reps[(i+1)%3]

# Goldman--Neumann affine D4 matrix: four outer roots then the central root.
G=-2*s.eye(5)
for i in range(4):G[i,4]=G[4,i]=1
null=s.Matrix([1,1,1,1,2])
assert G*null==s.zeros(5,1) and G.rank()==4
T=s.Matrix.hstack(s.eye(5)[:,4],s.eye(5)[:,0],s.eye(5)[:,1],s.eye(5)[:,2],null)
assert abs(T.det())==1
assert T.T*G*T==s.diag(GK,s.zeros(1))
snf=smith_normal_form(G,domain=s.ZZ)
assert sorted(abs(int(snf[i,i])) for i in range(5))==[0,1,1,2,2]
image=s.Matrix.hstack(roots[:,1],roots[:,2],roots[:,3],-2*roots[:,0]-roots[:,1]-roots[:,2]-roots[:,3],roots[:,0])
assert image.T*Q*image==G and image*null==s.zeros(7,1)
# Algebraic product of Picard--Lefschetz reflections in this specified order.
M=s.eye(5)
for i in range(5):
    refl=s.eye(5)+s.eye(5)[:,i]*G[i,:]
    assert refl.T*G*refl==G and refl**2==s.eye(5)
    M=M*refl
xi=s.symbols('xi')
assert s.factor(M.charpoly(xi).as_expr())==(xi-1)**2*(xi+1)**3
N=M**2-s.eye(5)
assert N==null*s.Matrix([[1,1,1,1,-2]]) and N.rank()==1 and N**2==s.zeros(5)
boundary_step=s.Matrix([[0,-1],[1,1]])
assert boundary_step**3==-s.eye(2)
sb=smith_normal_form(boundary_step**3-s.eye(2),domain=s.ZZ)
assert [abs(int(sb[i,i])) for i in range(2)]==[2,2]
# Triangle incidence, used in the weight spectral sequence.
inc=s.Matrix([[-1,0,1],[1,-1,0],[0,1,-1]])
assert inc.rank()==2 and len(inc.nullspace())==1

# Boalch--Paluba base map, with b=-4 lambda and c=8 h.
al=c+2+3*b
be=-b**3+3*b**2+3*b*c+3*b-2
al_lg=8*h+2-12*lam
be_lg=64*lam**3+48*lam**2-96*lam*h-12*lam-2
assert s.expand(al.subs({b:-4*lam,c:8*h})-al_lg)==0
assert s.expand(be.subs({b:-4*lam,c:8*h})-be_lg)==0
S1=lam**2+2*lam-2*h-1
S2=-16*lam**3-3*lam**2+12*lam*h+4*h*h+2*h
C0=16*lam**2-4*lam-8*h-1
assert s.expand((b*b-8*b-4*c-16).subs({b:-4*lam,c:8*h})-16*S1)==0
assert s.expand((4*b**3-3*b*b-6*b*c+c*c+4*c).subs({b:-4*lam,c:8*h})-16*S2)==0
assert s.expand((b*b+b-c-1).subs({b:-4*lam,c:8*h})-C0)==0
cases=[(s.Integer(2),s.Rational(7,2),-8,28,'D4'),
       (-s.Rational(1,4),s.Rational(1,8),1,1,'A2')]
for l0,h0,b0,c0,typ in cases:
    assert al_lg.subs({lam:l0,h:h0})==be_lg.subs({lam:l0,h:h0})==6
    assert -4*l0==b0 and 8*h0==c0
assert s.expand((b+8)*(b-1)**2-(b**3+6*b*b-15*b+8))==0
# SL2 boundary traces all 2 produce the same D4 Fricke coefficients.
assert -(2*2+2*2)==-8 and 2**4+4*2**2-4==28

certificate={
 'date':'2026-11-17','version':'e6-connections-v20','status':'PASS',
 'field':'Q and integral lattices; exact symbolic arithmetic',
 'LG_Fricke':'(p,q,r)=(-2u,-2v,-2w), coefficients=(-4A,-4B,-4C,8h)',
 'Picard_D4_Gram':GK.tolist(),'boundary_Gram':GD.tolist(),
 'Picard_boundary_direct_sum_index':4,
 'Picard_degree_restriction_surjective':True,
 'boundary_discriminant_triality':'cyclic permutation of the three nonzero (Z/2)^2 classes',
 'affine_D4_Gram':G.tolist(),'affine_primitive_radical':[1,1,1,1,2],
 'affine_D4_Smith_diagonal':[1,1,2,2,0],
 'specified_reflection_product_charpoly':'(xi-1)^2*(xi+1)^3',
 'square_unipotent_rank':1,'square_unipotent_nilpotency_index':2,
 'boundary_torus_monodromy':[[-1,0],[0,-1]],
 'triangle_incidence_rank':2,
 'expected_Hodge_graded_dimensions':{'weight2':4,'weight3':0,'weight4':1},
 'G2_parameter_map':['8h+2-12lambda','64lambda^3+48lambda^2-96lambda*h-12lambda-2'],
 'G2_unipotent_base':[6,6],
 'G2_component_parameter_polynomial':'(b+8)*(b-1)^2',
 'LG_D4_component':{'lambda':2,'h':'7/2','b':-8,'c':28},
 'LG_A2_component':{'lambda':'-1/4','h':'1/8','b':1,'c':1},
 'separate_mathematical_inputs':[
   'cohomology sequence of compactification and Poincare duality',
   'ADE local Milnor lattice and intersection preservation',
   'unimodular lattice gluing and Aut(D4)/W(D4)',
   'Goldman--Neumann topology and boundary plumbing',
   'Deligne weight spectral sequence',
   'Boalch--Paluba Corollary 11 and Remark 12'],
 'not_claimed':['canonical comparison without choosing the degeneration',
    'derived or Fukaya equivalence','G2 quantum algebra isomorphism',
    'Hodge extension splitting','independent audit of old H3 or S5xS5 claims','novelty']}
Path(__file__).with_name('lg_picard_g2_certificate.json').write_text(json.dumps(certificate,indent=2,default=lambda x:int(x))+'\n')
print('LG / PICARD D4 / TRIALITY / AFFINE D4 / G2: EXACT CHECKS PASS')
