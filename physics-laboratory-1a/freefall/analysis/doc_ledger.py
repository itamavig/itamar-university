"""Track which units of the shared Google Doc made it into the LaTeX report.

The report rephrases the Doc, so text can't be compared. Instead:
  - the Doc is split into numbered units (one sentence, list item or equation each),
  - every LaTeX passage carries a comment `% src: PLAN-07 PLAN-08` naming the units it covers,
  - units deliberately not carried over get a status in the ledger (dropped / replaced / fixed).

Commands (run from freefall/):
  fetch   download the Doc as Markdown to doc/doc-export.md, images to doc/images/
  sync    split doc-export.md into units and merge into doc/ledger.tsv
          (IDs are matched by exact text, so they stay stable when the partner edits the Doc)
  check   report untransferred units, unknown tags, and units that changed in the Doc
  side S  print each unit of section S next to the LaTeX lines tagged with it

Unit split rules (deterministic):
  - a heading is a line that is entirely **bold** (optionally ending with ':')
  - every other non-empty line is a block; image-definition lines are ignored
  - a block is split into sentences after '.', '?' or '!' followed by whitespace,
    except after a lone Hebrew letter label such as "א." (it stays with what follows)
"""
import base64
import csv
import hashlib
import re
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOC_DIR = ROOT / "doc"
EXPORT = DOC_DIR / "doc-export.md"
IMAGES = DOC_DIR / "images"
LEDGER = DOC_DIR / "ledger.tsv"
REPORT = ROOT / "report"
DOC_ID = "1MUINwf7WtN5xF8mn_HDU8LOiYBhBlKdToIahe57nC-M"

SECTIONS = {
    "מטרות הניסוי": "GOAL",
    "רקע תאורטי": "THEO",
    "רשימת ציוד": "EQUIP",
    "מערכת הניסוי": "SETUP",
    "מהלך הניסוי": "PROC",
    "תכנון עיבוד התוצאות": "PLAN",
    "עיבוד התוצאות": "RES",
    "שאלת מדריך": "QUEST",
    "דיון ומסקנות": "DISC",
}
# todo     = not handled yet (must end up tagged or given another status)
# dropped  = deliberately left out (note says why)
# replaced = covered by something generated (figure, numbers.tex, table)
# fixed    = carried over with a content correction approved by the user
# gone     = no longer in the Doc (partner removed or edited it)
STATUSES = {"todo", "dropped", "replaced", "fixed", "gone"}
FIELDS = ["id", "status", "note", "hash", "text"]
TAG = re.compile(r"%\s*src:\s*(.+)$")
IMAGE_DEF = re.compile(r"^\[(image\d+)\]:\s*<data:image/(\w+);base64,([^>]+)>")


def fetch():
    url = f"https://docs.google.com/document/d/{DOC_ID}/export?format=md"
    raw = urllib.request.urlopen(url).read().decode("utf-8")
    DOC_DIR.mkdir(exist_ok=True)
    IMAGES.mkdir(exist_ok=True)
    text_lines = []
    for line in raw.splitlines():
        m = IMAGE_DEF.match(line)
        if m:
            name, ext, data = m.groups()
            (IMAGES / f"{name}.{ext}").write_bytes(base64.b64decode(data))
        else:
            text_lines.append(line)
    EXPORT.write_text("\n".join(text_lines) + "\n", encoding="utf-8")
    print(f"wrote {EXPORT.relative_to(ROOT)} and {len(list(IMAGES.iterdir()))} images")


def clean(s):
    s = re.sub(r"\\([^\w\s]|_)", r"\1", s)      # markdown escapes: \+ \- \. \* \_
    s = s.replace("**", "")
    s = re.sub(r"^\s*(?:\d+\.|-)\s+", "", s)   # list markers
    return re.sub(r"\s+", " ", s).strip()


def units_from_export():
    section, out = None, []
    for line in EXPORT.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        head = re.fullmatch(r"\s*\*\*(.+?):?\*\*:?\s*", line)
        if head:
            title = head.group(1).strip().rstrip(":")
            if title not in SECTIONS:
                sys.exit(f"unknown heading in Doc: {title!r} — add it to SECTIONS")
            section = SECTIONS[title]
            continue
        if section is None:
            sys.exit(f"text before the first heading: {line[:60]!r}")
        pieces, carry = [], ""
        for piece in re.split(r"(?<=[.?!])\s+", clean(line)):
            if re.fullmatch(r"[א-ת]\.", piece):
                carry += piece + " "
            elif piece:
                pieces.append(carry + piece)
                carry = ""
        out += [(section, p) for p in pieces]
    return out


def text_hash(s):
    return hashlib.sha1(s.encode("utf-8")).hexdigest()[:10]


