---
title: "ערכים עצמיים ווקטורים עצמיים — הרצאה"
chapter: ch01-eigenvalues
source: lecture
status: lecture-done
tags: [la2, lecture, ch01-eigenvalues]
---

# ערכים עצמיים ווקטורים עצמיים — הרצאה

> [!info] מקור
> סיכומי הרצאות של פרופסור יהודה שלום, תשע"ט סמסטר ב׳ (עמודים 1–12).
> מסכם: יואב רוזין ונעמה שהם.

---

## § 1 — וקטורים וערכים עצמיים של טרנספורמציות

### מוטיבציה

> [!example] דוגמה 1.1 — סדרת פיבונאצ'י
> נסתכל על סדרת פיבונאצ'י:
> $$0,\ 1,\ 1,\ 2,\ 3,\ 5,\ 8,\ \ldots$$
> המקיימת $a_{n+2} = a_{n+1} + a_n$. ניתן לכתוב זאת בצורת מטריצה:
> $$\begin{pmatrix} a_{n+2} \\ a_{n+1} \end{pmatrix} = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} a_{n+1} \\ a_n \end{pmatrix}$$
> לכן עבור $A = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}$ מתקיים:
> $$\begin{pmatrix} a_{n+2} \\ a_{n+1} \end{pmatrix} = A^n \begin{pmatrix} 1 \\ 0 \end{pmatrix}$$
> לכן, אם נמצא דרך יעילה לחשב את $A^n$ זה יאפשר לנו להבין טוב יותר את סדרת פיבונאצ'י.

---

> [!abstract] הגדרה 1.2 — וקטור עצמי וערך עצמי
> יהי $F$ שדה, $V$ מרחב וקטורי מעל $F$ ו־$T : V \to V$ העתקה לינארית. וקטור $0 \neq v \in V$ ייקרא **וקטור עצמי** של $T$ אם קיים סקלר $\lambda \in F$ כך ש־$Tv = \lambda v$. (מחייבים כי $v \neq 0$, אך בהחלט יתכן כי $\lambda = 0$.)
>
> נשים לב שהערך $\lambda$ נקבע על ידי $v$ באופן יחיד: אם $Tv = \lambda_1 v$ וגם $Tv = \lambda_2 v$ אז $\lambda_1 v = \lambda_2 v$, ולכן בגלל ש־$v \neq 0$ נקבל $\lambda_1 = \lambda_2$.

> [!abstract] הגדרה 1.3 — ערך עצמי
> בסיטואציה הנ"ל נאמר ש־$\lambda$ הוא **הערך העצמי** של ההעתקה הלינארית $T$ עבור הוקטור $v$. לפעמים פשוט נאמר ש־$\lambda$ הוא ערך עצמי של $T$ בלי להתייחס לוקטור העצמי $v$ עצמו — ובכך נאמר שקיים $0 \neq v \in V$ כך ש־$Tv = \lambda v$.

> [!note] הערה 1.4
> אם $v$ וקטור עצמי של $T$ עם ערך עצמי $\lambda$, אזי לכל $0 \neq c \in F$, גם $cv$ הוא וקטור עצמי עם ערך עצמי $\lambda$:
> $$T(cv) = c\,Tv = c(\lambda v) = \lambda(cv)$$
>
> את ההערה הזו אפשר להכליל. בהינתן $\lambda \in F$ ו־$T : V \to V$ נגדיר את **המרחב העצמי** המתאים ל־$\lambda$ על ידי:
> $$V_\lambda = \{v \in V \mid Tv = \lambda v\}$$
> אלו בעצם כל הוקטורים העצמיים עם ערך עצמי $\lambda$ בתוספת וקטור האפס.

> [!abstract] טענה 1.5 — $V_\lambda$ הוא תת-מרחב
> $V_\lambda$ הינו תת-מרחב וקטורי של $V$.
>
> **הוכחה 1 (שלושה תנאים):** נבדוק שלושה תנאים:
> - $0 \in V_\lambda$ ✓
> - סגירות תחת כפל בסקלר: הוכחנו בהערה 1.4 ✓
> - סגירות תחת חיבור: יהיו $v, u \in V_\lambda$. מתקיים $T(v+u) = Tv + Tu = \lambda v + \lambda u = \lambda(v+u)$, ולכן $v + u \in V_\lambda$ ✓
>
> **הוכחה 2 (גרעין):** $V_\lambda = \ker(T - \lambda I)$, וגרעין של כל העתקה לינארית הינו תת-מרחב. $\blacksquare$

