---
title: "פרק 9 — הפולינום המינימלי: הרצאה"
chapter: ch09-minimal-poly
source: lecture-yehuda
status: lecture-done
tags: [la2, lecture, ch09-minimal-poly]
---

# הפולינום המינימלי — הרצאה

> [!info] מקור
> פרק 9 מתוך הרצאות יהודה שלום (שיעורים 7–8), עמ' 29–35.

---

## משפט 9.1 + הגדרה — הפולינום המינימלי

> [!abstract] משפט ו-הגדרה 9.1
> תהי $A \in M_n(F)$. נביט בקבוצה:
> $$I_A = \{p \in F[x] \mid p(A) = 0\}.$$
> אזי $I_A$ הוא **אידיאל** ב-$F[x]$, וקיים בו **איבר יחיד מתוקן בעל דרגה מינימלית**. הוא נקרא **הפולינום המינימלי** $m_A$ של $A$.

> [!note]- הוכחה
> $0 \in I_A$, סגירות תחת חיבור ותחת כפל בפולינום מ-$F[x]$ ברורות — לכן $I_A$ אידיאל. מכיוון $F[x]$ תחום ראשי, $I_A = \langle m_A \rangle$ עבור יוצר מתוקן $m_A$. היחידות: יוצרי אידיאל ראשי הם חברים; בפולינומים מתוקנים — זהים. $\square$

> [!proof]+ Natural Deduction — Proof 1 (Theorem 9.1)
> | # | Claim | Justification |
> |---|-------|---------------|
> | 1 | $I_A = \{p\in F[x]\mid p(A)=0\}$ | Definition |
> | 2 | $0\in I_A$; $I_A$ closed under addition and $F[x]$-multiplication | Polynomial substitution linearity |
> | 3 | $I_A$ is an ideal of $F[x]$ | Step 2 |
> | 4 | $F[x]$ is a PID (Theorem 7.26) | $\Rightarrow$ $I_A = \langle m_A\rangle$ for some monic $m_A$ |
> | 5 | $m_A$ has minimal degree among elements of $I_A$ | Generator of a principal ideal |
> | 6 | Any two monic generators of $I_A$ are associates and equal (monic) | Units of $F[x]$ are non-zero constants; monic associates are equal |
> | 7 | $m_A$ is the unique monic polynomial of minimal degree with $m_A(A)=0$ $\square$ | Steps 5, 6 |

> [!note] הערה 9.2
> אותה הגדרה והוכחה תופסת לט"ל $T : V \to V$: הפולינום המינימלי $m_T$ הוא הפולינום המתוקן בעל הדרגה המינימלית שמאפס את $T$.

> [!note] הערה 9.3 (התכונה הבסיסית)
> $m_A$ מחלק כל $p(x)$ עם $p(A) = 0$, כיוון ש-$I_A$ נוצר על ידי $m_A$.

---

## דוגמאות

> [!example] דוגמה 9.4 — טרנספורמציית הגזירה
> $V = \mathbb{R}_n[t]$, $T = \frac{d}{dt}$. ידוע $f_T(x) = x^{n+1}$. נטען $m_T = x^{n+1}$.
>
> אכן $T^{n+1} = 0$ לכן $m_T \mid x^{n+1}$, כלומר $m_T = x^k$ עבור $k \le n+1$. אבל $T^k(t^n) = \frac{n!}{(n-k)!}t^{n-k} \ne 0$ לכל $k < n+1$. לכן $m_T = x^{n+1}$.

> [!note] הערה 9.5
> לא תמיד $f_A = m_A$! (כן תמיד $m_A \mid f_A$.)

> [!example] דוגמה 9.6
> $A = I$ (מטריצת היחידה). $f_A(x) = (x-1)^n$, אבל $m_A(x) = x - 1$ כי $A - I = 0$.

---

## קשרים בין $m_A$ לשאר

> [!abstract] משפט 9.7
> תהי $A = A_f$ המטריצה המצורפת לפולינום $f(x) \in F[x]$. אזי $m_{A_f}(x) = f(x)$.

(הוכח בתרגיל בית 3.)

> [!abstract] משפט 9.8
> אם $A$ מטריצה מייצגת של $T : V \to V$ (ביחס לבסיס כלשהו), אזי $m_T = m_A$.

> [!note]- הוכחה
> לכל $p \in F[x]$ ובסיס $B$: $[p(T)]_B = p([T]_B)$. אגף ימין מתאפס אם ורק אם אגף שמאל מתאפס, לכן $I_A = I_T$ ויוצריהם שווים. $\square$

