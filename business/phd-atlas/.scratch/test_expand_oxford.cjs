const { chromium } = require('playwright');
(async () => {
  const browser = await chromium.launch({ headless: true, args: ['--disable-blink-features=AutomationControlled'] });
  const page = await browser.newPage();
  await page.goto('https://www.ox.ac.uk/admissions/graduate/courses/dphil-computer-science', { waitUntil: 'domcontentloaded', timeout: 45000 });
  await page.waitForTimeout(3000);
  
  // Find all accordion buttons
  const buttons = await page.$$eval('button', btns => btns.map(b => ({
    text: b.innerText.trim(),
    ariaExpanded: b.getAttribute('aria-expanded'),
    ariaControls: b.getAttribute('aria-controls')
  })).filter(b => b.text.length > 0));
  console.log('Buttons:', JSON.stringify(buttons.slice(0, 15), null, 2));

  // If there are buttons with aria-controls, click them
  const targets = await page.$$('button[aria-controls]');
  for (const b of targets) {
    try { await b.click(); } catch(e) {}
  }
  await page.waitForTimeout(1000);

  const text = await page.evaluate(() => document.body.innerText);
  console.log('After clicking aria-controls, length is:', text.length);
  const idx = text.indexOf('Proven and potential academic excellence');
  if (idx !== -1) {
    console.log(text.slice(idx, idx + 600));
  }
  await browser.close();
})();