> [!proof]+ Natural Deduction — Proof 1
>
> | # | Claim | Justification |
> |---|-------|---------------|
> | 1 | $T(0) = 0$ | $T$ is linear (Definition 1.2) |
> | 2 | $0 \in V_\lambda$ | row 1: $T(0) = 0 = \lambda \cdot 0$; definition of $V_\lambda$ |
> | 3 | Let $v, u \in V_\lambda$ | arbitrary; definition of $V_\lambda$ gives $Tv=\lambda v$, $Tu=\lambda u$ |
> | 4.0 | $T(v+u) =$ | &emsp;&emsp;<small>(show $v+u \in V_\lambda$)</small> |
> | 4.1 | &emsp;$= Tv + Tu$ | linearity of $T$ |
> | 4.2 | &emsp;$= \lambda v + \lambda u$ | row 3 |
> | 4.3 | &emsp;$= \lambda(v+u)$ | distributivity |
> | 5 | $v + u \in V_\lambda$ | rows 4.0–4.3; definition of $V_\lambda$ |
> | 6 | Let $v \in V_\lambda$, $c \in F$ | arbitrary; definition of $V_\lambda$ gives $Tv = \lambda v$ |
> | 7.0 | $T(cv) =$ | &emsp;&emsp;<small>(show $cv \in V_\lambda$)</small> |
> | 7.1 | &emsp;$= c(Tv)$ | linearity of $T$ |
> | 7.2 | &emsp;$= c(\lambda v)$ | row 6 |
> | 7.3 | &emsp;$= \lambda(cv)$ | commutativity of scalar multiplication |
> | 8 | $cv \in V_\lambda$ | rows 7.0–7.3; definition of $V_\lambda$ |
> | 9 | $V_\lambda$ is a subspace | subspace criterion; rows 2, 5, 8 |

> [!proof]+ Natural Deduction — Proof 2
>
> | # | Claim | Justification |
> |---|-------|---------------|
> | 1 | Let $v \in V_\lambda$ | arbitrary element of $V_\lambda$ |
> | 2.0 | $Tv = \lambda v$ | definition of $V_\lambda$ |
> | 2.1 | &emsp;$Tv - \lambda v = 0$ | subtract $\lambda v$ from both sides |
> | 2.2 | &emsp;$(T - \lambda I)v = 0$ | definition of $T - \lambda I$; $(\lambda I)v = \lambda v$ |
> | 2.3 | &emsp;$v \in \ker(T - \lambda I)$ | definition of $\ker$ |
> | 3 | $V_\lambda = \ker(T - \lambda I)$ | rows 1–2.3 (all steps are $\iff$, so $v \in V_\lambda \iff v \in \ker(T-\lambda I)$) |
> | 4 | $T - \lambda I$ is a linear map | linear combination of linear maps |
> | 5 | $\ker(T - \lambda I)$ is a subspace | row 4; kernel of any linear map is a subspace (Linear Algebra 1) |
> | 6 | $V_\lambda$ is a subspace | rows 3, 5 |

> [!abstract] הגדרה 1.6 — ריבוי גיאומטרי
> יהי $\lambda \in F$ ו־$T : V \to V$ העתקה לינארית. נגדיר את **הריבוי הגיאומטרי** של $\lambda$ (ביחס ל־$T$) כ־$\dim V_\lambda$.

> [!example] דוגמה 1.7
>
> **1. טרנספורמציית הזהות:** נניח כי $T : V \to V$ היא טרנספורמציית הזהות ($Tv = v$ לכל $v \in V$). אזי הערך העצמי של $T$ הוא $\lambda = 1$ (אכן, $Tv = \lambda v = v \Rightarrow \lambda = 1$). מתקיים $V_\lambda = V$, ולכן הריבוי הגיאומטרי של $\lambda = 1$ הוא $\dim V$.
>
> **2. טרנספורמציית הגזירה:** נסתכל על $V = \mathbb{R}_n[x]$ מרחב הפולינומים ממעלה $n$ ו־$T(p) = p'$ טרנספורמציית הגזירה. בדרישה $T(p) = \lambda p = p'$: מכיוון שגזירה מורידה דרגה לפולינום ממעלה חיובית, בהכרח $p$ פולינום קבוע ולכן $\lambda = 0$. מתקיים $V_0 = F$ ומימדו $1$, ולכן $\lambda = 0$ בעל ריבוי גיאומטרי $1$.
>
> **3. סיבוב בזווית $\theta$:** $T_\theta : \mathbb{R}^2 \to \mathbb{R}^2$ סיבוב. אם $\theta \neq 0, \pi$ אין ל־$T$ כלל וקטורים עצמיים. אם $\theta = 0$ אז $T = I$ וכבר ניתחנו. אם $\theta = \pi$ מתקיים $T = -I$, כלומר $Tv = -v$ לכל $v \in \mathbb{R}^2$, ולכן $\lambda = -1$ הוא הערך העצמי היחיד עם ריבוי גיאומטרי $\dim V_\lambda = \dim \mathbb{R}^2 = 2$.
>
> **4. טרנספורמציה ציקלית:** $V$ מרחב וקטורי ממימד $n$, $T : V \to V$ העתקה לינארית כך שקיים $v \in V$ המקיים $T^n v = v$ ו־$v, Tv, \ldots, T^{n-1}v$ בסיס של $V$. ניתוח לא קשה מראה שכל $\lambda \in F$ המקיים $\lambda^n = 1$ הוא ערך עצמי של $T$ עם ריבוי גיאומטרי $1$. הניתוח תלוי בשדה $F$ מעליו אנו עובדים.

