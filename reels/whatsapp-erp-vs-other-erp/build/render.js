const {chromium}=require('playwright');const fs=require('fs');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
const names=process.argv.slice(2);
for(const n of names){await p.goto('file://'+__dirname+'/frames/'+n+'.html');await p.waitForTimeout(150);await p.screenshot({path:__dirname+'/frames/'+n+'.png'});}
await b.close()})();
