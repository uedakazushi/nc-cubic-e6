# Fricke・Askey–Wilson・DAHAとの比較

2026-11-17 / e6-connections-v14 / 現在有効な文献比較。研究方針はリポジトリrootの `00_research_plan.md`、成分原稿は `papers/nc-cubic-e6.tex`。

## Askey–Wilson代数との厳密な表示同型・Casimir

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
**表示同型とCasimir規約まで証明済み。** Terwilliger [Definition 2.6](https://doi.org/10.3842/SIGMA.2013.047) の中心Casimirを $\Omega_{\mathrm{AW}}$ とすれば、元のPBW関係の厳密計算により
\[
\boxed{\Omega_{\mathrm{AW}}=q(1-q)^3\Omega_{a,b,c}=3(q+2)\Omega_{a,b,c}.}
\]
従ってCasimir切断 $V_{a,b,c}/(\Omega+D)$ は普遍Askey–Wilson代数の4中心パラメータ同時特殊化そのものである。主論文 `thm:aw-casimir-exact`、厳密計算は `computations/verify_daha_character.py`。$X,Y,Z$ は三乗根特有の追加中心である（全元をDAHA側で同定することは別課題）。

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
**具体的に** $u=-X/e,v=-Y/e,w=-Z/e$ ($e=-(2q+1)/9\ne0$) と変換すると、
\[
u^2+v^2+w^2+uvw+A u+B v+C w+D_0=0
\]
という標準Fricke形に直せる。4係数へのパラメータ写像のJacobianは、原点 $a=b=c=0$ で、固定非零スケールを除き
\[
\boxed{\det d\Psi=3D(D-2f/3)^4/e^9}
\]
となる。従って $D\neq0,2f/3$ では非零で、4パラメータ $(a,b,c,D)$ からFricke係数空間への写像はdominantである。これは具体的な微分計算に基づく結果である。

特に**Fricke–Askey–Wilson locus** はこの4次元部分族にふさわしい名前である。元の固定包絡のFricke pencilは $a=b=c=0$ の1次元切断に限る。

注意：固定包絡の全中心三次直線は $\mathbb P^4$ だが、一般の切断は $\Omega=-D$ と同値ではない。$X,Y,Z$ の係数も非零で、一般境界は滑らかな楕円曲線になる。従って固定包絡4次元stack全体さえFricke型ではない。

## 四穴球面SL2 character varietyとの明示的な係数対応

Goldman, *Trace coordinates on Fricke spaces of some simple hyperbolic surfaces*, [DOI 10.4171/055-1/16](https://doi.org/10.4171/055-1/16), §5.2.1 (5.2.1.2) を一次資料で確認。四穴球面の境界モノドロミーのトレース $r_1,r_2,r_3,r_4$ は

\[
A=-(r_1r_2+r_3r_4),\quad B=-(r_2r_3+r_1r_4),\quad C=-(r_1r_3+r_2r_4),\quad T=\sum r_i^2+r_1r_2r_3r_4-4.
\]

この四変数写像のJacobianは $(1,2,3,4)$ で厳密に $-200$。従ってGoldman側と本研究側の二つのFricke係数写像は共にdominantでgenerically finite、共通の係数空間の適切な開部分で有限étale底変更後に中心がcharacter varietyに同型になる（`thm:fricke-trace-dominant`）。**中心の幾何学的同型と、量子代数自体のskein/DAHA同型は別物**。

## Braid / mapping class・量子的Vieta・Poisson

Terwilligerの $\mathrm{PSL}_2(\mathbb Z)$ 作用の生成元は $a\leftrightarrow b$, $x\leftrightarrow y$, $z\mapsto(q^2-q)xy-q^2z+qc$。三元の中心変換は $X\leftrightarrow Y$, $Z\mapsto (XY+c\Omega-\ell_c)/e-Z$ であり、Fricke座標では

\[
\boxed{(u,v,w;A,B,C,T)\mapsto(v,u,-uv-C-w;B,A,C,T)}.
\]

原関係、Casimir不変、中心元のVieta式を `verify_daha_braid.py` で独立にPBW厳密再現した。$F=u^2+v^2+w^2+uvw+Au+Bv+Cw+T$ におけるJacobian括弧 $\{u,v\}=\partial_wF$（巡回）はGoldmanのトレースPoisson形式と符号・スカラーを除いて一致する。この量子的Vieta生成元はPoisson同型である。主論文 `thm:aw-braid-vieta`, `prop:fricke-poisson-logcy`。braid群、mapping class group、Dehn twistとの作用の正確なfaithfulness・relationは先行研究と今後詳細照合する。

## なぜD4とE6が同時に現れるか：三角形付き三次曲面のPicard格子

滑らかなFricke cubicの射影閉包 \(\bar C\) は三角形 \(D_1+D_2+D_3\in|-K|\) を持つ三次del Pezzo。Picard格子には \(K^\perp\cong E_6(-1)\) があり、三角形の各成分にも直交する格子は既知の \(D_4(-1)\)（[N. Schock, *Math. Nachr.* 297 (2024), §2](https://doi.org/10.1002/mana.202300459) はNaruki--Looijengaを参照）。六点blow-up markingでは \(D_i=H-E_{2i-1}-E_{2i}\) で、\(H-E_1-E_3-E_5,E_1-E_2,E_3-E_4,E_5-E_6\) が具体的な\(D_4\) 単純根。新規の格子同定ではなく、本稿で選んだFricke座標に対する幾何学的説明である。証明は主論文 `prop:d4-inside-e6`、独立交叉計算は `verify_d4_lattice.py`。

Goldman--Toledo, [arXiv:1006.3838](https://arxiv.org/abs/1006.3838) は、無限遠で非退化tritangent planeを持つ任意のaffine三次曲面が四穴球面の相対SL2 character varietyから得られることを証明する。従って「中心がFricke cubicになる」自体の既出性を再確認し、独自の新規性候補を**三乗根でのPBW・Casimir・Braidの厳密な量子化とH3理論との接合**に絞る。

## Skein・量子群・cluster・mirror・E6への関係図

| 話題 | 確立した接点／一次文献 | 本研究で残る同定 |
|---|---|---|
| 四穴球面 skein algebra | Crampéほか、[AW avatars](https://doi.org/10.1088/1751-8121/abd783) は普遍AWをKauffman bracket skein代数に同定し、半Dehn twistをbraid作用で説明 | 本稿の $q^3=1$ 特殊化が各同型の分母・中心/周辺トレースと適合するか定理単位で調べる |
| rank-one DAHA $(C_1^\vee,C_1)$ | Terwilliger [SIGMA 2013](https://doi.org/10.3842/SIGMA.2013.047) の普遍AWから普遍DAHAへの単射；Oblomkov [IMRN 2004](https://arxiv.org/abs/math/0306393) のFricke/DAHA | 同時中央特殊化後の単射、spherical idempotent のfullness、Morita範囲、中心を計算する |
| $U_q(\mathfrak{sl}_2)$ とRacah | [AW avatars](https://doi.org/10.1088/1751-8121/abd783) が3重テンソル積の中間Casimir・R行列を記述 | 三乗根でのrestricted/unrestricted量子群と中心・braid actionの適用範囲 |
| Goldman/character stack | Goldman [trace](https://doi.org/10.4171/055-1/16) により本稿の中心は一般Fricke cubic；Hikami [SIGMA 2019](https://doi.org/10.3842/SIGMA.2019.003) でclusterへの橋 | derived/stacky character varietyと本研究の内在的H3圏の間にcanonical functorがあるか |
| log Calabi--Yau, mirror | Casimir中心の射影閉包は滑らかな場合三角形反標準cycleを持つLooijenga pair。Bousseau [CMP 2023](https://doi.org/10.1007/s00220-022-04512-9) は四穴球面skeinを三次曲面のmirrorで実現 | theta/bracelet basisと本稿のPBW・中心三次切断の関係、量子化のcluster atlas |
| Painlevé confluence | Chekhov--Mazzocco--Rubtsov [IMRN](https://doi.org/10.1093/imrn/rnw219), [Adv. Math. 2021](https://doi.org/10.1016/j.aim.2020.107442) | degenerationで本研究の楕円E6族に到達できるか、PBW/AS4を保つ極限の導出 |
| 楕円E6・GDAHA | Etingof--Ginzburg [JEMS 2010](https://doi.org/10.4171/JEMS/235) と Etingof--Oblomkov--Rains [Adv. Math. 2007](https://doi.org/10.1016/j.aim.2006.11.008) | D4型三角境界のCasimir切断とE6型滑らかな楕円境界を同一視せず、横断変形・反標準環で橋渡しする |

**重要な分離:** Casimir切断は原稿での中心三次線の $(\beta,\gamma,\delta)=(0,0,0)$ の特別な枝で、境界は三角形（一般の滑らかな楕円境界とは異なる）。四穴球面は通常 $\widetilde D_4$ 型、Etingof--Ginzburgの一般三次del Pezzoは楕円 $\widetilde E_6$ 型である。全八次元intrinsic H3を「DAHA成分」と呼ぶ根拠にはならない。

**新規性:** Casimir規約、Vieta変換、Fricke係数のこの組合せは本稿で独立に算術確認したが、個々の式の文献上の既出性は未判定。一次文献の正確な適用仮定を今後継続確認する。

## DAHA・E6の既知の対応と限界

- P. Terwilliger, *The Universal Askey–Wilson Algebra and DAHA of Type $(C_1^\vee,C_1)$*, SIGMA 9 (2013), 047, DOI 10.3842/SIGMA.2013.047, [arXiv:1202.4673](https://arxiv.org/abs/1202.4673)。普遍Askey–Wilson代数から普遍階数1 DAHAへの単射を証明している。ただしその中央特殊化が全てspherical DAHAと同型になるとは、本研究では証明していない。
- A. Oblomkov, *Double affine Hecke algebras of rank 1 and affine cubic surfaces*, IMRN 2004 (18), 877–912, DOI 10.1155/S1073792804133072, [arXiv:math/0306393](https://arxiv.org/abs/math/0306393)。$(C_1^\vee,C_1)$ DAHAの中心の三角境界付きaffine cubicとspherical量子化。通常 $\widetilde D_4$ 側の幾何学。
- P. Etingof, A. Oblomkov, E. Rains, *Generalized double affine Hecke algebras of rank 1 and quantized del Pezzo surfaces*, Adv. Math. 212 (2007), 749–796, DOI 10.1016/j.aim.2006.11.008, [arXiv:math/0406480v3](https://arxiv.org/abs/math/0406480)。$\widetilde D_4$ は三角境界の三次曲面、$\widetilde E_6$ はnodal有理曲線境界の三次曲面。今回の一般8次元族を $\widetilde E_6$ GDAHAのspherical部分と無条件に同一視しない。
- P. Etingof, V. Ginzburg, *Noncommutative del Pezzo surfaces and Calabi–Yau algebras*, JEMS 12 (2010), 1371–1416, DOI 10.4171/JEMS/235, [arXiv:0709.3593](https://arxiv.org/abs/0709.3593)。次数3 del Pezzo、単純楕円特異点 $\widetilde E_6$、滑らかな反標準楕円曲線とPoisson変形・量子化。一般8次元成分の幾何学的比較対象としてより近い。

## 一般化Sklyanin--Painlevé代数との比較

L. Chekhov, M. Mazzocco, V. Rubtsov, *Quantised Painlevé monodromy manifolds, Sklyanin and Calabi–Yau algebras*, Adv. Math. **376** (2021), 107442, DOI [10.1016/j.aim.2020.107442](https://doi.org/10.1016/j.aim.2020.107442), [arXiv:1905.02772](https://arxiv.org/abs/1905.02772) は、一般化Sklyanin–Painlevé代数を導入しPBW/PHS/Koszul性を調べ、Etingof–Ginzburg・Etingof–Oblomkov–Rains型量子del Pezzoを極限例に含むと述べる（原論文の公表要旨で確認）。本研究の固定qによる七次元族と当該パラメータ表示の正確な同定、固定包絡の五節点／七次元族の連結五重被覆・既約結節因子が先行結果に含まれるかは未確認。論文の定理番号・証明範囲を未読のまま既知定理として利用しない。

## 暫定呼称と次の研究

全8次元候補の暫定名は **elliptic $E_6$ quantization component**（楕円 $E_6$ 量子化成分）。まだ全intrinsic H3モジュライの成分を大域同定したわけではなく、正式な命名ではない。三角境界のDAHA型部分には **Fricke–Askey–Wilson locus** を使う。

次は (1) Casimir・三乗中心の全元対応、(2) root-of-unity AW特殊化から実際のspherical DAHAへの比較とMorita範囲、(3) 一般8次元Etingof–Ginzburg型族と相対H3モジュライの比較、(4) DAHA braid／mapping class群作用と圏の自己同値の関係を検証する。証明前に全8次元族を「DAHA成分」と断定しない。
