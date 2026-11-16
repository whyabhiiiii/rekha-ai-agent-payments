"""Turn docs/*.md into styled web pages (docs/*.html) for the live site.

Run from the project folder after editing any doc:
    python3 scripts/build_docs.py
Needs the `markdown` package (pip3 install markdown).
"""
import html
import pathlib
import re

import markdown

ROOT = pathlib.Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"

TITLES = {
    "01_Discovery_and_Research": "Discovery & Research",
    "02_PRD": "PRD",
    "03_Metrics_and_Experiments": "Metrics & Experiments",
    "04_Strategy_and_GTM": "Strategy & GTM",
    "05_Trust_Safety_Threat_Model": "Threat Model",
    "06_Validation_Plan": "Validation Plan",
}

ICON = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='14' fill='%235B3CC4'/%3E"
        "%3Cpath d='M12 42C24 26 40 22 52 24' fill='none' stroke='white' stroke-width='6' stroke-linecap='round'/%3E%3Ccircle cx='12' cy='42' r='5' fill='white'/%3E%3C/svg%3E")

# Only pages that contain a diagram load Mermaid. Diagrams are never shrunk below
# about 11px text: when one is wider than the column, its own box scrolls sideways.
MERMAID = """<script src="https://cdn.jsdelivr.net/npm/mermaid@11.4.1/dist/mermaid.min.js"></script>
<script>
  (function () {
    if (!window.mermaid) return;
    var root = document.documentElement;
    var dark = root.getAttribute("data-theme") === "dark" ||
      (!root.getAttribute("data-theme") && window.matchMedia && matchMedia("(prefers-color-scheme: dark)").matches);
    mermaid.initialize({ startOnLoad: false, theme: dark ? "dark" : "neutral", securityLevel: "strict" });
    function fit() {
      document.querySelectorAll("pre.mermaid svg").forEach(function (svg) {
        var natural = svg.viewBox.baseVal.width, room = svg.closest(".mermaid-wrap").clientWidth - 34;
        var width = Math.min(natural, Math.max(room, natural * 0.68));
        svg.style.maxWidth = "none"; svg.style.width = width + "px"; svg.style.height = "auto";
      });
    }
    mermaid.run({ querySelector: "pre.mermaid" }).then(function () { fit(); window.addEventListener("resize", fit); });
  })();
</script>
"""

TEMPLATE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title} · Rekha</title>
<meta name="description" content="{title}: part of Rekha, a product case study on spending limits for AI agents on UPI, by Abhishek Kumar.">
<meta property="og:title" content="{title} · Rekha">
<meta property="og:image" content="https://whyabhiiiii.github.io/rekha-ai-agent-payments/og.png">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{icon}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Hanken+Grotesk:ital,wght@0,400;0,600;0,700;1,400&family=IBM+Plex+Mono:wght@400;500&family=Rozha+One&display=swap">
<style>
/* Layout: a single reading column pinned to the same violet margin rule as the case study. */
:root {{
  --paper: #F6F5FA; --surface: #FFFFFF; --ink: #17162B; --muted: #5D5B73; --faint: #6A6783; --rule: #E2E0EC;
  --line: #5B3CC4; --line-ink: #4A2FB0; --line-soft: #EEEAFC;
  --f-display: "Rozha One", "Noto Serif Devanagari", Georgia, serif;
  --f-body: "Hanken Grotesk", system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
  --f-mono: "IBM Plex Mono", ui-monospace, SFMono-Regular, Menlo, monospace;
  color-scheme: light;
}}
@media (prefers-color-scheme: dark) {{
  :root:not([data-theme="light"]) {{
    --paper: #121120; --surface: #1C1B2C; --ink: #ECEAF6; --muted: #A9A6C0; --faint: #908DA9; --rule: #2D2B42;
    --line: #A792FF; --line-ink: #C4B6FF; --line-soft: #262046; color-scheme: dark;
  }}
}}
:root[data-theme="dark"] {{
  --paper: #121120; --surface: #1C1B2C; --ink: #ECEAF6; --muted: #A9A6C0; --faint: #908DA9; --rule: #2D2B42;
  --line: #A792FF; --line-ink: #C4B6FF; --line-soft: #262046; color-scheme: dark;
}}
*, *::before, *::after {{ box-sizing: border-box; }}
body {{ margin: 0; background: var(--paper); color: var(--ink); font: 17px/1.65 var(--f-body); }}
a {{ color: var(--line-ink); text-underline-offset: 3px; }}
:focus-visible {{ outline: 2px solid var(--line); outline-offset: 2px; }}
.top {{ display: flex; flex-wrap: wrap; gap: 12px 20px; align-items: center; justify-content: space-between;
  padding: 14px max(16px, 4vw); border-bottom: 1px solid var(--rule); background: var(--paper); position: sticky; top: env(safe-area-inset-top, 0px); z-index: 2; }}
