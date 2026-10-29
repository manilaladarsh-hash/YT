const { chromium } = require('playwright');
const file = 'file://' + require('path').resolve(__dirname, '../../dist/STEM-PhD-Atlas-2027/Atlas.html');
const out = require('path').join(process.env.QA_OUT || require('os').tmpdir(), '') + require('path').sep;
(async () => {
  const browser = await chromium.launch();
  const report = {};
  for (const [name, vp, mobile] of [['desktop', { width: 1366, height: 900 }, false], ['phone', { width: 390, height: 844 }, true]]) {
    const ctx = await browser.newContext({ viewport: vp, isMobile: mobile, hasTouch: mobile, deviceScaleFactor: 1 });
    const page = await ctx.newPage();
    const errors = [], requests = [];
    page.on('console', m => { if (m.type() === 'error' || m.type() === 'warning') errors.push(m.type() + ': ' + m.text()); });
    page.on('pageerror', e => errors.push('pageerror: ' + e.message));
    page.on('request', r => { if (!r.url().startsWith('file:') && !r.url().startsWith('data:')) requests.push(r.url()); });
    const t0 = Date.now();
    await page.goto(file, { waitUntil: 'load' });
    await page.waitForFunction(() => document.querySelectorAll('.card').length > 0 || document.querySelector('.empty'), null, { timeout: 30000 }).catch(() => {});
    report[name] = { loadMs: Date.now() - t0, cards: await page.locator('.card').count(), externalRequests: requests.length };
    const hScroll = await page.evaluate(() => document.documentElement.scrollWidth - document.documentElement.clientWidth);
    report[name].horizontalOverflowPx = hScroll;
    await page.screenshot({ path: out + name + '-1-home.png', fullPage: false });
    // open situation panel on phone
    report[name].situationOpenOnLoad = await page.locator('#situation').evaluate(e => e.open);
    // quick pick and search
    const quick = page.locator('.quick button, [data-quick]');
    report[name].quickButtons = await quick.count();
    if (await quick.count() > 0) { await quick.nth(0).click().catch(e => errors.push('quick click: ' + e.message)); }
    await page.locator('input[type="search"]').fill('physics').catch(e => errors.push('search: ' + e.message));
    await page.waitForTimeout(300);
    report[name].summaryAfterSearch = (await page.locator('.summary').first().textContent()).trim().slice(0,120);
    await page.locator('input[type="search"]').fill('');
    // open first card detail
    const firstCard = page.locator('.card').first();
    await firstCard.locator('button', { hasText: 'Details' }).click().catch(e => errors.push('card open: ' + e.message));
    await page.waitForTimeout(300);
    report[name].dialogOpen = await page.locator('dialog[open]').count();
    await page.screenshot({ path: out + name + '-2-detail.png' });
    await page.keyboard.press('Escape');
    // star first two cards
    await page.locator('.star').nth(0).click().catch(e => errors.push('star: ' + e.message));
    await page.locator('.star').nth(1).click().catch(e => errors.push('star2: ' + e.message));
    // plan tab
    await page.getByRole('tab', { name: /plan/i }).or(page.locator('.tabs button', { hasText: /plan/i })).first().click().catch(e => errors.push('plan tab: ' + e.message));
    await page.waitForTimeout(300);
    report[name].planItems = await page.locator('.tl-item').count();
    report[name].todoCards = await page.locator('.todo').count();
    await page.screenshot({ path: out + name + '-3-plan.png', fullPage: true });
    // csv download
    const dl = page.waitForEvent('download', { timeout: 5000 }).catch(() => null);
    await page.locator('button', { hasText: /csv/i }).first().click().catch(e => errors.push('csv: ' + e.message));
    const d = await dl;
    report[name].csvDownload = d ? d.suggestedFilename() : 'none';
    report[name].errors = errors;
    await ctx.close();
  }
  console.log(JSON.stringify(report, null, 1));
  await browser.close();
})().catch(e => { console.error('FAILED', e); process.exit(1); });
