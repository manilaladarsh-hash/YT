import json
from pathlib import Path

targets = {
    "https://webusers.i3s.unice.fr/edstic/index-en.php",
    "https://enseignement.curie.fr/article/faire-son-doctorat",
    "https://www.minesparis.psl.eu/ismme/axes-scientifiques-et-laboratoires-daccueil/energetique-genie-des-procedes/",
    "https://www.minesparis.psl.eu/ismme/sujets-de-these-candidatures-et-recrutement/",
    "https://www.minesparis.psl.eu/ismme/la-vie-de-lecole-doctorale/sujets-de-these-candidatures-et-recrutement/",
    "https://ed561.u-paris.fr/",
}
hits = []
for p in Path(".cache/pages").glob("*.json"):
    d = json.loads(p.read_text(encoding="utf-8"))
    if d.get("url") in targets or d.get("final_url") in targets:
        hits.append(d)
out = []
for d in hits:
    out.append(f"=== {d.get('url')} (final={d.get('final_url')}) len={len(d.get('text',''))} ===\n" + d.get("text", ""))
Path("scratch/psl_extra_ed.txt").write_text("\n\n".join(out), encoding="utf-8")
print("Wrote", len(hits), "pages")
