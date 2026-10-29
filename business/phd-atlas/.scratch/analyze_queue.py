import json
from pathlib import Path

ROOT = Path(".")
with open("data/schema.json", encoding="utf-8") as f:
    schema = json.load(f)
UF = list(schema["university_fields"])

unis = {p.stem: json.load(open(p, encoding="utf-8")) for p in Path("data/universities").glob("*.json")}
progs = list(Path("data/programs").glob("*.json"))

prog_counts = {}
for p in progs:
    uid = p.stem.split("--")[0]
    prog_counts[uid] = prog_counts.get(uid, 0) + 1

# Check missing university fields
uni_missing = []
for uid, u in sorted(unis.items()):
    missing_fields = [f for f in UF if u["fields"].get(f, {}).get("code") == "Not stated"]
    if missing_fields:
        p_count = prog_counts.get(uid, 0)
        impact = len(missing_fields) * p_count
        uni_missing.append((impact, uid, len(missing_fields), p_count, missing_fields))

uni_missing.sort(key=lambda x: x[0], reverse=True)

print(f"Total universities with missing university fields: {len(uni_missing)}")
print("\nTop 30 universities by potential Not stated reduction (missing_fields * program_count):")
print(f"{'UID':<18} {'Impact':<8} {'Missing_UF':<12} {'Programs':<10} {'Missing Fields'}")
print("-" * 80)
for impact, uid, n_mf, n_p, mfs in uni_missing[:30]:
    print(f"{uid:<18} {impact:<8} {n_mf:<12} {n_p:<10} {', '.join(mfs)}")
