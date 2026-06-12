---
name: copy-pdf-to-vault
description: >
  Recipe for faithfully transcribing a long Hebrew mathematical PDF into an Obsidian vault,
  chunk by chunk, with LLM verification of each chunk. Use whenever a PDF source needs to
  be converted into structured vault markdown (lecture notes, tirgul, exercises).
---

# Copying a Long PDF into the Vault

## Background & why this matters

Copying a 50–400 line PDF in one shot reliably fails: context overflow causes truncation,
hallucination, or skipped sections. The safe method is to split first (non-LLM), then
transcribe one logical chunk at a time, verifying each before moving on.

---

## Step 0 — Git baseline (MANUAL — sandbox cannot run git)

Before touching any vault file, ask the user to run in their terminal:
```bash
cd la2-course
git add -A && git commit -m "pre-session baseline: before transcribing [PDF name]"
```
Remind them again at the end of each session: `git add -A && git commit -m "..."`.

---

## Step 1 — Extract raw text from PDF

```bash
pdftotext -layout -f FIRST_PAGE -l LAST_PAGE "sources/SOURCE.pdf" /tmp/source_raw.txt
```

- Use `-f` / `-l` to extract only the relevant page range (e.g. ch01 is pages 1–12).
- The output will contain Unicode bidi markers (`‪`, `‫`, `‬`) — this is normal.

---

## Step 2 — Split into chunks (non-LLM)

Use `scripts/split_pdf.py`. Choose mode based on PDF type:

| Mode       | Use for                              | Splits on                              |
|------------|--------------------------------------|----------------------------------------|
| `lecture`  | Yehuda lecture PDF                   | `הגדרה 1.2`, `משפט 2.1`, etc.         |
| `tirgul`   | Weekly tirgul PDFs                   | Standalone `הגדרה`, `דוגמה`, etc.     |
| `hw`       | Homework PDFs                        | Question numbers `.1`, `.2`, etc.      |

```bash
python3 scripts/split_pdf.py /tmp/source_raw.txt /tmp/chunks PREFIX MODE
```

Inspect the chunk list. Any chunk over ~80 lines should be reviewed — it may contain
multiple logical units that need sub-splitting. Chunks of 2–40 lines are ideal.

---

## Step 3 — Transcribe chunk by chunk

For each chunk file (in order):

1. **Read the raw chunk** with the Read tool or bash `cat`.
2. **Transcribe** it into the appropriate vault callout format:
   - Definitions → `[!abstract]` with Hebrew title
   - Theorems/Claims → `[!abstract]`
   - Remarks → `[!note]` or inline prose
   - Examples → `[!example]`
   - Proofs → `[!proof]-` (collapsed, prose only — ND tables are second pass)
3. **Write** the new content to the vault file with Write/Edit tools.
4. **Verify** (see Step 4).
5. Ask the user to commit: `git commit -am "ch01/01-lecture: add הגדרה 1.2"`.

**Rules:**
- Hebrew content only (no translation).
- Expand all ראשי תיבות (abbreviations) EXCEPT אמ"מ and חח"ע.
- Preserve all math as LaTeX (`$...$` inline, `$$...$$` display).
- Do NOT rephrase or improve prose during transcription — fidelity first.
- Do NOT add ND tables during this pass.

---

## Step 4 — Verify each chunk

After writing a chunk to the vault file, run a verification:

**LLM comparison (primary):** Feed both the raw chunk text and the vault markdown to a
verification prompt:
> "Compare these two versions of the same mathematical content. List any: (1) missing definitions/theorems/claims, (2) missing examples, (3) incorrect or missing math expressions, (4) missing proof steps. Be specific."

**Count check (secondary):**
```bash
# Count section keywords in raw source chunk
grep -c 'הגדרה\|משפט\|טענה\|הוכחה\|דוגמה' /tmp/chunks/PREFIX/CHUNK.txt

# Count callout headers in vault output
grep -c '\[!.*\]' vault/chXX/01-lecture.md
```

If verification fails: fix the vault file, re-verify, then commit.

---

## Step 5 — After all chunks done

1. Read the entire completed vault file end to end.
2. Cross-check: count total definitions/theorems/examples vs. the raw text.
3. Only then: rephrase, improve prose, expand abbreviations if any were missed.
4. Second pass (separate session): add ND proof tables.
5. Update `_index.md` status and `progress-log.md`.
6. Ask user to commit: `git commit -am "ch01/01-lecture: complete transcription, verified"`

---

## Chunk size guidance

| Chunk size   | Action                                                        |
|--------------|---------------------------------------------------------------|
| < 5 lines    | Fine; may batch 2–3 consecutive small chunks together         |
| 5–40 lines   | Ideal; transcribe and verify individually                     |
| 40–80 lines  | Transcribe individually; verify carefully                     |
| > 80 lines   | Sub-split manually before transcribing                        |

---

## Common pitfalls

- **Bidi markers in pdftotext:** The `‪/‫/‬` markers are not content — strip them when
  reading but do not include them in vault output.
- **Matrix notation:** pdftotext often misaligns matrix rows. Always verify matrix LaTeX
  against the original PDF visually.
- **Inline math split across lines:** pdftotext may break a LaTeX expression across two
  lines. Manually join them.
- **Never use sed or awk on vault files** — one wrong command truncates the entire file.
  Use the Edit tool with exact string matching only.
- **Never batch multiple files in one subagent call** — isolation prevents cross-file corruption.