---

> [!abstract] משפט 1.8 — וקטורים עצמיים עם ערכים עצמיים שונים הם בלתי תלויים לינארית
> תהי $T : V \to V$ העתקה לינארית ותהי $A \subseteq V$ קבוצה של וקטורים שכולם וקטורים עצמיים של $T$ עם ערכים עצמיים שונים זה מזה. אז $A$ בלתי תלויה לינארית.
>
> **הוכחה:** נניח בשלילה כי $A$ תלויה לינארית, ולכן קיים צירוף לינארי לא טריוויאלי של איבריה שמתאפס. נבחר צירוף לינארי כזה שהוא מינימלי (מערב מספר מינימלי של מחוברים). מתקיים:
> $$Tv_i = \lambda_i v_i,\quad i \neq j \Rightarrow \lambda_i \neq \lambda_j,\quad \sum_{i=1}^{m} a_i v_i = 0 \tag{$*$}$$
> נשים לב ש־$m > 1$: אם $m = 1$ אז $a_1 v_1 = 0$ אבל $v_1 \neq 0$ ו־$a_1 \neq 0$ (הצירוף אינו טריוויאלי) — סתירה.
>
> נפעיל את $T$ על $(*)$:
> $$0 = T(0) = T\!\left(\sum_{i=1}^m a_i v_i\right) = \sum_{i=1}^m a_i Tv_i = \sum_{i=1}^m \lambda_i a_i v_i$$
> נכפיל את $(*)$ ב־$\lambda_m$: $\displaystyle\sum_{i=1}^m \lambda_m a_i v_i = 0$. בהחסרה:
> $$\sum_{i=1}^{m-1} (\lambda_i - \lambda_m)\, a_i v_i = 0$$
> כל המקדמים $(\lambda_i - \lambda_m) a_i$ שונים מאפס: $\lambda_i \neq \lambda_m$ מהנחת הערכים העצמיים השונים, ו־$a_i \neq 0$ לכל $i$ כי אחרת היינו מוציאים את המחובר ה־$i$ ומקבלים צירוף לינארי קצר יותר — בסתירה למינימליות. קיבלנו צירוף לינארי לא טריוויאלי קצר יותר המתאפס — סתירה. $\blacksquare$

> [!proof]+ Natural Deduction — Proof 1
>
> | # | Claim | Justification |
> |---|-------|---------------|
> | 1 | Assume $A$ is linearly dependent | for contradiction |
> | 2 | There is a minimal non-trivial linear combination: $\sum_{i=1}^{m} a_i v_i = 0$, where $Tv_i = \lambda_i v_i$, $i \neq j \Rightarrow \lambda_i \neq \lambda_j$, not all $a_i = 0$ | definition of linear dependence; choose minimal such combination |
> | 3 | $m > 1$ | if $m=1$: $a_1 v_1 = 0$ with $v_1 \neq 0$ and $a_1 \neq 0$ — contradiction |
> | 4.0 | $0 =$ | &emsp;&emsp;<small>(apply $T$ to row 2)</small> |
> | 4.1 | &emsp;$= T\!\left(\displaystyle\sum_{i=1}^m a_i v_i\right)$ | $T(0)=0$; row 2 |
> | 4.2 | &emsp;$= \displaystyle\sum_{i=1}^m a_i T v_i$ | linearity of $T$ |
> | 4.3 | &emsp;$= \displaystyle\sum_{i=1}^m \lambda_i a_i v_i$ | row 2: $Tv_i = \lambda_i v_i$ |
> | 5 | $\displaystyle\sum_{i=1}^m \lambda_m a_i v_i = 0$ | multiply row 2 by $\lambda_m$ |
> | 6 | $\displaystyle\sum_{i=1}^{m-1} (\lambda_i - \lambda_m)\, a_i v_i = 0$ | row 4.3 minus row 5 |
> | 7 | $(\lambda_i - \lambda_m) a_i \neq 0$ for all $1 \leq i \leq m-1$ | $\lambda_i \neq \lambda_m$ (distinct eigenvalues, row 2); $a_i \neq 0$ (minimality: removing $v_i$ gives shorter combination) |
> | 8 | Row 6 is a non-trivial linear combination of $m-1$ eigenvectors equaling $0$ | row 7 |
> | 9 | Contradiction with minimality of $m$ | rows 6–8 vs. row 2 |
> | 10 | $A$ is linearly independent | by contradiction (rows 1–9) |

[[02-tirgul|דוגמאות מהתרגול →]]  |  [[03-exercises|תרגילים →]]
