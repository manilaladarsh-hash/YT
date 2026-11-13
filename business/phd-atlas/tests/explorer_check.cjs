// Drive dist/.../Atlas.html from file:// with the network blocked and report results as JSON.
// Usage: NODE_PATH=$(npm root -g) node tests/explorer_check.cjs <path-to-Atlas.html>
const fs = require("fs");
const path = require("path");
const { pathToFileURL } = require("url");
const { chromium } = require("playwright");

const FIXTURE = { degree: "bachelor", sgre: "no", english: "avoid", fees: "free", funding: "need" };

async function open(browser, file, opts, out) {
  const ctx = await browser.newContext({ ...opts, acceptDownloads: true });
  await ctx.route("**/*", (route) => {
    const u = route.request().url();
    if (/^(file|blob|data):/.test(u)) return route.continue();
    out.requests.push(u);
    return route.abort();
  });
  const page = await ctx.newPage();
  page.on("console", (m) => { if (m.type() === "error") out.errors.push(m.text()); });
  page.on("pageerror", (e) => out.errors.push(String(e)));
  return { ctx, page };
}

async function ready(page) {
  await page.waitForFunction(() => window.ATLAS_READY === true, null, { timeout: 20000 });
}

async function download(page, label) {
  const [dl] = await Promise.all([page.waitForEvent("download"), page.locator("button", { hasText: label }).first().click()]);
  return { name: dl.suggestedFilename(), text: fs.readFileSync(await dl.path(), "utf8") };
}

(async () => {
  const file = pathToFileURL(path.resolve(process.argv[2])).href;
  const out = { errors: [], requests: [] };
  const browser = await chromium.launch();
  try {
    // Desktop
    const { ctx, page } = await open(browser, file, { viewport: { width: 1366, height: 900 } }, out);
    const t0 = Date.now();
    await page.goto(file, { waitUntil: "load" });
    await ready(page);
    out.loadMs = Date.now() - t0;
    out.total = await page.evaluate(() => window.atlasTest.programs.length);
    out.firstPageCards = await page.locator(".card").count();
    out.summaryAll = await page.locator("#summary").innerText();

    await page.fill("#q", "waterloo");
    await page.waitForTimeout(400);
    out.searchCards = await page.locator(".card").count();
    await page.fill("#q", "");
    await page.waitForTimeout(400);

    // Answering one question through the panel marks the button and adds fit counts.
    const btn = page.locator("#sitBody button", { hasText: "Only free or waivable" }).first();
    await btn.click();
    out.feeButtonPressed = await btn.getAttribute("aria-pressed");

    await page.evaluate((p) => window.atlasTest.setProfile(p), FIXTURE);
    await page.waitForTimeout(300);
    out.summaryFit = await page.locator("#summary").innerText();
    out.fit = await page.evaluate(() => window.atlasTest.programs.map((p) => [p.id, window.atlasTest.fit(p).status]));
    out.firstCardStatus = await page.locator(".card").first().getAttribute("class");

    await page.locator(".card button", { hasText: "Details" }).first().click();
    await page.waitForSelector("dialog[open]");
    out.dialogLinks = await page.locator("dialog[open] a", { hasText: "Source" }).evaluateAll((as) => as.map((a) => a.href));
    out.dialogText = await page.locator("dialog[open]").innerText();
    await page.locator("#dClose").click();

    const starsBtn = page.locator(".card .star");
    for (let i = 0; i < 3; i++) await starsBtn.nth(i).click();
    out.starCount = (await page.locator("#starCount").innerText()).trim();
    await page.locator("#tab-plan").click();
    out.planText = await page.locator("#view-plan").innerText();
    const ics = await download(page, "calendar");
    out.icsName = ics.name;
    out.ics = ics.text;
    const csv = await download(page, "Spreadsheet");
    out.csvName = csv.name;
    out.csvLines = csv.text.trim().split("\r\n").length;

    const todo = page.locator(".todo input[type=checkbox]").first();
    await todo.check();
    await page.reload();
    await ready(page);
    out.persistedStars = (await page.locator("#starCount").innerText()).trim();
    out.planVisibleAfterReload = await page.locator("#view-plan").isVisible();
    out.todoPersisted = await page.locator(".todo input[type=checkbox]").first().isChecked();
    await ctx.close();

    // Phone, with a 4x CPU slowdown for the load-time budget.
    const ph = await open(browser, file, { viewport: { width: 390, height: 844 }, isMobile: true, hasTouch: true, deviceScaleFactor: 2 }, out);
    const cdp = await ph.ctx.newCDPSession(ph.page);
    await cdp.send("Emulation.setCPUThrottlingRate", { rate: 4 });
    const t1 = Date.now();
    await ph.page.goto(file, { waitUntil: "load" });
    await ready(ph.page);
    out.phoneLoadMs = Date.now() - t1;
    out.phoneOverflow = await ph.page.evaluate(() => document.documentElement.scrollWidth - document.documentElement.clientWidth);
    out.phoneFirstCardTop = await ph.page.locator(".card").first().evaluate((e) => e.getBoundingClientRect().top);
    await ph.page.evaluate((p) => window.atlasTest.setProfile(p), FIXTURE);
    await ph.page.locator("#tab-guide").click();
    out.phoneGuideOverflow = await ph.page.evaluate(() => document.documentElement.scrollWidth - document.documentElement.clientWidth);
    await ph.ctx.close();
  } finally {
    await browser.close();
  }
  process.stdout.write(JSON.stringify(out));
})().catch((e) => { console.error(e); process.exit(1); });
