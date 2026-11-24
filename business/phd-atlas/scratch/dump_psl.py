import glob, json

keys = ('psl.eu', 'obspm.fr', 'dauphine', 'ephe', 'ed388', 'ed391', 'ed406', 'ed129', 'ed515', 'ed3c', 'adum')
with open('scratch/psl_all_pages.txt', 'w', encoding='utf-8') as out, open('scratch/psl_index.txt', 'w', encoding='utf-8') as idx:
    for f in sorted(glob.glob('.cache/pages/*.json')):
        d = json.load(open(f, encoding='utf-8'))
        u = d.get('url', '')
        if any(k in u for k in keys):
            txt = d.get('text', '')
            idx.write(f"{u} -> {d.get('final_url')} | status={d.get('status')} len={len(txt)}\n")
            out.write(f"=== {u} (final={d.get('final_url')}, status={d.get('status')}, len={len(txt)}) ===\n")
            out.write(txt + "\n\n")
print("done")
