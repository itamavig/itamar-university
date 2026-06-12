---
title: "פרק 13 — מטריצות מוגדרות חיובית ופירוק פולארי: הרצאה"
chapter: ch13-polar-decomposition
source: lecture-yehuda
status: lecture-done
tags: [la2, lecture, ch13-polar-decomposition]
---

# מטריצות מוגדרות חיובית ופירוק פולארי — הרצאה

> [!info] מקור
> פרקים 17–18 מתוך הרצאות יהודה שלום, עמ' 85–87.

---

## פרק 17 — מטריצות מוגדרות חיובית

> [!note] תזכורת 17.1
> $V$ מ"פ מעל $F \in \{R, \mathbb{C}\}$. ט"ל $T : V \to V$ נקראת **חיובית** / **אי-שלילית** אם $T^* = T$ ומתקיים לכל $0 \ne v \in V$:
> $$\langle Tv, v \rangle > 0 \quad / \quad \langle Tv, v \rangle \ge 0.$$

---

### אפיון ע"י ע"ע

> [!abstract] משפט 17.2 — תנאים שקולים
> עבור $A = A^* \in M_n(F)$, הבאים שקולים:
> 1. $T_A(v) = Av$ על $F^n$ חיובית / אי-שלילית.
> 2. לכל $T : V \to V$ ובסיס א"נ $B$ עם $[T]_B = A$: $T$ חיובית / אי-שלילית.
> 3. קיים $T$ חיובי / אי-שלילי ו-$B$ בסיס א"נ עם $[T]_B = A$.
> 4. **כל ע"ע של $A$ חיובי / אי-שלילי** (הע"ע תמיד ממשיים כי $A$ צמודה לעצמה).
>
> (כאשר $F = \mathbb{R}$: שקול לכך שהתבנית הבילינארית המיוצגת ע"י $A$ חיובית / אי-שלילית.)

> [!note]- הוכחה
> **השוויון המרכזי:** אם $B$ בסיס א"נ ו-$A = [T]_B$, אז:
> $$\langle Tv, v \rangle_V = \langle A[v]_B, [v]_B \rangle_{F^n}.$$
> משוויון זה נובעת השקילות בין $1, 2, 3$.
>
> **$1 \Leftarrow 4$:** ממשפט הספקטרלי: $V = \bigoplus V_{\lambda_i}$ (בסיס א"נ $\{v_i\}$ עם $Tv_i = \lambda_i v_i$). לכל $v = \sum a_i v_i$:
> $$\langle Tv, v \rangle = \sum \lambda_i |a_i|^2.$$
> אם כל $\lambda_i > 0$ — ביטוי חיובי; אם כל $\lambda_i \ge 0$ — אי-שלילי.
>
> **$4 \Leftarrow 1$:** אם $\lambda$ ע"ע עם ו"ע $v$: $\langle Tv, v \rangle = \lambda \|v\|^2 > 0$ מחיוביות $T$. $\square$

> [!proof]+ Natural Deduction — Proof 1 (Theorem 17.2)
> | # | Claim | Justification |
> |---|-------|---------------|
> | 1 | $A = A^* \in M_n(F)$; equivalence (1)↔(2)↔(3) via $\langle Tv,v\rangle_V = \langle A[v]_B,[v]_B\rangle_{F^n}$ | ONB representation |
> | 2 | (4→1): Spectral theorem gives ONB $\{v_i\}$ with $Tv_i = \lambda_i v_i$ | Spectral theorem for self-adjoint |
> | 3 | For $v = \sum a_i v_i$: $\langle Tv,v\rangle = \sum \lambda_i |a_i|^2$ | ONB expansion; $\langle v_i, v_j\rangle = \delta_{ij}$ |
> | 4 | All $\lambda_i > 0 \Rightarrow \langle Tv,v\rangle > 0$ for $v \ne 0$; all $\lambda_i \ge 0 \Rightarrow \langle Tv,v\rangle \ge 0$ | Step 3 |
> | 5 | (1→4): If $Tv = \lambda v$, $v \ne 0$: $\langle Tv,v\rangle = \lambda\|v\|^2 > 0$ from positivity | Definition of positive T $\square$ |

---

### קשר לחתימה

> [!abstract] משפט 17.3 — חתימה דרך ע"ע
> אם $A$ מייצגת תבנית סימטרית $f$ מעל $\mathbb{R}$, אזי:
> $$\sigma_+(f) = \#\{\lambda \mid \lambda > 0\}, \quad \sigma_-(f) = \#\{\lambda \mid \lambda < 0\}, \quad \sigma_0(f) = \#\{\lambda \mid \lambda = 0\},$$
> כאשר $\lambda$ עובר על כל הע"ע של $A$.

> [!note]- הוכחה
> $A$ סימטרית, ממשפט הספקטרלי קיימת $U$ אורתוגונלית עם $U^t AU = D$ אלכסונית (ו-$U^{-1} = U^t$). לכן $A$ גם **חופפת** ל-$D$ (לא רק דומה). סימני הע"ע קובעים את החתימה. $\square$

> [!proof]+ Natural Deduction — Proof 1 (Theorem 17.3)
> | # | Claim | Justification |
> |---|-------|---------------|
> | 1 | $A$ symmetric real matrix; spectral theorem: $\exists$ orthogonal $U$ with $U^tAU = D$ diagonal | Spectral theorem (real case, Thm 14.13) |
> | 2 | $A = U^{-1}DU = U^tDU = (U^t)^tDU^t$, so $A$ is congruent to $D$ (not just similar) | $U$ orthogonal: $U^{-1} = U^t = (U^t)^t$ |
> | 3 | Signature $(p,q)$ of $f$ = signs of eigenvalues: $p = \#\{\lambda_i > 0\}$, $q = \#\{\lambda_i < 0\}$ | Diagonal matrix: Sylvester directly from diagonal entries |
> | 4 | Since $A$ congruent to $D$, the bilinear form has the same signature as $D$ | Congruence preserves signature (Sylvester's law) $\square$ |

---

### שורש ריבועי

> [!abstract] טענה 17.4 — שורש ריבועי יחיד
> לכל $T = T^* : V \to V$ אי-שלילית, קיימת **יחידה** $R = R^*$ אי-שלילית עם $R^2 = T$. מסמנים $R = \sqrt{T}$.

> [!note]- הוכחה (קיום)
> ממשפט הספקטרלי: $V = \bigoplus V_{\lambda_i}$. נגדיר $R$ שפועלת ב-$V_{\lambda_i}$ ככפל ב-$\sqrt{\lambda_i}$ (מוגדר כי $\lambda_i \ge 0$). אז $R^2 = T$ על כל ו"ע ולכן על כל $V$. ברור ש-$R = R^*$.
>
> **יחידות:** אם $R'$ כזו אז $R'$ מתחלפת עם $T = (R')^2$ ולכן שומרת כל $V_{\lambda_i}$. על $V_{\lambda_i}$: $R'$ אי-שלילית עם $R'^2 = \lambda_i I$, ולכן כל ע"ע $\alpha$ של $R'|_{V_{\lambda_i}}$ מקיים $\alpha^2 = \lambda_i$ ו-$\alpha \ge 0$, כלומר $\alpha = \sqrt{\lambda_i}$. לכן $R' = R$. $\square$

> [!proof]+ Natural Deduction — Proof 1 (Claim 17.4 — Square Root)
> | # | Claim | Justification |
> |---|-------|---------------|
> | 1 | $T = T^*$ non-negative; spectral theorem: $V = \bigoplus_i V_{\lambda_i}$, $\lambda_i \ge 0$ | Theorem 17.2 + Spectral theorem |
> | 2 | Define $R$: on each $V_{\lambda_i}$, act by $\sqrt{\lambda_i} \cdot I$ | $\lambda_i \ge 0$ so $\sqrt{\lambda_i} \in \mathbb{R}_{\ge 0}$ |
> | 3 | $R^2 = T$ on each $V_{\lambda_i}$ (since $(\sqrt{\lambda_i})^2 = \lambda_i$); $R = R^*$ (acts by real scalars on ONB) | Step 2; eigenspaces orthogonal |
> | 4 | Uniqueness: any $R'$ with $(R')^2 = T$, $R' = (R')^*$, $R' \ge 0$ must commute with $T$ (since $T = (R')^2$) | Polynomial in $R'$ |
> | 5 | $R'$ preserves each $V_{\lambda_i}$ (commutes with $T$, $T$-invariant decomposition) | Step 4 |
> | 6 | On $V_{\lambda_i}$: every eigenvalue $\alpha$ of $R'|_{V_{\lambda_i}}$ satisfies $\alpha^2 = \lambda_i$, $\alpha \ge 0$, so $\alpha = \sqrt{\lambda_i}$ | Steps 4–5; $R'$ non-negative |
> | 7 | $R' = R$ on all of $V$ | Step 6 for each summand $\square$ |

