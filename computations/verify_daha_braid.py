import sympy as s
from functools import lru_cache
q=s.symbols('q');a,b,c=s.symbols('a b c');Q=s.Poly(q*q+q+1,q)
q0=(-1+s.sqrt(-3))/2
# Straight rewrite with an arbitrary coefficient (commuting a,b,c,q).
@lru_cache(None)
def word_nf(word):
    for pos in range(len(word)-1):
        pair=word[pos:pos+2]
        if pair == 'yx':
            terms=[(q*q,'xy'),(-q*q,'z'),(-q*q*c,'')]
        elif pair=='zx':
            terms=[(q,'xz'),(1,'y'),(b,'')]
        elif pair=='zy':
            terms=[(q*q,'yz'),(-q*q,'x'),(-q*q*a,'')]
        else:continue
        out={}
        for coef,r in terms:
            for w,v in word_nf(word[:pos]+r+word[pos+2:]).items():
                out[w]=out.get(w,0)+coef*v
        return out
    return {word:s.Integer(1)}

def normalize(p):
  out={}
  for word,coef in p.items():
    for w,factor in word_nf(word).items():out[w]=out.get(w,0)+coef*factor
  return {k:v for k,v in out.items() if v!=0}
def add(p,q_,sign=1):
  o=p.copy()
  for k,v in q_.items():o[k]=o.get(k,0)+sign*v
  return o

def mul(p,q_):
  out={}
  for x,u in p.items():
    for y,v in q_.items():out[x+y]=out.get(x+y,0)+u*v
  return normalize(out)
def powp(p,n):
  result={'':s.Integer(1)}
  for _ in range(n):result=mul(result,p)
  return result

def zero_poly(p):
  rems={w:s.rem(s.Poly(s.expand(v),q),Q).as_expr() for w,v in p.items()}
  fails={w:s.factor(v) for w,v in rems.items() if v!=0}
  return fails
X={'x':1};Y={'y':1};Z={'z':1};I={'':1}
zprime={'xy':q*q-q, 'z':-q*q,'':q*c}
# target coefficients a,b swapped; source a maps to b and source b maps to a
# Here rewrite rules above use target parameters (a,b,c), and source params (b,a,c).
r1=add(add(mul(X,zprime),mul(zprime,X),-q),add(Y,I,b),-1)
r2=add(add(mul(zprime,Y),mul(Y,zprime),-q),add(X,I,a),-1)
r3=add(add(mul(Y,X),mul(X,Y),-q),add(zprime,I,c),-1)
for name,p in [('r1',r1),('r2',r2),('r3',r3)]:
 assert not zero_poly(p), (name,zero_poly(p))
# Comparing sigma of Z_h against Vieta on center.
f=(1-q)/3;e=-(2*q+1)/9;d=-(q+2)/3
Omega=add(add(add(mul(mul(X,Y),Z),{'xx':(q-1)/3,'zz':(q-1)/3,'yy':(q+2)/3}), {'x':d*a,'y':d*q*b,'z':d*c}),{})
Xh=add(powp(X,3),{'x':q*q});Yh=add(powp(Y,3),{'y':q*q});Zh=add(powp(Z,3),{'z':q*q});
Zph=add(powp(zprime,3),{k:q*q*v for k,v in zprime.items()})
lc=((2*q+1)*c**3+2*(q-1)*c+3*q*a*b)/9
RHS=add(add(mul(Xh,Yh), {w:c*val for w,val in Omega.items()}),{'':-lc})
# clear e denominator: e*(Zph+Zh) -(Xh*Yh+cOmega-lc) = 0
LHS=add({w:e*v for w,v in add(Zph,Zh).items()},RHS,-1)
assert not zero_poly(LHS), zero_poly(LHS)
Om_source=add(add(add(mul(mul(Y,X),zprime), {k:(q-1)*v/3 for k,v in add(powp(Y,2),powp(zprime,2)).items()}),{k:(q+2)*v/3 for k,v in powp(X,2).items()}), {})
Om_source=add(Om_source,{k:d*b*v for k,v in Y.items()})
Om_source=add(Om_source,{k:d*q*a*v for k,v in X.items()})
Om_source=add(Om_source,{k:d*c*v for k,v in zprime.items()})
assert not zero_poly(add(Om_source,Omega,-1)), zero_poly(add(Om_source,Omega,-1))

import json
from pathlib import Path
certificate = {
'date':'2026-11-17','version':'e6-daha-braid-v1','status':'PASS',
'field':'Q[q]/(q^2+q+1)','PBW_rules':['yx=q^2 xy-q^2(z+c)','zx=q xz+y+b','zy=q^2 yz-q^2(x+a)'],
'quantum_sigma':'a<->b, x<->y, z->(q^2-q)xy-q^2z+q c',
'verified':['all three defining relations preserved','Omega_abc fixed','e(sigma(Z)+Z)=XY+c Omega-ell_c'],
'authoritative_input':'Terwilliger sigma from Lemma 2.3/2.5; formulas checked in original PBW algebra',
'not_proved':['all skein/DAHA root-of-unity specialization equivalences','Braid action extending to full elliptic family','categorical autoequivalence of H3 hearts']
}
Path(__file__).with_name('daha_braid_certificate.json').write_text(json.dumps(certificate,indent=2)+'\n')
print('QUANTUM BRAID / VIETA IDENTITIES: PASS')