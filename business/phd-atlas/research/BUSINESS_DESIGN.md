# Business design: Physics PhD Atlas 2027

## Customer
Self-directed final-year BS-MS, MSc or BSc physics and astronomy students applying to US, Canadian and European PhD programs for 2027 entry. Most are in India (IISERs, IITs, IISc, NISER, central and state universities); there are secondary buyers in other countries. They are budget-conscious and often unaware of rules specific to international applicants.

## Problem
Each program publishes its own rules on different pages, and some of them contradict each other. The details that matter most to international applicants are the hardest to find:
- which programs waive fees for internationals;
- whether an English-medium Indian degree waives the English test;
- whether the Physics GRE is required this year;
- whether Canada requires a supervisor before admission, or a European program hires through advertised positions;
- whether a master's is needed first.

Getting these wrong costs $75–155 per application, missed deadlines, or a rejected file.

## Offer (v1.1)
| Component | What it does |
|---|---|
| Atlas.html | Offline explorer covering 40 programs (21 US, 10 Canada, 9 Europe: UK, Switzerland, Germany, Italy, Netherlands) and 10 fields each. Every value shows the exact official quote and link. |
| Atlas.xlsx | Planner: auto-filling shortlist, deadline countdown, fee budget by currency, recommender tracker, supervisor-outreach log, full sources sheet. |
| Atlas.csv | Raw data. |
| Playbook.pdf | 11 pages: timeline, English-test rules, GRE strategy, Canadian supervisors, how Europe differs (positions, fees, master's-first rules), email template, SOP framework, letter kit, ethical fee-waiver requests, checklist. |
| Free sample | 10 programs (US, Canada, Europe) plus "6 things international applicants miss". |
| Updates | Free for the Fall 2027 cycle, delivered by Gumroad's update emails. |

**Out of scope:** visa or study-permit advice (official links only), SOP writing or editing, and admission predictions.

## Differentiation
1. **Primary-source verification.** Every value carries the quote it came from, the URL and the date, and a script proves each quote exists on the page. No competitor found offers this.
2. **Fields aimed at international applicants** that free directories omit.
3. **Honest uncertainty.** "Not stated", "year inferred" and "sources conflict" are shown instead of guesses.
4. **Founder credibility.** It is built by an IISER → McMaster physics PhD student (your approval needed to show this publicly).
5. **Works offline**, and costs a fraction of one application fee.

## Pricing (a hypothesis to test)
- List price $15 USD. Gumroad's built-in purchasing-power parity is on, with the discount capped at 50% (≈$7.50 in India). This sits inside the market's range: generic kits run $1–£39.99, and SOP reviews $50–200.
- The free sample doubles as the lead magnet (a $0 product with an email opt-in).
- 14-day no-questions refund.

## Delivery process (automated)
1. The buyer pays on Gumroad, which acts as merchant of record and handles sales tax, VAT and GST.
2. Gumroad sends the receipt and ZIP download instantly.
3. Workflow emails go out automatically: welcome with a quick start (day 0), then the usefulness and checkout survey (day 10).
4. Data refreshes are uploaded as new versions, and Gumroad emails existing buyers ("Send update").
5. A weekly GitHub Action re-checks every cited page and opens an issue if a quote disappears.

## Acquisition
| Channel | Mechanism | Owner time | Cost |
|---|---|---|---|
| A. Your network | ~10 personal messages plus 1–3 group posts (exact drafts) | 20–30 min once | $0 |
| B. Reddit | Value-first posts linking the free sample, within each subreddit's rules | 10 min plus replies | $0 |
| C. Gumroad Discover | Passive marketplace listing | 0 | 30% fee on those sales |
| D. Next season | Free static SEO site (one page per program) on GitHub Pages | Build by me | $0 |

## Financial scenarios
Run with `python3 research/financials.py`. Assumptions are in the script's header. Only Gumroad's 10% + $0.50 and 30% Discover fees are published facts; everything else is an assumption.

| Scenario | This season (orders → net) | Next full season (orders → net) | Key assumptions |
|---|---|---|---|
| Conservative | 5 → **$33** | 30 → **$197** | 70% buy at the PPP price, 10% refunds, no Discover sales |
| Base | 25 → **$185** | 120 → **$886** | 60% PPP, 7% refunds, 5% via Discover |
| Optimistic | 80 → **$648** | 400 (three editions) → **$3,238** | 50% PPP, 5% refunds, 10% via Discover |

All scenarios assume:
- card processing of 2.9% + $0.30 charged on top of Gumroad's fee (conservative);
- fees on refunded orders are not returned;
- a 2% PayPal payout fee;
- $0 fixed costs and $0 customer-acquisition cash (your hours are counted instead).

Income is reported on your T2125. There is no GST/HST registration while you stay under the CAD 30,000 small-supplier threshold; confirm with CRA guidance or an accountant.

## Why this model fits your time limit
There is no inventory, no live service and no meetings. Support is a short FAQ plus email at ≤30 min/week. Data maintenance is automated detection plus a ~30-minute monthly refresh I can do in a session, with you approving the upload. The weekly checklist is in `ops/WEEKLY_CHECKLIST.md`.
