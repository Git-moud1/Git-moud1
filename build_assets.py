"""Generate the SVG assets used by the profile README.

    python build_assets.py

Writes:
  assets/header.svg           animated banner
  assets/featured-km.svg      header card for the featured project
  assets/contact/<id>.svg     contact buttons (logo + label)
  assets/tools/<id>.svg       one toolkit tile per tool (logo + name)

Tool logos are fetched once from skillicons.dev and embedded in each tile,
so the README never depends on a third-party image host at view time.
"""

import re
import urllib.request
from pathlib import Path

ROOT = Path(__file__).parent
ASSETS = ROOT / "assets"

SANS = "'Segoe UI', Inter, 'Helvetica Neue', Helvetica, Arial, sans-serif"
MONO = "ui-monospace, SFMono-Regular, 'Cascadia Code', Menlo, Consolas, monospace"

# One palette for every asset: deep navy surface, cyan-to-indigo accent.
NAVY_0 = "#050A16"
NAVY_1 = "#0B1630"
NAVY_2 = "#0F1D38"
EDGE = "#1E3A5F"
CYAN = "#38BDF8"
SKY = "#7DD3FC"
ICE = "#E0F2FE"
INDIGO = "#818CF8"
TEXT = "#E6EDF5"
MUTED = "#93A8C3"


# --------------------------------------------------------------------------
# Banner
# --------------------------------------------------------------------------

def header() -> str:
    w, h = 1200, 360
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="Med Ma7moud — Software Engineer">
<title>Med Ma7moud — Software Engineer</title>
<defs>
  <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="{NAVY_0}"/>
    <stop offset="1" stop-color="{NAVY_1}"/>
  </linearGradient>
  <radialGradient id="orbA" cx="0.5" cy="0.5" r="0.5">
    <stop offset="0" stop-color="#1D4ED8" stop-opacity="0.55"/>
    <stop offset="1" stop-color="#1D4ED8" stop-opacity="0"/>
  </radialGradient>
  <radialGradient id="orbB" cx="0.5" cy="0.5" r="0.5">
    <stop offset="0" stop-color="#0EA5E9" stop-opacity="0.35"/>
    <stop offset="1" stop-color="#0EA5E9" stop-opacity="0"/>
  </radialGradient>
  <radialGradient id="fade" cx="0.5" cy="0.5" r="0.6">
    <stop offset="0" stop-color="#fff" stop-opacity="1"/>
    <stop offset="1" stop-color="#fff" stop-opacity="0"/>
  </radialGradient>
  <mask id="gridMask"><rect width="{w}" height="{h}" fill="url(#fade)"/></mask>
  <pattern id="dots" width="28" height="28" patternUnits="userSpaceOnUse">
    <circle cx="2" cy="2" r="1.2" fill="#3B5B86"/>
  </pattern>
  <linearGradient id="name" x1="0" y1="0" x2="1" y2="0" gradientUnits="objectBoundingBox" spreadMethod="reflect">
    <stop offset="0" stop-color="{ICE}"/>
    <stop offset="0.35" stop-color="{SKY}"/>
    <stop offset="0.65" stop-color="{CYAN}"/>
    <stop offset="1" stop-color="{INDIGO}"/>
    <animateTransform attributeName="gradientTransform" type="translate"
      values="0 0; 1 0; 0 0" dur="9s" begin="1.4s" repeatCount="indefinite"/>
  </linearGradient>
  <linearGradient id="border" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="{CYAN}" stop-opacity="0.05"/>
    <stop offset="0.5" stop-color="{CYAN}" stop-opacity="0.7"/>
    <stop offset="1" stop-color="{INDIGO}" stop-opacity="0.05"/>
  </linearGradient>
  <linearGradient id="ruleL" x1="1" y1="0" x2="0" y2="0">
    <stop offset="0" stop-color="{CYAN}"/>
    <stop offset="1" stop-color="{CYAN}" stop-opacity="0"/>
  </linearGradient>
  <linearGradient id="ruleR" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="{INDIGO}"/>
    <stop offset="1" stop-color="{INDIGO}" stop-opacity="0"/>
  </linearGradient>
  <linearGradient id="sheen" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="#fff" stop-opacity="0"/>
    <stop offset="0.5" stop-color="#fff" stop-opacity="0.85"/>
    <stop offset="1" stop-color="#fff" stop-opacity="0"/>
  </linearGradient>
  <filter id="glow" x="-20%" y="-60%" width="140%" height="220%">
    <feGaussianBlur stdDeviation="22"/>
  </filter>
  <filter id="soft" x="-50%" y="-50%" width="200%" height="200%">
    <feGaussianBlur stdDeviation="40"/>
  </filter>
  <clipPath id="frame"><rect width="{w}" height="{h}" rx="24"/></clipPath>
  <clipPath id="nameClip">
    <text x="600" y="206" text-anchor="middle" font-family="{SANS}" font-size="132" font-weight="800" letter-spacing="-3">Med Ma7moud</text>
  </clipPath>
