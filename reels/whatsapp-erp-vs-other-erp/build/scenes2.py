"""Final Reel v2: clean style, real Hivon SVGs (chat + dashboard) embedded as iframes and driven by seek(t).
Serve the scratchpad root over http (same origin) before rendering. SAMPLE data."""
import sys, os, json, re
sys.path.insert(0, os.path.dirname(__file__))
from comp import P, BASE_CSS, person, svg_defs
from scenes import ENGINE, ANIM_CSS, an, SCENES

ROOT = os.path.join(os.path.dirname(__file__), "..")
OUT = os.path.join(ROOT, "final", "scenes2"); os.makedirs(OUT, exist_ok=True)
AS = os.path.join(ROOT, "assets2")
G, T, A, PR, C, CTA, NAVY = P['ground'], P['text'], P['accent'], P['problem'], P['card'], P['cta'], P['navy']
LP, LM = "#EFE4E1", "#E1EDE4"   # pale coral side, pale mint side


# ---------- timed copies of the real SVGs (only --d delays change) ----------
def timed_chat(src, dst, d):
    s = open(f"{AS}/{src}.svg").read()
    vals = iter(d)
    s = re.sub(r'style="--d:[0-9.]+s"', lambda m: f'style="--d:{next(vals)}s"', s)
    s = s.replace('<g id="typing"', '<g id="typing" display="none"') if 'id="typing" display' not in s else s
    open(f"{AS}/{dst}.svg", "w").write(s)


def prep_assets():
    timed_chat("chat_attendance", "t_att", [.15, .95, 1.25, 9, 9])
    timed_chat("chat_inward", "t_inw", [.15, .95, 1.25, 9, 1.5])
    timed_chat("chat_production", "t_prod", [.2, 1.5, 1.9, 9, 3.0])
    s = open(f"{AS}/dashboard_reel.svg").read()
    s = s.replace('<g id="alert-4" class="slide" style="--d:2.65s">', '<g id="alert-4" class="slide" style="--d:11.0s">')
    open(f"{AS}/t_dash.svg", "w").write(s)


CSS = f"""
.q-h{{position:absolute;left:90px;right:90px;font:800 78px Inter;letter-spacing:-2.5px;line-height:1.04;color:{T}}}
.q-k{{position:absolute;left:92px;font:700 28px Inter;letter-spacing:.16em;text-transform:uppercase}}
.q-card{{position:absolute;background:{C};border-radius:44px;box-shadow:0 24px 60px rgba(19,32,27,.10),0 2px 6px rgba(19,32,27,.06);overflow:hidden}}
.q-chip{{position:absolute;background:#fff;border-radius:999px;padding:16px 30px;font:700 34px Inter;color:{T};box-shadow:0 10px 26px rgba(19,32,27,.12);white-space:nowrap}}
.q-line{{position:absolute;left:90px;right:90px;font:600 40px Inter;line-height:1.25;color:{T}}}
.q-s{{font-family:'DejaVu Serif';font-style:italic;font-weight:700;letter-spacing:-1px}}
.q-vp{{position:absolute;overflow:hidden}}
iframe{{border:0;position:absolute;left:0;top:0;transform-origin:0 0;background:transparent}}
.q-sample{{position:absolute;font:600 22px Inter;color:rgba(19,32,27,.5);letter-spacing:.08em}}
"""
JS = """
function svgSeek(id,tt){const f=document.getElementById(id);const d=f&&f.contentDocument;if(!d||!d.getAnimations)return;
 d.getAnimations().forEach(a=>{a.pause();a.currentTime=Math.max(0,tt*1000)});}
"""


def scene(name, body, custom="", bg=G):
    html = f'<!doctype html><html><head><meta charset="utf-8"><style>{BASE_CSS}{ANIM_CSS}{CSS}</style></head><body style="background:{bg}">{body}<script>{ENGINE}{JS}{custom}\nseek(0);</script></body></html>'
    open(f"{OUT}/{name}.html", "w").write(html)


def svg(inner, w=1080, h=1920, x=0, y=0, z=1):
    return f'<svg class="hz-abs" style="left:{x}px;top:{y}px;z-index:{z}" width="{w}" height="{h}" viewBox="0 0 {w} {h}">{svg_defs()}{inner}</svg>'


