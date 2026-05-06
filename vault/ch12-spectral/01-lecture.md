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

> [!abstract] למה 14.11
> אם $T$ סימטרית ו-$\lambda \in \mathbb{R}$: אם $(T - \lambda I)^2 v = 0$ אז $(T - \lambda I) v = 0$.

> [!note]- הוכחה
> $S = T - \lambda I$ גם צמודה לעצמה. אם $S^2 v = 0$ אז $0 = \langle S^2 v, v \rangle = \|Sv\|^2$, ולכן $Sv = 0$. $\square$

> [!abstract] טענה 14.10
> כל הגורמים הלינאריים של $m_T$ (לטרנס' סימטרית $T$) שונים זה מזה. בפרט, $T$ לכסינה.

> [!note]- הוכחה
> נניח בשלילה $(x - \lambda)^2 \mid m_T(x)$. אזי $(T - \lambda I)^2 g(T) = 0$ לכל $v$. מלמה 14.11 עם $w = g(T)v$: $(T - \lambda I)w = 0$. ולכן $(x - \lambda)g(x)$ מאפס את $T$ בסתירה למינימליות. $\square$

> [!abstract] משפט 14.13 = 14.16 — המשפט הספקטרלי (F=R)
> תהי $T : V \to V$ סימטרית ($F = \mathbb{R}$). אזי קיים בסיס אורתונורמלי של $V$ המורכב מו"ע של $T$.

> [!note]- הוכחה
> הוכחנו ש-$T$ לכסינה. יהיו $\lambda_1, \ldots, \lambda_r$ הע"ע השונים ו-$V_{\lambda_i} = \ker(T - \lambda_i I)$. מלכסינות: $V = \bigoplus V_{\lambda_i}$.
>
> מטענה 14.14 (להלן): ו"ע ממ"ע שונים ניצבים זה לזה. לכן בכל $V_{\lambda_i}$ בנפרד מפעילים גרם-שמידט לקבלת $B_i$ א"נ. $B = \bigcup B_i$ הוא בסיס א"נ של $V$. $\square$

> [!abstract] משפט 14.17 — הכיוון ההפוך
> אם ל-$T : V \to V$ קיים בסיס א"נ של ו"ע (כל $\lambda_i \in \mathbb{R}$), אז $T$ סימטרית.

> [!note]- הוכחה
> יהי $\{e_i\}$ בסיס א"נ, $Te_i = \lambda_i e_i$. לכל $v = \sum a_i e_i$, $u = \sum b_i e_i$: $\langle Tv, u \rangle = \sum \lambda_i a_i b_i = \langle v, Tu \rangle$. $\square$

---

### ו"ע וניצביות

> [!abstract] טענה 14.14
> אם $T$ צמודה לעצמה ($F = \mathbb{R}$ או $\mathbb{C}$) ו-$Tv = \alpha v$, $Tu = \beta u$ עם $\alpha \ne \beta$, אזי $\langle v, u \rangle = 0$.

> [!note]- הוכחה
> $\alpha \langle v, u \rangle = \langle Tv, u \rangle = \langle v, Tu \rangle = \bar{\beta} \langle v, u \rangle$. אם $F = \mathbb{R}$: $\alpha \ne \beta$ ולכן $\langle v, u \rangle = 0$. אם $F = \mathbb{C}$: נשתמש בלמה 14.15. $\square$

> [!abstract] למה 14.15
> אם $T$ צמודה לעצמה אז כל ע"ע (אפילו מרוכב) ממשי.

> [!note]- הוכחה
> $Tu = \beta u \implies \beta \|u\|^2 = \langle Tu, u \rangle = \langle u, Tu \rangle = \bar{\beta} \|u\|^2 \implies \beta = \bar{\beta}$. $\square$

---

### הגדרה: אנטי-סימטריות

> [!abstract] הגדרה 14.18
> $T$ **אנטי-סימטרית** אם $\langle Tv, u \rangle = -\langle v, Tu \rangle$ לכל $v, u$.

> [!abstract] הערה 14.19
> הע"ע הממשי היחיד של $T$ אנטי-סימטרית הוא $\lambda = 0$.

> [!abstract] טענה 14.21
> אם $T$ אנטי-סימטרית ($F = \mathbb{R}$) אז $T^2$ סימטרית ואי-חיובית:
> $$\langle T^2 v, v \rangle = -\langle Tv, Tv \rangle = -\|Tv\|^2 \le 0.$$

---

### המשפט הספקטרלי — מקרה מרוכב

> [!abstract] הגדרה 14.37 — נורמלית
> $T : V \to V$ **נורמלית** אם $TT^* = T^*T$.

> [!abstract] משפט 14.23/14.40 — המשפט הספקטרלי (F=C)
> אם $T : V \to V$ נורמלית (מעל $\mathbb{C}$) אזי קיים בסיס א"נ של ו"ע של $T$.

> [!note]- הוכחה (סקיצה)
> נגדיר $S_1 = \frac{T + T^*}{2}$, $S_2 = \frac{T - T^*}{2i}$ — שתיהן צמודות לעצמן ומתחלפות (מנורמליות $T$). ממשפט 14.41 קיים בסיס א"נ מלכסן ביחד את $S_1$ ו-$S_2$. מ-$T = S_1 + iS_2$ כל איבר הבסיס הוא ו"ע של $T$. $\square$

> [!abstract] טענה 14.41
> אם $S_1^* = S_1$, $S_2^* = S_2$ ו-$S_1 S_2 = S_2 S_1$ — קיים בסיס א"נ מלכסן את שניהן יחד.

> [!note]- הוכחה
> מהמשפט הספקטרלי על $S_1$: $V = \bigoplus_\lambda \ker(S_1 - \lambda I)$, כאשר המ"ע ניצבים זה לזה. מהתחלפות, $S_2$ שומרת כל $\ker(S_1 - \lambda I)$. מהמשפט הספקטרלי לפעולת $S_2$ על כל מ"ע, קיים $B_\lambda$ א"נ של ו"ע. $B = \bigcup B_\lambda$ מספק. $\square$

> [!abstract] מסקנה 14.35
> אם $T$ מקיימת את המשפט הספקטרלי, אז $TT^* = T^*T$ (כלומר $T$ נורמלית).

---

### תכונות נוספות של ט"ל נורמלית

> [!abstract] טענה 14.42
> אם $T$ נורמלית ו-$Tv = \lambda v$, אזי $T^* v = \bar{\lambda} v$ (כל ו"ע של $T$ הוא גם ו"ע של $T^*$).

> [!note]- הוכחה
> מספיק להוכיח שאם $S$ נורמלית ו-$Sv = 0$ אז $S^* v = 0$. אכן: $0 = \langle Sv, Sv \rangle = \langle v, S^*Sv \rangle = \langle v, SS^*v \rangle = \|S^*v\|^2$. $\square$

> [!abstract] טענה 14.44
> אם $T$ נורמלית ו-$Tv = \alpha v$, $Tu = \beta u$ עם $\alpha \ne \beta$, אזי $v \perp u$.

---

## פרק 15 — מטריצות במ"פ

### הט"ל הצמודה

> [!abstract] משפט 14.25/14.26/14.29 — ט"ל הצמודה
> לכל ט"ל $T : V \to V$ קיימת **יחידה** ט"ל $T^* : V \to V$ המקיימת לכל $v, u \in V$:
> $$\langle Tv, u \rangle = \langle v, T^* u \rangle.$$

> [!note]- הוכחה (קיום)
> לכל $u$ קבוע, הפונקציה $\varphi(v) = \langle Tv, u \rangle$ היא פונקציונל לינארי. ממשפט ריס קיים $u^* \in V$ יחיד כך ש-$\varphi(v) = \langle v, u^* \rangle$. ההתאמה $u \mapsto u^*$ לינארית ומגדירה את $T^*$. $\square$

> [!note] משפט ריס 14.25
> לכל פונקציונל לינארי $\varphi : V \to F$ קיים $u \in V$ יחיד כך ש-$\varphi(v) = \langle v, u \rangle$.

> [!abstract] טענה 14.30 — תכונות בסיסיות
> - $(T^*)^* = T$
> - $(aT)^* = \bar{a} T^*$
> - $(T + S)^* = T^* + S^*$
> - $(TS)^* = S^* T^*$

> [!abstract] דוגמה 14.31–14.32
> עבור $A \in M_n(\mathbb{C})$ ו-$T_A(v) = Av$ על $\mathbb{C}^n$ (מ"פ סטנדרטית): $(T_A)^* = T_{A^*}$ כאשר $A^* = \bar{A}^t$.

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
> אם $A \in M_n(F)$ נורמלית, קיים פולינום $f(x) \in \mathbb{R}[x]$ כך ש-$A^* = f(A)$.

> [!note]- הוכחה
> ממשפט הספקטרלי: $P^{-1}AP = D$ (אלכסונית, $P$ א"נ). ממשפט אינטרפולציה קיים $f \in \mathbb{R}[x]$ עם $f(\lambda_i) = \bar{\lambda}_i$. אז $f(D)$ = $D^*$ ולכן $P^{-1}f(A)P = f(D) = D^* = P^{-1}A^*P$, כלומר $f(A) = A^*$. $\square$

> [!abstract] מסקנה 15.13
> אם $T : V \to V$ נורמלית, קיים $f(x) \in \mathbb{R}[x]$ כך ש-$T^* = f(T)$.

> [!abstract] טענה 15.14
> אם $U \subseteq V$ תת-מרחב $T$-שמור, אז $U^\perp$ הוא $T^*$-שמור.

> [!note]- הוכחה
> יהי $w \in U^\perp$. לכל $u \in U$: $\langle T^* w, u \rangle = \langle w, Tu \rangle = 0$ (כי $Tu \in U$ ו-$w \perp U$). $\square$

> [!abstract] משפט 15.16
> אם $T : V \to V$ נורמלית ו-$U \subseteq V$ הוא $T$-שמור, אז $U$ גם $T^*$-שמור, $U^\perp$ גם $T$-שמור, ו-$T|_U$ נורמלית.

> [!note]- הוכחה
> מ-$T^* = f(T)$: כל ת"מ $T$-שמור גם $f(T) = T^*$-שמור. $\square$

> [!abstract] טענה 15.17
> לכל $T : V \to V$ מעל $\mathbb{R}$ קיים ת"מ $T$-שמור $U \subseteq V$ מממד $\le 2$.

> [!note]- הוכחה
> ניקח $g$ גורם אי-פריק של $m_T$. אם $\deg g = 1$ — ו"ע נותן $\dim U = 1$. אם $\deg g = 2$ — לכל $0 \ne v \in \ker g(T)$: $U = \text{Sp}\{v, Tv\}$ נשמר תחת $T$ (מ-$g(T)v = 0$ נובע $T^2 v \in U$). $\square$

> [!abstract] משפט 15.19 — צורה קנונית ממשית
> אם $T : V \to V$ נורמלית ו-$V$ מ"פ ממשי, קיים בסיס א"נ שביחס אליו המטריצה המייצגת היא בלוקים אלכסוניים:
> - בלוקים $1 \times 1$: ע"ע ממשיים $\lambda_i$
> - בלוקים $2 \times 2$: $\begin{pmatrix} a_k & b_k \\ -b_k & a_k \end{pmatrix}$ עם $b_k \ne 0$

> [!example] דוגמה 15.9
> המטריצות $A \in M_2(\mathbb{R})$ הנורמליות הן בדיוק: $A = A^t$ (סימטריות) או $A = \begin{pmatrix} a & b \\ -b & a \end{pmatrix}$.

---

## פרק 16 — טרנספורמציות ומטריצות אוניטריות

> [!abstract] הגדרה 16.1 — אוניטרית / אורתוגונלית
> $T : V \to V$ נקראת **אוניטרית** ($F = \mathbb{C}$) או **אורתוגונלית** ($F = \mathbb{R}$) אם $T^* T = I$, כלומר $T^* = T^{-1}$.

> [!example] דוגמאות 16.2–16.3
> - $T_\theta$ — סיבוב בזווית $\theta$ ב-$\mathbb{R}^2$: $(T_\theta)^* = T_{-\theta} = T_\theta^{-1}$.
> - שיקוף במישור: $T^* = T$ ולכן $T^2 = I$.

> [!abstract] משפט 16.4 — תנאים שקולים
> הבאים שקולים על $T : V \to V$:
> 1. $T^* = T^{-1}$ (אוניטרית/אורתוגונלית)
> 2. $\langle Tv, Tu \rangle = \langle v, u \rangle$ לכל $v, u$
> 3. $T$ מעבירה כל בסיס א"נ לבסיס א"נ
> 4. קיים בסיס א"נ שהתמונות שלו הן בסיס א"נ
> 5. $\|Tv\| = \|v\|$ לכל $v$

> [!note]- הוכחה (סקיצה)
> $1 \Rightarrow 2$: $\langle Tv, Tu \rangle = \langle v, T^*Tu \rangle = \langle v, u \rangle$.
> $2 \Rightarrow 3 \Rightarrow 4$: ברורים.
> $4 \Rightarrow 5$: כתיבת $v = \sum a_i v_i$ נותנת $\|Tv\|^2 = \sum |a_i|^2 = \|v\|^2$.
> $5 \Rightarrow 1$: $S = T^*T - I$ צמודה לעצמה ו-$\langle Sv, v \rangle = \|Tv\|^2 - \|v\|^2 = 0$ לכל $v$. מטענה 16.5: $S = 0$. $\square$

> [!abstract] טענה 16.5
> אם $S$ צמודה לעצמה ו-$\langle Sv, v \rangle = 0$ לכל $v$, אזי $S = 0$.

> [!abstract] טענה 16.6
> אם $T$ אוניטרית/אורתוגונלית ו-$\lambda$ ע"ע, אזי $|\lambda| = 1$.

> [!note]- הוכחה
> $\|Tv\| = |\lambda| \|v\|$ ו-$\|Tv\| = \|v\|$ $\implies$ $|\lambda| = 1$. $\square$

---

### מטריצות אוניטריות/אורתוגונליות

> [!abstract] הגדרה 16.7
> $A \in M_n(F)$ **אוניטרית** ($F = \mathbb{C}$) / **אורתוגונלית** ($F = \mathbb{R}$) אם $AA^* = A^*A = I$.

> [!abstract] טענה 16.8
> $T$ א"נ אם ורק אם $[T]_B$ א"נ (עבור בסיס א"נ $B$).

> [!abstract] משפט 16.10 — תנאים שקולים
> עבור $A \in M_n(F)$, הבאים שקולים:
> 1. $A$ אוניטרית/אורתוגונלית
> 2. שורות $A$ הן בסיס א"נ של $F^n$
> 3. עמודות $A$ הן בסיס א"נ של $F^n$
> 4. $\langle Av, Au \rangle = \langle v, u \rangle$ לכל $v, u$
> 5. $\|Av\| = \|v\|$ לכל $v$

> [!example] דוגמה 16.11 — מטריצות אורתוגונליות $2 \times 2$
> $$A = \begin{pmatrix} \cos\theta & \sin\theta \\ -\sin\theta & \cos\theta \end{pmatrix} \quad \text{(סיבוב)} \qquad \text{או} \qquad A = \begin{pmatrix} \cos\theta & \sin\theta \\ \sin\theta & -\cos\theta \end{pmatrix} \quad \text{(שיקוף)}$$

---

### הצורה הקנונית של ט"ל אורתוגונלית

> [!abstract] מסקנה 16.12 — צורה קנונית אורתוגונלית
> אם $T : V \to V$ אורתוגונלית ($F = \mathbb{R}$), קיים בסיס א"נ שביחס אליו המטריצה המייצגת היא בלוקים אלכסוניים: בלוקי $1 \times 1$ עם $\pm 1$, ובלוקי $2 \times 2$ מהצורה $\begin{pmatrix} \cos\theta_k & \sin\theta_k \\ -\sin\theta_k & \cos\theta_k \end{pmatrix}$.

> [!abstract] משפט 16.13 — יחידות
> שתי מטריצות מהצורה הקנונית הנ"ל המייצגות את אותה $T$ שוות עד כדי סדר הבלוקים (ו-$b_i$ נקבעים עד כדי סימן).

> [!note]- הוכחה
> הצורה נקבעת על ידי הפולינום האופייני: $f_A(x) = \prod_i (x - \lambda_i) \cdot \prod_j (x^2 - 2a_j x + a_j^2 + b_j^2)$, ופירוק זה חד-ערכי ב-$\mathbb{R}[x]$ (PID). $\square$

---

### ניסוח מחדש של המשפט הספקטרלי

> [!abstract] משפט 16.14 — ניסוח מטריציוני
> תהי $A \in M_n(F)$: סימטרית (אם $F = \mathbb{R}$) או נורמלית (אם $F = \mathbb{C}$). אזי קיימת $P$ אורתוגונלית ($F = \mathbb{R}$) / אוניטרית ($F = \mathbb{C}$) ו-$D$ אלכסונית כך ש:
> $$A = P^{-1}DP.$$
> כאשר $F = \mathbb{R}$ ו-$P$ אורתוגונלית: $P^{-1} = P^t$, ולכן $A = P^t DP$ (ז"א $A$ גם **חופפת** ל-$D$).

> [!abstract] משפט 16.17 — אפיון ע"י ע"ע
> תהי $A \in M_n(\mathbb{C})$ נורמלית. אזי:
> 1. $A = A^*$ אם ורק אם כל ע"ע של $A$ ממשי.
> 2. $A^* = A^{-1}$ (כלומר $A$ אוניטרית) אם ורק אם $|\lambda| = 1$ לכל ע"ע $\lambda$ של $A$.

---

[[02-tirgul|דוגמאות מהתרגול →]]  |  [[03-exercises|תרגילים →]]
