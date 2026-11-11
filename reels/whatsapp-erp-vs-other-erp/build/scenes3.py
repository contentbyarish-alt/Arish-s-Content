"""Reel v3: clean premium style, button/form WhatsApp flows, real dashboard SVG, sub-beats every ~2 s, running captions.
Serve the scratchpad root over http before rendering. SAMPLE data."""
import sys, os, json
sys.path.insert(0, os.path.dirname(__file__))
from comp import BASE_CSS, phone, flow
from scenes import ENGINE, ANIM_CSS, an, SCENES
from scenes2 import (svg, G_, kicker, head, chip, face_card, flat, clean_monitor, clean_machine, dash_crop,
                     CSS as CSS2, JS as JS2, G, T, A, PR, C, CTA, NAVY, LP, LM)

ROOT = os.path.join(os.path.dirname(__file__), "..")
OUT = os.path.join(ROOT, "final", "scenes3"); os.makedirs(OUT, exist_ok=True)
START = {n: a for n, a, b in SCENES}; DUR = {n: (b - a) / 25 for n, a, b in SCENES}

SEGS = [(0.00, 2.18, "WhatsApp ERP vs other manufacturing ERP"), (2.24, 4.92, "Kisi bhi factory mein ERP lagane se pehle hi fail kyun ho jaata hai?"),
        (4.92, 5.96, "Iske teen bade reason hain"), (5.98, 8.14, "Pehla reason: factory mein koi system hi nahi hota"),
        (8.18, 10.14, "Aap software laga bhi doge, phir bhi fail ho jaayega"), (10.16, 12.18, "Doosra: kisi bhi SME manufacturing ke paas"),
        (12.22, 14.08, "skilled employees ki manpower bahut kam hoti hai"), (14.08, 17.18, "Teesra hai implementation time. Implementation time bahut lamba kheech jaata hai"),
        (17.22, 18.64, "Yahi teeno cheezon ko solve karta hai"), (18.68, 20.34, "Hivon Automation with its WhatsApp ERP"),
        (20.48, 22.22, "Hum sabse pehle aake aapka business seekhte hain"), (22.26, 23.86, "jisse aapko hamara software na seekhna pade"),
        (23.90, 25.16, "Uske baad SOPs banaate hain"), (25.18, 26.52, "aur SOPs bhi aise banaate hain"),
        (26.52, 28.92, "jo small-medium manufacturing mein implement ho sakein"), (28.96, 29.64, "Toh aap bologe"),
        (29.70, 31.86, "mera staff toh koi software seekhega nahi, chalaayega nahi"),
        (31.92, 34.42, "Kuch seekhne ki zaroorat nahi, kyunki saari cheezein chalti hain WhatsApp par"),
        (34.44, 37.12, "Aapki labour WhatsApp par ek click mein apni attendance laga sakti hai"),
        (37.12, 39.90, "Kitna maal andar aaya hai, uska ek click ke andar input kar sakti hai"),
        (39.94, 42.86, "Aapka supervisor kisi bhi machine par baithe ek input update kar sakta hai"), (42.88, 44.16, "ki aaj maine itni production ki"),
        (44.18, 46.12, "Aap apne dashboard mein live status dekh sakte hain"), (46.14, 48.36, "aapki kitni production hui hai, aapke paas kitni inventory hai"),
        (48.36, 51.12, "kitne log hain. Ye saari cheezein ek single dashboard mein"), (51.12, 52.14, "woh bhi WhatsApp ke through"),
        (52.14, 54.66, "Ye saari cheezein chaalu ho jaati hain ₹15,000 ke mahine se"),
        (54.66, 57.68, "Agar aapko apni factory mein WhatsApp ERP jaisa custom software lagana hai"),
        (57.72, 59.72, "toh neeche diye gaye WhatsApp number par humein DM kar do")]


def captions():
    out = []
    for a, b, txt in SEGS:
        words = txt.split(); chunks = []; cur = []
        for w in words:
            if cur and (len(cur) >= 4 or len(" ".join(cur + [w])) > 24): chunks.append(" ".join(cur)); cur = []
            cur.append(w)
        if cur:
            if chunks and len(cur) == 1 and len(chunks[-1] + " " + cur[0]) <= 30: chunks[-1] += " " + cur[0]
            else: chunks.append(" ".join(cur))
        tot = sum(len(c) + 2 for c in chunks); t = a
        for c in chunks:
            d = (b - a) * (len(c) + 2) / tot; out.append([round(t, 2), round(t + d, 2), c]); t += d
    return out


CAPS = captions()