def G_(inner, t=0, fx="pop", **kw):
    return f'<g {an(t, fx, **kw)}>{inner}</g>'


def kicker(text, t=.05, top=250, col=A):
    return f'<div class="q-k" {an(t, "fade", .25)} style="top:{top}px;color:{col}">{text}</div>'


def head(l1, l2="", t=.12, top=296, fs=78, col=A):
    l2h = f'<br><span style="color:{col}">{l2}</span>' if l2 else ""
    return f'<div class="q-h" {an(t, "u", .34)} style="top:{top}px;font-size:{fs}px">{l1}{l2h}</div>'


def line(text, t, top=1560, fs=40):
    return f'<div class="q-line" {an(t, "fade", .3)} style="top:{top}px;font-size:{fs}px">{text}</div>'


def chip(text, x, y, t, fx="pop", fs=34, extra=""):
    return f'<div class="q-chip" {an(t, fx)} style="left:{x}px;top:{y}px;font-size:{fs}px;{extra}">{text}</div>'


def phone_frame(fid, src, scale=1.45, cx=540, top=340):
    """Real chat SVG (900x1060; phone body at x226-674, y100-1000) scaled and centred on cx."""
    return f'<iframe id="{fid}" src="/assets2/{src}.svg" width="900" height="1060" style="left:{cx-450*scale:.0f}px;top:{top-100*scale:.0f}px;transform:scale({scale})"></iframe>'


def dash_crop(fid, x, y, w, h, scale, left, top, t, label="Hivon ERP dashboard"):
    return f'''<div {an(t, "u", .34)} class="q-card" style="left:{left}px;top:{top}px;width:{w*scale+48:.0f}px;height:{h*scale+92:.0f}px;z-index:8;border-radius:30px">
<div style="position:absolute;left:26px;top:16px;font:700 24px Inter;letter-spacing:.1em;color:{A}">{label.upper()}</div>
<div class="q-vp" style="left:24px;top:60px;width:{w*scale:.0f}px;height:{h*scale:.0f}px;border-radius:18px"><iframe id="{fid}" src="/assets2/dashboard_reel_static.svg" width="1600" height="900" style="transform:translate({-x*scale:.0f}px,{-y*scale:.0f}px) scale({scale})"></iframe></div></div>'''


def face_card(top, h, hg0, hgmax, vy=-150, left=60, w=960):
    sc = w / 1080
    return f'''<div class="q-card" {an(0, "fade", .2)} style="left:{left}px;top:{top}px;width:{w}px;height:{h}px;background:#cfdcd1">
<img id="hg" style="position:absolute;left:0;top:{vy}px;width:{w}px;height:{1920*sc:.0f}px" src="/final/hg/0001.jpg"></div>''', f'''
function faceSeek(t){{const n=Math.min(Math.round({hgmax}*25),Math.max(0,Math.round(({hg0}+t)*25)))+1;const i=document.getElementById('hg');const s='/final/hg/'+String(Math.min(291,n)).padStart(4,'0')+'.jpg';if(!i.src.endsWith(s))i.src=s;}}'''


def flat(role, x, y, s, pose="stand", flip=False):
    return person(role, "pill", x, y, s, pose=pose, flip=flip)


def clean_monitor(x, y, s=1):
    cells = ''.join(f'<rect x="{30+c*66}" y="{84+r*38}" width="54" height="24" rx="5" fill="{PR}" opacity="{.16+((r*3+c)%4)*.1}"/>' for r in range(6) for c in range(5))
    win = lambda dx, dy, o: f'<g transform="translate({dx},{dy})" opacity="{o}"><rect width="380" height="330" rx="18" fill="#fff"/><rect width="380" height="52" rx="18" fill="#E3C9C4"/><rect y="30" width="380" height="22" fill="#E3C9C4"/></g>'
    return f'''<g transform="translate({x},{y}) scale({s})" filter="url(#paperdrop)">{win(-34,-40,.55)}{win(-17,-20,.8)}{win(0,0,1)}{cells}
<circle cx="24" cy="26" r="7" fill="{PR}"/><circle cx="46" cy="26" r="7" fill="#fff"/><circle cx="68" cy="26" r="7" fill="#fff"/></g>'''