> [!proof]+ Natural Deduction — Proof 1 (Theorem 9.8)
> | # | Claim | Justification |
> |---|-------|---------------|
> | 1 | $A = [T]_B$ for some basis $B$ | Given |
> | 2 | $[p(T)]_B = p([T]_B) = p(A)$ for all $p\in F[x]$ | Claim 6.5 |
> | 3 | $p(T) = 0 \iff p(A) = 0$ | Step 2: matrix is zero iff map is zero |
> | 4 | $I_T = I_A$ as subsets of $F[x]$ | Step 3 |
> | 5 | $m_T = m_A$ (both are the monic minimal generator of the same ideal) $\square$ | Step 4 + uniqueness (Thm 9.1) |

> [!abstract] מסקנה 9.9
> $A, C$ דומות $\implies$ $m_A = m_C$.

> [!abstract] מסקנה 9.10
> נניח $A$ לכסינה עם ע"ע שונים $\lambda_1, \ldots, \lambda_k$. אזי:
> $$m_A(x) = \prod_{i=1}^k (x - \lambda_i).$$

> [!note]- הוכחה
> ניתן להניח $A$ אלכסונית (ממסקנה 9.9). מצד אחד, $m(A) = 0$ לכל $m = \prod(x-\lambda_i)$ (כפל של מטריצות אלכסוניות, כל איבר אלכסון מתאפס באחד הגורמים). מצד שני, הורדת גורם אחד משאירה איבר אלכסון שלא מתאפס בשום גורם — $m(A) \ne 0$. $\square$

> [!proof]+ Natural Deduction — Proof 1 (Corollary 9.10)
> | # | Claim | Justification |
> |---|-------|---------------|
> | 1 | $A$ is diagonalizable with distinct eigenvalues $\lambda_1,\ldots,\lambda_k$ | Given |
> | 2 | WLOG $A = \mathrm{diag}(\lambda_1,\ldots,\lambda_n)$ (some eigenvalues repeated) | Corollary 9.9: similar matrices share $m_A$ |
> | 3 | $\prod_{i=1}^k(A-\lambda_i I) = 0$: each diagonal entry $(a_{jj}-\lambda_1)\cdots(a_{jj}-\lambda_k) = 0$ since $a_{jj}$ is some $\lambda_i$ | Step 2, diagonal matrix computation |
> | 4 | $m = \prod_{i=1}^k(x-\lambda_i)$ satisfies $m(A)=0$, so $m_A\mid m$ | Step 3 + Theorem 9.1 |
> | 5 | For each $j$: omitting factor $(x-\lambda_j)$ leaves $\lambda_j$-diagonal entry non-zero | $\lambda_j\ne\lambda_i$ for $i\ne j$ |
> | 6 | $\prod_{i\ne j}(A-\lambda_i I)\ne 0$ for all $j$, so $m_A\nmid \prod_{i\ne j}(x-\lambda_i)$ | Step 5 |
> | 7 | $m_A = \prod_{i=1}^k(x-\lambda_i)$ $\square$ | Steps 4, 6: $m_A\mid m$ and no proper divisor annihilates $A$ |

---

## הפולינום המינימלי וע"ע

> [!abstract] משפט 9.15
> $\lambda$ ע"ע של $T$ $\implies$ $m_T(\lambda) = 0$.

> [!note]- הוכחה
> כלל: אם $p(T) = 0$ ו-$\lambda$ ע"ע עם ו"ע $v \ne 0$: $p(T)v = p(\lambda)v$, ומכיוון $p(T) = 0$: $0 = p(\lambda)v$, ו-$v \ne 0$ לכן $p(\lambda) = 0$. קח $p = m_T$. $\square$

> [!proof]+ Natural Deduction — Proof 1 (Theorem 9.15)
> | # | Claim | Justification |
> |---|-------|---------------|
> | 1 | $\lambda$ is an eigenvalue of $T$; $\exists v\ne 0$ with $Tv=\lambda v$ | Given |
> | 2 | $p(T)v = p(\lambda)v$ for all $p\in F[x]$ | Substitution: $T^k v = \lambda^k v$, then linearity |
> | 3 | $m_T(T) = 0$, so $m_T(T)v = 0$ | Definition of $m_T$ |
> | 4 | $m_T(\lambda)v = 0$ | Steps 2, 3 |
> | 5 | $m_T(\lambda) = 0$ $\square$ | Step 4: $v\ne 0$ |

> [!note] הערה 9.16
> לא השתמשנו במינימליות $m_T$ — הטענה נכונה לכל $p$ עם $p(T) = 0$.

