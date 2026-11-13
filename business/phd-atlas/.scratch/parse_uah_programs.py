import sys, json
sys.path.insert(0, '.')
from scripts.research import cache_paths

f = cache_paths("https://www.uah.edu/graduate/programs")
d = json.load(open(f, "r", encoding="utf-8"))
text = d["text"]
lines = [l.strip() for l in text.splitlines() if l.strip()]

# Find all occurrences of Doctor of Philosophy
for i, l in enumerate(lines):
    if "Doctor of Philosophy" in l:
        prog_name = lines[i-1]
        context = lines[max(0, i-2):min(len(lines), i+8)]
        print(f"PROGRAM: {prog_name}")
        print("  CONTEXT:", context)
