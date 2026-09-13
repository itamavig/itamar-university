# Goal: Build LA2 Concept Graph

Build a concept graph for the Obsidian vault at `vault/`. The graph lives entirely in a new folder `vault/concept-graph/` and must not touch any existing vault files.

---

## What to build

An Obsidian wiki-link graph where each node is a mathematical concept (theorem, definition, condition, property, lemma, corollary) and each edge is a logical relationship between two concepts. Obsidian renders this as an interactive graph when you enable **Show arrows** in Graph View settings.

Edge semantics:
- **Bidirectional (iff / שקול)**: file A contains `[[B]]` AND file B contains `[[A]]`. In Obsidian's graph with arrows enabled, this shows two opposite arrows.
- **Unidirectional (if / implies / גורר)**: only file A contains `[[B]]`. Shows one arrow A→B.

---

## Step 1 — Read the vault

Process every `01-lecture.md` and `02-tirgul.md` across all chapters in `vault/`. Do NOT read `03-exercises.md` or `04-flashcards.md`.

For each file, extract:

### Named concepts
Any `[!abstract]` callout whose title contains one of these Hebrew types:
- `הגדרה` (definition)
- `משפט` (theorem)
- `מסקנה` (corollary)
- `למה` (lemma)
- `טענה` (claim/proposition)

The concept name is the part after the dash `—` in the callout title, or the full title if no dash is present. Strip the number prefix (e.g., strip `2.4` from `מסקנה 2.4 — קריטריון ללכסינות`).

Also extract unnamed concepts that appear as subjects/objects in relationship statements (see below).

### Relationships
Within each callout block and in running text, look for:

**IFF (אמ"מ) — creates bidirectional link:**
- `אמ"מ`
- `אם ורק אם`
- `$\iff$`
- `שקול ל` / `שקולים`

**IF/IMPLIES (גורר) — creates unidirectional link A→B:**
- `גורר`
- `$\implies$` / `$\Rightarrow$`
- `מגרר`
- `נובע מ`

For each relationship, identify:
- **Left side**: the concept or condition before the relationship word
- **Right side**: the concept or condition after the relationship word
- Use your Hebrew language understanding to identify concept mentions — they are typically noun phrases referring to mathematical properties or named theorems.

---

## Step 2 — Build the concept index

Create `vault/concept-graph/_index.json` with this structure:

```json
{
  "concepts": [
    {
      "id": "slug-in-kebab-case",
      "canonical_name": "שם עברי קנוני",
      "aliases": ["שם חלופי", "שם אחר"],
      "type": "definition|theorem|corollary|lemma|property|condition",
      "sources": ["ch02-diagonalization/01-lecture", "ch09-minimal-poly/01-lecture"]
    }
  ],
  "relationships": [
    {
      "from": "concept-slug-a",
      "to": "concept-slug-b",
      "type": "iff|if",
      "source_file": "ch09-minimal-poly/01-lecture",
      "description": "optional short description of the relationship"
    }
  ],
  "built_at": "ISO timestamp",
  "source_files_processed": ["list of files"]
}
```

**Merging identical concepts**: If the same mathematical object appears under multiple names across files (e.g., `לכסינות` and `ניתן לאלכסון`), create ONE concept node with aliases. Use the most explicit/formal name as canonical. When uncertain, keep separate and note as potential duplicate in a `"possible_merge"` field.

**Slug rules**: Use the canonical Hebrew name directly as the file slug (Obsidian handles Hebrew filenames). Replace spaces with `-`. Example: `לכסינות`, `הפולינום-המינימלי`, `קריטריון-ריבוי-גיאומטרי`.

---

## Step 3 — Generate concept node files

For each concept in the index, create `vault/concept-graph/[slug].md`:

```markdown
---
aliases: [canonical_name, alias1, alias2]
type: theorem           ← use the concept type
concept-graph: true     ← allows filtering in Obsidian graph
auto-generated: true
---
# [canonical_name]

[One-line description if extractable from source, else omit]

[IFF links go here as plain wiki-links — one per line or separated by ·]
[[iff-concept-slug-a]]
[[iff-concept-slug-b]]

**גורר:**
[[implied-by-this-concept-a]]
[[implied-by-this-concept-b]]

**מקורות:**
[[../ch02-diagonalization/01-lecture|פרק 2 — הרצאה]]
[[../ch09-minimal-poly/01-lecture|פרק 9 — הרצאה]]

<!-- auto-generated — edit _index.json and re-run scripts/build_concept_graph.py -->
```

**Critical**: For iff relationships, both concept files must link to each other. For if (A→B), only A's file links to B.

Source links use relative paths from `vault/concept-graph/` to the chapter file. The `[[../ch02-diagonalization/01-lecture|display name]]` format keeps the vault graph connected to content.

---

## Step 4 — Write the build script

After generating the initial graph, write `scripts/build_concept_graph.py`:

```
Purpose: Full rebuild of vault/concept-graph/ from vault source files.
Usage: python scripts/build_concept_graph.py [--vault PATH] [--dry-run]

The script:
1. Reads all 01-lecture.md and 02-tirgul.md files
2. Calls claude (Claude Code CLI) with a targeted extraction prompt per file
3. Merges all extracted data into _index.json
4. Generates .md node files from the index
5. Prints a summary: X concepts, Y relationships, Z files processed
```

The script invokes Claude Code CLI as a subprocess for extraction (since Hebrew math requires semantic understanding, not just regex). Use:
  `claude -p "[extraction prompt]" --output-format json`

The extraction prompt per file should be:
> "You are extracting mathematical concepts and relationships from a Hebrew linear algebra course note. From the following markdown, list: (1) all named mathematical concepts (theorems, definitions, conditions, properties) with their exact Hebrew names; (2) all logical relationships between pairs of concepts — specify 'iff' or 'if', and identify left/right concept. Output JSON only: {concepts: [...], relationships: [...]}. Content:\n\n[file content]"

---

## Step 5 — Write the update script

Write `scripts/update_concept_graph.py`:

```
Purpose: Incremental update when a vault file is added or changed.
Usage: python scripts/update_concept_graph.py --file vault/ch09-minimal-poly/01-lecture.md

The script:
1. Reads _index.json
2. Removes all entries whose source is the specified file
3. Runs extraction on the new file content (via claude CLI)
4. Merges new concepts/relationships into the index
5. Regenerates only the affected node files
6. Reports what changed
```

---

## Output summary

When done, print:
- Number of concepts extracted per chapter
- Total concepts, total relationships (iff vs if)
- List any concepts flagged as possible duplicates
- Confirm `vault/concept-graph/` created with N files

## Constraints

- Do NOT modify any file outside `vault/concept-graph/` and `scripts/`
- Preserve existing `_index.json` if present — merge, don't overwrite (unless `--rebuild` flag)
- All concept node files must have `concept-graph: true` in frontmatter (for Obsidian graph filtering)
- Hebrew filenames are fine; avoid spaces (use `-` instead)
