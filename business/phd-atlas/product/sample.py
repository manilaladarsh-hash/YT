"""Free sample PDF: a dozen program cards across fields, plus what the full kit adds.

Programs are picked from the data at build time (the best-documented program per
field, then more regions), so the sample follows the research waves.
"""

import html

N_CARDS = 12
CARD_FIELDS = [("deadline", "Deadline"), ("app_fee", "Fee"), ("fee_waiver", "Fee waiver"), ("funding", "Funding"),
               ("gre_general", "GRE General"), ("gre_subject", "Subject GRE"), ("english_waiver", "English waiver"),
               ("supervisor", "Supervisor first"), ("entry_route", "Entry")]
TONE = {
    "fee_waiver": {"Available": "good", "No fee": "good", "Limited": "warn", "Domestic only": "bad", "None": "bad"},
    "gre_general": {"Required": "bad", "Recommended": "warn", "Optional": "good", "Not required": "good", "Not considered": "good"},
    "gre_subject": {"Required": "bad", "Recommended": "warn", "Optional": "good", "Not required": "good", "Not considered": "good"},
    "english_waiver": {"Yes": "good", "Conditional": "warn", "No": "bad", "Check tool": "warn"},
    "supervisor": {"Required": "warn", "Recommended": "warn", "Not required": "good"},
    "funding": {"Guaranteed": "good", "Typical": "good", "Competitive": "warn"},
    "entry_route": {"Direct from bachelor's": "good", "Either": "good", "Master's usually required": "warn"},
}
CSS = """
.cards { display: grid; grid-template-columns: 1fr 1fr; gap: 8pt; }
.card { border: 1px solid #dcdfe4; border-left: 3pt solid var(--gc); border-radius: 5pt; padding: 7pt 9pt; break-inside: avoid; font-size: 8.8pt; }
.card .ftag { font-size: 7.5pt; font-weight: 700; text-transform: uppercase; letter-spacing: .04em; color: var(--gc); }
.card h3 { margin: 1pt 0 0; font-size: 11pt; }
.card .meta { color: #5b6573; font-size: 8pt; margin-bottom: 4pt; }
.card dl { display: grid; grid-template-columns: auto 1fr auto 1fr; gap: 2pt 6pt; margin: 0; align-items: baseline; }
.card dl .wide { grid-column: 2 / 5; }
.card dt { color: #5b6573; }
.card dd { margin: 0; }
.card q { display: block; margin-top: 5pt; padding: 3pt 6pt; background: #f4f6f8; border-left: 2pt solid #1f5f8b; font-size: 8pt; quotes: "\\201C" "\\201D"; }
.card .src { font-size: 7.5pt; }
.facts li { margin: 3pt 0; }
"""
GROUP_COLOR = {"Physical sciences": "#2a5fa8", "Mathematical sciences": "#6b3fa0", "Computing": "#0f7a73",
               "Life sciences": "#2e7d32", "Earth & environment": "#8a5a14", "Engineering": "#b3471f"}


def stated(r, b):
    return sum(r["fields"][k]["code"] != "Not stated" for k in b.ALL_FIELDS)


def pick(recs, b):
    """Best-documented program per field first, then fill with unseen regions and universities."""
    ranked = sorted(recs, key=lambda r: (-stated(r, b), b.label(r)))
    chosen, fields, unis = [], set(), set()
    for r in ranked:
        if r["field"] not in fields and r["uni"] not in unis:
            chosen.append(r); fields.add(r["field"]); unis.add(r["uni"])
    chosen = chosen[:N_CARDS]
    regions = {b.region_of(r) for r in chosen}
    for want_new_region in (True, False):
        for r in ranked:
            if len(chosen) >= N_CARDS:
                break
            if r in chosen or r["uni"] in unis or (want_new_region and b.region_of(r) in regions):
                continue
            chosen.append(r); unis.add(r["uni"]); regions.add(b.region_of(r))
    order = [f["id"] for f in b.TAXONOMY["fields"]]
    return sorted(chosen, key=lambda r: (order.index(r["field"]), b.label(r)))


def cell(k, r, b):
    f = r["fields"][k]
    code = f["code"]
    if code == "Not stated":
        return "<span class='badge na'>Not stated</span>"
    if k == "deadline":
        text = b.deadline_text(r) + (" (year inferred)" if f.get("inferred") else "")
    elif k == "app_fee":
        inr = b.fee_inr(r)
        text = "No fee" if code.startswith("0") else (f"≈ {b.fmt_inr(inr)} ({code})" if inr else code)
    else:
        text = code
    tone = TONE.get(k, {}).get(code, "")
    return f"<span class='badge {tone}'>{html.escape(text)}</span>" if tone else html.escape(text)


