const { chromium } = require("playwright");

(async () => {
  const url = "https://www.ucl.ac.uk/prospective-students/graduate/applying-graduate-study/how-apply/application-fees";
  const browser = await chromium.launch({
    headless: true,
    args: ["--disable-blink-features=AutomationControlled"],
  });
  try {
    const page = await browser.newPage({
      userAgent:
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0 Safari/537.36",
    });
    console.log("Navigating to:", url);
    await page.goto(url, { waitUntil: "domcontentloaded", timeout: 45000 });
    
    for (let i = 0; i < 12; i++) {
      const title = await page.title();
      const text = await page.evaluate(() => document.body ? document.body.innerText : "");
      console.log(`Attempt ${i}: Title = "${title}", Text len = ${text.length}`);
      if (text.includes("Verification successful")) {
        console.log("Saw verification successful, waiting for navigation...");
      }
      if (!title.includes("Just a moment") && !text.includes("security verification") && !text.includes("Performance and Security by Cloudflare")) {
        console.log("Passed Cloudflare!");
        break;
      }
      await page.waitForTimeout(2000);
    }

    const finalText = await page.evaluate(() => document.body ? document.body.innerText : "");
    console.log("Final text snippet:", finalText.slice(0, 400));
  } catch (err) {
    console.error("Error:", err);
  } finally {
    await browser.close();
  }
})();
