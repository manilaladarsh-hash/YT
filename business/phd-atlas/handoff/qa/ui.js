const { chromium } = require('playwright');
const file = require('url').pathToFileURL(require('path').resolve(__dirname, '../../dist/STEM-PhD-Atlas-2027/Atlas.html')).href;
const out = require('path').join(process.env.QA_OUT || require('os').tmpdir(), 'ui-');
const FIX = { degree: "bachelor", sgre: "no", english: "avoid", fees: "free", funding: "need" };
(async () => {
  const b = await chromium.launch(); const errs = [];
  for (const [n, vp, m] of [['d', { width: 1366, height: 900 }, false], ['p', { width: 390, height: 844 }, true]]) {
    const ctx = await b.newContext({ viewport: vp, isMobile: m, hasTouch: m });
    const pg = await ctx.newPage(); pg.on('pageerror', e => errs.push(e.message)); pg.on('console', x => x.type() === 'error' && errs.push(x.text()));
    await pg.goto(file); await pg.waitForFunction(() => window.ATLAS_READY);
    await pg.evaluate(f => window.atlasTest.setProfile(f), FIX); await pg.waitForTimeout(200);
    await pg.screenshot({ path: out + n + '-fit.png' });
    await pg.locator('#fieldBtn').click(); await pg.locator('#fieldPanel label', { hasText: 'Physics' }).first().click(); await pg.locator('#fieldPanel label', { hasText: 'Computer Science' }).click();
    await pg.waitForTimeout(200); await pg.screenshot({ path: out + n + '-pop.png' });
    await pg.keyboard.press('Escape');
    if (n === 'd') { await pg.locator('#vTable').click(); await pg.waitForTimeout(800); await pg.screenshot({ path: out + n + '-table.png' }); await pg.locator('#vCards').click(); }
    if (n === 'p') { await pg.locator('#situation summary').click(); await pg.waitForTimeout(200); await pg.screenshot({ path: out + n + '-sit.png' }); await pg.locator('#situation summary').click(); }
    await pg.locator('#theme').click(); await pg.waitForTimeout(100); await pg.screenshot({ path: out + n + '-dark.png' });
    await pg.locator('.card .c-title').first().click(); await pg.waitForSelector('dialog[open]'); await pg.waitForTimeout(200); await pg.screenshot({ path: out + n + '-ddetail.png' });
    console.log(n, 'overflow', await pg.evaluate(() => document.documentElement.scrollWidth - document.documentElement.clientWidth));
    await ctx.close();
  }
  console.log('errors', errs); await b.close();
})();