CSS = CSS2 + f"""
body{{background:radial-gradient(120% 80% at 50% 30%,#F3F8F4 0%,{G} 55%,#D6E3D9 100%)}}
#stage{{position:absolute;inset:0;transform-origin:540px 900px}}
.bl{{position:absolute;border-radius:50%;filter:blur(90px);opacity:.5}}
#capt{{position:absolute;left:0;right:0;top:1532px;text-align:center;z-index:50}}
#capt span{{display:inline-block;background:{T};color:#fff;font:800 50px Inter;letter-spacing:-1px;padding:14px 34px;border-radius:22px;box-shadow:0 14px 30px rgba(19,32,27,.25)}}
.w-msg{{width:344px;align-self:flex-start;background:#fff;border-radius:14px;box-shadow:0 1px 1.5px rgba(0,0,0,.18);color:#101729;overflow:hidden}}
.w-b{{padding:11px 14px 8px}} .w-t{{font:700 16.5px Inter;margin-bottom:8px}} .w-x{{font:400 14.5px/1.45 Inter}}
.w-f{{display:flex;justify-content:space-between;align-items:flex-end;margin-top:8px;font:400 12.5px Inter;color:#6B7280}} .w-f span{{font-size:11px}}
.w-btn{{border-top:1px solid #E7E7E7;text-align:center;padding:11px;font:600 15.5px Inter;color:#1DA35E}} .w-btn.on{{background:#E4F5EA}}
.w-out{{align-self:flex-end;background:#E2FBCB;border-radius:14px;padding:9px 14px 6px;font:400 14.5px Inter;color:#101729;box-shadow:0 1px 1.5px rgba(0,0,0,.18)}}
.w-out small{{display:block;text-align:right;font-size:11px;color:#6B7280;margin-top:2px}}
#cur{{position:absolute;width:64px;height:64px;border-radius:50%;background:rgba(19,32,27,.28);border:4px solid #fff;z-index:40;opacity:0;box-shadow:0 6px 16px rgba(0,0,0,.25)}}
#rp{{position:absolute;width:150px;height:150px;border-radius:50%;border:8px solid {A};z-index:39;opacity:0}}
.n-note{{position:absolute;background:#FFF6D8;border-radius:10px;padding:12px 22px;font:700 30px Inter;color:{T};box-shadow:0 8px 18px rgba(19,32,27,.14)}}
"""
GLOBAL_JS = """
function tapAt(id,tt,t){const b=document.getElementById(id),c=document.getElementById('cur'),r=document.getElementById('rp');if(!b)return;
 const sr=document.getElementById('stage').getBoundingClientRect(),br=b.getBoundingClientRect();const k=sr.width/1080;
 const x=(br.left+br.width*0.62-sr.left)/k,y=(br.top+br.height/2-sr.top)/k;
 const p=E.out(E.cl((t-(tt-0.45))/0.4));const vis=t>tt-0.45&&t<tt+0.5;
 c.style.opacity=vis?1:0;c.style.left=(x-32+(1-p)*160)+'px';c.style.top=(y-32+(1-p)*260)+'px';c.style.transform=`scale(${(t>tt&&t<tt+0.14)?0.78:1})`;
 const q=E.cl((t-tt)/0.42);r.style.opacity=(t>tt&&q<1)?1-q:0;r.style.left=(x-75)+'px';r.style.top=(y-75)+'px';r.style.transform=`scale(${0.3+q*1.1})`;
 b.classList.toggle('on',t>tt);}
function fillFields(sel,ts,t){document.querySelectorAll(sel).forEach((f,i)=>{if(f.dataset.v===undefined)f.dataset.v=f.firstChild.textContent;
 const v=f.dataset.v,p=E.cl((t-ts[i])/0.35);f.firstChild.textContent=t>ts[i]?v.slice(0,Math.max(1,Math.round(v.length*p))):'\\u00a0';
 f.className='hz-fi'+((t>ts[i]-0.25&&t<(ts[i+1]||ts[i]+0.6)-0.25)?' hz-act':'');});}
function globalTick(t){const st=document.getElementById('stage');const d=window.SCDUR||3;
 if(!window.NODRIFT)st.style.transform=`scale(${1+0.035*E.cl(t/d)})`;
 document.querySelectorAll('.bl').forEach((b,i)=>{b.style.transform=`translate(${Math.sin(t*0.5+i*2)*60}px,${Math.cos(t*0.4+i)*50}px)`});
 const at=t+window.SCSTART;let c=null;for(const x of CAPS){if(at>=x[0]-0.02&&at<x[1]){c=x;break}}
 const e=document.getElementById('capt');if(c){const p=E.cl((at-c[0])/0.12);e.innerHTML='<span style="transform:scale('+(0.9+0.1*E.out(p))+')">'+c[2]+'</span>';e.style.opacity=1}else e.style.opacity=0;}
function cam(KF,t){let i=0;while(i<KF.length-2&&t>=KF[i+1][0])i++;const a=KF[i],b=KF[i+1];let p=E.cl((t-a[0])/(b[0]-a[0]));p=p<.5?4*p*p*p:1-Math.pow(-2*p+2,3)/2;
 const cx=a[1]+(b[1]-a[1])*p,cy=a[2]+(b[2]-a[2])*p,s=a[3]+(b[3]-a[3])*p;const st=document.getElementById('stage');st.style.transformOrigin='0 0';st.style.transform=`translate(${540-cx*s}px,${860-cy*s}px) scale(${s})`;}
function custom(t){if(window.sc)sc(t);globalTick(t);}
"""


