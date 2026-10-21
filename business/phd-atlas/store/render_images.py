"""Render the Gumroad cover and thumbnail images from store/templates/cover.html.

Usage: python3 store/render_images.py
Writes store/images/{cover-paid,cover-sample,thumb-paid,thumb-sample}.png
"""

import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "product"))
import build  # noqa: E402

IMAGES = ROOT / "store" / "images"
TPL = (ROOT / "store" / "templates" / "cover.html").read_text()


def render(name, size, values):
    w, h = size
    html = TPL
    for k, v in {**values, "W": w, "H": h}.items():
        html = html.replace("{{" + k + "}}", str(v))
    src = build.BUILD / f"{name}.html"
    build.BUILD.mkdir(parents=True, exist_ok=True)
    src.write_text(html, encoding="utf-8")
    env = dict(os.environ)
    env["NODE_PATH"] = subprocess.run(["npm", "root", "-g"], capture_output=True, text=True).stdout.strip()
    subprocess.run(["node", str(ROOT / "product" / "pdf.cjs"), str(src), str(IMAGES / f"{name}.png"), "--png", f"{w}x{h}"],
                   check=True, env=env)


def main():
    recs = build.load()
    n = len(recs)
    IMAGES.mkdir(parents=True, exist_ok=True)
    chips = "".join(f'<span class="chip">{c}</span>' for c in
                    ["Physics GRE rules", "Fee waivers for internationals", "English-test waivers", "Canada supervisor-first", "Europe position-based PhDs", "Offline explorer + planner"])
    wide = dict(PAD=64, TAG=22, H1=92, SUB=32, CHIP=22, FOOT=20)
    square = dict(PAD=40, TAG=16, H1=58, SUB=22, CHIP=15, FOOT=14)
    paid = dict(TAGTEXT="2027 ENTRY · US · CANADA · EUROPE", TITLE="Physics PhD Atlas 2027",
                SUBTEXT=f"{n} physics PhD programs checked for international applicants. Every value is linked to the official page it came from.",
                CHIPS=chips, FOOTTEXT="Built by an IISER → McMaster physics PhD student · free updates this cycle · 14-day refund")
    sample = dict(paid, TAGTEXT="FREE SAMPLE · 10 PROGRAMS",
                  SUBTEXT="Deadlines, fees, fee waivers, Physics GRE and English-test rules for 10 programs, plus 6 things international applicants miss this cycle.")
    render("cover-paid", (1280, 720), {**wide, **paid})
    render("cover-sample", (1280, 720), {**wide, **sample})
    square_chips = "".join(f'<span class="chip">{c}</span>' for c in ["Physics GRE", "Fee waivers", "English waivers", "Supervisors"])
    render("thumb-paid", (600, 600), {**square, **paid, "CHIPS": square_chips, "SUBTEXT": f"{n} programs in the US, Canada and Europe, every value sourced."})
    render("thumb-sample", (600, 600), {**square, **sample, "CHIPS": square_chips, "SUBTEXT": "10 programs + 6 things applicants miss."})
    print("rendered", sorted(p.name for p in IMAGES.glob("*.png")))


if __name__ == "__main__":
    main()
