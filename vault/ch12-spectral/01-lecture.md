---
title: "פרק 12 — המשפט הספקטרלי: הרצאה"
chapter: ch12-spectral
source: lecture-yehuda
status: lecture-done
tags: [la2, lecture, ch12-spectral]
---

# המשפט הספקטרלי — הרצאה

> [!info] מקור
> פרקים 14–16 מתוך הרצאות יהודה שלום, עמ' 65–84.

---

## פרק 14 — טרנספורמציות סימטריות והמשפט הספקטרלי

### הגדרות

> [!abstract] הגדרה 14.1 — צמודה לעצמה
> יהי $V$ מ"פ, $T : V \to V$ ט"ל. $T$ נקראת:
> - **סימטרית** (כשש $F = \mathbb{R}$) או **הרמיטית** (כש $F = \mathbb{C}$) — או בכלליות **צמודה לעצמה** — אם לכל $v, u \in V$:
> $$\langle Tv, u \rangle = \langle v, Tu \rangle.$$

> [!example] דוגמה 14.2
> $V = \mathbb{R}^n$ עם מ"פ סטנדרטית, $A \in M_n(\mathbb{R})$ מגדירה $T_A(v) = Av$. אזי $T_A$ סימטרית אם ורק אם $A = A^t$. (שכן $\langle T_A v, u \rangle = v^t A^t u$ ו-$\langle v, T_A u \rangle = v^t Au$.)

> [!abstract] משפט 14.3 — תכונות
> אם $T, S : V \to V$ צמודות לעצמן, אזי:
> 1. $T + S$ ו-$a \cdot T$ (עבור $a \in \mathbb{R}$) צמודות לעצמן.
> 2. $TS$ צמודה לעצמה אם ורק אם $TS = ST$.
> 3. $p(T)$ לכל $p(x) \in \mathbb{R}[x]$.

> [!abstract] הגדרה 14.4 — חיוביות
> $T : V \to V$ נקראת **חיובית** / **אי-שלילית** אם $\langle Tv, v \rangle > 0$ / $\langle Tv, v \rangle \ge 0$ לכל $0 \ne v \in V$.

> [!abstract] הערה 14.5
> אם $T$ חיובית אז $T$ הפיכה (שאם $Tv = 0$ אז $\langle Tv, v \rangle = 0$ — סתירה לחיוביות).

> [!abstract] טענה 14.6
> אם $S$ צמודה לעצמה אז $S^2$ צמודה לעצמה ואי-שלילית:
> $$\langle S^2 v, v \rangle = \langle Sv, Sv \rangle = \|Sv\|^2 \ge 0.$$

> [!abstract] מסקנה 14.7
> אם $p(x) \in \mathbb{R}[x]$ פולינום חיובי (כלומר $p(x) > 0$ לכל $x \in \mathbb{R}$) ו-$T$ צמודה לעצמה, אז $p(T)$ חיובית.

> [!note]- הוכחה
> מתרגיל בית ידוע שקיימים $g_1, \ldots, g_k$ ו-$c > 0$ כך ש-$p(x) = \sum g_i^2(x) + c$. אז $p(T) = \sum S_i^2 + cI$ כאשר $S_i = g_i(T)$. מטענה 14.6: $\langle p(T) v, v \rangle = \sum \|S_i v\|^2 + c\|v\|^2 \ge c\|v\|^2 > 0$. $\square$

> [!proof]+ Natural Deduction — Proof 1 (Corollary 14.7)
> | # | Claim | Justification |
> |---|-------|---------------|
> | 1 | $p(x) > 0$ for all $x \in \mathbb{R}$; $T$ self-adjoint | Given |
> | 2 | $p(x) = \sum_i g_i^2(x) + c$ with $c > 0$ (positive polynomial over $\mathbb{R}$) | HW result: sum-of-squares + positive constant |
> | 3 | $p(T) = \sum_i S_i^2 + cI$ where $S_i = g_i(T)$ | Polynomial evaluation is a ring homomorphism |
> | 4 | Each $S_i = g_i(T)$ is self-adjoint (polynomial in self-adjoint $T$) | Theorem 14.3 |
> | 5 | $\langle S_i^2 v, v\rangle = \|S_i v\|^2 \ge 0$ for all $v$ | Claim 14.6 |
> | 6 | $\langle p(T)v, v\rangle = \sum \|S_i v\|^2 + c\|v\|^2 \ge c\|v\|^2 > 0$ for $v \ne 0$ | Steps 3–5, $c>0$ $\square$ |

> [!abstract] מסקנה 14.8
> אם $T$ צמודה לעצמה ו-$p(x) \in \mathbb{R}[x]$ פולינום חיובי, אז $p(T)$ הפיכה.

---

### המשפט הספקטרלי — מקרה ממשי

