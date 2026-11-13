"""Re-fetch every cited source page and report quotes that no longer appear.

A missing quote usually means the program changed a deadline, fee or rule,
so the record needs a human look. Pages that cannot be fetched (bot blocks,
outages) are listed separately; they are not treated as changes.

Usage:
  python3 scripts/check_sources.py                 # live fetch, markdown report to stdout
  python3 scripts/check_sources.py --out report.md # also write the report to a file
  python3 scripts/check_sources.py --manifest      # rewrite data/source_manifest.json from the cache
Exit code 0 always for live checks (the report carries the result), so a
scheduled job can open an issue without failing.
"""

import argparse
import hashlib
import json
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from validate_data import DATA, norm, quote_parts  # noqa: E402

MANIFEST = ROOT / "data" / "source_manifest.json"


def cited_sources():
    """Yield (record_id, field, url, quote) for every quoted claim in university and program records."""
    for f in sorted((DATA / "universities").glob("*.json")) + sorted((DATA / "programs").glob("*.json")):
        rec = json.loads(f.read_text())
        for name, fld in rec["fields"].items():
            pairs = [(fld.get("quote", ""), fld.get("url", ""))]
            pairs += [(a.get("quote", ""), a.get("url", "")) for a in fld.get("also", [])]
            for quote, url in pairs:
                if quote:
                    yield rec["id"], name, url, quote


def http_text(url):
    import requests
    from research import UA, html_to_text

    r = requests.get(url, headers={"User-Agent": UA}, timeout=30)
    if r.status_code != 200:
        raise RuntimeError(f"HTTP {r.status_code}")
    return html_to_text(r.text)


def write_manifest():
    from research import cache_paths

    out = {}
    for _, _, url, _ in cited_sources():
        if url in out:
            continue
        p = cache_paths(url)
        if not p.exists():
            continue
        rec = json.loads(p.read_text())
        out[url] = {
            "fetched": rec["fetched"],
            "method": rec["method"].split(" ")[0],
            "status": rec["status"],
            "chars": len(rec["text"]),
            "sha256": hashlib.sha256(rec["text"].encode()).hexdigest(),
        }
    MANIFEST.write_text(json.dumps(dict(sorted(out.items())), indent=2) + "\n")
    return len(out)


def live_check():
    pages, unreachable = {}, {}
    missing = []
    for pid, field, url, quote in cited_sources():
        if url not in pages and url not in unreachable:
            try:
                pages[url] = norm(http_text(url).replace("\n", " "))
            except Exception as exc:  # network errors, bot blocks
                unreachable[url] = str(exc)[:120]
        if url in unreachable:
            continue
        lost = [p for p in quote_parts(quote) if norm(p) not in pages[url]]
        if lost:
            missing.append((pid, field, url, lost[0]))
    return missing, unreachable


def report(missing, unreachable):
    lines = [f"# Source watch report: {date.today().isoformat()}", ""]
    if missing:
        lines += [f"**{len(missing)} quoted claims no longer match their source page.** Review these records:", ""]
        lines += ["| Record | Field | Missing text | Source |", "|---|---|---|---|"]
        for pid, field, url, part in missing:
            lines.append(f"| {pid} | {field} | {part[:70]} | {url} |")
    else:
        lines.append("All reachable source pages still contain their quoted text.")
    if unreachable:
        lines += ["", f"{len(unreachable)} pages could not be fetched automatically (often bot protection); spot-check by hand if they stay unreachable:", ""]
        lines += [f"- {u} ({why})" for u, why in sorted(unreachable.items())]
    return "\n".join(lines) + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--manifest", action="store_true")
    ap.add_argument("--out")
    args = ap.parse_args()
    if args.manifest:
        print(f"manifest: {write_manifest()} source pages")
        return 0
    missing, unreachable = live_check()
    text = report(missing, unreachable)
    print(text)
    if args.out:
        Path(args.out).write_text(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