> [!abstract] משפט 9.17
> $$\lambda \text{ ע"ע של } T \iff m_T(\lambda) = 0.$$

> [!note]- הוכחה
> הכיוון $\Leftarrow$ הוכח. לכיוון $\Rightarrow$:
>
> **הוכחה 1:** $m_T(\lambda) = 0 \implies (x - \lambda) \mid m_T(x)$. מלמת המחלק (ראה להלן), $T - \lambda I$ אינה הפיכה, כלומר $\lambda$ ע"ע.
>
> **הוכחה 2 (קיילי-המילטון):** $m_T(\lambda) = 0$, ומכיוון $m_T \mid f_T$, גם $f_T(\lambda) = 0$, כלומר $\lambda$ ע"ע. $\square$

> [!proof]+ Natural Deduction — Proof 1 (Theorem 9.17, ⟸ direction, Proof 1)
> | # | Claim | Justification |
> |---|-------|---------------|
> | 1 | $m_T(\lambda) = 0$ | Given |
> | 2 | $(x-\lambda)\mid m_T(x)$ | Step 1: root → linear factor |
> | 3 | $T-\lambda I = (x-\lambda)|_{x=T}(T)$ is not invertible | Step 2, Lemma 9.13 |
> | 4 | $\lambda$ is an eigenvalue of $T$ $\square$ | Step 3: $\ker(T-\lambda I)\ne\{0\}$ |

> [!proof]+ Natural Deduction — Proof 2 (Theorem 9.17, ⟸ direction, Proof 2)
> | # | Claim | Justification |
> |---|-------|---------------|
> | 1 | $m_T(\lambda) = 0$ | Given |
> | 2 | $m_T\mid f_T$ | Cayley-Hamilton: $m_T$ generates $I_T$ which contains $f_T$ |
> | 3 | $f_T(\lambda) = 0$ | Steps 1, 2 |
> | 4 | $\lambda$ is an eigenvalue of $T$ $\square$ | Step 3: roots of $f_T$ are eigenvalues (Thm 4.4) |

---

## למת המחלק

> [!abstract] למה 9.13 (למת המחלק בפולינום המינימלי)
> אם $f(x) \mid m_T(x)$ ו-$\deg(f) > 0$, אזי $f(T)$ אינה הפיכה.

> [!note]- הוכחה
> $m_T(x) = f(x) \cdot g(x)$, לכן $f(T) \cdot g(T) = m_T(T) = 0$. אם $f(T)$ הפיכה, נכפיל ב-$f(T)^{-1}$ ונקבל $g(T) = 0$. אבל $\deg(g) < \deg(m_T)$ — סתירה למינימליות. $\square$

> [!proof]+ Natural Deduction — Proof 1 (Lemma 9.13)
> | # | Claim | Justification |
> |---|-------|---------------|
> | 1 | $f\mid m_T$, $\deg f > 0$: $m_T = fg$ | Given |
> | 2 | $f(T)\cdot g(T) = m_T(T) = 0$ | Step 1 + definition of $m_T$ |
> | 3 | Suppose $f(T)$ is invertible | For contradiction |
> | 4 | $g(T) = f(T)^{-1}\cdot 0 = 0$ | Steps 2, 3 |
> | 5 | $\deg g = \deg m_T - \deg f < \deg m_T$ | Step 1, $\deg f > 0$ |
> | 6 | $g\in I_T$ with $\deg g < \deg m_T$: contradiction to minimality | Steps 4, 5 |
> | 7 | $f(T)$ is not invertible $\square$ | Steps 3–6 by contradiction |

---

## חסמים על $m_A$

> [!abstract] הערה 9.12
> הפולינום המינימלי אינו משתנה בהרחבת שדה: $A \in M_n(F) \subseteq M_n(K)$ נותן את אותו $m_A$.

> [!abstract] משפט 9.18
> תהי $A \in M_n(F)$. מתקיים:
> $$m_A(x) \mid f_A(x) \mid (m_A(x))^n.$$

> [!note]- הוכחה
> החלוקה $m_A \mid f_A$ ידועה (קיילי-המילטון). לחלוקה $f_A \mid m_A^n$: מעל הרחבה $K$ שבה כל ע"ע קיים, נכתוב $f_A = \prod_i (x-\lambda_i)^{n_i}$ ו-$m_A = \prod_i (x-\lambda_i)^{m_i}$ עם $1 \le m_i \le n_i \le n$. אז $m_A^n = \prod_i (x-\lambda_i)^{n \cdot m_i}$ ו-$n_i \le n \le n \cdot m_i$, לכן $f_A \mid m_A^n$ מעל $K$. מיחידות החלוקה עם שארית, מעל $F$ גם כן. $\square$

> [!proof]+ Natural Deduction — Proof 1 (Theorem 9.18)
> | # | Claim | Justification |
> |---|-------|---------------|
> | 1 | $m_A\mid f_A$ | Cayley-Hamilton: $f_A(A)=0$, so $f_A\in I_A = \langle m_A\rangle$ |
> | 2 | $\exists$ field extension $F\subseteq K$ over which $f_A$ and $m_A$ split | Algebraic closure |
> | 3 | Eigenvalues of $A$ over $K$: $f_A = \prod(x-\lambda_i)^{n_i}$, $m_A = \prod(x-\lambda_i)^{m_i}$ | Step 2; $1\le m_i$ (Thm 9.17), $m_i\le n_i$ |
> | 4 | $m_A^n = \prod(x-\lambda_i)^{n\cdot m_i}$; $n_i\le n\le n\cdot m_i$ | Step 3 |
> | 5 | $f_A\mid m_A^n$ over $K$ | Step 4 |
> | 6 | $f_A\mid m_A^n$ over $F$ $\square$ | Step 5 + Corollary 7.5(3): divisibility transfers from $K$ to $F$ |

> [!abstract] מסקנה 9.19
> אותו משפט נכון לט"ל $T : V \to V$ עם $\dim(V) = n$.

> [!abstract] מסקנה 9.21 (שימושית)
> אם $g(x)$ גורם אי-פריק של $f_A(x)$, אזי $g(x) \mid m_A(x)$.

> [!note]- הוכחה
> $g \mid m_A^n$, ו-$g$ אי-פריק (ולכן ראשוני), לכן $g \mid m_A$. $\square$

> [!proof]+ Natural Deduction — Proof 1 (Corollary 9.21)
> | # | Claim | Justification |
> |---|-------|---------------|
> | 1 | $g$ is an irreducible factor of $f_A$ | Given |
> | 2 | $g\mid f_A\mid m_A^n$ | Step 1 + Theorem 9.18 |
> | 3 | $g$ is irreducible in $F[x]$, hence prime (PID: Theorem 7.22) | $F[x]$ is a PID |
> | 4 | $g\mid m_A$ $\square$ | Steps 2, 3: prime divides a power → divides the base |

> [!example] דוגמה 9.20
> $A = I$: $m_A(x) = x-1$, $f_A(x) = (x-1)^n$. אכן $m_A \mid f_A \mid m_A^n$.

---

## $m_A$ של מטריצת בלוקים

> [!abstract] משפט 9.22
> נניח $A = \mathrm{diag}(A_1, \ldots, A_k)$ מטריצת בלוקים (בלוקים על האלכסון). אזי:
> $$m_A(x) = \mathrm{lcm}(m_{A_1}(x), \ldots, m_{A_k}(x)).$$

> [!note]- הוכחה
> לכל $g$: $g(A) = \mathrm{diag}(g(A_1), \ldots, g(A_k))$, ולכן $g(A) = 0 \iff g(A_i) = 0$ לכל $i$, כלומר $m_{A_i} \mid g$ לכל $i$. זה בדיוק $\mathrm{lcm}(m_{A_i}) \mid g$. $\square$

> [!proof]+ Natural Deduction — Proof 1 (Theorem 9.22)
> | # | Claim | Justification |
> |---|-------|---------------|
> | 1 | $A = \mathrm{diag}(A_1,\ldots,A_k)$ block diagonal | Given |
> | 2 | $g(A) = \mathrm{diag}(g(A_1),\ldots,g(A_k))$ for all $g\in F[x]$ | Polynomial of block diagonal = block diagonal of polynomial |
> | 3 | $g(A)=0 \iff g(A_i)=0$ for all $i$ | Step 2 |
> | 4 | $g(A)=0 \iff m_{A_i}\mid g$ for all $i$ | Step 3, definition of $m_{A_i}$ |
> | 5 | $g\in I_A \iff \mathrm{lcm}(m_{A_1},\ldots,m_{A_k})\mid g$ | Step 4 |
> | 6 | $m_A = \mathrm{lcm}(m_{A_1},\ldots,m_{A_k})$ $\square$ | Step 5: $m_A$ is the monic generator of $I_A$ |

---

## תת-מרחבים שמורים ופירוק ישר

> [!abstract] הגדרה 9.23 (תת-מרחב $T$-שמור)
> $W \subseteq V$ תמ"ו נקרא **$T$-שמור** אם $T(w) \in W$ לכל $w \in W$.

> [!abstract] משפט 9.24
> תהיינה $T, S : V \to V$ ט"ל מתחלפות ($T \circ S = S \circ T$). אזי:
> 1. $\mathrm{Im}(S),\ \ker(S)$ הם $T$-שמורים.
> 2. אם $W$ הוא $T$-שמור, אזי $S(W)$ הוא $T$-שמור.
> 3. אם $W_1, W_2$ הם $T$-שמורים, אז $W_1 + W_2$ ו-$W_1 \cap W_2$ הם $T$-שמורים.
> 4. אם $f(x) \in F[x]$ ו-$W$ הוא $T$-שמור, אזי $W$ הוא $f(T)$-שמור.

> (הוכחה: קל.)

---

## משפט 10.1 — פירוק ל-$\ker$ (הקדמה לצורת ז'ורדן)

> [!abstract] משפט 10.1 (חשוב!)
> יהי $V$ מ"ו מעל $F$, $T : V \to V$ ט"ל, ו-$f(x) \in F[x]$ עם $f(T) = 0$. נניח $f(x) = g(x) \cdot h(x)$ עם $\gcd(g, h) = 1$. אזי:
> $$V = \ker g(T) \oplus \ker h(T),$$
> כאשר שני תת-המרחבים הם $T$-שמורים.
>
> יתרה מזאת, אם $f = m_T$, אז $g, h$ הם הפולינומים המינימלים של $T$ על שני תת-המרחבים בהתאמה.

> [!note]- הוכחה
> **הפירוק לסכום:** מ-$\gcd(g,h)=1$ קיימים $a,b \in F[x]$ עם $ag + bh = 1$. נציב $T$:
> $$I = a(T)g(T) + b(T)h(T). \tag{1}$$
> לכל $v \in V$: $v = a(T)g(T)v + b(T)h(T)v$. נוכיח $a(T)g(T)v \in \ker h(T)$:
> $$h(T)(a(T)g(T)v) = a(T)g(T)h(T)v = a(T)f(T)v = 0.$$
> באופן דומה $b(T)h(T)v \in \ker g(T)$.
>
> **הסכום ישר:** אם $v \in \ker g(T) \cap \ker h(T)$, נציב ב-(1): $v = 0 + 0 = 0$.
>
> **פולינומים מינימלים בפירוק:** נסמן $W_1 = \ker g(T),\ W_2 = \ker h(T)$, ו-$T_1, T_2$ הצמצומים. מתקיים $m_{T_1} \mid g$, $m_{T_2} \mid h$. ומהנוסחה $m_T = \mathrm{lcm}(m_{T_1}, m_{T_2})$ ומ-$\deg m_T = \deg g + \deg h$, נובע $\deg g = \deg m_{T_1}$ ו-$\deg h = \deg m_{T_2}$, לכן $m_{T_1} = g$ ו-$m_{T_2} = h$. $\square$

> [!proof]+ Natural Deduction — Proof 1 (Theorem 10.1)
> | # | Claim | Justification |
> |---|-------|---------------|
> | 1 | $f(T)=0$; $f=gh$; $\gcd(g,h)=1$ | Given |
> | 2 | $\exists a,b\in F[x]$ with $ag+bh=1$ | Step 1, Bezout (Thm 7.25: PID) |
> | 3 | $I = a(T)g(T) + b(T)h(T)$ | Step 2 evaluated at $T$ |
> | 4 | For any $v\in V$: $a(T)g(T)v\in\ker h(T)$ | $h(T)(a(T)g(T)v) = a(T)f(T)v = 0$ (Step 1) |
> | 5 | Similarly $b(T)h(T)v\in\ker g(T)$ | Symmetric argument |
> | 6 | $v = a(T)g(T)v + b(T)h(T)v\in \ker h(T) + \ker g(T)$ | Steps 3, 4, 5 |
> | 7 | $V = \ker g(T) + \ker h(T)$ | Step 6 |
> | 8 | If $v\in \ker g(T)\cap\ker h(T)$: apply Step 3, get $v = 0+0 = 0$ | Steps 3, 4, 5 with $g(T)v = h(T)v = 0$ |
> | 9 | $V = \ker g(T)\oplus\ker h(T)$, both $T$-invariant | Steps 7, 8; $T$-invariance from Thm 9.24 |
> | 10 | If $f = m_T$: $m_{T_1}\mid g$, $m_{T_2}\mid h$, and degree count forces $m_{T_1}=g$, $m_{T_2}=h$ $\square$ | $\mathrm{lcm}(m_{T_1},m_{T_2})=m_T$, $\deg m_T = \deg g + \deg h$ |

---

[[02-tirgul|דוגמאות מהתרגול →]]  |  [[03-exercises|תרגילים →]]
