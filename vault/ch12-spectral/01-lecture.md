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

> [!abstract] מסקנה 14.8
> אם $T$ צמודה לעצמה ו-$p(x) \in \mathbb{R}[x]$ פולינום חיובי, אז $p(T)$ הפיכה.

---

### המשפט הספקטרלי — מקרה ממשי

> [!abstract] משפט 14.9
> אם $T : V \to V$ סימטרית ($F = \mathbb{R}$) אז $m_T(x)$ מתפרק למכפלת גורמים לינאריים מעל $\mathbb{R}$ (כל ע"ע של $T$ ממשי).

> [!note]- הוכחה
> נניח בשלילה כי גורם אי-פריק $p_1$ של $m_T$ מקיים $\deg p_1 \ge 2$. מכיוון ש-$p_1$ אי-פריק (לכן מתוקן) הוא חיובי, ולכן $p_1(T)$ הפיך. אבל $m_T(T) = p_1(T) \cdot g(T) = 0$ ולכן $g(T) = 0$, בסתירה למינימליות. $\square$

> [!abstract] טענה 14.10
> כל הגורמים הלינאריים של $m_T$ (לטרנס' סימטרית $T$) שונים זה מזה. בפרט, $T$ לכסינה.

> [!note]- הוכחה
> נניח בשלילה $(x - \lambda)^2 \mid m_T(x)$. אזי $(T - \lambda I)^2 g(T) = 0$ לכל $v$. מלמה 14.11 עם $w = g(T)v$: $(T - \lambda I)w = 0$. ולכן $(x - \lambda)g(x)$ מאפס את $T$ בסתירה למינימליות. $\square$

> [!abstract] למה 14.11
> אם $T$ סימטרית ו-$\lambda \in \mathbb{R}$: אם $(T - \lambda I)^2 v = 0$ אז $(T - \lambda I) v = 0$.

> [!note]- הוכחה
> $S = T - \lambda I$ גם צמודה לעצמה. אם $S^2 v = 0$ אז $0 = \langle S^2 v, v \rangle = \|Sv\|^2$, ולכן $Sv = 0$. $\square$

> [!abstract] משפט 14.13
> אם $T : V \to V$ סימטרית ($F = \mathbb{R}$) אז $m_T(x)$ מתפצל למכפלת גורמים לינאריים **שונים**, ולכן $T$ ניתנת ללכסון.

### ו"ע וניצביות

> [!abstract] טענה 14.14
> אם $T$ צמודה לעצמה ($F = \mathbb{R}$ או $\mathbb{C}$) ו-$Tv = \alpha v$, $Tu = \beta u$ עם $\alpha \ne \beta$, אזי $\langle v, u \rangle = 0$.

> [!note]- הוכחה
> $\alpha \langle v, u \rangle = \langle Tv, u \rangle = \langle v, Tu \rangle = \bar{\beta} \langle v, u \rangle$. אם $F = \mathbb{R}$: $\alpha \ne \beta$ ולכן $\langle v, u \rangle = 0$. אם $F = \mathbb{C}$: נשתמש בלמה 14.15. $\square$

> [!abstract] למה 14.15
> אם $T$ צמודה לעצמה אז כל ע"ע (אפילו מרוכב) ממשי.

> [!note]- הוכחה
> $Tu = \beta u \implies \beta \|u\|^2 = \langle Tu, u \rangle = \langle u, Tu \rangle = \bar{\beta} \|u\|^2 \implies \beta = \bar{\beta}$. $\square$

> [!abstract] משפט 14.16 — המשפט הספקטרלי (המקרה הסימטרי)
> תהי $T : V \to V$ סימטרית ($F = \mathbb{R}$). אזי קיים בסיס אורתונורמלי של $V$ המורכב מו"ע של $T$.

> [!note]- הוכחה
> הוכחנו ש-$T$ לכסינה (משפט 14.13). יהיו $\lambda_1, \ldots, \lambda_r$ הע"ע השונים ו-$V_{\lambda_i} = \ker(T - \lambda_i I)$. מלכסינות: $V = \bigoplus V_{\lambda_i}$.
>
> מטענה 14.14 (לעיל): ו"ע ממ"ע שונים ניצבים זה לזה. לכן בכל $V_{\lambda_i}$ בנפרד מפעילים גרם-שמידט לקבלת $B_i$ א"נ. $B = \bigcup B_i$ הוא בסיס א"נ של $V$. $\square$

> [!abstract] משפט 14.17 — הכיוון ההפוך
> אם ל-$T : V \to V$ קיים בסיס א"נ של ו"ע (כל $\lambda_i \in \mathbb{R}$), אז $T$ סימטרית.

> [!note]- הוכחה
> יהי $\{e_i\}$ בסיס א"נ, $Te_i = \lambda_i e_i$. לכל $v = \sum a_i e_i$, $u = \sum b_i e_i$: $\langle Tv, u \rangle = \sum \lambda_i a_i b_i = \langle v, Tu \rangle$. $\square$

---

### הגדרה: אנטי-סימטריות

> [!abstract] הגדרה 14.18
> $T$ **אנטי-סימטרית** אם $\langle Tv, u \rangle = -\langle v, Tu \rangle$ לכל $v, u$.

> [!abstract] הערה 14.19
> הע"ע הממשי היחיד של $T$ אנטי-סימטרית הוא $\lambda = 0$.

> [!abstract] טענה 14.21
> אם $T$ אנטי-סימטרית ($F = \mathbb{R}$) אז $T^2$ סימטרית ואי-חיובית:
> $$\langle T^2 v, v \rangle = -\langle Tv, Tv \rangle = -\|Tv\|^2 \le 0.$$

> [!example] דוגמה 14.22
> יהי $V = C^\infty(\mathbb{R})$ מרחב הפונקציות הגזירות אינסוף פעמים המקיימות $f(x+1) = f(x)$ לכל $x \in \mathbb{R}$ (פונקציות 1-מחזוריות), עם מ"פ:
> $$\langle f, g \rangle = \int_0^1 f(x)\,g(x)\,dx.$$
> נגדיר $T(f) = f'$ (טרנספורמציית הגזירה); ברור $T : V \to V$. נראה ש-$T$ **אנטי-סימטרית**:
> $$\int_0^1 (f'g - fg') = \int_0^1 (fg)'\,dx = fg\Big|_0^1 = f(1)g(1) - f(0)g(0) = 0$$
> (מתאפס ממחזוריות). לכן $-T^2$ סימטרית אי-שלילית, ו-$T^2$ סימטרית אי-חיובית.
>
> הו"ע של $T$: $f' = \lambda f$ נותן $f = ce^{\lambda x}$; ממחזוריות $\lambda = 0$ (רק הפונקציות הקבועות).
>
> הו"ע של $T^2$: $f'' = \lambda f$. הפתרונות המחזוריים היחידים הם $\sin(2\pi mx)$ ו-$\cos(2\pi mx)$ עם $f'' = -(2\pi m)^2 f$.

---

### המשפט הספקטרלי — מקרה מרוכב

> [!abstract] הגדרה 14.37 — נורמלית
> $T : V \to V$ **נורמלית** אם $TT^* = T^*T$.

> [!note] הערה 14.38
> ברור שאם $T$ צמודה לעצמה ($T^* = T$) אז $T$ נורמלית.

> [!example] דוגמה 14.39
> יהי $V = \mathbb{R}^3$ עם מ"פ סטנדרטית, ו-$T_\theta$ טרנספורמציית הסיבוב בזווית $\theta$. אזי $(T_\theta)^* = T_{-\theta}$, ומכיוון ש-$T_{-\theta} = (T_\theta)^{-1}$, הן מתחלפות — לכן $T_\theta$ נורמלית.

> [!abstract] משפט 14.23 — המשפט הספקטרלי לצמודה לעצמה (F=C)
> אם $T : V \to V$ צמודה לעצמה ($T^* = T$) מעל $\mathbb{C}$, אזי קיים בסיס א"נ של ו"ע של $T$.

> [!abstract] משפט 14.40 — המשפט הספקטרלי הכללי (F=C)
> אם $T : V \to V$ נורמלית ($TT^* = T^*T$) מעל $\mathbb{C}$, אזי קיים בסיס א"נ של ו"ע של $T$. (לא נשתמש במשפט היסודי של האלגברה.)

> [!note]- הוכחה (סקיצה)
> נגדיר $S_1 = \frac{T + T^*}{2}$, $S_2 = \frac{T - T^*}{2i}$ — שתיהן צמודות לעצמן ומתחלפות (מנורמליות $T$). ממשפט 14.41 קיים בסיס א"נ מלכסן ביחד את $S_1$ ו-$S_2$. מ-$T = S_1 + iS_2$ כל איבר הבסיס הוא ו"ע של $T$. $\square$

> [!abstract] טענה 14.41
> אם $S_1^* = S_1$, $S_2^* = S_2$ ו-$S_1 S_2 = S_2 S_1$ — קיים בסיס א"נ מלכסן את שניהן יחד.

> [!note]- הוכחה
> מהמשפט הספקטרלי על $S_1$: $V = \bigoplus_\lambda \ker(S_1 - \lambda I)$, כאשר המ"ע ניצבים זה לזה. מהתחלפות, $S_2$ שומרת כל $\ker(S_1 - \lambda I)$. מהמשפט הספקטרלי לפעולת $S_2$ על כל מ"ע, קיים $B_\lambda$ א"נ של ו"ע. $B = \bigcup B_\lambda$ מספק. $\square$

> [!example] דוגמה 14.24
> יהי $V$ מ"ו מעל $\mathbb{C}$ עם מ"פ, ונגדיר $T(v) = iv$. כל $v \ne 0$ הוא ו"ע של $T$ עם ע"ע $i$, ולכן כל בסיס א"נ מלכסן. אבל $T$ **אינה** צמודה לעצמה:
> $$\langle Tv, u \rangle = \langle iv, u \rangle = i\langle v, u \rangle, \qquad \langle v, Tu \rangle = \langle v, iu \rangle = -i\langle v, u \rangle.$$
> לכן $\langle Tv, u \rangle = -\langle v, Tu \rangle$ — $T$ היא **אנטי-הרמיטית** ולא צמודה לעצמה. זה מראה שמשפחת הט"ל שעבורן מתקיים המשפט הספקטרלי מעל $\mathbb{C}$ רחבה יותר מהסימטריות.

> [!abstract] טענה 14.34
> נניח שהמשפט הספקטרלי נכון ל-$T$ — קיים בסיס א"נ של ו"ע $\{e_i\}$. אז כל $e_i$ הוא גם ו"ע של $T^*$.

> [!note]- הוכחה
> מספיק להראות ל-$e_1$. יש להוכיח $T^* e_1 \in \mathrm{Sp}\{e_1\}$. מתקיים $\mathrm{Sp}\{e_1\}^\perp = \mathrm{Sp}\{e_2, \ldots, e_n\}$ (כי $e_1$ ניצב לכולם). לכן מספיק להראות שלכל $2 \le i \le n$: $\langle T^* e_1, e_i \rangle = 0$. אכן:
> $$\langle T^* e_1, e_i \rangle = \langle e_1, Te_i \rangle = \langle e_1, \lambda_i e_i \rangle = \bar{\lambda}_i \langle e_1, e_i \rangle = 0. \quad \square$$

> [!abstract] מסקנה 14.35
> אם $T$ מקיימת את המשפט הספקטרלי, אז $TT^* = T^*T$ (כלומר $T$ נורמלית).

> [!note] הערה 14.36
> בהוכחה לעיל לא השתמשנו עדיין בעובדה ש-$\mu_i = \bar{\lambda}_i$. אך נוכיח זאת בהמשך (ראו טענה 14.42).

---

### תכונות נוספות של ט"ל נורמלית

> [!abstract] טענה 14.42
> אם $T$ נורמלית ו-$Tv = \lambda v$, אזי $T^* v = \bar{\lambda} v$ (כל ו"ע של $T$ הוא גם ו"ע של $T^*$).

> [!note]- הוכחה
> מספיק להוכיח שאם $S$ נורמלית ו-$Sv = 0$ אז $S^* v = 0$. אכן: $0 = \langle Sv, Sv \rangle = \langle v, S^*Sv \rangle = \langle v, SS^*v \rangle = \|S^*v\|^2$. $\square$

> [!note] הערה 14.43
> זה מסביר מדוע $\mu_i = \bar{\lambda}_i$ בהוכחת המשפט הספקטרלי: אם $T$ נורמלית ו-$Tv = \lambda v$, אז $T^* v = \bar{\lambda} v$, ולכן ע"ע $T^*$ הם בדיוק הצמודים לע"ע של $T$.

> [!abstract] טענה 14.44
> אם $T$ נורמלית ו-$Tv = \alpha v$, $Tu = \beta u$ עם $\alpha \ne \beta$, אזי $v \perp u$.

---

## פרק 15 — מטריצות במ"פ

> [!note] תזכורת 15.1
> לכל $T : V \to V$ הגדרנו את הט"ל הצמודה $T^* : V \to V$ המקיימת $\langle Tv, u \rangle = \langle v, T^* u \rangle$ לכל $v, u$. $T$ נורמלית אם $TT^* = T^*T$.

> [!abstract] מסקנה 15.2
> אם $T^* = T$ (צמודה לעצמה) אזי כל ע"ע של $T$ ממשי.

> [!note]- הוכחה
> $Tv = \lambda v \implies \lambda \|v\|^2 = \langle Tv, v \rangle = \langle v, T^* v \rangle = \langle v, Tv \rangle = \bar{\lambda} \|v\|^2$, לכן $\lambda = \bar{\lambda}$. $\square$

### הט"ל הצמודה

> [!abstract] משפט 14.26 — קיום הט"ל הצמודה
> תהי $T : V \to V$ ט"ל, $V$ מ"פ מעל $F \in \{\mathbb{R}, \mathbb{C}\}$. קיימת ט"ל (יחידה) $T^* : V \to V$ המקיימת לכל $v, u \in V$:
> $$\langle Tv, u \rangle = \langle v, T^* u \rangle.$$
> $T^*$ נקראת **הטרנספורמציה הצמודה** של $T$.

> [!abstract] משפט 14.29 — קיום, יחידות ואפיון
> לכל ט"ל $T : V \to V$ קיימת יחידה $T^* : V \to V$ עם $\langle Tv, u \rangle = \langle v, T^* u \rangle$ לכל $v, u$. בפרט, $T$ צמודה לעצמה אם ורק אם $T^* = T$.

> [!note]- הוכחה (קיום)
> לכל $u$ קבוע, הפונקציה $\varphi(v) = \langle Tv, u \rangle$ היא פונקציונל לינארי. ממשפט ריס קיים $u^* \in V$ יחיד כך ש-$\varphi(v) = \langle v, u^* \rangle$. ההתאמה $u \mapsto u^*$ לינארית ומגדירה את $T^*$. $\square$

> [!note] משפט ריס 14.25
> לכל פונקציונל לינארי $\varphi : V \to F$ קיים $u \in V$ יחיד כך ש-$\varphi(v) = \langle v, u \rangle$.

> [!example] דוגמה 14.27 — בניית $T^*$ ואם $T$ צמודה לעצמה אז $T^* = T$
> נקבע $u \in V$ ונסתכל על הפונקציונל הלינארי $\varphi(v) = \langle Tv, u \rangle$. ממשפט ריס קיים $u^* \in V$ יחיד כך ש-$\langle Tv, u \rangle = \langle v, u^* \rangle$ לכל $v$. ההתאמה $u \mapsto u^*$ לינארית:
> $$\langle Tv, u_1 + u_2 \rangle = \langle v, u_1^* \rangle + \langle v, u_2^* \rangle = \langle v, u_1^* + u_2^* \rangle \implies (u_1 + u_2)^* = u_1^* + u_2^*.$$
> באופן דומה $(tu)^* = t \cdot u^*$ לכל $t \in F$. לכן $T^*(u) = u^*$ מגדירה ט"ל המקיימת $\langle Tv, u \rangle = \langle v, T^* u \rangle$. כאשר $T$ צמודה לעצמה, $\langle Tv, u \rangle = \langle v, Tu \rangle$ נותן $T^* = T$. $\square$

> [!abstract] טענה 14.30 — תכונות בסיסיות
> - $(T^*)^* = T$
> - $(aT)^* = \bar{a} T^*$
> - $(T + S)^* = T^* + S^*$
> - $(TS)^* = S^* T^*$

> [!example] דוגמה 14.31
> עבור $A \in M_n(\mathbb{C})$ ו-$T_A(v) = Av$ על $\mathbb{C}^n$ (מ"פ סטנדרטית): $(T_A)^* = T_{A^*}$ כאשר $A^* = \bar{A}^t$.

> [!abstract] מסקנה 14.32
> אם נסמן $A^* = \bar{A}^t$, אזי $\langle T_A v, u \rangle = \langle v, T_{A^*} u \rangle$ ולכן $(T_A)^* = T_{A^*}$. לדוגמה:
> $$A = \begin{pmatrix} 2+i & 8i \\ 6-i & 3 \end{pmatrix} \implies A^* = \begin{pmatrix} 2-i & 6+i \\ -8i & 3 \end{pmatrix}.$$

> [!example] דוגמה 14.33
> אם $T$ צמודה לעצמה, אזי $T^* = T$ (ראו דוגמה 14.27). בפרט, $\langle Tv, u \rangle = \langle v, Tu \rangle$ לכל $v, u \in V$.

---

### קשר למטריצות מייצגות

> [!abstract] משפט 15.4
> אם $B$ בסיס א"נ של $V$ ו-$A = [T]_B$, אזי $[T^*]_B = A^*$.

> [!note]- הוכחה
> $a_{ij} = \langle Te_j, e_i \rangle$. עבור $C = [T^*]_B$: $c_{ij} = \langle T^* e_j, e_i \rangle = \langle e_j, Te_i \rangle = \overline{\langle Te_i, e_j \rangle} = \bar{a}_{ji}$. ולכן $C = A^*$. $\square$

> [!abstract] מסקנה 15.5
> אם $B$ בסיס א"נ: $T$ צמודה לעצמה / נורמלית אם ורק אם $[T]_B$ כזו. (הגדרת: $A$ נורמלית אם $AA^* = A^*A$.)

> [!note] הערה חשובה
> המשפט נכון **רק** כשהבסיס הוא א"נ! בבסיס שאינו א"נ ייתכן ש-$T$ צמודה לעצמה אבל $[T]_B$ אינה.

---

### משפטים עיקריים על מטריצות נורמליות

> [!abstract] משפט 15.6
> אם $T : V \to V$ נורמלית, קיים פולינום $f(x) \in \mathbb{R}[x]$ כך ש-$T^* = f(T)$.

> [!abstract] משפט 15.11 — גרסה מטריציונית
> אם $A \in M_n(F)$ נורמלית, קיים $f(x) \in \mathbb{R}[x]$ כך ש-$A^* = f(A)$.

> [!example] דוגמה 15.12
> $A \in M_2(\mathbb{R})$ נורמלית אם ורק אם $A = A^t$ (סימטרית) או $A = \begin{pmatrix} a & b \\ -b & a \end{pmatrix}$ (סיבוב). במקרה השני: $A^t + A = 2aI$, ולכן $A^* = A^t = -A + 2aI = f(A)$ עם $f(x) = -x + 2a$.

> [!note]- הוכחה
> ממשפט הספקטרלי: $P^{-1}AP = D$ (אלכסונית, $P$ א"נ). ממשפט אינטרפולציה קיים $f \in \mathbb{R}[x]$ עם $f(\lambda_i) = \bar{\lambda}_i$. אז $f(D)$ = $D^*$ ולכן $P^{-1}f(A)P = f(D) = D^* = P^{-1}A^*P$, כלומר $f(