---

## פרק 18 — פירוק פולארי

> [!abstract] משפט 18.1 — פירוק פולארי
> תהי $T : V \to V$ ט"ל הפיכה. אזי קיימים **יחידים**:
> - $R : V \to V$ — חיובית, $R = R^*$
> - $U : V \to V$ — אוניטרית
>
> כך ש-$T = UR$.

> [!note]- הוכחה
> **קיום:** נגדיר $S = TT^*$. אזי $S^* = S$ ו-$S$ חיובית (כי $T$ הפיכה: $\langle Sv, v \rangle = \|T^*v\|^2 > 0$ לכל $v \ne 0$). לפי טענה 17.4 קיים $R = \sqrt{S}$ יחיד. נגדיר $U = TR^{-1}$ ונוכיח שהוא אוניטרי:
> $$U^*U = (TR^{-1})^*(TR^{-1}) = R^{-1}T^*TR^{-1} = R^{-1}SR^{-1} = R^{-1}R^2 R^{-1} = I.$$
>
> **יחידות:** בכל פירוק $T = UR$: $T^*T = R^*U^*UR = R^2$. לכן $R = \sqrt{T^*T}$ נקבע ביחידות, ואז $U = TR^{-1}$ נקבע ביחידות. $\square$

> [!proof]+ Natural Deduction — Proof 1 (Theorem 18.1 — Polar Decomposition, existence)
> | # | Claim | Justification |
> |---|-------|---------------|
> | 1 | $T$ invertible; define $S = TT^*$ | Construction |
> | 2 | $S^* = (TT^*)^* = TT^* = S$ (self-adjoint) | $(AB)^* = B^*A^*$ |
> | 3 | $\langle Sv,v\rangle = \langle TT^*v,v\rangle = \langle T^*v, T^*v\rangle = \|T^*v\|^2 \ge 0$; $= 0$ only if $T^*v = 0$, but $T$ invertible so $T^*$ invertible, giving $v = 0$ | $T$ invertible $\Rightarrow$ $S$ positive |
> | 4 | $R = \sqrt{S}$ exists and is unique (positive self-adjoint with $R^2 = S$) | Claim 17.4 |
> | 5 | Define $U = TR^{-1}$ ($R$ positive so invertible) | Step 4 |
> | 6 | $U^*U = (R^{-1})^*T^*TR^{-1} = R^{-1}SR^{-1} = R^{-1}R^2R^{-1} = I$ | Steps 2–4; $R^{-1}$ self-adjoint |
> | 7 | $U$ is unitary; $T = UR$ is the polar decomposition | Step 6 $\square$ |

