# Week 2 — Review Table (Pending Approval)

**Sources:**
- Lecture: `Memphys_2_week_2.pdf` (Tomer Snehar)
- Tutorial: `ClassEx2 2026.pdf` (Elior Orisman)

**Legend:** ✅ INCLUDE · ❌ EXCLUDE · ⚠️ BORDERLINE

---

## Section 1 — Triple Products (מכפלות משולשות)

| # | Formula / Definition | Topic Tag | Decision | Reason |
|---|---|---|---|---|
| 1 | $V\text{ (volume)} = (\vec{a} \times \vec{b}) \cdot \vec{c} = \vec{c} \cdot (\vec{a} \times \vec{b})$ | Triple scalar product | ✅ INCLUDE | Named formula; geometric meaning (parallelepiped volume); needed for computation |
| 2–3 | **Computation forms:** $\vec{a}\cdot(\vec{b}\times\vec{c}) = \begin{vmatrix} a_x & a_y & a_z \\ b_x & b_y & b_z \\ c_x & c_y & c_z \end{vmatrix} = \varepsilon_{ijk}\,a_i b_j c_k$ | Triple scalar product | ✅ INCLUDE | Determinant form for computation; index form bridges to Levi-Civita |
| 4–5 | **Cyclic / anti-cyclic:** $\vec{a}\cdot(\vec{b}\times\vec{c}) = \vec{c}\cdot(\vec{a}\times\vec{b}) = -\vec{b}\cdot(\vec{a}\times\vec{c})$ | Triple scalar product | ✅ INCLUDE | Two cyclic iterations + one anti-cyclic sign flip in a single row |
| 6 | $\vec{a} \times (\vec{b} \times \vec{c}) = \vec{b}(\vec{a} \cdot \vec{c}) - \vec{c}(\vec{a} \cdot \vec{b})$ | Triple vector product (BAC-CAB) | ✅ INCLUDE | Named identity ("BAC-CAB"); heavily used in EM and mechanics |
| 7 | Proof via $\epsilon_{ijk}\epsilon_{mnk} = \delta_{im}\delta_{jn} - \delta_{in}\delta_{jm}$ | Levi-Civita contraction | ❌ EXCLUDE | Derivation of BAC-CAB; the identity itself is already in sheet (Week 1, same identity up to relabelling) |

---

## Section 2 — Nabla Operator & Gradient (גרדיאנט)

| # | Formula / Definition | Topic Tag | Decision | Reason |
|---|---|---|---|---|
| 8 | $\vec{\nabla} \equiv (\partial_x, \partial_y, \partial_z) \equiv \hat{e}_i\,\partial_i$ | Nabla operator | ✅ INCLUDE | Definition of a central operator; foundation for all following entries |
| 9 | $\operatorname{grad}f = \vec{\nabla}f = (\partial_x f,\, \partial_y f,\, \partial_z f) = \hat{e}_i\,\partial_i f$ | Gradient | ✅ INCLUDE | Core definition; scalar field in → vector field out |
| 10 | $df \equiv \vec{\nabla}f \cdot d\vec{r} \approx f(\vec{r}+d\vec{r}) - f(\vec{r})$ | Gradient / differential | ✅ INCLUDE | Fundamental relation tying gradient to infinitesimal change; used constantly |
| 11 | $f(\vec{r}+d\vec{r}) \approx f(\vec{r}) + \vec{\nabla}f \cdot d\vec{r}$ | Linear approximation (3D Taylor) | ❌ EXCLUDE | Redundant with #10 (same equation rearranged) |
| 12 | $r(x,y,z) = |\vec{r}(x,y,z)|$; $\;\vec{\nabla}r = \hat{r}$ | Gradient example | ✅ INCLUDE | Key result for central-force problems; appears in almost every physics application |
| 13 | $\vec{\nabla}(fg) = f\,\vec{\nabla}g + g\,\vec{\nabla}f$ | Gradient — product rule | ✅ INCLUDE | Named rule; essential for manipulating vector identities |
| 14–15 | **Chain rule (index notation — general):** $\frac{df}{du} = (\partial_i f)\frac{dx_i}{du}$; special cases: scalar composition ($u=x_j$): $\vec{\nabla}(f(g)) = f'(g)\vec{\nabla}g$; parametric path ($u=t$): $\frac{d}{dt}f(\vec{r}(t)) = (\partial_i f)\dot{x}_i$ | Chain rule (unified) | ✅ INCLUDE | Unified index form; both cases follow by choosing $u$ |
| 16 | $\partial_x f(x,y,z) := \lim_{\Delta x\to 0} \frac{f(x+\Delta x,y,z)-f(x,y,z)}{\Delta x}$ | Partial derivative (reminder) | ❌ EXCLUDE | Calculus 1 carry-over; assumed known; derivation/reminder prose |
| 17 | $df = \frac{\partial f}{\partial x}dx + \frac{\partial f}{\partial y}dy + \frac{\partial f}{\partial z}dz$ | Total differential (component form) | ⚠️ BORDERLINE | Equivalent to entry 10 in components; could be a useful alternative representation, or redundant |
| 18 | Derivation of gradient from Taylor expansion | Derivation | ❌ EXCLUDE | Pedagogical derivation; not a formula |

---

