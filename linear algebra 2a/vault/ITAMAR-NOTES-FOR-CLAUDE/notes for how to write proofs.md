take this card for example:
> [!abstract] טענה 1.5 — $V_\lambda$ הוא תת-מרחב
> $V_\lambda$ הינו תת-מרחב וקטורי של $V$.
>
> **הוכחה 1 (שלושה תנאים):** נבדוק שלושה תנאים:
> - $0\in V_\lambda$ ✓
> - סגירות תחת כפל בסקלר: הוכחנו בהערה 1.4 ✓
> - סגירות תחת חיבור: לכל $v,u\in V_\lambda$ מתקיים $T(v+u)=Tv+Tu=\lambda v+\lambda u=\lambda(v+u)$ ✓
>
> **הוכחה 2 (גרעין):** $V_\lambda=\ker(T-\lambda I)$, וגרעין של כל טרנספורמציה לינארית הינו תת-מרחב. $\blacksquare$
>
> ---
>
> **ניכוי טבעי — הוכחה 1:**
>
> | # | טענה | הצדקה |
> |---|------|--------|
> | 1 | $T(0)=0$ | $T$ לינארית (הגדרה 1.2) |
> | 2 | $T(0)=0=\lambda\cdot 0$ | אריתמטיקה |
> | 3 | $0\in V_\lambda$ | שורות 1–2 + הגדרת $V_\lambda$ |
> | 4 | יהיו $v,u\in V_\lambda$: $Tv=\lambda v$, $Tu=\lambda u$ | הגדרת $V_\lambda$ |
> | 5 | $T(v+u)=Tv+Tu$ | לינאריות של $T$ |
> | 6 | $Tv+Tu=\lambda v+\lambda u=\lambda(v+u)$ | שורה 4; דיסטריבוטיביות |
> | 7 | $v+u\in V_\lambda$ | שורות 5–6 + הגדרת $V_\lambda$ |
> | 8 | יהי $v\in V_\lambda$, $c\in F$: $Tv=\lambda v$ | הגדרת $V_\lambda$ |
> | 9 | $T(cv)=c(Tv)=c(\lambda v)=\lambda(cv)$ | לינאריות של $T$; שורה 8 |
> | 10 | $cv\in V_\lambda$ | שורה 9 + הגדרת $V_\lambda$ |
> | 11 | $V_\lambda$ תת-מרחב | קריטריון תת-מרחב + שורות 3, 7, 10 |
>
> **ניכוי טבעי — הוכחה 2:**
>
> | # | טענה | הצדקה |
> |---|------|--------|
> | 1 | $v\in V_\lambda \iff Tv=\lambda v$ | הגדרת $V_\lambda$ |
> | 2 | $Tv=\lambda v \iff Tv-\lambda v=0 \iff (T-\lambda I)v=0$ | אריתמטיקת טרנספורמציה לינארית; $(\lambda I)v=\lambda v$ |
> | 3 | $V_\lambda=\ker(T-\lambda I)$ | שורות 1–2 |
> | 4 | $T-\lambda I$ היא טרנספורמציה לינארית | צירוף לינארי של טרנספורמציה לינארית |
> | 5 | גרעין של כל טרנספורמציה לינארית הוא תת-מרחב | משפט מלינארית 1 |
> | 6 | $V_\lambda$ תת-מרחב | שורות 3, 5 |




a. the table orientation should be left to right: step number, claim, justification. currently the table is mapped like hebrew, but the table should be in "mathematical language", which is left to right and not right to left.
b. change "הצדקה" to "נימוק"
c. every claim should be in english (e.g. use "let" instead of "יהי")
d. equal signs and algebraic manipulations may sometimes take several substeps. we want each substep in a new line, with its own explanation. The substeps should be numbered "x.y", when x is the step number, and y is the substep number. substep "x.0" should look like "T(v+u) = ", and every substep afterward should look like "= ...".

Take the card above and create a fixed copy of it using the instructions given here:

> [!abstract] טענה 1.5 — $V_\lambda$ הוא תת-מרחב
> $V_\lambda$ הינו תת-מרחב וקטורי של $V$.
>
> **הוכחה 1 (שלושה תנאים):** נבדוק שלושה תנאים:
> - $0\in V_\lambda$ ✓
> - סגירות תחת כפל בסקלר: הוכחנו בהערה 1.4 ✓
> - סגירות תחת חיבור: לכל $v,u\in V_\lambda$ מתקיים $T(v+u)=Tv+Tu=\lambda v+\lambda u=\lambda(v+u)$ ✓
>
> **הוכחה 2 (גרעין):** $V_\lambda=\ker(T-\lambda I)$, וגרעין של כל טרנספורמציה לינארית הינו תת-מרחב. $\blacksquare$

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
