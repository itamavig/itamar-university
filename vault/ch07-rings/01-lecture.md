---
title: "פרק 7 — חוגים וחוג הפולינומים: הרצאה"
chapter: ch07-rings
source: lecture-yehuda
status: lecture-done
tags: [la2, lecture, ch07-rings]
---

# חוגים וחוג הפולינומים — הרצאה

> [!info] מקור
> פרק 7 מתוך הרצאות יהודה שלום (שיעורים 5–6), עמ' 20–27.

---

## הגדרה 7.1 — חוג ותחום שלמות

> [!abstract] הגדרה 7.1 (חוג)
> קבוצה שבה מוגדרות פעולות חיבור וכפל ובעלת אברים נייטרליים לחיבור ($0$) וכפל ($1$), כך שמתקיימות כל אקסיומות השדה **למעט** קיום איבר הופכי, נקראת **חוג**.

**תחום שלמות** — חוג חילופי שבו **אין מחלקי אפס**:
$$ab = 0 \implies a = 0 \text{ או } b = 0.$$

> [!abstract] טענה 7.2 (כלל הצמצום)
> אם $ab = ac$ ו-$a \ne 0$, אזי $b = c$.

> [!note]- הוכחה
> $ab = ac \implies a(b - c) = 0$. מכיוון $a \ne 0$ ואין מחלקי אפס: $b - c = 0$, כלומר $b = c$. $\square$

> [!proof]+ Natural Deduction — Proof 1 (Claim 7.2)
> | # | Claim | Justification |
> |---|-------|---------------|
> | 1 | $ab = ac$, $a \ne 0$, $R$ is an integral domain | Given |
> | 2 | $a(b-c) = ab - ac = 0$ | Step 1 and distributivity |
> | 3 | $b - c = 0$ | Step 2, step 1: no zero divisors, $a\ne 0$ |
> | 4 | $b = c$ $\square$ | Step 3 |

> [!example] דוגמה 7.3
> - השלמים $\mathbb{Z}$ הם חוג (ותחום שלמות).
> - $F[x]$ — חוג הפולינומים מעל שדה $F$ — הוא תחום שלמות.
> - כל שדה הוא תחום שלמות (כי לכל $a \ne 0$ יש הופכי, ולכן אין מחלקי אפס).

---

## 7.1 — חוג הפולינומים

> [!abstract] משפט 7.4 (חלוקה עם שארית)
> לכל $f, g \in F[x]$ קיימים **יחידים** $h, r \in F[x]$ כך ש:
> $$f = h \cdot g + r$$
> כאשר $r = 0$ או $\deg(r) < \deg(g)$.

> [!abstract] מסקנה 7.5
> 1. אם $f(a) = 0$ אז $f(x) = (x - a)h(x)$ (כלומר $(x - a) \mid f$).
> 2. אם $\deg f = n$ אז ל-$f$ יש לכל היותר $n$ שורשים שונים.
> 3. אם $f, g \in F[x]$ ו-$F \subseteq K$: אם $f \mid g$ כפולינומים מעל $K$ אז $f \mid g$ גם מעל $F$.

> [!note]- הוכחה
> 1. נחלק $f$ ב-$(x-a)$: $f(x) = (x-a)h(x) + r$, עם $\deg r < 1$, לכן $r$ סקלר. הצבת $x = a$ נותנת $r = 0$.
> 2. נובע מ-1 ומאדיטיביות הדרגה ביחס לכפל.
> 3. מיחידות $r$: אם $f \nmid g$ מעל $F$ (כלומר $r \ne 0$), אותה שארית נכונה מעל $K$, ולכן $f \nmid g$ מעל $K$ בסתירה. $\square$

