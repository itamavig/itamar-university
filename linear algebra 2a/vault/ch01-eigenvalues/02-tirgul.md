---
title: "פרק 1 — תרגול: ערכים עצמיים ולכסון ושורשי יחידה"
chapter: ch01
type: tirgul
status: tirgul-done
---

# תרגול 1 — ערכים עצמיים ולכסון

## § ערכים עצמיים ולכסון

> [!abstract] הגדרה — ערך עצמי, וקטור עצמי, מרחב עצמי, לכסינות
> יהי $V$ מרחב וקטורי מעל $F$ ותהא $T : V \to V$ העתקה לינארית. $\lambda \in F$ נקרא **ערך עצמי** (ע"ע בקיצור) של $T$ אם קיים וקטור $0 \ne v \in V$ כך ש-
> $$T v = \lambda v.$$
> כל וקטור כנ"ל נקרא **וקטור עצמי** (ו"ע בקיצור) המתאים ל-$\lambda$. עבור ע"ע $\lambda$ נסמן
> $$V_\lambda = \{v \in V \mid T v = \lambda v\},$$
> זהו תת-מרחב וקטורי הנקרא **המרחב העצמי** המתאים ל-$\lambda$. ממדו נקרא **הריבוי הגיאומטרי** (ר"ג בקיצור) של $\lambda$. אם ל-$T$ יש בסיס המורכב כולו מו"ע של $T$, היא נקראת **לכסינה**, ובסיס כזה (לא יחיד!) נקרא **מלכסן**.

---

> [!example] דוגמאות
>
> **דוגמה 1.** תהא $T : \mathbb{R}^2 \to \mathbb{R}^2$ המוגדרת על ידי
> $$T\begin{pmatrix}x\\y\end{pmatrix} = \begin{pmatrix}2x+y\\x+2y\end{pmatrix}.$$
>
> וקטור עצמי $v_\lambda = \begin{pmatrix}x\\y\end{pmatrix}$ יקיים:
> $$\begin{pmatrix}\lambda x\\\lambda y\end{pmatrix} = \begin{pmatrix}2x+y\\x+2y\end{pmatrix} \iff \begin{cases}(2-\lambda)x + y = 0\\ x + (2-\lambda)y = 0\end{cases} \iff \begin{cases}(2-\lambda)x + y = 0\\(-3+4\lambda-\lambda^2)y = 0.\end{cases}$$
>
> אם $-3+4\lambda-\lambda^2 \ne 0$ אין פתרונות לא-טריוויאליים, ולכן אין ו"ע המתאימים לע"ע שאינם שורשים של
> $$-3+4x-x^2 = -(x-1)(x-3).$$
> עבור $\lambda = 1, 3$ ישנם פתרונות לא-טריוויאליים:
> $$\lambda = 1 \;\Rightarrow\; x + y = 0 \;\Rightarrow\; V_1 = \operatorname{Sp}\!\left\{\begin{pmatrix}1\\-1\end{pmatrix}\right\},$$
> $$\lambda = 3 \;\Rightarrow\; x - y = 0 \;\Rightarrow\; V_3 = \operatorname{Sp}\!\left\{\begin{pmatrix}1\\1\end{pmatrix}\right\}.$$
> לכן $T$ לכסינה ($\{v_1, v_3\}$ בסיס מלכסן).
>
> שימו לב: הפולינום $x^2 - 4x + 3$ נקרא **הפולינום האופייני** של $T$; נפגוש אותו עוד רבות.
>
> ---
>
> **דוגמה 2.** תהא $T : F^2 \to F^2$ המוגדרת על ידי
> $$T\begin{pmatrix}x\\y\end{pmatrix} = \begin{pmatrix}x+y\\y\end{pmatrix}.$$
>
> ו"ע $v_\lambda = \begin{pmatrix}x\\y\end{pmatrix}$ יקיים:
> $$\begin{pmatrix}\lambda x\\\lambda y\end{pmatrix} = \begin{pmatrix}x+y\\y\end{pmatrix} \iff \begin{cases}(1-\lambda)x + y = 0\\(1-\lambda)y = 0.\end{cases}$$
>
> עבור $\lambda \ne 1$ המערכת בדרגה מלאה ולכן אין ו"ע המתאימים לע"ע פרט ל-$\lambda = 1$. עבור $\lambda = 1$:
> $$y = 0 \;\Rightarrow\; V_1 = \operatorname{Sp}\!\left\{\begin{pmatrix}1\\0\end{pmatrix}\right\}.$$
> ולכן $T$ **אינה לכסינה** (לא קיים בסיס מלכסן).
>
> ---
>
> **דוגמה 3.** תהא $T : F^2 \to F^2$ המוגדרת על ידי
> $$T\begin{pmatrix}x\\y\end{pmatrix} = \begin{pmatrix}y\\-x\end{pmatrix}.$$
>
> ו"ע $v_\lambda = \begin{pmatrix}x\\y\end{pmatrix}$ יקיים:
> $$\begin{cases}-\lambda x + y = 0\\ -x - \lambda y = 0\end{cases} \xrightarrow{R_1 \leftrightarrow R_2,\; R_2 \to R_2 + \lambda R_1} \begin{cases}x + \lambda y = 0\\(\lambda^2+1)y = 0.\end{cases}$$
>
> $\lambda$ הוא ע"ע אם ורק אם הוא פתרון של $x^2 + 1 = 0$. יש חשיבות לשדה:
> - אם $F = \mathbb{R}$: מכיוון ש-$\lambda^2 + 1 > 0$ לכל $\lambda \in \mathbb{R}$, אין ע"ע ל-$T$.
> - אם $F = \mathbb{C}$: הע"ע הם $\pm i$ עם הו"ע המתאימים
> $$v_i = \begin{pmatrix}-i\\1\end{pmatrix}, \qquad v_{-i} = \begin{pmatrix}i\\1\end{pmatrix}.$$
>
> ---
>
> **דוגמה 4.** נראה עוד דוגמה שבה לשדה יש חשיבות — וגם דוגמה לטענה שתופיע בהמשך. תהא $T : F^4 \to F^4$ המוגדרת על ידי
> $$T\begin{pmatrix}x_1\\x_2\\x_3\\x_4\end{pmatrix} = \begin{pmatrix}x_4\\x_1\\x_2\\x_3\end{pmatrix}.$$
>
> אם $v_\lambda = (x_1, x_2, x_3, x_4)^T$ הוא ו"ע עם ע"ע $\lambda$, אז
> $$\lambda\begin{pmatrix}x_1\\x_2\\x_3\\x_4\end{pmatrix} = \begin{pmatrix}x_4\\x_1\\x_2\\x_3\end{pmatrix} \;\Rightarrow\; x_4 = \lambda x_1 = \lambda^2 x_2 = \lambda^3 x_3 = \lambda^4 x_4.$$
>
> כלומר, או ש-$x_4 = 0$ או ש-$\lambda^4 = 1$. האפשרות הראשונה לא תתן ו"ע (אז $V_\lambda$ הוא וקטור האפס). האפשרות השנייה נותנת:
> $$V_\lambda = \operatorname{Sp}\!\left\{\begin{pmatrix}\lambda^3\\\lambda^2\\\lambda\\1\end{pmatrix}\right\},$$
> שממדו (הר"ג של $\lambda$) הוא $1$. כעת נפריד לפי שדה הבסיס:
> - אם $F = \mathbb{R}$: למשוואה $\lambda^4 = 1$ יש $2$ פתרונות, $\pm 1$, כל אחד עם ר"ג $1$, וההעתקה **לא לכסינה**.
> - אם $F = \mathbb{C}$: יש $4$ פתרונות, $\pm 1, \pm i$. לכן מעל $\mathbb{C}$ ל-$T$ יש $4$ ע"ע שונים; הו"ע המתאימים הם
> $$v_1 = \begin{pmatrix}1\\1\\1\\1\end{pmatrix}, \quad v_{-1} = \begin{pmatrix}-1\\1\\-1\\1\end{pmatrix}, \quad v_i = \begin{pmatrix}-i\\-1\\i\\1\end{pmatrix}, \quad v_{-i} = \begin{pmatrix}i\\-1\\-i\\1\end{pmatrix},$$
> והם יוצרים בסיס ל-$\mathbb{C}^4$, כלומר $T$ **לכסינה**.

---

> [!abstract] טענה — ערך עצמי $0$ וחח"ע
> תהא $T : V \to V$ העתקה לינארית. ל-$T$ ע"ע $0$ אם ורק אם $T$ אינה חח"ע.

> [!proof]- הוכחה
> התנאי "ל-$T$ יש ע"ע $\lambda = 0$" מתרגם לקיום וקטור $v \ne 0$ עם $Tv = \lambda v = 0$, כלומר לכך ש-$\ker T$ אינו טריוויאלי, מה ששקול לכך ש-$T$ אינה חח"ע.

---

> [!abstract] משפט (מההרצאה) — בלתי-תלות של וקטורים עצמיים עם ע"ע שונים
> תהא $T : V \to V$ העתקה לינארית ויהיו $v_1, \ldots, v_k$ ו"ע של $T$ עם ע"ע שונים. אז $\{v_1, \ldots, v_k\}$ בלתי-תלויים לינארית.

---

> [!abstract] מסקנה
> 1. ל-$T : V \to V$ יש לכל היותר $\dim V$ ע"ע שונים.
> 2. אם ל-$T$ יש $\dim V$ ע"ע שונים, אז $T$ לכסינה.

---

## § שורשי יחידה

> [!abstract] הגדרה — שורש יחידה
> יהי $F$ שדה ו-$m \in \mathbb{N}$. איבר $\zeta \in F$ יקרא **שורש יחידה מסדר $m$** אם $\zeta^m = 1$.

---

> [!note] הערה
> יהי $\zeta \in F$ שורש יחידה מסדר $m$ ו-$d \in \mathbb{Z}$. אז $\zeta^d \in F$ הוא שורש יחידה מסדר $m$, מכיוון ש-$(\zeta^d)^m = \zeta^{md} = 1^d = 1$.

---

> [!example] דוגמאות — שורשי יחידה
>
> 1. עבור $F = \mathbb{C}$: $\zeta = e^{2\pi i/m} = \cos\!\left(\tfrac{2\pi}{m}\right) + i\sin\!\left(\tfrac{2\pi}{m}\right)$ הוא שורש יחידה מסדר $m$. כל שורש יחידה מסדר $m$ ב-$\mathbb{C}$ הוא מהצורה $\zeta^k$ עבור $k = 0, \ldots, m-1$.
>
> 2. עבור $F = \mathbb{R}$: המספר $1$ הוא שורש יחידה מסדר $1$, המספר $-1$ הוא שורש יחידה מסדר $2$, ואין עוד שורשי יחידה.
>
> 3. אם $p \in \mathbb{N}$ ראשוני, אז המספרים מודולו $p$ מהווים שדה, נסמנו ב-$\mathbb{F}_p$. בשיעורי הבית תראו שלכל $0 \ne a \in \mathbb{F}_p$ מתקיים $a^{p-1} = 1$, כלומר כל $a \in \mathbb{F}_p \setminus \{0\}$ הוא שורש יחידה מסדר $p-1$.

---

> [!abstract] הגדרה — תת-מרחב שמור וצמצום
> יהי $V$ מרחב וקטורי מעל $F$ ו-$T : V \to V$ העתקה לינארית. תת-מרחב $W \subseteq V$ נקרא **$T$-שמור** אם $T(W) \subseteq W$. במקרה זה קיימת ויחידה העתקה לינארית $T|_W : W \to W$ כך ש-$T|_W(w) = T(w)$ לכל $w \in W$, הנקראת **הצמצום** של $T$ ל-$W$.

---

> [!abstract] טענה — ע"ע של צמצום לתת-מרחב שנוצר על ידי מסלול
> יהי $V$ מרחב וקטורי מעל $F$, $f \in V$, ותהא $T : V \to V$ העתקה לינארית עבורה $T^n f = f$ וגם $\{f, Tf, \ldots, T^{n-1}f\}$ בלתי-תלויים לינארית. נסמן $W = \operatorname{Sp}\{f, Tf, \ldots, T^{n-1}f\}$. אז:
>
> 1. $W$ הוא $T$-שמור, כל ע"ע של $T|_W$ הוא שורש יחידה מסדר $n$, וכל שורש יחידה מסדר $n$ ב-$F$ הוא ע"ע עם ריבוי גיאומטרי $1$.
>
> 2. אם ב-$F$ יש $n$ שורשי יחידה שונים מסדר $n$, אז $T|_W$ לכסינה. במקרה זה, אם $B = \{v_1, \ldots, v_n\} \subset W$ בסיס מלכסן, אז כל הקואורדינטות של $[f]_B$ שונות מ-$0$.

---

> [!example] דוגמה — התמורה המחזורית ב-$\mathbb{C}^n$
> עבור $T : \mathbb{C}^n \to \mathbb{C}^n$ המוגדרת על ידי
> $$T(e_i) = \begin{cases}e_n & i = 1\\ e_{i-1} & i > 1,\end{cases}$$
> נבחין שתנאי הטענה מתקיימים (עבור $f = e_1$). עבור $\zeta = e^{2\pi i/n}$ שורש יחידה מסדר $n$, הוקטור
> $$w_k = \begin{pmatrix}1\\ \zeta^k\\ \zeta^{2k}\\ \vdots\\ \zeta^{(n-1)k}\end{pmatrix}$$
> הוא וקטור עצמי לערך העצמי $\zeta^k$, לכל $0 \le k \le n-1$ (ודאו זאת). כמו כן
> $$e_1 = \frac{1}{n}\sum_{k=0}^{n-1} w_k,$$
> כלומר כל המקדמים שונים מ-$0$.

> [!proof]- הוכחת הטענה
> **חלק 1 — $W$ שמור וע"ע הם שורשי יחידה.**
>
> יהי $w \in W$. הוא ניתן להצגה כ-$w = \sum_{i=0}^{n-1} \alpha_i T^i f$. לכן
> $$Tw = \alpha_{n-1} f + \sum_{i=0}^{n-2} \alpha_i T^{i+1} f \in W,$$
> כלומר $W$ הוא $T$-שמור.
>
> נחפש ע"ע של $T|_W$. נניח ש-$0 \ne w = \sum_{i=0}^{n-1} \alpha_i T^i f \in W$ הוא ו"ע עם ע"ע $\lambda$. ראשית, $T|_W$ הפיכה (היא מעבירה את הבסיס $\{f, Tf, \ldots, T^{n-1}f\}$ לבסיס $\{Tf, T^2f, \ldots, T^n f = f\}$), ולכן $\lambda \ne 0$. כעת:
> $$\sum_{i=0}^{n-1} \lambda\alpha_i T^i f = \lambda w = Tw = \alpha_{n-1} f + \sum_{i=1}^{n-1} \alpha_{i-1} T^i f.$$
> מהנחת הבלתי-תלות של $\{f, Tf, \ldots, T^{n-1}f\}$, המקדמים בשני האגפים שווים:
> $$\alpha_{i-1} = \lambda\alpha_i \;\Rightarrow\; \alpha_i = \lambda^{-i}\alpha_0,$$
> לכל $i$, וגם $\lambda\alpha_0 = \alpha_{n-1}$. לכן
> $$\lambda\alpha_0 = \alpha_{n-1} = \lambda^{1-n}\alpha_0 \;\Rightarrow\; (\lambda^n - 1)\alpha_0 = 0 \;\Rightarrow\; \lambda^n = 1.$$
> כלומר, $\lambda$ הוא ע"ע אם ורק אם הוא שורש יחידה מסדר $n$, וכל שורש יחידה הוא ע"ע עם מרחב עצמי ממד $1$ (ר"ג הוא $1$).
>
> **חלק 2 — לכסינות וקואורדינטות שונות מאפס.**
>
> יהיו $\lambda_1, \ldots, \lambda_n \in F$ שורשי היחידה השונים מסדר $n$. מכיוון של-$T|_W$ יש $n$ ע"ע שונים, היא לכסינה. נרשום $f = \sum_{i=1}^n \alpha_i v_i$ כאשר $v_i$ הוא ו"ע עם ע"ע $\lambda_i$. נניח בשלילה ש-$\alpha_k = 0$ עבור איזשהו $1 \le k \le n$, בלי הגבלת הכלליות $k = n$. אז לכל $0 \le m \le n-1$:
> $$T^m f = T^m\!\left(\sum_{i=1}^{n-1} \alpha_i v_i\right) = \sum_{i=1}^{n-1} \alpha_i \lambda_i^m v_i \;\in\; \operatorname{Sp}\{v_1, \ldots, v_{n-1}\}.$$
> לכן $W = \operatorname{Sp}\{f, Tf, \ldots, T^{n-1}f\} \subseteq \operatorname{Sp}\{v_1, \ldots, v_{n-1}\}$, כלומר ממד $W$ הוא לכל היותר $n-1$. זו סתירה לכך ש-$f, Tf, \ldots, T^{n-1}f$ בלתי-תלויים לינארית.

---

## § השערת ארדש

> [!abstract] השערת ארדש
> יהיו $\left(a_1^{(k)}\right)_{k\in\mathbb{Z}},\, \left(a_2^{(k)}\right)_{k\in\mathbb{Z}},\, \ldots,\, \left(a_n^{(k)}\right)_{k\in\mathbb{Z}}$ סדרות חשבוניות אין-סופיות דו-צדדיות של מספרים שלמים (האינדקס העליון מסמן המיקום בסדרה והתחתון את הסדרה). נתון שכל מספר שלם מופיע בדיוק בסדרה אחת (פעם אחת). אז קיימות $2$ סדרות עם הפרש זהה.

> [!example] דוגמה — חלוקה המקיימת את התנאי
> הסדרות
> $$(2k)_{k\in\mathbb{Z}} = (\ldots, -2, 0, 2, 4, \ldots),$$
> $$(4k+1)_{k\in\mathbb{Z}} = (\ldots, -3, 1, 5, \ldots),$$
> $$(4k-1)_{k\in\mathbb{Z}} = (\ldots, -1, 3, 7, \ldots)$$
> מקיימות את התנאי (כל מספר שלם מופיע בדיוק פעם אחת). הפרשי הסדרות הם $2, 4, 4$ — ויש שתי סדרות עם הפרש זהה ($4$).

> [!proof]- הוכחת השערת ארדש באמצעות אלגברה לינארית
> נסמן $a_i^{(k)} = a_i^{(0)} + k \cdot d_i$. בלי הגבלת הכלליות נניח ש-$d_1 \ge d_2 \ge \cdots \ge d_n$. נוכיח ש-$d_1 = d_2$.
>
> **תרגום לאלגברה לינארית.** נתבונן במרחב $V$ של סדרות מרוכבות עם אינדקסים שלמים (סכום וכפל בסקלר נקודתית). נתבונן בהעתקת ההזזה $T : V \to V$ המוגדרת על ידי
> $$T\!\left(\left(b^{(k)}\right)_{k\in\mathbb{Z}}\right) = \left(b^{(k-1)}\right)_{k\in\mathbb{Z}}.$$
>
> לכל סדרה $\left(a_i^{(k)}\right)_{k\in\mathbb{Z}}$ נגדיר **סדרה מונה**:
> $$f_i^{(k)} = \begin{cases}1 & k \equiv a_i^{(0)} \pmod{d_i}\\ 0 & \text{אחרת.}\end{cases}$$
>
> מהנתון שכל מספר שלם מופיע בדיוק בסדרה אחת, מתקיים $\sum_{i=1}^n f_i = \mathbf{1}$, כאשר $\mathbf{1}$ היא הסדרה הקבועה $\mathbf{1}^{(k)} = 1$. כמו כן $T^{d_i} f_i = f_i$ לכל $1 \le i \le n$, וגם הוקטורים $\{T^j f_i \mid 0 \le j < d_i\}$ בלתי-תלויים לינארית.
>
> נסמן $\zeta_{i,k} = \zeta_{d_i}^k$ כאשר $\zeta_{d_i}$ שורש יחידה מסדר $d_i$. מהטענה הקודמת, קיימים וקטורים עצמיים $w_{i,k} \in \operatorname{Sp}\{T^j f_i \mid 0 \le j < d_i\}$ המתאימים לע"ע $\zeta_{i,k}$, ו-
> $$f_i = \sum_{k=0}^{d_i-1} \alpha_{i,k}\, w_{i,k}$$
> כאשר $\alpha_{i,k} \ne 0$ לכל $k$. בלי הגבלת הכלליות נניח ש-$w_{i,0} = \mathbf{1}$ לכל $i$ (ניתן להניח זאת מכיוון ש-$\zeta_{i,0} = 1$ הוא ע"ע, ו-$\mathbf{1} \in \operatorname{Sp}\{T^j f_i \mid 0 \le j < d_i\}$ הוא וקטור עצמי המתאים לו). לכן:
> $$0 = \sum_{i=1}^n f_i - \mathbf{1} = \sum_{i=1}^n\sum_{k=0}^{d_i-1} \alpha_{i,k}\, w_{i,k} - \mathbf{1} = -1 + \sum_{i=1}^n \alpha_{i,0}\cdot\mathbf{1} + \sum_{i=1}^n\sum_{k=1}^{d_i-1} \alpha_{i,k}\, w_{i,k}.$$
>
> **הגעה לסתירה.** נניח בשלילה ש-$d_1 > d_i$ לכל $i > 1$ (כלומר, שלא קיימות שתי סדרות עם הפרש זהה ל-$d_1$). אז $\zeta_{d_1}^1 \ne \zeta_{d_i}^k$ לכל $(i,k) \ne (1,1)$, ולכן $w_{1,1}$ משתתף בסכום רק פעם אחת. המקדם של $w_{1,1}$ במשוואה הוא $\alpha_{1,1} \ne 0$, כלומר קיימת תלות לינארית לא-טריוויאלית של קבוצת הוקטורים $\{w_{i,k} \mid 1 \le i \le n,\, 0 \le k \le d_i - 1\}$. אבל אלו וקטורים עצמיים של ע"ע שונים, ולכן הם בלתי-תלויים לינארית — סתירה. לכן $d_1 = d_2$.
