const { chromium } = require("playwright");

(async () => {
  const browser = await chromium.launch({
    headless: true,
    args: ["--disable-blink-features=AutomationControlled"],
  });
  const page = await browser.newPage({
    userAgent:
      "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0 Safari/537.36",
  });
  await page.goto("https://www.ox.ac.uk/admissions/graduate/courses/dphil-computer-science", {
    waitUntil: "domcontentloaded",
    timeout: 45000,
  });
  await page.waitForTimeout(3000);

  // Unhide all elements with .hidden, .h-0, or aria-hidden
  await page.evaluate(() => {
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
    document.querySelectorAll('*').forEach(el => {
      if (el.style) {
        el.style.visibility = 'visible';
        if (el.style.display === 'none') el.style.display = 'block';
      }
    });
  });

  const text = await page.evaluate(() => document.body.innerText);
  console.log("Text length after unhiding:", text.length);

  for (const kw of ["first-class", "degree-level qualifications", "supervisor", "gre", "funding"]) {
    const idx = text.toLowerCase().indexOf(kw);
    console.log(`Keyword "${kw}": found at ${idx}`);
    if (idx !== -1) {
      console.log(`Snippet: ${text.slice(idx, idx + 250).replace(/\n/g, ' ')}`);
    }
  }

  await browser.close();
})();
