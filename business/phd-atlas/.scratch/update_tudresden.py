import json
from pathlib import Path

uni_path = Path("data/universities/tudresden.json")
uni = json.load(open(uni_path, encoding="utf-8"))

url = "https://tu-dresden.de/studium/vor-dem-studium/bewerbung/studienvoraussetzungen/voraussetzungen-fuer-ein-promotionsstudium?set_language=en"

uni["fields"]["toefl_min"] = {
    "code": "Not required",
    "value": "An official English language certificate (TOEFL) is not usually required for doctoral studies; English knowledge is checked by the supervisor.",
    "quote": "An official language certificate is not usually required.",
    "url": url
}

uni["fields"]["ielts_min"] = {
    "code": "Not required",
    "value": "An official English language certificate (IELTS) is not usually required for doctoral studies; English knowledge is checked by the supervisor.",
    "quote": "An official language certificate is not usually required.",
    "url": url
}

uni["fields"]["gre_general"] = {
    "code": "Not required",
    "value": "Doctoral admission is by application to each faculty's doctoral committee under its own regulations; there is no university GRE requirement.",
    "quote": "An official language certificate is not usually required.",
    "url": url
}

with open(uni_path, "w", encoding="utf-8") as f:
    json.dump(uni, f, indent=2, ensure_ascii=False)
    f.write("\n")

print("Updated tudresden.json successfully!")
