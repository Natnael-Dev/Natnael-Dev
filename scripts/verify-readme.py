"""Check local README assets with Python's standard library and FFprobe."""
import json
import re
import subprocess
import xml.etree.ElementTree as ET
from pathlib import Path

root = Path(__file__).resolve().parent.parent
readme = (root / 'README.md').read_text(encoding='utf-8-sig')
references = set(re.findall(r'(?:src|srcset)="(assets/[^"]+)"', readme))
for reference in references:
    if not (root / reference).is_file():
        raise SystemExit(f'Missing asset: {reference}')

svgs = list((root / 'assets').glob('*.svg'))
for svg in svgs:
    ET.parse(svg)
    if '<script' in svg.read_text():
        raise SystemExit(f'Script found in {svg.name}')

for image in re.findall(r'<img\b[^>]*>', readme):
    if not re.search(r'alt="[^"]+"', image):
        raise SystemExit('An image is missing descriptive alt text.')

probe = subprocess.run([
    'ffprobe', '-v', 'error', '-select_streams', 'v:0',
    '-show_entries', 'stream=width,height,nb_frames', '-of', 'json',
    str(root / 'assets/creation-of-adam.gif'),
], capture_output=True, text=True, check=True)
stream = json.loads(probe.stdout)['streams'][0]
if (stream['width'], stream['height'], int(stream['nb_frames'])) != (960, 320, 36):
    raise SystemExit(f'Unexpected hero encoding: {stream}')

asset_bytes = sum(path.stat().st_size for path in (root / 'assets').iterdir())
if asset_bytes >= 600_000:
    raise SystemExit(f'Asset budget exceeded: {asset_bytes}')
for obsolete in ['example.com', 'healthcare', 'reciprocal']:
    if obsolete in readme.lower():
        raise SystemExit(f'Obsolete content: {obsolete}')

print(f'PASS: {len(references)} image references; {len(svgs)} SVGs; '
      f'36 GIF frames at 960x320; {asset_bytes} asset bytes; '
      'all image alt text; 3 obsolete-content checks.')
