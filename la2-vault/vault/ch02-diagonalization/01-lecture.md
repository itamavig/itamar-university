---
title: "פרק 2 — אלכסוניות של העתקות לינאריות: הרצאה"
chapter: ch02-diagonalization
source: lecture-yehuda
status: lecture-done
tags: [la2, lecture, ch02-diagonalization]
---

# אלכסוניות של העתקות לינאריות — הרצאה

> [!info] מקור
> פרק 2 מתוך הרצאות יהודה שלום, תשע"ט סמסטר ב׳ (עמודים 1–12).

---

## § 2 — לכסינות של העתקה לינארית

> [!abstract] הגדרה 2.1 — לכסינות
> תהי $T : V \to V$ העתקה לינארית על מרחב וקטורי $V$ ממימד סופי $n$ מעל שדה $F$. נאמר ש-$T$ **לכסינה** אם קיים בסיס של $V$ המורכב כולו מוקטורים עצמיים של $T$.

> [!abstract] מסקנה 2.2 — $n$ ערכים עצמיים שונים גוררים לכסינות
> אם ל-$T : V \to V$ ($\dim V = n$) יש $n$ ערכים עצמיים שונים זה מזה, אז $T$ לכסינה.
>
> **הוכחה:** יהיו $v_1, \ldots, v_n$ וקטורים עצמיים עם ערכים עצמיים שונים $\lambda_1, \ldots, \lambda_n$. לפי משפט 1.8 (וקטורים עצמיים עם ערכים עצמיים שונים הם בת"ל), הקבוצה $\{v_1, \ldots, v_n\}$ בת"ל. מכיוון ש-$|B| = n = \dim V$, הרי שזהו בסיס של $V$ המורכב מוקטורים עצמיים. $\blacksquare$
>
> חשוב להעיר שבהחלט $T$ יכולה להיות לכסינה גם כשלא כל הו"ע בבסיס הם עם ע"ע שונים — כמו בטרנספורמציית הזהות.

> [!proof]+ Natural Deduction — Proof 1
>
> | # | Claim | Justification |
> |---|-------|---------------|
> | 1 | Let $v_1, \ldots, v_n$ be eigenvectors of $T$ with distinct eigenvalues $\lambda_1, \ldots, \lambda_n$ | $T$ has $n$ distinct eigenvalues (hypothesis) |
> | 2 | $\{v_1, \ldots, v_n\}$ is linearly independent | Theorem 1.8 |
> | 3 | $|\{v_1,\ldots,v_n\}| = n = \dim V$ | by construction |
> | 4 | $\{v_1, \ldots, v_n\}$ is a basis of $V$ | rows 2–3: LI set of $n$ vectors in an $n$-dimensional space is a basis |
> | 5 | $T$ is diagonalizable | row 4: basis consists of eigenvectors (Definition 2.1) |

> [!abstract] מסקנה 2.3 — איחוד קבוצות בת"ל ממרחבים עצמיים הוא בת"ל
> תהי $T : V \to V$ העתקה לינארית. יהיו $\lambda_1, \ldots, \lambda_k$ ערכים עצמיים שונים של $T$, ולכל $i$ תהי $B_i \subseteq V_{\lambda_i}$ קבוצה בלתי תלויה לינארית. אזי $B = B_1 \cup \cdots \cup B_k$ בלתי תלויה לינארית.
<!-- corrected: source says Bᵢ is any LI subset of V_{λᵢ}, not necessarily a basis; also updated title accordingly -->
>
> (זוהי הכללה טבעית של משפט 1.8, בו כל $B_i$ מכיל וקטור עצמי בודד.)

> [!note]- הוכחה
> נניח בשלילה שיש תלות לינארית, כלומר קיים צירוף לינארי לא טריוויאלי:
> $$\sum_{i=1}^{k} \sum_{j} a_{ij} v_{ij} = 0,\quad v_{ij} \in B_i,$$
> עם לפחות מקדם אחד שונה מאפס. נגדיר לכל $i$:
> $$u_i = \sum_{j} a_{ij} v_{ij} \in V_{\lambda_i}.$$
> אז $\displaystyle\sum_{i=1}^{k} u_i = 0$ עם $u_i \in V_{\lambda_i}$.
>
> כעת, $u_i$ הוא צירוף לינארי של וקטורי $B_i \subseteq V_{\lambda_i}$ — לכן $u_i \in V_{\lambda_i}$.
>
> לפי משפט 1.8 (וקטורים עצמיים עם ע"ע שונים בת"ל), הביטוי $\sum u_i = 0$ מחייב $u_i = 0$ לכל $i$. אבל $B_i$ בת"ל, ולכן $u_i = 0$ גורר שכל מקדמי $u_i$ (כלומר $a_{ij}$ לכל $j$) אפסיים. אבל זה סותר את ההנחה שהצירוף לא טריוויאלי. $\blacksquare$

> [!proof]+ Natural Deduction — Proof 1
>
> | # | Claim | Justification |
> |---|-------|---------------|
> | 1 | Assume $B = B_1 \cup \cdots \cup B_k$ is linearly dependent | for contradiction |
> | 2 | There is a non-trivial linear combination: $\displaystyle\sum_{i=1}^{k}\sum_{j} a_{ij} v_{ij} = 0$, $v_{ij} \in B_i$, not all $a_{ij} = 0$ | definition of linear dependence |
> | 3 | Define $u_i = \displaystyle\sum_j a_{ij} v_{ij}$ for each $i$ | grouping terms by eigenvalue block |
> | 4 | $u_i \in V_{\lambda_i}$ | row 3: $B_i \subseteq V_{\lambda_i}$ and $V_{\lambda_i}$ is a subspace (Claim 1.5) |
> | 5 | $\displaystyle\sum_{i=1}^k u_i = 0$ | rows 2–3: rearranging the original sum |
> | 6 | $u_i = 0$ for all $i$ | row 5 + row 4: Theorem 1.8 (eigenvectors of distinct eigenvalues are LI) |
> | 7 | $a_{ij} = 0$ for all $i, j$ | row 6: each $B_i$ is LI, so $u_i = \sum_j a_{ij}v_{ij} = 0$ forces all coefficients to zero |
> | 8 | Contradiction | rows 2, 7 |
> | 9 | $B$ is linearly independent | by contradiction (rows 1–8) |

> [!abstract] מסקנה 2.4 — קריטריון ללכסינות דרך מרחבים עצמיים
> תהי $T : V \to V$ העתקה לינארית עם $\dim V = n$. אזי תמיד מתקיים:
> $$\sum_{\lambda} \dim V_\lambda \leq n,$$
> ושוויון מתקיים אם ורק אם $T$ לכסינה.
<!-- corrected: source states the inequality ∑dim V_λ ≤ n explicitly, with equality iff T is diagonalizable; the vault previously only stated the equality criterion without the inequality -->

> [!note]- הוכחה
> **($\Rightarrow$)** נניח ש-$T$ לכסינה, ויהי $\{v_1, \ldots, v_n\}$ בסיס של $V$ מוקטורים עצמיים. כל $v_i$ שייך למרחב עצמי $V_{\lambda}$ כלשהו. נקבץ: לכל ע"ע $\lambda$ בין $v_1,\ldots,v_n$ יש בדיוק כמה שהם וקטורים עם ע"ע $\lambda$; אלה בת"ל (חלק מבסיס) ושייכים ל-$V_\lambda$, ולכן $\dim V_\lambda \ge$ מספרם. מסך כל הקבוצות מתקבל $\sum_\lambda \dim V_\lambda \ge n$. מכיוון שכל $V_\lambda \subseteq V$ ו-$\sum_\lambda \dim V_\lambda \le \dim V = n$ (ממסקנה 2.3, האיחוד בת"ל ולכן הסכום לא עולה על $n$), נקבל שוויון.
>
> **($\Leftarrow$)** נניח $\sum_\lambda \dim V_\lambda = n$. יהי $B_\lambda$ בסיס של $V_\lambda$ לכל ע"ע $\lambda$, ויהי $B = \bigcup_\lambda B_\lambda$. לפי מסקנה 2.3, $B$ בת"ל. מספר האיברים ב-$B$ הוא $\sum_\lambda \dim V_\lambda = n = \dim V$. קבוצה בת"ל עם $n$ איברים במרחב ממימד $n$ היא בסיס. לכן $B$ בסיס של $V$ המורכב מוקטורים עצמיים, כלומר $T$ לכסינה. $\blacksquare$

