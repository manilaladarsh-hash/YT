import json
import hashlib

poids = [
    ("physics", "https://uwyo.catalog.acalog.com/preview_program.php?catoid=19&poid=20350"),
    ("chemistry", "https://uwyo.catalog.acalog.com/preview_program.php?catoid=19&poid=20264"),
    ("math", "https://uwyo.catalog.acalog.com/preview_program.php?catoid=19&poid=20328"),
    ("cs", "https://uwyo.catalog.acalog.com/preview_program.php?catoid=19&poid=20454"),
    ("ece", "https://uwyo.catalog.acalog.com/preview_program.php?catoid=19&poid=20463"),
    ("mech", "https://uwyo.catalog.acalog.com/preview_program.php?catoid=19&poid=20468"),
    ("chemeng", "https://uwyo.catalog.acalog.com/preview_program.php?catoid=19&poid=20437"),
    ("civil", "https://uwyo.catalog.acalog.com/preview_program.php?catoid=19&poid=20443"),
    ("earth", "https://uwyo.catalog.acalog.com/preview_program.php?catoid=19&poid=20298"),
    ("biomed", "https://uwyo.catalog.acalog.com/preview_program.php?catoid=19&poid=20502"),
    ("neuro", "https://uwyo.catalog.acalog.com/preview_program.php?catoid=19&poid=20505"),
    ("environment", "https://uwyo.catalog.acalog.com/preview_program.php?catoid=19&poid=20503"),
    ("biology", "https://uwyo.catalog.acalog.com/preview_program.php?catoid=19&poid=20388")
]

for field, url in poids:
    key = hashlib.sha1(url.encode()).hexdigest()[:16]
    with open(f".cache/pages/{key}.json", encoding="utf-8") as f:
        text = json.load(f)["text"]
    print(f"\n====================== {field.upper()} ======================")
    for line in text.split("\n"):
        l = line.lower()
        if any(k in l for k in ["admission", "bachelor", "master", "gre", "supervisor", "advisor", "deadline", "hours"]):
            print("  *", line.strip()[:140])