</defs>
<style>
  .in   {{ animation: in 1.1s cubic-bezier(.16,1,.3,1) both; }}
  .sub  {{ animation: fade .9s ease-out 1s both; }}
  .rule {{ transform-box: fill-box; animation: grow .9s cubic-bezier(.16,1,.3,1) 1.1s both; }}
  .ruleL {{ transform-origin: right center; }}
  .ruleR {{ transform-origin: left center; }}
  .halo {{ animation: fade 1.6s ease-out .4s both, breathe 5s ease-in-out 2s infinite; }}
  .sweep {{ animation: sweep 6s ease-in-out 1.6s infinite; transform: translateX(-420px); }}
  @keyframes in     {{ from {{ opacity: 0; transform: translateY(22px); }} to {{ opacity: 1; transform: none; }} }}
  @keyframes fade   {{ from {{ opacity: 0; }} to {{ opacity: 1; }} }}
  @keyframes grow   {{ from {{ transform: scaleX(0); }} to {{ transform: scaleX(1); }} }}
  @keyframes breathe {{ 0%,100% {{ opacity: .6; }} 50% {{ opacity: 1; }} }}
  @keyframes sweep  {{ 0% {{ transform: translateX(-420px); }} 35%,100% {{ transform: translateX(1300px); }} }}
  @media (prefers-reduced-motion: reduce) {{
    .in, .sub, .halo {{ animation: none; opacity: 1; transform: none; }}
    .rule {{ animation: none; transform: none; }}
    .sweep {{ animation: none; opacity: 0; }}
  }}
</style>

<g clip-path="url(#frame)">
  <rect width="{w}" height="{h}" fill="url(#bg)"/>
  <rect width="{w}" height="{h}" fill="url(#dots)" mask="url(#gridMask)" opacity="0.45"/>
  <ellipse cx="250" cy="40" rx="380" ry="230" fill="url(#orbA)" filter="url(#soft)"/>
  <ellipse cx="980" cy="330" rx="400" ry="220" fill="url(#orbB)" filter="url(#soft)"/>

  <!-- name: glow layer, gradient fill, then a light sweep clipped to the glyphs -->
  <text class="halo" x="600" y="206" text-anchor="middle" font-family="{SANS}" font-size="132" font-weight="800" letter-spacing="-3" fill="{CYAN}" opacity="0.6" filter="url(#glow)">Med Ma7moud</text>
  <g class="in">
    <text x="600" y="206" text-anchor="middle" font-family="{SANS}" font-size="132" font-weight="800" letter-spacing="-3" fill="url(#name)">Med Ma7moud</text>
    <g clip-path="url(#nameClip)" opacity="0.35">
      <rect class="sweep" x="0" y="60" width="160" height="180" fill="url(#sheen)"/>
    </g>
  </g>

  <!-- subtitle -->
  <rect class="rule ruleL" x="150" y="273" width="200" height="1.5" fill="url(#ruleL)"/>
  <rect class="rule ruleR" x="850" y="273" width="200" height="1.5" fill="url(#ruleR)"/>
  <text class="sub" x="600" y="283" text-anchor="middle" font-family="{SANS}" font-size="28" font-weight="600" letter-spacing="9" fill="#BAE6FD">SOFTWARE ENGINEER</text>
