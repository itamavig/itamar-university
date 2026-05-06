---
title: "פרק 11 — צורות בילינאריות, צורות ריבועיות ומרחבי מכפלה פנימית: הרצאה"
chapter: ch11-inner-product
source: lecture-yehuda
status: lecture-done
tags: [la2, lecture, ch11-inner-product]
---

# צורות בילינאריות, צורות ריבועיות ומרחבי מכפלה פנימית — הרצאה

> [!info] מקור
> פרקים 11–13 מתוך הרצאות יהודה שלום, עמ' 43–65.

---

## פרק 11 — צורות בילינאריות

### הגדרות בסיסיות

> [!abstract] הגדרה 11.1 — פונקציונל לינארי
> **פונקציונל לינארי** על $V$ הוא העתקה לינארית $f : V \to F$.

> [!abstract] הגדרה 11.2 — צורה בילינארית
> תהיינה $V, W$ מ"ו מעל $F$. **צורה בילינארית** היא פונקציה $f : V \times W \to F$ המקיימת:
> - לינאריות בארגומנט הראשון: $f(u + v, w) = f(u,w) + f(v,w)$, $f(\alpha v, w) = \alpha f(v,w)$
> - לינאריות בארגומנט השני: $f(v, u + w) = f(v,u) + f(v,w)$, $f(v, \alpha w) = \alpha f(v,w)$

> [!example] דוגמאות 11.3–11.4
> - $f : \mathbb{R}^n \times \mathbb{R}^n \to \mathbb{R}$, $f(v,w) = v^t w$ (המכפלה הפנימית הסטנדרטית)
> - $f : M_n(F) \times M_n(F) \to F$, $f(A,B) = \mathrm{tr}(AB)$
> - $f : F^n \times F^m \to F$, $f(v,w) = v^t A w$ עבור מטריצה $A \in M_{n \times m}(F)$

> [!abstract] טענה 11.5
> $B(V,W) = \{$צורות בילינאריות $f : V \times W \to F\}$ הוא מ"ו מעל $F$ עם פעולות טבעיות.

---

### מטריצה המייצגת

> [!abstract] הגדרה 11.7 — מטריצה מייצגת
> יהיו $B = (v_1, \ldots, v_n)$ בסיס ל-$V$ ו-$C = (w_1, \ldots, w_m)$ בסיס ל-$W$. המטריצה המייצגת של $f$ ביחס ל-$B, C$ היא:
> $$[f]_{B,C} = A \in M_{n \times m}(F), \quad a_{ij} = f(v_i, w_j).$$

> [!abstract] משפט 11.8
> לכל $v \in V$, $w \in W$:
> $$f(v,w) = [v]_B^t \cdot A \cdot [w]_C.$$

> [!abstract] משפט 11.9 — איזומורפיזם
> ההעתקה $M : B(V,W) \to M_{n \times m}(F)$, $f \mapsto [f]_{B,C}$ היא איזומורפיזם של מ"ו. בפרט, $\dim B(V,W) = nm$.

---

### החלפת בסיס

> [!abstract] משפט 11.10 — נוסחת החלפת בסיס
> יהיו $B, B'$ בסיסים ל-$V$ ו-$C, C'$ בסיסים ל-$W$. אם $P = [I]_{B'}^B$ ו-$Q = [I]_{C'}^C$ מטריצות המעבר, אז:
> $$[f]_{B',C'} = P^t \cdot [f]_{B,C} \cdot Q.$$

> [!abstract] מסקנה 11.13 — דרגת צורה בילינארית
> **הדרגה** של $f$ מוגדרת כ-$\mathrm{rank}(A)$ ואינה תלויה בבחירת הבסיסים (כי $\mathrm{rank}(P^t AQ) = \mathrm{rank}(A)$ כשהמטריצות הפיכות).

> [!abstract] מסקנה 11.14 — צורה קנונית
> לכל צורה בילינארית $f$ מדרגה $r$ קיים בסיס שבו המטריצה המייצגת היא:
> $$\begin{pmatrix} I_r & 0 \\ 0 & 0 \end{pmatrix}.$$

---

### צורות על $V \times V$

