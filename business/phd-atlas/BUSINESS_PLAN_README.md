# STEM PhD Atlas 2027: business plan and research handoff

**Status as of 2026-10-24 (UTC).** After testing v1.2 (physics only), the owner asked for a full overhaul before launch and for **every STEM field** [D, 2026-10-22]. The STEM edition (v2.0) is being researched and built; **launch is paused until the release gate in §2 passes**. A Gemini deep-research audit was checked claim by claim, and the changes are in `research/AUDIT_RESPONSE.md`. There are **zero customers, sales, revenue and testimonials**. Every number below is labelled as one of:

- **[F] fact:** verified, with a source and date in §16;
- **[E] estimate or assumption:** not verified;
- **[D] decision:** made by the owner or by the assistant on the owner's behalf.

---

## 0. Read this first (for the AI receiving this file)

You are being asked to **deep-research this plan and change it where the evidence says it should change**. Ground rules from the owner:

1. **Never invent customers, testimonials, sales, demand signals or validation.** If you can't verify something, label it [E].
2. **Affordability for Indian students is a hard requirement.** The owner's words: "if I'm targeting Indian students it needs to be really affordable for them as they are usually poor. $10 is a lot for them."
3. **Keep the owner's ongoing work to about 2–3 h/week once running.** Cash spend is $0 by default.
4. **The owner is a full-time physics PhD student in Canada on a study permit.** Self-employment counts toward the 24 h/week off-campus work limit during terms [F], so every business hour is logged.
5. **Accounts.** The owner has granted broad authority for routine decisions [D, 2026-10-21]. Anything that needs the owner's accounts (Gumroad, bank, WhatsApp, Reddit, LinkedIn, GitHub settings) still has to be done by the owner.
6. **Data.** Every published program value must stay tied to an exact quote from an official page. Unknowns stay "Not stated", never guessed.

The research questions where your work would change the plan most are in **§13**. A first deep-research pass (Gemini, 2026-10-22) has already been checked against primary sources. Read `research/AUDIT_RESPONSE.md` first so you don't redo it.

---

## 1. One-paragraph summary

**STEM PhD Atlas 2027** is a downloadable kit for international, mostly Indian, students applying to PhD programs in **any STEM field** (physics, astronomy, chemistry, materials, maths, statistics, computer science, data science and AI, biology, biomedical sciences, neuroscience, earth and environmental science, and five engineering fields) for 2027 entry. It covers about 200 universities in the **US, the UK, continental Europe, Canada and Australia & NZ**. Other directories don't collect the rules that trip international applicants up, so the Atlas does:
- international fee waivers;
- whether an English-medium Indian degree waives TOEFL or IELTS;
- whether the GRE General or the field's GRE Subject test is required this cycle;
- whether you need a supervisor before admission;
- whether a master's is required first;
- whether funding is guaranteed;
- deadlines.

Every value carries the exact official sentence it came from, the link and the check date. It is sold on **Gumroad** for **$5**. Gumroad's purchasing-power pricing brings that to **about ₹190 in India**, and Indian buyers can pay by **UPI**. A **$20 batch licence** covers up to 30 students. There is a **free 12-program sample** across fields as the lead magnet, and a free copy for any student who can't pay. Alumni abroad can **sponsor a batch** by buying the batch licence at full price.

---

## 2. Status snapshot

| Item | State |
|---|---|
| Dataset | **Schema 2.0, two levels:** a university record holds the graduate-school rules (fee, fee waiver, GRE General, TOEFL and IELTS minimums, English waiver for Indian degrees); a program record per field holds the department's rules (deadline, GRE Subject, supervisor-first, funding, entry route) and any override. The frozen list has 222 universities and 18 fields. One research agent per university writes to `data/staging/`; each university is reviewed and promoted. `python3 scripts/coverage.py` shows live progress. |
| Release gate | ≥180 universities, ≥12 fields, every quote verified, Not stated under 15% overall and under 25% in every field with 30+ programs, explorer tests on desktop and phone, explorer ≤5 MB and loading in under 2 s on a 4× slower CPU, PDFs clean. `python3 scripts/coverage.py --gate`. |
| Verification | A script checks that every quote appears verbatim on the cached official page (0 errors required at both levels). Pages that block automated reads (Oxford, UCL, Michigan) can be saved by the owner in a browser and imported with `scripts/import_saved_page.py`. |
| Product | Offline explorer (HTML), planner workbook (XLSX), CSV, Playbook (PDF), START-HERE (PDF), licence, and a free sample (PDF). Built into a ZIP by `product/build.py`. |
| Tests | 24 automated end-to-end tests: data checks, ZIP contents, PDFs (START-HERE one page, sample ≤3 pages), the explorer in a real browser with the network blocked (the fit engine checked against the written rules for a fixture applicant, My plan, a valid .ics, CSV, persistence, phone layout, load time) and workbook formulas recalculated in LibreOffice. |
| Store | Listing copy, cover images, Gumroad setup steps, emails and policies are written. **The Gumroad account doesn't exist yet** (owner action). Gumroad emails stay locked until the first $100 payout, so the receipt does the welcome (§11). |
| Launch | Messages are drafted for WhatsApp, group posts, alumni sponsors, Reddit (no links, with a pinned profile post) and LinkedIn, all with per-channel tracking links. **Nothing has been sent.** |
| Ops | Weekly checklist, maintenance plan, support playbook, and an owner dashboard workbook with actuals, gates, forecast, expenses and a study-permit hours log. A weekly GitHub Action re-checks every cited page (live on `main`). |
| Repo | `manilaladarsh-hash/YT`, folder `business/phd-atlas/`. Work happens on branch `claude/magical-dirac-6pfq3g` and is merged to `main`. **The repo is still public** (R1). The paid ZIP is no longer tracked in git, but the history still holds v1.1. |
| Revenue | $0. No customers. |

