---
title: "פרק 3 — ע״ע וו״ע של מטריצות: הרצאה"
chapter: ch03-matrix-eigenvalues
source: lecture-yehuda
status: lecture-done
tags: [la2, lecture, ch03-matrix-eigenvalues]
---

# ע״ע וו״ע של מטריצות — הרצאה

> [!info] מקור
> פרק 3 מתוך הרצאות יהודה שלום, תשע״ט סמסטר ב׳ (עמודים 1–12).

---

## § 3 — ערכים עצמיים ווקטורים עצמיים של מטריצות

> [!abstract] הגדרה 3.1 — ו״ע וע״ע של מטריצה
> יהי $F$ שדה ו-$A \in M_n(F)$. וקטור $0 \neq v \in F^n$ נקרא **וקטור עצמי** של $A$ אם קיים $\lambda \in F$ כך ש-$Av = \lambda v$. הסקלר $\lambda$ נקרא **הערך העצמי** של $A$ המתאים ל-$v$.
>
> נשים לב שהגדרה זו היא מקרה פרטי של אותם מושגים עבור ט"ל: בהינתן $A$ נביט בט"ל $T_A : F^n \to F^n$ הנתונה על ידי $T_A(v) = Av$. אז $v$ ו"ע של $A$ אם ורק אם הוא ו"ע של $T_A$, וכנ"ל עבור $\lambda$.



> [!example] דוגמה 3.2
> תהי
> $$A = \begin{pmatrix} 5 & 2 & -1 \\ 2 & 2 & 2 \\ -1 & 4 & 3 \end{pmatrix}, \qquad v = \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix}.$$
> נבדוק:
> $$Av = \begin{pmatrix} 5+2-1 \\ 2+2+2 \\ -1+4+3 \end{pmatrix} = \begin{pmatrix} 6 \\ 6 \\ 6 \end{pmatrix} = 6v.$$
> לכן $v$ הוא ו״ע של $A$ עם ע״ע $\lambda = 6$.

---

> [!abstract] משפט 3.3 — קשר בין ו״ע של מטריצה לו״ע של ההעתקה
> יהי $V$ מ״ו ממימד $n$ מעל $F$, $T : V \to V$ העתקה לינארית, ו-$B$ בסיס של $V$. נסמן $A = [T]_B$. אז:
> $v$ הוא ו״ע של $T$ עם ע״ע $\lambda$ אם ורק אם $[v]_B$ הוא ו״ע של $A$ עם ע״ע $\lambda$.

> [!note]- הוכחה
> נניח ש-$v \in V$ ו״ע של $T$ עם ע״ע $\lambda$. מתקיים:
> $$A[v]_B = [Tv]_B = [\lambda v]_B = \lambda[v]_B.$$
> לכן $[v]_B$ הוא ו״ע של $A$ עם ע״ע $\lambda$.
>
> בכיוון השני חוזרים על אותו סיפור: נניח כי $A[v]_B = \lambda[v]_B$. אז מתקיים $[Tv]_B = [\lambda v]_B$, ולכן $Tv = \lambda v$. מכאן נקבל כי $v$ ו״ע של $T$ עם ע״ע $\lambda$. $\blacksquare$

> [!proof]+ Natural Deduction — Proof 1 (⇒)
>
> | # | Claim | Justification |
> |---|-------|---------------|
> | 1 | Assume $v \in V$ is an eigenvector of $T$ with eigenvalue $\lambda$: $Tv = \lambda v$ | hypothesis |
> | 2.0 | $A[v]_B =$ | &emsp;&emsp;<small>(show $[v]_B$ is eigenvector of $A$)</small> |
> | 2.1 | &emsp;$= [Tv]_B$ | $A = [T]_B$: representing matrix acts as $A[v]_B = [Tv]_B$ |
> | 2.2 | &emsp;$= [\lambda v]_B$ | row 1: $Tv = \lambda v$ |
> | 2.3 | &emsp;$= \lambda[v]_B$ | linearity of the coordinate map |
> | 3 | $[v]_B$ is an eigenvector of $A$ with eigenvalue $\lambda$ | rows 2.0–2.3 |

