// Print an HTML file to PDF (or PNG with --png WxH) with headless Chromium.
// Usage: NODE_PATH=$(npm root -g) node pdf.cjs in.html out.pdf
//        NODE_PATH=$(npm root -g) node pdf.cjs in.html out.png --png 1280x720
const path = require("path");
const { chromium } = require("playwright");

(async () => {
  const [input, output, flag, size] = process.argv.slice(2);
  const browser = await chromium.launch();
  try {
    if (flag === "--png") {
      const [w, h] = size.split("x").map(Number);
      const page = await browser.newPage({ viewport: { width: w, height: h }, deviceScaleFactor: 1 });
      await page.goto("file://" + path.resolve(input), { waitUntil: "load" });
      await page.screenshot({ path: output, clip: { x: 0, y: 0, width: w, height: h } });
    } else {
      const page = await browser.newPage();
      await page.goto("file://" + path.resolve(input), { waitUntil: "load" });
      await page.pdf({
        path: output,
        format: "A4",
        printBackground: true,
        margin: { top: "16mm", bottom: "16mm", left: "15mm", right: "15mm" },
        displayHeaderFooter: true,
        headerTemplate: "<span></span>",
        footerTemplate:
          '<div style="font-size:8px;color:#777;width:100%;text-align:center;">Physics PhD Atlas 2027 · <span class="pageNumber"></span>/<span class="totalPages"></span></div>',
      });
    }
  } finally {
    await browser.close();
  }
})().catch((err) => {
  console.error(err);
  process.exit(1);
});