> [!proof]+ Natural Deduction — Proof 2 (Theorem 18.1 — uniqueness)
> | # | Claim | Justification |
> |---|-------|---------------|
> | 1 | Any $T = UR$ with $U$ unitary, $R$ positive self-adjoint | Assumption |
> | 2 | $T^*T = R^*U^*UR = R^*R = R^2$ | $U^*U = I$, $R^* = R$ |
> | 3 | $R = \sqrt{T^*T}$ is uniquely determined by $T$ | Claim 17.4 uniqueness |
> | 4 | $U = TR^{-1}$ is then uniquely determined | Step 3 $\square$ |

> [!abstract] הערה 18.2 — פירוק פולארי מהצד השני
> ניתן לרשום גם $T = R_1 U_1$ (חיוב מצד שמאל). נובע מ-$T^* = \tilde{U}\tilde{R}$ ע"י הצמדה.

---

### ערכים סינגולריים

> [!abstract] הגדרה 18.3 — ערכים סינגולריים
> **הערכים הסינגולריים** של $T$ הם הע"ע של $R$ בפירוק הפולארי, כלומר $\sqrt{\lambda_i}$ כאשר $\lambda_i$ הע"ע (אי-שליליים) של $T^*T$.

> [!abstract] למה 18.4
> ל-$T^*T$ ול-$TT^*$ יש אותם ע"ע.

> [!note]- הוכחה
> $TT^* = UR^2 U^{-1}$ ו-$T^*T = R^2$ — שתי המטריצות דומות. $\square$

> [!proof]+ Natural Deduction — Proof 1 (Lemma 18.4)
> | # | Claim | Justification |
> |---|-------|---------------|
> | 1 | $T = UR$ (polar decomposition); $R$ positive self-adjoint | Theorem 18.1 |
> | 2 | $T^*T = R^*U^*UR = R^2$ | $U^*U = I$, $R^* = R$ |
> | 3 | $TT^* = UR(UR)^* = URR^*U^* = UR^2U^{-1}$ | $(AB)^* = B^*A^*$; $U$ unitary so $U^* = U^{-1}$ |
> | 4 | $TT^*$ and $T^*T$ are similar ($TT^* = U(T^*T)U^{-1}$) | Step 3 |
> | 5 | Similar matrices have the same eigenvalues | Characteristic polynomial invariant under similarity $\square$ |

---

