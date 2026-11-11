const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const d=__dirname+'/extras/';
let p=await b.newPage({viewport:{width:1080,height:1920}});await p.goto('file://'+d+'thumb.html');await p.waitForTimeout(150);await p.screenshot({path:d+'thumb_whatsapp-erp-vs_cover.png'});
await p.screenshot({path:d+'thumb_whatsapp-erp-vs_grid.png',clip:{x:0,y:240,width:1080,height:1440}});
await p.setViewportSize({width:1080,height:1350});
for(let i=1;i<=9;i++){await p.goto('file://'+d+'c'+i+'.html');await p.waitForTimeout(120);await p.screenshot({path:d+'slide_0'+i+'.png'});}
await p.setViewportSize({width:1200,height:900});await p.goto('file://'+d+'gbp.html');await p.waitForTimeout(120);await p.screenshot({path:d+'gbp_whatsapp-erp-vs_4x3.png'});
await b.close()})();
