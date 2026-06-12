---
title: "פרק 1 — תרגילים: ערכים עצמיים ולכסון"
chapter: ch01
type: exercises
status: exercises-done
source: hw1
tags: [la2, exercises, ch01]
---

# תרגילים — ערכים עצמיים ולכסון

> [!info] מקור
> שאלות 1–3, 7 מתוך תרגיל בית 1. פתרונות: עצמאיים — **לא הושוו לפתרון הרשמי**.

---

## שאלה 1 — תכונות ערכים עצמיים תחת פעולות

#hw #medium #ch01 #proof

> [!question]- שאלה 1
> יהי $V$ מרחב וקטורי מעל $F$, $T, S : V \to V$ העתקות לינאריות, ו-$\lambda_T, \lambda_S \in F$ ע"ע של $T, S$ בהתאמה. הוכיחו או הפריכו:
>
> **(א)** $\lambda_T + \lambda_S$ הוא ע"ע של $T + S$.
>
> **(ב)** $\lambda_T^2$ הוא ע"ע של $T^2 := T \circ T$.
>
> **(ג)** לכל $\alpha \in F$, $\alpha\lambda_T$ הוא ע"ע של $\alpha T$.
>
> > [!tip]- רמז
> > בסעיפים (ב) ו-(ג): חשבו מה קורה לוקטור העצמי המתאים ל-$\lambda_T$ כאשר מפעילים $T^2$ ו-$\alpha T$.
> > בסעיף (א): הוקטורים העצמיים של $T$ ו-$S$ עשויים להיות **שונים** — חפשו דוגמה נגדית בה הם שונים.
> >
> > > [!example]- פתרון חלקי
> > > **(א) שקר.** דוגמה נגדית: $V = \mathbb{R}^2$, $T = \begin{pmatrix}1&0\\0&0\end{pmatrix}$ (הטלה על הציר ה-$x$), $S = \begin{pmatrix}0&0\\0&1\end{pmatrix}$ (הטלה על הציר ה-$y$). קח $\lambda_T = 1$ (ו"ע $e_1$) ו-$\lambda_S = 1$ (ו"ע $e_2$). אז $T + S = I$, שיש לה ע"ע $1$ בלבד — אך $\lambda_T + \lambda_S = 2$ אינו ע"ע של $I$.
> > >
> > > **(ב) נכון.** אם $Tv = \lambda_T v$, חשבו מה מתקבל מ-$T^2 v = T(Tv)$.
> > >
> > > **(ג) נכון.** הפעילו $\alpha T$ על ו"ע של $T$.
> > >
> > > > [!success]- פתרון מלא
> > > > **(א) שקר — דוגמה נגדית.**
> > > >
> > > > $V = \mathbb{R}^2$, $T = \begin{pmatrix}1&0\\0&0\end{pmatrix}$, $S = \begin{pmatrix}0&0\\0&1\end{pmatrix}$.
> > > >
> > > > $\lambda_T = 1$ עם ו"ע $e_1 = \begin{pmatrix}1\\0\end{pmatrix}$; $\lambda_S = 1$ עם ו"ע $e_2 = \begin{pmatrix}0\\1\end{pmatrix}$.
> > > >
> > > > $T + S = I_2$, שכל ו"ע שלה ממד 1 עם ע"ע $1$. אבל $\lambda_T + \lambda_S = 1 + 1 = 2$ אינו ע"ע של $I_2$.
> > > >
> > > > ---
> > > >
> > > > **(ב) נכון.**
> > > >
> > > > יהי $0 \ne v \in V$ ו"ע של $T$ עם ע"ע $\lambda_T$, כלומר $Tv = \lambda_T v$. אז:
> > > > $$T^2 v = T(Tv) = T(\lambda_T v) = \lambda_T (Tv) = \lambda_T \cdot \lambda_T v = \lambda_T^2 v.$$
> > > > לכן $v$ הוא ו"ע של $T^2$ עם ע"ע $\lambda_T^2$. $\square$
> > > >
> > > > ---
> > > >
> > > > **(ג) נכון.**
> > > >
> > > > יהי $0 \ne v \in V$ ו"ע של $T$ עם ע"ע $\lambda_T$. אז:
> > > > $$(\alpha T)(v) = \alpha (Tv) = \alpha (\lambda_T v) = (\alpha\lambda_T) v.$$
> > > > לכן $v$ הוא ו"ע של $\alpha T$ עם ע"ע $\alpha\lambda_T$. $\square$

---

## שאלה 2 — וקטור עצמי משותף

#hw #easy #ch01 #proof

