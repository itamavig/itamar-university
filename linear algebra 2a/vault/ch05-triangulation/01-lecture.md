---
title: "פרק 5 — לכסון ושילוש: הרצאה"
chapter: ch05-triangulation
source: lecture-yehuda
status: lecture-done
tags: [la2, lecture, ch05-triangulation]
---

# לכסון ושילוש — הרצאה

> [!info] מקור
> פרק 5 מתוך הרצאות יהודה שלום (שיעור 4), עמ' 13–14.

---

## תזכורת 5.1 — סדרת פיבונאצי מעל $\mathbb{F}_m$

בשיעור הראשון ראינו כי לסדרת פיבונאצי $(a_n)$ מתקיים:
$$\begin{pmatrix} a_{n+1} \\ a_n \end{pmatrix} = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}^n \begin{pmatrix} 1 \\ 0 \end{pmatrix}.$$
נסמן $A = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}$.

כאשר מסתכלים על הסדרה מעל $\mathbb{F}_m$ (עם $m \in \mathbb{N}$), הסדרה חייבת להיות מחזורית — שכן מספר הזוגות $(a_n, a_{n+1})$ האפשריים הוא לכל היותר $m^2$, ואורך המחזור חסום מלעיל על ידי $m^2$.

> [!example] דוגמה: $m = 7$
> $$0, 1, 1, 2, 3, 5, 1, 6, 0, 6, 6, 5, 4, 2, 6, 1, 0, 1, \ldots$$
> אורך המחזור יוצא $16$.

---

## טענה 5.2 — חסם משופר לפיבונאצי מעל $\mathbb{F}_p$

> [!abstract] טענה 5.2
> אם $p$ ראשוני ו-$p \equiv 1, 4 \pmod{5}$, אז אורך המחזור של סדרת פיבונאצי מעל $\mathbb{F}_p$ חסום מלעיל על ידי $p - 1$.

> [!note]- הוכחה
> נעבוד עם סדרת פיבונאצי בשדה $\mathbb{F}_p$ (מוגדרת באופן זהה).
>
> מחזוריות מובטחת כאשר $A^k = I$, שכן אז:
> $$\begin{pmatrix} a_{n+k+1} \\ a_{n+k} \end{pmatrix} = A^k \begin{pmatrix} a_{n+1} \\ a_n \end{pmatrix} = \begin{pmatrix} a_{n+1} \\ a_n \end{pmatrix}.$$
> כל $k$ המקיים $A^k = I$ נותן חסם על אורך המחזור.
>
> **לכסון $A$:** הפולינום האופייני הוא $f_A(x) = x^2 - x - 1$. נניח (ונוכיח בהמשך) ש-$f_A$ מתפצל ב-$\mathbb{F}_p$, כלומר יש ל-$A$ ערכים עצמיים $\lambda_1, \lambda_2 \in \mathbb{F}_p$.
>
> שימו לב: $\lambda_1, \lambda_2 \ne 0$ כי אפס אינו שורש של $f_A$. לכן:
> $$A = P^{-1} \begin{pmatrix} \lambda_1 & 0 \\ 0 & \lambda_2 \end{pmatrix} P \implies A^k = P^{-1} \begin{pmatrix} \lambda_1^k & 0 \\ 0 & \lambda_2^k \end{pmatrix} P.$$
>
> נרצה $k$ כך ש-$\lambda_1^k = \lambda_2^k = 1$. **משפט פרמה הקטן** מבטיח ש-$k = p - 1$ מקיים זאת (שכן $\lambda_i \ne 0$ בשדה $\mathbb{F}_p$).
>
> **מדוע $f_A$ מתפצל עבור $p \equiv 1,4 \pmod{5}$?**
>
> בשדה עם מציין שונה מ-$2$, פולינום ריבועי $x^2 - x - 1 = 0$ מתפצל אם ורק אם הדיסקרימיננט $\Delta = b^2 - 4ac = 1 + 4 = 5$ הוא ריבוע מושלם בשדה, כלומר קיים $q \in \mathbb{F}_p$ עם $q^2 = 5$.
>
> מ**חוק ההדדיות הריבועית** של גאוס: $5$ הוא ריבוע מודולו $p$ אם ורק אם $p$ הוא ריבוע מודולו $5$. הריבועים ב-$\mathbb{F}_5$ הם $\{1, 4\}$ (שכן $1^2=1,\, 2^2=4,\, 3^2=4,\, 4^2=1$). לכן התנאי $p \equiv 1, 4 \pmod{5}$ מבטיח בדיוק ש-$5$ ריבוע ב-$\mathbb{F}_p$, ו-$f_A$ מתפצל לשני שורשים שונים. $\square$