def clean_machine(x, y, s=1, lamp=CTA):
    return f'''<g transform="translate({x},{y}) scale({s})"><rect width="300" height="220" rx="22" fill="#B4C9BA"/><rect x="24" y="26" width="120" height="80" rx="12" fill="#F8FBF8"/>
<circle cx="220" cy="104" r="54" fill="#F8FBF8"/><circle cx="220" cy="104" r="16" fill="#7E9A87"/><rect x="50" y="220" width="200" height="46" rx="8" fill="#93AD9B"/><circle cx="262" cy="34" r="12" fill="{lamp}"/></g>'''


# ------------------------------------------------------------------ scenes
def s01():
    pts = [(540 + (22 if i % 2 else -22), y) for i, y in enumerate(range(-40, 2000, 130))]
    L = "0px 0px," + ",".join(f"{x}px {y}px" for x, y in pts) + ",0px 1920px"
    R = ",".join(f"{x}px {y}px" for x, y in pts) + ",1080px 1920px,1080px 0px"
    crack = "M" + " L".join(f"{x} {y}" for x, y in pts)
    body = f'''<div class="hz-abs" style="inset:0;background:{T}"></div>
<div class="hz-abs" {an(-.14, "l", .34)} style="inset:0;clip-path:polygon({L});background:{LP}">
 {svg(clean_monitor(92, 640, 1.0) + G_(flat("owner", 160, 1130, 1.3, "head"), .5))}
 <div class="q-k" style="left:70px;top:270px;color:{PR}">Purana tareeka</div>
 <div class="q-h" style="left:66px;top:314px;right:auto;font-size:92px;color:{PR}">Other<br>ERP</div></div>
<div class="hz-abs" {an(-.1, "r", .34)} style="inset:0;clip-path:polygon({R});background:{LM}">
 {phone_frame("ph", "chat_production_static", .82, 810, 600)}
 {svg(G_(flat("supervisor", 690, 1330, 1.05, "wave"), .6), z=3)}
 <div class="q-k" style="left:600px;top:270px;color:{A}">Naya tareeka</div>
 <div class="q-h" style="left:596px;top:314px;right:auto;font-size:80px;color:{A}">WhatsApp<br>ERP</div></div>
{svg(f'<path d="{crack}" stroke="{T}" stroke-width="5" fill="none"/>', z=5)}
<div class="hz-abs" {an(.82, "pop", .3)} style="left:430px;top:850px;width:220px;height:220px;border-radius:50%;background:#fff;box-shadow:0 20px 50px rgba(19,32,27,.25);display:flex;align-items:center;justify-content:center;z-index:7"><span class="q-s" style="font-size:110px;color:{T}">vs</span></div>
<div class="hz-abs" {an(1.5, "u", .34)} style="left:0;right:0;top:1610px;text-align:center;z-index:7"><span style="background:{T};color:#fff;border-radius:999px;padding:16px 44px;font:800 52px Inter;letter-spacing:-1px">for Manufacturing</span></div>'''
    scene("s01", body, "function custom(t){svgSeek('ph',99)}", bg=T)


def s02():
    fc, fj = face_card(250, 1090, 0.02, 3.70)
    body = f'''{fc}{head("Factory mein ERP", '<span style="color:' + PR + '">fail</span> kyun hota hai?', .3, 1390, 76, T)}
{chip("3 bade reason", 600, 1190, 2.68, extra=f"background:{T};color:#fff;font-size:40px;z-index:6")}'''
    scene("s02", body, fj + "function custom(t){faceSeek(t)}")


def reason(name, num, l1, l2, art, cap, tcap):
    body = f'''{kicker(f"Reason {num}", .05, 250, PR)}{head(l1, l2, .12, 296, 84, PR)}
<div class="q-card" {an(.1, "u", .36)} style="left:60px;top:560px;width:960px;height:880px">{svg(art, w=960, h=880)}</div>
{line(cap, tcap, 1500, 42)}'''
    scene(name, body)


