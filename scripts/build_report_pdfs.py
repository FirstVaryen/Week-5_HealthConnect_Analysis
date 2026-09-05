# -*- coding: utf-8 -*-
"""Convert the Week 5 markdown reports to PDF."""
from pathlib import Path
import markdown
from xhtml2pdf import pisa

REPORTS = Path(__file__).resolve().parent.parent / "reports"

CSS = """
@page { size: A4; margin: 2cm; }
body { font-family: Helvetica, Arial, sans-serif; font-size: 10.5pt; line-height: 1.45; color: #1a1a1a; }
h1 { font-size: 17pt; border-bottom: 2px solid #2a4d69; padding-bottom: 4px; margin-bottom: 10px; }
h2 { font-size: 13pt; color: #2a4d69; margin-top: 18px; }
h3 { font-size: 11.5pt; color: #2a4d69; margin-top: 14px; }
p { margin: 6px 0; }
code { font-family: Courier, monospace; font-size: 9pt; background: #f0f0f0; padding: 1px 3px; }
table { border-collapse: collapse; width: 100%; margin: 8px 0; font-size: 9.5pt; }
th, td { border: 1px solid #bbb; padding: 4px 6px; text-align: left; vertical-align: top; }
th { background: #e8eef4; }
ul, ol { margin: 6px 0; padding-left: 20px; }
li { margin: 3px 0; }
strong { color: #12243a; }
hr { border: none; border-top: 1px solid #ccc; margin: 14px 0; }
"""

for md_path in sorted(REPORTS.glob("*.md")):
    text = md_path.read_text(encoding="utf-8")
    html_body = markdown.markdown(text, extensions=["tables","sane_lists","nl2br"])
    html = f"<html><head><meta charset='utf-8'><style>{CSS}</style></head><body>{html_body}</body></html>"
    pdf_path = md_path.with_suffix(".pdf")
    with open(pdf_path, "wb") as f:
        result = pisa.CreatePDF(html, dest=f, encoding="utf-8")
    status = "OK" if not result.err else f"ERRORS ({result.err})"
    print(f"{md_path.name} -> {pdf_path.name}  [{status}]")
