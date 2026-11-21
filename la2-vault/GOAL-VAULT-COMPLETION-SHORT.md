# Claude Code Goal — LA2 Vault Completion (compact)

> Paste everything below the horizontal rule as the `/goal` prompt in Claude Code,
> run from inside `C:\Users\itama\code\la2-course`.

---

## Goal
Complete the LA2 Obsidian vault. Two passes per chapter, each with its own branch+PR:
1. **Correction** — fix/add content vs. Yehuda source chunks
2. **ND** — append Natural Deduction table after every prose proof

## Layout
- `vault/chXX-<slug>/01-lecture.md` — edit target
- `scripts/chunks/lecture/lec_NNN_*.txt` — Yehuda source
- `vault/ITAMAR-NOTES-FOR-CLAUDE/notes for how to write proofs.md` — ND spec (authoritative)
- `research/chunk_audit_ch05_ch18.md` — prior coverage audit (reference)
- `CLAUDE.md` — project rules

## Chapter → chunks
ch01 lec_001-007 | ch02 lec_008-009 | ch03 lec_010-018 | ch04 lec_019-028 | ch05 lec_029-060 | ch06 lec_061-075 | ch07 lec_076-090 | ch08 lec_091-103 | ch09 lec_104-120 | ch10 lec_121-145 | ch11 lec_146-170 | ch12 lec_171-195 | ch13 lec_196-218

## Branching
```
main → vault/chXX-<slug>/correction → vault/chXX-<slug>/nd-proofs
```
- PR-A title: `[Correction] chXX — <name>` → target: `main`
- PR-B title: `[ND Proofs] chXX — <name>` → target: correction branch
- PR-B description must say: "Targets the correction branch. After PR-A merges to main, please retarget this PR to main — the diff will then show only ND tables."

## Pass 1 — Correction
```bash
git checkout -b vault/chXX-<slug>/correction main
```
1. Read `01-lecture.md` + all chunks in range
2. Add missing items; fix wrong statements (append `<!-- corrected: ... -->`); complete proofs; fix theorem numbers
3. Skip ND tables. Skip `02-tirgul.md`, `03-exercises.md`, `04-flashcards.md`
4. Commit `correction: chXX — align with Yehuda source chunks` → push → PR-A → main

## Pass 2 — ND Tables
```bash
git checkout -b vault/chXX-<slug>/nd-proofs vault/chXX-<slug>/correction
```
Read `vault/ITAMAR-NOTES-FOR-CLAUDE/notes for how to write proofs.md` first — it overrides everything below.

Key rules:
- Callout: `> [!proof]+ Natural Deduction — Proof N` (`+` = default open)
- Placement: top-level sibling immediately after the `[!abstract]` (or `[!note]`) block that contains the prose proof — NOT nested inside it
- Columns: `# | Claim | Justification` — all claims in English
- Named proof variants (e.g. "הוכחה 1 (שלושה תנאים)" / "הוכחה 2 (גרעין)") → one ND table per variant, titled "Proof 1", "Proof 2", etc.
- Even 1-sentence proofs get a table
- Algebraic chains: substep rows `x.0`, `x.1`, `x.2`… Row `x.0`: Claim = `$expr =$`, Justification = `&emsp;&emsp;<small>(show ...)</small>`; rows `x.1+`: Claim = `&emsp;$= \text{next}$`, Justification = reason
- Don't alter the prose proof

Proof blocks: `**הוכחה` … `$\blacksquare$`

Commit `nd-proofs: chXX — add Natural Deduction tables to all proofs` → push → PR-B → correction branch

## Execution
Per chapter: correction → PR-A → cut ND branch → ND tables → PR-B → next chapter. Don't wait for review.

## Callouts
- Def/Thm/Claim/Corollary: `> [!abstract] הגדרה/משפט/טענה/מסקנה N.M — <name>`
- Remark: `> [!note] הערה N.M`
- Example: `> [!example] דוגמה N.M`
- ND table: `> [!proof]+ Natural Deduction — Proof N`

Hebrew content; ND claims in English; LaTeX `$...$` / `$$...$$`.

## Done per chapter
- [ ] correction branch + PR-A open (→ main)
- [ ] nd-proofs branch + PR-B open (→ correction, with retarget note)
- [ ] Both PRs describe changes + item counts
