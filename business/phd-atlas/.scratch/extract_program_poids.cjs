const { chromium } = require("playwright");

(async () => {
  const browser = await chromium.launch();
  try {
    const page = await browser.newPage();
    await page.goto("https://uwyo.catalog.acalog.com/content.php?catoid=19&navoid=1924", { waitUntil: "domcontentloaded", timeout: 45000 });
    await page.waitForTimeout(2000);
    const phds = await page.evaluate(() => {
      return Array.from(document.querySelectorAll("td.block_content a[href*='preview_program.php']"))
        .map(a => ({ text: a.innerText.trim(), href: a.href }))
        .filter(l => l.text.toLowerCase().includes("ph.d.") || l.text.toLowerCase().includes("doctor"));
    });
    console.log(JSON.stringify(phds, null, 2));
  } finally {
    await browser.close();
  }
})();
