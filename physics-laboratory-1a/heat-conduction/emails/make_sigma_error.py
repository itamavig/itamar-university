"""Writes sigma-error-tamir.tex: the error of sigma (part a) computed two ways, with substitution.
Data: '../heat conduction part a.xlsx' values, copied below (2026-11-09). Run with the free-fall venv."""
import numpy as np

def comb(x, res):
    x = np.array(x, float)
    st = x.std(ddof=1) / np.sqrt(len(x))
    r = res / np.sqrt(12)
    return x.mean(), st, r, np.hypot(st, r)

m = comb([1.27] * 4, 0.01)
t = comb([18.63, 18.6, 18.68, 18.81, 18.61, 18.6, 18.43, 18.58, 18.83, 18.46], 0.01)
d = comb([5.99, 5.88, 5.98, 5.9], 0.01)
Dc = comb([6.01, 6.03, 6.06, 6.0], 0.01)
D = comb([19.91, 19.98, 19.95, 19.98], 0.01)
L, dL = 20.0, 0.1 / np.sqrt(12)
g, dg = 981.0, 10.0
mu0M, f = 0.65, 1.75

a, da = Dc[0] / 2, Dc[3] / 2
r, dr = d[0] / 2, d[3] / 2
w, dw = (D[0] - Dc[0]) / 2, 0.5 * np.hypot(D[3], Dc[3])
sig = 8 * (m[0] * 1e-3) * (g * 1e-2) * (a * 1e-3) ** 2 * t[0] / (
    mu0M ** 2 * np.pi * (r * 1e-3) ** 4 * (L * 1e-2) * (w * 1e-3) * f)

T1 = [("\\frac{\\Delta m}{m}", m[3] / m[0]), ("\\frac{\\Delta g}{g}", dg / g),
      ("\\frac{2\\Delta a}{a}", 2 * da / a), ("\\frac{\\Delta t}{t}", t[3] / t[0]),
      ("\\frac{4\\Delta r_m}{r_m}", 4 * dr / r), ("\\frac{\\Delta L_0}{L_0}", dL / L),
      ("\\frac{\\Delta w}{w}", dw / w)]
S1 = sum(v ** 2 for _, v in T1)
cDc = (2 / Dc[0] + 1 / (D[0] - Dc[0])) * Dc[3]
cD = D[3] / (D[0] - Dc[0])
T2 = [T1[0], T1[1], T1[3], ("\\frac{4\\Delta d}{d}", 4 * d[3] / d[0]), T1[5],
      ("\\left(\\frac{2}{D_{ch}} + \\frac{1}{D - D_{ch}}\\right)\\Delta D_{ch}", cDc),
      ("\\frac{\\Delta D}{D - D_{ch}}", cD)]
S2 = sum(v ** 2 for _, v in T2)
cross = 4 * Dc[3] ** 2 / (Dc[0] * (D[0] - Dc[0]))
assert abs((S2 - S1) - cross) < 1e-12

def sci(v, n):
    e = int(np.floor(np.log10(abs(v))))
    return f"{v/10**e:.{n}f} \\cdot 10^{{{e}}}"

def e3(v): return f"{v*1e3:.3f}"     # in units of 1e-3
def e6(v): return f"{v*1e6:.2f}"     # in units of 1e-6
def rows(T): return " \\\\\n".join(f"$\\displaystyle {n}$ & ${e3(v)}$ & ${e6(v**2)}$" for n, v in T)

def terms(T): return " + ".join(e6(v**2) for _, v in T)

