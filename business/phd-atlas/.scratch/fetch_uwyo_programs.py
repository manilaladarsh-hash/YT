import subprocess

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
    print(f"Fetching {field}: {url}...")
    res = subprocess.run(["python", "scripts/research.py", url, "--render"], capture_output=True, text=True, encoding="utf-8")
    print(res.stdout[:160])

print("Done fetching all UWYO programs.")