> [!proof]+ Natural Deduction — Proof 1 (⇒)
>
> | # | Claim | Justification |
> |---|-------|---------------|
> | 1 | Assume $T$ is diagonalizable; let $\{v_1,\ldots,v_n\}$ be a basis of eigenvectors | Definition 2.1 |
> | 2 | For each eigenvalue $\lambda$, let $B_\lambda = \{v_i \mid Tv_i = \lambda v_i\}$ | grouping basis vectors by eigenvalue |
> | 3 | $B_\lambda$ is LI and $B_\lambda \subseteq V_\lambda$, so $|B_\lambda| \leq \dim V_\lambda$ | row 2: LI subset of a subspace has size ≤ subspace dimension |
> | 4 | $\displaystyle\sum_\lambda |B_\lambda| = n$ | row 1: the $B_\lambda$ partition the basis of $n$ vectors |
> | 5 | $\displaystyle\sum_\lambda \dim V_\lambda \geq n$ | rows 3–4 |
> | 6 | $\displaystyle\sum_\lambda \dim V_\lambda \leq n$ | Corollary 2.3: union of bases $B_\lambda'$ of $V_\lambda$ is LI, so $\sum \dim V_\lambda \leq \dim V = n$ |
> | 7 | $\displaystyle\sum_\lambda \dim V_\lambda = n$ | rows 5–6 |

> [!proof]+ Natural Deduction — Proof 2 (⇐)
>
> | # | Claim | Justification |
> |---|-------|---------------|
> | 1 | Assume $\displaystyle\sum_\lambda \dim V_\lambda = n$; for each eigenvalue $\lambda$ let $B_\lambda$ be a basis of $V_\lambda$ | hypothesis |
> | 2 | $B = \bigcup_\lambda B_\lambda$ is linearly independent | Corollary 2.3 |
> | 3 | $|B| = \displaystyle\sum_\lambda \dim V_\lambda = n = \dim V$ | rows 1–2 |
> | 4 | $B$ is a basis of $V$ | rows 2–3: LI set of $n$ vectors in an $n$-dimensional space |
> | 5 | $T$ is diagonalizable | row 4: $B$ is a basis of eigenvectors (Definition 2.1) |

---

[[02-tirgul|דוגמאות מהתרגול →]]  |  [[03-exercises|תרגילים →]]
