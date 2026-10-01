#!/usr/bin/env python3
"""Local authoring checks; requires Python 3.11+ and Pillow. Not needed to install."""
from pathlib import Path
import re, tomllib
from PIL import Image
root = Path(__file__).resolve().parents[1]
p = tomllib.loads((root / 'colors.toml').read_text())
assert p['mode'] == 'dark'
required = 'accent background foreground selection muted red yellow green cyan blue magenta'.split()
assert all(k in p for k in required)
assert all(re.fullmatch(r'#[0-9A-Fa-f]{6}',v) for k,v in p.items() if k != 'mode')
assert len(p) == 26
for f in root.rglob('*'):
    assert not f.is_symlink(), f
assert not any((root/f).exists() for f in ['alacritty.toml','foot.ini','kitty.conf','ghostty.conf','vscode.json'])
assert not list(root.glob('*.lua'))
def lum(c):
    rgb = [int(c[i:i+2],16)/255 for i in (1,3,5)]
    a = [v/12.92 if v <= .04045 else ((v+.055)/1.055)**2.4 for v in rgb]
    return sum(x*y for x,y in zip(a,[.2126,.7152,.0722]))
for a,b,target in [('foreground','background',4.5),('foreground','selection',4.5),('accent','background',3),('muted','background',4.5)]:
    x,y = sorted([lum(p[a]),lum(p[b])])
    ratio=(y+.05)/(x+.05)
    assert ratio >= target, (a,b,ratio)
    print(f'{a}/{b}: {ratio:.2f}:1 (target {target}:1)')
images=sorted((root/'backgrounds').glob('*.png'))
assert len(images)==8
for f in images:
    with Image.open(f) as im:
        im.load()
        if 'icon-' in f.name: assert im.size == (3840,2160)
        assert im.width >= 1600 and abs(im.width/im.height-16/9)<.01
        print(f'{f.name}: {im.width}x{im.height}, {f.stat().st_size:,} bytes; decoded OK')
print('PASS: local palette, contrast, package and image checks')
print('NOT RUN: Rust helper (cargo unavailable), live Omarchy, Git staging, registry validation')