> [!proof]+ Natural Deduction — Proof 1 (Corollary 7.5)
> | # | Claim | Justification |
> |---|-------|---------------|
> | 1 | $f(a) = 0$, $f, (x-a)\in F[x]$ | Given for part 1 |
> | 2 | $f(x) = (x-a)h(x) + r$, $r$ is a scalar | Division algorithm (Thm 7.4): $\deg r < 1$ |
> | 3 | $0 = f(a) = 0\cdot h(a) + r$, so $r = 0$ | Step 2 with $x=a$ |
> | 4 | $(x-a)\mid f(x)$ $\square$ (part 1) | Step 3 |
> | 5 | If $f$ has $n+1$ distinct roots $a_0,\ldots,a_n$: $(x-a_0)\cdots(x-a_n)\mid f$ | Applying part 1 inductively: $\deg f \ge n+1$ via multiplicativity of degree |
> | 6 | $\deg f = n$ implies $f$ has $\le n$ roots $\square$ (part 2) | Step 5 would give $\deg f \ge n+1$, contradiction |
> | 7 | If $f\mid g$ over $K$ then $g = fq$ over $K$; uniqueness of remainder over $F$ gives $r = 0$ over $F$ | Division algorithm is unique; same $r$ over $F\subseteq K$ |
> | 8 | $f\mid g$ over $F$ $\square$ (part 3) | Step 7 |

---

## 7.2 — תחומי שלמות

### מושגי חלוקה

> [!abstract] הגדרה 7.6 (חלוקה)
> יהי $R$ תחום שלמות ו-$a, b \in R$. נאמר ש-$a$ **מחלק** את $b$ ($a \mid b$) אם קיים $c \in R$ כך ש-$b = a \cdot c$.

> [!abstract] הגדרה 7.7 (הפיך / יחידה)
> $u \in R$ נקרא **הפיך** (או **יחידה**) אם קיים $\alpha \in R$ עם $\alpha \cdot u = 1$.

> [!example] דוגמה 7.8
> - בשדה: כל $u \ne 0$ הפיך.
> - ב-$\mathbb{Z}$: רק $\pm 1$ הפיכים.
> - ב-$F[x]$: הפולינומים הקבועים השונים מאפס הם ההפיכים.

> [!abstract] הגדרה 7.9 (חברות)
> $a, b \in R$ נקראים **חברים** ($a \sim b$) אם קיים הפיך $u$ כך ש-$b = a \cdot u$. לחברים יש אותן "תכונות חלוקה".

> [!abstract] הגדרה 7.10 (זרות)
> $a, b \in R$ נקראים **זרים** אם $c \mid a$ ו-$c \mid b$ גורר ש-$c$ הפיך.

> [!abstract] טענה 7.11
> יהיו $0 \ne a, b \in R$. אם $a \mid b$ ו-$b \mid a$ אזי $a \sim b$.

> [!note]- הוכחה
> $b = ac$ ו-$a = bd$, לכן $b = bdc$, ומכלל הצמצום $dc = 1$, כלומר $c, d$ הפיכים. $\square$

> [!proof]+ Natural Deduction — Proof 1 (Claim 7.11)
> | # | Claim | Justification |
> |---|-------|---------------|
> | 1 | $a\mid b$ and $b\mid a$, $a,b\ne 0$ | Given |
> | 2 | $b = ac$ and $a = bd$ for some $c, d\in R$ | Definition of divisibility |
> | 3 | $b = bdc$ | Substituting Step 2: $b = ac = (bd)c$ |
> | 4 | $dc = 1$ (i.e., $c,d$ are units) | Step 3 + cancellation law (Claim 7.2): $b\ne 0$ |
> | 5 | $b = ac$ with $c$ a unit, so $a\sim b$ $\square$ | Definition of associates + Step 4 |

---

### אי-פריקים וראשוניים

> [!abstract] הגדרה 7.12 (אי-פריק)
> $p \in R$ נקרא **אי-פריק** אם $p = a \cdot b$ גורר ש-$a$ או $b$ הפיך (ו-$p$ חבר של השני).

