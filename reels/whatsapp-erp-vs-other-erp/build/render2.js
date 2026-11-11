const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
let names=process.argv.slice(2); if(!names.length) names=['D','E','F'].flatMap(l=>[1,2,3,4,5,6].map(i=>l+i));
for(const n of names){await p.goto('file://'+__dirname+'/frames2/'+n+'.html');await p.waitForTimeout(120);await p.screenshot({path:__dirname+'/frames2/'+n+'.png'});}
await b.close()})();
