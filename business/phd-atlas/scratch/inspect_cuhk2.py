import hashlib
import json
import pathlib

urls = [
    "https://www.gs.cuhk.edu.hk/programmes",
    "https://www.gs.cuhk.edu.hk/programmes/study-options",
    "https://www.gs.cuhk.edu.hk/admissions/faqs",
    "https://www.gs.cuhk.edu.hk/admissions/scholarships-fees/VCPHD",
    "https://www.gs.cuhk.edu.hk/regulations/general-regulations-postgraduate",
]
out = []
for u in urls:
    h = hashlib.sha1(u.encode()).hexdigest()[:16]
    p = pathlib.Path(".cache/pages") / f"{h}.json"
    d = json.loads(p.read_text(encoding="utf-8"))
    out.append("=" * 80)
    out.append(f"URL: {u}")
    out.append(f"FINAL: {d.get('final_url')}")
    out.append(f"CHARS: {len(d.get('text', ''))}")
    out.append(d.get("text", ""))
    out.append("--- RELEVANT LINKS ---")
    seen = set()
    for a, b in d.get("links", []):
        if b in seen:
            continue
        seen.add(b)
        bl = b.lower()
        if any(k in bl for k in ["programme", "phd", "mphil", "study", "fac", "sci", "erg", "med", "cuhk.edu.hk"]):
            out.append(f"  {a} -> {b}")
pathlib.Path("scratch/cuhk_central2.txt").write_text("\n".join(out), encoding="utf-8")
print("Wrote", len(urls), "sections to scratch/cuhk_central2.txt")