> [!abstract] מסקנה 11.15 — החלפת בסיס על $V \times V$
> עבור $f : V \times V \to F$, אם $P$ מטריצת המעבר מ-$B'$ ל-$B$:
> $$[f]_{B'} = P^t \cdot [f]_B \cdot P.$$

> [!abstract] הגדרה 11.16 — מטריצות חופפות (congruent)
> $A, C \in M_n(F)$ **חופפות** אם קיימת $P$ הפיכה כך ש-$C = P^t A P$.

> [!abstract] טענה 11.17
> אם $A' = P^t AP$ (מטריצות חופפות), אז:
> 1. $\mathrm{rank}(A') = \mathrm{rank}(A)$
> 2. $\det(A') = (\det P)^2 \cdot \det(A)$

> [!abstract] הגדרה 11.18 — סימטריות
> $f : V \times V \to F$ היא:
> - **סימטרית** אם $f(v,u) = f(u,v)$ לכל $v,u$
> - **אנטי-סימטרית** אם $f(v,u) = -f(u,v)$ לכל $v,u$

> [!abstract] משפט 11.19
> $f$ סימטרית $\iff$ $[f]_B$ מטריצה סימטרית (עבור בסיס כלשהו, ולכן לכל בסיס).

---

## פרק 12 — צורות ריבועיות

> [!abstract] הגדרה 12.1 — צורה ריבועית
> תהי $f : V \times V \to F$ צורה בילינארית סימטרית. **הצורה הריבועית** המשורשרת היא:
> $$Q_f : V \to F, \quad Q_f(v) = f(v,v).$$

> [!example] דוגמה 12.2
> ב-$\mathbb{R}^2$: $f((x_1,x_2),(y_1,y_2)) = 2x_1y_1 - x_1y_2 - x_2y_1 + 3x_2y_2$ נותן $Q_f(x_1,x_2) = 2x_1^2 - 2x_1x_2 + 3x_2^2$.

> [!abstract] משפט 12.3 — שחזור $f$ מ-$Q_f$
> אם $\mathrm{char}(F) \ne 2$, ניתן לשחזר את $f$ מ-$Q_f$:
> $$f(v,w) = \frac{Q_f(v+w) - Q_f(v) - Q_f(w)}{2}.$$

---

### לכסון צורה ריבועית

> [!abstract] משפט 12.5 — לכסון על בסיס אורתוגונלי
> תהי $f : V \times V \to F$ סימטרית, $\mathrm{char}(F) \ne 2$. אז קיים בסיס $B$ של $V$ שבו:
> $$[f]_B = \mathrm{diag}(d_1, \ldots, d_n).$$

> [!note]- הוכחה
> באינדוקציה על $\dim V$.
>
> **בסיס האינדוקציה:** $\dim V = 0$ — ברור.
>
> **צעד האינדוקציה:** אם $f \equiv 0$ — כל בסיס עובד. אחרת, קיים $v$ עם $f(v,v) \ne 0$ (למה: אם $f(v,v)=0$ לכל $v$, מ-12.3 נובע $f(v,w)=0$ לכל $v,w$, סתירה). נגדיר $e_1 = v$ ונסתכל על:
> $$e_1^\perp = \{w \in V \mid f(e_1, w) = 0\}.$$
> $e_1^\perp$ תת-מרחב, $V = \mathrm{Sp}\{e_1\} \oplus e_1^\perp$ (כי $w = \frac{f(e_1,w)}{f(e_1,e_1)} e_1 + (w - \ldots)$). מאינדוקציה על $e_1^\perp$ מסיימים. $\square$

---

### צורות קנוניות

> [!abstract] משפט 12.6 — מעל $F = \mathbb{C}$
> כל צורה ריבועית מדרגה $r$ מייוצגת (על בסיס מתאים) על ידי:
> $$\mathrm{diag}(\underbrace{1,\ldots,1}_{r}, 0, \ldots, 0).$$

> [!abstract] משפט 12.7 — מעל $F = \mathbb{R}$
> כל צורה ריבועית מייוצגת (על בסיס מתאים) על ידי:
> $$\mathrm{diag}(\underbrace{1,\ldots,1}_{p}, \underbrace{-1,\ldots,-1}_{q}, 0, \ldots, 0).$$
> הזוג $(p, q)$ נקרא **חתימת** הצורה.

---

### חיוביות ושליליות

> [!abstract] הגדרה 12.10 — חיוביות ושליליות
> צורה ריבועית $Q : V \to \mathbb{R}$ היא:
> - **חיובית לחלוטין** (positive definite) אם $Q(v) > 0$ לכל $v \ne 0$
> - **שלילית לחלוטין** (negative definite) אם $Q(v) < 0$ לכל $v \ne 0$
> - **חיובית למחצה** (positive semidefinite) אם $Q(v) \ge 0$ לכל $v$
> - **שלילית למחצה** (negative semidefinite) אם $Q(v) \le 0$ לכל $v$
> - **אינה מוגדרת** (indefinite) אחרת

> [!abstract] טענה 12.11 — אפיון על פי חתימה
> אם $[f]_B = \mathrm{diag}(d_1, \ldots, d_n)$, אז:
> - $Q_f$ חיובית לחלוטין $\iff$ $d_i > 0$ לכל $i$
> - $Q_f$ חיובית למחצה $\iff$ $d_i \ge 0$ לכל $i$
> - (ובאופן דומה עבור שלילית לחלוטין/למחצה)

---

### חוק האינרציה של סילבסטר

> [!abstract] משפט 12.12 — חוק האינרציה של סילבסטר
> מעל $\mathbb{R}$: החתימה $(p, q)$ אינה תלויה בבחירת הבסיס — היא אינווריאנט של הצורה.

> [!note]- הוכחה
> נניח שני בסיסים נותנים חתימות $(p, q)$ ו-$(p', q')$. נראה $p = p'$.
>
> יהי $U = \mathrm{Sp}\{u_1, \ldots, u_p\}$ (כיוונים חיוביים בבסיס הראשון, $Q(u) > 0$ לכל $0 \ne u \in U$) ו-$W = \mathrm{Sp}\{w_{p'+1}, \ldots, w_n\}$ (כיוונים שאינם חיוביים בבסיס השני, $Q(w) \le 0$ לכל $w \in W$).
>
> אם $p > p'$ אז $\dim U + \dim W = p + (n - p') > n$, לכן $U \cap W \ne \{0\}$. אבל $v \in U \cap W \setminus \{0\}$ נותן $Q(v) > 0$ וגם $Q(v) \le 0$ — סתירה. לכן $p \le p'$, וסימטרית $p' \le p$. $\square$

---

## פרק 13 — מרחבי מכפלה פנימית

### הגדרות

> [!abstract] הגדרה 13.1 — מכפלה פנימית מעל $\mathbb{R}$
> **מכפלה פנימית** על מ"ו $V$ מעל $\mathbb{R}$ היא צורה בילינארית סימטרית וחיובית לחלוטין $\langle \cdot, \cdot \rangle : V \times V \to \mathbb{R}$.

> [!example] דוגמאות 13.2–13.4
> - **סטנדרטית על $\mathbb{R}^n$:** $\langle v, u \rangle = v^t u = \sum v_i u_i$
> - **על $M_n(\mathbb{R})$:** $\langle A, B \rangle = \mathrm{tr}(AB^t)$
> - **על $C[0,1]$:** $\langle f, g \rangle = \int_0^1 f(t) g(t)\, dt$

> [!abstract] הגדרה 13.5 — מכפלה פנימית מעל $\mathbb{C}$
> **מכפלה פנימית** על מ"ו $V$ מעל $\mathbb{C}$ היא $\langle \cdot, \cdot \rangle : V \times V \to \mathbb{C}$ המקיימת:
> - לינארית בארגומנט הראשון
> - **ססקווי-לינארית**: $\langle v, \alpha w \rangle = \overline{\alpha} \langle v, w \rangle$
> - הרמיטית: $\langle v, u \rangle = \overline{\langle u, v \rangle}$
> - חיובית לחלוטין: $\langle v, v \rangle \ge 0$, ושוויון $\iff$ $v = 0$

> [!example] דוגמאות 13.6–13.8
> - **סטנדרטית על $\mathbb{C}^n$:** $\langle v, u \rangle = \sum v_i \overline{u_i}$
> - **על $M_n(\mathbb{C})$:** $\langle A, B \rangle = \mathrm{tr}(AB^*)$ כאשר $B^* = \overline{B^t}$ (צמוד הרמיטי)

---

### נורמה ומרחק

> [!abstract] הגדרה 13.9 — נורמה
> **הנורמה** של $v$ היא $\|v\| = \sqrt{\langle v, v \rangle}$.

> [!note] תזכורת 13.10–13.11
> - **וקטור יחידה**: $\|v\| = 1$
> - **נרמול**: $\hat{v} = v / \|v\|$

---

### אי-שוויון קושי-שוורץ

> [!abstract] טענה 13.12 — אי-שוויון קושי-שוורץ
> לכל $v, u \in V$:
> $$|\langle v, u \rangle| \le \|v\| \cdot \|u\|,$$
> ושוויון $\iff$ $v, u$ תלויים לינארית.

> [!note]- הוכחה
> אם $u = 0$ — ברור. אחרת, נגדיר $t_0 = \langle v, u \rangle / \|u\|^2$ ונסתכל על:
> $$0 \le \|v - t_0 u\|^2 = \|v\|^2 - t_0 \overline{\langle v, u \rangle} - \overline{t_0} \langle v, u \rangle + |t_0|^2 \|u\|^2 = \|v\|^2 - \frac{|\langle v, u \rangle|^2}{\|u\|^2}.$$
> כפל ב-$\|u\|^2$ נותן את הטענה. שוויון $\iff$ $v = t_0 u$. $\square$

> [!abstract] טענה 13.14 — אי-שוויון המשולש
> $$\|v + u\| \le \|v\| + \|u\|.$$

> [!note]- הוכחה
> $\|v+u\|^2 = \|v\|^2 + 2\mathrm{Re}\langle v, u \rangle + \|u\|^2 \le \|v\|^2 + 2|\langle v,u \rangle| + \|u\|^2 \le (\|v\| + \|u\|)^2$. $\square$

---

### אורתוגונליות

> [!abstract] הגדרות 13.15–13.16
> - **מרחק**: $d(v, u) = \|v - u\|$
> - $v \perp u$ (אורתוגונליים) $\iff$ $\langle v, u \rangle = 0$

> [!abstract] טענה 13.19
> $v^\perp = \{u \in V \mid \langle v, u \rangle = 0\}$ הוא תת-מרחב של $V$.

> [!abstract] משפט פיתגורס 13.20–13.21
> $v \perp u \implies \|v + u\|^2 = \|v\|^2 + \|u\|^2$.
>
> בכלליות: אם $v_1, \ldots, v_k$ זוגית אורתוגונליים: $\left\|\sum_{i=1}^k v_i\right\|^2 = \sum_{i=1}^k \|v_i\|^2$.

---

### קבוצות אורתוגונליות ובסיסים

> [!abstract] הגדרה 13.22
> - קבוצה $\{v_i\}$ היא **אורתוגונלית** (OG) אם $\langle v_i, v_j \rangle = 0$ לכל $i \ne j$
> - **אורתונורמלית** (ON) אם בנוסף $\|v_i\| = 1$ לכל $i$

> [!abstract] טענה 13.25 — קואורדינטות ב-ONB
> אם $\{e_1, \ldots, e_n\}$ ON ו-$v = \sum a_i e_i$, אזי $a_i = \langle v, e_i \rangle$.
>
> **אי-שוויון בסל:** $\displaystyle\sum_{i=1}^k |\langle v, e_i \rangle|^2 \le \|v\|^2$.

> [!abstract] טענה 13.26
> כל מ"ו עם מכפלה פנימית ממימד סופי מכיל ONB.

---

### הטלה אורתוגונלית

> [!abstract] בעיה 13.27 — קירוב הכי טוב
> נתון תת-מרחב $U \subseteq V$ ו-$v \in V$. מצא $u_0 \in U$ הממזער את $\|v - u\|$ עבור $u \in U$.

> [!abstract] טענה 13.28 — הטלה אורתוגונלית
> יהי $\{e_1, \ldots, e_k\}$ ONB של $U$. אז הקירוב הטוב ביותר הוא:
> $$u_0 = P_U(v) = \sum_{i=1}^k \langle v, e_i \rangle e_i,$$
> ומתקיים $v - u_0 \perp U$.

> [!note]- הוכחה
> לכל $u \in U$: $\|v - u\|^2 = \|(v - u_0) + (u_0 - u)\|^2 = \|v - u_0\|^2 + \|u_0 - u\|^2 \ge \|v - u_0\|^2$, כיוון ש-$(v - u_0) \perp (u_0 - u)$. שוויון $\iff$ $u = u_0$. $\square$

> [!abstract] הגדרה 13.29
> $P_U : V \to V$ המוגדרת על ידי $v \mapsto u_0$ כנ"ל היא **ההטלה האורתוגונלית** על $U$.

---

### אלגוריתם גרם-שמידט

> [!abstract] טענה 13.30 — אלגוריתם גרם-שמידט
> נתון בסיס $(v_1, \ldots, v_n)$ של $V$. האלגוריתם הבא מייצר ONB $(e_1, \ldots, e_n)$:
>
> 1. $u_1 = v_1$, $e_1 = u_1 / \|u_1\|$
> 2. לכל $k = 2, \ldots, n$:
>    $$u_k = v_k - \sum_{i=1}^{k-1} \langle v_k, e_i \rangle e_i, \qquad e_k = u_k / \|u_k\|$$
>
> ומתקיים $\mathrm{Sp}\{e_1, \ldots, e_k\} = \mathrm{Sp}\{v_1, \ldots, v_k\}$ לכל $k$.

> [!note]- הוכחה (סקיצה)
> $u_k \ne 0$ כי $v_1, \ldots, v_k$ בת"ל ו-$u_k = v_k - P_{\mathrm{Sp}\{e_1,\ldots,e_{k-1}\}}(v_k)$. אורתוגונליות: $\langle e_k, e_j \rangle = 0$ לכל $j < k$ מבנייה. $\square$

---

[[02-tirgul|דוגמאות מהתרגול →]]  |  [[03-exercises|תרגילים →]]