def scene(name, body, js="", extra_head="", nodrift=False):
    html = f'''<!doctype html><html><head><meta charset="utf-8"><style>{BASE_CSS}{ANIM_CSS}{CSS}</style></head><body>
<div class="bl" style="left:-150px;top:200px;width:600px;height:600px;background:#CFE6D6"></div><div class="bl" style="left:650px;top:1100px;width:620px;height:620px;background:#F0E2D2"></div>
<div id="stage">{body}<div id="cur"></div><div id="rp"></div></div><div id="capt"></div>
<script>window.SCSTART={START[name]/25};window.SCDUR={DUR[name]};window.NODRIFT={"true" if nodrift else "false"};const CAPS={json.dumps(CAPS, ensure_ascii=False)};
{ENGINE}{JS2}{GLOBAL_JS}{js}\nseek(0);</script></body></html>'''
    open(f"{OUT}/{name}.html", "w").write(html)


def card(inner, t=.1, top=540, h=920, extra=""):
    return f'<div class="q-card" {an(t, "u", .36)} style="left:60px;top:{top}px;width:960px;height:{h}px;{extra}">{inner}</div>'


def tmsg(title, body, time, btns=(), t=0, mid=""):
    b = ''.join(f'<div class="w-btn" id="{bid}">{lab}</div>' for bid, lab in btns)
    return f'<div class="w-msg" {an(t, "pop", .28)} id="{mid}" style="transform-origin:0 100%"><div class="w-b"><div class="w-t">{title}</div><div class="w-x">{body}</div><div class="w-f">Powered by Hivon Automations<span>{time}</span></div></div>{b}</div>'


def wout(text, time, t):
    return f'<div class="w-out" {an(t, "pop", .25)} style="transform-origin:100% 100%">{text}<small>{time} <span style="color:#1D8FF5;letter-spacing:-3px">✓✓</span></small></div>'


def sheet(title, fields, t_in, t_out, btn="Submit"):
    s = flow(title, "Hivon Automations · sample", fields, btn)
    s = s.replace('<div class="hz-dim"></div>', f'<div class="hz-dim" {an(t_in, "fade", .2, out=t_out, od=.25)}></div>')
    s = s.replace('<div class="hz-sheet">', f'<div class="hz-sheet" {an(t_in, "u", .34, out=t_out, od=.25)}>')
    return s


REPLY = '<svg width="20" height="16" viewBox="0 0 20 16" style="vertical-align:-2px;margin-right:6px"><path d="M8 1 L1 7.500 L8 14 V10 C13 10 16 11.500 18.500 15 C18 9 14.500 5 8 5 Z" fill="none" stroke="#1DA35E" stroke-width="1.8" stroke-linejoin="round"/></svg>'
PH = dict(x=271, y=420, s=1.2)


def ph(chat, sh="", t=0.0, **kw):
    p = {**PH, **kw}
    return f'<div {an(t, "u", .38)} class="hz-abs" style="left:0;top:0;width:1080px;height:1920px;z-index:4">{phone(p["x"], p["y"], p["s"], chat, sh)}</div>'


SAMPLE = '<div class="q-sample" style="left:90px;top:1478px;z-index:9">SAMPLE DATA</div>'
DATE = '<div class="hz-date">Today · sample data</div>'
SAMPLE_C = ''
ATT = lambda t=0: tmsg("Please Mark Your Attendance", "Hi, <b>Suresh (Operator)</b><br>Don't forget to mark your Check-in", "9:00 AM", [("b1", REPLY + "Check-in")], t)