def card(r, b):
    f = b.FIELD_BY_ID[r["field"]]
    also = ", ".join(b.FIELD_BY_ID[x]["name"] for x in r["also_fields"])
    meta = " · ".join(x for x in [r["name"] or r["department"], r["country"]] if x)
    rows = "".join(f"<dt>{lab}</dt><dd{' class=wide' if k == 'entry_route' else ''}>{cell(k, r, b)}</dd>" for k, lab in CARD_FIELDS)
    q = r["fields"]["deadline"] if r["fields"]["deadline"]["quote"] else next(
        (r["fields"][k] for k in b.ALL_FIELDS if r["fields"][k]["quote"]), None)
    quote = (f"<q>{html.escape(q['quote'].split(' | ')[0])}</q><a class='src' href='{html.escape(q['url'], quote=True)}'>Source ↗</a>" if q else "")
    return (f"<div class='card' style='--gc:{GROUP_COLOR.get(f['group'], '#1f5f8b')}'>"
            f"<div class='ftag'>{html.escape(f['name'])}{(' + ' + html.escape(also)) if also else ''}</div>"
            f"<h3>{html.escape(b.short_uni(r))}</h3><div class='meta'>{html.escape(meta)}</div>"
            f"<dl>{rows}</dl>{quote}</div>")


def facts(recs, values, b):
    code = lambda r, k: r["fields"][k]["code"]
    out = []
    subj = [r for r in recs if code(r, "gre_subject") == "Required"]
    if subj:
        out.append(f"<b>The GRE Subject test is still required</b> at {len(subj)} programs, including "
                   f"{html.escape(b.names(subj, lambda r: True, 6, True))}.")
    out.append(f"<b>{values['NO_FEE_COUNT']} programs charge no application fee</b>, and {values['WAIVER_AVAILABLE_COUNT']} more "
               f"offer a fee waiver to international applicants.")
    if values["ENGLISH_YES_COUNT"] != "0":
        out.append(f"<b>{values['ENGLISH_YES_COUNT']} universities accept an English-medium Indian degree</b> instead of TOEFL or IELTS, "
                   f"{values['ENGLISH_CONDITIONAL_COUNT']} with conditions; {values['ENGLISH_NO_COUNT']} require a test regardless.")
    if values["TOP_US_DATE_COUNT"] != "0":
        out.append(f"<b>{values['TOP_US_DATE']} is the most common US deadline</b> ({values['TOP_US_DATE_COUNT']} programs). "
                   f"{values['DEC_COUNT']} deadlines in the Atlas fall in December.")
    sup = [r for r in recs if code(r, "supervisor") == "Required"]
    if sup:
        out.append(f"<b>{len(sup)} programs need a supervisor's agreement before admission</b>, mostly in Europe, Australia and Canada.")
    return "".join(f"<li>{x}</li>" for x in out)


def write(recs, path, values, b):
    chosen = pick(recs, b)
    buy = ""
    if b.PAID_URL:
        link = html.escape(f"{b.PAID_URL}?utm_source=sample&utm_medium=pdf&utm_campaign=launch2026", quote=True)
        buy = f"<p>Get the full Atlas: <a href='{link}'>{html.escape(b.PAID_URL)}</a></p>"
    n_fields = len({r["field"] for r in chosen})
    body = f"""<style>{CSS}</style>
<div class="cover" style="padding-top:6mm"><span class="tag">FREE SAMPLE · {values['CHECKED']}</span>
<h1>{html.escape(b.TITLE)}</h1>
<p><b>{len(chosen)} of {values['N']} programs</b> in {n_fields} of {values['N_FIELDS']} fields. Every value is copied from an official university page.</p></div>
<h2>What applicants miss</h2>
<ul class="facts">{facts(recs, values, b)}</ul>
<h2>{len(chosen)} programs</h2>
<div class="cards">{''.join(card(r, b) for r in chosen)}</div>
<h2>The full kit</h2>
<ul>
<li><b>Offline explorer</b>: all {values['N']} programs at {values['N_UNIS']} universities. Enter your degree, tests and budget, and each program shows what fits and what to check, with the official sentence behind every value.</li>
<li><b>My plan</b>: deadlines in date order, total fees in ₹, a checklist per program and a calendar file.</li>
<li><b>Planner workbook</b> and <b>Playbook</b>: timeline, English tests for Indian degrees, GRE, how each field admits, country systems, supervisor emails, SOP, letters, fee waivers.</li>
<li>Free updates for the 2027 cycle. 14-day refund.</li>
</ul>
<p><b>{html.escape(b.PRICE_LINE)}</b></p>
{buy}
<p class="note">Confirm every value on the official page before you pay or submit. Not affiliated with any university. Not immigration, visa or legal advice.</p>
"""
    b.to_pdf(b.html_doc(f"{b.TITLE}: Free Sample", body), path, "sample")
    return chosen
