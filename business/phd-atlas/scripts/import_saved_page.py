"""Add a page saved from a normal browser to the page cache.

Some university sites (Oxford, UCL, Michigan) block automated fetches with a
bot check. Open the page in your own browser, save it with Ctrl+S ("Webpage,
HTML only"), then import it so its quotes can be checked like any other page:

  python3 scripts/import_saved_page.py URL saved.html [--date 2026-10-22]

The record is marked method "manual-save". The weekly source watch cannot
re-fetch these pages and lists them as unreachable, so check them by hand at
each refresh.
"""

import argparse
import json
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from research import CACHE, cache_paths, html_to_text  # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("url", help="the page's real address, exactly as cited in records")
    ap.add_argument("html", help="the saved .html file")
    ap.add_argument("--date", default=date.today().isoformat(), help="the day the page was saved")
    args = ap.parse_args()
    if not args.url.startswith("https://"):
        sys.exit("url must start with https://")
    html = Path(args.html).read_text(errors="replace")
    text = html_to_text(html)
    if len(text) < 800 or "security verification" in text.lower()[:500]:
        sys.exit(f"saved page looks empty or like a bot check ({len(text)} chars); save it again after it loads")
    record = {
        "url": args.url,
        "final_url": args.url,
        "status": 200,
        "method": "manual-save",
        "fetched": args.date,
        "text": text,
        "links": [],
    }
    CACHE.mkdir(parents=True, exist_ok=True)
    path = cache_paths(args.url)
    path.write_text(json.dumps(record))
    print(f"cached {len(text)} chars for {args.url} -> {path.name}")


if __name__ == "__main__":
    main()