# ------------------------------------------------------------------ scenes
def s01():
    pts = [(540 + (22 if i % 2 else -22), y) for i, y in enumerate(range(-40, 2000, 130))]
    L = "0px 0px," + ",".join(f"{x}px {y}px" for x, y in pts) + ",0px 1920px"
    R = ",".join(f"{x}px {y}px" for x, y in pts) + ",1080px 1920px,1080px 0px"
    crack = "M" + " L".join(f"{x} {y}" for x, y in pts)
    tags = ''.join(f'<div class="q-chip" {an(.35 + i*.14, "pop")} style="left:{x}px;top:{y}px;font-size:28px;padding:10px 22px;color:{PR}">{t}</div>' for i, (x, y, t) in enumerate([(60, 1050, "Modules"), (250, 1120, "Training"), (90, 1200, "Manuals")]))
    body = f'''<div class="hz-abs" style="inset:0;background:{T}"></div>
<div class="hz-abs" {an(-.14, "l", .34)} style="inset:0;clip-path:polygon({L});background:{LP}">
 {svg(clean_monitor(92, 640, 1.0) + G_(flat("owner", 200, 1230, 1.0, "head"), .5))}{tags}
 <div class="q-k" style="left:70px;top:270px;color:{PR}">Purana tareeka</div>
 <div class="q-h" style="left:66px;top:314px;right:auto;font-size:92px;color:{PR}">Other<br>ERP</div></div>
<div class="hz-abs" {an(-.1, "r", .34)} style="inset:0;clip-path:polygon({R});background:{LM}">
 {phone(628, 600, .82, DATE + ATT())}
 {svg(G_(flat("supervisor", 700, 1250, 1.0, "wave"), .6), z=3)}
 <div class="q-k" style="left:600px;top:270px;color:{A}">Naya tareeka</div>
 <div class="q-h" style="left:596px;top:314px;right:auto;font-size:80px;color:{A}">WhatsApp<br>ERP</div></div>
{svg(f'<path d="{crack}" stroke="{T}" stroke-width="5" fill="none"/>', z=5)}
<div class="hz-abs" {an(.82, "pop", .3)} style="left:430px;top:850px;width:220px;height:220px;border-radius:50%;background:#fff;box-shadow:0 20px 50px rgba(19,32,27,.25);display:flex;align-items:center;justify-content:center;z-index:7"><span class="q-s" style="font-size:110px;color:{T}">vs</span></div>'''
    scene("s01", body)


def face_scene(name, hg0, hgmax, cut, below, top=250, h=1010, vy=-150):
    fc, fj = face_card(top, h, hg0, hgmax, vy)
    js = fj + f"function sc(t){{faceSeek(t);const i=document.getElementById('hg');i.style.transformOrigin='50% 32%';i.style.transform=`scale(${{(t>{cut}?1.14:1)+0.03*t}})`;}}"
    scene(name, fc + below, js)


def s02():
    nums = ''.join(f'<div class="hz-abs" {an(2.68 + i*.16, "pop")} style="left:{110+i*300}px;top:1290px;width:260px;height:190px;border-radius:36px;background:#fff;box-shadow:0 14px 34px rgba(19,32,27,.12);display:flex;align-items:center;justify-content:center;font:900 120px Inter;color:{PR};letter-spacing:-5px">0{i+1}</div>' for i in range(3))
    face_scene("s02", 0.02, 3.70, 2.68, f'''<div class="q-h" {an(.3, "u", .34, out=2.55, od=.15)} style="top:1296px;font-size:60px">Factory mein ERP<br><span style="color:{PR}">fail</span> kyun hota hai?</div>{nums}''')


def s03():
    papers = ''.join(G_(f'<g transform="translate({x},{y}) rotate({r})" filter="url(#paperdrop)"><rect width="130" height="165" rx="8" fill="#fff"/>{"".join(f"<rect x=\"18\" y=\"{26+k*26}\" width=\"{94-(k%2)*30}\" height=\"8\" rx=\"4\" fill=\"#CBD5CE\"/>" for k in range(5))}</g>', .3 + i * .08, fl=i * 1.3)
                     for i, (x, y, r) in enumerate([(60, 110, -16), (760, 520, 14), (90, 600, 12), (420, 60, 4)]))
    reg = G_(f'<g transform="translate(600,690) rotate(6)" filter="url(#paperdrop)"><rect width="300" height="170" rx="10" fill="#EAD9C6"/><rect x="146" width="8" height="170" fill="#D3BFA8"/><text x="150" y="-14" text-anchor="middle" font-family="Inter" font-weight="700" font-size="24" fill="{T}">Register</text></g>', .5, fl=2)
    art = papers + reg + G_(flat("owner", 300, 330, 1.5, "head"), .25)
    mon = f'''<div {an(2.2, "dn", .36)} class="hz-abs" style="left:520px;top:70px;width:400px;height:300px;border-radius:24px;background:#fff;box-shadow:0 20px 50px rgba(19,32,27,.2);padding:26px 28px">
<div style="font:700 26px Inter;color:{T};opacity:.6">New ERP software</div><div id="st" style="font:800 40px Inter;color:{T};margin:16px 0 20px">Installing…</div>
<div style="height:22px;border-radius:11px;background:#E3EAE5;overflow:hidden"><div id="pb" style="height:100%;width:0;background:{A};border-radius:11px"></div></div></div>'''
    body = f'''{kicker("Reason 01", .05, 250, PR)}{head("Koi system", "hi nahi", .12, 296, 84, PR)}{card(svg(art, w=960, h=920) + mon)}'''
    js = f"""function sc(t){{const p=E.cl((t-2.5)/1.1),f=t>3.68;document.getElementById('pb').style.width=(f?72:p*72)+'%';document.getElementById('pb').style.background=f?'{PR}':'{A}';
const s=document.getElementById('st');s.textContent=f?'Failed ✕':'Installing…';s.style.color=f?'{PR}':'{T}';s.parentElement.style.marginLeft=(f&&t<4.0)?(Math.sin(t*70)*8)+'px':'0';}}"""
    scene("s03", body, js)