> [!question]- שאלה 2
> יהי $V$ מרחב וקטורי מעל $F$, $T, S : V \to V$ העתקות לינאריות, ו-$v \in V$ ו"ע **משותף** של $T$ ושל $S$ עם ע"ע $\lambda_T, \lambda_S$ בהתאמה. הוכיחו:
>
> **(א)** $v$ הוא ו"ע של $T + S$ ושל $T \circ S$. מצאו את הע"ע המתאימים.
>
> **(ב)** $T \circ S - S \circ T$ אינה הפיכה.
>
> > [!tip]- רמז
> > **(א)** הפעילו $T+S$ ו-$T\circ S$ ישירות על $v$, תוך שימוש בהגדרה $Tv=\lambda_T v$, $Sv=\lambda_S v$.
> >
> > **(ב)** הראו ש-$v \in \ker(T\circ S - S\circ T)$ כדי לסיים.
> >
> > > [!example]- פתרון חלקי
> > > **(א)** $(T+S)v = Tv + Sv = \lambda_T v + \lambda_S v = (\lambda_T + \lambda_S)v$. הע"ע של $T+S$ הוא $\lambda_T + \lambda_S$.
> > >
> > > $(T\circ S)v = T(Sv) = T(\lambda_S v) = \lambda_S(Tv) = \lambda_S\lambda_T v$. הע"ע של $T\circ S$ הוא $\lambda_T\lambda_S$.
> > >
> > > **(ב)** חשבו $(T\circ S - S\circ T)v$ וזכרו ש-$v \ne 0$.
> > >
> > > > [!success]- פתרון מלא
> > > > **(א)**
> > > >
> > > > מכיוון ש-$Tv = \lambda_T v$ ו-$Sv = \lambda_S v$:
> > > > $$(T+S)v = Tv + Sv = \lambda_T v + \lambda_S v = (\lambda_T + \lambda_S)v.$$
> > > > לכן $v$ הוא ו"ע של $T+S$ עם ע"ע $\lambda_T + \lambda_S$.
> > > >
> > > > $$(T\circ S)v = T(Sv) = T(\lambda_S v) = \lambda_S(Tv) = \lambda_S \cdot \lambda_T v = \lambda_T\lambda_S v.$$
> > > > לכן $v$ הוא ו"ע של $T\circ S$ עם ע"ע $\lambda_T\lambda_S$. $\square$
> > > >
> > > > ---
> > > >
> > > > **(ב)**
> > > >
> > > > מסעיף (א), $v$ הוא ו"ע של $T\circ S$ עם ע"ע $\lambda_T\lambda_S$, וגם ו"ע של $S\circ T$ עם ע"ע $\lambda_S\lambda_T$ (אותו ערך). לכן:
> > > > $$(T\circ S - S\circ T)v = (T\circ S)v - (S\circ T)v = \lambda_T\lambda_S v - \lambda_S\lambda_T v = 0.$$
> > > > מכיוון ש-$v \ne 0$, הוא איבר לא-טריוויאלי ב-$\ker(T\circ S - S\circ T)$, ולכן הגרעין אינו טריוויאלי ו-$T\circ S - S\circ T$ אינה הפיכה. $\square$

---

## שאלה 3 — ע"ע של $S \circ T$ מול $T \circ S$

#hw #medium #ch01 #proof