> [!proof]+ Natural Deduction — Proof 2 (⇐)
>
> | # | Claim | Justification |
> |---|-------|---------------|
> | 1 | Assume $A[v]_B = \lambda[v]_B$ | hypothesis |
> | 2 | $[Tv]_B = \lambda[v]_B = [\lambda v]_B$ | row 1; $A = [T]_B$ gives $[Tv]_B = A[v]_B$ |
> | 3 | $Tv = \lambda v$ | row 2: coordinate map is injective |
> | 4 | $v$ is an eigenvector of $T$ with eigenvalue $\lambda$ | row 3; $v \neq 0$ (since $[v]_B \neq 0$) |

---

> [!abstract] הגדרה 3.4 — לכסינות מטריצה
> מטריצה $A \in M_n(F)$ נקראת **לכסינה** אם היא דומה למטריצה אלכסונית, כלומר קיימת $P \in M_n(F)$ הפיכה כך ש-$P^{-1}AP$ אלכסונית.

> [!abstract] משפט 3.5 — לכסינות דרך עמודות הפיכה
> $A$ לכסינה אם ורק אם קיימת $P$ הפיכה כך ש-$P^{-1}AP = \mathrm{diag}(\lambda_1, \ldots, \lambda_n)$. במקרה זה, עמודות $P$ הן ו״ע של $A$ עם ע״ע $\lambda_1, \ldots, \lambda_n$ (בהתאמה).

> [!note]- הוכחה
> נסמן את עמודות $P$ כ-$p_1, \ldots, p_n$. אזי $AP = PD$ (כאשר $D = \mathrm{diag}(\lambda_1,\ldots,\lambda_n)$) שקול לכך ש-$Ap_i = \lambda_i p_i$ לכל $i$. מאחר ש-$P$ הפיכה, עמודותיה שונות מאפס, ולכן הן אכן ו״ע. $\blacksquare$

> [!proof]+ Natural Deduction — Proof 1
>
> | # | Claim | Justification |
> |---|-------|---------------|
> | 1 | Let $p_1, \ldots, p_n$ denote the columns of $P$ | notation |
> | 2.0 | $AP =$ | &emsp;&emsp;<small>(expand column-wise)</small> |
> | 2.1 | &emsp;$= (Ap_1 \mid Ap_2 \mid \cdots \mid Ap_n)$ | column-by-column matrix multiplication |
> | 3.0 | $PD =$ | &emsp;&emsp;<small>(where $D = \mathrm{diag}(\lambda_1,\ldots,\lambda_n)$)</small> |
> | 3.1 | &emsp;$= (\lambda_1 p_1 \mid \lambda_2 p_2 \mid \cdots \mid \lambda_n p_n)$ | $D$ scales each column by the corresponding eigenvalue |
> | 4 | $P^{-1}AP = D \iff AP = PD$ | multiply by $P$ on the right ($P$ invertible) |
> | 5 | $AP = PD \iff Ap_i = \lambda_i p_i$ for all $i$ | rows 2.0–3.1: column-wise equality |
> | 6 | $p_i \neq 0$ for all $i$ | $P$ is invertible, so its columns are linearly independent, hence non-zero |
> | 7 | $p_1, \ldots, p_n$ are eigenvectors of $A$ with eigenvalues $\lambda_1, \ldots, \lambda_n$ | rows 5–6 |

> [!abstract] מסקנה 3.6 — שקילות לכסינות מטריצה והעתקה
> $A$ לכסינה (כמטריצה) אם ורק אם $T_A : F^n \to F^n$ (כפל ב-$A$) לכסינה (כהעתקה לינארית).

---