def s04():
    cells = ''
    for i in range(6):
        r, c = divmod(i, 3); x, y = 50 + c * 300, 90 + r * 400; keep = i == 4
        cells += G_(clean_machine(x, y, .78, CTA if keep else "#D9A79E"), .15 + i * .09)
        cells += f'<g {an(.3 + i*.09, "pop", **({} if keep else dict(out=2.1 + (i % 5)*.14, ofx="dim", od=.4)))}>{flat("supervisor" if keep else "worker", x + 120, y + 110, .78)}</g>'
    body = f'''{kicker("Reason 02", .05, 250, PR)}{head("Skilled manpower", "bahut kam", .12, 296, 84, PR)}{card(svg(cells, w=960, h=920))}
{chip("skilled operator", 420, 960, 2.95, extra=f"background:{A};color:#fff;z-index:6")}'''
    scene("s04", body)


def s05():
    cal = ''.join(f'<g {an(.2 + i*.05, "pop", out=.55 + i*.3, ofx="fall", od=.7)}><g transform="translate({40+i*148},{90+(i%2)*40})" filter="url(#paperdrop)"><rect width="130" height="150" rx="14" fill="#fff"/><rect width="130" height="40" rx="14" fill="{PR}"/><rect y="24" width="130" height="16" fill="{PR}"/><text x="65" y="112" text-anchor="middle" font-family="Inter" font-weight="800" font-size="46" fill="{T}">M{i+1}</text></g></g>' for i in range(6))
    bar = f'<rect x="60" y="700" width="840" height="26" rx="13" fill="#DDE6DF"/><rect id="bar" x="60" y="700" width="840" height="26" rx="13" fill="{PR}" style="transform-origin:60px 713px"/>'
    more = ''.join(f'<div class="q-chip" style="position:static;display:inline-block;margin-right:22px;font-size:34px;color:{PR}">Month {m}</div>' for m in range(7, 15))
    body = f'''{kicker("Reason 03", .05, 250, PR)}{head("Implementation time", "bahut lamba", .12, 296, 80, PR)}
{card(svg(cal + bar + G_(flat("worker", 380, 330, 1.0, "shrug"), .3), w=960, h=920) + f'<div style="position:absolute;left:60px;top:750px;font:600 30px Inter;color:{T};opacity:.6">Implementation</div><div id="pc" style="position:absolute;right:60px;top:750px;font:700 30px Inter;color:{PR}">0%</div><div id="mq" style="position:absolute;left:0;top:810px;white-space:nowrap">{more}</div>')}'''
    scene("s05", body, "function sc(t){const p=0.08+0.2*E.out(E.cl(t/3));document.getElementById('bar').style.transform=`scaleX(${p})`;document.getElementById('pc').textContent=Math.round(p*100)+'%';const m=document.getElementById('mq');m.style.opacity=t>1.7?1:0;m.style.transform=`translateX(${980-(t-1.7)*620}px)`;}")


def s06():
    ch = ''.join(f'<div class="q-chip" id="c{i}" {an(.1 + i*.1, "pop", out=1.25, od=.15)} style="left:120px;top:{620+i*190}px;font-size:76px;padding:30px 60px;width:840px"></div>' for i in range(3))
    ch += chip(f'<b style="color:{A}">✓</b> System &nbsp; <b style="color:{A}">✓</b> Manpower &nbsp; <b style="color:{A}">✓</b> Time', 150, 1400, 2.0, fs=38)
    body = f'''{kicker("Hivon Automation", 1.3)}{head("WhatsApp ERP", "", 1.4, 296, 112)}
<div class="q-h" {an(.1, "u", .3, out=1.25, od=.15)} style="top:296px;font-size:84px">Teeno ka <span style="color:{A}">ek solution</span></div>
{ph(DATE + ATT(), t=1.45, x=315, y=490, s=1.0)}{ch}'''
    js = f"""const NM=['System','Manpower','Time'];function sc(t){{NM.forEach((n,i)=>{{const ok=t>0.5+i*0.28,e=document.getElementById('c'+i);e.innerHTML='<b style="color:'+(ok?'{A}':'{PR}')+'">'+(ok?'✓':'✕')+'</b> '+n;}});}}"""
    scene("s06", body, js)


