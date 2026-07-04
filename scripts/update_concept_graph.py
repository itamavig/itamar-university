#!/usr/bin/env python3
"""
update_concept_graph.py — Incremental updater for the LA2 concept graph.

Usage:
    python scripts/update_concept_graph.py --file vault/ch09-minimal-poly/01-lecture.md
    python scripts/update_concept_graph.py --file vault/ch09-minimal-poly/02-tirgul.md
    python scripts/update_concept_graph.py --rebuild          # full rebuild via GRAPH_GOAL

Behaviour:
    1. Reads vault/concept-graph/_index.json
    2. Strips all concepts/relationships whose sole source is the given file
    3. Extracts new concepts/relationships from the file (via claude CLI)
    4. Merges into the index
    5. Regenerates affected node .md files only
    6. Reports changes

Requirements:
    - `claude` CLI must be on PATH (Claude Code)
    - vault/concept-graph/ must exist (run full build first via GRAPH_GOAL.md)
"""

import argparse
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

# Hebrew output on Windows consoles (cp1252 chokes otherwise)
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

# ── Paths ────────────────────────────────────────────────────────────────────

SCRIPT_DIR = Path(__file__).parent
VAULT_DIR = SCRIPT_DIR.parent / "vault"
GRAPH_DIR = VAULT_DIR / "concept-graph"
INDEX_FILE = GRAPH_DIR / "_index.json"
GOAL_FILE = SCRIPT_DIR / "GRAPH_GOAL.md"

# ── Claude extraction prompt ──────────────────────────────────────────────────

EXTRACTION_PROMPT = """\
You are extracting mathematical concepts and relationships from a Hebrew linear algebra course note.

From the markdown content below, extract:
1. All NAMED mathematical concepts: theorems, definitions, conditions, properties, lemmas, corollaries.
   - A concept is named if it has a Hebrew noun phrase describing a mathematical object or property.
   - Include concepts that appear as subjects/objects in relationship statements even if not in a callout.
   - For each concept: provide its exact Hebrew name (canonical), any alternate names/aliases seen, \
     and its type (theorem / definition / corollary / lemma / property / condition).

2. All LOGICAL RELATIONSHIPS between pairs of concepts:
   - "iff" relationships: triggered by אמ"מ / אם ורק אם / $\\iff$ / שקול ל / שקולים
   - "if" relationships: triggered by גורר / $\\implies$ / $\\Rightarrow$ / מגרר / נובע מ
   - For each relationship: identify left-concept and right-concept (the mathematical objects \
     on either side of the relationship word).

Output JSON ONLY — no prose, no markdown fences — in this exact schema:
{
  "concepts": [
    {
      "canonical_name": "שם עברי",
      "aliases": [],
      "type": "definition|theorem|corollary|lemma|property|condition"
    }
  ],
  "relationships": [
    {
      "from_concept": "canonical name of source concept",
      "to_concept": "canonical name of target concept",
      "type": "iff|if",
      "note": "optional one-line description"
    }
  ]
}

Content to process:
"""


# ── Slug helpers ──────────────────────────────────────────────────────────────

def make_slug(hebrew_name: str) -> str:
    """Convert a Hebrew concept name to a filename slug."""
    slug = hebrew_name.strip()
    # Replace spaces and slashes with hyphens
    slug = re.sub(r'[\s/\\]+', '-', slug)
    # Remove characters Obsidian doesn't allow in filenames
    slug = re.sub(r'[<>:"|?*\[\]#^]', '', slug)
    # Collapse multiple hyphens
    slug = re.sub(r'-+', '-', slug).strip('-')
    return slug


# ── Index I/O ─────────────────────────────────────────────────────────────────

def load_index() -> dict:
    if not INDEX_FILE.exists():
        print(f"ERROR: {INDEX_FILE} not found. Run the full build first using GRAPH_GOAL.md.")
        sys.exit(1)
    with open(INDEX_FILE, encoding="utf-8") as f:
        return json.load(f)


def save_index(index: dict) -> None:
    index["last_updated"] = datetime.now(timezone.utc).isoformat()
    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        json.dump(index, f, ensure_ascii=False, indent=2)


# ── Extraction via Claude CLI ─────────────────────────────────────────────────

