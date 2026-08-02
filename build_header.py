from pathlib import Path

MONO = "ui-monospace, SFMono-Regular, Menlo, Consolas, 'DejaVu Sans Mono', monospace"

THEMES = {
    "dark": dict(
        bg="#0B1220", panel="#111C2E", grid="#1E3A5F", line="#27476F",
        primary="#13B9FD", accent="#FFCA28", text="#E6EDF5", muted="#7D93AD",
        grid_op="0.35", panel_op="0.9",
    ),
    "light": dict(
        bg="#F5F8FC", panel="#FFFFFF", grid="#DDE9F5", line="#9FBBD6",
        primary="#0175C2", accent="#C98A00", text="#0B1220", muted="#5A7086",
        grid_op="1", panel_op="1",
    ),
}

NODES = [
    ("MaterialApp", 490, 114, 104, 28, 1.05),
    ("Scaffold",    634, 114,  86, 28, 1.45),
    ("AppBar",      776,  60,  76, 26, 1.95),
    ("Body",        776, 115,  66, 26, 2.15),
    ("FAB",         776, 170,  60, 26, 2.35),
]

EDGES = [
    ("M594,128 H634", 1.30),
    ("M720,128 H748", 1.70),
    ("M748,128 V73 H776", 1.85),
    ("M748,128 H776", 2.05),
    ("M748,128 V183 H776", 2.25),
]


def build(t):
    grid = "".join(
        f'<line x1="{x}" y1="0" x2="{x}" y2="260"/>' for x in range(0, 1001, 40)
    ) + "".join(
        f'<line x1="0" y1="{y}" x2="1000" y2="{y}"/>' for y in range(0, 261, 40)
    )

    nodes = ""
    for label, x, y, w, h, d in NODES:
        nodes += (
            f'<g class="node" style="animation-delay:{d}s">'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" '
            f'fill="{t["panel"]}" fill-opacity="{t["panel_op"]}" '
            f'stroke="{t["line"]}" stroke-width="1"/>'
            f'<circle cx="{x + 13}" cy="{y + h/2}" r="3" fill="{t["primary"]}"/>'
            f'<text x="{x + 24}" y="{y + h/2 + 4}" font-family="{MONO}" '
            f'font-size="11.5" fill="{t["text"]}">{label}</text>'
            f"</g>"
        )

    edges = "".join(
        f'<path class="edge" style="animation-delay:{d}s" d="{p}" fill="none" '
        f'stroke="{t["line"]}" stroke-width="1.5" stroke-linecap="round"/>'
        for p, d in EDGES
    )

    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 260" width="1000" height="260" role="img" aria-label="Moud — Flutter and full stack developer">
<style>
  .edge {{ stroke-dasharray: 220; stroke-dashoffset: 220; animation: draw .55s ease-out forwards; }}
  .node {{ opacity: 0; animation: pop .5s ease-out forwards; }}
  .rise {{ opacity: 0; animation: rise .7s cubic-bezier(.2,.8,.2,1) forwards; }}
  .rule {{ transform: scaleX(0); transform-origin: left center; transform-box: fill-box;
           animation: sweep .8s cubic-bezier(.2,.8,.2,1) .55s forwards; }}
  .caret {{ animation: blink 1.1s steps(1) infinite; }}
  .pulse {{ animation: pulse 2.6s ease-in-out 2.6s infinite; }}
  @keyframes draw  {{ to {{ stroke-dashoffset: 0; }} }}
  @keyframes pop   {{ from {{ opacity: 0; }} to {{ opacity: 1; }} }}
  @keyframes rise  {{ from {{ opacity: 0; }} to {{ opacity: 1; }} }}
  @keyframes sweep {{ to {{ transform: scaleX(1); }} }}
  @keyframes blink {{ 0%,49% {{ opacity: 1; }} 50%,100% {{ opacity: 0; }} }}
  @keyframes pulse {{ 0%,100% {{ opacity: .35; }} 50% {{ opacity: 1; }} }}
  @media (prefers-reduced-motion: reduce) {{
    .edge, .node, .rise, .rule, .caret, .pulse {{ animation: none; opacity: 1;
      stroke-dashoffset: 0; transform: none; }}
  }}
</style>

<rect width="1000" height="260" rx="14" fill="{t['bg']}"/>
<g stroke="{t['grid']}" stroke-width="0.5" opacity="{t['grid_op']}">{grid}</g>
<rect x="0.5" y="0.5" width="999" height="259" rx="14" fill="none" stroke="{t['line']}"/>

<g class="rise" style="animation-delay:.1s">
  <text x="56" y="76" font-family="{MONO}" font-size="11" letter-spacing="4.5" fill="{t['muted']}">@GIT-MOUD1</text>
</g>

<g class="rise" style="animation-delay:.25s">
  <text x="54" y="140" font-family="{MONO}" font-size="58" font-weight="700" letter-spacing="2" fill="{t['text']}">MOUD</text>
  <rect class="caret" x="228" y="103" width="12" height="42" fill="{t['primary']}"/>
</g>

<rect class="rule" x="56" y="160" width="180" height="3" rx="1.5" fill="{t['primary']}"/>

<g class="rise" style="animation-delay:.75s">
  <text x="56" y="192" font-family="{MONO}" font-size="12.5" letter-spacing="2.6" fill="{t['muted']}">FLUTTER &amp; FULL STACK DEVELOPER</text>
  <text x="56" y="214" font-family="{MONO}" font-size="12.5" letter-spacing="2.6" fill="{t['accent']}">MOBILE &#183; WEB &#183; BACKEND</text>
</g>

{edges}
{nodes}

<g class="rise" style="animation-delay:2.6s">
  <circle class="pulse" cx="496" cy="220" r="3.5" fill="{t['accent']}"/>
  <text x="508" y="224" font-family="{MONO}" font-size="10" letter-spacing="2.4" fill="{t['muted']}">WIDGET TREE &#8212; ASSEMBLED ON BUILD</text>
</g>
</svg>
"""


out = Path("assets")
out.mkdir(exist_ok=True)
for name, theme in THEMES.items():
    (out / f"header-{name}.svg").write_text(build(theme), encoding="utf-8")
    print("wrote", f"header-{name}.svg")
