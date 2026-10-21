---
title: "פרק 4 — הפולינום האופייני: הרצאה"
chapter: ch04-characteristic-poly
source: lecture-yehuda
status: lecture-done
tags: [la2, lecture, ch04-characteristic-poly]
---

# הפולינום האופייני — הרצאה

> [!info] מקור
> פרק 4 מתוך הרצאות יהודה שלום, תשע״ט סמסטר ב׳ (עמודים 1–12).

---

## § 4 — הפולינום האופייני של העתקה לינארית

> [!abstract] הגדרה 4.1 — פולינום אופייני של העתקה
> יהי $V$ מ״ו ממימד $n$ מעל $F$ ו-$T : V \to V$ העתקה לינארית. **הפולינום האופייני** של $T$ מוגדר כ:
> $$f_T(x) = f_{[T]_B}(x) = \det(xI - [T]_B),$$
> כאשר $B$ בסיס כלשהו של $V$. ההגדרה אינה תלויה בבחירת הבסיס (ראו משפט 4.2).

> [!abstract] משפט 4.2 — מטריצות דומות → אותו פולינום אופייני
> אם $A, C \in M_n(F)$ דומות (קיימת $P$ הפיכה עם $C = P^{-1}AP$), אז $f_A(x) = f_C(x)$.

> [!note]- הוכחה
> נתון ש-$A, C$ דומות, כלומר קיימת $P$ הפיכה כך ש-$P^{-1}AP = C$. מכאן נובע שלכל $x \in F$:
> $$P^{-1}(xI - A)P = xI - C.$$
> לכן המטריצות $xI - A$ ו-$xI - C$ דומות, ומטריצות דומות הן בעלות אותה דטרמיננטה, ולכן:
> $$f_C(x) = \det(xI - C) = \det(xI - A) = f_A(x).$$
>
> ההוכחה הזו מראה שוויון בין שתי **פונקציות** ב-$x$ (לכל הצבת סקלר). כדי להסיק שוויון בין **פולינומים פורמליים**, נחשוב על הכל מעל שדה הפונקציות הרציונליות $F(x)$. שם $P, A, C \in M_n(F) \subseteq M_n(F(x))$, ואותו חישוב נותן דמיון של $xI - A$ ו-$xI - C$ מעל $M_n(F(x))$, ולכן שוויון דטרמיננטות כאיברים של $F(x)$ — שהם בדיוק הפולינומים האופייניים. $\blacksquare$

---

> [!example] דוגמה 4.3 — פולינומים אופייניים של העתקות קלאסיות
>
> **סיבוב $T_\theta : \mathbb{R}^2 \to \mathbb{R}^2$:** $[T_\theta]_B = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}$, ולכן:
> $$f_{T_\theta}(x) = x^2 - 2\cos\theta \cdot x + 1.$$
> הפולינום מתפצל מעל $\mathbb{R}$ רק כאשר $\theta = 0$ ($f = (x-1)^2$) או $\theta = \pi$ ($f = (x+1)^2$).
>
> **גזירה $D : \mathbb{R}_n[x] \to \mathbb{R}_n[x]$:** $[D]_B$ משולשית עליונה עם $0$ על האלכסון, ולכן:
> $$f_D(x) = x^{n+1}.$$

---

> [!abstract] משפט 4.4 — ע״ע הם שורשי הפולינום האופייני
> $\lambda \in F$ הוא ע״ע של $T$ אם ורק אם $f_T(\lambda) = 0$.

> [!note]- הוכחה
> $\lambda$ ע״ע $\iff \ker(T - \lambda I) \neq \{0\} \iff T - \lambda I$ לא הפיכה $\iff \det(\lambda I - [T]_B) = 0 \iff f_T(\lambda) = 0$. $\blacksquare$

---

> [!abstract] הגדרה 4.5 — ריבוי אלגברי
> יהי $\lambda$ ע״ע של $T$. **הריבוי האלגברי** של $\lambda$ (ביחס ל-$T$) הוא החזקה המקסימלית של $(x - \lambda)$ המחלקת את $f_T(x)$, כלומר:
> $$r_a(\lambda) = \max\{k \in \mathbb{N} \mid (x-\lambda)^k \mid f_T(x)\}.$$

