import json
from pathlib import Path

ROOT = Path(".")
with open("data/schema.json", encoding="utf-8") as f:
    schema = json.load(f)
UF = list(schema["university_fields"])
PF = list(schema["program_fields"])

unis = {p.stem: json.load(open(p, encoding="utf-8")) for p in Path("data/universities").glob("*.json")}
progs = [json.load(open(p, encoding="utf-8")) for p in Path("data/programs").glob("*.json")]

def get_missing_for_field(field_name):
    field_progs = [p for p in progs if p["field"] == field_name]
    missing_by_uni = []
    
    for p in field_progs:
        uid = p["university"]
        u = unis.get(uid)
        missing_keys = []
        for k in PF:
            if p["fields"].get(k, {}).get("code") == "Not stated":
                missing_keys.append(f"prog:{k}")
        for k in UF:
            own = p["fields"].get(k)
            eff_code = own["code"] if own and own["code"] != "Not stated" else (u["fields"].get(k, {}).get("code", "Not stated") if u else "Not stated")
            if eff_code == "Not stated":
                missing_keys.append(f"uni:{k}")
        if missing_keys:
            missing_by_uni.append((len(missing_keys), uid, u["institution"] if u else uid, u["country"] if u else "", missing_keys))
    
    missing_by_uni.sort(key=lambda x: x[0], reverse=True)
    return field_progs, missing_by_uni

phys_progs, phys_missing = get_missing_for_field("physics")
math_progs, math_missing = get_missing_for_field("math")

print(f"=== PHYSICS ({len(phys_progs)} programs, {sum(x[0] for x in phys_missing)} total missing values) ===")
print("Top 20 Physics programs by missing values:")
for count, uid, name, country, keys in phys_missing[:20]:
    print(f"  {uid:<15} ({country:<10}): {count} missing -> {', '.join(keys)}")

print(f"\n=== MATH ({len(math_progs)} programs, {sum(x[0] for x in math_missing)} total missing values) ===")
print("Top 20 Math programs by missing values:")
for count, uid, name, country, keys in math_missing[:20]:
    print(f"  {uid:<15} ({country:<10}): {count} missing -> {', '.join(keys)}")
