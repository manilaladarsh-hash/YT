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
  const browser = await chromium.launch();
  try {
    const page = await browser.newPage({
      userAgent:
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0 Safari/537.36",
    });
    const resp = await page.goto(url, { waitUntil: "domcontentloaded", timeout: 45000 });
    await page.waitForTimeout(2500);
    const text = await page.evaluate(() => document.body ? document.body.innerText : "");
    process.stdout.write(JSON.stringify({ status: resp ? resp.status() : 0, final_url: page.url(), text }));
  } finally {
    await browser.close();
  }
})().catch((err) => {
  console.error(String(err));
  process.exit(1);
});