.mark {{ display: inline-flex; align-items: baseline; gap: 8px; text-decoration: none; color: var(--ink); }}
.mark .dev {{ font-family: var(--f-display); font-size: 26px; line-height: 1; border-bottom: 3px solid var(--line); }}
.mark .lat {{ font-family: var(--f-display); font-size: 18px; }}
.top nav {{ display: flex; flex-wrap: wrap; gap: 6px 16px; font-size: 14.5px; font-weight: 600; }}
.top nav a {{ text-decoration: none; }}
.top nav a:hover {{ text-decoration: underline; }}
.wrap {{ max-width: 980px; margin: 0 auto; padding: 32px max(16px, 4vw) 64px; }}
article {{ border-left: 2px solid var(--line); padding-left: clamp(16px, 4vw, 40px); min-width: 0; }}
article > * {{ max-width: 72ch; }}
article > .tw, article > pre, article > .mermaid-wrap {{ max-width: none; }}
h1 {{ font-family: var(--f-display); font-weight: 400; font-size: clamp(32px, 5vw, 48px); line-height: 1.08; margin: 0 0 18px; text-wrap: balance; }}
h2 {{ font-family: var(--f-display); font-weight: 400; font-size: clamp(25px, 3.4vw, 32px); line-height: 1.15; margin: 44px 0 12px; text-wrap: balance; }}
h3 {{ font-size: 19px; margin: 28px 0 8px; }}
h4 {{ font-size: 16px; margin: 20px 0 6px; }}
p, li {{ margin: 0 0 12px; }}
ul, ol {{ padding-left: 22px; margin: 0 0 14px; }}
hr {{ border: 0; border-top: 1px solid var(--rule); margin: 32px 0; }}
blockquote {{ margin: 0 0 16px; padding: 10px 16px; border-left: 4px solid var(--line); background: var(--line-soft); border-radius: 0 12px 12px 0; }}
blockquote p:last-child {{ margin-bottom: 0; }}
code {{ font-family: var(--f-mono); font-size: .86em; background: var(--line-soft); color: var(--line-ink); padding: 1px 5px; border-radius: 5px; }}
pre {{ background: var(--surface); border: 1px solid var(--rule); border-radius: 12px; padding: 14px 16px; overflow-x: auto; margin: 0 0 16px; }}
pre code {{ background: none; color: var(--ink); padding: 0; font-size: 13.5px; line-height: 1.55; }}
.tw {{ overflow-x: auto; border: 1px solid var(--rule); border-radius: 12px; background: var(--surface); margin: 0 0 18px; }}
table {{ width: 100%; border-collapse: collapse; font-size: 14.5px; min-width: 560px; }}
th {{ text-align: left; font-size: 12px; letter-spacing: .06em; text-transform: uppercase; color: var(--muted); font-weight: 600; padding: 10px 12px; border-bottom: 1px solid var(--rule); }}
td {{ padding: 9px 12px; border-top: 1px solid var(--rule); vertical-align: top; }}
tr:first-child td {{ border-top: 0; }}
.mermaid-wrap {{ background: var(--surface); border: 1px solid var(--rule); border-radius: 12px; padding: 16px; overflow-x: auto; margin: 0 0 18px; }}
pre.mermaid {{ border: 0; padding: 0; margin: 0; background: none; overflow: visible; }}
pre.mermaid svg {{ display: block; margin-inline: auto; }}
/* trees (opportunity tree, metric tree): nested lists drawn with connector lines */
ul.tree {{ list-style: none; padding: 14px 16px; margin: 0 0 18px; max-width: none; background: var(--surface); border: 1px solid var(--rule); border-radius: 12px; font-size: 15.5px; }}
ul.tree ul {{ list-style: none; margin: 8px 0 4px 6px; padding-left: 18px; border-left: 2px solid var(--line-soft); }}
ul.tree li {{ margin: 0 0 6px; line-height: 1.5; }}
ul.tree > li > ul > li {{ margin-bottom: 12px; }}
ul.tree em {{ color: var(--muted); font-size: .93em; }}
.pager {{ display: flex; justify-content: space-between; gap: 12px; flex-wrap: wrap; margin-top: 48px; padding-top: 18px; border-top: 1px solid var(--rule); font-weight: 600; }}
.foot {{ margin-top: 24px; font-size: 13.5px; color: var(--faint); }}
</style>
</head>
<body>
<header class="top">
  <a class="mark" href="../index.html"><span class="dev" lang="hi">रेखा</span><span class="lat">Rekha</span></a>
  <nav aria-label="Project">
    <a href="../index.html">Case study</a>
    <a href="../prototype.html">Prototype</a>
    <a href="../index.html#docs">All documents</a>
  </nav>
