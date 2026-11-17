#!/usr/bin/env python3
"""Exact algebra for affine zero entropy versus filtered and proper growth.

Cone complexity, saturation comparison, localization, and cyclic HKR are
ordinary mathematical proofs, not claims certified by this script.
"""
from pathlib import Path
import json
import sympy as s

u,v,w,A,B,C,h=s.symbols('u v w A B C h')
variables=(u,v,w)
W=u*v*w-(u*u+v*v+w*w)/2-A*u-B*v-C*w-h

def involution(coords, i):
    out=list(coords)
    j,k=[z for z in range(3) if z!=i]
    out[i]=s.expand(2*out[j]*out[k]-out[i]-2*(A,B,C)[i])
    return tuple(out)

coords=variables
for i in (2,0,2,1):
    coords=involution(coords,i)
assert s.expand(W.subs(dict(zip(variables,coords)),simultaneous=True)-W)==0
expected_degrees=(3,7,4)
expected_top=(4*u*v*v,64*u*u*v**5,8*u*v**3)
for expr,degree,top in zip(coords,expected_degrees,expected_top):
    p=s.Poly(expr,*variables)
    assert p.total_degree()==degree
    leading=sum(cf*s.prod(z**a for z,a in zip(variables,mon))
                for mon,cf in p.terms() if sum(mon)==degree)
    assert s.expand(leading-top)==0
    assert not any(mon[2] for mon,cf in s.Poly(leading,*variables).terms())

M=s.Matrix([[1,-2],[-2,5]])
N=s.Matrix([[1,2],[2,5]])
assert M.det()==1 and M.trace()==6
assert N==s.diag(1,-1)*M*s.diag(1,-1)
assert M**2-6*M+s.eye(2)==s.zeros(2)
G=s.Matrix([[-1,1,1],[1,-1,1],[1,1,-1]])
b,c,z=s.symbols('b c z')
d=b+c
P=s.Matrix([c,b,d])
assert (P.T*G*P)[0]==4*b*c
assert (s.ones(1,3)*G*P)[0]==2*d
assert G*P==s.Matrix([2*b,2*c,0])
# Riemann--Roch on a rational cubic surface, K=-H.
H=s.ones(3,1)
def chi_div(L):
    return 1+((L.T*G*L)[0]+(L.T*G*H)[0])/2
assert s.expand(chi_div(z*H)-chi_div(z*H-P)-(2*d*z+d-2*b*c))==0

rows=[]
previous=[]
for n in range(25):
    T=M**n
    an,bn,cn=int(T[0,0]),-int(T[0,1]),int(T[1,1])
    dn=bn+cn
    pn=an+bn
    vector=s.Matrix([cn,bn,dn])
    poles=[]
    for ray in (s.Matrix([0,1]),s.Matrix([1,0]),s.Matrix([1,-1])):
        r,t=T*ray
        poles.append(int(abs(t)))  # pole of the v-coordinate after pullback
    assert poles==list(vector)
    assert (vector.T*G*vector)[0]==4*bn*cn
    assert (H.T*G*vector)[0]==2*dn
    genus=1+2*bn*cn-dn
    assert genus>=0
    assert dn*dn-2*cn*cn==-1
    if n>=2:assert dn==6*previous[-1]-previous[-2]
    previous.append(dn)
    rows.append({'n':n,'b':bn,'c':cn,'d':dn,'degree':2*dn,
                 'arithmetic_genus':genus,'chi_structure_sheaf':dn-2*bn*cn})
assert [r['arithmetic_genus'] for r in rows[:4]]==[0,14,656,23422]
assert [r['degree'] for r in rows[:4]]==[2,14,82,478]

# The pole-order filtration is the degree filtration for a projective cubic.
hilbert=[]
for m in range(21):
    count=sum(1 for i in range(m+1) for j in range(m+1-i)
                for k in range(m+1-i-j) if min(i,j,k)==0)
    formula=(3*m*m+3*m+2)//2
    assert count==formula
    hilbert.append(count)

certificate={
 'date':'2026-11-17','version':'e6-connections-v26','status':'PASS',
 'arithmetic':'Q[A,B,C,h] and integral intersection matrices; no numerical inference',
 'Vieta_word':'iota_v iota_w iota_u iota_w (right to left)',
 'one_step_minimal_degrees':expected_degrees,
 'one_step_leading_terms':[str(x) for x in expected_top],
 'filtration_dimension':'(3m^2+3m+2)/2',
 'Hilbert_dimensions_m0_to20':hilbert,
 'curve_polar_class':'c_n D_u+b_n D_v+(b_n+c_n)D_w',
 'curve_degree':'2d_n',
 'curve_self_intersection':'4b_n c_n',
 'curve_arithmetic_genus':'1+2b_n c_n-d_n',
 'curve_Hilbert_polynomial':'2d_n m+d_n-2b_n c_n',
 'checked_n_range':[0,24],
 'displayed_integer_rows':rows[:4]+rows[-1:],
 'ordinary_proof_conclusions':{
   'affine_DHKK_entropy':'h_t(Lg*)=0 for every real t',
   'pole_distortion_exponent':'log(3+2sqrt(2))',
   'proper_closure_object_complexity_rate':'2log(3+2sqrt(2))',
   'affine_curve_object_complexity':'at most 2 relative to O_U',
   'periodic_cyclic_action':'identity; HP_even rank 6, HP_odd zero'},
 'not_computer_certified':[
   'DHKK tower lower bound and fixed generator proof',
   'general linear-equivalence invariance of filtration distortion',
   'all-n boundary and degree statements from the preceding section',
   'normalization genus and boundary singularity support',
   'proper saturated DHKK comparison and cohomology estimates',
   'HKR/cyclic de Rham comparison',
   'equivariant or filtered homological mirror equivalence',
   'novelty or independent audit of the entire manuscript']}
Path(__file__).with_name('localization_entropy_certificate.json').write_text(
 json.dumps(certificate,ensure_ascii=False,indent=2)+'\n')
print('LOCALIZATION / POLE DISTORTION / PROPER CLOSURE: EXACT CHECKS PASS')
print('n degree genus:',[(r['n'],r['degree'],r['arithmetic_genus']) for r in rows[:4]])
