"""Fetch official program pages and print only the sentences that matter.

Pages are cached under .cache/pages/ so quotes can be re-checked later.
A plain HTTP fetch is tried first; blocked or script-only pages fall back
to headless Chromium (render_fetch.cjs).

Usage:
  python3 scripts/research.py URL [URL ...] [--kw deadline,fee,...] [--window 220] [--refresh]
"""

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
from datetime import date
from pathlib import Path

import requests
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parent.parent
CACHE = ROOT / ".cache" / "pages"
UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/141.0 Safari/537.36"
)

DEFAULT_KW = [
    "deadline", "fee", "waiver", "GRE", "TOEFL", "IELTS", "Duolingo",
    "stipend", "supervisor", "English",
]


def cache_paths(url):
    key = hashlib.sha1(url.encode()).hexdigest()[:16]
    return CACHE / f"{key}.json"


BLOCK_TAGS = [
    "p", "div", "li", "ul", "ol", "tr", "table", "section", "article", "header",
    "footer", "nav", "h1", "h2", "h3", "h4", "h5", "h6", "dd", "dt", "td", "th",
]


def html_to_text(html):
    soup = BeautifulSoup(html, "lxml")
    for tag in soup(["script", "style", "noscript", "svg"]):
        tag.decompose()
    for br in soup.find_all("br"):
        br.replace_with("\n")
    for tag in soup.find_all(BLOCK_TAGS):
        tag.insert_before("\n")
        tag.insert_after("\n")
    return normalize(soup.get_text())


def normalize(text):
    lines = [re.sub(r"[ \t ]+", " ", ln).strip() for ln in text.splitlines()]
    return "\n".join(ln for ln in lines if ln)


def pdf_to_text(data):
    out = subprocess.run(
        ["pdftotext", "-layout", "-", "-"], input=data, capture_output=True, timeout=60
    )
    return normalize(out.stdout.decode("utf-8", "replace"))


def is_pdf(r):
    return r.content[:5] == b"%PDF-" or "pdf" in r.headers.get("Content-Type", "")


def render(url):
    env = dict(os.environ)
    env["NODE_PATH"] = subprocess.run(
        [shutil.which("npm") or "npm", "root", "-g"], capture_output=True, text=True, encoding="utf-8"
    ).stdout.strip()
    out = subprocess.run(
        ["node", str(ROOT / "scripts" / "render_fetch.cjs"), url],
        capture_output=True, text=True, encoding="utf-8", env=env, timeout=90,
    )
    if out.returncode != 0:
        raise RuntimeError(out.stderr.strip()[:300])
    data = json.loads(out.stdout)
    return data["status"], data["final_url"], normalize(data["text"])


def fetch(url, refresh=False, force_render=False):
    path = cache_paths(url)
    if path.exists() and not refresh:
        cached = json.loads(path.read_text(encoding="utf-8"))
        # Early caches stored PDFs as raw bytes; re-fetch those as text.
        if not cached.get("text", "").startswith("%PDF"):
            return cached
    status, final_url, text, method = 0, url, "", "http"
    try:
        r = requests.get(url, headers={"User-Agent": UA}, timeout=30)
        status, final_url = r.status_code, r.url
        if r.ok and is_pdf(r):
            text, method = pdf_to_text(r.content), "pdf"
        elif r.ok:
            text = html_to_text(r.text)
    except requests.RequestException as exc:
        text = ""
        status = f"error: {exc.__class__.__name__}"
    if method != "pdf" and (force_render or status != 200 or len(text) < 800):
        try:
            status, final_url, text = render(url)
            method = "chromium"
        except Exception as exc:  # keep the http result if rendering fails
            method = f"http (render failed: {exc})"
    links = []
    if method == "http" and status == 200:
        soup = BeautifulSoup(r.text, "lxml")
        for a in soup.find_all("a", href=True):
            label = " ".join(a.get_text(" ").split())
            links.append([label[:120], requests.compat.urljoin(final_url, a["href"])])
    record = {
        "url": url,
        "final_url": final_url,
        "status": status,
        "method": method,
        "fetched": date.today().isoformat(),
        "text": text,
        "links": links,
    }
    CACHE.mkdir(parents=True, exist_ok=True)
    # Several research sessions share the cache, so write atomically.
    tmp = path.with_suffix(f".{os.getpid()}.tmp")
    tmp.write_text(json.dumps(record), encoding="utf-8")
    os.replace(tmp, path)
    return record


