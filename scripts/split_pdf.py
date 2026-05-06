#!/usr/bin/env python3
"""
Split pdftotext Hebrew output into per-section chunk files.
Three modes:
  lecture  -- splits on "keyword N.M" (הגדרה 1.2, משפט 2.1, etc.)
  tirgul   -- splits on standalone keyword lines (bare הגדרה, דוגמה, etc.)
  hw       -- splits on top-level question numbers (".N" pattern in RTL output)
"""
import re, sys, os

BIDI = re.compile(r'[‪‫‬‭‮‎‏]')

KEYWORDS = r'(?:הגדרה|משפט|טענה|הערה|דוגמה|דוגמאות|למה|מסקנה|סימון|הוכחה|משפט \(תראו בהרצאה\))'

PATTERNS = {
    'lecture': re.compile(rf'^\s*{KEYWORDS}\s+\d+\.\d+'),
    'tirgul':  re.compile(rf'^\s*{KEYWORDS}\s*$'),
    'hw':      re.compile(r'^\s*\.\d+\s*$'),   # RTL: ".1", ".2" etc (period before number)
}

def clean(line):
    return BIDI.sub('', line)

def split_file(txt_path, out_dir, prefix, mode):
    header_re = PATTERNS[mode]
    with open(txt_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    chunks = []
    current_header = "preamble"
    current_lines = []

    for line in lines:
        c = clean(line)
        if header_re.match(c):
            if current_lines:
                chunks.append((current_header, current_lines))
            current_header = c.strip()[:60]
            current_lines = [line]
        else:
            current_lines.append(line)

    if current_lines:
        chunks.append((current_header, current_lines))

    os.makedirs(out_dir, exist_ok=True)
    written = []
    for i, (header, chunk_lines) in enumerate(chunks):
        safe = re.sub(r'\s+', '_', header.strip())
        safe = re.sub(r'[^\w֐-׿\d\._]', '', safe)[:50]
        fname = f"{prefix}_{i:03d}_{safe}.txt"
        fpath = os.path.join(out_dir, fname)
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(''.join(chunk_lines).strip() + '\n')
        written.append((i, header.strip(), len(chunk_lines), fpath))
    return written

if __name__ == '__main__':
    src, out_dir, prefix, mode = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    results = split_file(src, out_dir, prefix, mode)
    print(f"Split into {len(results)} chunks ({mode} mode):")
    for i, header, nlines, path in results:
        print(f"  [{i:03d}] ({nlines:3d} lines) {header[:70]}")
