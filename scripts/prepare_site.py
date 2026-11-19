#!/usr/bin/env python3
"""Copy the static homepage into the Sites deployment directory."""
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parent.parent
DEST = ROOT / 'dist'
DEST.mkdir(exist_ok=True)
for name in ('index.html', 'stylesheet.css', 'images', 'data', 'mipnerf'):
    source = ROOT / name
    target = DEST / name
    if source.is_dir():
        shutil.copytree(source, target, dirs_exist_ok=True)
    else:
        shutil.copy2(source, target)
print(f'Static site prepared in {DEST}')
