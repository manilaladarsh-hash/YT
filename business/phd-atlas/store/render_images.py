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
    n_fields = len({r["field"] for r in recs})
    n_unis = len({r["uni"] for r in recs})
    IMAGES.mkdir(parents=True, exist_ok=True)
    chips = "".join(f'<span class="chip">{c}</span>' for c in
                    ["Fits your situation", "English waivers for Indian degrees", "Fee waivers + no-fee programs", "GRE & Subject GRE", "Supervisor-first rules", "Fees in ₹ · deadline plan"])
    wide = dict(PAD=64, TAG=22, H1=92, SUB=32, CHIP=22, FOOT=20)
    square = dict(PAD=40, TAG=16, H1=58, SUB=22, CHIP=15, FOOT=14)
    paid = dict(TAGTEXT="2027 ENTRY · US · UK · EUROPE · AUSTRALIA · CANADA", TITLE="STEM PhD Atlas 2027",
                SUBTEXT=f"{n} PhD programs in {n_fields} STEM fields at {n_unis} universities, checked for international applicants. Every value is linked to the official page it came from.",
                CHIPS=chips, FOOTTEXT="Built by an IISER → McMaster physics PhD student · about ₹190 in India · free updates this cycle")
    sample = dict(paid, TAGTEXT="FREE SAMPLE · 12 PROGRAMS",
                  SUBTEXT="Deadlines, fees, fee waivers, GRE and English-test rules for 12 programs across fields, plus what international applicants miss this cycle.")
    render("cover-paid", (1280, 720), {**wide, **paid})
    render("cover-sample", (1280, 720), {**wide, **sample})
    square_chips = "".join(f'<span class="chip">{c}</span>' for c in ["Every STEM field", "Fee waivers", "English waivers", "Supervisors"])
    render("thumb-paid", (600, 600), {**square, **paid, "CHIPS": square_chips, "SUBTEXT": f"{n} programs, {n_fields} fields: US, UK, Europe, Canada, Australia. Every value sourced."})
    render("thumb-sample", (600, 600), {**square, **sample, "CHIPS": square_chips, "SUBTEXT": "12 programs + what applicants miss."})
    print("rendered", sorted(p.name for p in IMAGES.glob("*.png")))


if __name__ == "__main__":
    main()
