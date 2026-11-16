from pathlib import Path
from html import escape
root = Path('assets')
projects = {
 'teragrant': ('voice + docs', 'check the facts', 'application'),
 'agenthelm': ('agent task', 'isolated work', 'review changes'),
 'signalintel': ('live broadcast', 'speech + text', 'search + alerts'),
 'ghostreply': ('new message', 'draft a reply', 'my approval'),
}
for key, labels in projects.items():
 nodes=''.join(f'<rect x="{x}" y="48" width="176" height="70" rx="8" fill="#151d26" stroke="#344250"/><text x="{x+88}" y="90" text-anchor="middle" fill="#e4e9ed" font-family="Arial, sans-serif" font-size="22">{escape(label)}</text>' for x,label in zip([16,232,448],labels))
 base=f'''<svg xmlns="http://www.w3.org/2000/svg" width="640" height="166" viewBox="0 0 640 166" role="img" aria-labelledby="title">
<title id="title">{key}: {' to '.join(labels)}</title>
<rect width="640" height="166" rx="10" fill="#0d1117"/>
<path d="M192 83h40m176 0h40" fill="none" stroke="#657688" stroke-width="2"/>
{nodes}
<path d="M16 143h608" stroke="#263340"/>
<text x="20" y="32" fill="#d6ac69" font-family="monospace" font-size="16">{'[ ? ]' if key=='ghostreply' else '[ + ]' if key=='teragrant' else '[ &gt; ]' if key=='agenthelm' else '[ ~ ]'}</text>
MOTION
</svg>'''
 motion='<circle r="3" fill="#d6ac69"><animateMotion dur="5s" repeatCount="indefinite" path="M192 83L232 83"/></circle><circle r="3" fill="#d6ac69"><animateMotion dur="5s" begin="2.5s" repeatCount="indefinite" path="M408 83L448 83"/></circle>'
 (root/f'project-{key}.svg').write_text(base.replace('MOTION',motion),encoding='utf-8')
 (root/f'project-{key}-still.svg').write_text(base.replace('MOTION',''),encoding='utf-8')