def extract_from_file(vault_file: Path) -> dict:
    """Call claude CLI to extract concepts and relationships from a vault file."""
    content = vault_file.read_text(encoding="utf-8")
    prompt = EXTRACTION_PROMPT + content

    print(f"  Calling claude CLI for extraction on {vault_file.name}...")
    result = subprocess.run(
        ["claude", "-p", prompt, "--output-format", "json"],
        capture_output=True,
        text=True,
        encoding="utf-8",
    )

    if result.returncode != 0:
        print(f"  WARNING: claude CLI exited with code {result.returncode}")
        print(f"  stderr: {result.stderr[:500]}")
        # Fall back to empty extraction
        return {"concepts": [], "relationships": []}

    # claude --output-format json wraps the response; try to find JSON in output
    output = result.stdout.strip()
    # Try parsing directly
    try:
        return json.loads(output)
    except json.JSONDecodeError:
        # Try to find a JSON block inside the output
        match = re.search(r'\{[\s\S]+\}', output)
        if match:
            try:
                return json.loads(match.group())
            except json.JSONDecodeError:
                pass
        print(f"  WARNING: Could not parse claude output as JSON. Raw output:\n{output[:500]}")
        return {"concepts": [], "relationships": []}


# ── Index manipulation ────────────────────────────────────────────────────────

def file_to_source_key(vault_file: Path) -> str:
    """Convert absolute path to source key used in the index (relative to vault/)."""
    try:
        return str(vault_file.relative_to(VAULT_DIR)).replace("\\", "/").removesuffix(".md")
    except ValueError:
        return str(vault_file).removesuffix(".md")


def strip_source_from_index(index: dict, source_key: str) -> tuple[set, set]:
    """
    Remove all concepts/relationships whose ONLY source is source_key.
    Returns (removed_concept_ids, modified_concept_ids).
    """
    removed_ids = set()
    modified_ids = set()

    new_concepts = []
    for concept in index.get("concepts", []):
        sources = concept.get("sources", [])
        if source_key in sources:
            sources.remove(source_key)
            concept["sources"] = sources
            if not sources:
                removed_ids.add(concept["id"])
            else:
                modified_ids.add(concept["id"])
                new_concepts.append(concept)
        else:
            new_concepts.append(concept)
    index["concepts"] = new_concepts

    # Remove relationships sourced from this file
    index["relationships"] = [
        r for r in index.get("relationships", [])
        if r.get("source_file") != source_key
    ]

    return removed_ids, modified_ids


def find_or_create_concept(index: dict, canonical_name: str, aliases: list, ctype: str, source_key: str) -> str:
    """
    Find existing concept by name/alias match, update it, or create a new one.
    Returns concept id (slug).
    """
    # Search by canonical name or alias
    for concept in index["concepts"]:
        all_names = [concept["canonical_name"]] + concept.get("aliases", [])
        if canonical_name in all_names or any(a in all_names for a in aliases):
            # Merge: add new aliases, update sources
            existing_aliases = set(concept.get("aliases", []))
            existing_aliases.update(aliases)
            existing_aliases.discard(concept["canonical_name"])
            concept["aliases"] = sorted(existing_aliases)
            if source_key not in concept.get("sources", []):
                concept.setdefault("sources", []).append(source_key)
            return concept["id"]

    # New concept
    slug = make_slug(canonical_name)
    # Deduplicate slug if collision
    existing_slugs = {c["id"] for c in index["concepts"]}
    original_slug = slug
    counter = 2
    while slug in existing_slugs:
        slug = f"{original_slug}-{counter}"
        counter += 1

    new_concept = {
        "id": slug,
        "canonical_name": canonical_name,
        "aliases": [a for a in aliases if a != canonical_name],
        "type": ctype,
        "sources": [source_key],
    }
    index["concepts"].append(new_concept)
    return slug