## Section 3 — Directional Derivative (נגזרת כיוונית)

| # | Formula / Definition | Topic Tag | Decision | Reason |
|---|---|---|---|---|
| 19 | $D_{\hat{v}}f(\vec{r}) \equiv \lim_{h\to 0} \frac{f(\vec{r}+h\hat{v})-f(\vec{r})}{h}$ | Directional derivative — definition | ⚠️ BORDERLINE | Formal limit definition; some exams ask for it, but more "definition to know" than formula to use |
| 20 | $D_{\hat{v}}f(\vec{r}) = \vec{\nabla}f \cdot \hat{v}$ | Directional derivative | ✅ INCLUDE | Key formula; scalar rate of change in direction $\hat{v}$ |
| 21 | $D_{\hat{v}}f = |\vec{\nabla}f|\cos\theta$, maximised at $\theta=0$ | Gradient as steepest ascent | ✅ INCLUDE | Explains why gradient = direction of max change; core exam concept |

---

## Section 4 — Curves & Line Integrals (מסלולים ואינטגרל מסלולי)

| # | Formula / Definition | Topic Tag | Decision | Reason |
|---|---|---|---|---|
| 22 | $\vec{r}(t) = (x(t), y(t), z(t))$ | Parametric curve | ✅ INCLUDE | Definition/setup for all line-integral work; notation foundation |
| 23 | $d\vec{r} = \vec{r}'(t)\,dt$ | Curve differential | ✅ INCLUDE | Key formula needed to convert line integrals to ordinary integrals |
| 24 | $W = \int_C \vec{F} \cdot d\vec{r}$ | Line integral / work | ✅ INCLUDE | Central formula of the week; definition of work as line integral |
| 25 | $W = \int_{t_1}^{t_2} \vec{F}(\vec{r}(t)) \cdot \vec{r}'(t)\,dt$ | Line integral (parametric form) | ✅ INCLUDE | Computational form needed for every calculation; directly usable |
| 26 | Conservative force: $W=0$ on any closed path | Conservative forces | ⚠️ BORDERLINE | Important concept but only briefly stated; no standalone formula |
| 27 | Worked examples: axes integrals, helix, gravity | Examples | ❌ EXCLUDE | Illustrate the formula but are not cheat-sheet material |

---

## Section 5 — Gradient Theorem (משפט הגרדיאנט)

| # | Formula / Definition | Topic Tag | Decision | Reason |
|---|---|---|---|---|
| 28 | $\int_{\vec{r}_1}^{\vec{r}_2} \vec{\nabla}f \cdot d\vec{r} = f(\vec{r}_2) - f(\vec{r}_1)$ | Gradient theorem | ✅ INCLUDE | Multi-dimensional FTC; path-independent; major named theorem |

---

## Section 6 — Surfaces (משטחים)

| # | Formula / Definition | Topic Tag | Decision | Reason |
|---|---|---|---|---|
| 29 | $\vec{r}(u,v) = (x(u,v), y(u,v), z(u,v))$ | Parametric surface | ✅ INCLUDE | Standard definition; setup notation for surface integrals |
| 30 | $d\vec{S} = \left(\frac{\partial\vec{r}}{\partial u} \times \frac{\partial\vec{r}}{\partial v}\right)du\,dv$ | Surface area element | ✅ INCLUDE | Essential formula for surface integration; directly used in flux integrals |
| 31 | $\hat{n} = \frac{\vec{\nabla}f}{|\vec{\nabla}f|}$ for implicit surface $f(\vec{r})=C$ | Unit normal to surface | ✅ INCLUDE | Standard formula; used whenever a surface normal is needed |
| 32 | Proof: $\vec{\nabla}f \perp$ tangent to surface $f=C$ (via chain rule) | Derivation | ❌ EXCLUDE | Derivation; the result (entry 31) is what belongs in the sheet |
| 33 | Implicit surface notation: $f(x,y,z)=C$ | Surface — implicit form | ⚠️ BORDERLINE | Useful context for entry 31, but really just notation, not a formula |

---

## Section 7 — Applications

| # | Formula / Definition | Topic Tag | Decision | Reason |
|---|---|---|---|---|
| 34 | Extremum condition: $\vec{\nabla}f = 0$ | Extrema | ✅ INCLUDE | Necessary condition for local extrema; direct analogue of $f'=0$ |
| 35 | Tutorial Example 1: line integral over $\vec{r}(t)=(t,t^3)$ | Worked example | ❌ EXCLUDE | Worked example; not a cheat-sheet entry |
| 36 | Tutorial Example 2: cone parametrisation and surface intersection | Worked example | ❌ EXCLUDE | Worked example; useful for practice but not a cheat-sheet entry |

---

## Items Needing Your Decision (⚠️ BORDERLINE)

| # | Item | Question |
|---|---|---|
| 17 | $df = \partial_x f\,dx + \partial_y f\,dy + \partial_z f\,dz$ | Include as alternative form of entry 10, or redundant? |
| 19 | Limit definition of directional derivative | Include in case the exam asks "state the definition"? |
| 26 | Conservative forces: $W=0$ on closed path | Include as a concept note? |
| 33 | Implicit surface notation $f(x,y,z)=C$ | Include as a parenthetical alongside entry 31, or skip? |
