# Claude Code Goal — LA2 Vault Completion

> Paste everything below the horizontal rule as the `/goal` prompt in Claude Code,
> run from inside `C:\Users\itama\code\la2-course`.

---

## Goal

Complete the Linear Algebra 2 Obsidian vault at `vault/`. Two independent passes are needed for every chapter:

1. **Correction pass** — compare each chapter's `01-lecture.md` against the Yehuda source chunks and fix any missing, incorrect, or misrepresented content.
2. **Natural Deduction (ND) pass** — every proof that currently exists only as prose gets a Natural Deduction table appended immediately after it.

Each pass produces its own **branch and PR** per chapter so the human can review them independently. The ND branch for a chapter is always cut from the tip of that chapter's correction branch — never from `main` — so no rebases are needed.

---

## Project layout

```
la2-course/
  vault/
    ch01-eigenvalues/01-lecture.md
    ch02-diagonalization/01-lecture.md
    ... (ch03 through ch13)
    ITAMAR-NOTES-FOR-CLAUDE/
      notes for how to write proofs.md   ← ND table spec and worked example
  scripts/chunks/lecture/
    lec_001_*.txt  ...  lec_218_*.txt   ← Yehuda 2019 source, one chunk per item
  scripts/copy-pdf-to-vault-SKILL.md    ← transcription conventions
  CLAUDE.md                             ← project rules (language, callout types, tags)
  research/chunk_audit_ch05_ch18.md     ← prior coverage audit (reference)
```

Read `vault/ITAMAR-NOTES-FOR-CLAUDE/notes for how to write proofs.md` before writing any ND table. It contains the full spec and a worked example you must follow exactly.

---

## Chapter → chunk mapping

| Chapter | Vault folder | Chunk range (approx) |
|---------|-------------|----------------------|
| ch01 | ch01-eigenvalues | lec_001 – lec_007 |
| ch02 | ch02-diagonalization | lec_008 – lec_009 |
| ch03 | ch03-matrix-eigenvalues | lec_010 – lec_018 |
| ch04 | ch04-characteristic-poly | lec_019 – lec_028 |
| ch05 | ch05-triangulation | lec_029 – lec_060 |
| ch06 | ch06-cayley-hamilton | lec_061 – lec_075 |
| ch07 | ch07-rings | lec_076 – lec_090 |
| ch08 | ch08-fields | lec_091 – lec_103 |
| ch09 | ch09-minimal-poly | lec_104 – lec_120 |
| ch10 | ch10-jordan | lec_121 – lec_145 |
| ch11 | ch11-inner-product | lec_146 – lec_170 |
| ch12 | ch12-spectral | lec_171 – lec_195 |
| ch13 | ch13-polar-decomposition | lec_196 – lec_218 |

These ranges are approximate. Verify boundaries by reading chunk filenames — they encode the theorem/definition number.

---

## Branching strategy

For every chapter `chXX`:

```
main
 └── vault/chXX-<slug>/correction          ← branched from main
      └── vault/chXX-<slug>/nd-proofs      ← branched from correction tip
```

- **Never** branch `nd-proofs` from `main`.
- **Never** branch `nd-proofs` from another chapter's branch.
- The ND branch is cut **after the correction branch's final commit**, so it builds on the corrected content and produces a clean diff (only ND tables, no correction noise).

### PR targets

| PR | Title | Source branch | Target branch |
|----|-------|--------------|---------------|
| PR-A | `[Correction] chXX — <name>` | `vault/chXX/correction` | `main` |
| PR-B | `[ND Proofs] chXX — <name>` | `vault/chXX/nd-proofs` | `vault/chXX/correction` |

PR-B targets the correction branch, not `main`. When the human merges PR-A into `main`, they will then retarget PR-B to `main` (GitHub shows a "Change base branch" button) — at that point the diff for PR-B will show only the ND tables. This design means **zero rebases are ever required**.

---

## Pass 1 — Correction

### Branch
```bash
git checkout -b vault/chXX-<slug>/correction main
```

### What to do
1. Read the chapter's `01-lecture.md` in full.
2. Read every chunk in the chapter's range (`scripts/chunks/lecture/lec_XXX_*.txt`).
3. For each chunk, check whether its content is faithfully represented in the vault:
   - **Missing item** → add it in the right place using the callout conventions in `CLAUDE.md`.
   - **Wrong statement** → correct it; add a one-line HTML comment `<!-- corrected: <what changed> -->` directly after the affected line.
   - **Incomplete proof** → fill in the missing steps inside the existing `**הוכחה:**` block.
   - **Wrong theorem number** → fix to match the source.
4. Do **not** add ND tables in this pass. Do **not** touch `02-tirgul.md`, `03-exercises.md`, or `04-flashcards.md`.
5. Commit: `git commit -m "correction: chXX — align with Yehuda source chunks"`.
6. Push and open PR-A targeting `main`.