def s03():
    papers = ''.join(G_(f'<g transform="translate({x},{y}) rotate({r})" filter="url(#paperdrop)"><rect width="130" height="165" rx="8" fill="#fff"/>{"".join(f"<rect x=\"18\" y=\"{26+k*26}\" width=\"{94-(k%2)*30}\" height=\"8\" rx=\"4\" fill=\"#CBD5CE\"/>" for k in range(5))}</g>', .3 + i * .08, fl=i * 1.3)
                     for i, (x, y, r) in enumerate([(70, 90, -16), (760, 110, 14), (110, 560, 12), (740, 560, -10), (430, 40, 4)]))
    reason("s03", "01", "Koi system", "hi nahi", papers + G_(flat("owner", 330, 260, 1.55, "head"), .25),
           f'Software laga bhi doge, <b style="color:{PR}">phir bhi fail</b>', 2.3)


def s04():
    crew = ''.join(f'<g {an(.25 + i*.08, "pop", **({} if i == 2 else dict(out=1.0 + i*.16, ofx="dim", od=.4)))}>{flat("supervisor" if i == 2 else "worker", 10+i*186, 300, 1.05)}</g>' for i in range(5))
    body = f'''{kicker("Reason 02", .05, 250, PR)}{head("Skilled manpower", "bahut kam", .12, 296, 84, PR)}
<div class="q-card" {an(.1, "u", .36)} style="left:60px;top:560px;width:960px;height:880px">{svg(crew, w=960, h=880)}</div>
{chip("skilled", 440, 760, 2.0, extra=f"background:{A};color:#fff;z-index:6")}
{line("SME manufacturing ki asli dikkat", 2.7, 1500, 42)}'''
    scene("s04", body)


def s05():
    cal = ''.join(f'<g {an(.2 + i*.05, "pop", out=.6 + i*.36, ofx="fall", od=.7)}><g transform="translate({40+i*148},{90+(i%2)*40})" filter="url(#paperdrop)"><rect width="130" height="150" rx="14" fill="#fff"/><rect width="130" height="40" rx="14" fill="{PR}"/><rect y="24" width="130" height="16" fill="{PR}"/><text x="65" y="112" text-anchor="middle" font-family="Inter" font-weight="800" font-size="46" fill="{T}">M{i+1}</text></g></g>' for i in range(6))
    bar = f'<rect x="60" y="640" width="840" height="26" rx="13" fill="#DDE6DF"/><rect id="bar" x="60" y="640" width="840" height="26" rx="13" fill="{PR}" style="transform-origin:60px 653px"/>'
    body = f'''{kicker("Reason 03", .05, 250, PR)}{head("Implementation time", "bahut lamba", .12, 296, 80, PR)}
<div class="q-card" {an(.1, "u", .36)} style="left:60px;top:560px;width:960px;height:880px">{svg(cal + bar + G_(flat("worker", 360, 300, 1.0, "shrug"), .3), w=960, h=880)}
<div style="position:absolute;left:60px;top:690px;font:600 30px Inter;color:{T};opacity:.6">Implementation</div><div id="pc" style="position:absolute;right:60px;top:690px;font:700 30px Inter;color:{PR}">0%</div></div>
{line("Kheechta hi jaata hai", 2.3, 1500, 42)}'''
    scene("s05", body, "function custom(t){const p=0.08+0.22*E.out(E.cl(t/3));document.getElementById('bar').style.transform=`scaleX(${p})`;document.getElementById('pc').textContent=Math.round(p*100)+'%';}")


def s06():
    chips = ''.join(chip(f'<span style="color:{A}">✓</span> {t}', x, 1500, 1.5 + i * .22) for i, (x, t) in enumerate([(80, "System"), (350, "Manpower"), (700, "Time")]))
    body = f'''{kicker("Hivon Automation", .05)}{head("WhatsApp ERP", "", .12, 296, 110)}
<div {an(.68, "u", .4)} class="hz-abs" style="left:0;top:0;width:1080px;height:1920px">{phone_frame("ph", "chat_production_static", 1.12, 540, 470)}</div>
{chips}{line(f'Yahi teeno cheezein <b style="color:{A}">solve</b> karta hai', .3, 1620, 44)}'''
    scene("s06", body, "function custom(t){svgSeek('ph',99)}")


