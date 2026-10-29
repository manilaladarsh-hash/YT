const { chromium } = require('playwright');
const file = 'file://' + require('path').resolve(__dirname, '../../dist/STEM-PhD-Atlas-2027/Atlas.html');
(async () => { const b = await chromium.launch(); const p = await (await b.newContext({viewport:{width:1920,height:1080}})).newPage();
await p.goto(file); await p.waitForFunction(()=>window.ATLAS_READY);
await p.evaluate(f => window.atlasTest.setProfile(f), { degree: "bachelor", sgre: "no", english: "avoid", fees: "free", funding: "need" });
await p.waitForTimeout(200); await p.screenshot({path:'w-fit-1920.png'});
for (let i=0;i<5;i++) await p.locator('.card .star').nth(i).click();
await p.locator('#tab-plan').click(); await p.waitForTimeout(200); await p.screenshot({path:'w-plan-1920.png'});
await b.close(); })();