---

## Pass 2 — Natural Deduction tables

### Branch
```bash
git checkout -b vault/chXX-<slug>/nd-proofs vault/chXX-<slug>/correction
```
(Cut from the correction branch tip, not from `main`.)

### ND table format — read the spec first

Before writing any table, re-read the worked example in
`vault/ITAMAR-NOTES-FOR-CLAUDE/notes for how to write proofs.md`.

Key rules (summary only — the file is authoritative):

1. **Callout type and title**
   ```markdown
   > [!proof]+ Natural Deduction — Proof N
   ```
   Use `+` (default open). If the proof has no variant name, use `Proof 1`. If there are named variants (e.g. "הוכחה 1 (שלושה תנאים)" and "הוכחה 2 (גרעין)"), produce one ND callout per proof.

2. **Placement**
   The ND callout is a **top-level sibling** placed immediately after the `[!abstract]` (or `[!note]`) callout that contains the prose proof. It is **not** nested inside the theorem callout. Example structure:
   ```markdown
   > [!abstract] משפט 1.8 — ...
   > ...prose proof... $\blacksquare$

   > [!proof]+ Natural Deduction — Proof 1
   > | # | Claim | Justification |
   ```

3. **Column order and language**
   Columns are `# | Claim | Justification` — left to right, in English.
   Every claim is written in English (`let`, `assume`, `then`, etc. — not Hebrew).

4. **Algebraic chain substeps**
   When a step involves a chain of equalities, break it into sub-rows numbered `x.0`, `x.1`, `x.2`, …:
   - Row `x.0`: `$\text{expression} =$` with `&emsp;&emsp;<small>(show ...)</small>` in the Justification column.
   - Rows `x.1+`: `&emsp;$= \text{next form}$` in the Claim column; justification in the Justification column.

   Example:
   ```markdown
   | 4.0 | $T(v+u) =$ | &emsp;&emsp;<small>(show $v+u \in V_\lambda$)</small> |
   | 4.1 | &emsp;$= Tv + Tu$ | linearity of $T$ |
   | 4.2 | &emsp;$= \lambda v + \lambda u$ | row 3 |
   | 4.3 | &emsp;$= \lambda(v+u)$ | distributivity |
   ```

5. **Do not alter the prose proof** — only add the sibling ND callout after it.

6. **Short proofs** — if a proof is a single sentence (e.g. "הוכחה 2 (גרעין): $V_\lambda=\ker(T-\lambda I)$, וגרעין של כל טרנספורמציה לינארית הינו תת-מרחב"), it still gets its own ND table, even if it has only 2–3 rows.

### What to do
1. Read the chapter's `01-lecture.md` (now on the correction branch — fully corrected content).
2. Identify every prose proof block. A proof block starts with `**הוכחה` and ends at `$\blacksquare$`.
3. For each proof, generate the ND table and insert it as a new top-level callout immediately after the closing `>` line of the containing `[!abstract]` block.
4. Commit: `git commit -m "nd-proofs: chXX — add Natural Deduction tables to all proofs"`.
5. Push and open PR-B targeting the **correction branch** (`vault/chXX-<slug>/correction`). Include in the PR description: "Targets the correction branch. After that PR merges to main, please retarget this PR to main — the diff will then show only ND tables."

---

## Execution order

Work chapter by chapter: complete both branches for `ch01` before starting `ch02`.

Within a chapter:
1. Create and push the correction branch → open PR-A.
2. Immediately (without waiting for review) cut the ND branch from the correction tip.
3. Write ND tables → commit → push → open PR-B.
4. Move to next chapter.

The human reviews PRs asynchronously and merges in order (PR-A first, then retargets and merges PR-B).

---

## Callout conventions (from CLAUDE.md)

| Type | Callout |
|------|---------|
| Definition | `> [!abstract] הגדרה N.M — <name>` |
| Theorem / Claim | `> [!abstract] משפט / טענה N.M — <name>` |
| Remark | `> [!note] הערה N.M` |
| Example | `> [!example] דוגמה N.M` |
| Corollary | `> [!abstract] מסקנה N.M` |
| ND proof table | `> [!proof]+ Natural Deduction — Proof N` |

All vault content (definitions, theorems, remarks) is in **Hebrew**. ND table content (claims and justifications) is in **English**. LaTeX math is standard `$...$` / `$$...$$` throughout.

---

## Definition of done per chapter

- [ ] `vault/chXX/correction` pushed + PR-A open (target: `main`)
- [ ] `vault/chXX/nd-proofs` pushed + PR-B open (target: correction branch, with retarget note)
- [ ] Both PR descriptions name what changed and how many items were corrected / how many proofs received ND tables
