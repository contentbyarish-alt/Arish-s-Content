const {chromium}=require('playwright');const {spawn}=require('child_process');
(async()=>{const out=process.argv[2],f0=+(process.argv[3]||0),f1=+(process.argv[4]||1966);
const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920},deviceScaleFactor:1});
await p.goto('file://'+process.cwd()+'/reel.html');await p.waitForTimeout(800);
if(process.env.FACE){await p.evaluate(f=>{window.FACE=JSON.parse(f)},process.env.FACE);}
const ff=spawn('ffmpeg',['-hide_banner','-loglevel','error','-y','-f','image2pipe','-c:v','mjpeg','-r','25','-i','-','-c:v','libx264','-preset','medium','-crf','15','-pix_fmt','yuv420p','-r','25',out]);
ff.stderr.on('data',d=>process.stderr.write(d));
for(let f=f0;f<f1;f++){await p.evaluate(t=>{seek(t);return new Promise(r=>requestAnimationFrame(()=>r()))},f/25+0.0001);
 if(process.env.FACE){await p.evaluate(()=>Promise.all([...document.querySelectorAll('.facevid')].filter(i=>i.style.display==='block').map(i=>i.decode().catch(()=>{}))));}
 const buf=await p.screenshot({type:'jpeg',quality:93});if(!ff.stdin.write(buf))await new Promise(r=>ff.stdin.once('drain',r));
 if(f%200==0)console.log('frame',f);}
ff.stdin.end();await new Promise(r=>ff.on('close',r));await b.close();console.log('done')})();
