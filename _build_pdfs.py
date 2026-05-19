"""
Build polished PDFs from TraderLab101 markdown docs.

Pipeline: Markdown -> styled HTML (with embedded CSS for print) -> Chrome headless --print-to-pdf -> PDF.

Run from the TraderLab101 folder:
    python _build_pdfs.py
"""

import html as htmllib
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

import markdown

ROOT = Path(__file__).parent.resolve()
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

DOCS = [
    {
        "src": ROOT / "USERGUIDE.md",
        "out": ROOT / "USERGUIDE.pdf",
        "title": "TraderLab 101",
        "subtitle": "User Guide",
        "version": "v2.3.16 · May 2026",
        "header_text": "TraderLab 101 — User Guide",
    },
    {
        "src": ROOT / "QUICKSTART.md",
        "out": ROOT / "QUICKSTART.pdf",
        "title": "TraderLab 101",
        "subtitle": "Quick Start",
        "version": "v2.3.16 · May 2026",
        "header_text": "TraderLab 101 — Quick Start",
    },
    {
        "src": ROOT / "MULTI_SYMBOL_NOTES.md",
        "out": ROOT / "MULTI_SYMBOL_NOTES.pdf",
        "title": "TraderLab 101",
        "subtitle": "Multi-Symbol Notes",
        "version": "v2.3.16 · May 2026",
        "header_text": "TraderLab 101 — Multi-Symbol Notes",
    },
]

