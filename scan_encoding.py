from pathlib import Path
from collections import Counter

for p in [Path("privacy.html"), Path("support.html"), Path("terms.html")]:
    s = p.read_text(encoding="utf-8")
    bad = Counter(ch for ch in s if ord(ch) > 127 and ch not in "\u2014\u2013\u2019\u2018\u201c\u201d\u2026")
    print(p.name, {hex(ord(k)): v for k, v in bad.items()})
