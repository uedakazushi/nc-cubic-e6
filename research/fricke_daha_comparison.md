# Fricke・Askey–Wilson・DAHAとの比較

2026-11-17 / triangle-component-v3 / 現在有効な文献比較。研究方針はリポジトリrootの `00_research_plan.md`、成分原稿は `papers/quantum_cubic_component.tex`。

## Askey–Wilson代数との厳密な表示同型

$q^2+q+1=0$ とし、Terwilligerの規約の普遍Askey–Wilson代数を $\Delta_q$ とする。中心元 $\alpha,\beta,\gamma$ は
\[
\frac{\alpha}{q+q^{-1}}
=A+\frac{qBC-q^{-1}CB}{q^2-q^{-2}}
\]
とその巡回式で与えられる。$q+q^{-1}=-1$ なので、
\[
BC-qCB=(1-q)(A+\alpha).
\]
$x=A/(1-q)$, $y=B/(1-q)$, $z=C/(1-q)$ と置くと
\[
yz-qzy=x+\frac{\alpha}{1-q},\qquad
zx-qxz=y+\frac{\beta}{1-q},\qquad
xy-qyx=z+\frac{\gamma}{1-q}.
\]
従って
\[
V_{a,b,c}:=
k\langle x,y,z\rangle/
(yz-qzy-x-a,\ zx-qxz-y-b,\ xy-qyx-z-c)
\]
は、定義関係の両方向の比較から
\[
\boxed{
V_{a,b,c}\simeq
\Delta_q/
(\alpha-(1-q)a,\ \beta-(1-q)b,\ \gamma-(1-q)c).
}
\]
**これは証明済みの表示同型**。Askey–Wilson Casimirと、三乗根で拡大する中心は現行原稿の $\Omega,X,Y,Z$ に対応する。ただしCasimirの規約を含む完全な元の対応表はまだ作成していない。

## Fricke型4次元部分族と係数空間へのdominance

中央Casimir直線だけの切断 $\Omega=-D$ を取る。$f=(1-q)/3$, $e=-(2q+1)/9$ とし、
\[
\ell_a=\frac{(2q+1)a^3+2(q-1)a+3qbc}{9}
\]
および巡回的な $\ell_b,\ell_c$、現行原稿と同じ $K,L$ を使うと、中心の式は
\[
XYZ-e(X^2+Y^2+Z^2)
-(Da+\ell_a)X-(Db+\ell_b)Y-(Dc+\ell_c)Z
+D^3-fD^2+DK-L=0.
\]
非零の座標スケール変換で
\[
u^2+v^2+w^2+uvw+A u+B v+C w+D_0=0
\]
という標準Fricke形に直せる。4係数へのパラメータ写像のJacobianは、原点 $a=b=c=0$ で、固定非零スケールを除き
\[
\boxed{-3D(D-2f/3)^4}
\]
となる。従って $D\neq0,2f/3$ では非零で、4パラメータ $(a,b,c,D)$ からFricke係数空間への写像はdominantである。これは具体的な微分計算に基づく結果である。

特に**Fricke–Askey–Wilson locus** はこの4次元部分族にふさわしい名前である。元の固定包絡のFricke pencilは $a=b=c=0$ の1次元切断に限る。

注意：固定包絡の全中心三次直線は $\mathbb P^4$ だが、一般の切断は $\Omega=-D$ と同値ではない。$X,Y,Z$ の係数も非零で、一般境界は滑らかな楕円曲線になる。従って固定包絡4次元stack全体さえFricke型ではない。

## DAHA・E6の既知の対応と限界

- P. Terwilliger, *The Universal Askey–Wilson Algebra and DAHA of Type $(C_1^\vee,C_1)$*, SIGMA 9 (2013), 047, DOI 10.3842/SIGMA.2013.047, [arXiv:1202.4673](https://arxiv.org/abs/1202.4673)。普遍Askey–Wilson代数から普遍階数1 DAHAへの単射を証明している。ただしその中央特殊化が全てspherical DAHAと同型になるとは、本研究では証明していない。
- A. Oblomkov, *Double affine Hecke algebras of rank 1 and affine cubic surfaces*, IMRN 2004 (18), 877–912, DOI 10.1155/S1073792804133072, [arXiv:math/0306393](https://arxiv.org/abs/math/0306393)。$(C_1^\vee,C_1)$ DAHAの中心の三角境界付きaffine cubicとspherical量子化。通常 $\widetilde D_4$ 側の幾何学。
- P. Etingof, A. Oblomkov, E. Rains, *Generalized double affine Hecke algebras of rank 1 and quantized del Pezzo surfaces*, Adv. Math. 212 (2007), 749–796, DOI 10.1016/j.aim.2006.11.008, [arXiv:math/0406480v3](https://arxiv.org/abs/math/0406480)。$\widetilde D_4$ は三角境界の三次曲面、$\widetilde E_6$ はnodal有理曲線境界の三次曲面。今回の一般8次元族を $\widetilde E_6$ GDAHAのspherical部分と無条件に同一視しない。
- P. Etingof, V. Ginzburg, *Noncommutative del Pezzo surfaces and Calabi–Yau algebras*, JEMS 12 (2010), 1371–1416, DOI 10.4171/JEMS/235, [arXiv:0709.3593](https://arxiv.org/abs/0709.3593)。次数3 del Pezzo、単純楕円特異点 $\widetilde E_6$、滑らかな反標準楕円曲線とPoisson変形・量子化。一般8次元成分の幾何学的比較対象としてより近い。

## 暫定呼称と次の研究

全8次元候補の暫定名は **elliptic $E_6$ quantization component**（楕円 $E_6$ 量子化成分）。まだ全intrinsic H3モジュライの成分を大域同定したわけではなく、正式な命名ではない。三角境界のDAHA型部分には **Fricke–Askey–Wilson locus** を使う。

次は (1) Casimir・三乗中心の全元対応、(2) root-of-unity AW特殊化から実際のspherical DAHAへの比較とMorita範囲、(3) 一般8次元Etingof–Ginzburg型族と相対H3モジュライの比較、(4) DAHA braid／mapping class群作用と圏の自己同値の関係を検証する。証明前に全8次元族を「DAHA成分」と断定しない。