</g>
<rect x="0.75" y="0.75" width="{w - 1.5}" height="{h - 1.5}" rx="23.5" fill="none" stroke="url(#border)" stroke-width="1.5"/>
</svg>
"""


# --------------------------------------------------------------------------
# Featured project card
# --------------------------------------------------------------------------

def featured_km() -> str:
    w, h = 800, 240
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="Featured project: KM — maths e-learning platform">
<title>Featured project: KM</title>
<defs>
  <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="{NAVY_0}"/>
    <stop offset="1" stop-color="{NAVY_2}"/>
  </linearGradient>
  <linearGradient id="edge" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="{CYAN}"/>
    <stop offset="1" stop-color="{INDIGO}"/>
  </linearGradient>
  <linearGradient id="title" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="{ICE}"/>
    <stop offset="0.5" stop-color="{SKY}"/>
    <stop offset="1" stop-color="{INDIGO}"/>
  </linearGradient>
  <radialGradient id="orb" cx="0.5" cy="0.5" r="0.5">
    <stop offset="0" stop-color="#1D4ED8" stop-opacity="0.5"/>
    <stop offset="1" stop-color="#1D4ED8" stop-opacity="0"/>
  </radialGradient>
  <filter id="soft" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="30"/></filter>
  <clipPath id="frame"><rect width="{w}" height="{h}" rx="20"/></clipPath>
</defs>
<g clip-path="url(#frame)">
  <rect width="{w}" height="{h}" fill="url(#bg)"/>
  <ellipse cx="680" cy="60" rx="260" ry="160" fill="url(#orb)" filter="url(#soft)"/>

  <!-- decorative formula, right side -->
  <g font-family="'Cambria Math', 'STIX Two Math', 'Times New Roman', serif" font-style="italic" fill="{SKY}" opacity="0.18">
    <text x="500" y="84" font-size="30">f(x) = ax² + bx + c</text>
    <text x="610" y="136" font-size="28">∫₀¹ x dx = ½</text>
    <text x="600" y="186" font-size="26">Δ = b² − 4ac</text>
  </g>

  <rect x="40" y="34" width="196" height="38" rx="19" fill="{CYAN}" fill-opacity="0.12" stroke="{CYAN}" stroke-opacity="0.5"/>
  <circle cx="62" cy="53" r="5.5" fill="{CYAN}">
    <animate attributeName="opacity" values="1;.3;1" dur="2.4s" repeatCount="indefinite"/>
  </circle>
  <text x="78" y="59.5" font-family="{MONO}" font-size="18" font-weight="600" letter-spacing="2" fill="{SKY}">FEATURED</text>

  <text x="38" y="152" font-family="{SANS}" font-size="92" font-weight="800" letter-spacing="-2" fill="url(#title)">K.M</text>
  <text x="40" y="200" font-family="{SANS}" font-size="32" font-weight="500" fill="{TEXT}">Mathematics e-learning platform</text>
</g>
<rect x="1" y="1" width="{w - 2}" height="{h - 2}" rx="19" fill="none" stroke="url(#edge)" stroke-width="2" stroke-opacity="0.8"/>
</svg>
"""


# --------------------------------------------------------------------------
# Toolkit tiles
# --------------------------------------------------------------------------

TOOLS = [
    # (file id, skillicons id, label)
    ("typescript", "ts", "TypeScript"),
    ("javascript", "js", "JavaScript"),
    ("python", "py", "Python"),
    ("react", "react", "React"),
    ("nextjs", "nextjs", "Next.js"),
    ("nodejs", "nodejs", "Node.js"),
    ("fastapi", "fastapi", "FastAPI"),
    ("supabase", "supabase", "Supabase"),
    ("postgresql", "postgres", "PostgreSQL"),
    ("firebase", "firebase", "Firebase"),
    ("mysql", "mysql", "MySQL"),
    ("mongodb", "mongodb", "MongoDB"),
    ("pytorch", "pytorch", "PyTorch"),
    ("scikit-learn", "sklearn", "scikit-learn"),
    ("git", "git", "Git"),
]