---

## 3. Owner and constraints

- **Owner.** An international student doing a full-time physics PhD at McMaster (Ontario), with an IISER Thiruvananthapuram BS-MS. That background is both the credibility story and the network for the first customers. The listing says "Built by an IISER → McMaster physics PhD student", and the owner can remove that line.
- **Earlier experiments.** The owner's earlier online-business experiments (a mystery-game product, a spectroscopy funding brief, a researcher tool called SpecReply) have **zero sales**. All stalled at "getting the first buyer". This plan is designed around that failure point.
- **Time.** About 3 h one-off setup by the owner, then about 20–30 min/week.
- **Cash.** $0 planned. Hard cap $30 this cycle, and only with approval. No ads.
- **Legal.**
  - Self-employment counts toward the 24 h/week off-campus limit (IRCC) [F]. Thesis-based graduate students usually have no scheduled summer break, so the plan treats the limit as year-round [E; confirm with McMaster ISS].
  - Gumroad is merchant of record and handles sales tax, VAT and GST worldwide [F].
  - **Sell under the owner's full legal name** on Gumroad. "STEM PhD Atlas 2027" is the product title, not a trade name. Under Ontario's Business Names Act, only a name other than your own full name needs registering, and fines run up to $2,000 [F, Ministry form and law-firm guidance].
  - Income goes on the Canadian T2125. GST/HST registration isn't needed below CAD 30,000 a year (small-supplier rule) [F, but the owner should confirm with CRA guidance].

---

## 4. Customer and problem

**Customer.** Self-directed final-year BS-MS, MSc, BSc, BTech or MTech students in any STEM field applying abroad for 2027 entry. The largest groups are computer science, data science, biology and engineering; physics remains the owner's home network. Most are at Indian institutions (IISERs, IITs, IISc, NISER, central and state universities). They are budget-constrained, apply to 8–15 programs, and often first learn the rules from forums.