def merge_extraction_into_index(index: dict, extracted: dict, source_key: str) -> tuple[int, int]:
    """
    Merge extracted concepts and relationships into the index.
    Returns (new_concepts_count, new_relationships_count).
    """
    new_concepts = 0
    name_to_id = {}

    for c in extracted.get("concepts", []):
        name = c.get("canonical_name", "").strip()
        if not name:
            continue
        existing_count = sum(1 for x in index["concepts"] if x["canonical_name"] == name)
        cid = find_or_create_concept(
            index,
            name,
            c.get("aliases", []),
            c.get("type", "property"),
            source_key,
        )
        name_to_id[name] = cid
        # Count as new if concept was freshly created
        if existing_count == 0 and any(x["id"] == cid and source_key in x["sources"]
                                        and len(x["sources"]) == 1
                                        for x in index["concepts"]):
            new_concepts += 1

    new_rels = 0
    for r in extracted.get("relationships", []):
        from_name = r.get("from_concept", "").strip()
        to_name = r.get("to_concept", "").strip()
        if not from_name or not to_name:
            continue

        # Resolve names to ids
        from_id = name_to_id.get(from_name)
        to_id = name_to_id.get(to_name)

        # Fall back to slug-based lookup
        if not from_id:
            for concept in index["concepts"]:
                if concept["canonical_name"] == from_name:
                    from_id = concept["id"]
                    break
        if not to_id:
            for concept in index["concepts"]:
                if concept["canonical_name"] == to_name:
                    to_id = concept["id"]
                    break

        if not from_id or not to_id:
            print(f"  WARNING: Could not resolve relationship: '{from_name}' → '{to_name}'")
            continue

        rel_type = r.get("type", "if")
        # Check for duplicate
        already_exists = any(
            x["from"] == from_id and x["to"] == to_id and x["type"] == rel_type
            for x in index["relationships"]
        )
        if not already_exists:
            index["relationships"].append({
                "from": from_id,
                "to": to_id,
                "type": rel_type,
                "source_file": source_key,
                "description": r.get("note", ""),
            })
            new_rels += 1

    return new_concepts, new_rels


# ── Node file generation ──────────────────────────────────────────────────────

def get_concept_by_id(index: dict, cid: str) -> dict | None:
    for c in index["concepts"]:
        if c["id"] == cid:
            return c
    return None


def generate_node_file(index: dict, concept: dict) -> None:
    """Write/overwrite vault/concept-graph/[slug].md for one concept."""
    cid = concept["id"]
    name = concept["canonical_name"]
    aliases = concept.get("aliases", [])
    ctype = concept.get("type", "property")
    sources = concept.get("sources", [])

    # Gather relationships
    iff_targets = []
    if_targets = []  # concepts this one implies
    for rel in index["relationships"]:
        if rel["type"] == "iff":
            if rel["from"] == cid:
                iff_targets.append(rel["to"])
            elif rel["to"] == cid:
                iff_targets.append(rel["from"])
        elif rel["type"] == "if":
            if rel["from"] == cid:
                if_targets.append(rel["to"])

    # Build frontmatter aliases list
    all_aliases = [name] + aliases
    aliases_yaml = "\n".join(f"  - \"{a}\"" for a in all_aliases)

    # Build link sections
    iff_links = "\n".join(f"[[{t}]]" for t in iff_targets) if iff_targets else ""
    if_links = "\n".join(f"[[{t}]]" for t in if_targets) if if_targets else ""

    # Source links (relative path from concept-graph/ to chapter file)
    source_links = []
    for src in sources:
        chapter, _, part = src.partition("/")
        if chapter.startswith("ch"):
            num = chapter[2:].split("-", 1)[0]
            display = f"פרק {num.lstrip('0') or '0'}"
        else:
            display = chapter
        if "lecture" in part:
            kind = "הרצאה"
        elif "tirgul" in part:
            kind = "תרגול"
        else:
            kind = part or chapter
        source_links.append(f"[[../{src}|{display} — {kind}]]")
    source_section = "\n".join(source_links) if source_links else ""

    # Assemble content
    sections = [
        f"---",
        f"aliases:",
        aliases_yaml,
        f"type: {ctype}",
        f"concept-graph: true",
        f"auto-generated: true",
        f"---",
        f"",
        f"# {name}",
        f"",
    ]

    if iff_links:
        sections += [f"**שקול ל (אמ\"מ):**", iff_links, ""]

    if if_links:
        sections += [f"**גורר:**", if_links, ""]

    if source_section:
        sections += [f"**מקורות:**", source_section, ""]

    sections.append("<!-- auto-generated — edit _index.json and re-run build_concept_graph.py -->")

    content = "\n".join(sections)

    node_path = GRAPH_DIR / f"{cid}.md"
    node_path.write_text(content, encoding="utf-8")