> [!abstract] הגדרה 7.13 (ראשוני)
> $p \in R$ נקרא **ראשוני** אם $p \mid ab$ גורר $p \mid a$ או $p \mid b$.

> [!note] הערה 7.14
> האברים ההפיכים אינם נחשבים אי-פריקים או ראשוניים.

> [!abstract] טענה 7.15
> בכל תחום שלמות, ראשוני $\implies$ אי-פריק.

> [!note]- הוכחה
> נניח $p = a \cdot b$. מראשוניות, $p \mid ab$, לכן $p \mid a$ (נניח בה"כ). אז $p \cdot d = a$ ולכן $a \cdot b \cdot d = a$, ומכלל הצמצום $bd = 1$, כלומר $b$ הפיך. $\square$

> [!proof]+ Natural Deduction — Proof 1 (Claim 7.15)
> | # | Claim | Justification |
> |---|-------|---------------|
> | 1 | $p$ is prime; $p = ab$ | Given |
> | 2 | $p\mid ab$ | Step 1: $p = ab$ |
> | 3 | $p\mid a$ or $p\mid b$ (say $p\mid a$) | Step 2, primality of $p$ |
> | 4 | $a = pd$ for some $d\in R$ | Step 3 |
> | 5 | $p = ab = pdb$, so $db = 1$ | Steps 1, 4 + cancellation (Claim 7.2) |
> | 6 | $b$ is a unit, so $p$ is irreducible $\square$ | Step 5 |

> [!note] הערה 7.16
> הכיוון ההפוך **לא תמיד נכון**! ראו דוגמה נגדית בתרגיל.

---

### פריקות חד-ערכית

> [!abstract] משפט 7.17
> אם בתחום $R$ כל אי-פריק הוא גם ראשוני, אז מתקיימת **פריקות חד-ערכית**: אם $\prod_{i=1}^n p_i = \prod_{j=1}^m q_j$ עם $p_i, q_j$ אי-פריקים, אז $m = n$ ואחרי סידור מחדש $p_i \sim q_i$ לכל $i$.

> [!note]- הוכחה
> באינדוקציה על $m + n$. מקרה הבסיס $m + n = 2$ טריוויאלי. בצעד, $p_1 \mid \prod q_j$, ומראשוניות קיים $j_0$ עם $p_1 \mid q_{j_0}$. נניח $j_0 = 1$. מאי-פריקות $q_1$: $p_1 \sim q_1$, ונכתוב $q_1 = u \cdot p_1$ ($u$ הפיך). נצמצם ב-$p_1$ ונפעיל הנחת אינדוקציה. $\square$

> [!proof]+ Natural Deduction — Proof 1 (Theorem 7.17)
> | # | Claim | Justification |
> |---|-------|---------------|
> | 1 | Every irreducible in $R$ is prime; $\prod_{i=1}^n p_i = \prod_{j=1}^m q_j$ with all $p_i,q_j$ irreducible | Given |
> | 2 | **Base:** $m+n=2$: $p_1 = q_1$, trivially $p_1\sim q_1$ | Only possibility |
> | 3 | **Step:** $p_1\mid\prod_j q_j$ | Step 1: $p_1 = \prod_i p_i / p_2\cdots$ and primality |
> | 4 | $\exists j_0$ with $p_1\mid q_{j_0}$ | Step 3, primality of $p_1$ applied repeatedly |
> | 5 | WLOG $j_0=1$: $q_1 = p_1 u$ for unit $u$ (i.e., $p_1\sim q_1$) | Step 4, irreducibility of $q_1$ |
> | 6 | Cancel $p_1$: $\prod_{i=2}^n p_i = u\cdot\prod_{j=2}^m q_j$ | Step 5 |
> | 7 | By IH: $n-1 = m-1$ and $p_i\sim q_{\sigma(i)}$ for some permutation $\sigma$ | IH on $m+n-2$ |
> | 8 | $m=n$ and $p_i\sim q_{\sigma(i)}$ for all $i$ $\square$ | Steps 5, 7 |

---

### אידיאלים ותחומים ראשיים

> [!abstract] הגדרה 7.18 (אידיאל)
> $I \subseteq R$ נקראת **אידיאל** אם: $0 \in I$, $I$ סגורה תחת חיבור ($a, b \in I \implies a + b \in I$), ו-$I$ סגורה תחת כפל מ-$R$ ($a \in I, b \in R \implies ab \in I$).

> [!example] דוגמה 7.19
> - הזוגיים ב-$\mathbb{Z}$.
> - ב-$F[x]$: $I = \{p \mid p(1) = 0\}$.
> - הבנייה הכללית: עבור $a \in R$, $Ra = \{ra \mid r \in R\}$ היא אידיאל.
> - הכללה: $Ra + Rb = \{ra + sb \mid r, s \in R\}$ לכל $a, b \in R$.

> [!abstract] הגדרה 7.20 (אידיאל ראשי)
> אידיאל $I$ נקרא **ראשי** אם $I = Ra$ לאיזה $a \in R$.

> [!abstract] הגדרה 7.21 (תחום ראשי / PID)
> תחום שלמות נקרא **ראשי** (PID) אם כל אידיאל בו הינו ראשי.

---

### תכונות תחומים ראשיים

> [!abstract] משפט 7.22
> בתחום ראשי: כל אי-פריק הוא ראשוני.

> [!note]- הוכחה
> יהי $p$ אי-פריק ו-$p \mid ab$. נביט ב-$I = Rp + Ra$. מהנחת הראשיות, $I = Rc$ לאיזה $c$. מכיוון $p, a \in I$ — $c \mid p$ ו-$c \mid a$.
>
> מאחר ש-$c \mid p$ ו-$p$ אי-פריק, שתי אפשרויות:
>
> **מקרה 1:** $c \sim p$ — אז $p \mid a$.
>
> **מקרה 2:** $c$ הפיך — אז $I = R$, ולכן קיימים $r, s \in R$ עם $rp + sa = 1$. נכפיל ב-$b$: $rpb + sab = b$, ומכיוון $p \mid ab$ מתקיים $p \mid b$. $\square$

> [!proof]+ Natural Deduction — Proof 1 (Theorem 7.22)
> | # | Claim | Justification |
> |---|-------|---------------|
> | 1 | $R$ is a PID; $p$ irreducible; $p\mid ab$ | Given |
> | 2 | $I = Rp + Ra$ is an ideal; $I = Rc$ for some $c$ | $R$ is a PID |
> | 3 | $c\mid p$ and $c\mid a$ | $p, a\in I=Rc$ |
> | 4 | Since $p$ is irreducible and $c\mid p$: either $c\sim p$ or $c$ is a unit | Definition of irreducible |
> | 5 | **Case 1** ($c\sim p$): $Rc = Rp$, so $a\in Rp$, hence $p\mid a$ | Step 4 |
> | 6 | **Case 2** ($c$ is a unit): $I = Rc = R$, so $\exists r,s$ with $rp+sa=1$ | Step 4 |
> | 7 | Case 2: multiply by $b$: $rpb + sab = b$; $p\mid rpb$ and $p\mid sab$ (since $p\mid ab$) | Step 6 |
> | 8 | Case 2: $p\mid b$ | Step 7 |
> | 9 | $p\mid a$ or $p\mid b$; $p$ is prime $\square$ | Steps 5, 8 |

> [!abstract] מסקנה 7.23
> בתחום ראשי קיימת **פריקות חד-ערכית** למכפלת אי-פריקים.

---

### מחלק משותף גדול ביותר

> [!abstract] משפט 7.24 (gcd בתחום ראשי)
> יהי $R$ תחום ראשי ו-$a, b \in R$.
> 1. אם קיימים $r, s \in R$ כך ש-$g = ra + sb$ מחלק את $a$ ואת $b$, אז $g = \gcd(a, b)$.
> 2. ה-$\gcd$ יחיד עד כדי חברות.
> 3. בתחום ראשי, לכל $a, b$ קיים $g = ra + sb$ כנ"ל.

> [!note]- הוכחה
> 1. $g$ מחלק משותף. אם $d \mid a$ ו-$d \mid b$ אז $d \mid ra + sb = g$, לכן $g$ הגדול ביותר.
> 2. אם $d, g$ שניהם $\gcd$: $g \mid d$ ו-$d \mid g$, לכן $d \sim g$.
> 3. נסמן $I = Ra + Rb$. מהנחת הראשיות $I = Rg$, ומהסימון: $g \mid a$, $g \mid b$, ו-$g = ra + sb$. $\square$

> [!proof]+ Natural Deduction — Proof 1 (Theorem 7.24)
> | # | Claim | Justification |
> |---|-------|---------------|
> | 1 | $R$ is a PID; $a, b\in R$; $g = ra+sb$ divides $a$ and $b$ | Given for part 1 |
> | 2 | $g$ is a common divisor of $a$ and $b$ | Given |
> | 3 | If $d\mid a$ and $d\mid b$, then $d\mid ra+sb = g$ | Steps 1, 2 |
> | 4 | $g$ is the greatest common divisor $\square$ (part 1) | Step 3 |
> | 5 | If $d,g$ both $\gcd$: $g\mid d$ and $d\mid g$, so $d\sim g$ $\square$ (part 2) | Claim 7.11 |
> | 6 | Let $I = Ra + Rb$; since $R$ is PID: $I = Rg$ for some $g$ | Definition of PID |
> | 7 | $g\mid a$ and $g\mid b$ (since $a,b\in Rg$), and $g = r a + sb$ for some $r,s$ | Step 6 |
> | 8 | By part 1: $g = \gcd(a,b)$ $\square$ (part 3) | Steps 7, 4 |

> [!abstract] מסקנה 7.25
> בתחום ראשי, אם $a, b$ זרים, אז קיימים $r, s \in R$ עם $ra + sb = 1$.

---

### $F[x]$ הוא תחום ראשי

> [!abstract] משפט 7.26
> התחום $F[x]$ הוא ראשי.

> [!note]- הוכחה
> יהי $I \subseteq F[x]$ אידיאל (נניח $I \ne \{0\}$). יהי $p \in I$ פולינום בעל **דרגה מינימלית** ב-$I$. לכל $f \in I$, נחלק עם שארית: $f = hp + r$ עם $r = 0$ או $\deg r < \deg p$. אם $r \ne 0$, אז $r = f - hp \in I$ בעל דרגה נמוכה מ-$p$ — סתירה למינימליות. לכן $r = 0$ ו-$f = hp \in Rp$, כלומר $I = Rp$ ראשי. $\square$

> [!proof]+ Natural Deduction — Proof 1 (Theorem 7.26)
> | # | Claim | Justification |
> |---|-------|---------------|
> | 1 | $I\subseteq F[x]$ is a non-zero ideal | Given |
> | 2 | Let $p\in I$ have minimal degree | Well-ordering on $\mathbb{N}$ |
> | 3 | For any $f\in I$: $f = hp + r$ with $r=0$ or $\deg r < \deg p$ | Division algorithm (Thm 7.4) |
> | 4 | $r = f - hp \in I$ (since $I$ is an ideal) | Step 3, ideal absorbs $R$-multiples |
> | 5 | $\deg r < \deg p$ contradicts minimality of $p$ | Step 2 |
> | 6 | Therefore $r = 0$ and $f = hp\in Rp$ | Steps 4, 5: $r\ne 0$ impossible |
> | 7 | $I\subseteq Rp$; also $Rp\subseteq I$ since $p\in I$ | Steps 6; ideal axiom |
> | 8 | $I = Rp$ is principal $\square$ | Step 7 |

> [!abstract] מסקנה 7.27–7.28
> ההוכחה הנ"ל השתמשה רק בחלוקה עם שארית. לכן גם $\mathbb{Z}$ הוא תחום ראשי (כי בו מתקיים חלוקה עם שארית $f = hp + r$ עם $r = 0$ או $|r| < |p|$). לכן ב-$\mathbb{Z}$: ראשוני = אי-פריק, ומתקיימת פריקות חד-ערכית.

---

### תחומים אוקלידיים

> [!abstract] הגדרה 7.29 (תחום אוקלידי)
> תחום $R$ נקרא **אוקלידי** אם קיימת פונקציה $N : R \setminus \{0\} \to \mathbb{Z}$ כך שלכל $f, p \in R$ קיימים $h, r \in R$ עם:
> $$f = hp + r, \quad r = 0 \text{ או } N(r) < N(p).$$

> [!note] הערה 7.30
> ניתן להוכיח בדיוק כמו משפט 7.26 שכל תחום אוקלידי הוא ראשי.

> [!example] דוגמה 7.31 — חוג השלמים של גאוס
> $$R = \mathbb{Z}[i] = \{a + bi \mid a, b \in \mathbb{Z}\}$$
> הוא תחום אוקלידי ביחס לנורמה $N(a + bi) = a^2 + b^2$.
>
> **ההפיכים ב-$\mathbb{Z}[i]$:** אם $\alpha\beta = 1$ אז $N(\alpha)N(\beta) = N(1) = 1$, לכן $N(\alpha) = N(\beta) = 1$, כלומר $\alpha \in \{\pm 1, \pm i\}$.

---

### ייצוג ראשוניים ב-$\mathbb{Z}[i]$

> [!abstract] משפט 7.32
> יהי $p \in \mathbb{Z}$ ראשוני. התנאים הבאים שקולים:
> 1. $p$ פריק ב-$\mathbb{Z}[i]$.
> 2. $p = m^2 + n^2$ עבור $m, n \in \mathbb{Z}$.
> 3. $p \equiv 1 \pmod{4}$ או $p = 2$.

> [!note]- הוכחה
> **$(1) \implies (2)$:** אם $p = \alpha\beta$ ב-$\mathbb{Z}[i]$, אז $p^2 = N(p) = N(\alpha)N(\beta)$. מאי-פריקות $p$ מעל $\mathbb{Z}$: $N(\alpha) = N(\beta) = p$. עבור $\alpha = m + in$: $p = N(\alpha) = m^2 + n^2$.
>
> **$(2) \implies (3)$:** בדיקת שאריות מודולו $4$:
> - אם $m, n$ זוגיים: $m^2 + n^2 \equiv 0 \pmod 4$ — סתירה לאי-פריקות $p$.
> - אם $m, n$ אי-זוגיים: $m^2 + n^2 \equiv 1 + 1 = 2 \pmod 4$ — לכן $p = 2$.
> - אם אחד זוגי ואחד אי-זוגי: $n^2 = (2t+1)^2 = 4t^2 + 4t + 1 \equiv 1 \pmod 4$ ו-$m^2 \equiv 0$, לכן $p \equiv 1 \pmod 4$.
>
> **$(3) \implies (1)$:** הוכחנו בתרגיל בית 1 (שאלה 6) שאם $p \equiv 1 \pmod 4$ אז קיים $n$ עם $n^2 \equiv -1 \pmod p$, כלומר $p \mid n^2 + 1 = (n+i)(n-i)$ ב-$\mathbb{Z}[i]$. אם $p$ אי-פריק ב-$\mathbb{Z}[i]$ אז ראשוני, ולכן $p \mid (n+i)$ או $p \mid (n-i)$ — סתירה (כי $n/p \notin \mathbb{Z}$). לכן $p$ פריק ב-$\mathbb{Z}[i]$. עבור $p = 2$: $2 = -i(1+i)^2$ פריק. $\square$

> [!proof]+ Natural Deduction — Proof 1 (Theorem 7.32, $(1)\Rightarrow(2)$)
> | # | Claim | Justification |
> |---|-------|---------------|
> | 1 | $p\in\mathbb{Z}$ is prime; $p = \alpha\beta$ in $\mathbb{Z}[i]$, neither factor a unit | Given (hypothesis (1)) |
> | 2 | $p^2 = N(p) = N(\alpha\beta) = N(\alpha)N(\beta)$ | $N(a+bi)=a^2+b^2$ is multiplicative |
> | 3 | $N(\alpha)N(\beta) = p^2$ and $N(\alpha),N(\beta) > 1$ (not units) | Step 2, units have $N=1$ |
> | 4 | $N(\alpha) = N(\beta) = p$ | Step 3: only factorization of $p^2$ with both factors $> 1$ |
> | 5 | For $\alpha = m+in$: $p = N(\alpha) = m^2 + n^2$ $\square$ | Step 4 |

> [!proof]+ Natural Deduction — Proof 2 (Theorem 7.32, $(2)\Rightarrow(3)$)
> | # | Claim | Justification |
> |---|-------|---------------|
> | 1 | $p = m^2 + n^2$ | Given (hypothesis (2)) |
> | 2.0 | If $m,n$ both even: $m^2+n^2\equiv 0\pmod 4$ | $p$ prime $\ge 2$, but $p$ not divisible by $4$ |
> | 2.1 | Case both even: contradiction since $p$ is prime | Step 2.0 |
> | 3.0 | If $m,n$ both odd: $m^2+n^2\equiv 1+1=2\pmod 4$ | Odd squares $\equiv 1\pmod 4$ |
> | 3.1 | Case both odd: $p = 2$ | Step 3.0 |
> | 4.0 | If one even, one odd: $m^2+n^2\equiv 0+1=1\pmod 4$ | Even square $\equiv 0$, odd square $\equiv 1$ |
> | 4.1 | Case one even/one odd: $p\equiv 1\pmod 4$ | Step 4.0 |
> | 5 | $p=2$ or $p\equiv 1\pmod 4$ $\square$ | Steps 3.1, 4.1 |

> [!proof]+ Natural Deduction — Proof 3 (Theorem 7.32, $(3)\Rightarrow(1)$)
> | # | Claim | Justification |
> |---|-------|---------------|
> | 1 | $p\equiv 1\pmod 4$ or $p=2$ | Given (hypothesis (3)) |
> | 2 | Case $p=2$: $2 = -i(1+i)^2$ factors non-trivially in $\mathbb{Z}[i]$ | Direct computation: $N(1+i)=2$, $1+i$ not a unit |
> | 3 | Case $p\equiv 1\pmod 4$: $\exists n$ with $n^2\equiv -1\pmod p$ | HW 1, Q6 (Wilson/Euler) |
> | 4 | $p\mid n^2+1 = (n+i)(n-i)$ in $\mathbb{Z}[i]$ | Step 3 |
> | 5 | If $p$ were irreducible in $\mathbb{Z}[i]$, then $p$ is prime (Thm 7.22, $\mathbb{Z}[i]$ is PID) | $\mathbb{Z}[i]$ is a Euclidean domain, hence PID |
> | 6 | Then $p\mid(n+i)$ or $p\mid(n-i)$, so $n/p\in\mathbb{Z}$ — contradiction | Step 5 + Step 4 |
> | 7 | $p$ is reducible (not irreducible) in $\mathbb{Z}[i]$, i.e., $p$ factors $\square$ | Steps 5, 6 by contradiction |

---

[[02-tirgul|דוגמאות מהתרגול →]]  |  [[03-exercises|תרגילים →]]