TILE_W, TILE_H, ICON = 104, 110, 56


def fetch_icon(skill_id: str) -> str:
    url = f"https://skillicons.dev/icons?i={skill_id}&theme=dark"
    req = urllib.request.Request(url, headers={"User-Agent": "profile-readme-build"})
    with urllib.request.urlopen(req, timeout=30) as r:
        svg = r.read().decode("utf-8")
    # Strip the outer <svg ...> wrapper; keep the inner markup.
    inner = re.sub(r"^\s*<svg[^>]*>", "", svg, count=1)
    inner = re.sub(r"</svg>\s*$", "", inner.strip(), count=1)
    return inner


def tile(label: str, icon_inner: str) -> str:
    x = (TILE_W - ICON) / 2
    return f"""<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 {TILE_W} {TILE_H}" width="{TILE_W}" height="{TILE_H}" role="img" aria-label="{label}">
<title>{label}</title>
<rect x="0.5" y="0.5" width="{TILE_W - 1}" height="{TILE_H - 1}" rx="16" fill="{NAVY_1}" stroke="{EDGE}"/>
<svg x="{x}" y="14" width="{ICON}" height="{ICON}" viewBox="0 0 256 256">{icon_inner}</svg>
<text x="{TILE_W / 2}" y="94" text-anchor="middle" font-family="{SANS}" font-size="13" font-weight="600" fill="{TEXT}">{label}</text>
</svg>
"""


CONTACTS = [
    # (file id, skillicons id, label)
    ("email", "gmail", "Email"),
    ("linkedin", "linkedin", "LinkedIn"),
    ("github", "github", "GitHub"),
]

BTN_W, BTN_H, BTN_ICON = 184, 64, 40


def contact_button(label: str, icon_inner: str) -> str:
    pad = (BTN_H - BTN_ICON) / 2
    return f"""<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 {BTN_W} {BTN_H}" width="{BTN_W}" height="{BTN_H}" role="img" aria-label="{label}">
<title>{label}</title>
<defs>
  <linearGradient id="edge" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="{CYAN}" stop-opacity="0.7"/>
    <stop offset="1" stop-color="{INDIGO}" stop-opacity="0.7"/>
  </linearGradient>
</defs>
<rect x="1" y="1" width="{BTN_W - 2}" height="{BTN_H - 2}" rx="{(BTN_H - 2) / 2}" fill="{NAVY_1}" stroke="url(#edge)" stroke-width="1.5"/>
<svg x="{pad + 4}" y="{pad}" width="{BTN_ICON}" height="{BTN_ICON}" viewBox="0 0 256 256">{icon_inner}</svg>
<text x="{pad + 4 + BTN_ICON + 14}" y="{BTN_H / 2 + 7}" font-family="{SANS}" font-size="20" font-weight="600" fill="{TEXT}">{label}</text>
</svg>
"""


def main() -> None:
    ASSETS.mkdir(exist_ok=True)
    (ASSETS / "header.svg").write_text(header(), encoding="utf-8")
    (ASSETS / "featured-km.svg").write_text(featured_km(), encoding="utf-8")

    contact_dir = ASSETS / "contact"
    contact_dir.mkdir(exist_ok=True)
    for file_id, skill_id, label in CONTACTS:
        (contact_dir / f"{file_id}.svg").write_text(
            contact_button(label, fetch_icon(skill_id)), encoding="utf-8"
        )

    tools_dir = ASSETS / "tools"
    tools_dir.mkdir(exist_ok=True)
    for file_id, skill_id, label in TOOLS:
        (tools_dir / f"{file_id}.svg").write_text(
            tile(label, fetch_icon(skill_id)), encoding="utf-8"
        )
    print(f"wrote header, featured card and {len(TOOLS)} tool tiles")


if __name__ == "__main__":
    main()
