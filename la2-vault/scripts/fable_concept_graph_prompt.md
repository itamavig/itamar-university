Build a concept graph for a Hebrew Linear Algebra 2 Obsidian vault at `vault/`. Output only to `vault/concept-graph/` and `scripts/`. Do NOT touch any other vault files.

**Edge types:**
- **IFF (bidirectional):** file A has `[[B]]` AND file B has `[[A]]`
- **IF (unidirectional):** only file A has `[[B]]` (A→B)

**Step 1 — Extract**

Read every `vault/ch*/01-lecture.md` and `vault/ch*/02-tirgul.md`. Skip `03-exercises.md` and `04-flashcards.md`.

**Concepts:** from `[!abstract]` callouts titled with `הגדרה`, `משפט`, `מסקנה`, `למה`, or `טענה`. Name = part after `—` (strip number prefix like `2.4`).

**Relationships:**

| Signal | Type |
|--------|------|
| `אמ"מ`, `אם ורק אם`, `$\iff$`, `שקול ל`, `שקולים` | IFF |
| `גורר`, `$\implies$`, `$\Rightarrow$`, `מגרר`, `נובע מ` | IF (A→B) |

**Step 2 — Build `vault/concept-graph/_index.json`**

```json
{
  "concepts": [
    {
      "id": "hebrew-kebab-slug",
      "canonical_name": "שם עברי",
      "aliases": ["שם נוסף"],
      "type": "definition|theorem|corollary|lemma|property|condition",
      "sources": ["ch02-diagonalization/01-lecture"]
    }
  ],
  "relationships": [
    {
      "from": "slug-a", "to": "slug-b",
      "type": "iff|if",
      "source_file": "ch09-minimal-poly/01-lecture",
      "description": "optional"
    }
  ],
  "built_at": "<ISO timestamp>",
  "source_files_processed": ["..."]
}
```

**Slugs:** Hebrew canonical name, spaces → `-`. Example: `הפולינום-המינימלי`.
**Duplicates:** same concept under different names → one node with aliases. If uncertain, keep separate with `"possible_merge": true`.

**Step 3 — Node files**

For each concept create `vault/concept-graph/[slug].md`:

```markdown
---
aliases: [canonical_name, alias1]
type: theorem
concept-graph: true
auto-generated: true
---
# [canonical_name]

[One-line description if extractable]

[[iff-concept-a]]

**גורר:**
[[implied-concept-a]]

**מקורות:**
[[../ch02-diagonalization/01-lecture|פרק 2 — הרצאה]]
```

IFF pairs: BOTH files link each other. IF (A→B): only A links B.

**Step 4 — `scripts/build_concept_graph.py`**

Full rebuild. Usage: `python scripts/build_concept_graph.py [--vault PATH] [--dry-run]`

1. Read all `01-lecture.md` + `02-tirgul.md`
2. Per file, call: `claude -p "[prompt]" --output-format json`
3. Merge into `_index.json`; generate node `.md` files
4. Print: X concepts, Y relationships, Z files

Extraction prompt: `"Extract from this Hebrew linear algebra note: (1) named concepts with exact Hebrew names; (2) logical relationships — 'iff' or 'if', left/right concept. JSON only: {concepts:[...], relationships:[...]}. Content:\n\n[file content]"`

**Step 5 — `scripts/update_concept_graph.py`**

Incremental. Usage: `python scripts/update_concept_graph.py --file vault/ch09.../01-lecture.md`

1. Read `_index.json`; remove entries from that file
2. Re-extract via claude CLI; merge; regenerate affected nodes
3. Report changes

**Constraints**

- Only write to `vault/concept-graph/` and `scripts/`
- All node files: `concept-graph: true` in frontmatter
- Preserve `_index.json` unless `--rebuild` flag
- Hebrew filenames OK; no spaces (use `-`)

**When done, print**

- Concepts per chapter; total concepts + relationships (iff vs if)
- Any possible-duplicate flags
- `vault/concept-graph/` file count