def s07():
    art = G_(clean_machine(560, 150, 1.0), .2) + G_(clean_machine(90, 90, .7), .28) + G_(flat("owner", 440, 360, 1.5, "point"), .35) + G_(flat("store", 120, 380, 1.5, "carry"), .45)
    body = f'''{kicker("Hivon ka tareeka", .05)}{head("Pehle aapka", "business seekhte hain", .12, 296, 80)}
<div class="q-card" {an(.1, "u", .36)} style="left:60px;top:560px;width:960px;height:880px">{svg(art, w=960, h=880)}</div>
{line(f'Taaki aapko hamara software <b style="color:{A}">na seekhna pade</b>', 1.78, 1500, 40)}'''
    scene("s07", body)


def s08():
    rows = ["Aapka process samjha", "SOP banaya", "Factory mein implement"]
    rw = ''.join(f'''<div style="display:flex;gap:28px;align-items:center;margin:34px 0"><div style="width:84px;height:84px;border-radius:24px;background:{G};flex:none;position:relative"><svg {an(.6 + i*.75, "pop", .25)} width="84" height="84" style="position:absolute;left:0;top:0"><rect width="84" height="84" rx="24" fill="{A}"/><path d="M22 44 l14 14 l28 -32" stroke="#fff" stroke-width="10" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg></div><div style="font:700 52px Inter;letter-spacing:-1px;color:{T}">{t}</div></div>''' for i, t in enumerate(rows))
    body = f'''{kicker("Hivon ka tareeka", .05)}{head("Phir aapke", "SOPs banaate hain", .12, 296, 84)}
<div class="q-card" {an(.1, "u", .36)} style="left:60px;top:580px;width:960px;height:700px;padding:50px 60px"><div style="font:800 34px Inter;letter-spacing:.14em;color:{A}">SOP</div>{rw}</div>
{line(f'SOPs jo <b style="color:{A}">small-medium manufacturing</b> mein implement ho sakein', 2.7, 1360, 42)}'''
    scene("s08", body)


def s09():
    fc, fj = face_card(250, 1090, 3.77, 6.66)
    body = f'''{fc}{head('"Mera staff software', '<span style="color:' + PR + '">seekhega nahi</span>"', .5, 1390, 72, T)}'''
    scene("s09", body, fj + "function custom(t){faceSeek(t)}")


def s10():
    body = f'''{kicker("Staff ke liye", .05)}{head("Kuch seekhne ki", "zaroorat nahi", .12, 296, 88)}
<div {an(.9, "u", .4)} class="hz-abs" style="left:0;top:0;width:1080px;height:1920px">{phone_frame("ph", "t_att", 1.2, 540, 560)}</div>
{chip("Sab kuch WhatsApp par", 250, 1580, 1.62, extra=f"background:{A};color:#fff;font-size:46px;padding:22px 44px;z-index:6")}'''
    scene("s10", body, "function custom(t){svgSeek('ph',0.62)}")


def chat_scene(name, kick, l1, l2, src, t0, crop, tcrop):
    body = f'''{kicker(kick, .05, 196)}{head(l1, l2, .1, 236, 62)}
<div {an(.0, "u", .36)} class="hz-abs" style="left:0;top:0;width:1080px;height:1920px">{phone_frame("ph", src, 1.34, 540, 420)}</div>
{crop}<div class="q-sample" style="left:90px;top:1700px">SAMPLE DATA</div>'''
    scene(name, body, f"function custom(t){{svgSeek('ph',t-{t0});svgSeek('dc',99)}}")


def s11():
    chat_scene("s11", "Labour · attendance", "WhatsApp par", "ek click mein attendance", "t_att", .3,
               dash_crop("dc", 1160, 200, 404, 156, 1.5, 213, 1340, 1.9), 1.9)


def s12():
    chat_scene("s12", "Store · maal inward", "Kitna maal aaya,", "ek input", "t_inw", .25,
               dash_crop("dc", 1112, 692, 440, 56, 2.0, 76, 1440, 2.25, "Dashboard · Live Alerts"), 2.25)


def s13():
    chat_scene("s13", "Supervisor · machine se", "Aaj ki production,", "ek input update", "t_prod", .3, "", 0)


