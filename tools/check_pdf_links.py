"""Check the downloadable Week 03 PDF, including its embedded resource links.

Run: uv run --with pymupdf python tools/check_pdf_links.py [PDF path or URL]
"""
import sys
from pathlib import Path
from urllib.parse import urlparse
from urllib.request import urlopen

import pymupdf

BASE = 'https://gmthu.github.io/aspnet-course/week03/'
EXPECTED = [
    (4, BASE + 'materials/Week03-student.zip'),
    (31, BASE + 'materials/Week03-student.zip'),
    (31, BASE + 'materials/activity-reference.html'),
    (31, BASE + 'materials/Index-body-reference.txt'),
    (31, BASE + 'ASP.NET-Week03.pdf'),
]
source = sys.argv[1] if len(sys.argv) > 1 else str(
    Path(__file__).resolve().parents[1] / 'week03/ASP.NET-Week03.pdf'
)
if source.startswith('https://'):
    with urlopen(source, timeout=40) as response:
        data = response.read()
else:
    data = Path(source).read_bytes()
with pymupdf.open(stream=data, filetype='pdf') as doc:
    links = [(i + 1, link['uri']) for i, page in enumerate(doc)
             for link in page.get_links() if link.get('uri')]
    local = [(page, uri) for page, uri in links
             if urlparse(uri).hostname in {'127.0.0.1', 'localhost', '::1'}
             or urlparse(uri).scheme == 'file']
    assert not local, f'Local-only PDF links: {local}'
    assert len(doc) == 31, f'Unexpected page count: {len(doc)}'
    for expected in EXPECTED:
        assert links.count(expected) == 1, f'Missing/duplicate resource link: {expected}'
    print('PASS: 31 pages; all 5 resource links use GitHub Pages; no local-only URI links.')
