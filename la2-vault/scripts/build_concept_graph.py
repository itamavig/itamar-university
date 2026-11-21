#!/usr/bin/env python3
"""
build_concept_graph.py — Full (re)build of the LA2 concept graph.

Usage:
    python scripts/build_concept_graph.py                 # extract + merge + generate
    python scripts/build_concept_graph.py --dry-run       # list files, no claude calls, no writes
    python scripts/build_concept_graph.py --rebuild       # ignore existing _index.json, start fresh
    python scripts/build_concept_graph.py --from-index    # skip extraction, regenerate nodes from _index.json
    python scripts/build_concept_graph.py --vault PATH    # use a different vault directory

Pipeline:
    1. Collect all vault/ch*/01-lecture.md and vault/ch*/02-tirgul.md files
    2. Per file, call `claude -p "<extraction prompt>" --output-format json`
       (semantic extraction of Hebrew concepts/relationships)
    3. Merge extractions into vault/concept-graph/_index.json
       (preserves an existing index unless --rebuild is passed)
    4. Generate one node .md file per concept
    5. Print a summary: concepts per chapter, totals, possible merges, file count

Requirements:
    - `claude` CLI on PATH (only for extraction; --from-index / --dry-run need none)
"""

import argparse
import json
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
sys.path.insert(0, str(SCRIPT_DIR))

# Hebrew output on Windows consoles (cp1252 chokes otherwise)
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

import update_concept_graph as ucg  # shared helpers (extraction, merging, node generation)


def collect_source_files(vault_dir: Path) -> list[Path]:
    """All 01-lecture.md and 02-tirgul.md files across chapter directories."""
    files = []
    for chapter_dir in sorted(vault_dir.glob("ch*")):
        if not chapter_dir.is_dir():
            continue
        for name in ("01-lecture.md", "02-tirgul.md"):
            f = chapter_dir / name
            if f.exists():
                files.append(f)
    return files


def empty_index() -> dict:
    return {
        "concepts": [],
        "relationships": [],
        "built_at": None,
        "source_files_processed": [],
    }


def print_summary(index: dict, graph_dir: Path) -> None:
    concepts = index.get("concepts", [])
    relationships = index.get("relationships", [])

    per_chapter = Counter()
    for c in concepts:
        chapters = {src.split("/")[0] for src in c.get("sources", [])}
        for ch in chapters:
            per_chapter[ch] += 1

    print("\n=== Concept graph summary ===")
    print("Concepts per chapter (a concept sourced from several chapters counts in each):")
    for ch in sorted(per_chapter):
        print(f"  {ch}: {per_chapter[ch]}")

    iff_count = sum(1 for r in relationships if r.get("type") == "iff")
    if_count = sum(1 for r in relationships if r.get("type") == "if")
    print(f"Total concepts: {len(concepts)}")
    print(f"Total relationships: {len(relationships)} (iff: {iff_count}, if: {if_count})")

    merges = [c["id"] for c in concepts if c.get("possible_merge")]
    if merges:
        print(f"Possible duplicates (possible_merge=true): {', '.join(merges)}")
    else:
        print("Possible duplicates: none flagged")

    if graph_dir.exists():
        n_files = sum(1 for _ in graph_dir.iterdir() if _.is_file())
        print(f"Files in {graph_dir}: {n_files}")


def main():
    parser = argparse.ArgumentParser(description="Full rebuild of the LA2 concept graph.")
    parser.add_argument("--vault", metavar="PATH", default=str(ucg.VAULT_DIR),
                        help=f"Path to vault directory (default: {ucg.VAULT_DIR})")
    parser.add_argument("--dry-run", action="store_true",
                        help="List source files and current index stats; no extraction, no writes")
    parser.add_argument("--rebuild", action="store_true",
                        help="Start from an empty index instead of merging into the existing one")
    parser.add_argument("--from-index", action="store_true",
                        help="Skip extraction; regenerate all node files from the existing _index.json")
    args = parser.parse_args()

    vault_dir = Path(args.vault).resolve()
    graph_dir = vault_dir / "concept-graph"
    index_file = graph_dir / "_index.json"

    # Point the shared helpers at the chosen vault
    ucg.VAULT_DIR = vault_dir
    ucg.GRAPH_DIR = graph_dir
    ucg.INDEX_FILE = index_file

    source_files = collect_source_files(vault_dir)
    print(f"Vault:  {vault_dir}")
    print(f"Graph:  {graph_dir}")
    print(f"Source files found: {len(source_files)}")

    if args.dry_run:
        for f in source_files:
            print(f"  would process: {ucg.file_to_source_key(f)}")
        if index_file.exists():
            with open(index_file, encoding="utf-8") as fh:
                index = json.load(fh)
            print("\nExisting index found:")
            print_summary(index, graph_dir)
        else:
            print("\nNo existing index; a full run would create it.")
        print("\nDry run — nothing was written.")
        return

    # Load or initialize index
    if args.rebuild or not index_file.exists():
        index = empty_index()
        if args.rebuild:
            print("Rebuild requested: starting from an empty index.")
    else:
        with open(index_file, encoding="utf-8") as fh:
            index = json.load(fh)
        print(f"Merging into existing index ({len(index.get('concepts', []))} concepts).")

    graph_dir.mkdir(parents=True, exist_ok=True)

    if not args.from_index:
        skipped = []
        for f in source_files:
            source_key = ucg.file_to_source_key(f)
            print(f"\nProcessing {source_key}")
            ucg.strip_source_from_index(index, source_key)
            extracted = ucg.extract_from_file(f)
            if not extracted.get("concepts") and not extracted.get("relationships"):
                skipped.append(source_key)
            new_c, new_r = ucg.merge_extraction_into_index(index, extracted, source_key)
            print(f"  merged: +{new_c} concepts, +{new_r} relationships")
            processed = set(index.get("source_files_processed", []))
            processed.add(source_key)
            index["source_files_processed"] = sorted(processed)
        if skipped:
            print(f"\nFiles with no extracted content (skipped/empty): {', '.join(skipped)}")

    # Save index
    index["built_at"] = datetime.now(timezone.utc).isoformat()
    with open(index_file, "w", encoding="utf-8") as fh:
        json.dump(index, fh, ensure_ascii=False, indent=2)
    print(f"\nIndex written: {index_file}")

    # Generate all node files
    for concept in index.get("concepts", []):
        ucg.generate_node_file(index, concept)
    print(f"Node files generated: {len(index.get('concepts', []))}")

    print_summary(index, graph_dir)


if __name__ == "__main__":
    main()
