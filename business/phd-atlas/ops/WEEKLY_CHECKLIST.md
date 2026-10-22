# Weekly checklist (20–30 minutes, Mondays)

| # | Task | Time | Automated? |
|---|---|---|---|
| 1 | Open Gumroad → Analytics/Sales and copy last week's views, sample downloads, paid orders, refunds, gross and payout into `ops/Business-Dashboard.xlsx` → *Weekly actuals*. Also mark how many orders came from people you don't know (check buyer emails and names) | 8 min | No: needs your judgement on "unrelated" |
| 2 | Per-channel orders from Gumroad's UTM-links dashboard (network = `whatsapp` + `group`; `reddit`) into the same row. Also count orders from India (Sales → filter by country) and any batch licences | 2 min | No |
| 3 | Read and reply to emails: refunds (just approve them), free-copy requests (send the `STUDENTAID` template), data-error reports (forward to a Claude session), survey replies (count concrete benefits) | 5–10 min | Partly: welcome and survey emails send themselves |
| 4 | Check the GitHub issue "Source watch report" if one was opened this week. Each listed program needs a quick look: has the deadline or rule changed? | 2–5 min | Detection is automated; deciding what changed needs judgement |
| 5 | Log your business minutes in *Hours* (study-permit record) | 1 min | No |
| 6 | Glance at *Gates* | 1 min | Yes |

## Monthly during the season (Nov–Jan), about 30 minutes
- Start a Claude session in this repo with: "Refresh the Atlas data and ship v1.x." I re-fetch every source, update changed values with new quotes, re-run validation and tests, and rebuild the ZIP.
- You upload the new ZIP to Gumroad and click **Send update to customers** (text in `store/EMAILS.md`).

## Each August (new cycle), 1–2 hours of your time
- Decide whether to run the next edition, using the gate results from last season.
- If yes, I refresh all programs for the new cycle, and you re-upload and relaunch with the same messages.

## What needs you vs what runs itself
| Runs itself | Needs you |
|---|---|
| Checkout, tax, delivery, receipts (Gumroad) | Approving any spend or message |
| Welcome and survey emails (Gumroad workflows) | Judging refunds in edge cases (default: just refund) |
| Weekly source-change detection (GitHub Actions) | Deciding whether a flagged change matters |
| Data validation and build checks (scripts) | Uploading new versions to Gumroad |
| Gate calculation (workbook formulas) | The Dec 15 proceed/change/stop decision |
