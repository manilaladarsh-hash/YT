import json
from pathlib import Path

ROOT = Path(".")
with open("data/schema.json", encoding="utf-8") as f:
    schema = json.load(f)
UF = list(schema["university_fields"])

unis = {p.stem: json.load(open(p, encoding="utf-8")) for p in Path("data/universities").glob("*.json")}
progs = [json.load(open(p, encoding="utf-8")) for p in Path("data/programs").glob("*.json")]

# Group programs by university
uni_progs = {}
for p in progs:
    u = p["university"]
    uni_progs.setdefault(u, []).append(p)

candidates = []
for uid, u in sorted(unis.items()):
    p_list = uni_progs.get(uid, [])
    fields = {p["field"] for p in p_list}
    has_physics = "physics" in fields
    has_math = "math" in fields
    
    missing_uf = [f for f in UF if u["fields"].get(f, {}).get("code") == "Not stated"]
    
    # Count missing in physics & math specifically
    ns_physics = 0
    ns_math = 0
    for p in p_list:
        if p["field"] == "physics":
            for k in p["fields"]:
                eff_code = p["fields"][k]["code"]
                if eff_code == "Not stated" and k in UF:
                    eff_code = u["fields"].get(k, {}).get("code", "Not stated")
                if eff_code == "Not stated":
                    ns_physics += 1
        elif p["field"] == "math":
            for k in p["fields"]:
                eff_code = p["fields"][k]["code"]
                if eff_code == "Not stated" and k in UF:
                    eff_code = u["fields"].get(k, {}).get("code", "Not stated")
                if eff_code == "Not stated":
                    ns_math += 1

    total_progs = len(p_list)
    impact = len(missing_uf) * total_progs
    candidates.append({
        "uid": uid,
        "name": u["institution"],
        "country": u["country"],
        "has_physics": has_physics,
        "has_math": has_math,
        "missing_uf": missing_uf,
        "len_missing_uf": len(missing_uf),
        "total_progs": total_progs,
        "impact": impact,
        "ns_physics": ns_physics,
        "ns_math": ns_math,
        "pm_impact": (1 if has_physics else 0) * len(missing_uf) + (1 if has_math else 0) * len(missing_uf)
    })

# Filter for those with physics or math and missing UF
pm_candidates = [c for c in candidates if (c["has_physics"] or c["has_math"]) and c["len_missing_uf"] > 0]
pm_candidates.sort(key=lambda x: (x["pm_impact"], x["impact"]), reverse=True)

print(f"Top 25 universities with Physics/Math programs and missing university fields:")
print(f"{'UID':<15} {'Country':<12} {'Missing UF':<12} {'Total P':<8} {'Tot Impact':<12} {'PM Impact':<10} {'Missing Fields'}")
print("-" * 95)
for c in pm_candidates[:25]:
    print(f"{c['uid']:<15} {c['country']:<12} {c['len_missing_uf']:<12} {c['total_progs']:<8} {c['impact']:<12} {c['pm_impact']:<10} {', '.join(c['missing_uf'])}")
