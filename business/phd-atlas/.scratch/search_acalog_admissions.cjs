const { chromium } = require("playwright");

(async () => {
  const browser = await chromium.launch();
  try {
    const page = await browser.newPage();
    // Search in catalog for Graduate Admissions
    await page.goto("https://uwyo.catalog.acalog.com/search_advanced.php?catoid=19&search_database=Search&search_db=Search&cpage=1&ecpage=1&ppage=1&spage=1&tpage=1&location=3&filter%5Bexact_search%5D=1&filter%5Bkeyword%5D=Graduate+Admissions", { waitUntil: "domcontentloaded", timeout: 45000 });
    await page.waitForTimeout(2500);
    const results = await page.evaluate(() => {
      return Array.from(document.querySelectorAll("td.block_content a[href]")).map(a => ({
        text: a.innerText.trim(),
        href: a.href
      }));
    });
    console.log(JSON.stringify(results, null, 2));
  } finally {
    await browser.close();
  }
})();