# CSS designed for a clean white printable PDF with TraderLab gold (#f5a623) accents.
CSS = r"""
@page {
  size: Letter;
  margin: 0.75in 0.75in 0.85in 0.75in;
  @bottom-center {
    content: counter(page) " of " counter(pages);
    font-family: -apple-system, "Segoe UI", Helvetica, Arial, sans-serif;
    font-size: 9pt;
    color: #888;
  }
  @top-right {
    content: string(doc-header);
    font-family: -apple-system, "Segoe UI", Helvetica, Arial, sans-serif;
    font-size: 9pt;
    color: #888;
  }
}

@page :first {
  margin: 0.75in 0.75in 0.85in 0.75in;
  @top-right { content: ""; }
}

html { -webkit-print-color-adjust: exact; print-color-adjust: exact; }

body {
  font-family: -apple-system, "Segoe UI", Helvetica, Arial, sans-serif;
  font-size: 11pt;
  line-height: 1.55;
  color: #1a1a1a;
  margin: 0;
  padding: 0;
  background: #ffffff;
  -webkit-font-smoothing: antialiased;
}

/* ---- Cover block on page 1 ---- */
.cover {
  string-set: doc-header attr(data-header);
  page-break-after: always;
  display: flex;
  flex-direction: column;
  justify-content: center;
  height: 8.0in;
  border-top: 4px solid #f5a623;
  border-bottom: 1px solid #e6e6e6;
  padding: 0.5in 0;
  text-align: left;
}
.cover-mark {
  display: inline-block;
  width: 38px;
  height: 38px;
  background: #f5a623;
  border-radius: 6px;
  text-align: center;
  line-height: 38px;
  color: #000;
  font-weight: 900;
  font-size: 18px;
  margin-bottom: 18px;
}
.cover h1 {
  font-size: 38pt;
  font-weight: 800;
  margin: 0 0 6pt 0;
  color: #1a1a1a;
  letter-spacing: -0.5px;
  border: none;
}
.cover .subtitle {
  font-size: 22pt;
  font-weight: 600;
  color: #f5a623;
  margin: 0 0 18pt 0;
}
.cover .version {
  font-size: 11pt;
  color: #666;
  letter-spacing: 0.4px;
  text-transform: uppercase;
  margin-bottom: 22pt;
}
.cover .tagline {
  font-size: 12pt;
  color: #444;
  font-style: italic;
  border-left: 3px solid #f5a623;
  padding: 2pt 0 2pt 14pt;
  max-width: 5.5in;
  line-height: 1.55;
}

/* ---- The body content (after cover) carries the page header ---- */
.content { string-set: doc-header attr(data-header); }

/* ---- Headings ---- */
h1, h2, h3, h4, h5 {
  font-weight: 700;
  color: #1a1a1a;
  margin-top: 1.6em;
  margin-bottom: 0.4em;
  page-break-after: avoid;
  break-after: avoid;
  page-break-inside: avoid;
  break-inside: avoid;
}
h1 {
  font-size: 22pt;
  border-bottom: 3px solid #f5a623;
  padding-bottom: 6pt;
  margin-top: 0.4em;
}
h2 {
  font-size: 16pt;
  color: #1a1a1a;
  border-bottom: 1px solid #e6e6e6;
  padding-bottom: 4pt;
  margin-top: 1.4em;
}
h3 {
  font-size: 13pt;
  color: #b8810f;
}
h4 {
  font-size: 11.5pt;
  color: #444;
  text-transform: uppercase;
  letter-spacing: 0.3px;
}

/* Keep the heading + the next paragraph/table together where possible */
h1 + *, h2 + *, h3 + *, h4 + * {
  page-break-before: avoid;
  break-before: avoid;
}

p {
  margin: 0.55em 0;
  orphans: 3;
  widows: 3;
}

/* ---- Inline ---- */
strong { color: #1a1a1a; font-weight: 700; }
em { color: #444; }
a { color: #b8810f; text-decoration: none; border-bottom: 1px dotted #c9a060; }

/* ---- Lists ---- */
ul, ol {
  margin: 0.4em 0 0.6em 0;
  padding-left: 1.4em;
}
li { margin: 0.18em 0; }
li > p { margin: 0.18em 0; }

/* ---- Code & pre ---- */
code {
  font-family: "Consolas", "SF Mono", Menlo, Monaco, "Courier New", monospace;
  font-size: 9.8pt;
  background: #f5f5f4;
  padding: 1px 4px;
  border-radius: 3px;
  color: #2a2a2a;
}
pre {
  font-family: "Consolas", "SF Mono", Menlo, Monaco, "Courier New", monospace;
  font-size: 9pt;
  line-height: 1.45;
  background: #f5f5f4;
  border: 1px solid #e6e6e6;
  border-left: 3px solid #f5a623;
  border-radius: 4px;
  padding: 10px 14px;
  white-space: pre;
  overflow: hidden;
  page-break-inside: avoid;
  break-inside: avoid;
  max-width: 100%;
}
pre code {
  background: transparent;
  padding: 0;
  border-radius: 0;
  font-size: 9pt;
  color: #2a2a2a;
}

/* ---- Blockquote ---- */
blockquote {
  margin: 0.8em 0;
  padding: 6px 14px;
  border-left: 3px solid #f5a623;
  background: #fffaf0;
  color: #444;
  font-style: italic;
  page-break-inside: avoid;
  break-inside: avoid;
}
blockquote p { margin: 0.25em 0; }

/* ---- Tables ---- */
table {
  width: 100%;
  border-collapse: collapse;
  margin: 0.7em 0 1em 0;
  font-size: 10pt;
  page-break-inside: avoid;
  break-inside: avoid;
  table-layout: auto;
}
thead { display: table-header-group; }
tr { page-break-inside: avoid; break-inside: avoid; }
th, td {
  border: 1px solid #dcdcdc;
  padding: 6px 9px;
  text-align: left;
  vertical-align: top;
  word-wrap: break-word;
  overflow-wrap: break-word;
}
th {
  background: #fafafa;
  font-weight: 700;
  color: #1a1a1a;
  border-bottom: 2px solid #f5a623;
}
tr:nth-child(even) td { background: #fcfcfc; }

/* ---- Horizontal rule ---- */
hr {
  border: none;
  border-top: 1px solid #e6e6e6;
  margin: 1.4em 0;
}

/* ---- TOC list looks tidier ---- */
.toc, h2 + ol {
  font-size: 10.5pt;
}
"""

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>{title} — {subtitle}</title>
<style>{css}</style>
</head>
<body>
<section class="cover" data-header="{header}">
  <div class="cover-mark">T</div>
  <h1>{title}</h1>
  <div class="subtitle">{subtitle}</div>
  <div class="version">{version}</div>
  <div class="tagline">If this — then that. If not — then what?<br><span style="font-style:normal;color:#888;font-size:10pt;">— Tom B., Traders Lab</span></div>