def s07():
    art = G_(clean_machine(580, 110, 1.0), .2) + G_(clean_machine(60, 70, .7), .28) + G_(flat("owner", 470, 400, 1.45, "point"), .35) + G_(flat("store", 150, 420, 1.45, "carry"), .45)
    notes = ''.join(f'<div class="n-note" {an(.75 + i*.28, "pop", base=f"rotate({r}deg)")} style="left:{x}px;top:{y}px">{t}</div>' for i, (x, y, r, t) in enumerate([(60, 330, -5, "Purchase"), (300, 290, 4, "Production"), (650, 820, 3, "Dispatch")]))
    man = f'''<div {an(1.8, "r", .34, out=2.9, od=.3)} class="hz-abs" style="left:560px;top:560px;width:330px;height:300px;border-radius:22px;background:#EAD9D5;box-shadow:0 20px 50px rgba(19,32,27,.2);padding:34px 30px">
<div style="font:800 42px Inter;color:{T};line-height:1.1">Software<br>training</div><div style="font:600 26px Inter;color:{T};opacity:.6;margin-top:10px">manual</div>
<div {an(2.35, "pop", .22)} style="position:absolute;left:20px;top:128px;width:290px;height:14px;border-radius:7px;background:{PR};transform-origin:0 50%"></div></div>'''
    body = f'''{kicker("Hivon ka tareeka", .05)}{head("Pehle aapka", "business seekhte hain", .12, 296, 80)}{card(svg(art, w=960, h=920) + notes + f'<div class="q-chip" {an(.5, "pop")} style="left:150px;top:350px;font-size:26px;padding:8px 20px;background:{A};color:#fff;display:none">Hivon</div>' + man)}
{chip("Software seekhna nahi padega", 250, 1380, 2.6, extra=f"background:{A};color:#fff;z-index:6")}'''
    scene("s07", body)


def s08():
    lines = ''.join(f'<div class="ln" style="height:14px;border-radius:7px;background:#CBD5CE;margin:20px 0;width:{[92,70,84,60,88,52][k]}%;transform-origin:0 50%"></div>' for k in range(6))
    rows = ["Process samjha", "SOP banaya", "Aapne approve kiya"]
    rw = ''.join(f'''<div {an(1.35 + i*.42, "l", .3)} style="display:flex;gap:22px;align-items:center;margin:26px 0"><svg width="70" height="70"><rect width="70" height="70" rx="20" fill="{A}"/><path d="M18 37 l12 12 l24 -27" stroke="#fff" stroke-width="9" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg><div style="font:700 42px Inter;letter-spacing:-1px;color:{T}">{t}</div></div>''' for i, t in enumerate(rows))
    mach = ''.join(G_(clean_machine(50 + i * 300, 610, .8), 2.7 + i * .12, "u", d=.34) + f'<g {an(3.3 + i*.45, "pop")}><circle cx="{170+i*300}" cy="620" r="44" fill="{A}"/><path d="M{150+i*300} 622 l14 14 l28 -32" stroke="#fff" stroke-width="10" fill="none" stroke-linecap="round" stroke-linejoin="round"/></g>' for i in range(3))
    body = f'''{kicker("Hivon ka tareeka", .05)}{head("Phir aapke", "SOPs banaate hain", .12, 296, 84)}
{card(f'<div {an(.2, "pop")} style="position:absolute;left:50px;top:50px;width:360px;height:480px;border-radius:20px;background:#fff;box-shadow:0 14px 34px rgba(19,32,27,.14);padding:34px"><div style="font:900 60px Inter;color:{A};letter-spacing:-2px">SOP</div>{lines}</div><div style="position:absolute;left:460px;top:110px;width:480px">{rw}</div>' + svg(mach, w=960, h=920))}
{chip("Small-medium factory mein implement", 150, 1385, 2.9, extra=f"background:{A};color:#fff;z-index:6;font-size:36px")}'''
    scene("s08", body, "function sc(t){document.querySelectorAll('.ln').forEach((l,i)=>{l.style.transform=`scaleX(${E.out(E.cl((t-0.4-i*0.14)/0.3))})`})}")


def s09():
    face_scene("s09", 3.77, 6.66, .72, f'''<div class="q-h" {an(.74, "u", .34)} style="top:1300px;font-size:70px">"Mera staff software<br><span style="color:{PR}">seekhega nahi</span>"</div>''')


def s10():
    body = f'''{kicker("Staff ke liye", .05)}{head("Kuch seekhne ki", "zaroorat nahi", .12, 296, 88)}
<div {an(.15, "pop", out=1.1, od=.25)} class="hz-abs" style="left:0;top:0;width:1080px;height:1920px">{svg(clean_monitor(350, 760, 1.0) + f'<g {an(.55, "stamp", .2)}><path d="M330 700 L750 1120 M750 700 L330 1120" stroke="{PR}" stroke-width="40" stroke-linecap="round"/></g>')}
<div class="q-chip" style="left:400px;top:1150px;font-size:34px;color:{PR}">Naya software</div></div>
{ph(DATE + ATT(), t=1.25, x=294, y=540, s=1.05)}
{chip("Sab kuch WhatsApp par", 230, 1380, 1.7, extra=f"background:{A};color:#fff;font-size:48px;padding:22px 44px;z-index:6")}'''
    scene("s10", body)