tex = rf"""\documentclass[11pt,a4paper]{{article}}
\usepackage[a4paper,margin=2cm]{{geometry}}
\usepackage{{amsmath}}
\usepackage{{fontspec}}
\usepackage[bidi=basic, main=hebrew, english]{{babel}}
\babelfont[hebrew]{{rm}}{{Times New Roman}}
\newcommand{{\U}}[1]{{\,\mathrm{{#1}}}}
\setlength{{\parindent}}{{0pt}}
\setlength{{\parskip}}{{6pt}}
\pagestyle{{empty}}
\begin{{document}}
\begin{{center}}\large השגיאה ב-$\sigma$ בשתי דרכים (הולכת חום, חלק א׳)\end{{center}}

התוצאה: $\sigma = {sig/1e7:.3f} \cdot 10^7 \U{{S/m}}$. בשתי הדרכים לפי נוסחה (43) בחוברת. $D_{{ch}}$ קוטר התעלה, $D$ הקוטר החיצוני, $d$ גובה המגנט.

\textbf{{דרך א׳: $a$ ו-$w$ בלתי תלויים}}
\[ \left(\frac{{\Delta\sigma}}{{\sigma}}\right)^2 = \left(\frac{{\Delta m}}{{m}}\right)^2 + \left(\frac{{\Delta g}}{{g}}\right)^2 + \left(\frac{{2\Delta a}}{{a}}\right)^2 + \left(\frac{{\Delta t}}{{t}}\right)^2 + \left(\frac{{4\Delta r_m}}{{r_m}}\right)^2 + \left(\frac{{\Delta L_0}}{{L_0}}\right)^2 + \left(\frac{{\Delta w}}{{w}}\right)^2 \]
\[ = ({terms(T1)}) \cdot 10^{{-6}} = {e6(S1)} \cdot 10^{{-6}} \]
\[ \frac{{\Delta\sigma}}{{\sigma}} = {np.sqrt(S1)*100:.3f}\%, \quad \Delta\sigma = {sig*np.sqrt(S1)/1e7:.3f} \cdot 10^7 \U{{S/m}} \]

\textbf{{דרך ב׳: לפי המשתנים שנמדדו ישירות}} ($\sigma \propto \frac{{D_{{ch}}^2}}{{d^4 (D - D_{{ch}})}}$)
\begin{{multline*}}
\left(\frac{{\Delta\sigma}}{{\sigma}}\right)^2 = \left(\frac{{\Delta m}}{{m}}\right)^2 + \left(\frac{{\Delta g}}{{g}}\right)^2 + \left(\frac{{\Delta t}}{{t}}\right)^2 + \left(\frac{{4\Delta d}}{{d}}\right)^2 + \left(\frac{{\Delta L_0}}{{L_0}}\right)^2 \\
+ \left[\left(\frac{{2}}{{D_{{ch}}}} + \frac{{1}}{{D - D_{{ch}}}}\right)\Delta D_{{ch}}\right]^2 + \left(\frac{{\Delta D}}{{D - D_{{ch}}}}\right)^2
\end{{multline*}}
\[ = ({terms(T2)}) \cdot 10^{{-6}} = {e6(S2)} \cdot 10^{{-6}} \]
\[ \frac{{\Delta\sigma}}{{\sigma}} = {np.sqrt(S2)*100:.3f}\%, \quad \Delta\sigma = {sig*np.sqrt(S2)/1e7:.3f} \cdot 10^7 \U{{S/m}} \]

\textbf{{ההפרש}} הוא איבר צולב אחד, כי $D_{{ch}}$ מופיע גם ב-$a$ וגם ב-$w$:
\[ \left(\frac{{\Delta\sigma}}{{\sigma}}\right)^2_{{\text{{ב}}}} - \left(\frac{{\Delta\sigma}}{{\sigma}}\right)^2_{{\text{{א}}}} = \frac{{4\,(\Delta D_{{ch}})^2}}{{D_{{ch}}\,(D - D_{{ch}})}} = {cross*1e6:.2f} \cdot 10^{{-6}} \]
לאחר עיגול, בשתי הדרכים: $\sigma = ({sig/1e7:.2f} \pm {sig*np.sqrt(S1)/1e7:.2f}) \cdot 10^7 \U{{S/m}}$.
\end{{document}}
"""
open("sigma-error-tamir.tex", "w").write(tex)
print(f"sigma={sig:.6e} rel1={np.sqrt(S1):.5%} rel2={np.sqrt(S2):.5%} cross={cross:.4e}")
print(f"rounded: ({sig/1e7:.2f} ± {sig*np.sqrt(S1)/1e7:.2f}) vs ({sig/1e7:.2f} ± {sig*np.sqrt(S2)/1e7:.2f}) e7")