> [!proof]+ Natural Deduction — Proof 1 (Claim 5.2)
> | # | Claim | Justification |
> |---|-------|---------------|
> | 1 | $p$ is prime and $p \equiv 1,4 \pmod 5$ | Given |
> | 2 | The Fibonacci sequence over $\mathbb{F}_p$ satisfies $\binom{a_{n+1}}{a_n} = A^n\binom{1}{0}$ where $A = \begin{pmatrix}1&1\\1&0\end{pmatrix}$ | Definition of Fibonacci recurrence |
> | 3 | If $A^k = I$ then the sequence is periodic with period dividing $k$ | Step 2: $A^k\binom{a_{n+1}}{a_n} = \binom{a_{n+1}}{a_n}$ |
> | 4 | $f_A(x) = x^2 - x - 1$ splits over $\mathbb{F}_p$ (has roots $\lambda_1,\lambda_2 \in \mathbb{F}_p$) | Steps 1, 7 (proved below) |
> | 5 | $\lambda_1, \lambda_2 \ne 0$ | $f_A(0) = -1 \ne 0$, so $0$ is not a root |
> | 6 | $A = P^{-1}\mathrm{diag}(\lambda_1,\lambda_2)P$, so $A^k = P^{-1}\mathrm{diag}(\lambda_1^k,\lambda_2^k)P$ | Step 4: $A$ diagonalizable over $\mathbb{F}_p$ |
> | 7 | $A^{p-1} = I$ | Steps 5,6: Fermat's little theorem gives $\lambda_i^{p-1}=1$ for $\lambda_i\ne 0$ in $\mathbb{F}_p$ |
> | 8 | Period of Fibonacci over $\mathbb{F}_p$ divides $p-1$, hence $\le p-1$ | Steps 3, 7 |
> | 9 | $f_A$ splits over $\mathbb{F}_p$ iff $\Delta = 5$ is a square in $\mathbb{F}_p$ | Quadratic formula (char $\ne 2$) |
> | 10 | $5$ is a square mod $p$ iff $p$ is a square mod $5$ | Quadratic reciprocity |
> | 11 | Squares in $\mathbb{F}_5$ are $\{1,4\}$ (since $1^2=1,2^2=4,3^2=4,4^2=1$) | Direct computation |
> | 12 | $p \equiv 1,4\pmod 5$ implies $5$ is a square in $\mathbb{F}_p$, so $f_A$ splits | Steps 10, 11 → confirms Step 4 |
> | 13 | Period $\le p-1$ $\square$ | Step 8 |

---

## הגדרה 5.3 — ט"ל ניתנת לשילוש

> [!abstract] הגדרה 5.3 (שילוש)
> ט"ל $T : V \to V$ נקראת **ניתנת לשילוש** אם קיים בסיס $B$ של $V$ כך ש-$[T]_B$ משולשית עליונה.

**תנאי הכרחי:** אם $T$ ניתנת לשילוש, אז $f_T$ מתפצל למכפלת גורמים לינאריים:
$$f_T(x) = \prod_{i=1}^n (x - \lambda_i), \quad \lambda_i \in F.$$
(הפולינום האופייני של מטריצה משולשית הוא מכפלת הגורמים $(x - \lambda_{ii})$.)

---

## משפט 5.4 — שילוש כאשר הפולינום מתפצל

> [!abstract] משפט 5.4
> נניח $f_T(x) = \displaystyle\prod_{i=1}^n (x - \lambda_i)$ עם $\lambda_i \in F$. אז קיים בסיס $B$ של $V$ כך ש-$[T]_B$ משולשית עליונה.
>
> (יחד עם ההכרחיות לעיל, קיבלנו: $T$ ניתנת לשילוש $\iff$ $f_T$ מתפצל מעל $F$.)