**Where they apply [D, owner's market knowledge, 2026-10-22]:** "less people apply to Canada. Most people apply for PhD in US, UK, Australia, Europe." The product, sample and copy were rebalanced accordingly. Canadian coverage stays, but stopped growing. (Q1 below asks for data to confirm or refine the split.)

**Market size signals:**
- 177,892 Indian graduate students were in the US in 2024/25 [F, Open Doors].
- **Germany:** about 426,200 international students and doctoral candidates in WS 2025/26. India is now the #1 country of origin, with about 69,000. There were about 50,700 international doctoral candidates in 2024 [F, DAAD, Oct 14 2026]. This supports Europe as the growth segment.
- Field-level counts of Indian PhD applicants aren't established. Gemini's physics estimate (1,100–1,500 Indian applicants a year to the US) is unverified [E]; see Q1.

**Headwind (US).** For fall 2026, more than 60% of PhD-granting US physics and astronomy departments received fewer international applications, 55% made fewer offers to international students, and 41% did both. 16% expect to make fewer international offers for 2027 [F, AIP, Jun 4 2026, 81 departments]. The international doctoral applicant pool fell 21% for 2026-27 [F, AIP].

**Canada, a fact for the playbook, not a pivot:** since Jan 1, 2026, master's and doctoral students at public institutions need no provincial attestation letter, and IRCC targets 2-week study-permit processing for PhD applicants [F, canada.ca].

**Problem.** Each program publishes its rules across 2–4 pages, and the rules international applicants most need are the hardest to find. Getting them wrong costs money (US application fees: median USD 95, about ₹9,000, in this dataset [F, computed]), missed deadlines or rejected files. Real examples from the data [F]:
- GRE Subject tests are still required at a number of US physics, maths and chemistry programs (for example the Physics GRE at Berkeley, Caltech, Stanford and UChicago);
- Alberta's English-exemption list includes the IITs and IISc but not the IISERs;
- Waterloo rejects medium-of-instruction letters;
- UT Austin exempts applicants from India;
- Cambridge, Imperial and Durham don't exempt Indian degrees;
- KTH and Chalmers accept CBSE or CISCE Class XII English grades;
- Sweden admits only funded PhD students;
- Copenhagen introduces PhD tuition of DKK 85,000 a year from 2027.

---

## 5. Product

| Component | What it does |
|---|---|
| `Atlas.html` | Offline single-file explorer (gzip-embedded data). **Your situation:** fields, regions, degree, GRE Subject and General plans, English route or scores, fee budget, funding need, supervisor preference. A **fit engine** marks each program Strong match / Check first / Obstacle and names the reasons; best fit sorts first. Results are cards (or a table on desktop), with fees in ₹ and deadline countdowns; tap any value to read the official quote, marked university-wide or department. **My plan:** starred programs' deadlines in date order, total fees in ₹ net of waivers, an auto-generated checklist per program, and export to calendar (.ics with a 7-day reminder), CSV and print. Light/dark theme, phone-first. |
| `Atlas.xlsx` | Planner workbook. The **Shortlist** sheet auto-fills from a drop-down. There is a deadline countdown, a **Budget** sheet converting all fees to rupees (with an editable rate pre-filled from the Bank of Canada), a recommender tracker, a supervisor-outreach log with automatic follow-up dates, and a Sources sheet with every quote. |
| `Playbook.pdf` | About 13 pages. Facts are computed from the data at build time (field-by-field admission table, GRE by field, English rules, deadlines grouped by university). It covers:<br>• late-season timeline and deadline calendar;<br>• budgeting in rupees;<br>• English tests (including TOEFL's January 2026 scale change);<br>• the GRE and GRE Subject tests by field;<br>• how each field admits PhD students (physical, mathematical, computing, life, earth and engineering sciences);<br>• the UK (funding deadlines, English rules for Indian degrees);<br>• **how the rest of Europe differs** (positions versus calls, fees, master's-first rules, funding as a job, English rules), plus **Max Planck Schools, MSCA Doctoral Networks and APS**;<br>• Australia and NZ (supervisor first);<br>• Canada (supervisor-first rules and the 2026 study-permit changes);<br>• a 6-sentence supervisor email;<br>• an SOP framework (outline only, no ghost-writing);<br>• a letter-request kit;<br>• ethical fee-waiver requests;<br>• a checklist;<br>• scam warnings. |
| `START-HERE.pdf`, `LICENSE.txt` | Quick start, and the personal or batch licence terms. |
| Free sample PDF | 3 pages: 12 program cards across fields and regions, chosen from the best-documented records, plus data-driven "What applicants miss", the price line and the free-copy offer. |
| Updates | Free for the 2027 cycle. The owner replaces the ZIP, and each buyer's receipt link and Gumroad Library serve the new file. No email is needed, which matters while Gumroad's email lock applies. |

**Data method.** Program pages are fetched (plain HTTP, falling back to headless Chromium) and cached. Values are extracted with exact quotes. `scripts/validate_data.py` checks every quote appears on its cached page. `scripts/check_sources.py` runs weekly through GitHub Actions and opens an issue when a cited quote disappears.

The schema has two levels. A university record holds what the graduate school sets once (fee, fee waiver, GRE General, TOEFL, IELTS, English waiver for Indian degrees). A program record holds what each department decides (deadline, GRE Subject, supervisor rule, funding, entry route) plus any department override, which wins. Every value has a code, a plain-English value, a quote and a URL, plus optional flags: year inferred, time-sensitive, scope, and sources-conflict.

**Out of scope:** visa or immigration advice (official links only), SOP writing or editing, and admission predictions.

---

## 6. Differentiation and competition

| Alternative | What it lacks |
|---|---|
| AIP GradSchoolShopper (free) [F] | Department-supplied profiles. No international fee-waiver, India English-waiver or supervisor-first fields; US-centric. |
| Reddit, GradCafe, Telegram and WhatsApp groups (free) | Unverified, scattered and often out of date. |
| Generic Gumroad PhD kits ($1–£39.99) [F] | Generic advice, with no verified program data. |
| SOP reviews and consultants ($50–200 on Fiverr) [F]; Indian study-abroad counsellors [E: pricing not yet researched] | Expensive. Different job (personal service). |

**Moat (modest):** primary-source verification with a quote for every value, fields built for international applicants, honest "Not stated" labels, an India-first price, and the founder's own story. Weakness: the data is public information, so anyone willing to spend the hours could reproduce it.

---

## 7. Pricing and payments [D, 2026-10-21]

| Version | List price | India (Gumroad PPP) | Notes |
|---|---|---|---|
| Personal licence | **$5** | **≈ $2, about ₹190** [E] | Gumroad charges in INR for eligible card purchases, and accepts UPI from buyers in India [F] |
| Batch licence (up to 30 students) | **$20** | **≈ $8, about ₹750** [E] | About ₹25 per student; for a batch, society, mentor, or an **alumnus abroad sponsoring a batch** (who pays full price) |
| Free sample | $0 | $0 | Lead magnet |
| Free copy on request | $0 | $0 | Code `STUDENTAID`, 20 uses at a time, never posted publicly |
| Tips | optional | optional | Gumroad tipping on; the default tip is 0% [F] |

**Facts behind it [F, Gumroad help, checked 2026-10-21]:**
- Fees are 10% + $0.50 per sale, plus card processing of 2.9% + $0.30. Discover marketplace sales cost a flat 30%.
- On a refund, Gumroad returns its own fee and keeps only the processing fee.
- PPP discounts run from 20% to 60% based on World Bank data. Creators can cap them. If the buyer fails the location check, they pay full price.
- PWYW minimum is $0.99 if they pay.
- Payout minimum is $100; the first payout review typically needs 3–4 sales and a balance over $100.
- Gumroad's help says PPP and discount codes don't stack, and the larger discount applies [F as reported in its help, not re-verified]. So channel attribution uses **UTM links**, not codes [D].

**Price math:**
- **[F, computed]** A $2 sale nets about **$0.94**. A $5 sale nets about **$3.56**. A ₹99 sale would net about $0.11, so about ₹190 is near the practical floor on Gumroad.
- **[F, computed]** A $20 batch licence bought abroad nets **$16.62**, as much as about 17.7 Indian personal sales. Bought from India at PPP ($8), it nets about $6.17. That's why the alumni sponsor-a-batch channel (E5) matters.
- **[F] Email lock.** Gumroad: "You cannot send emails until you've earned $100 after fees and received a payout." This covers Workflows and update emails. At these prices, that's roughly 30–100 sales away.
- **[D] Payments fallback.** Topmate as a second, India-only store is a last resort, used only if the India checkout test fails, and only after Topmate confirms in writing that it handles India GST for non-resident sellers. Never use an Indian gateway into an Indian bank account (NRI/FEMA).
- **[E]** India's PPP factor (about 22 INR per international dollar) is far below the market rate (94.5 INR per USD, Bank of Canada, Oct 21, 2026) [F]. So India should get Gumroad's full 60% discount. This is **untested until the owner's account exists.** A friend in India should check the rupee price and UPI option before launch.

---

## 8. Go-to-market and launch plan

**Timing is critical:**
- US deadlines cluster on Dec 1–15 and Canada's on Jan 7–15. Europe's first wave closes Nov 1–3, and the Max Planck Schools close Dec 1 [F, dataset].
- Each week of delay loses part of this season. Launch is **paused until the release gate passes** (≥180 universities, Not stated <15%), and that trades December-deadline buyers for a much fuller kit. Additions after launch ship as free updates. The rest of the value is the **next cycle** (Aug 2027–Jan 2028) [E].

| # | Experiment | Who acts | Cost | Measure |
|---|---|---|---|---|
| E1 | About 10 personal WhatsApp messages to applicants and mentors the owner knows (IISER batchmates, juniors) | Owner sends | $0 | UTM `whatsapp` orders and downloads |
| E2 | 1–3 alumni or student group posts, where allowed, pushing the batch licence | Owner posts | $0 | UTM `group` |
| E3 | Value-first Reddit post **with no links**, pointing to a pinned profile post that holds the links (r/gradadmissions, r/Indians_StudyAbroad, r/Indian_Academia, **only where the rules allow**) | Owner posts | $0 | UTM `reddit_profile` |
| E4 | LinkedIn post | Owner posts | $0 | UTM `linkedin` |
| E5 | **Alumni sponsor-a-batch:** about 5 IISER, NISER and IIT alumni abroad buy a $20 batch licence for their old department | Owner sends | $0 | UTM `alumni`; batch licences |
| E6 | (Optional) free copies to 5–10 science, computing or engineering club or batch coordinators, with no review obligation | Owner sends | $0 | UTM `club`; code `CLUBCOPY` |
| E7 | Gumroad Discover (passive) | Automatic | 30% fee on those sales | "Recommended by Gumroad" sales |

All message drafts are in `launch/messages/`, with the `{PAID_URL}` and `{SAMPLE_URL}` placeholders to fill. The honesty rules: disclose that you made it, no fake urgency, no testimonials until real ones exist, and respect each group's no-promotion rules.

---

## 9. Financial model (`research/financials.py`, all assumptions except the fees) [E]

| Scenario | This season: orders → net | Next season: orders → net | Assumptions |
|---|---|---|---|
| Conservative | 10 → **$13** | 50 → **$65** | 80% pay the India/PPP price, 8% refunds |
| Base | 40 → **$59** | 200 → **$296** | 75% PPP, 5% refunds, 5% via Discover |
| Optimistic | 120 → **$196** | 600 → **$981** | 70% PPP, 4% refunds, 10% via Discover |

Batch licences aren't modelled. Each adds $6.17 (India) to $16.62 (abroad) net. Fixed costs are $0.

**Plain reading:** at student-friendly prices this is a **small, mission-first business**, with base case well under $500 a season. The upside depends on **reach** (batch licences through student societies, future editions, other subjects), not on price.

---

## 10. Validation plan and decision gates (`research/VALIDATION_PLAN.md`)

**Riskiest assumptions:**
1. Students will pay about ₹190 when free sources exist.
2. A no-audience founder can reach them late in the season.
3. Checkout works from India (rupee pricing, UPI).
4. The data stays accurate cheaply.
5. The kit changes real decisions.
6. Selling is allowed under the owner's study permit.

**Dec 15, 2026 gate (hard stop Jan 15, 2027):**
- **Proceed** if all of these hold:
  - ≥10 paid orders;
  - ≥2 retained purchases from buyers unrelated to the owner;
  - refunds ≤10%;
  - ≥2 buyers report a concrete benefit;
  - 0 critical data errors.
- **Change** the channel or offer for one more 3-week cycle if there are ≥50 sample downloads or ≥500 views but <5 orders, or if sales come only from the owner's network.
- **Stop** (leave it listed passively, build nothing more) if, after both channels run, there are <20 downloads and 0 unrelated orders.

These don't count as validation: views, likes, compliments, friends buying to be supportive, passing tests, or the number of programs.

---

## 11. Operations

- **Weekly (about 20–30 min):**
  - copy Gumroad numbers and per-UTM orders into the dashboard, including orders from India and batch licences;
  - answer email (refunds: approve them; free-copy requests: send the template);
  - review the source-watch issue;
  - log hours.
- **Monthly in season:** a data refresh session. It re-fetches every source, updates values with new quotes, re-validates, rebuilds and uploads the new version. Buyers get the update through their existing link.
- **Automated:** checkout, tax, delivery, receipts (which carry the welcome and the one feedback question), source-change detection and gate calculations. The day-10 survey and sample follow-up workflows are drafted in `store/EMAILS.md`, and the owner switches them on after the first payout lifts Gumroad's email lock.
- **Needs judgement:** edge-case refunds, whether a flagged page change matters, the posts themselves, and the Dec 15 decision.

---

## 12. Risks and known issues (most serious first)

| # | Risk | Impact | Current mitigation / recommendation |
|---|---|---|---|
| R1 | **The repo is public** (checked 2026-10-22). The paid ZIP is no longer tracked, but git history holds v1.1, and the data and build scripts are there. | Anyone can get the product free, which undercuts every sale and exposes the owner's details. | **Make the repo private before launch** (GitHub → Settings → Change visibility; one minute, owner only). GitHub Free still runs the weekly Actions job on private repos. |
| R2 | Late season, made later by the overhaul | Fewer buyers before the December US deadlines | Research runs continuously toward the gate; Europe, UK and Canada deadlines run into January–August; position as a next-cycle product too |
| R3 | Shrinking international applicant pool (−21%) [F] | Smaller market | India-first pricing; Europe coverage (less exposed to US policy) |
| R4 | PPP and UPI behaviour untested | Indian buyers might see a higher price or no UPI | A friend in India checks before launch; fallbacks in `store/GUMROAD_SETUP.md` (card/PayPal note, free copy, Topmate only after GST confirmation) |
| R4b | **Gumroad email lock** until the first $100 payout [F] | No automated welcome, survey or update emails at launch | Receipt text does the welcome and feedback ask; updates via the same download link; workflows switched on after the first payout |
| R4c | Reddit removes promotional links | Posts removed, or the account restricted | Zero-link post plus a pinned profile post; read the rules or ask the mods first |
| R5 | Data decay mid-cycle | Wrong advice and refunds | Weekly automated quote check, monthly refresh, "confirm on the official page" everywhere |
| R6 | Coverage gaps. Some department pages block automated fetching (403, Cloudflare) or are PDF-only; those values stay Not stated | Buyers may want these | Each research agent lists blocked URLs; the owner can save key pages in a browser for `import_saved_page.py`; `scripts/coverage.py` tracks the gaps |
| R7 | Gumroad dependence and the $100 payout threshold | Slow first payout at about $1 per sale | Accept, or research alternatives (Q5) |
| R8 | Study-permit and tax compliance | Legal risk to the owner | Hours log; owner checks permit conditions first |
| R9 | Low revenue for the effort | Owner may lose interest | Gate rules stop investment early if demand isn't there |

---

## 13. Deep-research brief: questions that would change the plan

Please research these, cite primary sources, and say what you would change.

1. **Market size and destination split.** Roughly how many students from India apply to STEM PhD programs abroad each cycle, by field (CS, data science, biology, engineering, physics, chemistry, maths), and how do they split across the US, UK, Germany and the rest of Europe, Australia and Canada? This would test the owner's view that Canada is a minor destination. Possible sources: AIP, NSF NCSES (SED and GSS data), Open Doors by field, UK HESA, Australian DESE data, DAAD, IRCC study-permit data.
2. **Where these students actually gather in 2026.** Telegram and WhatsApp communities, Discord servers, IISER/IIT/NISER/IISc science, computing and engineering clubs, YouTube or Instagram creators covering "PhD abroad", r/Indian_Academia's rules, and Indian subject societies. Which allow posts, and who are the gatekeepers?
3. **Price benchmarks in India** for comparable digital study products (Topmate, Gumroad, Instamojo, Notion-template sellers; study-abroad counsellors such as Yocket or Leverage Edu and what they charge). Is about ₹190 right, too high or too low? Would pay-what-you-want with a ₹99–₹149 floor raise total reach without breaking Gumroad's fixed fees?
4. **Distribution leverage.** Would an affiliate programme (Gumroad affiliates), student-society batch deals, or free institutional licences to IISER/IIT career cells grow reach more than direct posts? What commission would student creators accept?
5. **Payment platform.** Is Gumroad still the best choice for a Canada-resident seller selling mainly to India? Compare Lemon Squeezy, Payhip, Paddle and Indian platforms (Topmate, Razorpay Payment Pages, Instamojo). Cover fees at a ₹190 price, UPI support, merchant-of-record status, payout to a Canadian bank, and FEMA or tax implications if the owner used an Indian account.
6. **Competition check.** Is there any international-applicant, source-cited STEM PhD dataset (free or paid) that we missed? Check Indian edtech, PhD-abroad newsletters and university-run resources.
*Status after the Gemini pass (2026-10-22, details in `research/AUDIT_RESPONSE.md`):*
- *Q1 is partly answered: AIP and DAAD figures verified, regional applicant counts still [E].*
- *Q3 confirmed ₹190, and PWYW at ₹99–149 was rejected on fee math.*
- *Q4 recommended alumni sponsorship, which was adopted.*
- *Q5: keep Gumroad, with Topmate as a guarded fallback.*
- *Q7: Max Planck Schools and MSCA were added; Asia is deferred.*
- *Q9: sell under the legal name, and the 24 h/week cap applies all year.*

*Still open: Q2 (current community rules, which need a human Reddit or Telegram account), Q6 and Q8.*

7. **Product priorities.** For Indian STEM applicants, which missing programs or fields matter most? Candidates:
   - Asia: OIST, NUS, NTU, HKUST, KAIST;
   - MIT, Oxford and the other blocked sites;
   - stipend amounts in rupee terms;
   - BS-MS recognition as a master's;
   - interview formats;
   - fellowship deadlines (e.g., DAAD, Max Planck, Marie Skłodowska-Curie doctoral networks).
8. **Business model alternatives.** Free Atlas with paid extras? A sponsorship or donation model? An annual edition, or field-specific editions sold alongside the full kit? Which keeps the owner's time ≤3 h/week and stays affordable?
9. **Legal check.** Do IRCC rules or the owner's study-permit conditions add constraints on selling a digital product to customers outside Canada? Any Ontario registration needed when selling under one's legal name?

**Please don't change:** the verification standard (quote-backed values only), the ban on invented social proof, the affordability requirement, and the owner-approval rule for anything sent from the owner's accounts.

---

## 14. Decision log

| Date | Decision | Why | Alternatives rejected |
|---|---|---|---|
| 2026-10-21 | Build a physics-PhD application kit for international (Indian) applicants | Reachable through the owner's network, buildable without owner content work, low cost | TPT physics mystery games had the best demand evidence, but TPT announced a ban on AI-generated content on Oct 8, 2026 [F], so the owner would have had to write everything; also an AP Physics KDP workbook (crowded), a homeschool course (heavy), a teacher SaaS (slow) |
| 2026-10-21 | Gumroad as merchant of record | Handles tax and VAT, PPP, UPI, emails and updates; no monthly fee | Payhip, Lemon Squeezy (not deeply compared, see Q5) |
| 2026-10-21 | Push the repo publicly | Owner's choice after being warned | Private repo (recommended again, R1) |
| 2026-10-21 | Add Europe | Owner request | — |
| 2026-10-21 | **$5 list, PPP up to 60% (about ₹190 India), $20 batch licence, free copies on request, tips on** | Owner: "$10 is a lot for them"; Gumroad's fixed fees set a floor of about $2 | $15 list (the original plan, about $7.50 in India), ₹99 (nets about $0.11) |
| 2026-10-21 | UTM links instead of discount codes | PPP and codes don't stack on Gumroad | Discount codes NETWORK and REDDIT (the original plan) |
| 2026-10-21 | Exclude records that are too thin (Manchester, IFAE) and keep them in `data/pending/` | Quality over count | Shipping records with 3 of 10 fields known |
| 2026-10-22 | **Overhaul into the STEM PhD Atlas: every STEM field, about 200 universities, one kit at $5 (about ₹190), $20 batch** | Owner tested v1.2 and asked for a full overhaul and all STEM fields; CS, data science and biology are far larger applicant groups than physics | Physics-only launch; separate kits per field; a higher price for the bigger kit |
| 2026-10-22 | Two-level data and one research agent per university | ~2,800 department entries are only feasible if graduate-school rules are verified once per university | One agent per program (too slow, inconsistent university rules) |
| 2026-10-24 | Don't ship program records whose every field is Not stated; separate schools (engineering, medicine) get their own overrides | An empty card or a graduate-school rule shown for an engineering school would mislead | Inheriting the graduate-school rule silently |
| 2026-10-22 | **Act on the Gemini audit:**<br>• launch v1.2 now, with UK/AU as v1.3;<br>• design around Gumroad's email lock;<br>• add the alumni sponsor-a-batch channel;<br>• make the Reddit post link-free;<br>• keep Topmate as a fallback only;<br>• sell under the legal name;<br>• add Max Planck Schools and MSCA;<br>• fix the AIP figures;<br>• stop tracking the paid ZIP in git | Checked against primary sources (`research/AUDIT_RESPONSE.md`) | A dual Gumroad + Topmate checkout (GST uncertainty, double ops); a 3-email funnel (blocked by Gumroad); a 15-program sample; Asia now |
| 2026-10-22 | **Reposition to the US, UK, Europe and Australia; Canada secondary.** Stop adding Canadian programs; add about 20 UK and about 10 Australian/NZ programs; restructure the Playbook (UK §6, rest of Europe §7, Australia & NZ §8, Canada §9); rebalance the sample to 4 US, 2 UK, 2 Europe, 1 Australia and 1 Canada | Owner: most Indian applicants target the US, UK, Australia and Europe | Equal weight on Canada (the original plan, which followed the owner's own route to Canada) |

---

## 15. File map (`business/phd-atlas/`)

| Path | What |
|---|---|
| `README.md` | Operator README with the owner's remaining actions |
| `BUSINESS_PLAN_README.md` | This file |
| `research/OPPORTUNITY_RESEARCH.md` | The five-option comparison, with sources |
| `research/AUDIT_RESPONSE.md` | Claim-by-claim check of the Gemini deep-research audit |
| `research/VALIDATION_PLAN.md`, `research/BUSINESS_DESIGN.md`, `research/financials.py` | Gates, design, scenario model |
| `data/programs/*.json` | One verified record per program |
| `data/pending/` | Incomplete records |
| `data/staging/` | Draft records from research sessions, waiting for review (not built) |
| `data/schema.json`, `data/fx.json`, `data/source_manifest.json` | Schema, exchange rates, sources |
| `scripts/` | `research.py` (fetch and extract), `validate_data.py`, `check_sources.py`, `fx.py`, `rec.py`, `import_saved_page.py` (pages saved by hand) |
| `product/` | `build.py`, the explorer template, playbook and START-HERE content |
| `dist/` | Built deliverables. Only the free sample PDF is tracked in git. The paid ZIP is rebuilt locally and sent to the owner in chat |
| `store/` | Listing copy, Gumroad setup, emails, policies, images |
| `launch/` | Launch plan, message drafts, experiment log |
| `ops/` | Weekly checklist, maintenance, expenses, support playbook, `Business-Dashboard.xlsx` |
| `tests/` | End-to-end tests |

Rebuild: `python3 scripts/validate_data.py && python3 product/build.py && python3 -m pytest -q tests`

---

## 16. Verified facts used in this plan (sources)

| Fact | Source (checked) |
|---|---|
| Self-employed students track their own off-campus hours; 24 h/week during terms | [IRCC: work off campus](https://www.canada.ca/en/immigration-refugees-citizenship/services/study-canada/work/work-off-campus.html) (2026-10-21) |
| TPT announced a generative-AI content ban on Oct 8, 2026 | [Chalkbeat, 2026-10-15](https://www.chalkbeat.org/2026/10/15/teachers-pay-teachers-to-ban-ai-generated-teaching-resources/) |
| 177,892 Indian graduate students in the US, 2024/25 | [Open Doors India fact sheet](https://opendoorsdata.org/wp-content/uploads/2026/01/OD_India_Fact-Sheet-2025.pdf) |
| Fall 2026: >60% of 81 PhD-granting physics/astronomy departments got fewer international applications, 55% made fewer offers, 41% both; 16% expect fewer international offers for 2027 | [AIP, Jun 4 2026](https://www.aip.org/statistics/federal-funding-and-visa-uncertainty-shape-fall-2026-graduate-admissions-in-physics-and-astronomy) (2026-10-22) |
| Germany: about 426,200 international students and doctoral candidates (WS 2025/26); India #1 with about 69,000; about 50,700 international doctoral candidates (2024) | [DAAD, Oct 14 2026](https://www.daad.de/en/press-releases/2026/germany-remains-a-sought-after-destination-worldwide-for-undergraduate-and-postgraduate-study/) (2026-10-22) |
| Canada: no PAL/TAL for master's/doctoral students at public institutions from Jan 1, 2026; about 2-week processing for PhD applicants applying online from outside Canada | [canada.ca: graduate students](https://www.canada.ca/en/immigration-refugees-citizenship/services/study-canada/graduate-student/how-to-apply.html), [faster processing](https://www.canada.ca/en/immigration-refugees-citizenship/services/study-canada/graduate-student/faster-processing.html) (2026-10-22) |
| Gumroad: no emails (Workflows or updates) until $100 earned after fees and a payout | [Gumroad: Workflows](https://gumroad.com/help/article/131-using-workflows-to-send-automated-updates), [email updates](https://gumroad.com/help/article/169-how-to-send-an-update) (2026-10-22) |
| MSCA Doctoral Networks: any nationality, no doctorate at recruitment, 12-in-36-months mobility rule | [EC: Doctoral Networks](https://marie-sklodowska-curie-actions.ec.europa.eu/actions/doctoral-networks) (2026-10-22) |
| Max Planck Schools: apply Sep 1–Dec 1, bachelor's and master's graduates, full funding up to 5 years | [maxplanckschools.org](https://www.maxplanckschools.org/en/application) (2026-10-22) |
| GradSchoolShopper's scope | [AIP Observer](https://students.aip.org/observer/grad-school-shopper-com-simplifies-the-grad-school-search) |
| SOP reviews $50–200; generic PhD kits $1–£39.99 | [Fiverr example](https://fiverr.com/phd_po_editor/revise-phd-application-materials-personal-statement-cv), [phdtoprof](https://phdtoprof.gumroad.com/l/phd-application), [skatergrandpa](https://skatergrandpa.gumroad.com/l/pzdlf) |
| Gumroad 10% + $0.50; Discover 30% | [Gumroad pricing](https://gumroad.com/pricing) (2026-10-21) |
| Card processing 2.9% + $0.30 on top; refund fee rules | [Gumroad: fees](https://gumroad.com/help/article/66-gumroads-fees) (2026-10-21) |
| PPP 20–60%, World Bank data, cap available, location check | [Gumroad: PPP](https://gumroad.com/help/article/327-purchasing-power-parity) (2026-10-21) |
| UPI accepted for buyers in India; $100 payout minimum; first payout review | [Gumroad: getting paid](https://gumroad.com/help/article/13-getting-paid) (2026-10-21) |
| INR among checkout currencies for eligible card purchases | [Gumroad: currency](https://gumroad.com/help/article/46-what-currency-does-gumroad-use) (2026-10-21) |
| PWYW minimum $0.99 | [Gumroad: pay what you want](https://gumroad.com/help/article/133-pay-what-you-want-pricing) (2026-10-21) |
| UTM links feature; tipping default 0% | [Gumroad announcement, Jan 30, 2025](https://gumroad.gumroad.com/p/paypal-is-back-on-gumroad-utm-links) |
| USD 1 = 94.47 INR (and CAD cross rates) on 2026-10-21 | [Bank of Canada daily rates](https://www.bankofcanada.ca/rates/exchange/daily-exchange-rates/) (Valet API, saved in `data/fx.json`) |
| Cards issued in India since Mar 2020 have international online use off by default | RBI circular RBI/2019-20/142 (Jan 2020), as reported by banks' FAQs (e.g., [HDFC](https://www.hdfc.bank.in/credit-cards/enhanced-security-for-card-transactions)); not re-read from RBI directly |
| All program facts (deadlines, fees, waivers, GRE, English, supervisor, funding, entry) | Per value in `data/programs/*.json`, each with the exact quote, URL and check date |