### פירוק פולארי למטריצות

> [!abstract] טענה 18.5 — פירוק פולארי למטריצות
> לכל $A \in M_n(F)$ הפיכה קיימות $U \in M_n(F)$ אוניטרית ו-$R \in M_n(F)$ אי-שלילית ($R = R^*$) כך ש-$A = UR$.

> [!note]- הוכחה
> נסתכל על $A^*A$: צמודה לעצמה ואי-שלילית. קיים $R$ יחיד עם $R^2 = A^*A$. מגדירים $U = AR^{-1}$ ומוכיחים $U^*U = I$ כמו בהוכחת משפט 18.1. לחישוב $R$ בפועל: ממשפט הספקטרלי $A^*A = P^{-1}DP$, ואז $R = P^{-1}\sqrt{D}P$. $\square$

> [!proof]+ Natural Deduction — Proof 1 (Claim 18.5 — Polar for Matrices)
> | # | Claim | Justification |
> |---|-------|---------------|
> | 1 | $A \in M_n(F)$ invertible; $A^*A$ self-adjoint and non-negative | $(A^*A)^* = A^*A$; $\langle A^*Av,v\rangle = \|Av\|^2 \ge 0$ |
> | 2 | $R = \sqrt{A^*A}$ exists, unique, positive self-adjoint | Claim 17.4 |
> | 3 | $U = AR^{-1}$; verify $U^*U = R^{-1}A^*AR^{-1} = R^{-1}R^2R^{-1} = I$ | Step 2; same calculation as Theorem 18.1 |
> | 4 | $A = UR$ with $U$ unitary, $R$ positive | Steps 2–3 |
> | 5 | Compute $R$ explicitly: $A^*A = P^{-1}DP$ (spectral), then $R = P^{-1}\sqrt{D}P$ | Spectral theorem for self-adjoint matrices $\square$ |

---

### פירוק לערכים סינגולריים (SVD)

> [!abstract] משפט 18.6 — פירוק SVD
> לכל $A \in M_n(F)$ קיימות מטריצות אוניטריות $U, V$ ומטריצה אלכסונית $D$ עם ערכים אי-שליליים על האלכסון כך ש:
> $$A = UDV.$$
> הערכים האלכסוניים של $D$ הם **הערכים הסינגולריים** של $A$.

> [!note]- הוכחה
> נבצע פירוק פולארי $A = \tilde{U}R$. ממשפט הספקטרלי ל-$R$ (צמודה לעצמה): $R = V^{-1}DV$ עם $V$ אוניטרית ו-$D$ אלכסונית אי-שלילית. אזי:
> $$A = \tilde{U}R = \tilde{U}V^{-1}DV = UDV \quad (U = \tilde{U}V^{-1} \text{ אוניטרית}).$$
> $\square$

> [!proof]+ Natural Deduction — Proof 1 (Theorem 18.6 — SVD)
> | # | Claim | Justification |
> |---|-------|---------------|
> | 1 | $A \in M_n(F)$; polar decomposition $A = \tilde{U}R$ with $\tilde{U}$ unitary, $R$ positive self-adjoint | Claim 18.5 (even when $A$ not invertible, apply to invertible approximation or modify) |
> | 2 | Spectral theorem on $R$ (self-adjoint): $R = V^{-1}DV$ with $V$ unitary, $D$ diagonal non-negative | Spectral theorem; $R$ non-negative $\Rightarrow$ diagonal entries $\ge 0$ |
> | 3 | $A = \tilde{U}R = \tilde{U}V^{-1}DV = UDV$ where $U = \tilde{U}V^{-1}$ | Step 2 substituted |
> | 4 | $U = \tilde{U}V^{-1}$ is unitary (product of unitaries) | $\tilde{U}$ and $V^{-1}$ unitary |
> | 5 | $A = UDV$ with $U,V$ unitary, $D$ diagonal non-negative — this is the SVD | Steps 3–4 $\square$ |

> [!abstract] הערה 18.7
> $A^*A = V^{-1}D^2V$ ו-$AA^* = UD^2U^{-1}$.

> [!abstract] הגדרה 18.8 — סיכום ערכים סינגולריים
> הערכים הסינגולריים של $A$ הם השורשים האי-שליליים של הע"ע של $A^*A$. הם שווים גם ל:
> - שורשי הע"ע של $AA^*$
> - ע"ע של $R$ בפירוק הפולארי $A = UR$
> - ע"ע של $R$ בפירוק הפולארי $A = RU$
> - ערכי האלכסון $D$ בפירוק ה-SVD

---

[[02-tirgul|דוגמאות מהתרגול →]]  |  [[03-exercises|תרגילים →]]
