# Launch plan: first paying customers

**Goal:** 10 paid orders, including ≥2 from buyers you don't know, within 6 weeks of launch (and by Jan 15, 2027 at the latest). Budget: **$0** (hard cap $30, only with your approval). No ads.

**Launch day (L) is the day the release gate passes** (≥180 universities, ≥12 fields, Not stated under 15%; `python3 scripts/coverage.py --gate`). Nothing is sold or posted before then. Universities added after launch ship as free updates through the same download link, and give you a second, honest reason to post.

You've given me authority to decide, but the messages have to go out from your own accounts, which I can't access. Every message is drafted in `launch/messages/`, with links tagged by channel: `utm_source=whatsapp`, `group`, `reddit_profile`, `linkedin`, `alumni`, `club` and `sample`. Replace `{PAID_URL}` and `{SAMPLE_URL}` after Gumroad setup, and keep the `?utm_...` endings.

**Price:** $5 personal / $20 batch licence. India sees about ₹190 / ₹750 through Gumroad's regional pricing, and can pay by UPI. Students who can't pay get a free copy on request (code `STUDENTAID`, 20 uses).

## Experiments

| # | Experiment | Audience | Action (who) | Cost | Your time | Success by | Measure |
|---|---|---|---|---|---|---|---|
| E1 | Personal messages | ~10 people you know who are applying this cycle, or who mentor juniors (IISER batchmates, lab juniors, TAs) | You send `whatsapp_personal.md` one by one | $0 | 20 min | L+14 | Orders and downloads from `utm_source=whatsapp` links (Gumroad UTM dashboard); replies |
| E2 | Group posts | 1–3 alumni/student groups where you're a member and posts like this are allowed | You post `group_post.md` once per group | $0 | 10 min | L+14 | Sample downloads and orders from `utm_source=group` links |
| E3 | Reddit, zero-link | r/gradadmissions, r/Indians_StudyAbroad, r/Indian_Academia, **only where the rules allow** | First pin `reddit_profile_post.md` on your profile. Then post `reddit_post.md`, which has **no links**, and answer comments for 2 days | $0 | 15 min + 20 min replies | L+21 | Orders and sample downloads from `utm_source=reddit_profile` links |
| E4 | LinkedIn post | Your network | You post `linkedin_post.md` | $0 | 5 min | L+21 | Sample downloads from `utm_source=linkedin` links |
| E5 | Alumni sponsor-a-batch | 5 IISER/NISER/IIT alumni now doing PhDs or postdocs abroad, whom you know | You send `alumni_sponsor.md` one by one | $0 | 15 min | L+21 | Batch licences from `utm_source=alumni`. Each nets about $16.62 (≈17 Indian personal sales) |
| E6 | Club coordinators (optional) | Student-society or final-year batch coordinators at 5–10 IISERs/NISER/IITs | Send `whatsapp_personal.md` adapted with the CLUBCOPY free copy (template in `store/EMAILS.md`) | $0 | 15 min | L+28 | Batch licences or sample downloads from `utm_source=club` |
| E7 | Passive marketplace | Gumroad Discover | Enable Discover listing | $0 (30% fee on those sales) | 0 | L+6 weeks | Sales Gumroad labels "Recommended by Gumroad" |

**Order of operations:**
- **Launch day:** E1, E2 and E5. Lead with the nearest real deadlines from the Playbook's deadline table, not with urgency you invented.
- **Days 3–7:** E3 and E4.
- **First free update:** one short follow-up post (LinkedIn, and a comment on your own Reddit post) saying what was added. No re-messaging individuals.
- E6 is optional. E7 runs throughout.

## Reddit rules (why E3 has no links)
Subreddits like these commonly ban self-promotion and commercial links, and Reddit filters often remove posts with store links. I couldn't fetch the current rules (Reddit blocks automated reads), so:
1. Read each subreddit's rules in the app before posting. If promotion is banned, either skip it or message the mods first ("I compiled official-page rules for STEM PhD applicants. Can I share a summary? It contains no links.").
2. The post body has no links at all. It ends with a one-line disclosure that you made a kit and that details are on your profile.
3. The links live only in the pinned profile post (`reddit_profile_post.md`).
4. Never send unsolicited DMs with links. If someone asks for the link in comments, point them to your profile.

## Calendar
| Date | Milestone |
|---|---|
| Now | You: make the repo private (1 min). Research continues toward the gate |
| Gate passes | I rebuild v2.0 and open the PR; you set up Gumroad (45 min) and run the friend-in-India checkout test |
| L | Live. E1, E2 and E5 sent |
| L+3 to L+7 | E3 and E4 |
| First update | Free update with added universities, and one follow-up post |
| Weekly | 20-min checklist (`ops/WEEKLY_CHECKLIST.md`), with numbers into `ops/Business-Dashboard.xlsx` |
| L+6 weeks (no later than Jan 15) | **Gate review:** proceed / change / stop (rules in `research/VALIDATION_PLAN.md`) |
| Jan 15, 2027 | Season close and lessons recorded in Notion |

## What I can do between now and launch (no account needed)
- Research the remaining universities (each value re-verified by script) until the gate passes, then keep adding as free updates.
- Import pages you save from your browser for sites that block me (I'll list them). Upload the saved .html files in chat.
- Rebuild the free sample with your live store link once you send me the Gumroad URLs.
- Answer questions in a session if a buyer asks something hard (you forward it).

## Rules for honesty in every channel
- Say you made it and that there's a paid version. Never post as a "random student who found this".
- No fake urgency, no invented numbers, no testimonials until real ones exist (and then only with permission).
- Free copies (STUDENTAID, CLUBCOPY) come with no obligation. Never ask for a review in return.
- If a group or subreddit bans promotion, don't post there.
- CASL: personal messages to people you know personally are generally exempt. Group posts should identify you and give an easy way to opt out ("reply STOP and I won't message you about this again"). If you're unsure about a group, skip it.