def snippets(text, keywords, window, per_kw=3, context=1):
    """Return matching lines with `context` neighbouring lines, joined by ' ¶ '.

    Lines are capped at `window` characters. Each keyword contributes at most
    `per_kw` snippets so navigation menus do not flood the output.
    """
    lines = text.splitlines()
    chosen = []
    for kw in keywords:
        pattern = kw[3:] if kw.startswith("re:") else r"\b" + re.escape(kw) + r"(s|es)?\b"
        flags = 0 if kw.isupper() else re.IGNORECASE
        count = 0
        for i, ln in enumerate(lines):
            if len(ln.split()) < 3 and not re.search(r"\d", ln):
                continue  # skip bare menu labels
            if re.search(pattern, ln, flags=flags):
                chosen.append((max(0, i - context), min(len(lines), i + context + 1)))
                count += 1
                if count >= per_kw:
                    break
    chosen.sort()
    merged = []
    for s, e in chosen:
        if merged and s <= merged[-1][1]:
            merged[-1] = (merged[-1][0], max(e, merged[-1][1]))
        else:
            merged.append((s, e))
    return [" ¶ ".join(ln[:window] for ln in lines[s:e]) for s, e in merged]


PROFILE = {
    "deadline": (r"\b(Jan(uary)?|Feb(ruary)?|Mar(ch)?|Apr(il)?|Oct(ober)?|Nov(ember)?|Dec(ember)?)\.?\s+\d{1,2}\b", r"deadline|due|apply|application|consider|submit"),
    "fee": (r"(\$|USD|CAD|CDN|US\$)\s?\d{2,3}", r"fee"),
    "waiver": (r"waive", None),
    "gre": (r"\bGRE\b|Graduate Record", None),
    "english": (r"TOEFL|IELTS|Duolingo|DET\b|English (language )?proficiency|language of instruction|medium of instruction", None),
    "supervisor": (r"supervisor|advisor", None),
    "funding": (r"stipend|guarantee|funding package|fully funded|financial support", None),
    "entry": (r"master'?s degree|M\.Sc\.? degree|bachelor'?s degree|direct(ly)? (entry|to the Ph)", None),
}


def sentences(text):
    flat = re.sub(r"\s*\n\s*", " ¶ ", text)
    parts = re.split(r"(?<=[.?!])\s+(?=[A-Z])|\s¶\s", flat)
    return [p.strip() for p in parts if len(p.strip()) > 12]


def profile(text, per_cat=3, cap=360):
    out = {}
    sents = sentences(text)
    for cat, (pat, must) in PROFILE.items():
        hits = []
        for snt in sents:
            if len(snt.split()) < 7 and not re.search(r"\d", snt):
                continue  # navigation labels
            if re.search(pat, snt, re.I) and (must is None or re.search(must, snt, re.I)):
                if snt not in hits:
                    hits.append(snt)
            if len(hits) >= per_cat:
                break
        out[cat] = [h[:cap] for h in hits]
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("urls", nargs="+")
    ap.add_argument("--kw", default=",".join(DEFAULT_KW))
    ap.add_argument("--window", type=int, default=400, help="max characters per line")
    ap.add_argument("--per-kw", type=int, default=3)
    ap.add_argument("--context", type=int, default=1)
    ap.add_argument("--refresh", action="store_true")
    ap.add_argument("--render", action="store_true", help="force headless Chromium")
    ap.add_argument("--profile", action="store_true", help="print standard admissions facts by category")
    ap.add_argument("--max", type=int, default=12, help="max snippets per page")
    ap.add_argument("--links", default="", help="print links whose text/href match these words")
    args = ap.parse_args()
    keywords = [k.strip() for k in args.kw.split(",") if k.strip()]
    link_words = [k.strip().lower() for k in args.links.split(",") if k.strip()]
    for url in args.urls:
        rec = fetch(url, refresh=args.refresh or args.render, force_render=args.render)
        print(f"=== {url}\n    status={rec['status']} via={rec['method']} chars={len(rec['text'])} final={rec['final_url']}")
        if link_words:
            seen = set()
            for label, href in rec.get("links", []):
                hay = (label + " " + href).lower()
                if any(w in hay for w in link_words) and href not in seen:
                    seen.add(href)
                    print(f"  → {label} :: {href}")
        if args.profile:
            for cat, hits in profile(rec["text"], args.per_kw).items():
                for h in hits:
                    print(f"  [{cat}] {h}")
        elif keywords:
            found = snippets(rec["text"], keywords, args.window, args.per_kw, args.context)
            for snip in found[: args.max]:
                print("  •", snip)
        print()


if __name__ == "__main__":
    sys.exit(main())