> [!abstract] משפט 14.9
> אם $T : V \to V$ סימטרית ($F = \mathbb{R}$) אז $m_T(x)$ מתפרק למכפלת גורמים לינאריים מעל $\mathbb{R}$ (כל ע"ע של $T$ ממשי).

> [!note]- הוכחה
> נניח בשלילה כי גורם אי-פריק $p_1$ של $m_T$ מקיים $\deg p_1 \ge 2$. מכיוון ש-$p_1$ אי-פריק (לכן מתוקן) הוא חיובי, ולכן $p_1(T)$ הפיך. אבל $m_T(T) = p_1(T) \cdot g(T) = 0$ ולכן $g(T) = 0$, בסתירה למינימליות. $\square$

> [!proof]+ Natural Deduction — Proof 1 (Theorem 14.9)
> | # | Claim | Justification |
> |---|-------|---------------|
> | 1 | $T$ symmetric, $m_T = p_1 \cdots p_r$ irreducible factorization over $\mathbb{R}$ | Given |
> | 2 | Assume for contradiction: some $p_1$ irreducible with $\deg p_1 \ge 2$ | Assumption |
> | 3 | $p_1$ is monic and positive on $\mathbb{R}$ (irreducible quadratic over $\mathbb{R}$ has no real root, so $> 0$ everywhere) | Irreducible over $\mathbb{R}$ with $\deg \ge 2$ |
> | 4 | $p_1(T)$ is invertible | Corollary 14.8 (positive polynomial of self-adjoint T) |
> | 5 | $m_T(T) = p_1(T) \cdot g(T) = 0$ where $g = m_T/p_1$ | $m_T(T) = 0$ |
> | 6 | Since $p_1(T)$ invertible: $g(T) = 0$ | Step 4, multiply by $(p_1(T))^{-1}$ |
> | 7 | Contradiction: $g$ has degree $< \deg m_T$ and annihilates $T$ | Minimality of $m_T$ $\square$ |

> [!abstract] למה 14.11
> אם $T$ סימטרית ו-$\lambda \in \mathbb{R}$: אם $(T - \lambda I)^2 v = 0$ אז $(T - \lambda I) v = 0$.

> [!note]- הוכחה
> $S = T - \lambda I$ גם צמודה לעצמה. אם $S^2 v = 0$ אז $0 = \langle S^2 v, v \rangle = \|Sv\|^2$, ולכן $Sv = 0$. $\square$

> [!proof]+ Natural Deduction — Proof 1 (Lemma 14.11)
> | # | Claim | Justification |
> |---|-------|---------------|
> | 1 | $T$ self-adjoint, $\lambda \in \mathbb{R}$; set $S = T - \lambda I$ | Given; $S$ self-adjoint since $\lambda \in \mathbb{R}$ |
> | 2 | Assume $S^2 v = 0$ | Hypothesis |
> | 3 | $0 = \langle S^2 v, v\rangle = \langle S v, S^* v\rangle = \langle Sv, Sv\rangle = \|Sv\|^2$ | $S^* = S$, inner product linearity |
> | 4 | $\|Sv\|^2 = 0 \implies Sv = 0$ | Definiteness of norm $\square$ |

> [!abstract] טענה 14.10
> כל הגורמים הלינאריים של $m_T$ (לטרנס' סימטרית $T$) שונים זה מזה. בפרט, $T$ לכסינה.

> [!note]- הוכחה
> נניח בשלילה $(x - \lambda)^2 \mid m_T(x)$. אזי $(T - \lambda I)^2 g(T) = 0$ לכל $v$. מלמה 14.11 עם $w = g(T)v$: $(T - \lambda I)w = 0$. ולכן $(x - \lambda)g(x)$ מאפס את $T$ בסתירה למינימליות. $\square$

> [!proof]+ Natural Deduction — Proof 1 (Claim 14.10)
> | # | Claim | Justification |
> |---|-------|---------------|
> | 1 | $T$ symmetric; $m_T$ splits over $\mathbb{R}$ into linear factors | Theorem 14.9 |
> | 2 | Assume for contradiction $(x-\lambda)^2 \mid m_T(x)$; write $m_T = (x-\lambda)^2 h(x)$ | Assumption |
> | 3 | $(T-\lambda I)^2 h(T) = m_T(T) = 0$, so for all $v$: $(T-\lambda I)^2 (h(T)v) = 0$ | $m_T(T) = 0$ |
> | 4 | By Lemma 14.11 with $w = h(T)v$: $(T-\lambda I)w = 0$ | Step 3, Lemma 14.11 |
> | 5 | So $(T-\lambda I)h(T) = 0$, meaning $(x-\lambda)h(x)$ annihilates $T$ | Step 4 for all $v$ |
> | 6 | $\deg((x-\lambda)h) = 1 + \deg h < \deg m_T$ — contradiction | Minimality of $m_T$ $\square$ |

> [!abstract] משפט 14.13 = 14.16 — המשפט הספקטרלי (F=R)
> תהי $T : V \to V$ סימטרית ($F = \mathbb{R}$). אזי קיים בסיס אורתונורמלי של $V$ המורכב מו"ע של $T$.

> [!note]- הוכחה
> הוכחנו ש-$T$ לכסינה. יהיו $\lambda_1, \ldots, \lambda_r$ הע"ע השונים ו-$V_{\lambda_i} = \ker(T - \lambda_i I)$. מלכסינות: $V = \bigoplus V_{\lambda_i}$.
>
> מטענה 14.14 (להלן): ו"ע ממ"ע שונים ניצבים זה לזה. לכן בכל $V_{\lambda_i}$ בנפרד מפעילים גרם-שמידט לקבלת $B_i$ א"נ. $B = \bigcup B_i$ הוא בסיס א"נ של $V$. $\square$

> [!proof]+ Natural Deduction — Proof 1 (Theorem 14.13/14.16 — Spectral, F=R)
> | # | Claim | Justification |
> |---|-------|---------------|
> | 1 | $T$ symmetric over $\mathbb{R}$ | Given |
> | 2 | $m_T$ splits into distinct linear factors | Theorems 14.9, 14.10 |
> | 3 | $T$ is diagonalizable; $V = \bigoplus_i V_{\lambda_i}$ (eigenspace decomposition) | Corollary 10.11 / Corollary 10.5 |
> | 4 | Eigenvectors from distinct eigenspaces are orthogonal | Claim 14.14 |
> | 5 | Apply Gram-Schmidt to each $V_{\lambda_i}$ independently to get $B_i$ ONB of $V_{\lambda_i}$ | Theorem 13.30 |
> | 6 | $B = \bigcup_i B_i$: vectors from different $B_i$ are orthogonal (step 4), within $B_i$ also ON (step 5) | Steps 4–5 |
> | 7 | $B$ is an ONB of $V$ consisting of eigenvectors of $T$ | Steps 3, 6 $\square$ |

> [!abstract] משפט 14.17 — הכיוון ההפוך
> אם ל-$T : V \to V$ קיים בסיס א"נ של ו"ע (כל $\lambda_i \in \mathbb{R}$), אז $T$ סימטרית.

> [!note]- הוכחה
> יהי $\{e_i\}$ בסיס א"נ, $Te_i = \lambda_i e_i$. לכל $v = \sum a_i e_i$, $u = \sum b_i e_i$: $\langle Tv, u \rangle = \sum \lambda_i a_i b_i = \langle v, Tu \rangle$. $\square$

> [!proof]+ Natural Deduction — Proof 1 (Theorem 14.17)
> | # | Claim | Justification |
> |---|-------|---------------|
> | 1 | $\{e_i\}$ ONB with $Te_i = \lambda_i e_i$, $\lambda_i \in \mathbb{R}$ | Given |
> | 2 | For $v = \sum a_i e_i$, $u = \sum b_i e_i$: $\langle Tv, u\rangle = \langle \sum a_i \lambda_i e_i, \sum b_j e_j\rangle$ | Linearity |
> | 3 | $= \sum_{i,j} a_i \lambda_i \overline{b_j} \langle e_i, e_j\rangle = \sum_i \lambda_i a_i \overline{b_i}$ | ONB: $\langle e_i, e_j\rangle = \delta_{ij}$ |
> | 4 | $\langle v, Tu\rangle = \langle \sum a_i e_i, \sum b_j \lambda_j e_j\rangle = \sum_i a_i \overline{b_i \lambda_i} = \sum_i \lambda_i a_i \overline{b_i}$ | $\lambda_i \in \mathbb{R}$ so $\overline{\lambda_i} = \lambda_i$ |
> | 5 | $\langle Tv,u\rangle = \langle v, Tu\rangle$ for all $v,u$ $\implies$ $T$ self-adjoint | Steps 3–4 $\square$ |

---

### ו"ע וניצביות

> [!abstract] טענה 14.14
> אם $T$ צמודה לעצמה ($F = \mathbb{R}$ או $\mathbb{C}$) ו-$Tv = \alpha v$, $Tu = \beta u$ עם $\alpha \ne \beta$, אזי $\langle v, u \rangle = 0$.

> [!note]- הוכחה
> $\alpha \langle v, u \rangle = \langle Tv, u \rangle = \langle v, Tu \rangle = \bar{\beta} \langle v, u \rangle$. אם $F = \mathbb{R}$: $\alpha \ne \beta$ ולכן $\langle v, u \rangle = 0$. אם $F = \mathbb{C}$: נשתמש בלמה 14.15. $\square$

> [!proof]+ Natural Deduction — Proof 1 (Claim 14.14)
> | # | Claim | Justification |
> |---|-------|---------------|
> | 1 | $T$ self-adjoint, $Tv = \alpha v$, $Tu = \beta u$, $\alpha \ne \beta$ | Given |
> | 2 | $\alpha\langle v,u\rangle = \langle \alpha v, u\rangle = \langle Tv, u\rangle$ | Linearity |
> | 3 | $= \langle v, Tu\rangle = \langle v, \beta u\rangle = \bar{\beta}\langle v,u\rangle$ | $T$ self-adjoint; sesquilinearity |
> | 4 | $(\alpha - \bar{\beta})\langle v,u\rangle = 0$ | Steps 2–3 |
> | 5 | Over $\mathbb{R}$: $\bar{\beta} = \beta$, so $(\alpha - \beta)\langle v,u\rangle = 0$; $\alpha \ne \beta$ gives $\langle v,u\rangle = 0$ | $\alpha,\beta \in \mathbb{R}$ for self-adjoint over $\mathbb{R}$ |
> | 6 | Over $\mathbb{C}$: eigenvalues are real (Lemma 14.15), so $\bar{\beta} = \beta$; same conclusion | Lemma 14.15 $\square$ |

> [!abstract] למה 14.15
> אם $T$ צמודה לעצמה אז כל ע"ע (אפילו מרוכב) ממשי.

> [!note]- הוכחה
> $Tu = \beta u \implies \beta \|u\|^2 = \langle Tu, u \rangle = \langle u, Tu \rangle = \bar{\beta} \|u\|^2 \implies \beta = \bar{\beta}$. $\square$

> [!proof]+ Natural Deduction — Proof 1 (Lemma 14.15)
> | # | Claim | Justification |
> |---|-------|---------------|
> | 1 | $T$ self-adjoint, $Tu = \beta u$, $u \ne 0$ | Given |
> | 2 | $\beta\|u\|^2 = \langle \beta u, u\rangle = \langle Tu, u\rangle$ | Linearity |
> | 3 | $= \langle u, Tu\rangle = \langle u, \beta u\rangle = \bar{\beta}\|u\|^2$ | $T$ self-adjoint; sesquilinearity |
> | 4 | $(\beta - \bar{\beta})\|u\|^2 = 0$; $\|u\|^2 > 0$ so $\beta = \bar{\beta}$ | $u \ne 0$; $\beta \in \mathbb{R}$ $\square$ |

---

### הגדרה: אנטי-סימטריות

> [!abstract] הגדרה 14.18
> $T$ **אנטי-סימטרית** אם $\langle Tv, u \rangle = -\langle v, Tu \rangle$ לכל $v, u$.

> [!abstract] הערה 14.19
> הע"ע הממשי היחיד של $T$ אנטי-סימטרית הוא $\lambda = 0$.

> [!abstract] טענה 14.21
> אם $T$ אנטי-סימטרית ($F = \mathbb{R}$) אז $T^2$ סימטרית ואי-חיובית:
> $$\langle T^2 v, v \rangle = -\langle Tv, Tv \rangle = -\|Tv\|^2 \le 0.$$

---

### המשפט הספקטרלי — מקרה מרוכב

> [!abstract] הגדרה 14.37 — נורמלית
> $T : V \to V$ **נורמלית** אם $TT^* = T^*T$.

> [!abstract] משפט 14.23/14.40 — המשפט הספקטרלי (F=C)
> אם $T : V \to V$ נורמלית (מעל $\mathbb{C}$) אזי קיים בסיס א"נ של ו"ע של $T$.

> [!note]- הוכחה (סקיצה)
> נגדיר $S_1 = \frac{T + T^*}{2}$, $S_2 = \frac{T - T^*}{2i}$ — שתיהן צמודות לעצמן ומתחלפות (מנורמליות $T$). ממשפט 14.41 קיים בסיס א"נ מלכסן ביחד את $S_1$ ו-$S_2$. מ-$T = S_1 + iS_2$ כל איבר הבסיס הוא ו"ע של $T$. $\square$

> [!proof]+ Natural Deduction — Proof 1 (Theorem 14.23/14.40 — Spectral, F=C, sketch)
> | # | Claim | Justification |
> |---|-------|---------------|
> | 1 | $T$ normal over $\mathbb{C}$: $TT^* = T^*T$ | Given |
> | 2 | Define $S_1 = (T+T^*)/2$, $S_2 = (T-T^*)/2i$; both self-adjoint | Compute $(S_j)^* = S_j$ directly |
> | 3 | $S_1 S_2 = S_2 S_1$: follows from $TT^* = T^*T$ | Algebraic manipulation using $TT^* = T^*T$ |
> | 4 | $T = S_1 + iS_2$ | By definition of $S_1, S_2$ |
> | 5 | By Claim 14.41: $\exists$ ONB $B$ simultaneously diagonalizing $S_1$ and $S_2$ | Commuting self-adjoint operators |
> | 6 | Each $b \in B$: $S_1 b = \lambda_1 b$, $S_2 b = \lambda_2 b$, so $Tb = (S_1+iS_2)b = (\lambda_1+i\lambda_2)b$ | Step 4 |
> | 7 | $B$ is an ONB of eigenvectors of $T$ | Steps 5–6 $\square$ |

> [!abstract] טענה 14.41
> אם $S_1^* = S_1$, $S_2^* = S_2$ ו-$S_1 S_2 = S_2 S_1$ — קיים בסיס א"נ מלכסן את שניהן יחד.

> [!note]- הוכחה
> מהמשפט הספקטרלי על $S_1$: $V = \bigoplus_\lambda \ker(S_1 - \lambda I)$, כאשר המ"ע ניצבים זה לזה. מהתחלפות, $S_2$ שומרת כל $\ker(S_1 - \lambda I)$. מהמשפט הספקטרלי לפעולת $S_2$ על כל מ"ע, קיים $B_\lambda$ א"נ של ו"ע. $B = \bigcup B_\lambda$ מספק. $\square$

> [!proof]+ Natural Deduction — Proof 1 (Claim 14.41)
> | # | Claim | Justification |
> |---|-------|---------------|
> | 1 | $S_1^* = S_1$, $S_2^* = S_2$, $S_1 S_2 = S_2 S_1$ | Given |
> | 2 | Spectral theorem on $S_1$: $V = \bigoplus_\lambda W_\lambda$ with $W_\lambda = \ker(S_1 - \lambda I)$ orthogonal | Theorem 14.13/14.16 applied to $S_1$ |
> | 3 | Each $W_\lambda$ is $S_2$-invariant: for $w \in W_\lambda$, $S_1(S_2 w) = S_2(S_1 w) = \lambda S_2 w$ | Commutativity step 1 |
> | 4 | $S_2|_{W_\lambda}$ is self-adjoint; apply spectral theorem on each $W_\lambda$ | Restriction of self-adjoint to invariant subspace |
> | 5 | Get ONB $B_\lambda$ of $W_\lambda$ from eigenvectors of $S_2|_{W_\lambda}$ | Step 4, Theorem 14.13 |
> | 6 | $B = \bigcup_\lambda B_\lambda$: each $b \in B_\lambda$ is eigenvector of both $S_1$ and $S_2$; across $\lambda$ orthogonal (step 2) | Steps 2, 5 $\square$ |

> [!abstract] מסקנה 14.35
> אם $T$ מקיימת את המשפט הספקטרלי, אז $TT^* = T^*T$ (כלומר $T$ נורמלית).

---

### תכונות נוספות של ט"ל נורמלית

> [!abstract] טענה 14.42
> אם $T$ נורמלית ו-$Tv = \lambda v$, אזי $T^* v = \bar{\lambda} v$ (כל ו"ע של $T$ הוא גם ו"ע של $T^*$).

> [!note]- הוכחה
> מספיק להוכיח שאם $S$ נורמלית ו-$Sv = 0$ אז $S^* v = 0$. אכן: $0 = \langle Sv, Sv \rangle = \langle v, S^*Sv \rangle = \langle v, SS^*v \rangle = \|S^*v\|^2$. $\square$

> [!proof]+ Natural Deduction — Proof 1 (Claim 14.42)
> | # | Claim | Justification |
> |---|-------|---------------|
> | 1 | $T$ normal, $Tv = \lambda v$; set $S = T - \lambda I$ | Given; $S$ is also normal |
> | 2 | $Sv = 0$; need to show $S^* v = 0$ | From $Tv = \lambda v$ |
> | 3 | $SS^* = S^*S$ (S normal since T normal and $\lambda I$ commutes with everything) | Normality |
> | 4 | $0 = \langle Sv, Sv\rangle = \langle v, S^*Sv\rangle = \langle v, SS^*v\rangle = \|S^*v\|^2$ | Step 2, normality |
> | 5 | $S^*v = 0$, i.e., $(T-\lambda I)^* v = (T^* - \bar\lambda I)v = 0$, so $T^*v = \bar\lambda v$ | Step 4 $\square$ |

> [!abstract] טענה 14.44
> אם $T$ נורמלית ו-$Tv = \alpha v$, $Tu = \beta u$ עם $\alpha \ne \beta$, אזי $v \perp u$.

---

## פרק 15 — מטריצות במ"פ

### הט"ל הצמודה

> [!abstract] משפט 14.25/14.26/14.29 — ט"ל הצמודה
> לכל ט"ל $T : V \to V$ קיימת **יחידה** ט"ל $T^* : V \to V$ המקיימת לכל $v, u \in V$:
> $$\langle Tv, u \rangle = \langle v, T^* u \rangle.$$

> [!note]- הוכחה (קיום)
> לכל $u$ קבוע, הפונקציה $\varphi(v) = \langle Tv, u \rangle$ היא פונקציונל לינארי. ממשפט ריס קיים $u^* \in V$ יחיד כך ש-$\varphi(v) = \langle v, u^* \rangle$. ההתאמה $u \mapsto u^*$ לינארית ומגדירה את $T^*$. $\square$

> [!proof]+ Natural Deduction — Proof 1 (Theorem 14.25/14.26/14.29 — Adjoint Exists)
> | # | Claim | Justification |
> |---|-------|---------------|
> | 1 | Fix $u \in V$; define $\varphi_u(v) = \langle Tv, u\rangle$ | For each $u$, this is a function of $v$ |
> | 2 | $\varphi_u$ is a linear functional: $\varphi_u(\alpha v + w) = \alpha\varphi_u(v) + \varphi_u(w)$ | Linearity of $T$ and inner product in first arg |
> | 3 | Riesz representation: $\exists!\ u^* \in V$ s.t. $\varphi_u(v) = \langle v, u^*\rangle$ for all $v$ | Theorem 14.25 (Riesz) |
> | 4 | Define $T^*(u) = u^*$; then $\langle Tv, u\rangle = \langle v, T^*u\rangle$ | Steps 1–3 |
> | 5 | $T^*$ is linear: $T^*(\alpha u + w) = \alpha T^*(u) + T^*(w)$ by uniqueness in Riesz | Step 3 uniqueness |
> | 6 | Uniqueness of $T^*$: if $T'$ also satisfies the adjoint identity, Riesz uniqueness gives $T'=T^*$ | Step 3 $\square$ |

> [!note] משפט ריס 14.25
> לכל פונקציונל לינארי $\varphi : V \to F$ קיים $u \in V$ יחיד כך ש-$\varphi(v) = \langle v, u \rangle$.

> [!abstract] טענה 14.30 — תכונות בסיסיות
> - $(T^*)^* = T$
> - $(aT)^* = \bar{a} T^*$
> - $(T + S)^* = T^* + S^*$
> - $(TS)^* = S^* T^*$

> [!abstract] דוגמה 14.31–14.32
> עבור $A \in M_n(\mathbb{C})$ ו-$T_A(v) = Av$ על $\mathbb{C}^n$ (מ"פ סטנדרטית): $(T_A)^* = T_{A^*}$ כאשר $A^* = \bar{A}^t$.

---

### קשר למטריצות מייצגות

> [!abstract] משפט 15.4
> אם $B$ בסיס א"נ של $V$ ו-$A = [T]_B$, אזי $[T^*]_B = A^*$.

> [!note]- הוכחה
> $a_{ij} = \langle Te_j, e_i \rangle$. עבור $C = [T^*]_B$: $c_{ij} = \langle T^* e_j, e_i \rangle = \langle e_j, Te_i \rangle = \overline{\langle Te_i, e_j \rangle} = \bar{a}_{ji}$. ולכן $C = A^*$. $\square$

> [!proof]+ Natural Deduction — Proof 1 (Theorem 15.4)
> | # | Claim | Justification |
> |---|-------|---------------|
> | 1 | $B = \{e_1,\ldots,e_n\}$ ONB, $A = [T]_B$, so $a_{ij} = \langle Te_j, e_i\rangle$ | ONB coordinate formula |
> | 2 | Let $C = [T^*]_B$; compute $c_{ij} = \langle T^* e_j, e_i\rangle$ | Definition of representing matrix |
> | 3 | $= \langle e_j, Te_i\rangle$ | Adjoint definition: $\langle T^*v,u\rangle = \langle v,Tu\rangle$ (swap roles) |
> | 4 | $= \overline{\langle Te_i, e_j\rangle} = \bar{a}_{ji}$ | Hermitian property of inner product |
> | 5 | $C = A^*$ (conjugate transpose) | Step 4 gives $c_{ij} = \bar{a}_{ji}$ for all $i,j$ $\square$ |

> [!abstract] מסקנה 15.5
> אם $B$ בסיס א"נ: $T$ צמודה לעצמה / נורמלית אם ורק אם $[T]_B$ כזו. (הגדרת: $A$ נורמלית אם $AA^* = A^*A$.)

> [!note] הערה חשובה
> המשפט נכון **רק** כשהבסיס הוא א"נ! בבסיס שאינו א"נ ייתכן ש-$T$ צמודה לעצמה אבל $[T]_B$ אינה.

---

### משפטים עיקריים על מטריצות נורמליות

> [!abstract] משפט 15.6
> אם $A \in M_n(F)$ נורמלית, קיים פולינום $f(x) \in \mathbb{R}[x]$ כך ש-$A^* = f(A)$.

> [!note]- הוכחה
> ממשפט הספקטרלי: $P^{-1}AP = D$ (אלכסונית, $P$ א"נ). ממשפט אינטרפולציה קיים $f \in \mathbb{R}[x]$ עם $f(\lambda_i) = \bar{\lambda}_i$. אז $f(D)$ = $D^*$ ולכן $P^{-1}f(A)P = f(D) = D^* = P^{-1}A^*P$, כלומר $f(A) = A^*$. $\square$

> [!abstract] מסקנה 15.13
> אם $T : V \to V$ נורמלית, קיים $f(x) \in \mathbb{R}[x]$ כך ש-$T^* = f(T)$.

> [!abstract] טענה 15.14
> אם $U \subseteq V$ תת-מרחב $T$-שמור, אז $U^\perp$ הוא $T^*$-שמור.

> [!note]- הוכחה
> יהי $w \in U^\perp$. לכל $u \in U$: $\langle T^* w, u \rangle = \langle w, Tu \rangle = 0$ (כי $Tu \in U$ ו-$w \perp U$). $\square$

> [!proof]+ Natural Deduction — Proof 1 (Claim 15.14)
> | # | Claim | Justification |
> |---|-------|---------------|
> | 1 | $U \subseteq V$ $T$-invariant: $T[U] \subseteq U$ | Given |
> | 2 | Let $w \in U^\perp$; want to show $T^*w \in U^\perp$ | Goal |
> | 3 | For any $u \in U$: $\langle T^*w, u\rangle = \langle w, Tu\rangle$ | Adjoint definition |
> | 4 | $Tu \in U$ (T-invariance); $w \perp U$ so $\langle w, Tu\rangle = 0$ | Steps 1, 2 |
> | 5 | $\langle T^*w, u\rangle = 0$ for all $u \in U$, so $T^*w \in U^\perp$ | Steps 3–4 $\square$ |

> [!abstract] משפט 15.16
> אם $T : V \to V$ נורמלית ו-$U \subseteq V$ הוא $T$-שמור, אז $U$ גם $T^*$-שמור, $U^\perp$ גם $T$-שמור, ו-$T|_U$ נורמלית.

> [!note]- הוכחה
> מ-$T^* = f(T)$: כל ת"מ $T$-שמור גם $f(T) = T^*$-שמור. $\square$

> [!proof]+ Natural Deduction — Proof 1 (Theorem 15.16)
> | # | Claim | Justification |
> |---|-------|---------------|
> | 1 | $T$ normal, $U$ $T$-invariant | Given |
> | 2 | $T^* = f(T)$ for some $f \in \mathbb{R}[x]$ | Theorem 15.6 (normal $\Rightarrow$ $T^*$ is polynomial in $T$) |
> | 3 | $U$ is $f(T)$-invariant (= $T^*$-invariant): $f(T)[U] \subseteq U$ | $U$ $T$-invariant $\Rightarrow$ $U$ $p(T)$-invariant for any poly $p$ |
> | 4 | $U^\perp$ is $T^*$-invariant | Claim 15.14 applied to $T$ |
> | 5 | $U^\perp$ is $T$-invariant: apply steps 1–3 with $T^*$ and $(T^*)^* = T$ | Steps 2–3 applied symmetrically |
> | 6 | $T|_U$ normal: $(T|_U)(T|_U)^* = (T|_U)^*(T|_U)$ since $T^*|_U = (T|_U)^*$ (from step 3) | Steps 1–3 $\square$ |

> [!abstract] טענה 15.17
> לכל $T : V \to V$ מעל $\mathbb{R}$ קיים ת"מ $T$-שמור $U \subseteq V$ מממד $\le 2$.

> [!note]- הוכחה
> ניקח $g$ גורם אי-פריק של $m_T$. אם $\deg g = 1$ — ו"ע נותן $\dim U = 1$. אם $\deg g = 2$ — לכל $0 \ne v \in \ker g(T)$: $U = \text{Sp}\{v, Tv\}$ נשמר תחת $T$ (מ-$g(T)v = 0$ נובע $T^2 v \in U$). $\square$

> [!proof]+ Natural Deduction — Proof 1 (Claim 15.17)
> | # | Claim | Justification |
> |---|-------|---------------|
> | 1 | $T : V \to V$ over $\mathbb{R}$; pick $g$ irreducible factor of $m_T$ | Factorization in $\mathbb{R}[x]$ |
> | 2 | Case $\deg g = 1$: $g = x - \lambda$, so $\exists v \ne 0$ with $Tv = \lambda v$ | Eigenvalue; $U = \mathrm{Sp}\{v\}$, $\dim U = 1$ |
> | 3 | Case $\deg g = 2$: pick $0 \ne v \in \ker g(T)$; set $U = \mathrm{Sp}\{v, Tv\}$ | $g(T)v = 0$ |
> | 4 | $U$ is $T$-invariant: $T(v) = Tv \in U$; $T(Tv) = T^2 v \in U$ since $g(T)v = 0$ gives $T^2 v = -a_1 Tv - a_0 v$ | Write $g = x^2 + a_1 x + a_0$ |
> | 5 | $\dim U \le 2$; in both cases $U$ is $T$-invariant with $\dim U \le 2$ | Steps 2–4 $\square$ |

> [!abstract] משפט 15.19 — צורה קנונית ממשית
> אם $T : V \to V$ נורמלית ו-$V$ מ"פ ממשי, קיים בסיס א"נ שביחס אליו המטריצה המייצגת היא בלוקים אלכסוניים:
> - בלוקים $1 \times 1$: ע"ע ממשיים $\lambda_i$
> - בלוקים $2 \times 2$: $\begin{pmatrix} a_k & b_k \\ -b_k & a_k \end{pmatrix}$ עם $b_k \ne 0$

> [!example] דוגמה 15.9
> המטריצות $A \in M_2(\mathbb{R})$ הנורמליות הן בדיוק: $A = A^t$ (סימטריות) או $A = \begin{pmatrix} a & b \\ -b & a \end{pmatrix}$.

---

## פרק 16 — טרנספורמציות ומטריצות אוניטריות

> [!abstract] הגדרה 16.1 — אוניטרית / אורתוגונלית
> $T : V \to V$ נקראת **אוניטרית** ($F = \mathbb{C}$) או **אורתוגונלית** ($F = \mathbb{R}$) אם $T^* T = I$, כלומר $T^* = T^{-1}$.

> [!example] דוגמאות 16.2–16.3
> - $T_\theta$ — סיבוב בזווית $\theta$ ב-$\mathbb{R}^2$: $(T_\theta)^* = T_{-\theta} = T_\theta^{-1}$.
> - שיקוף במישור: $T^* = T$ ולכן $T^2 = I$.

> [!abstract] משפט 16.4 — תנאים שקולים
> הבאים שקולים על $T : V \to V$:
> 1. $T^* = T^{-1}$ (אוניטרית/אורתוגונלית)
> 2. $\langle Tv, Tu \rangle = \langle v, u \rangle$ לכל $v, u$
> 3. $T$ מעבירה כל בסיס א"נ לבסיס א"נ
> 4. קיים בסיס א"נ שהתמונות שלו הן בסיס א"נ
> 5. $\|Tv\| = \|v\|$ לכל $v$

> [!note]- הוכחה (סקיצה)
> $1 \Rightarrow 2$: $\langle Tv, Tu \rangle = \langle v, T^*Tu \rangle = \langle v, u \rangle$.
> $2 \Rightarrow 3 \Rightarrow 4$: ברורים.
> $4 \Rightarrow 5$: כתיבת $v = \sum a_i v_i$ נותנת $\|Tv\|^2 = \sum |a_i|^2 = \|v\|^2$.
> $5 \Rightarrow 1$: $S = T^*T - I$ צמודה לעצמה ו-$\langle Sv, v \rangle = \|Tv\|^2 - \|v\|^2 = 0$ לכל $v$. מטענה 16.5: $S = 0$. $\square$

> [!proof]+ Natural Deduction — Proof 1 (Theorem 16.4)
> | # | Claim | Justification |
> |---|-------|---------------|
> | 1 | (1→2): $\langle Tv, Tu\rangle = \langle v, T^*Tu\rangle = \langle v, u\rangle$ | $T^*T = I$ |
> | 2 | (2→3→4): if $T$ preserves inner product, ONB maps to ON set (hence basis) | Inner product preserved |
> | 3 | (4→5): if some ONB $\{v_i\}$ maps to ONB, write $v = \sum a_i v_i$; $\|Tv\|^2 = \|\sum a_i Tv_i\|^2 = \sum|a_i|^2 = \|v\|^2$ | Pythagoras on ONB |
> | 4 | (5→1): $S = T^*T - I$ self-adjoint; $\langle Sv, v\rangle = \|Tv\|^2 - \|v\|^2 = 0$ for all $v$ | Step 3 applied to condition 5 |
> | 5 | $S = 0$ by Claim 16.5; hence $T^*T = I$ | Claim 16.5 $\square$ |

> [!abstract] טענה 16.5
> אם $S$ צמודה לעצמה ו-$\langle Sv, v \rangle = 0$ לכל $v$, אזי $S = 0$.

> [!abstract] טענה 16.6
> אם $T$ אוניטרית/אורתוגונלית ו-$\lambda$ ע"ע, אזי $|\lambda| = 1$.

> [!note]- הוכחה
> $\|Tv\| = |\lambda| \|v\|$ ו-$\|Tv\| = \|v\|$ $\implies$ $|\lambda| = 1$. $\square$

> [!proof]+ Natural Deduction — Proof 1 (Claim 16.6)
> | # | Claim | Justification |
> |---|-------|---------------|
> | 1 | $T$ unitary/orthogonal, $Tv = \lambda v$, $v \ne 0$ | Given |
> | 2 | $\|Tv\| = \|\lambda v\| = |\lambda|\|v\|$ | Eigenvalue |
> | 3 | $\|Tv\| = \|v\|$ (T preserves norms) | Unitary condition (Theorem 16.4, condition 5) |
> | 4 | $|\lambda|\|v\| = \|v\|$; $\|v\| > 0$ so $|\lambda| = 1$ | Steps 2–3 $\square$ |

---

### מטריצות אוניטריות/אורתוגונליות

> [!abstract] הגדרה 16.7
> $A \in M_n(F)$ **אוניטרית** ($F = \mathbb{C}$) / **אורתוגונלית** ($F = \mathbb{R}$) אם $AA^* = A^*A = I$.

> [!abstract] טענה 16.8
> $T$ א"נ אם ורק אם $[T]_B$ א"נ (עבור בסיס א"נ $B$).

> [!abstract] משפט 16.10 — תנאים שקולים
> עבור $A \in M_n(F)$, הבאים שקולים:
> 1. $A$ אוניטרית/אורתוגונלית
> 2. שורות $A$ הן בסיס א"נ של $F^n$
> 3. עמודות $A$ הן בסיס א"נ של $F^n$
> 4. $\langle Av, Au \rangle = \langle v, u \rangle$ לכל $v, u$
> 5. $\|Av\| = \|v\|$ לכל $v$

> [!example] דוגמה 16.11 — מטריצות אורתוגונליות $2 \times 2$
> $$A = \begin{pmatrix} \cos\theta & \sin\theta \\ -\sin\theta & \cos\theta \end{pmatrix} \quad \text{(סיבוב)} \qquad \text{או} \qquad A = \begin{pmatrix} \cos\theta & \sin\theta \\ \sin\theta & -\cos\theta \end{pmatrix} \quad \text{(שיקוף)}$$

---

### הצורה הקנונית של ט"ל אורתוגונלית

> [!abstract] מסקנה 16.12 — צורה קנונית אורתוגונלית
> אם $T : V \to V$ אורתוגונלית ($F = \mathbb{R}$), קיים בסיס א"נ שביחס אליו המטריצה המייצגת היא בלוקים אלכסוניים: בלוקי $1 \times 1$ עם $\pm 1$, ובלוקי $2 \times 2$ מהצורה $\begin{pmatrix} \cos\theta_k & \sin\theta_k \\ -\sin\theta_k & \cos\theta_k \end{pmatrix}$.

> [!abstract] משפט 16.13 — יחידות
> שתי מטריצות מהצורה הקנונית הנ"ל המייצגות את אותה $T$ שוות עד כדי סדר הבלוקים (ו-$b_i$ נקבעים עד כדי סימן).

> [!note]- הוכחה
> הצורה נקבעת על ידי הפולינום האופייני: $f_A(x) = \prod_i (x - \lambda_i) \cdot \prod_j (x^2 - 2a_j x + a_j^2 + b_j^2)$, ופירוק זה חד-ערכי ב-$\mathbb{R}[x]$ (PID). $\square$

> [!proof]+ Natural Deduction — Proof 1 (Theorem 16.13)
> | # | Claim | Justification |
> |---|-------|---------------|
> | 1 | Two ONBs give canonical block forms for orthogonal $T$ | Two applications of the canonical form theorem |
> | 2 | Characteristic polynomial reads off: $f_T(x) = \prod_i(x-\lambda_i)\cdot\prod_j(x^2-2a_j x+a_j^2+b_j^2)$ | From block structure: $1\times1$ blocks give linear factors, $2\times2$ blocks give quadratic |
> | 3 | The factorization of $f_T$ in $\mathbb{R}[x]$ is unique | $\mathbb{R}[x]$ is a PID (UFD) |
> | 4 | The multiset of $\{\lambda_i\}$ and $\{(a_j, |b_j|)\}$ is uniquely determined by $f_T$ | Step 3 |
> | 5 | Both canonical forms give the same multiset of blocks (up to ordering and $b_j$ sign) | Steps 2–4 $\square$ |

---

### ניסוח מחדש של המשפט הספקטרלי

> [!abstract] משפט 16.14 — ניסוח מטריציוני
> תהי $A \in M_n(F)$: סימטרית (אם $F = \mathbb{R}$) או נורמלית (אם $F = \mathbb{C}$). אזי קיימת $P$ אורתוגונלית ($F = \mathbb{R}$) / אוניטרית ($F = \mathbb{C}$) ו-$D$ אלכסונית כך ש:
> $$A = P^{-1}DP.$$
> כאשר $F = \mathbb{R}$ ו-$P$ אורתוגונלית: $P^{-1} = P^t$, ולכן $A = P^t DP$ (ז"א $A$ גם **חופפת** ל-$D$).

> [!abstract] משפט 16.17 — אפיון ע"י ע"ע
> תהי $A \in M_n(\mathbb{C})$ נורמלית. אזי:
> 1. $A = A^*$ אם ורק אם כל ע"ע של $A$ ממשי.
> 2. $A^* = A^{-1}$ (כלומר $A$ אוניטרית) אם ורק אם $|\lambda| = 1$ לכל ע"ע $\lambda$ של $A$.

---

[[02-tirgul|דוגמאות מהתרגול →]]  |  [[03-exercises|תרגילים →]]