> [!note]- הוכחה (אינדוקציה על $\dim(V)$)
> **תצפית:** ייצוג $[T]_B$ ביחס לבסיס $B = \{v_i\}$ הוא משולשית עליונה **אם ורק אם**:
> $$\forall 1 \le i \le n : T(v_i) \in \mathrm{Sp}\{v_1, \ldots, v_i\}.$$
>
> **בסיס האינדוקציה:** $\dim(V) = 1$ — טריוויאלי, כל מטריצה $1 \times 1$ משולשית.
>
> **צעד האינדוקציה:** נניח הטענה ל-$n$ ונוכיח ל-$n+1$. נתון:
> $$f_T(x) = \prod_{i=1}^{n+1}(x - \lambda_i).$$
>
> ניקח $\lambda = \lambda_1$. מכיוון $f_T(\lambda_1) = 0$, הרי $\lambda_1$ הוא ע"ע של $T$. יהי $0 \ne v_1$ ו"ע המתאים: $Tv_1 = \lambda_1 v_1$.
>
> נשלים $v_1$ לבסיס $B' = \{v_1, w_2, \ldots, w_{n+1}\}$ של $V$, ונסמן $W = \mathrm{Sp}\{w_2, \ldots, w_{n+1}\}$. ביחס לבסיס $B'$ יש ל-$T$ ייצוג בלוק-משולש:
> $$[T]_{B'} = A = \begin{pmatrix} \lambda_1 & * & \cdots & * \\ 0 & & & \\ \vdots & & C & \\ 0 & & & \end{pmatrix}$$
> כאשר $C$ היא מטריצת $n \times n$ המתאימה לבלוק הימני-תחתון.
>
> **הגדרת $S$:** תהי $S : W \to W$ הט"ל שייצוגה ביחס לבסיס $\{w_2, \ldots, w_{n+1}\}$ הוא $C$.
>
> **הפולינום של $S$:** מחישוב הפ"א של מטריצת בלוקים:
> $$f_A(x) = (x - \lambda_1) \cdot f_C(x).$$
> מצד שני, $f_A = f_T = \prod_{i=1}^{n+1}(x-\lambda_i)$, ולכן:
> $$f_C(x) = f_S(x) = \prod_{i=2}^{n+1}(x-\lambda_i).$$
> זה מתפצל, ולכן ניתן להפעיל את **הנחת האינדוקציה** על $S$ ($\dim(W) = n$): קיים בסיס $B'' \subseteq W$ המשלש את $S$.
>
> **הבסיס המשלש ל-$T$:** נסמן $B'' = \{v_2, \ldots, v_{n+1}\}$. נטען ש-$\{v_1\} \cup B''$ משלש את $T$.
>
> מהגדרת $S$ ומלינאריות, לכל $w \in W$:
> $$(T - S)(w) = T(w) - S(w) = a \cdot v_1 \quad \text{עבור איזה } a \in F.$$
> כלומר, $\mathrm{Im}(T - S) \subseteq \mathrm{Sp}\{v_1\}$.
>
> לכן, לכל $v_i \in B''$: $T(v_i) = S(v_i) + (T-S)(v_i) \in \mathrm{Sp}\{v_2, \ldots, v_i\} + \mathrm{Sp}\{v_1\} = \mathrm{Sp}\{v_1, \ldots, v_i\}$.
>
> יחד עם $T(v_1) = \lambda_1 v_1 \in \mathrm{Sp}\{v_1\}$, קיבלנו ש-$[T]_{\{v_1\} \cup B''}$ משולשית עליונה. $\square$

> [!proof]+ Natural Deduction — Proof 1 (Theorem 5.4)
> | # | Claim | Justification |
> |---|-------|---------------|
> | 1 | $f_T(x) = \prod_{i=1}^n(x-\lambda_i)$, $\lambda_i \in F$ | Given |
> | 2 | $[T]_B$ is upper triangular iff $\forall i: T(v_i) \in \mathrm{Sp}\{v_1,\ldots,v_i\}$ | Observation about triangular matrices |
> | 3 | **Base:** $\dim V = 1$: any $1\times 1$ matrix is upper triangular | Trivial |
> | 4 | **Step:** Assume true for $\dim = n$; prove for $\dim = n+1$ | Induction hypothesis |
> | 5 | $\lambda_1$ is an eigenvalue of $T$ | $f_T(\lambda_1) = 0$ |
> | 6 | $\exists\, 0\ne v_1$ with $Tv_1 = \lambda_1 v_1$; extend to basis $B' = \{v_1,w_2,\ldots,w_{n+1}\}$ | Step 5 + basis extension |
> | 7 | $[T]_{B'} = \begin{pmatrix}\lambda_1 & *\\ 0 & C\end{pmatrix}$ (block upper triangular) | $Tv_1 = \lambda_1 v_1$, so first column is $(\lambda_1,0,\ldots,0)^t$ |
> | 8 | Let $S: W\to W$ be the operator with matrix $C$ w.r.t. $\{w_2,\ldots,w_{n+1}\}$, where $W = \mathrm{Sp}\{w_2,\ldots,w_{n+1}\}$ | Definition |
> | 9 | $f_A(x) = (x-\lambda_1)\cdot f_C(x)$, and $f_A = f_T = \prod_{i=1}^{n+1}(x-\lambda_i)$ | Block triangular char poly formula |
> | 10 | $f_S(x) = f_C(x) = \prod_{i=2}^{n+1}(x-\lambda_i)$ splits over $F$ | Steps 1, 9 |
> | 11 | By IH: $\exists$ basis $B'' = \{v_2,\ldots,v_{n+1}\}\subseteq W$ that triangulates $S$ | Steps 4, 10: $\dim W = n$ |
> | 12 | For all $w\in W$: $(T-S)(w) = av_1$ for some $a\in F$, i.e., $\mathrm{Im}(T-S)\subseteq \mathrm{Sp}\{v_1\}$ | Follows from definition of $S$ and linearity |
> | 13 | For each $v_i\in B''$: $T(v_i) = S(v_i) + (T-S)(v_i) \in \mathrm{Sp}\{v_2,\ldots,v_i\} + \mathrm{Sp}\{v_1\} = \mathrm{Sp}\{v_1,\ldots,v_i\}$ | Steps 11, 12 |
> | 14 | $T(v_1) = \lambda_1 v_1 \in \mathrm{Sp}\{v_1\}$ | Step 6 |
> | 15 | $\{v_1\}\cup B''$ triangulates $T$; by Step 2, $[T]_{\{v_1\}\cup B''}$ is upper triangular $\square$ | Steps 2, 13, 14 |

---

[[02-tirgul|דוגמאות מהתרגול →]]  |  [[03-exercises|תרגילים →]]
