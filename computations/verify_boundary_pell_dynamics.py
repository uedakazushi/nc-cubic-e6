#!/usr/bin/env python3
"""Exact arithmetic behind boundary valuations and Pell degree growth.

No random tests or floating-point inference. Piecewise-linear identities are
checked on every chamber of the relevant rational line arrangement. The
valuation-space identification and non-regularization use ordinary proofs.
"""
from pathlib import Path
import json
import sympy as s

u,v,w,A,B,C,h=s.symbols('u v w A B C h')
r,t=s.symbols('r t')
W=u*v*w-(u*u+v*v+w*w)/2-A*u-B*v-C*w
ivs=[(2*v*w-u-2*A,v,w),(u,2*u*w-v-2*B,w),(u,v,2*u*v-w-2*C)]
for iv in ivs:
    assert s.expand(W.subs(dict(zip((u,v,w),iv)), simultaneous=True)-W)==0
    jac=s.Matrix(iv).jacobian((u,v,w))
    assert s.expand(jac.det())==-1
# Vieta product relation, used to avoid cancellation in the largest sector.
P=W-h
assert s.expand(u*ivs[0][0]-(v*v+w*w+2*B*v+2*C*w+2*h)-2*P)==0

Ru=s.Matrix([[-1,-2],[0,1]])
Rv=s.Matrix([[1,0],[-2,-1]])
Rw=s.diag(1,-1)
M=s.Matrix([[1,-2],[-2,5]])
assert Rv*Rw*Ru*Rw==-M
assert all(R*R==s.eye(2) for R in (Ru,Rv,Rw))
assert M.det()==1 and M.trace()==6

# Exact all-chamber validation of Theta R_i = tropical_i Theta.
# These rays include zeros of r,t,r+t,r-t,r+2t,2r+t.
rays=[(1,0),(1,1),(0,1),(-1,2),(-1,1),(-2,1),
      (-1,0),(-1,-1),(0,-1),(1,-2),(1,-1),(2,-1)]
def ev(poly,vec):
    return s.expand(poly).subs({r:vec[0],t:vec[1]})
def abs_on(poly,left,right):
    center=(left[0]+right[0],left[1]+right[1])
    val=ev(poly,center)
    assert val!=0
    sign=1 if val>0 else -1
    assert sign*ev(poly,left)>=0 and sign*ev(poly,right)>=0
    return s.expand(sign*poly)
def max_on(f,g,left,right):
    diff=s.expand(f-g)
    if diff==0:return f
    center=(left[0]+right[0],left[1]+right[1])
    val=ev(diff,center)
    assert val!=0
    if val>0:
        assert ev(diff,left)>=0 and ev(diff,right)>=0
        return f
    assert ev(diff,left)<=0 and ev(diff,right)<=0
    return g
chambers=0
for i,left in enumerate(rays):
    right=rays[(i+1)%len(rays)]
    assert s.det(s.Matrix.hstack(s.Matrix(left),s.Matrix(right)))>0
    base=[abs_on(r,left,right),abs_on(t,left,right),abs_on(r+t,left,right)]
    for k,R in enumerate((Ru,Rv,Rw)):
        p,q=R*s.Matrix([r,t])
        image=[abs_on(p,left,right),abs_on(q,left,right),abs_on(p+q,left,right)]
        expected=base[:]
        j,l=[a for a in range(3) if a!=k]
        expected[k]=2*max_on(base[j],base[l],left,right)-base[k]
        assert all(s.expand(a-b)==0 for a,b in zip(image,expected))
        chambers+=1
assert chambers==36

def theta(pair):
    a,b=pair
    return (abs(a),abs(b),abs(a+b))
# Assemble the exact polynomial g, rightmost involution first.
g=(u,v,w)
for k in (2,0,2,1):
    g=tuple(s.expand(f.subs(dict(zip((u,v,w),g)),simultaneous=True)) for f in ivs[k])
polys=[s.Poly(f,u,v,w) for f in g]
assert [p.total_degree() for p in polys]==[3,7,4]
expected_top=[4*u*v**2,64*u**2*v**5,8*u*v**3]
for p,top in zip(polys,expected_top):
    degree=p.total_degree()
    actual=sum(cf*u**i*v**j*w**k for (i,j,k),cf in p.terms() if i+j+k==degree)
    assert s.expand(actual-top)==0
# The associated graded surface has equation uvw=0, hence all these
# pure-u,v leading monomials survive. This is justified in the manuscript.