def s14():
    kf = [(0, 950, 490, .76), (1.9, 950, 490, .76), (2.4, 520, 445, 2.15), (3.3, 520, 445, 2.15), (3.75, 940, 445, 2.15), (4.3, 940, 445, 2.15),
          (4.75, 1362, 277, 2.15), (5.15, 1362, 277, 2.15), (5.6, 1332, 712, 2.0), (6.75, 1332, 712, 2.0), (7.25, 950, 490, .76), (9, 950, 490, .76)]
    body = f'''{kicker("Hivon ERP · live status", .05)}{head("Poori factory,", "ek single dashboard", .12, 296, 80)}
<div class="q-card" {an(.1, "u", .36)} style="left:40px;top:540px;width:1000px;height:720px;border-radius:36px"><div class="q-vp" style="left:0;top:0;width:1000px;height:720px"><iframe id="db" src="/assets2/t_dash.svg" width="1600" height="900"></iframe></div></div>
<div id="lab" class="q-chip" style="left:90px;top:1320px;font-size:44px;background:{T};color:#fff;padding:20px 40px"></div>
{line(f'Woh bhi <b style="color:{A}">WhatsApp ke through</b>', 6.96, 1470, 46)}<div class="q-sample" style="left:90px;top:1580px">SAMPLE DATA</div>'''
    cj = f"""const KF={json.dumps(kf)};const LB=[[2.3,'Kitni production hui'],[3.6,'Kitni inventory hai'],[4.65,'Kitne log hain'],[5.5,'Machine M-4: abhi-abhi update'],[7.0,'']];
function custom(t){{svgSeek('db',Math.max(0,t-0.15)*2);
 let i=0;while(i<KF.length-2&&t>=KF[i+1][0])i++;const a=KF[i],b=KF[i+1];let p=E.cl((t-a[0])/(b[0]-a[0]));p=p<.5?4*p*p*p:1-Math.pow(-2*p+2,3)/2;
 const cx=a[1]+(b[1]-a[1])*p,cy=a[2]+(b[2]-a[2])*p,s=a[3]+(b[3]-a[3])*p;
 document.getElementById('db').style.transform=`translate(${{500-cx*s}}px,${{360-cy*s}}px) scale(${{s}})`;
 let l='';for(const [tt,x] of LB)if(t>=tt)l=x;const e=document.getElementById('lab');e.textContent=l;e.style.opacity=l?1:0;}}"""
    scene("s14", body, cj)


def s15():
    body = f'''{kicker("Ye sab chaalu hota hai", .1, 560)}
<div class="hz-abs" {an(1.4, "pop", .34)} style="left:80px;top:640px;font:900 240px Inter;letter-spacing:-12px;color:{T}">₹15,000</div>
<div class="hz-abs" {an(1.9, "u", .34)} style="left:92px;top:920px;font:700 72px Inter;letter-spacing:-2px;color:{A}">ke mahine se</div>'''
    scene("s15", body)


def s16():
    fc, fj = face_card(230, 900, 6.72, 11.6, vy=-190)
    body = f'''{fc}{head("Apni factory ka", "custom WhatsApp ERP?", .52, 1190, 76)}
<div class="q-line" {an(.8, "fade", .3)} style="top:1380px;font-size:38px;opacity:.75">₹15,000 ke mahine se shuru</div>
<div class="hz-abs" {an(3.02, "u", .36)} style="left:90px;top:1480px;background:{CTA};color:{NAVY};border-radius:999px;padding:28px 50px;font:800 50px Inter;letter-spacing:-1px;z-index:9">WhatsApp pe DM karo ↓</div>
<div class="hz-abs" {an(.3, "fade", .3)} style="right:90px;top:1680px;font:800 50px Inter;letter-spacing:-1px;color:{T}">hivon<span style="color:{CTA}">.</span></div>'''
    scene("s16", body, fj + "function custom(t){faceSeek(t)}")


if __name__ == "__main__":
    prep_assets()
    fs = [s01, s02, s03, s04, s05, s06, s07, s08, s09, s10, s11, s12, s13, s14, s15, s16]
    only = sys.argv[1:]
    for f in fs:
        if not only or f.__name__ in only: f()
    sc = [list(x) for x in SCENES]; sc[-1][2] = 1494
    json.dump(sc, open(f"{OUT}/scenes.json", "w"))
    print("ok")
