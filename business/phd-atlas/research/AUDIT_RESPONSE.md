# Response to the Gemini deep-research audit (2026-10-22)

The owner shared "Strategic Audit and Deep-Research Revision of the Physics PhD Atlas 2027 Business Plan", produced with Gemini deep research. It was based on an earlier copy of `BUSINESS_PLAN_README.md` (74 programs; we now have 106). I checked its main claims against primary sources on 2026-10-22 and changed the plan where the evidence held up. Labels: **[F]** verified here, **[E]** estimate, **[D]** decision.

## Headline

1. **Right:** don't hold the launch for more data. v1.2 (106 programs) is launch-ready now. UK/Australia additions ship as a free v1.3 around Nov 5.
2. **Missed by both Gemini and our earlier plan:** Gumroad sends **no emails** until the seller has earned $100 after fees and received a payout [F]. That rules out automated welcome or survey workflows and "updates emailed to you" at launch, and it rules out Gemini's proposed 3-email funnel too. The kit now relies on the receipt (sent automatically) and on the download link, which always serves the newest file.
3. **Over-reach:** a second "India UPI" store on Topmate. It adds tax uncertainty (India's GST rules for non-resident sellers) and double the setup, for a problem that isn't yet shown to exist. It is now a documented fallback, only used if the friend-in-India checkout test fails.

## Claim by claim

### Claims checked against primary sources

| Gemini claim | Check | Result | Change made |
|---|---|---|---|
| Launch delayed to add UK/AU programs | Our README made it look that way; nothing actually blocked launch | Agree | Launch-ready status everywhere; v1.3 for additions; agents write to `data/staging/` so builds never pick up unreviewed records |
| AIP: >60% of departments got fewer international applications, 55% made fewer offers, 41% both | [AIP, Jun 4 2026](https://www.aip.org/statistics/federal-funding-and-visa-uncertainty-shape-fall-2026-graduate-admissions-in-physics-and-astronomy) (81 PhD-granting departments) | **Confirmed** [F]. Also: 16% expect fewer international offers for 2027 | Fixed our misquote ("41% fewer applicants") in the plan and research docs |
| Germany: 426,200 international students and doctoral candidates; India #1 with 69,000; 50,700 international doctoral candidates | [DAAD press release, Oct 14 2026](https://www.daad.de/en/press-releases/2026/germany-remains-a-sought-after-destination-worldwide-for-undergraduate-and-postgraduate-study/) | **Confirmed** [F] (the doctoral figure is for 2024) | Added to the plan §4 |
| Canada: from Jan 1 2026, PhD and master's students need no PAL; 14-day PhD processing | [canada.ca, graduate students](https://www.canada.ca/en/immigration-refugees-citizenship/services/study-canada/graduate-student/how-to-apply.html); [faster processing](https://www.canada.ca/en/immigration-refugees-citizenship/services/study-canada/graduate-student/faster-processing.html) | **Confirmed** [F]. The no-PAL rule covers public institutions only. The 2-week target counts from when the school verifies the acceptance letter, and needs an online application from outside Canada | Playbook §9 now states both, as facts with links. Canada stays secondary |
| Max Planck Schools: Sep 1–Dec 1 window, bachelor's welcome, full funding up to 5 years | [maxplanckschools.org](https://www.maxplanckschools.org/en/application) plus each school's application and FAQ pages | **Confirmed** [F] | Two new records (Photonics, Matter to Life) and a Playbook §7 paragraph |
| FAU Erlangen charges non-EU applicants €100 | [MPS Photonics FAQ](https://photonics.maxplanckschools.org/faq) | **Confirmed** [F] | Playbook §7 fee note |
| APS certificate needed by Indian applicants to Germany | aps-india.de was down (503); the [Matter to Life FAQ](https://mattertolife.maxplanckschools.org/faq) requires APS for Indian certificates | Partly confirmed | A hedged Playbook line: check each program and aps-india.de |
| MSCA Doctoral Networks: any nationality; 12-of-36-months mobility rule | [EC MSCA Doctoral Networks page](https://marie-sklodowska-curie-actions.ec.europa.eu/actions/doctoral-networks) | **Confirmed** [F] | New Playbook §7 subsection, with a EURAXESS search tip |
| Repo is public and exposes the paid kit | GitHub API, 2026-10-22: public | **Confirmed** [F] | The paid ZIP and kit folder are no longer tracked in git. **The owner still needs to make the repo private**, because the git history keeps v1.1 |
| Flagships blocked: MIT, Oxford, UCL, Michigan, ISTA… | MIT is already in the Atlas. Oxford, UCL and Michigan still return 403 (Cloudflare) to me; ISTA now loads | Partly outdated | New `scripts/import_saved_page.py`: the owner saves a page in a normal browser, uploads it, and it's quote-checked like any other |
| Add `skip_live_fetch` so the weekly job doesn't open false issues | `check_sources.py` already lists unreachable pages separately and only opens issues for changed quotes | **Not needed** | None |

### Ideas adopted

| Gemini claim | Check | Result | Change made |
|---|---|---|---|
| Alumni "sponsor a batch": $20 at full price nets $16.62 | `research/financials.py` | **Confirmed math** [F, computed]: 17.7× one ₹190 sale | New `launch/messages/alumni_sponsor.md` (E5); listing line; licence now says the buyer needn't be in the group |
| Free copies for physics club coordinators | — | Sensible, $0 | Optional E6 with a `CLUBCOPY` code (10 uses), no review obligation |
| Ontario: trade under your exact legal name to avoid registration | Ministry form and law-firm guidance: only a name other than your full legal name needs registering; fines up to $2,000 | Confirmed (secondary sources) | Gumroad setup now says: Gumroad name = full legal name; "Physics PhD Atlas 2027" is only the product title |
| 24 h/week applies all year for PhD students | Plausible: thesis-based grad students usually have no scheduled break | [E] | Ops rule: treat 24 h/week as year-round; confirm with McMaster ISS |
| Cold-email rules | A Reddit anecdote | Two rules are sound | Playbook §10: no call request in the first email; no quiz-style questions. CV and transcript were already attached |

### Claims modified, deferred or rejected

| Gemini claim | Check | Result | Change made |
|---|---|---|---|
| Gumroad UPI is "erratic" | Sources are competitor and SEO blogs; Gumroad's help says UPI is offered to Indian buyers | Unproven | Keep the friend-in-India checkout test as the launch gate, and add fallbacks to the setup guide |
| Topmate as an "India UPI Express" mirror | Topmate's pages say creators outside India withdraw by PayPal or to a US bank. A non-resident selling digital services to Indian consumers generally must register for Indian GST (no threshold) unless the platform is the deemed supplier, and Topmate's role isn't confirmed. Two stores split updates and licences | **Modified** [D] | Fallback only, after Topmate confirms GST handling in writing. Never use an Indian gateway into an Indian bank account (NRI/FEMA; ask a CA) |
| Reddit: links get posts removed; use a pinned profile post | I can't read Reddit rules (blocked). Gemini's citations are weak (an r/beauty rules page, an unrelated thread). The conservative approach is still right | Adopted on caution | `reddit_post.md` has no links; new `reddit_profile_post.md` (UTM `reddit_profile`); read the rules or ask the mods first |
| A 3-email Gumroad funnel for sample downloaders | Gumroad's email lock (above) | **Not possible at launch** [F] | The sample's receipt text carries the upsell. The workflow is drafted for after the first payout |
| Gate the sample behind a $0 Gumroad checkout | Already the plan | — | None |
| Expand the sample to 15 programs | No evidence it converts better | Rejected | None |
| Asia (OIST, NUS, NTU, HKUST) | Gemini itself defers it | Deferred | Backlog for v1.4 or the next season |
| Applicant counts by region (e.g. US 1,100–1,500/yr) | Gemini's own estimates, not reproducible | [E], unverified | Noted in §13; not used in any marketing |
| UK PGR +11%; Australia 16% Indian share | Secondary sources only | Unverified | Not used |
| DHS "duration of status" rule | Visa policy; out of scope | — | None (the kit gives no visa advice) |

## What the owner needs to do (unchanged, short)
1. Make the repo private (1 minute).
2. Set up Gumroad under your full legal name (about 45 min, steps in `store/GUMROAD_SETUP.md`).
3. Ask a friend in India to check the ₹190 price and UPI.
4. Optionally, save the Oxford DPhil Physics, UCL Physics PhD and Michigan Physics admissions pages in a normal browser (Ctrl+S, "HTML only") and upload them in chat.