</header>
<main class="wrap">
<article>
{body}
<nav class="pager" aria-label="Documents">
  <span>{prev}</span><span>{next}</span>
</nav>
<p class="foot">Rekha is a concept case study by Abhishek Kumar. Market facts are cited; sizing and targets are labelled assumptions.</p>
</article>
</main>
{mermaid}</body>
</html>
"""


def convert(md_text: str) -> str:
    body = markdown.markdown(md_text, extensions=["tables", "fenced_code", "sane_lists", "toc"], output_format="html5")
    # Mermaid fences become <pre class="mermaid"> so mermaid.js renders them.
    body = re.sub(
        r'<pre><code class="language-mermaid">(.*?)</code></pre>',
        lambda m: '<div class="mermaid-wrap"><pre class="mermaid">' + m.group(1) + "</pre></div>",
        body,
        flags=re.S,
    )
    # A list that follows a <!--tree--> marker is drawn as a tree.
    body = re.sub(r"<!--tree-->\s*<ul>", '<ul class="tree">', body)
    # Wide tables scroll inside their own box on phones.
    body = body.replace("<table>", '<div class="tw"><table>').replace("</table>", "</table></div>")
    # Links between docs point at the HTML versions.
    body = re.sub(r'href="([0-9]{2}_[A-Za-z_]+)\.md"', r'href="\1.html"', body)
    return body


def main() -> None:
    names = sorted(p.stem for p in DOCS.glob("[0-9][0-9]_*.md"))
    for stale in DOCS.glob("[0-9][0-9]_*.html"):
        if stale.stem not in names:
            stale.unlink()
    for i, name in enumerate(names):
        md_text = (DOCS / f"{name}.md").read_text(encoding="utf-8")
        prev_link = f'<a href="{names[i-1]}.html">← {html.escape(TITLES.get(names[i-1], names[i-1]))}</a>' if i > 0 else ""
        next_link = f'<a href="{names[i+1]}.html">{html.escape(TITLES.get(names[i+1], names[i+1]))} →</a>' if i < len(names) - 1 else ""
        body = convert(md_text)
        page = TEMPLATE.format(title=html.escape(TITLES.get(name, name)), icon=ICON, body=body, prev=prev_link, next=next_link,
                               mermaid=MERMAID if 'class="mermaid"' in body else "")
        (DOCS / f"{name}.html").write_text(page, encoding="utf-8")
        print("built", f"docs/{name}.html")


if __name__ == "__main__":
    main()
