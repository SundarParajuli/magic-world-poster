from pathlib import Path

REPL = {
    "\ufeff": "",
    "\u00e2\u2020\u2019": "\u2192",
    "\u00c2\u00a9": "\u00a9",
    "\u00c2\u00a0": " ",
    "\u00e2\u20ac\u201d": "\u2014",
    "\u00e2\u20ac\u201c": "\u2013",
    "\u00e2\u20ac\u2122": "\u2019",
    "\u00e2\u20ac\u02dc": "\u2018",
    "\u00e2\u20ac\u0153": "\u201c",
    "\u00e2\u20ac\u009d": "\u201d",
    "\u00e2\u20ac\u00a6": "\u2026",
}

for p in sorted(Path(".").glob("*.html")):
    s = p.read_text(encoding="utf-8")
    orig = s
    for bad, good in REPL.items():
        s = s.replace(bad, good)
    if s != orig:
        p.write_text(s, encoding="utf-8", newline="\n")
        print("fixed", p.name)
    bad = [hex(ord(ch)) for ch in s if ord(ch) in (0xFEFF, 0x00C2, 0x00E2, 0x2020)]
    if bad:
        print("still bad", p.name, bad)
