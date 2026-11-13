const { chromium } = require("playwright");

(async () => {
  const browser = await chromium.launch();
  try {
    const page = await browser.newPage();
    await page.goto("https://uwyo.catalog.acalog.com/", { waitUntil: "domcontentloaded", timeout: 45000 });
    await page.waitForTimeout(2000);
    const links = await page.evaluate(() => {
      return Array.from(document.querySelectorAll("a[href]")).map(a => ({
        text: a.innerText.trim(),
        href: a.href
      })).filter(l => l.text.length > 0);
    });
    console.log(JSON.stringify(links, null, 2));
  } finally {
    await browser.close();
  }
})();
