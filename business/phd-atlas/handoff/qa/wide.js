const { chromium } = require('playwright');
const file = require('url').pathToFileURL(require('path').resolve(__dirname, '../../dist/STEM-PhD-Atlas-2027/Atlas.html')).href;
(async () => { const b = await chromium.launch();
for (const [w,h] of [[1920,1080],[1536,864],[1280,720]]) { const p = await (await b.newContext({viewport:{width:w,height:h}})).newPage();
await p.goto(file); await p.waitForFunction(()=>window.ATLAS_READY); await p.screenshot({path:'wide-'+w+'.png'}); }
await b.close(); })();
