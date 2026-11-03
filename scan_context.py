from pathlib import Path

for p in [Path("privacy.html"), Path("support.html"), Path("terms.html")]:
    s = p.read_text(encoding="utf-8")
    print("==", p.name)
    for i, ch in enumerate(s):
        if ord(ch) in (0xFEFF, 0x00C2, 0x00A9, 0x00E2, 0x2020):
            print(i, hex(ord(ch)), ascii(s[max(0, i-45):i+45]))