> [!question]- שאלה 3
> יהיו $V, W$ מרחבות וקטוריים מעל $F$ ויהיו $T : V \to W$ ו-$S : W \to V$ העתקות לינאריות.
>
> **(א)** הראו כי כל ע"ע $\lambda \ne 0$ של $S \circ T$ הוא ע"ע של $T \circ S$.
>
> **(ב)** הראו כי אם בנוסף $V = W$ נוצר סופית, אז $0$ הוא ע"ע של $S \circ T$ אם ורק אם הוא ע"ע של $T \circ S$.
>
> **(ג)** מצאו דוגמה ל-$V, W, S, T$ כך ש-$0$ הוא ע"ע של $S \circ T$ אך לא של $T \circ S$.
>
> > [!tip]- רמז
> > **(א)** אם $w$ הוא ו"ע של $ST$ עם ע"ע $\lambda\ne 0$, הגדירו $u = T(w)$ — הראו ש-$u\ne0$ ושהוא ו"ע של $TS$.
> >
> > **(ב)** $0$ הוא ע"ע אם ורק אם הגרעין אינו טריוויאלי. כשהמרחב נוצר סופית, השתמשו בנוסחת הממד.
> >
> > **(ג)** חפשו $V, W$ ממדים שונים — אחד ממד 2 ואחד ממד 3.
> >
> > > [!example]- פתרון חלקי
> > > **(א)** יהי $w$ ו"ע של $ST$ עם ע"ע $\lambda\ne0$, כלומר $S(T(w))=\lambda w$. הגדר $u=T(w)$. אם $u=0$ אז $\lambda w = S(0)=0$, ומכיוון $\lambda\ne0$ מתקבל $w=0$ — סתירה. לכן $u\ne0$. חשבו $T(S(u))$.
> > >
> > > **(ב)** $0$ ע"ע של $ST$ אם ורק אם $ST$ אינה חח"ע (כי $V$ נ"ס). השתמשו בזה: $\det(ST) = \det(S)\det(T) = \det(TS)$.
> > >
> > > **(ג)** $V = \mathbb{R}^3$, $W = \mathbb{R}^2$: הגדירו $T$ כהטלה (surjective) ו-$S$ כהצבה (injective). אז $T\circ S = \mathrm{Id}_{W}$ (אין ע"ע $0$) ו-$S\circ T$ מכניסה את $e_3$ לגרעין.
> > >
> > > > [!success]- פתרון מלא
> > > > **(א)**
> > > >
> > > > יהי $0 \ne w \in W$ ו"ע של $S \circ T$ עם ע"ע $\lambda \ne 0$, כלומר $S(T(w)) = \lambda w$.
> > > >
> > > > נגדיר $u = T(w) \in V$. נטען ש-$u \ne 0$: אם $T(w) = 0$, אז $\lambda w = S(T(w)) = S(0) = 0$. מכיוון $\lambda \ne 0$ ו-$\lambda w = 0$, מתקבל $w = 0$ — סתירה להנחה $w \ne 0$. לכן $u = T(w) \ne 0$.
> > > >
> > > > עתה:
> > > > $$(T \circ S)(u) = T(S(T(w))) = T(\lambda w) = \lambda T(w) = \lambda u.$$
> > > > לכן $u \ne 0$ הוא ו"ע של $T \circ S$ עם ע"ע $\lambda$. $\square$
> > > >
> > > > ---
> > > >
> > > > **(ב)** ($V = W$ נוצר סופית, $T, S : V \to V$)
> > > >
> > > > $0$ הוא ע"ע של $S \circ T$ אם ורק אם $\ker(ST) \ne \{0\}$ אם ורק אם $ST$ אינה הפיכה.
> > > >
> > > > מכיוון $V$ נוצר סופית: $ST$ הפיכה אם ורק אם $\det(ST) \ne 0$ אם ורק אם $\det(S)\det(T) \ne 0$ אם ורק אם $\det(TS) \ne 0$ אם ורק אם $TS$ הפיכה.
> > > >
> > > > לכן $ST$ אינה הפיכה אם ורק אם $TS$ אינה הפיכה, כלומר $0$ ע"ע של $ST$ אם ורק אם $0$ ע"ע של $TS$. $\square$
> > > >
> > > > ---
> > > >
> > > > **(ג) דוגמה.**
> > > >
> > > > $V = \mathbb{R}^3$, $W = \mathbb{R}^2$. נגדיר:
> > > > $$T : \mathbb{R}^3 \to \mathbb{R}^2, \quad T(e_1) = e_1,\; T(e_2) = e_2,\; T(e_3) = 0 \quad \text{(הטלה)},$$
> > > > $$S : \mathbb{R}^2 \to \mathbb{R}^3, \quad S(e_1) = e_1,\; S(e_2) = e_2 \quad \text{(הצבה לתת-מרחב)}.$$
> > > >
> > > > $T \circ S : \mathbb{R}^2 \to \mathbb{R}^2$: $(T \circ S)(v) = T(S(v)) = v$ לכל $v \in \mathbb{R}^2$, כלומר $T \circ S = \mathrm{Id}_{\mathbb{R}^2}$. ל-$\mathrm{Id}$ אין ע"ע $0$.
> > > >
> > > > $S \circ T : \mathbb{R}^3 \to \mathbb{R}^3$: $(S \circ T)(e_3) = S(T(e_3)) = S(0) = 0$. לכן $e_3 \ne 0$ הוא ו"ע של $S \circ T$ עם ע"ע $0$, כלומר $0$ הוא ע"ע של $S \circ T$. $\square$

---

## שאלה 7 — תמ"ו ומשלימים (מלינארית 1)

#hw #medium #ch01 #proof

> [!question]- שאלה 7
> הוכיחו את הטענות הבאות:
>
> **(א)** יהיו $V$ מרחב וקטורי נוצר-סופית ו-$U, W \subseteq V$ תת-מרחבות כך ש-$U + W = V$. הראו כי קיים $W' \subseteq W$ כך ש-$U \oplus W' = V$.
>
> (הדרכה: דומה להוכחה של משפט הממדים. בחרו בסיס ל-$U \cap W$ והשלימו אותו לבסיס של $W$. הוקטורים שהוספתם יהיו בסיס של $W'$.)
>
> **(ב)** יהיו $W_1 \subseteq W_2 \subseteq V$ תת-מרחבות ו-$U \subseteq V$ תת-מרחב נוסף. נתון ש-$U \cap W_1 = \{0\}$ ו-$U + W_2 = V$. הראו כי קיים $W_1 \subseteq W' \subseteq W_2$ כך ש-$U \oplus W' = V$.
>
> (הדרכה: יהי $B_0$ בסיס של $U \cap W_2$ ו-$B_1$ בסיס של $W_1$. הראו ש-$B_0 \cup B_1$ בת"ל, השלימו אותו לבסיס $B_0 \cup B_1 \cup B_2$ של $W_2$. הראו ש-$B_1 \cup B_2$ בסיס למרחב המבוקש.)
>
> **(ג)** תהי $T : V \to W$ העתקה לינארית ו-$U \subseteq W$ תת-מרחב. הראו כי
> $$T^{-1}(U) := \{v \in V \mid Tv \in U\}$$
> הוא תת-מרחב של $V$.
>
> > [!tip]- רמז
> > **(א)** בחרו $B_U$ בסיס של $U \cap W$, ו-$B_W = B_U \cup \{w_1,\ldots,w_k\}$ בסיס של $W$. הגדירו $W' = \operatorname{Sp}\{w_1,\ldots,w_k\}$. כדי להוכיח $U \cap W' = \{0\}$: כל איבר ב-$U \cap W'$ שייך גם ל-$U \cap W$ ולכן ניתן להצגה בשני אופנים — השתמשו בבלתי-תלות.
> >
> > **(ב)** עקבו אחרי ההדרכה. הנקודה הקשה: הראו ש-$B_0 \cup B_1$ בת"ל (השתמשו ב-$U \cap W_1 = \{0\}$).
> >
> > **(ג)** בדקו שלושה תנאים: $0 \in T^{-1}(U)$, סגור תחת חיבור, סגור תחת כפל בסקלר.
> >
> > > [!example]- פתרון חלקי
> > > **(א)** יהי $B_U = \{b_1,\ldots,b_m\}$ בסיס של $U \cap W$. מכיוון $U \cap W \subseteq W$, ניתן להשלים ל-$B_W = B_U \cup \{w_1,\ldots,w_k\}$ בסיס של $W$. הגדירו $W' = \operatorname{Sp}\{w_1,\ldots,w_k\}$.
> > >
> > > להוכחת $U \cap W' = \{0\}$: אם $v \in U \cap W'$, אז $v = \sum \alpha_i w_i \in U$. מכיוון $w_i \in W$ ו-$v \in U$, נקבל $v \in U \cap W$. לכן $v = \sum \beta_j b_j$ גם. מבת"ל של $B_W$ יוצא $v = 0$.
> > >
> > > להוכחת $U + W' = V$: לכל $v \in V = U + W$, כתבו $v = u + w$ עם $w \in W$. פרקו $w = \sum \beta_j b_j + \sum \alpha_i w_i$, ושימו לב ש-$\sum \beta_j b_j \in U$.
> > >
> > > **(ג)** $T(0) = 0 \in U$ (כי $U$ תת-מרחב). שאר התנאים מהלינאריות של $T$.
> > >
> > > > [!success]- פתרון מלא
> > > > **(א)**
> > > >
> > > > יהי $B_U = \{b_1, \ldots, b_m\}$ בסיס של $U \cap W$. מכיוון $U \cap W \subseteq W$, לפי משפט ההרחבה קיים $B_W = B_U \cup \{w_1,\ldots,w_k\}$ בסיס של $W$. נגדיר $W' = \operatorname{Sp}\{w_1,\ldots,w_k\} \subseteq W$.
> > > >
> > > > נוכיח $U \oplus W' = V$:
> > > >
> > > > **$U \cap W' = \{0\}$:** יהי $v \in U \cap W'$. אז $v = \sum_{i=1}^k \alpha_i w_i$ וגם $v \in U$. מכיוון $w_i \in W$ ו-$v \in U$, נקבל $v \in U \cap W$, ולכן $v = \sum_{j=1}^m \beta_j b_j$. אז:
> > > > $$\sum_{j=1}^m \beta_j b_j - \sum_{i=1}^k \alpha_i w_i = 0.$$
> > > > מבלתי-תלות של $B_W = \{b_1,\ldots,b_m,w_1,\ldots,w_k\}$: כל המקדמים אפס. לכן $v = 0$.
> > > >
> > > > **$U + W' = V$:** יהי $v \in V = U + W$. כתוב $v = u + w$ עם $u \in U$, $w \in W$. פרק $w = \sum \beta_j b_j + \sum \alpha_i w_i$ לפי הבסיס של $W$. מכיוון $b_j \in U \cap W \subseteq U$:
> > > > $$v = \underbrace{\left(u + \sum_{j=1}^m \beta_j b_j\right)}_{\in U} + \underbrace{\sum_{i=1}^k \alpha_i w_i}_{\in W'} \in U + W'. \quad \square$$
> > > >
> > > > ---
> > > >
> > > > **(ב)**
> > > >
> > > > יהי $B_0$ בסיס של $U \cap W_2$ ו-$B_1$ בסיס של $W_1$.
> > > >
> > > > **ראשית: $B_0 \cup B_1$ בלתי-תלוי לינארית.**
> > > > נניח $\sum \alpha_i b_i + \sum \beta_j c_j = 0$ עם $b_i \in B_0$, $c_j \in B_1$. אז $\sum \beta_j c_j = -\sum \alpha_i b_i$. האגף הימני שייך ל-$U$ (כי $b_i \in U \cap W_2 \subseteq U$), והאגף השמאלי שייך ל-$W_1$ (כי $c_j \in B_1 \subseteq W_1$). לכן $\sum \beta_j c_j \in U \cap W_1 = \{0\}$, ומבלתי-תלות $B_1$: כל $\beta_j = 0$. אז $\sum \alpha_i b_i = 0$, ומבלתי-תלות $B_0$: כל $\alpha_i = 0$.
> > > >
> > > > **הרחבה:** מכיוון $B_0 \cup B_1 \subseteq W_2$, ניתן להשלים ל-$B_0 \cup B_1 \cup B_2$ בסיס של $W_2$ (עם $B_2 \subseteq W_2$). נגדיר $W' = \operatorname{Sp}(B_1 \cup B_2)$.
> > > >
> > > > $W_1 \subseteq W'$: כי $B_1 \subseteq B_1 \cup B_2$.
> > > > $W' \subseteq W_2$: כי $B_1, B_2 \subseteq W_2$.
> > > >
> > > > **$U \cap W' = \{0\}$:** יהי $v \in U \cap W'$. כתוב $v = \sum \beta_j c_j + \sum \delta_k d_k$ עם $c_j \in B_1$, $d_k \in B_2$. מכיוון $v \in U \cap W_2$, כתוב $v = \sum \alpha_i b_i$. מבלתי-תלות של $B_0 \cup B_1 \cup B_2$: כל המקדמים אפס, לכן $v = 0$.
> > > >
> > > > **$U + W' = V$:** יהי $v \in V = U + W_2$. כתוב $v = u + w_2$ עם $u \in U$, $w_2 \in W_2$. פרק $w_2 = \sum \alpha_i b_i + \sum \beta_j c_j + \sum \delta_k d_k$. מכיוון $b_i \in U \cap W_2 \subseteq U$:
> > > > $$v = \underbrace{\left(u + \sum \alpha_i b_i\right)}_{\in U} + \underbrace{\sum \beta_j c_j + \sum \delta_k d_k}_{\in W'} \in U + W'. \quad \square$$
> > > >
> > > > ---
> > > >
> > > > **(ג)**
> > > >
> > > > נוכיח ש-$T^{-1}(U)$ הוא תת-מרחב של $V$:
> > > >
> > > > **$0 \in T^{-1}(U)$:** $T(0) = 0 \in U$ (כי $U$ תת-מרחב). ✓
> > > >
> > > > **סגור תחת חיבור:** יהיו $v_1, v_2 \in T^{-1}(U)$, כלומר $T(v_1), T(v_2) \in U$. אז $T(v_1 + v_2) = T(v_1) + T(v_2) \in U$ (כי $U$ תת-מרחב). לכן $v_1 + v_2 \in T^{-1}(U)$. ✓
> > > >
> > > > **סגור תחת כפל בסקלר:** יהי $v \in T^{-1}(U)$ ו-$\alpha \in F$. אז $T(\alpha v) = \alpha T(v) \in U$ (כי $U$ תת-מרחב). לכן $\alpha v \in T^{-1}(U)$. ✓
> > > >
> > > > לכן $T^{-1}(U)$ הוא תת-מרחב של $V$. $\square$
