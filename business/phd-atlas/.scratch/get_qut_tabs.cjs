const { chromium } = require("C:/Users/manil/AppData/Roaming/npm/node_modules/playwright");

(async () => {
  const browser = await chromium.launch({
    headless: true,
    args: ["--disable-blink-features=AutomationControlled"],
  });
  const page = await browser.newPage({
    userAgent:
      "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
  });
  await page.goto("https://www.qut.edu.au/courses/doctor-of-philosophy", {
    waitUntil: "networkidle",
    timeout: 45000,
  });

  // Click tabs
  for (const tabName of ["Requirements", "Fees", "Scholarships"]) {
    const el = await page.locator(`a:has-text("${tabName}"), button:has-text("${tabName}")`).first();
    if (await el.isVisible()) {
      await el.click();
      await page.waitForTimeout(1500);
    }
  }

  const text = await page.evaluate(() => (document.body ? document.body.innerText : ""));
  console.log("Full text length:", text.length);

  // Print sections
  for (const kw of ["Requirements", "English language", "IELTS", "TOEFL", "Fees", "Application fee"]) {
    const idx = text.indexOf(kw);
    if (idx !== -1) {
      console.log(`\n=== SECTION: ${kw} ===\n`, text.slice(idx, idx + 600));
    }
  }

  await browser.close();
})().catch(console.error);
