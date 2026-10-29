import json
from pathlib import Path

ROOT = Path(".")
with open("data/schema.json", encoding="utf-8") as f:
    schema = json.load(f)
UF = list(schema["university_fields"])
PF = list(schema["program_fields"])

unis = {p.stem: json.load(open(p, encoding="utf-8")) for p in Path("data/universities").glob("*.json")}
progs = [json.load(open(p, encoding="utf-8")) for p in Path("data/programs").glob("*.json")]

uni_progs = {}
for p in progs:
    uni_progs.setdefault(p["university"], {})[p["field"]] = p

shared = []
for uid, fields_dict in uni_progs.items():
    if "physics" in fields_dict and "math" in fields_dict:
        phys_p = fields_dict["physics"]
        math_p = fields_dict["math"]
        u = unis.get(uid)
        
        # Missing in phys
        phys_missing = []
        for k in PF:
            if phys_p["fields"].get(k, {}).get("code") == "Not stated":
                phys_missing.append(f"p_{k}")
        for k in UF:
            own = phys_p["fields"].get(k)
            eff_code = own["code"] if own and own["code"] != "Not stated" else (u["fields"].get(k, {}).get("code", "Not stated") if u else "Not stated")
            if eff_code == "Not stated":
                phys_missing.append(f"u_{k}")
                
        # Missing in math
        math_missing = []
        for k in PF:
            if math_p["fields"].get(k, {}).get("code") == "Not stated":
                math_missing.append(f"p_{k}")
        for k in UF:
            own = math_p["fields"].get(k)
            eff_code = own["code"] if own and own["code"] != "Not stated" else (u["fields"].get(k, {}).get("code", "Not stated") if u else "Not stated")
            if eff_code == "Not stated":
                math_missing.append(f"u_{k}")
                
        tot_missing = len(phys_missing) + len(math_missing)
        if tot_missing > 0:
            shared.append({
                "uid": uid,
                "name": u["institution"] if u else uid,
                "country": u["country"] if u else "",
                "tot": tot_missing,
                "phys_m": len(phys_missing),
                "math_m": len(math_missing),
                "phys_keys": phys_missing,
                "math_keys": math_missing
            })

shared.sort(key=lambda x: x["tot"], reverse=True)

print(f"Universities with BOTH Physics and Math programs having missing values ({len(shared)}):")
for s in shared[:30]:
    print(f"{s['uid']:<16} ({s['country']:<10}): Total={s['tot']:<2} (Phys={s['phys_m']}, Math={s['math_m']})")
    print(f"   Phys: {', '.join(s['phys_keys'])}")
    print(f"   Math: {', '.join(s['math_keys'])}")
