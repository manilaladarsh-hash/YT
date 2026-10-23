"""Numbers and lists quoted in the Playbook, START-HERE and the free sample.

Everything is computed from the effective records at build time, so the text
stays true as research waves add programs.
"""

import collections
import statistics
from datetime import date


def compute(recs, b):
    code = lambda r, k: r["fields"][k]["code"]
    by_uni = {}
    for r in recs:
        by_uni.setdefault(r["uni"], r)  # university-wide fields are identical for every program there
    unis = list(by_uni.values())
    region = b.region_of
    us = [r for r in recs if r["country"] == "USA"]
    uk = [r for r in recs if r["country"] == "United Kingdom"]
    ca = [r for r in recs if r["country"] == "Canada"]
    au = [r for r in recs if region(r) == "Australia & NZ"]
    eu = [r for r in recs if region(r) == "Europe"]
    dated = sorted((r for r in recs if b.deadline_date(r)), key=lambda r: (r["fields"]["deadline"]["code"], b.label(r)))
    today = date.today().isoformat()
    upcoming = [r for r in dated if r["fields"]["deadline"]["code"] >= today]
    month = lambda m: str(sum(1 for r in dated if r["fields"]["deadline"]["code"][:7] == m))
    us_dates = collections.Counter(r["fields"]["deadline"]["code"] for r in us if b.deadline_date(r))
    top_us = us_dates.most_common(1)[0] if us_dates else ("2026-12-15", 0)

    def median_fee(cur):
        vals = [b.fee_parts(code(r, "app_fee"))[0] for r in recs if code(r, "app_fee").endswith(" " + cur)]
        return statistics.median(vals) if vals else None

    def money(cur):
        m = median_fee(cur)
        return (f"{m:.0f}", b.fmt_inr(b.convert(m, cur, "INR"))) if m else ("n/a", "n/a")

    usd, gbp, cad = money("USD"), money("GBP"), money("CAD")
    no_fee = lambda r: code(r, "app_fee").startswith("0") or code(r, "fee_waiver") == "No fee"
    stated = lambda rs, k: [r for r in rs if code(r, k) != "Not stated"]

    def share(rs, k, ok):
        s = stated(rs, k)
        return f"{round(100 * sum(1 for r in s if code(r, k) in ok) / len(s))}%" if s else "n/a"

    rows = []
    gre_rows = []
    for f in b.TAXONOMY["fields"]:
        fr = [r for r in recs if f["id"] == r["field"] or f["id"] in r["also_fields"]]
        if not fr:
            continue
        fus = [r for r in fr if r["country"] == "USA"]
        dates = collections.Counter(r["fields"]["deadline"]["code"] for r in fus if b.deadline_date(r))
        rows.append([f["name"], len(fr), share(fr, "entry_route", {"Direct from bachelor's", "Either"}),
                     share(fr, "gre_subject", {"Required"}) if f["subject_gre"] else "no test",
                     share(fr, "funding", {"Guaranteed"}), share(fr, "supervisor", {"Required"}),
                     b.nice_date(date.fromisoformat(dates.most_common(1)[0][0])) if dates else "—"])
        if fus:
            gre_rows.append([f["name"], len(fus), share(fus, "gre_general", {"Required"}),
                             share(fus, "gre_general", {"Optional", "Not required", "Not considered"}),
                             share(fus, "gre_general", {"Not considered"})])
    eng = lambda c: [r for r in unis if code(r, "english_waiver") in c]
    uk_unis = [r for r in unis if r["country"] == "United Kingdom"]
    names_u = lambda rs: ", ".join(sorted({b.short_uni(r) for r in rs})[:14]) + ("" if len({b.short_uni(r) for r in rs}) <= 14 else f" and {len({b.short_uni(r) for r in rs}) - 14} more") if rs else "none in this edition"
    subj_req = [r for r in recs if code(r, "gre_subject") == "Required"]
    subj_by_field = collections.defaultdict(list)
    for r in subj_req:
        subj_by_field[r["field_name"]].append(b.short_uni(r))
    subj_text = "\n".join(f"- **{fn}:** {', '.join(sorted(set(v)))}" for fn, v in sorted(subj_by_field.items())) or "- None in this edition."
    waiver_av = [r for r in recs if code(r, "fee_waiver") == "Available" and not no_fee(r)]
    pos = lambda r: code(r, "deadline") in ("Per position", "Rolling") or code(r, "supervisor") == "Required"
    fx = b.FX
    values = {
        "VERSION": b.VERSION,
        "CHECKED": date.fromisoformat(max(r["checked"] for r in recs)).strftime("%B %d, %Y").replace(" 0", " "),
        "N": f"{len(recs):,}",
        "N_FIELDS": str(len({x for r in recs for x in [r["field"]] + r["also_fields"]})),
        "N_UNIS": str(len(unis)),
        "N_US": f"{len(us):,}", "N_UK": str(len(uk)), "N_CA": str(len(ca)), "N_AU": str(len(au)), "N_EU": str(len(eu)),
        "EU_COUNTRIES": ", ".join(sorted({r["country"] for r in eu})) or "none",
        "AU_COUNTRIES": " and ".join(sorted({r["country"] for r in au})) or "none in this edition",
        "NOV_COUNT": month("2026-11"), "DEC_COUNT": month("2026-12"), "JAN_COUNT": month("2027-01"),
        "TOP_US_DATE": b.nice_date(date.fromisoformat(top_us[0])), "TOP_US_DATE_COUNT": str(top_us[1]),
        "US_DATED_COUNT": str(sum(us_dates.values())), "N_DATED": f"{len(dated):,}",
        "DEADLINE_TABLE": b.md_table(["Deadline", "Program", "Country", "Note"],
                                     [[b.deadline_text(r), b.label(r), r["country"], b.flags_text(r["fields"]["deadline"])] for r in upcoming[:40]]),
        "MEDIAN_USD": usd[0], "MEDIAN_USD_INR": usd[1], "MEDIAN_GBP": gbp[0], "MEDIAN_GBP_INR": gbp[1],
        "MEDIAN_CAD": cad[0], "MEDIAN_CAD_INR": cad[1],
        "TEN_US_INR": b.fmt_inr(10 * b.convert(median_fee("USD"), "USD", "INR")) if median_fee("USD") else "n/a",
        "NO_FEE_COUNT": str(sum(1 for r in recs if no_fee(r))),
        "WAIVER_ROUTE_COUNT": str(sum(1 for r in recs if not no_fee(r) and code(r, "fee_waiver") in ("Available", "Limited"))),
        "FX_SOURCE": fx["source"], "FX_DATE": date.fromisoformat(fx["date"]).strftime("%B %d, %Y").replace(" 0", " "),
        "USD_INR": f"{fx['cad_per_unit']['USD'] / fx['cad_per_unit']['INR']:.1f}",
        "ENGLISH_YES_COUNT": str(len(eng({"Yes"}))), "ENGLISH_YES_LIST": names_u(eng({"Yes"})),
        "ENGLISH_CONDITIONAL_COUNT": str(len(eng({"Conditional", "Check tool"}))), "ENGLISH_CONDITIONAL_LIST": names_u(eng({"Conditional", "Check tool"})),
        "ENGLISH_NO_COUNT": str(len(eng({"No"}))), "ENGLISH_NO_LIST": names_u(eng({"No"})),
        "GRE_REQUIRED_COUNT": str(sum(1 for r in recs if code(r, "gre_general") == "Required")),
        "GRE_OPTIONAL_COUNT": str(sum(1 for r in recs if code(r, "gre_general") in ("Optional", "Not required"))),
        "GRE_NOT_CONSIDERED_COUNT": str(sum(1 for r in recs if code(r, "gre_general") == "Not considered")),
        "GRE_FIELD_TABLE": b.md_table(["Field (US programs)", "Programs", "GRE General required", "Optional or not needed", "Will not look at it"], gre_rows),
        "SUBJECT_REQUIRED_LIST": subj_text,
        "FIELD_TABLE": b.md_table(["Field", "Programs", "Bachelor's OK", "Subject GRE required", "Funding guaranteed", "Supervisor first", "Most common US deadline"], rows),
        "UK_NO_FEE_COUNT": str(sum(1 for r in uk if no_fee(r))),
        "UK_ENGLISH_NO_LIST": names_u([r for r in uk_unis if code(r, "english_waiver") == "No"]),
        "UK_ENGLISH_ROUTE_LIST": names_u([r for r in uk_unis if code(r, "english_waiver") in ("Yes", "Conditional")]),
        "EU_POSITION_COUNT": str(sum(1 for r in eu if pos(r))),
        "EU_NO_FEE_COUNT": str(sum(1 for r in eu if no_fee(r))),
        "EU_MASTERS_PCT": share(eu, "entry_route", {"Master's usually required"}),
        "AU_SUP_PCT": share(au, "supervisor", {"Required"}),
        "AU_NO_FEE_COUNT": str(sum(1 for r in au if no_fee(r))),
        "CA_SUP_PCT": share(ca, "supervisor", {"Required", "Recommended"}),
        "CA_MASTERS_PCT": share(ca, "entry_route", {"Master's usually required"}),
        "WAIVER_AVAILABLE_COUNT": str(len(waiver_av)), "WAIVER_AVAILABLE_LIST": b.names(waiver_av, lambda r: True, 10, True),
        "WAIVER_LIMITED_COUNT": str(sum(1 for r in recs if code(r, "fee_waiver") == "Limited" and not no_fee(r))),
        "WAIVER_NONE_COUNT": str(sum(1 for r in recs if code(r, "fee_waiver") in ("Domestic only", "None"))),
        "NOT_STATED_PCT": f"{round(100 * b.not_stated_share(recs))}%",
    }
    return values
