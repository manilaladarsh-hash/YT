// Print an HTML file to PDF (or PNG with --png WxH) with headless Chromium.
// Usage: NODE_PATH=$(npm root -g) node pdf.cjs in.html out.pdf [--footer TEXT]
//        NODE_PATH=$(npm root -g) node pdf.cjs in.html out.png --png 1280x720
const path = require("path");
const { chromium } = require("playwright");

(async () => {
  const [input, output, ...rest] = process.argv.slice(2);
  const opt = (name) => { const i = rest.indexOf(name); return i >= 0 ? rest[i + 1] : null; };
  const size = opt("--png");
  const footer = (opt("--footer") || "STEM PhD Atlas 2027").replace(/[<>&]/g, "");
  const browser = await chromium.launch();
  try {
    if (size) {
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
          '<div style="font-size:8px;color:#777;width:100%;text-align:center;">' + footer + ' · <span class="pageNumber"></span>/<span class="totalPages"></span></div>',
      });
    }
  } finally {
    await browser.close();
  }
})().catch((err) => {
  console.error(err);
  process.exit(1);
});
