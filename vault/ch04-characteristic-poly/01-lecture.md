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
> **אם $f_T(x) = \prod_{i=1}^k (x-\lambda_i)^{n_i}$ (עם $\lambda_i$ שונים זה מזה):** נטען שהריבוי האלגברי של $\lambda_i$ הוא בדיוק $n_i$.
> ברור ש-$n_i \le r_a(\lambda_i)$ כי $(x-\lambda_i)^{n_i}$ מחלק את $f_T$.
> נניח בשלילה ש-$r_a(\lambda_i) \ge n_i + 1$, כלומר $(x-\lambda_i)^{n_i+1} \mid f_T(x)$. אזי:
> $$\prod_{j=1}^k (x-\lambda_j)^{n_j} = f_T(x) = (x-\lambda_i)^{n_i+1} \cdot p(x).$$
> נעביר אגפים:
> $$(x-\lambda_i)^{n_i}\left[\prod_{j \ne i}(x-\lambda_j)^{n_j} - (x-\lambda_i)\,p(x)\right] = 0.$$
> מכיוון ש-$(x-\lambda_i)^{n_i} \ne 0$ (כפולינום), הסוגר מתאפס. נציב $x = \lambda_i$:
> $$\prod_{j \ne i}(\lambda_i - \lambda_j)^{n_j} = 0.$$
> אבל כל $\lambda_i - \lambda_j \ne 0$ (כי $\lambda_i$ שונים) — סתירה. לכן $r_a(\lambda_i) = n_i$.

> [!note] הערה 4.8
> נשים לב שבדוגמה $r_a(\lambda_i) = n_i = \deg f_T / k$ — אך זה **אינו** חייב להיות המצב בכלל. לדוגמה, עבור $f_T = x^2(x^2+1)$ (מעל $\mathbb{R}$), סכום הריבויים האלגבריים הוא $2$ (רק ל-$\lambda = 0$) בעוד שדרגת הפולינום היא $4$.

---

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
> $T : V \to V$ (עם $\dim V = n$) לכסינה אם ורק אם ש