def chat_head(k, l1, l2, out=0.3):
    h = f'{kicker(k, .05, 196)}{head(l1, l2, .1, 236, 62)}'
    return h.replace('data-fx=', f'data-out="{out}" data-od="0.2" data-fx=')


def s11():
    chat = DATE + ATT(.25) + wout("Check-in", "9:01 AM", 1.3) + tmsg("✅ Attendance Marked", "<b>Suresh (Operator)</b> · Shift A<br>In time: <b>9:01 AM</b>", "9:01 AM", (), 1.62)
    body = f'''{chat_head("Labour · attendance", "WhatsApp par", "ek click mein attendance", .5)}{ph(chat)}
{dash_crop("dc", 1160, 200, 404, 156, 1.45, 222, 1140, 2.0)}{SAMPLE_C}'''
    scene("s11", body, "function sc(t){tapAt('b1',1.1,t);svgSeek('dc',99);cam([[0,540,860,1],[0.45,540,860,1],[0.9,540,800,1.5],[1.95,540,820,1.5],[2.3,540,860,1],[9,540,860,1]],t)}", nodrift=True)


def s12():
    chat = DATE + tmsg("Material Inward", "Gate par maal aaya hai.<br>Kitna aaya, entry karein.", "10:14 AM", [("b1", REPLY + "Inward entry")], .2)
    sh = sheet("Inward Entry", [("Item", "Steel Rod 12mm", True, False), ("Quantity", "500 kg", False, False), ("Vendor", "Vendor A", True, False)], .78, 2.32)
    body = f'''{chat_head("Store · maal inward", "Kitna maal aaya,", "ek click mein input")}{ph(chat, sh)}
{dash_crop("dc", 1112, 692, 440, 56, 2.0, 76, 1270, 2.4, "Dashboard · Live Alerts")}{SAMPLE_C}'''
    scene("s12", body, "function sc(t){tapAt('b1',0.66,t);fillFields('.hz-fi',[1.05,1.4,1.75],t);const b=document.querySelector('.hz-btn');b.style.filter=(t>2.15&&t<2.3)?'brightness(.85)':'';svgSeek('dc',99);cam([[0,540,860,1],[0.2,540,860,1],[0.55,540,760,1.45],[0.8,540,760,1.45],[1.1,540,1230,1.45],[2.3,540,1230,1.45],[2.6,540,860,1],[9,540,860,1]],t)}", nodrift=True)


def s13():
    chat = (DATE + tmsg("Production Update", "Shift A ki production entry karein.<br>Machine aur quantity select karein.", "5:55 PM", [("b1", REPLY + "Entry karein"), ("b2", REPLY + "Aaj ka target")], .2) +
            tmsg("✅ Production Logged", "Machine: <b>M-4</b><br>Item: <b>Flange 40mm</b><br>Qty: <b>120 pcs</b>", "5:56 PM", (), 3.72))
    sh = sheet("Production Entry", [("Machine", "M-4 (CNC Lathe)", True, False), ("Item", "Flange 40mm", True, False), ("Quantity (pcs)", "120", False, False)], .95, 3.55)
    body = f'''{chat_head("Supervisor · machine se", "Aaj ki production,", "ek input update")}
{svg(G_(clean_machine(30, 900, .78), .2) + G_(flat("supervisor", 60, 1130, 1.0, "phone"), .3), z=3)}{ph(chat, sh, x=420, y=420, s=1.2)}'''
    scene("s13", body, "function sc(t){tapAt('b1',0.8,t);fillFields('.hz-fi',[1.5,2.05,2.6],t);const b=document.querySelector('.hz-btn');b.style.filter=(t>3.35&&t<3.52)?'brightness(.85)':'';b.style.transform=(t>3.35&&t<3.52)?'scale(.96)':'';cam([[0,540,860,1],[0.3,540,860,1],[0.7,690,760,1.45],[0.95,690,760,1.45],[1.3,690,1230,1.45],[3.5,690,1230,1.45],[3.8,690,860,1.4],[9,690,880,1.45]],t)}", nodrift=True)


