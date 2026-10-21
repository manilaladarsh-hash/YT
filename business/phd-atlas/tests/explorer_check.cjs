// Drive dist/.../Atlas.html from file:// with the network blocked and report results as JSON.
// Usage: NODE_PATH=$(npm root -g) node tests/explorer_check.cjs <path-to-Atlas.html>
const path = require("path");
const { chromium } = require("playwright");

(async () => {
  const file = "file://" + path.resolve(process.argv[2]);
  const out = { errors: [], requests: [] };
  const browser = await chromium.launch();
  try {
    const ctx = await browser.newContext({ acceptDownloads: true });
    await ctx.route("**/*", (route) => {
      const u = route.request().url();
      if (u.startsWith("file://") || u.startsWith("blob:") || u.startsWith("data:")) return route.continue();
      out.requests.push(u);
      return route.abort();
    });
    const page = await ctx.newPage();
    page.on("console", (m) => { if (m.type() === "error") out.errors.push(m.text()); });
    page.on("pageerror", (e) => out.errors.push(String(e)));
    await page.setViewportSize({ width: 1280, height: 900 });
    await page.goto(file, { waitUntil: "load" });

    out.total = await page.locator("#rows tr").count();
    out.subtitle = await page.locator("#subtitle").textContent();

    await page.selectOption("#country", "Canada");
    out.canada = await page.locator("#rows tr").count();
    await page.selectOption("#country", "");
    out.countryOptions = await page.locator("#country option").count();
    await page.selectOption("#area", "Europe");
    out.europe = await page.locator("#rows tr").count();
    out.perPositionShown = (await page.locator("#rows").textContent()).includes("Per position");
    await page.selectOption("#area", "");

    await page.selectOption("#pgre", "required");
    out.pgreRequired = await page.locator("#rows tr").count();
    await page.selectOption("#pgre", "");

    await page.selectOption("#waiver", "free");
    out.free = await page.locator("#rows tr").count();
    await page.selectOption("#waiver", "");

    await page.fill("#q", "Waterloo");
    out.search = await page.locator("#rows tr").count();
    await page.fill("#q", "");

    // Sorting by deadline: first row should have the earliest date.
    out.firstByDeadline = await page.locator("#rows tr").first().locator("td.prog b").textContent();

    // Open a detail dialog and read the quote.
    await page.locator("#rows tr").first().locator("td").nth(2).locator("button").click();
    out.dialogOpen = await page.locator("#detail").evaluate((d) => d.open);
    out.dialogQuote = await page.locator("#dQuote").textContent();
    out.dialogLink = await page.locator("#dLink").getAttribute("href");
    await page.locator("#detail button.primary").click();

    // Star two programs, filter to shortlist, export CSV.
    await page.locator("#rows tr").nth(0).locator(".star").click();
    await page.locator("#rows tr").nth(1).locator(".star").click();
    await page.locator("#onlyStar").click();
    out.starred = await page.locator("#rows tr").count();
    const [dl] = await Promise.all([page.waitForEvent("download"), page.locator("#exportBtn").click()]);
    const fs = require("fs");
    const csvPath = await dl.path();
    out.csvLines = fs.readFileSync(csvPath, "utf8").trim().split(/\r?\n/).length;
    out.csvName = dl.suggestedFilename();

    // Reload: shortlist should persist via localStorage.
    await page.reload({ waitUntil: "load" });
    out.persistedStars = await page.locator(".star[aria-pressed='true']").count();

    // Phone width: cards visible, no horizontal page scroll.
    await page.setViewportSize({ width: 375, height: 800 });
    out.cardsVisible = await page.locator("#cards").isVisible();
    out.horizontalOverflow = await page.evaluate(() => document.documentElement.scrollWidth > window.innerWidth + 1);

    // Dark mode toggle.
    await page.locator("#theme").click();
    out.theme = await page.evaluate(() => document.documentElement.dataset.theme || "");
  } finally {
    await browser.close();
  }
  process.stdout.write(JSON.stringify(out));
})().catch((e) => { console.error(e); process.exit(1); });
