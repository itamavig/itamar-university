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

---

> [!abstract] הגדרה 3.4 — לכסינות מטריצה
> מטריצה $A \in M_n(F)$ נקראת **לכסינה** אם היא דומה למטריצה אלכסונית, כלומר קיימת $P \in M_n(F)$ הפיכה כך ש-$P^{-1}AP$ אלכסונית.

> [!abstract] משפט 3.5 — לכסינות דרך עמודות הפיכה
> $A$ לכסינה אם ורק אם קיימת $P$ הפיכה כך ש-$P^{-1}AP = \mathrm{diag}(\lambda_1, \ldots, \lambda_n)$. במקרה זה, עמודות $P$ הן ו״ע של $A$ עם ע״ע $\lambda_1, \ldots, \lambda_n$ (בהתאמה).

> [!note]- הוכחה
> נסמן את עמודות $P$ כ-$p_1, \ldots, p_n$. אזי $AP = PD$ (כאשר $D = \mathrm{diag}(\lambda_1,\ldots,\lambda_n)$) שקול לכך ש-$Ap_i = \lambda_i p_i$ לכל $i$. מאחר ש-$P$ הפיכה, עמודותיה שונות מאפס, ולכן הן אכן ו״ע. $\blacksquare$

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
