// node render_scene.js <name> <nframes> <outdir> [still_t ...]
const {chromium}=require('playwright');const fs=require('fs');
(async()=>{const [name,n,out,...st]=process.argv.slice(2);fs.mkdirSync(out,{recursive:true});
const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
p.on('pageerror',e=>console.log('ERR',name,e.message));
await p.goto('http://127.0.0.1:8765/final/scenes3/'+name+'.html',{waitUntil:'load'});await p.waitForTimeout(500);
const shot=async(t,path)=>{await p.evaluate(async(t)=>{seek(t);const i=document.getElementById('hg');if(i){try{await i.decode()}catch(e){}}},t);await p.screenshot({path,type:'jpeg',quality:93});};
if(st.length){for(const t of st)await shot(+t,`${out}/${name}_${t}.jpg`);}
else for(let f=0;f<+n;f++)await shot(f/25,`${out}/${String(f).padStart(4,'0')}.jpg`);
await b.close()})();
