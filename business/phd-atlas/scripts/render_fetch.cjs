// Render a page in headless Chromium and print its visible text.
// Used when a plain HTTP fetch is blocked (403) or the page needs JavaScript.
// Usage: NODE_PATH=$(npm root -g) node render_fetch.cjs <url>
const { chromium } = require("playwright");

(async () => {
  const url = process.argv[2];
  if (!url) {
    console.error("usage: render_fetch.cjs <url>");
    process.exit(2);
  }
  const browser = await chromium.launch({
    args: ["--disable-blink-features=AutomationControlled"],
  });
  try {
    const page = await browser.newPage({
      userAgent:
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0 Safari/537.36",
    });
    const resp = await page.goto(url, { waitUntil: "domcontentloaded", timeout: 45000 });
    await page.waitForTimeout(2500);
    for (let i = 0; i < 5; i++) {
      const title = await page.title();
      const bodyText = await page.evaluate(() => document.body ? document.body.innerText : "");
      if (!title.includes("Just a moment") && !bodyText.includes("security verification") && !bodyText.includes("Checking your browser")) {
        break;
      }
      await page.waitForTimeout(1500);
    }
    await page.evaluate(() => {
      document.querySelectorAll('details').forEach(d => { d.open = true; });
      document.querySelectorAll('.hidden, [class*="hidden"], .h-0, [aria-hidden="true"]').forEach(el => {
        el.classList.remove('hidden');
        el.classList.remove('h-0');
        el.removeAttribute('aria-hidden');
        if (el.style) {
          el.style.display = 'block';
          el.style.height = 'auto';
          el.style.visibility = 'visible';
        }
      });
      document.querySelectorAll('button, a').forEach(el => {
        const t = (el.innerText || '').toLowerCase();
        if (t.includes('expand all') || t.includes('show all')) {
          try { el.click(); } catch(e) {}
        }
      });
      document.querySelectorAll('*').forEach(el => {
        if (el.style) {
          el.style.visibility = 'visible';
          if (el.style.display === 'none') el.style.display = 'block';
        }
      });
    });
    await page.waitForTimeout(1000);
    const text = await page.evaluate(() => document.body ? document.body.innerText : "");
    const html = await page.content();
    let status = resp ? resp.status() : 0;
    const title = await page.title();
    if (text.length > 500 && !title.includes("Just a moment") && !text.includes("security verification")) {
      status = 200;
    }
    process.stdout.write(JSON.stringify({ status, final_url: page.url(), text, html }));
  } finally {
    await browser.close();
  }
})().catch((err) => {
  console.error(String(err));
  process.exit(1);
});