</section>
<main class="content" data-header="{header}">
{body}
</main>
</body>
</html>
"""


def md_to_html(md_text: str) -> str:
    """Convert markdown to HTML with the extensions we rely on."""
    md = markdown.Markdown(
        extensions=[
            "tables",
            "fenced_code",
            "sane_lists",
            "attr_list",
            "toc",
        ],
        extension_configs={
            "toc": {"title": "", "toc_depth": "2-3"},
        },
    )
    body = md.convert(md_text)
    # Strip the auto-generated title 1 from page 1 (we have a cover already).
    body = re.sub(
        r"^\s*<h1[^>]*>.*?</h1>\s*",
        "",
        body,
        count=1,
        flags=re.IGNORECASE | re.DOTALL,
    )
    return body


def build_html(doc) -> str:
    md_text = doc["src"].read_text(encoding="utf-8")
    body = md_to_html(md_text)
    return HTML_TEMPLATE.format(
        title=htmllib.escape(doc["title"]),
        subtitle=htmllib.escape(doc["subtitle"]),
        version=htmllib.escape(doc["version"]),
        header=htmllib.escape(doc["header_text"]),
        body=body,
        css=CSS,
    )


def html_to_pdf(html_path: Path, pdf_path: Path) -> None:
    """Use Chrome headless to render HTML to PDF."""
    if not Path(CHROME).exists():
        raise FileNotFoundError(f"Chrome not found at {CHROME}")
    file_url = "file:///" + str(html_path.resolve()).replace("\\", "/")
    cmd = [
        CHROME,
        "--headless=new",
        "--disable-gpu",
        "--no-sandbox",
        "--no-pdf-header-footer",
        "--virtual-time-budget=2000",
        "--run-all-compositor-stages-before-draw",
        f"--print-to-pdf={pdf_path}",
        file_url,
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
    if result.returncode != 0:
        # Fall back: try without --no-pdf-header-footer (older flag name)
        cmd2 = [
            CHROME,
            "--headless",
            "--disable-gpu",
            "--no-sandbox",
            "--print-to-pdf-no-header",
            f"--print-to-pdf={pdf_path}",
            file_url,
        ]
        result = subprocess.run(cmd2, capture_output=True, text=True, timeout=120)
        if result.returncode != 0:
            raise RuntimeError(
                f"Chrome failed: rc={result.returncode}\nSTDOUT:\n{result.stdout}\nSTDERR:\n{result.stderr}"
            )


def build_one(doc) -> None:
    print(f"Building {doc['out'].name} ...", flush=True)
    html_str = build_html(doc)
    with tempfile.NamedTemporaryFile(
        mode="w", encoding="utf-8", suffix=".html", delete=False
    ) as f:
        f.write(html_str)
        tmp_html = Path(f.name)
    try:
        html_to_pdf(tmp_html, doc["out"])
    finally:
        try:
            tmp_html.unlink()
        except Exception:
            pass
    size = doc["out"].stat().st_size
    print(f"  -> {doc['out']} ({size/1024:.1f} KB)", flush=True)


def main() -> int:
    for d in DOCS:
        if not d["src"].exists():
            print(f"ERROR: source not found: {d['src']}", file=sys.stderr)
            return 1
    for d in DOCS:
        build_one(d)
    print("Done.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