N=s.Matrix([[1,2],[2,5]])
assert N==s.diag(1,-1)*M*s.diag(1,-1)
assert N**2-6*N+s.eye(2)==s.zeros(2)
values=[]
for n in range(0,25):
    T=N**n
    pn,qn=T*s.Matrix([1,1])
    if n==0:
        record={'n':0,'coordinate_degrees':[1,1,1],'min_affine_degree':1,
                'H_pullback_intersection':3}
    else:
        assert qn>pn>0
        # Strict dominance in the next polynomial substitution.
        assert pn+2*qn>qn+(qn-pn)
        assert pn+3*qn>2*qn+(qn-pn)
        for i in range(2):
            assert int(sum(T.row(i)))==int((pn,qn)[i])
        # Three primitive boundary divisorial valuations.
        boundary_vectors=[(0,1),(1,0),(1,-1)]
        poles=[max(theta(M**n*s.Matrix(vec))) for vec in boundary_vectors]
        assert max(poles)==qn and sum(poles)==2*qn
        a,b,c=(M**n)[0,0],-(M**n)[0,1],(M**n)[1,1]
        assert poles==[c,b,b+c]
        assert qn==b+c
        assert qn*qn-2*c*c==-1
        aa,bb=int(qn-pn),int(pn)
        cf=[]
        while bb:
            cf.append(aa//bb)
            aa,bb=bb,aa%bb
        assert cf==[1]+[2]*(2*n-2)+[3]
        assert sum(cf)==4*n
        record={'n':n,'coordinate_degrees':[int(pn),int(qn),int(qn-pn)],
                'min_affine_degree':int(qn),
                'H_pullback_intersection':int(2*qn),
                'generic_boundary_poles':[int(x) for x in poles],
                'continued_fraction_at_vertex_v':cf,
                'minimal_corner_blowups':sum(cf),
                'leading_uv_exponents':[list(map(int,T.row(0))),list(map(int,T.row(1))),
                                        list(map(int,T.row(1)-T.row(0)))]}
    values.append(record)
degrees=[x['min_affine_degree'] for x in values]
assert degrees[:7]==[1,7,41,239,1393,8119,47321]
for n in range(len(degrees)-2):
    assert degrees[n+2]==6*degrees[n+1]-degrees[n]
lam=3+2*s.sqrt(2)
vp=s.Matrix([1,-1-s.sqrt(2)])
vm=s.Matrix([1,-1+s.sqrt(2)])
assert (M*vp-lam*vp).applyfunc(s.simplify)==s.zeros(2,1)
assert (M*vm-(3-2*s.sqrt(2))*vm).applyfunc(s.simplify)==s.zeros(2,1)
for n in range(6):
    closed=((1+s.sqrt(2))*lam**n+(1-s.sqrt(2))*(3-2*s.sqrt(2))**n)/2
    assert s.simplify(closed-degrees[n])==0
# Primitive orbit approximating the expanding ray; gcd remains one.
from math import gcd
orbit=[]
for n in range(7):
    a,b=M**n*s.Matrix([1,-1])
    assert gcd(abs(int(a)),abs(int(b)))==1
    orbit.append({'n':n,'slope_pair':[int(a),int(b)],'pole_vector':list(map(int,theta((a,b))))})

cert={
    'date':'2026-11-17','version':'e6-connections-v25','status':'PASS',
    'arithmetic':'Q-polynomials, exact rational chambers and integer matrices',
    'automorphism':'g=iota_v iota_w iota_u iota_w (rightmost first)',
    'boundary_coordinates':'Theta(r,t)=(|r|,|t|,|r+t|), modulo simultaneous sign',
    'tropical_iota_u':'(2max(b,c)-a,b,c), cyclic',
    'linear_reflections':[R.tolist() for R in (Ru,Rv,Rw)],
    'all_linear_chambers_verified':chambers,
    'projective_matrix':M.tolist(),
    'leading_terms_one_iterate':[str(x) for x in expected_top],
    'exact_affine_degree_recurrence':'d0=1,d1=7,d(n+2)=6d(n+1)-d(n)',
    'degree_table':values[:8],
    'recurrence_checked_through_n':24,
    'boundary_orbit':orbit,
    'pell_identity':'d_n^2-2*c_n^2=-1',
    'minimal_corner_blowups_for_gn_Dw':'4*n, n>=1',
    'eigenvalue':'3+2sqrt(2)',
    'expanding_slope_pair':['1','-1-sqrt(2)'],
    'expanding_pole_vector':['1','1+sqrt(2)','sqrt(2)'],
    'contracting_pole_vector':['1','sqrt(2)-1','sqrt(2)'],
    'ordinary_proof_inputs':[
        'monomial valuations of the boundary triangle and invariance under Vieta',
        'associated graded quotient k[u,v,w]/(uvw) and all-n leading-term induction',
        'pole-divisor and projective pullback comparison',
        'irrational eigenlines imply no periodic boundary divisorial ray',
        'finite boundary blowup extension would permute its boundary components'],
    'known_inputs_not_reproved':[
        'Goldman--Neumann identity on open H2 for an even Vieta word',
        'Cantat--Loray entropy formula',
        'Jang tropical Markov dynamics general theory'],
    'not_claimed':[
        'new general tropicalization theorem',
        'regularization impossible on all unrelated compactifications',
        'non-Archimedean good reduction or essential skeleton theorem',
        'categorical entropy, mirror equivalence, or novelty']}
Path(__file__).with_name('boundary_pell_dynamics_certificate.json').write_text(
    json.dumps(cert,ensure_ascii=False,indent=2,default=int)+'\n')
print('BOUNDARY VALUATIONS / PELL DEGREES: EXACT CHECKS PASS')
print('first degrees:',degrees[:8])
print('linear chamber identities:',chambers)