> [!example] דוגמה 3.7 — לכסון מטריצה $2 \times 2$
> תהי
> $$A = \begin{pmatrix} -7 & 8 \\ -6 & 7 \end{pmatrix}.$$
> נחפש ע״ע: $Av = \lambda v \Rightarrow (A - \lambda I)v = 0$, יש פתרון לא טריוויאלי אם ורק אם $\det(A - \lambda I) = 0$:
> $$\det \begin{pmatrix} -7-\lambda & 8 \\ -6 & 7-\lambda \end{pmatrix} = (-7-\lambda)(7-\lambda) + 48 = \lambda^2 - 1 = 0.$$
> לכן $\lambda = \pm 1$.
>
> עבור $\lambda = 1$: $(A - I)v = 0 \Rightarrow v_1 = (1, 1)^t$.
> עבור $\lambda = -1$: $(A + I)v = 0 \Rightarrow v_2 = (4, 3)^t$.
>
> לכן $P = \begin{pmatrix} 1 & 4 \\ 1 & 3 \end{pmatrix}$ ומתקיים $P^{-1}AP = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$. שימו לב: $A^2 = P \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} P^{-1} = I$.

---

> [!abstract] משפט 3.8 — מציאת ע״ע דרך דטרמיננטה
> $\lambda \in F$ הוא ע״ע של $A \in M_n(F)$ אם ורק אם $\det(A - \lambda I) = 0$.

> [!note]- הוכחה
> $\lambda$ ע״ע $\iff$ קיים $v \neq 0$ עם $Av = \lambda v \iff \ker(A - \lambda I) \neq \{0\} \iff A - \lambda I$ לא הפיכה $\iff \det(A - \lambda I) = 0$. $\blacksquare$

> [!proof]+ Natural Deduction — Proof 1
>
> | # | Claim | Justification |
> |---|-------|---------------|
> | 1.0 | $\lambda$ is an eigenvalue of $A \iff$ | &emsp;&emsp;<small>(unfold definition step by step)</small> |
> | 1.1 | &emsp;$\iff \exists\, 0 \neq v \in F^n : Av = \lambda v$ | definition of eigenvalue (Definition 3.1) |
> | 1.2 | &emsp;$\iff \exists\, 0 \neq v \in F^n : (A - \lambda I)v = 0$ | $Av = \lambda v \iff Av - \lambda Iv = 0 \iff (A-\lambda I)v = 0$ |
> | 1.3 | &emsp;$\iff \ker(A - \lambda I) \neq \{0\}$ | definition of kernel |
> | 1.4 | &emsp;$\iff A - \lambda I$ is not invertible | a matrix is invertible iff its kernel is trivial |
> | 1.5 | &emsp;$\iff \det(A - \lambda I) = 0$ | a matrix is invertible iff its determinant is non-zero |

---

> [!abstract] הגדרה 3.9 — הפולינום האופייני של מטריצה
> **הפולינום האופייני** של $A \in M_n(F)$ מוגדר כ:
> $$f_A(x) = \det(xI - A) \in F[x].$$

> [!note] הערה (ניסוח שקול למשפט 3.8)
> ניתן לנסח את משפט 3.8 גם כך: $\lambda$ הוא ע״ע של $A$ אם ורק אם $\lambda$ הוא שורש של $f_A$.

> [!example] דוגמה 3.10 — פולינום אופייני של מטריצה מדוגמה 3.7
> עבור המטריצה $A = \begin{pmatrix} -7 & 8 \\ -6 & 7 \end{pmatrix}$ (מדוגמה 3.7), הפולינום האופייני הוא:
> $$f_A(x) = x^2 - 1.$$

> [!abstract] משפט 3.11 — מבנה הפולינום האופייני
> $f_A(x)$ הוא פולינום **מתוקן** (מוניק) ממעלה $n$, עם:
> $$f_A(x) = x^n - \mathrm{tr}(A)\, x^{n-1} + \cdots + (-1)^n \det(A).$$
> בפרט, המקדם של $x^{n-1}$ הוא $-\mathrm{tr}(A)$ והאיבר החופשי הוא $(-1)^n \det(A)$.