def read_ledger():
    if not LEDGER.exists():
        return []
    with LEDGER.open(encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f, delimiter="\t", quoting=csv.QUOTE_NONE))
    for r in rows:
        if r["status"] not in STATUSES:
            sys.exit(f"{r['id']}: unknown status {r['status']!r}")
    return rows


def write_ledger(rows):
    with LEDGER.open("w", encoding="utf-8", newline="") as f:
        # Text never holds tabs or newlines (clean() collapses whitespace), so no quoting:
        # Hebrew abbreviations like ס"מ stay readable.
        w = csv.DictWriter(f, FIELDS, delimiter="\t", lineterminator="\n",
                           quoting=csv.QUOTE_NONE, quotechar=None)
        w.writeheader()
        w.writerows(rows)


def sync():
    old = read_ledger()
    by_hash = {}
    for r in old:
        by_hash.setdefault(r["hash"], []).append(r)
    next_num = {}
    for r in old:
        prefix, num = r["id"].rsplit("-", 1)
        next_num[prefix] = max(next_num.get(prefix, 0), int(num))

    rows, seen, added = [], set(), 0
    for section, text in units_from_export():
        h = text_hash(text)
        match = next((r for r in by_hash.get(h, []) if r["id"] not in seen), None)
        if match:
            if match["status"] == "gone":
                match["status"] = "todo"
            rows.append(match)
            seen.add(match["id"])
        else:
            next_num[section] = next_num.get(section, 0) + 1
            rows.append({"id": f"{section}-{next_num[section]:02d}", "status": "todo",
                         "note": "", "hash": h, "text": text})
            added += 1
    gone = 0
    for r in old:
        if r["id"] not in seen:
            if r["status"] != "gone":
                r["status"], gone = "gone", gone + 1
            rows.append(r)
    write_ledger(rows)
    print(f"{len(rows)} units in ledger: {added} new, {gone} newly gone from the Doc")


def tex_tags():
    """Map unit ID -> list of (file, line number, line) that carry it."""
    tags = {}
    for tex in sorted(REPORT.glob("*.tex")):
        for n, line in enumerate(tex.read_text(encoding="utf-8").splitlines(), 1):
            m = TAG.search(line)
            if m:
                for uid in m.group(1).split():
                    tags.setdefault(uid, []).append((tex.name, n, line))
    return tags


def check():
    rows = read_ledger()
    ids = {r["id"] for r in rows}
    tags = tex_tags()
    todo = [r for r in rows if r["status"] == "todo" and r["id"] not in tags]
    unknown = sorted(set(tags) - ids)
    gone = [r for r in rows if r["status"] == "gone"]
    gone_tagged = [r for r in gone if r["id"] in tags]

    per = {}
    for r in rows:
        if r["status"] == "gone":
            continue
        done = r["id"] in tags or r["status"] != "todo"
        d, t = per.get(r["id"].rsplit("-", 1)[0], (0, 0))
        per[r["id"].rsplit("-", 1)[0]] = (d + done, t + 1)
    print("section  handled/total")
    for prefix in SECTIONS.values():
        if prefix in per:
            print(f"  {prefix:6} {per[prefix][0]:3}/{per[prefix][1]}")

    for title, items in (("NOT YET TRANSFERRED", todo), ("CHANGED OR REMOVED IN DOC", gone)):
        if items:
            print(f"\n{title} ({len(items)}):")
            for r in items:
                flag = "  [still tagged in report]" if r in gone_tagged else ""
                print(f"  {r['id']:9} {r['text'][:90]}{flag}")
    if unknown:
        print(f"\nTAGS WITH NO SUCH UNIT ({len(unknown)}):")
        for uid in unknown:
            for f, n, _ in tags[uid]:
                print(f"  {uid} at {f}:{n}")
    problems = len(todo) + len(unknown) + len(gone_tagged)
    print("\nALL UNITS HANDLED" if problems == 0 else f"\n{problems} open item(s)")
    return problems


def side(prefix):
    tags = tex_tags()
    for r in read_ledger():
        if not r["id"].startswith(prefix + "-"):
            continue
        print(f"=== {r['id']} [{r['status']}] {r['note']}")
        print(f"DOC:   {r['text']}")
        for f, n, line in tags.get(r["id"], []):
            before = line.split("%", 1)[0].strip()
            if before:  # tag at the end of a line (table rows): that line is the passage
                print(f"TEX:   {f}:{n}  {before}")
            else:       # tag on its own line: the passage is the next line
                lines = (REPORT / f).read_text(encoding="utf-8").splitlines()
                print(f"TEX:   {f}:{n + 1}  {lines[n] if n < len(lines) else ''}")
        print()


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "check"
    if cmd == "fetch":
        fetch()
    elif cmd == "sync":
        sync()
    elif cmd == "check":
        sys.exit(1 if check() else 0)
    elif cmd == "side":
        side(sys.argv[2])
    else:
        sys.exit(__doc__)