> [!note] הערה 4.6 — ריבוי גיאומטרי
> לצד הריבוי האלגברי, **הריבוי הגיאומטרי** של $\lambda$ הוא:
> $$r_g(\lambda) = \dim V_\lambda = \dim \ker(T - \lambda I).$$
> תמיד מתקיים $1 \le r_g(\lambda) \le r_a(\lambda)$ (ראו טענה 4.9).

---

> [!example] דוגמה 4.7 — ריבויים אלגבריים וגיאומטריים
>
> **גזירה $D$ על $\mathbb{R}_n[x]$:** $f_D(x) = x^{n+1}$, ולכן $r_a(0) = n+1$. אבל $V_0 = \ker D = \mathbb{R}_0[x]$ (פולינומים קבועים), ולכן $r_g(0) = 1$. כאן $r_g < r_a$.
>
> **מטריצה אלכסונית עם ריבויים:** $A = \mathrm{diag}(\lambda_1, \lambda_1, \lambda_2)$ ($\lambda_1 \neq \lambda_2$):
> $f_A(x) = (x-\lambda_1)^2(x-\lambda_2)$, לכן $r_a(\lambda_1) = 2$, $r_a(\lambda_2) = 1$.
> $r_g(\lambda_1) = \dim \ker(A - \lambda_1 I) = 2$, $r_g(\lambda_2) = 1$. כאן $r_g = r_a$ לכל ע״ע.

---

> [!note] הערה 4.8
> ייתכן מצב שבו $\sum_{\lambda} r_a(\lambda) < \deg f_T$. לדוגמה, עבור $f_T(x) = x^2(x^2 + 1)$ (מעל $\mathbb{R}$), סכום הריבויים האלגבריים הוא $2$ (רק $\lambda = 0$ ע״ע), בעוד שדרגת הפולינום היא $4$.

> [!abstract] טענה 4.9 — ריבוי גיאומטרי $\le$ ריבוי אלגברי
> לכל ע״ע $\lambda$ של $T$: $r_g(\lambda) \le r_a(\lambda)$.

> [!note]- הוכחה
> נסמן $r = r_g(\lambda)$ ויהי $\{v_1, \ldots, v_r\}$ בסיס של $V_\lambda$. נרחיב לבסיס $B = \{v_1, \ldots, v_r, w_{r+1}, \ldots, w_n\}$ של $V$. בבסיס זה:
> $$[T]_B = \begin{pmatrix} \lambda I_r & * \\ 0 & C \end{pmatrix}$$
> (כי $Tv_i = \lambda v_i$ לכל $i \le r$, ועל שאר האיברים $T$ מחזיר משהו כלשהו). לכן:
> $$f_T(x) = \det(xI - [T]_B) = \det \begin{pmatrix} (x-\lambda)I_r & -* \\ 0 & xI-C \end{pmatrix} = (x-\lambda)^r \cdot f_C(x).$$
> לכן $(x-\lambda)^r \mid f_T(x)$, כלומר $r_a(\lambda) \ge r = r_g(\lambda)$. $\blacksquare$

---

> [!abstract] משפט 4.10 — קריטריון ללכסינות (מלא)
> $T : V \to V$ (עם $\dim V = n$) לכסינה אם ורק אם שני התנאים מתקיימים:
> 1. $f_T(x)$ מתפצל לחלוטין לגורמים לינאריים מעל $F$, כלומר $f_T(x) = \prod_{i=1}^k (x-\lambda_i)^{r_a(\lambda_i)}$.
> 2. לכל ע״ע $\lambda_i$: $r_g(\lambda_i) = r_a(\lambda_i)$.

> [!note]- הוכחה
> **($\Rightarrow$)** אם $T$ לכסינה, קיים בסיס של ו״ע. כל ע״ע מופיע בו $r_g(\lambda_i)$ פעמים, ולכן $f_T(x) = \prod (x-\lambda_i)^{r_g(\lambda_i)}$ — כלומר מתפצל. בנוסף $\sum r_g(\lambda_i) = n = \deg f_T = \sum r_a(\lambda_i)$, ויחד עם $r_g \le r_a$ נובע $r_g = r_a$ לכל $i$.
>
> **($\Leftarrow$)** אם שני התנאים מתקיימים: $\sum r_g(\lambda_i) = \sum r_a(\lambda_i) = n$. לפי מסקנה 2.4, $T$ לכסינה. $\blacksquare$

---

[[02-tirgul|דוגמאות מהתרגול →]]  |  [[03-exercises|תרגילים →]]