def s14():
    kf = [(0, 950, 490, .76), (1.6, 950, 490, .76), (2.1, 520, 445, 2.15), (3.3, 520, 445, 2.15), (3.75, 940, 445, 2.15), (4.3, 940, 445, 2.15),
          (4.75, 1362, 277, 2.15), (5.2, 1362, 277, 2.15), (5.65, 1332, 712, 2.0), (6.75, 1332, 712, 2.0), (7.25, 950, 490, .76), (9, 950, 490, .76)]
    body = f'''{kicker("Hivon ERP · live status", .05)}{head("Poori factory,", "ek single dashboard", .12, 296, 80)}
<div class="q-card" {an(.1, "u", .36)} style="left:40px;top:540px;width:1000px;height:760px;border-radius:36px"><div class="q-vp" style="left:0;top:0;width:1000px;height:760px"><iframe id="db" src="/assets2/t_dash.svg" width="1600" height="900"></iframe></div></div>
<div id="lab" class="q-chip" style="left:90px;top:1350px;font-size:44px;background:{A};color:#fff;padding:20px 40px"></div>{SAMPLE}'''
    js = f"""const KF={json.dumps(kf)};const LB=[[2.0,'Production'],[3.6,'Inventory'],[4.65,'Kitne log'],[5.55,'Live: Machine M-4 update'],[7.0,'Sab kuch ek jagah']];
function sc(t){{svgSeek('db',Math.max(0,t-0.15)*2);
 let i=0;while(i<KF.length-2&&t>=KF[i+1][0])i++;const a=KF[i],b=KF[i+1];let p=E.cl((t-a[0])/(b[0]-a[0]));p=p<.5?4*p*p*p:1-Math.pow(-2*p+2,3)/2;
 const cx=a[1]+(b[1]-a[1])*p,cy=a[2]+(b[2]-a[2])*p,s=a[3]+(b[3]-a[3])*p;
 document.getElementById('db').style.transform=`translate(${{500-cx*s}}px,${{380-cy*s}}px) scale(${{s}})`;
 let l='';for(const [tt,x] of LB)if(t>=tt)l=x;const e=document.getElementById('lab');e.textContent=l;e.style.opacity=l?1:0;}}"""
    scene("s14", body, js, nodrift=True)


def s15():
    tiles = ''.join(f'<div class="q-card" {an(.1 + i*.2, "pop")} style="left:{90+(i%2)*470}px;top:{330+(i//2)*200}px;width:430px;height:170px;border-radius:32px;display:flex;align-items:center;gap:22px;padding:0 34px;font:700 40px Inter;color:{T}"><span style="font-size:60px">{e}</span>{t}</div>' for i, (e, t) in enumerate([("🕘", "Attendance"), ("🚚", "Inward"), ("⚙️", "Production"), ("📊", "Dashboard")]))
    body = f'''{kicker("Ye sab chaalu hota hai", .05, 250)}{tiles}
<div class="hz-abs" {an(1.35, "pop", .34)} style="left:80px;top:800px;font:900 240px Inter;letter-spacing:-12px;color:{T}">₹<span id="pr">0</span></div>
<div class="hz-abs" {an(1.95, "u", .34)} style="left:92px;top:1080px;font:700 76px Inter;letter-spacing:-2px;color:{A}">ke mahine se</div>'''
    scene("s15", body, "function sc(t){document.getElementById('pr').textContent=Math.round(15000*E.out(E.cl((t-1.35)/0.5))).toLocaleString('en-IN')}")


def s16():
    below = f'''{head("Apni factory ka", "custom WhatsApp ERP?", .52, 1170, 74)}
<div class="hz-abs" {an(3.02, "u", .36)} style="left:90px;top:1360px;background:{CTA};color:{NAVY};border-radius:999px;padding:26px 48px;font:800 50px Inter;letter-spacing:-1px;z-index:9">WhatsApp pe DM karo <span id="ar" style="display:inline-block">↓</span></div>
<div class="hz-abs" {an(.3, "fade", .3)} style="right:90px;top:1392px;font:800 50px Inter;letter-spacing:-1px;color:{T}">hivon<span style="color:{CTA}">.</span></div>'''
    fc, fj = face_card(230, 880, 6.72, 11.6, -190)
    js = fj + "function sc(t){faceSeek(t);const i=document.getElementById('hg');i.style.transformOrigin='50% 32%';i.style.transform=`scale(${(t>3.0?1.12:1)+0.02*t})`;document.getElementById('ar').style.transform=`translateY(${Math.sin(t*7)*7}px)`;}"
    scene("s16", fc + below, js)


if __name__ == "__main__":
    fs = [s01, s02, s03, s04, s05, s06, s07, s08, s09, s10, s11, s12, s13, s14, s15, s16]
    only = sys.argv[1:]
    for f in fs:
        if not only or f.__name__ in only: f()
    sc = [list(x) for x in SCENES]; sc[-1][2] = 1494
    json.dump(sc, open(f"{OUT}/scenes.json", "w"))
    json.dump(CAPS, open(f"{OUT}/captions.json", "w"), ensure_ascii=False)
    print("ok", len(CAPS))