def regenerate_affected_nodes(index: dict, affected_ids: set) -> None:
    """Regenerate node files for the given concept ids."""
    for cid in affected_ids:
        concept = get_concept_by_id(index, cid)
        if concept:
            generate_node_file(index, concept)
        else:
            # Concept was removed — delete its node file
            node_path = GRAPH_DIR / f"{cid}.md"
            if node_path.exists():
                node_path.unlink()
                print(f"  Deleted node: {cid}.md")


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Incrementally update the LA2 concept graph.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--file", metavar="PATH",
                       help="Vault file to process (01-lecture.md or 02-tirgul.md)")
    group.add_argument("--rebuild", action="store_true",
                       help="Trigger a full rebuild via GRAPH_GOAL.md (runs claude -g)")
    parser.add_argument("--vault", metavar="PATH", default=str(VAULT_DIR),
                        help=f"Path to vault directory (default: {VAULT_DIR})")
    args = parser.parse_args()

    if args.rebuild:
        print("Triggering full rebuild via claude CLI with GRAPH_GOAL.md...")
        goal_text = GOAL_FILE.read_text(encoding="utf-8")
        subprocess.run(["claude", "-p", goal_text], check=True)
        return

    # ── Incremental update ────────────────────────────────────────────────────

    vault_file = Path(args.file).resolve()
    if not vault_file.exists():
        print(f"ERROR: File not found: {vault_file}")
        sys.exit(1)

    allowed_names = {"01-lecture.md", "02-tirgul.md"}
    if vault_file.name not in allowed_names:
        print(f"WARNING: Expected a 01-lecture.md or 02-tirgul.md file, got: {vault_file.name}")
        print("Proceeding anyway...")

    source_key = file_to_source_key(vault_file)
    print(f"\nProcessing: {source_key}")
    print(f"Index:      {INDEX_FILE}")
    print()

    # Ensure graph dir exists
    GRAPH_DIR.mkdir(parents=True, exist_ok=True)

    # Load index
    index = load_index()
    concepts_before = len(index.get("concepts", []))
    rels_before = len(index.get("relationships", []))

    # Strip old data from this source
    removed_ids, modified_ids = strip_source_from_index(index, source_key)
    if removed_ids:
        print(f"  Removed {len(removed_ids)} concepts that had no other sources: {', '.join(sorted(removed_ids))}")
    if modified_ids:
        print(f"  Updated {len(modified_ids)} concepts (still have other sources)")

    # Extract from new/changed file
    extracted = extract_from_file(vault_file)
    extracted_concepts = extracted.get("concepts", [])
    extracted_rels = extracted.get("relationships", [])
    print(f"  Extracted {len(extracted_concepts)} concepts, {len(extracted_rels)} relationships from claude")

    # Merge into index
    new_c, new_r = merge_extraction_into_index(index, extracted, source_key)

    # Update source file list in index
    processed = set(index.get("source_files_processed", []))
    processed.add(source_key)
    index["source_files_processed"] = sorted(processed)

    # Determine which node files need regeneration
    affected = set()
    affected.update(removed_ids)
    affected.update(modified_ids)
    for c in extracted_concepts:
        name = c.get("canonical_name", "").strip()
        for concept in index["concepts"]:
            if concept["canonical_name"] == name:
                affected.add(concept["id"])
    # Also regenerate nodes linked to newly added iff/if relationships
    for rel in index["relationships"]:
        if rel.get("source_file") == source_key:
            affected.add(rel["from"])
            affected.add(rel["to"])

    print(f"  Regenerating {len(affected)} node files...")
    regenerate_affected_nodes(index, affected)

    # Save updated index
    save_index(index)

    concepts_after = len(index.get("concepts", []))
    rels_after = len(index.get("relationships", []))
    print()
    print(f"Done.")
    print(f"  Concepts: {concepts_before} → {concepts_after} (+{new_c} new)")
    print(f"  Relationships: {rels_before} → {rels_after} (+{new_r} new)")
    print(f"  Node files updated: {len(affected)}")


if __name__ == "__main__":
    main()
