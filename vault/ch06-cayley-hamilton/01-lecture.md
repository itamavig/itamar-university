---
title: "פרק 6 — הצבת ל\"ט בפולינומים; משפט קיילי-המילטון: הרצאה"
chapter: ch06-cayley-hamilton
source: lecture-yehuda
status: lecture-done
tags: [la2, lecture, ch06-cayley-hamilton]
---

# הצבת ל"ט בפולינומים; משפט קיילי-המילטון — הרצאה

> [!info] מקור
> פרק 6 מתוך הרצאות יהודה שלום (שיעורים 4–5), עמ' 15–19.

---

## הגדרה 6.1 — הצבת ט"ל בפולינום

> [!abstract] הגדרה 6.1
> יהי $f(x) = \sum_{i=0}^n a_i x^i \in F[x]$. נתונה $T : V \to V$ ט"ל. נגדיר:
> $$f(T) = \sum_{i=0}^n a_i T^i$$
> כאשר $T^0 = I$.

### הגדרה 6.3 — הצבת מטריצות בפולינומים

> [!abstract] הגדרה 6.3
> בדומה, עבור $A \in M_k(F)$:
> $$f(A) = \sum_{i=0}^n a_i A^i, \quad A^0 = I.$$

---

## דוגמאות

> [!example] דוגמה 6.2
>
> **(1)** תהי $T : \mathbb{R}_n[x] \to \mathbb{R}_n[x]$ טרנספורמציית הגזירה, ו-$f(x) = 2x^3 - 5x + 8$.
> $$f(T)(P) = 2P''' - 5P' + 8P.$$
>
> **(2)** תהי $T = T_\theta : \mathbb{R}^2 \to \mathbb{R}^2$ טרנספורמציית הסיבוב בזווית $\theta = 10°$, ו-$f(x) = 3x^{18} + 2$.
> $$f(T) = 3T^{18} + 2I = -3I + 2I = -I \implies f(T)(v) = -v.$$
> (כאן $T^{18} = T_{180°} = -I$ כי $18 \times 10° = 180°$.)

> [!example] דוגמה 6.4
> נניח $f(x) = x^2 - x - 1$, $A = \begin{pmatrix} -7 & 8 \\ -6 & 7 \end{pmatrix}$.
>
> ידוע כי $f_A(x) = x^2 - 1$ ולמעשה $A^2 = I$, לכן:
> $$f(A) = A^2 - A - I = I - A - I = -A = \begin{pmatrix} 7 & -8 \\ 6 & -7 \end{pmatrix}.$$

---

## טענה 6.5 — קשר בין ייצוג ט"ל להצבה

> [!abstract] טענה 6.5
> אם $A = [T]_B$ ו-$f(x) \in F[x]$, אזי $[f(T)]_B = f(A)$.

> [!note]- הוכחה
> נובע ישירות מהתכונות: אם $A = [T]_B,\ C = [S]_B,\ \alpha \in F$, אז:
> $$AC = [TS]_B, \quad A + C = [T+S]_B, \quad \alpha A = [\alpha T]_B.$$
> לכן בהצבת פולינום שומרים על הייצוג. $\square$

> [!proof]+ Natural Deduction — Proof 1 (Claim 6.5)
> | # | Claim | Justification |
> |---|-------|---------------|
> | 1 | $A = [T]_B$, $f(x) = \sum_{i=0}^n a_i x^i \in F[x]$ | Given |
> | 2 | $[T^k]_B = A^k$ for all $k \ge 0$ | Matrix multiplication represents composition; $[I]_B = I$ |
> | 3 | $[\alpha T]_B = \alpha A$ for all $\alpha \in F$ | Scalar multiple representation |
> | 4 | $[f(T)]_B = \left[\sum_{i=0}^n a_i T^i\right]_B = \sum_{i=0}^n a_i [T^i]_B = \sum_{i=0}^n a_i A^i = f(A)$ | Steps 2, 3 and linearity of $[\cdot]_B$ $\square$ |

---

## טענה 6.7 — תכונות בסיסיות

> [!abstract] טענה 6.7
> יהיו $f, g \in F[x]$. אזי:
> $$(f \cdot g)(T) = f(T) \cdot g(T), \quad (f + g)(T) = f(T) + g(T).$$
> בפרט: $[T]_B = A \implies [f(T)]_B = f(A)$, ולכן:
> $$f(A) = 0 \iff f(T) = 0.$$

---

## מסקנה 6.8 — שמירת אפסיות תחת דמיון

> [!abstract] מסקנה 6.8
> אם $A, C$ דומות, אז $f(C) = 0 \iff f(A) = 0$.

> [!note]- הוכחה
> $A, C$ דומות אם ורק אם הן מייצגות את אותה ט"ל $T$ מעל בסיסים שונים, ואז:
> $$f(C) = 0 \iff f(T) = 0 \iff f(A) = 0.$$
> (דרך ישירה: אם $C = P^{-1}AP$ אז $f(C) = P^{-1}f(A)P$.) $\square$

> [!proof]+ Natural Deduction — Proof 1 (Corollary 6.8)
> | # | Claim | Justification |
> |---|-------|---------------|
> | 1 | $A, C$ are similar matrices | Given |
> | 2 | $A, C$ represent the same linear map $T$ w.r.t. different bases | Definition of similar matrices |
> | 3 | $f(C) = 0 \iff f(T) = 0$ | Claim 6.5: $[f(T)]_{B_1} = f(C)$ |
> | 4 | $f(A) = 0 \iff f(T) = 0$ | Claim 6.5: $[f(T)]_{B_2} = f(A)$ |
> | 5 | $f(C) = 0 \iff f(A) = 0$ $\square$ | Steps 3, 4 (transitivity) |

---

## 6.1 — משפט קיילי-המילטון

> [!abstract] משפט 6.9 (קיילי-המילטון)
> לכל ט"ל $T : V \to V$ ולכל $A \in M_k(F)$ מתקיים:
> $$f_T(T) = 0, \quad f_A(A) = 0.$$

> [!note]- הוכחה (שלושה שלבים)
>
> **שלב 1: המשפט נכון כאשר $T$ ניתנת לשילוש.**
>
> נסמן $B = \{v_1, \ldots, v_{n+1}\}$ בסיס משלש. נוכיח באינדוקציה על $n = \dim(V)$. מקרה הבסיס $n = 1$ טריוויאלי. בצעד האינדוקציה: נסמן $W = \mathrm{Sp}\{v_1, \ldots, v_n\}$. מתנאי השילוש, $W$ נשמר תחת $T$, ולכן מוגדרת $T_W : W \to W$ (הצמצום). $T_W$ ניתנת לשילוש עם:
> $$f_{T_W}(x) = \prod_{i=1}^n (x - \lambda_i),$$
> ומהנחת האינדוקציה $f_{T_W}(T_W) = 0$, כלומר:
> $$\prod_{i=1}^n (T_W - \lambda_i I)(w) = 0 \quad \forall w \in W.$$
>
> צריך להראות: $\forall v \in V,\ \prod_{i=1}^n (T - \lambda_i I) \cdot (T - \lambda_{n+1} I)(v) = 0$.
>
> מספיק להראות $(T - \lambda_{n+1} I)v \in W$ לכל $v \in V$. כשנבדוק על איברי הבסיס:
> - לכל $v_i$ ($1 \le i \le n$): $(T - \lambda_{n+1} I)v_i = T v_i - \lambda_{n+1} v_i \in W$ (כי $T v_i \in W$).
> - עבור $v_{n+1}$: מהמשולש $T(v_{n+1}) = \sum_{i=1}^n \alpha_i v_i + \lambda_{n+1} v_{n+1}$, לכן $(T - \lambda_{n+1} I)v_{n+1} = \sum_{i=1}^n \alpha_i v_i \in W$. $\checkmark$
>
> ---
>
> **שלב 2: המשפט נכון למטריצה $A$ משולשית (או דומה למשולשית).**
>
> אם $A$ משולשית, אז $T_A : F^n \to F^n$ (כפל ב-$A$) ניתנת לשילוש ביחס לבסיס הסטנדרטי, ושלב 1 נותן $f_A(A) = 0$. אם $A$ דומה למשולשית $C$, אז $f_A = f_C$, ו-$f_C(C) = 0$ (שלב 2 ישיר) גורר $f_A(A) = 0$ (מסקנה 6.8).
>
> ---
>
> **שלב 3: מטריצה כללית.**
>
> לא כל פולינום אופייני מתפצל מעל $F$, ולכן $A$ לא בהכרח דומה למשולשית מעל $F$. אולם, לכל שדה $F$ ולכל $f \in F[x]$ קיים הרחבת שדה $F \subseteq K$ כך ש-$f$ מתפצל מעל $K$ (למשל $K = \mathbb{C}$ עבור $F = \mathbb{R}$). על $A \in M_n(F)$ מסתכלים כעל מטריצה ב-$M_n(K)$: הפ"א לא השתנה, ומעל $K$ הוא מתפצל, ולכן $A$ דומה למשולשית מעל $K$. משלב 2 מעל $K$: $f_A(A) = 0$ (אי-שוויון במטריצות עם ערכים ב-$F \subseteq K$). $\square$

> [!proof]+ Natural Deduction — Proof 1 (Theorem 6.9, Cayley-Hamilton, Step 1: triangulizable T)
> | # | Claim | Justification |
> |---|-------|---------------|
> | 1 | $T$ is triangulizable with basis $B = \{v_1,\ldots,v_{n+1}\}$; $f_T(x) = \prod_{i=1}^{n+1}(x-\lambda_i)$ | Given for Step 1 |
> | 2 | $\forall i: T(v_i)\in \mathrm{Sp}\{v_1,\ldots,v_i\}$ | Definition of triangular basis |
> | 3 | $W = \mathrm{Sp}\{v_1,\ldots,v_n\}$ is $T$-invariant | Step 2 with $i\le n$ |
> | 4 | Restriction $T_W: W\to W$ is triangulizable; $f_{T_W}(x)=\prod_{i=1}^n(x-\lambda_i)$ | Step 3 + triangular block structure |
> | 5 | By IH: $\prod_{i=1}^n(T_W-\lambda_i I)(w)=0$ for all $w\in W$ | IH on $\dim W = n$, Step 4 |
> | 6 | $(T-\lambda_{n+1}I)(v_i)\in W$ for $1\le i\le n$ | $T(v_i)\in W$ (Step 3), $\lambda_{n+1}v_i\in W$ |
> | 7 | $(T-\lambda_{n+1}I)(v_{n+1}) = \sum_{i=1}^n\alpha_i v_i\in W$ | Triangular condition: $T(v_{n+1})=\sum\alpha_iv_i+\lambda_{n+1}v_{n+1}$ |
> | 8 | $(T-\lambda_{n+1}I)(v)\in W$ for all $v\in V$ | Steps 6, 7 + linearity |
> | 9 | $\prod_{i=1}^{n+1}(T-\lambda_i I)(v)=0$ for all $v\in V$ | Steps 5, 8: apply Step 5 after Step 8 |
> | 10 | $f_T(T) = 0$ $\square$ | Step 9 |

> [!proof]+ Natural Deduction — Proof 2 (Theorem 6.9, Steps 2–3: general matrix)
> | # | Claim | Justification |
> |---|-------|---------------|
> | 1 | $A\in M_n(F)$ is upper triangular | Step 2 hypothesis |
> | 2 | $T_A: F^n\to F^n$ is triangulizable (w.r.t. standard basis) | Step 1 |
> | 3 | $f_A(A) = 0$ for triangular $A$ | Step 1 of proof (Proof 1 above) applied to $T_A$ |
> | 4 | If $A\sim C$ (similar to triangular): $f_A=f_C$ and $f_C(C)=0$ | Step 3 + similar matrices share char poly |
> | 5 | $f_A(A)=0$ for $A$ similar to triangular | Step 4 + Corollary 6.8 |
> | 6 | For general $A\in M_n(F)$: $\exists$ extension $F\subseteq K$ over which $f_A$ splits | Algebraic closure (proved later) |
> | 7 | $A\in M_n(K)$ is similar to upper triangular $C\in M_n(K)$ | Step 6 + Theorem 5.4 |
> | 8 | $f_A(A)=0$ holds over $M_n(K)$ | Steps 5, 7 |
> | 9 | $f_A(A)=0$ holds over $M_n(F)$ $\square$ | Step 8: all matrix entries lie in $F\subseteq K$ |

---

## הערה 6.10 — מדוע קיילי-המילטון לא טריוויאלי

> [!note] הערה 6.10
> הקיום של **איזשהו** פולינום $f$ עם $f(A) = 0$ הוא טריוויאלי: $\dim(M_n(F)) = n^2$, ולכן $I, A, A^2, \ldots, A^{n^2}$ בהכרח תלויים לינארית, ומכאן קיים פולינום ממעלה $\le n^2$ המאפס את $A$.
>
> קיילי-המילטון אומר שקיים פולינום ממעלה $n$ (כלומר, כבר $I, A, A^2, \ldots, A^n$ תלויים לינארית) — זה הרבה יותר חזק.

---

## דוגמה 6.11 — שימושים

> [!example] דוגמה 6.11
>
> **(1)** $T : \mathbb{R}_n[x] \to \mathbb{R}_n[x]$ טרנספורמציית הגזירה: $f_T(x) = x^{n+1}$, לכן $f_T(T) = T^{n+1} = 0$ (ידוע ישירות: גזירה $(n+1)$ פעמים מאפסת).
>
> **(2)** $A = \begin{pmatrix} -7 & 8 \\ -6 & 7 \end{pmatrix}$: הפ"א הוא $f_A(x) = x^2 - 1$, ולכן $A^2 - I = 0$, כלומר $A^2 = I$ (ניתן לאמת ישירות).
>
> **(3) שימוש מעשי:** נניח $f_A(x) = x^3 - 2x^2 + 5x - 3$. מקיילי-המילטון:
> $$A^3 - 2A^2 + 5A - 3I = 0. \tag{*}$$
> מכיוון $0$ אינו ע"ע של $A$ (כלומר $A$ הפיכה), ניתן לכפול ב-$A^{-1}$:
> $$A^{-1} = \frac{1}{3}(A^2 - 2A + 5I).$$
> וניתן לחשב $A^4$ ע"י הורדת חזקות גבוהות: מ-$(*)$, $A^3 = 2A^2 - 5A + 3I$, לכן:
> $$A^4 = 2A^3 - 5A^2 + 3A = 2(2A^2 - 5A + 3I) - 5A^2 + 3A = -A^2 - 7A + 6I.$$

---

[[02-tirgul|דוגמאות מהתרגול →]]  |  [[03-exercises|תרגילים →]]