> [!note]- הוכחה (מקדמים קיצוניים)
> $\det(xI - A) = \prod_i (x - a_{ii}) + \text{(איברים ממעלה} \le n-2\text{)}$. הגורם הדומיננטי הוא מכפלת האיברים האלכסוניים: $\prod_{i=1}^n (x - a_{ii})$, שנותן מקדם $x^n$ שווה $1$ (מתוקן) ומקדם $x^{n-1}$ שווה $-\sum_i a_{ii} = -\mathrm{tr}(A)$. האיבר החופשי הוא $f_A(0) = \det(-A) = (-1)^n \det(A)$. $\blacksquare$

> [!proof]+ Natural Deduction — Proof 1
>
> | # | Claim | Justification |
> |---|-------|---------------|
> | 1 | $f_A(x) = \det(xI - A) = \displaystyle\sum_\sigma \mathrm{sgn}(\sigma)\prod_{i=1}^n (xI-A)_{i,\sigma(i)}$ | Leibniz formula for determinants |
> | 2 | $(xI - A)_{ij} = x\delta_{ij} - a_{ij}$, so each entry is linear (or constant) in $x$ | definition of $xI - A$ |
> | 3 | The identity permutation $\sigma = \mathrm{id}$ contributes $\displaystyle\prod_{i=1}^n (x - a_{ii})$, which has degree $n$ | row 2: each diagonal entry $x - a_{ii}$ is degree 1 |
> | 4 | Every other permutation $\sigma \neq \mathrm{id}$ contributes a term of degree $\leq n-2$ | row 2: any non-identity $\sigma$ forces $\geq 2$ off-diagonal entries $(xI-A)_{i,\sigma(i)} = -a_{i,\sigma(i)}$ (constants), reducing degree by $\geq 2$ |
> | 5 | The leading coefficient of $f_A(x)$ is $1$ (monic) | row 3: $\prod(x - a_{ii})$ has leading coefficient $1$ |
> | 6 | The coefficient of $x^{n-1}$ in $f_A(x)$ is $-\displaystyle\sum_{i=1}^n a_{ii} = -\mathrm{tr}(A)$ | rows 3–4: only row 3 contributes to $x^{n-1}$; expanding $\prod(x-a_{ii})$ gives $-(\sum a_{ii})x^{n-1}$ |
> | 7 | $f_A(0) = \det(0 \cdot I - A) = \det(-A) = (-1)^n \det(A)$ | substitute $x=0$; $\det(-A) = (-1)^n \det(A)$ (factor $-1$ from each row) |
> | 8 | The constant term of $f_A$ is $(-1)^n \det(A)$ | row 7 |

> [!example] דוגמה 3.12 — חישוב פולינום אופייני
>
> **מטריצה $2 \times 2$ כללית:** $A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$:
> $$f_A(x) = x^2 - (a+d)x + (ad-bc) = x^2 - \mathrm{tr}(A)\, x + \det(A).$$
>
> **מטריצה אלכסונית:** $A = \mathrm{diag}(\lambda_1, \ldots, \lambda_n)$:
> $$f_A(x) = \prod_{i=1}^n (x - \lambda_i).$$
>
> **מטריצה משולשית עליונה:** $A = \begin{pmatrix} \lambda_1 & * \\ 0 & \lambda_2 \end{pmatrix}$ (כלל לגודל כלשהו):
> $$f_A(x) = \prod_{i=1}^n (x - a_{ii}).$$
> (הדטרמיננטה של מטריצה משולשית היא מכפלת האלכסון.)
>
> **מטריצת בלוקים:** $A = \begin{pmatrix} B & * \\ 0 & C \end{pmatrix}$:
> $$f_A(x) = f_B(x) \cdot f_C(x).$$

---

[[02-tirgul|דוגמאות מהתרגול →]]  |  [[03-exercises|תרגילים →]]
