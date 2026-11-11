"""Final Reel scenes (Storyboard A, Comic Panel Pop). One HTML per scene with seek(t). SAMPLE data."""
import sys, os, json
sys.path.insert(0, os.path.dirname(__file__))
from comp import *
from frames2 import D_CSS, dots, burst, speed, zig, halves, svg, PINK, MINT, AMB, G, T, A, PR, C, CTA, NAVY
from extras import mini_phone, monitor

OUT = os.path.join(os.path.dirname(__file__), "..", "final", "scenes")
os.makedirs(OUT, exist_ok=True)
BG = G + ";" + dots('19,32,27', .07, 22)
FPS = 25
# (name, start_frame, end_frame)
SCENES = [("s01", 0, 56), ("s02", 56, 149), ("s03", 149, 254), ("s04", 254, 352), ("s05", 352, 430), ("s06", 430, 512),
          ("s07", 512, 597), ("s08", 597, 724), ("s09", 724, 798), ("s10", 798, 861), ("s11", 861, 928), ("s12", 928, 998),
          ("s13", 998, 1104), ("s14", 1104, 1304), ("s15", 1304, 1367), ("s16", 1367, 1495)]

ENGINE = """
const E={out:p=>1-Math.pow(1-p,3),back:p=>{const c=1.9;return 1+(c+1)*Math.pow(p-1,3)+c*Math.pow(p-1,2)},cl:(v)=>Math.min(1,Math.max(0,v))};
function seek(t){
 document.querySelectorAll('[data-in],[data-float]').forEach(el=>{
  const ds=el.dataset,a=ds.in===undefined?-1:+ds.in,d=+(ds.d||0.3),fx=ds.fx||'pop';
  const p=E.cl((t-a)/d); let op=p>0?1:0,tr='';
  if(fx=='pop'){tr=`scale(${p<=0?0.001:E.back(p)})`;op=Math.min(1,p*3)}
  else if(fx=='fade'){op=p}
  else if(fx=='l'){tr=`translateX(${(1-E.out(p))*-1100}px)`}
  else if(fx=='r'){tr=`translateX(${(1-E.out(p))*1100}px)`}
  else if(fx=='u'){tr=`translateY(${(1-E.out(p))*1400}px)`}
  else if(fx=='dn'){tr=`translateY(${(1-E.out(p))*-900}px)`}
  else if(fx=='stamp'){tr=`scale(${1+(1-E.out(p))*1.4})`;op=Math.min(1,p*2.5)}
  if(ds.out!==undefined){const q=E.cl((t-(+ds.out))/(+(ds.od||0.5)));
    if(ds.ofx=='fall'){tr+=` translate(${q*q*120}px,${q*q*1300}px) rotate(${q*50}deg)`}
    else if(ds.ofx=='dim'){op*=1-q*0.72}
    else op*=1-q;}
  if(ds.float!==undefined){const f=+ds.float;tr+=` translate(${Math.sin(t*1.7+f)*7}px,${Math.cos(t*1.3+f*2)*9}px) rotate(${Math.sin(t*1.1+f)*2.5}deg)`}
  if(ds.shake!==undefined&&t>a){const k=Math.max(0,1-(t-a)/0.9);tr+=` rotate(${Math.sin(t*60)*5*k}deg)`}
  el.style.opacity=op; el.style.transform=tr+' '+(ds.base||'');
 });
 if(window.custom) custom(t);
}
"""
ANIM_CSS = "[data-in],[data-float]{transform-box:fill-box;transform-origin:center;will-change:transform}"


def an(t=0, fx="pop", d=.3, base="", fl=None, out=None, ofx=None, od=None, shake=False):
    s = f'data-in="{t}" data-fx="{fx}" data-d="{d}"'
    if base: s += f' data-base="{base}"'
    if fl is not None: s += f' data-float="{fl}"'
    if out is not None: s += f' data-out="{out}"'
    if ofx: s += f' data-ofx="{ofx}"'
    if od: s += f' data-od="{od}"'
    if shake: s += ' data-shake="1"'
    return s


def scene(name, body, bg=BG, custom="", css=""):
    html = f'<!doctype html><html><head><meta charset="utf-8"><style>{BASE_CSS}{D_CSS}{ANIM_CSS}{css}</style></head><body style="background:{bg}">{body}<script>{ENGINE}{custom}\nseek(0);</script></body></html>'
    open(f"{OUT}/{name}.html", "w").write(html)


def cap(text, x, y, t, rot=-2, fs=46, bg=AMB, col=T, fx="pop", extra=""):
    return f'<div class="cap" {an(t, fx, base=f"rotate({rot}deg)")} style="left:{x}px;top:{y}px;font-size:{fs}px;background:{bg};color:{col};white-space:nowrap;{extra}">{text}</div>'


def bub(text, x, y, t, fs=38, tl=70, extra=""):
    return f'<div class="bub" {an(t)} style="left:{x}px;top:{y}px;font-size:{fs}px;--tl:{tl}px;transform-origin:{tl}px 100%;{extra}">{text}</div>'


def sfx(text, x, y, t, fs=96, rot=-10, col=PR, shake=False):
    return f'<div class="sfx" {an(t, "stamp", .25, base=f"rotate({rot}deg)", shake=shake)} style="left:{x}px;top:{y}px;font-size:{fs}px;color:{col}">{text}</div>'


def G_(inner, t=0, fx="pop", **kw):
    return f'<g {an(t, fx, **kw)}>{inner}</g>'


def title(l1, l2, t=.15, top=300, fs=104, inv=True, col2=None):
    s2 = f'<span style="background:{T};color:#fff;padding:0 18px">{l2}</span>' if inv else f'<span style="color:{col2 or A}">{l2}</span>'
    return f'<div class="hz-abs" {an(t, "l", .28)} style="left:100px;top:{top}px;font:900 {fs}px Inter;letter-spacing:-3.5px;line-height:1;color:{T};z-index:7">{l1}<br>{s2}</div>'


def face_panel(top=250, h=1330, hg0=0.0, hgmax=11.6, vy=-140):
    return f'''<div class="cp" {an(0, "pop", .22)} style="left:50px;top:{top}px;width:980px;height:{h}px;background:#cfdcd1">
<img id="hg" style="position:absolute;left:-8px;top:{vy}px;width:980px;height:1742px" src="../hg/0001.jpg"></div>''', f'''
window.custom0=function(t){{const n=Math.min(Math.round({hgmax}*25),Math.max(0,Math.round(({hg0}+t)*25)))+1;const i=document.getElementById('hg');const s='../hg/'+String(Math.min(291,n)).padStart(4,'0')+'.jpg';if(!i.src.endsWith(s))i.src=s;}};'''


# ------------------------------------------------------------------ scenes
def s01():
    pts = zig(11, amp=58, step=150); L, R = halves(pts, 13)
    books = ''.join(f'<rect x="{60+(i%2)*14}" y="{1470-i*46}" width="{200-(i%3)*18}" height="46" rx="4" fill="{["#B5483F","#D9A79E","#C96D62","#E4C2BB"][i%4]}" stroke="{T}" stroke-width="6"/>' for i in range(5))
    left = monitor(70, 540) + books + person("owner", "comic", 250, 1130, 1.25, pose="head")
    right = mini_phone(690, 520, 1, 5) + person("supervisor", "comic", 650, 1150, 1.25, pose="wave")
    body = f'''<div class="hz-abs" style="inset:0;background:{T}"></div>
<div class="hz-abs" {an(-0.14, "l", .3)} style="inset:0;clip-path:polygon({L});background-color:{PINK};{dots('181,72,63',.2)}">{svg(left)}</div>
<div class="hz-abs" {an(-0.1, "r", .3)} style="inset:0;clip-path:polygon({R});background-color:{MINT};{dots('47,125,87',.2)}">{svg(speed(830, 800, 22, 330, 1500, 'rgba(47,125,87,.12)') + right)}</div>
{cap("OTHER ERP", 60, 270, .3, -3, 54, "#fff", PR)}{cap("WHATSAPP ERP", 572, 270, .42, 2, 44, "#fff", A)}
{svg(G_(burst(540, 930, 215, 140, 14, AMB, T, 9, .1), .82, "stamp", d=.2), z=6)}
<div class="hz-abs" {an(.84, "stamp", .2, base="rotate(-6deg)")} style="left:390px;top:850px;width:300px;text-align:center;font:italic 900 150px Inter;color:#fff;-webkit-text-stroke:8px {T};paint-order:stroke fill;text-shadow:9px 9px 0 {T};z-index:7;letter-spacing:-6px">VS</div>
{bub("Yeh kaise<br>chalega?!", 60, 1000, 1.2, 32, 150)}{bub("Ho gaya!", 820, 1040, 1.36, 32, 30, "padding:16px 26px")}
{cap("for MANUFACTURING", 215, 1650, 1.5, -1.5, 58, T, "#fff", extra=f"box-shadow:8px 8px 0 {A}")}'''
    scene("s01", body, G)


def s02():
    fp, cj = face_panel(hg0=0.02, hgmax=3.70)
    body = f'''{fp}{cap(f'hivon<span style="color:{CTA}">.</span> WhatsApp ERP', 30, 190, .1, -2, 42, "#fff")}
{cap(f'Factory mein ERP <span style="color:{PR}">fail</span> kyun?', 90, 1500, .5, 1, 50, "#fff")}
{svg(G_(burst(850, 1300, 150, 98, 13, AMB, T, 8, .1), 2.68, "stamp", d=.22), z=8)}
<div class="hz-abs" {an(2.7, "stamp", .22, base="rotate(-8deg)")} style="left:740px;top:1232px;width:220px;text-align:center;font:italic 900 58px Inter;line-height:.95;color:{T};z-index:9">3 bade<br>reason</div>'''
    scene("s02", body, custom=cj + "function custom(t){custom0(t)}")


def s03():
    papers = ''.join(G_(f'<g transform="translate({x},{y}) rotate({r})" stroke="{T}" stroke-width="6"><rect width="150" height="190" fill="#fff"/>{"".join(f"<line x1=\"22\" y1=\"{38+k*28}\" x2=\"{120-(k%2)*36}\" y2=\"{38+k*28}\" stroke-width=\"5\" opacity=\".45\"/>" for k in range(5))}</g>', .25 + i * .08, fl=i * 1.3)
                     for i, (x, y, r) in enumerate([(90, 560, -20), (820, 520, 16), (150, 1010, 14), (800, 980, -12), (470, 470, 5)]))
    reg = G_(f'<g transform="translate(610,1290) rotate(7)" stroke="{T}" stroke-width="7"><rect width="340" height="200" rx="6" fill="{PINK}"/><line x1="170" y1="0" x2="170" y2="200"/></g>', .5, fl=2)
    ph = f'<g {an(.6, "pop", shake=True)}><g transform="translate(150,810) rotate(-16)"><rect width="120" height="200" rx="20" fill="{T}"/><rect x="10" y="12" width="100" height="176" rx="12" fill="#CFE9D6"/></g></g>'
    body = f'''<div class="cp" {an(0, "r", .24)} style="left:50px;top:230px;width:980px;height:1320px;background-color:{PINK};{dots('181,72,63',.18)}">
{svg(speed(540, 780, 30, 380, 1500, 'rgba(181,72,63,.13)') + papers + ph + reg + G_(person("owner", "comic", 330, 640, 1.9, pose="head"), .2), w=980, h=1320)}</div>
{cap("REASON 1", 30, 190, .05)}{title("Koi system", "hi nahi", .3)}
{sfx("TRING!", 60, 960, .62, 84, -14, shake=True)}{bub("Register<br>kahan hai?!", 560, 690, 1.3, 38, 60)}
<div class="cap" {an(2.3, "stamp", .22, base="rotate(1deg)")} style="left:70px;top:1500px;font-size:38px;background:#fff;white-space:nowrap">Software laga bhi doge… <span style="color:{PR}">phir bhi FAIL</span></div>'''
    scene("s03", body)


def s04():
    crew = ''.join(f'<g {an(.2 + i*.08, "pop", **({} if i == 2 else dict(out=1.0 + i*.16, ofx="dim", od=.4)))}>{person("supervisor" if i == 2 else "worker", "comic", 20+i*186, 520, 1.05)}</g>' for i in range(5))
    body = f'''<div class="cp" {an(0, "r", .24)} style="left:50px;top:230px;width:980px;height:1320px;background-color:{PINK};{dots('181,72,63',.18)}">
{svg(speed(490, 700, 28, 340, 1500, 'rgba(181,72,63,.12)') + crew + G_(burst(490, 400, 130, 86, 12, AMB, T, 7), 2.0, "stamp", d=.2) + f'<text {an(2.02, "stamp", .2)} x="490" y="416" text-anchor="middle" font-family="Inter" font-weight="900" font-size="44" fill="{T}">skilled</text>', w=980, h=1320)}</div>
{cap("REASON 2", 30, 190, .05)}{title("Skilled manpower", "bahut kam", .3, fs=92)}
<div class="cap" {an(2.7, "stamp", .22, base="rotate(1deg)")} style="left:90px;top:1500px;font-size:40px;background:#fff;white-space:nowrap">SME manufacturing ki asli dikkat</div>'''
    scene("s04", body)


def s05():
    cal = ''.join(f'<g {an(.15 + i*.05, "pop", out=.55 + i*.38, ofx="fall", od=.7)}><g transform="translate({70+i*140},{520+(i%2)*60}) rotate({-8+i*4})" stroke="{T}" stroke-width="6"><rect width="150" height="180" fill="#fff"/><rect width="150" height="46" fill="{PR}"/><text x="75" y="132" text-anchor="middle" font-family="Inter" font-weight="900" font-size="58" fill="{T}" stroke="none">M{i+1}</text></g></g>' for i in range(6))
    body = f'''<div class="cp" {an(0, "r", .24)} style="left:50px;top:230px;width:980px;height:1320px;background-color:{PINK};{dots('181,72,63',.18)}">
{svg(cal + G_(person("worker", "comic", 370, 800, 1.5, pose="shrug"), .2), w=980, h=1320)}
<div id="lamba" style="position:absolute;left:30px;top:760px;font:italic 900 124px Inter;letter-spacing:-5px;color:{PR};-webkit-text-stroke:6px {T};paint-order:stroke fill;transform-origin:left center;white-space:nowrap;opacity:.0">LAMBAAAAAAAAAA</div></div>
{cap("REASON 3", 30, 190, .05)}{title("Implementation", "time", .3, fs=96)}
<div class="cap" {an(2.3, "stamp", .22, base="rotate(1deg)")} style="left:90px;top:1500px;font-size:40px;background:#fff;white-space:nowrap">Bahut lamba kheech jaata hai</div>'''
    scene("s05", body, custom="function custom(t){const e=document.getElementById('lamba');const p=E.out(E.cl((t-1.5)/1.5));e.style.opacity=t>1.5?1:0;e.style.transform=`translateX(${(1-p)*900-200*p}px) rotate(-4deg)`;}")


def big_phone():
    return f'''<g transform="translate(360,520) rotate(-7)"><rect x="14" y="14" width="360" height="680" rx="56" fill="{T}"/><rect width="360" height="680" rx="56" fill="#0D0D0D" stroke="{T}" stroke-width="8"/><rect x="20" y="20" width="320" height="640" rx="38" fill="#EAE6DF"/>
<rect x="20" y="20" width="320" height="76" fill="#F6F6F6"/><circle cx="66" cy="60" r="22" fill="#0D0D0D"/><text x="66" y="67" text-anchor="middle" font-family="Inter" font-weight="800" font-size="17" fill="#fff">HI</text><text x="100" y="67" font-family="Inter" font-weight="700" font-size="21" fill="#101729">Hivon Automations</text>
<rect x="40" y="124" width="250" height="100" rx="14" fill="#fff"/><text x="58" y="162" font-family="Inter" font-weight="800" font-size="22" fill="#101729">🏭 Production Update</text><rect x="58" y="182" width="170" height="12" rx="6" fill="#9aa0a6"/>
<rect x="40" y="227" width="250" height="48" fill="#EAF4FF"/><text x="165" y="259" text-anchor="middle" font-family="Inter" font-weight="700" font-size="21" fill="#1D8FF5">📝 Entry karein</text>
<rect x="130" y="304" width="190" height="60" rx="14" fill="#E2FBCB"/><text x="148" y="342" font-family="Inter" font-weight="600" font-size="21" fill="#101729">M-4 · 120 pcs</text>
<rect x="40" y="392" width="260" height="110" rx="14" fill="#fff"/><text x="58" y="434" font-family="Inter" font-weight="800" font-size="24" fill="{A}">✅ Logged!</text><rect x="58" y="454" width="180" height="12" rx="6" fill="#9aa0a6"/><rect x="58" y="474" width="120" height="12" rx="6" fill="#9aa0a6"/></g>'''


def s06():
    ticks = ''.join(cap(f'<span style="color:{A}">✔</span> {t}', x, y, 1.5 + i * .22, r, 36, "#fff") for i, (x, y, r, t) in enumerate([(70, 1290, -3, "System"), (390, 1330, 2, "Manpower"), (760, 1290, -2, "Time")]))
    body = f'''<div class="cp" {an(0, "pop", .22)} style="left:50px;top:420px;width:980px;height:820px;background-color:{MINT};{dots('47,125,87',.2)}">{svg(speed(490, 400, 34, 300, 1400, 'rgba(47,125,87,.16)'), w=980, h=820)}</div>
{svg(G_(big_phone(), .68, "pop", d=.34, fl=.5), z=6)}
{cap("HIVON AUTOMATION", 60, 200, .1, -2, 40, "#fff")}
<div class="hz-abs" {an(1.5, "stamp", .24)} style="left:60px;top:290px;font:italic 900 112px Inter;letter-spacing:-4px;color:{A};-webkit-text-stroke:7px {T};paint-order:stroke fill;text-shadow:8px 8px 0 {T};z-index:7">WhatsApp ERP</div>
{sfx("POP!", 700, 560, .78, 104, 10, AMB)}{ticks}
<div class="hz-abs" {an(.2, "fade", .3)} style="left:70px;top:1470px;right:70px;font:800 50px Inter;line-height:1.15;color:{T}">Yahi teeno cheezein<br><span style="background:{A};color:#fff;padding:0 14px">solve</span> karta hai</div>'''
    scene("s06", body)


def machine_svg(x, y, s=1, label="M-4"):
    return f'''<g transform="translate({x},{y}) scale({s})"><g stroke="{T}" stroke-width="7" stroke-linejoin="round"><rect width="330" height="260" rx="14" fill="#B9CCBE"/><rect x="28" y="30" width="130" height="90" rx="8" fill="#fff"/>
<circle cx="240" cy="120" r="62" fill="#fff"/><circle cx="240" cy="120" r="18" fill="{T}"/><rect x="60" y="260" width="210" height="60" fill="#8FA596"/><rect x="270" y="28" width="36" height="26" rx="6" fill="{CTA}"/></g>
<text x="32" y="232" font-family="Inter" font-weight="900" font-size="44" fill="{T}">{label}</text></g>'''


def s07():
    body = f'''<div class="cp" {an(0, "r", .24)} style="left:50px;top:230px;width:980px;height:1320px;background-color:{MINT};{dots('47,125,87',.18)}">
{svg(G_(machine_svg(560, 520, 1.1, "M-1"), .15) + G_(machine_svg(80, 420, .8, "M-2"), .22) + G_(person("owner", "comic", 420, 760, 1.6, pose="point"), .3) + G_(person("store", "comic", 90, 780, 1.6, pose="carry"), .4), w=980, h=1320)}</div>
{cap("HIVON KA TAREEKA", 30, 190, .05, bg="#fff", fs=42)}{title("Pehle aapka", "business seekhte hain", .3, fs=78, inv=False)}
{bub("Yeh hamara<br>process hai", 560, 760, .9, 36, 60)}
<div class="cap" {an(1.78, "stamp", .22, base="rotate(1deg)")} style="left:70px;top:1500px;font-size:37px;background:#fff;white-space:nowrap">Aapko hamara software <span style="color:{A}">na seekhna pade</span></div>'''
    scene("s07", body)


def s08():
    rows = ["Process samjha", "SOP likha", "Aapne approve kiya"]
    rw = ''.join(f'''<div style="display:flex;gap:24px;align-items:center;margin:26px 0"><div style="width:76px;height:76px;border:7px solid {T};background:#fff;flex:none;position:relative"><svg {an(.6 + i*.55, "stamp", .2)} width="62" height="62" style="position:absolute;left:0;top:0"><path d="M8 32 l16 16 l30 -38" stroke="{A}" stroke-width="11" fill="none" stroke-linecap="round"/></svg></div><div style="font:800 50px Inter;letter-spacing:-1px;color:{T}">{t}</div></div>''' for i, t in enumerate(rows))
    body = f'''<div class="cp" {an(0, "r", .24)} style="left:50px;top:230px;width:980px;height:1320px;background-color:{MINT};{dots('47,125,87',.18)}">
<div {an(.3, "pop")} style="position:absolute;left:70px;top:330px;width:820px;background:#fff;border:8px solid {T};box-shadow:12px 12px 0 {T};padding:30px 44px;transform-origin:center"><div style="font:900 84px Inter;color:{A};letter-spacing:-2px">SOP</div>{rw}</div>
{svg(G_(person("owner", "comic", 80, 880, 1.25, pose="wave"), .5) + G_(person("store", "comic", 640, 880, 1.25, pose="point", flip=True), .6), w=980, h=1320)}</div>
{cap("HIVON KA TAREEKA", 30, 190, .05, bg="#fff", fs=42)}{title("Phir aapke", "SOPs banaate hain", .3, fs=84, inv=False)}
{bub("Yeh chalega!", 240, 1040, 3.7, 38, 60)}
<div class="cap" {an(2.7, "stamp", .22, base="rotate(1deg)")} style="left:60px;top:1500px;font-size:35px;background:#fff;white-space:nowrap">Jo <span style="color:{A}">small-medium factory</span> mein implement ho sakein</div>'''
    scene("s08", body)


def s09():
    fp, cj = face_panel(hg0=3.77, hgmax=6.66)
    body = f'''{fp}{cap("Toh aap bologe…", 30, 190, .1, -2, 44, "#fff")}
{bub(f'Mera staff software<br><span style="color:{PR}">seekhega nahi!</span>', 150, 1400, .74, 46, 120, "border-radius:70px;padding:28px 40px")}'''
    scene("s09", body, custom=cj + "function custom(t){custom0(t)}")


def s10():
    man = f'''<g transform="translate(300,560) rotate(-6)" stroke="{T}" stroke-width="8"><rect x="20" y="20" width="440" height="560" rx="10" fill="{T}"/><rect width="440" height="560" rx="10" fill="#E4C2BB"/><rect width="60" height="560" fill="{PR}"/>
<text x="250" y="220" text-anchor="middle" font-family="Inter" font-weight="900" font-size="64" fill="{T}" stroke="none">USER</text><text x="250" y="300" text-anchor="middle" font-family="Inter" font-weight="900" font-size="64" fill="{T}" stroke="none">MANUAL</text></g>'''
    cross = f'<g {an(.5, "stamp", .2)}><path d="M260 560 L800 1180 M800 560 L260 1180" stroke="{PR}" stroke-width="46" stroke-linecap="round"/><path d="M260 560 L800 1180 M800 560 L260 1180" stroke="{T}" stroke-width="62" stroke-linecap="round" opacity="0"/></g>'
    body = f'''{svg(f'<g {an(.05, "pop", out=1.15, od=.3)}>{man}{cross}</g>', z=3)}
{cap("STAFF KE LIYE", 30, 190, .05, bg="#fff", fs=42)}{title("Kuch seekhne ki", "zaroorat nahi", .15, fs=96)}
{svg(G_(mini_phone(330, 620, 1.35, -4), 1.2, "u", d=.36), z=5)}
<div class="hz-abs" {an(1.62, "stamp", .22)} style="left:120px;top:1460px;font:italic 900 96px Inter;letter-spacing:-3.5px;color:{A};-webkit-text-stroke:7px {T};paint-order:stroke fill;text-shadow:8px 8px 0 {T};z-index:8">Sab WhatsApp par</div>'''
    scene("s10", body)


def s11():
    chat = ('<div class="hz-date">Today</div>' + tin("🕘 Attendance", "Good morning! Aaj ki attendance lagayein.", "09:00") +
            '<div class="hz-qr"><div id="qr1">✅ Check-in</div><div>🏖️ Leave</div></div>' +
            f'<div id="o1" style="align-self:flex-end;opacity:0">{tout("✅ Check-in", "09:01")}</div>' +
            f'<div id="o2" style="opacity:0">{tin("✅ Attendance Marked!", "👤 Worker 12 · Shift A<br>🕘 In time: <b>09:01</b>", "09:01")}</div>')
    k = kpi("Today Present", '<span id="pn">93</span>', "checked in · Shift A", DB['green'], "🗓️", DB['mint'], f"position:absolute;left:0;top:0;width:430px;border:6px solid {T};box-shadow:10px 10px 0 {T}")
    body = f'''<div class="cp" {an(0, "r", .24)} style="left:50px;top:230px;width:980px;height:1400px;background-color:{MINT};{dots('47,125,87',.18)}">{svg(G_(person("worker", "comic", 40, 880, 1.45, pose="phone"), .2), w=980, h=1400)}</div>
<div {an(.1, "u", .34)} class="hz-abs" style="left:0;top:0;width:1080px;height:1920px;z-index:6">{phone(430, 330, 1.3, chat, extra=f"box-shadow:14px 14px 0 {T}")}</div>
<svg id="tap" class="hz-abs" style="left:560px;top:690px;z-index:9;opacity:0" width="200" height="200"><circle cx="100" cy="100" r="60" fill="none" stroke="{T}" stroke-width="10"/></svg>
{cap("Labour · attendance", 30, 190, .05)}
<div {an(1.76, "l", .3)} class="hz-abs" style="left:70px;top:420px;z-index:8;width:440px;height:230px">{k}</div>
{sfx("EK CLICK!", 70, 1490, 1.3, 84, -8, CTA)}{SAMPLE_(90, 1670)}'''
    cj = """function custom(t){const tp=1.16;document.getElementById('qr1').className=t>tp?'hz-on':'';
const tap=document.getElementById('tap');const p=E.cl((t-tp)/0.35);tap.style.opacity=(t>tp&&p<1)?1-p:0;tap.style.transform=`scale(${0.4+p})`;
document.getElementById('o1').style.opacity=t>tp+0.12?1:0;document.getElementById('o2').style.opacity=t>tp+0.4?1:0;
document.getElementById('pn').textContent=t>2.05?'94':'93';}"""
    scene("s11", body, custom=cj)


SAMPLE_ = lambda x, y: f'<div class="hz-sample" style="left:{x}px;top:{y}px;z-index:9">SAMPLE DATA</div>'


def s12():
    truck = f'''<g stroke="{T}" stroke-width="7" stroke-linejoin="round"><rect x="0" y="0" width="330" height="200" rx="8" fill="#C7D6CA"/><path d="M330 60 h110 l60 70 v70 h-170z" fill="{A}"/><rect x="350" y="80" width="80" height="50" fill="#fff"/>
<circle cx="90" cy="210" r="44" fill="{T}"/><circle cx="90" cy="210" r="16" fill="#fff"/><circle cx="410" cy="210" r="44" fill="{T}"/><circle cx="410" cy="210" r="16" fill="#fff"/></g>
<text x="165" y="118" text-anchor="middle" font-family="Inter" font-weight="900" font-size="40" fill="{T}">STEEL ROD</text>'''
    chat = '<div class="hz-date">Today</div>' + tin("🚚 Material Inward", "Gate par maal aaya hai.<br>Entry karein.", "10:14") + qr("📝 Inward entry", on="📝 Inward entry")
    sheet = flow("Inward Entry", "Hivon Automations · sample", [("Item", "Steel rod 12mm", True, False), ("Quantity", "500 kg", False, True), ("Vendor", "Vendor A", True, False)])
    al = alerts([("Inward: Steel rod 500 kg", "Gate entry • 10:15", "DONE")], 0, title="Live Alerts", extra=f"width:560px;border:6px solid {T};box-shadow:10px 10px 0 {T}")
    body = f'''<div class="cp" {an(0, "r", .24)} style="left:50px;top:230px;width:980px;height:1400px;background-color:{MINT};{dots('47,125,87',.18)}">
{svg(f'<g {an(.1, "l", .5)}><g transform="translate(30,1010) scale(.82)">{truck}</g></g>' + G_(person("store", "comic", 60, 420, 1.2, pose="phone"), .3) + f'<path d="M0 1215 h980" stroke="{T}" stroke-width="8"/>', w=980, h=1400)}</div>
<div {an(.5, "u", .34)} class="hz-abs" style="left:0;top:0;width:1080px;height:1920px;z-index:6">{phone(470, 330, 1.22, chat, sheet, extra=f"box-shadow:14px 14px 0 {T}")}</div>
{cap("Maal andar aaya · ek input", 30, 190, .05, fs=42)}
<div {an(2.18, "stamp", .22, base="rotate(-2deg)")} class="hz-abs" style="left:60px;top:1330px;z-index:9">{al}</div>{SAMPLE_(90, 1670)}'''
    scene("s12", body)


def s13():
    ch, sh = chat_production("flow"); ch2, _ = chat_production("done")
    body = f'''<div class="cp" {an(0, "r", .24)} style="left:50px;top:230px;width:980px;height:1400px;background-color:{MINT};{dots('47,125,87',.18)}">{svg(G_(machine_svg(40, 560), .15) + G_(person("supervisor", "comic", 70, 860, 1.25, pose="phone"), .25), w=980, h=1400)}</div>
<div {an(.2, "u", .34)} class="hz-abs" style="left:0;top:0;width:1080px;height:1920px;z-index:6"><div id="phA">{phone(420, 330, 1.34, ch, sh, extra=f"box-shadow:14px 14px 0 {T}")}</div><div id="phB" style="opacity:0">{phone(420, 330, 1.34, ch2, "", extra=f"box-shadow:14px 14px 0 {T}")}</div></div>
{cap("Supervisor · machine se", 30, 190, .05)}{bub("Aaj ki<br>production?", 60, 390, .7, 36, 120, "padding:18px 26px")}
{sfx("EK INPUT!", 70, 1500, 3.72, 84, -8, CTA)}{SAMPLE_(90, 1660)}'''
    cj = """const F=[...document.querySelectorAll('#phA .hz-fi')];F.forEach(f=>{f.dataset.v=f.firstChild.textContent;});
function custom(t){const ts=[1.28,1.88,2.48];F.forEach((f,i)=>{f.firstChild.textContent=t>ts[i]?f.dataset.v:'\\u00a0';f.className='hz-fi'+((t>ts[i]-0.3&&t<(ts[i+1]||9)-0.3)?' hz-act':'');});
const b=document.querySelector('#phA .hz-btn');b.style.transform=(t>3.44&&t<3.6)?'scale(.94)':'';b.style.filter=(t>3.44&&t<3.6)?'brightness(.85)':'';
document.getElementById('phA').style.opacity=t>3.62?0:1;document.getElementById('phB').style.opacity=t>3.62?1:0;}"""
    scene("s13", body, custom=cj)


def s14():
    bd = "border:5px solid " + T
    k = (kpi("Today Production", '<span class="cn" data-v="1240" data-t="2.2">0</span>', "pcs · Shift A", DB['deep'], "⚙️", DB['mint'], f"position:absolute;left:40px;top:140px;width:435px;{bd}") +
         kpi("Inventory", '<span class="cn" data-v="312" data-t="3.4">0</span>', "SKUs in stock", DB['ink'], "📦", "#F1F2F5", f"position:absolute;left:495px;top:140px;width:435px;{bd}") +
         kpi("Today Present", '<span class="cn" data-v="94" data-t="4.3">0</span>', "checked in", DB['green'], "🗓️", DB['mint'], f"position:absolute;left:40px;top:365px;width:435px;{bd}") +
         kpi("Pending Inward", "3", "gate entries", DB['amber'], "🚚", "#FDF1DD", f"position:absolute;left:495px;top:365px;width:435px;{bd}"))
    al = alerts(ALERT_ROWS[:3], 0, extra=f"position:absolute;left:40px;top:595px;width:890px;{bd}").replace('<div class="hd-row hd-hl">', f'<div class="hd-row hd-hl" {an(4.9, "l", .3)}>', 1)
    body = f'''<div id="stage" style="position:absolute;inset:0;transform-origin:540px 1150px">
<div class="cp" {an(0, "r", .24)} style="left:50px;top:230px;width:980px;height:1090px;background:{DB['canvas']}">
<div style="position:absolute;left:40px;top:50px;font:800 42px Inter;color:{T}">Hivon ERP <span style="font-weight:500;color:{DB['muted']};font-size:30px">· Management Overview</span></div>{k}{al}</div>
{svg(G_(burst(900, 800, 90, 58, 11, AMB, T, 7, .2), 5.1, "stamp", d=.2), z=7)}
<div class="hz-abs" {an(5.12, "stamp", .2, base="rotate(-10deg)")} style="left:848px;top:774px;font:italic 900 44px Inter;color:{T};z-index:8">NEW!</div>
{cap("Live status · ek dashboard", 30, 170, .05)}
{svg(G_(person("owner", "comic", 90, 1290, 1.35, pose="wave"), 5.9), z=6)}
{bub(f'Sab kuch <span style="color:{A}">live</span><br>dikh raha hai!', 400, 1380, 6.1, 40, 40, "border-radius:50px")}
<div class="cap" {an(6.96, "stamp", .22, base="rotate(1deg)")} style="left:380px;top:1590px;font-size:38px;background:{T};color:#fff;white-space:nowrap;box-shadow:7px 7px 0 {A}">Woh bhi WhatsApp se</div>
{SAMPLE_(90, 1680)}</div>'''
    cj = """function custom(t){document.querySelectorAll('.cn').forEach(e=>{const p=E.cl((t-(+e.dataset.t-0.5))/0.5);e.textContent=Math.round(+e.dataset.v*E.out(p)).toLocaleString('en-IN');});
const z=E.out(E.cl((t-5.0)/0.4))-E.out(E.cl((t-5.85)/0.35));document.getElementById('stage').style.transform=`scale(${1+z*0.3})`;}"""
    scene("s14", body, custom=cj)


def s15():
    body = f'''<div class="cp" {an(0, "pop", .22)} style="left:50px;top:420px;width:980px;height:900px;background-color:{MINT};{dots('47,125,87',.2)}">{svg(speed(490, 430, 34, 320, 1400, 'rgba(47,125,87,.16)'), w=980, h=900)}</div>
{cap("Ye sab chaalu hota hai", 60, 370, .15, -2, 48, "#fff")}
<div class="hz-abs" {an(1.4, "stamp", .22, base="rotate(-4deg)")} style="left:90px;top:620px;font:italic 900 230px Inter;letter-spacing:-10px;color:{AMB};-webkit-text-stroke:10px {T};paint-order:stroke fill;text-shadow:12px 12px 0 {T};z-index:7">₹15,000</div>
<div class="cap" {an(1.9, "stamp", .2, base="rotate(2deg)")} style="left:380px;top:930px;font-size:64px;background:{T};color:#fff;box-shadow:8px 8px 0 {A}">ke mahine se</div>
{svg(G_(person("supervisor", "comic", 110, 990, 1.3, pose="wave"), .4), z=6)}'''
    scene("s15", body)


def s16():
    fp, cj = face_panel(top=230, h=900, hg0=6.72, hgmax=11.6, vy=-170)
    body = f'''{fp}{cap(f'hivon<span style="color:{CTA}">.</span> WhatsApp ERP', 30, 150, .1, -2, 42, "#fff")}
<div class="bub" {an(.52)} style="left:70px;top:1120px;width:940px;border-radius:70px;padding:44px 50px;text-align:left;--tl:200px;transform-origin:200px 0">
<div style="font:900 66px Inter;letter-spacing:-2px;line-height:1.02">Apni factory ka<br><span style="color:{A}">custom WhatsApp ERP?</span></div>
<div style="font:700 34px Inter;margin-top:16px;opacity:.75">₹15,000/mahine se shuru</div></div>
<div class="hz-abs" {an(3.02, "u", .34, base="rotate(-2deg)")} style="left:190px;top:1500px;background:{CTA};border:7px solid {NAVY};box-shadow:10px 10px 0 {T};padding:26px 44px;font:900 54px Inter;color:{NAVY};z-index:9">WhatsApp pe DM karo ↓</div>'''
    scene("s16", body, custom=cj + "function custom(t){custom0(t)}")


if __name__ == "__main__":
    fs = [s01, s02, s03, s04, s05, s06, s07, s08, s09, s10, s11, s12, s13, s14, s15, s16]
    only = sys.argv[1:]
    for f in fs:
        if not only or f.__name__ in only: f()
    json.dump(SCENES, open(f"{OUT}/scenes.json", "w"))
    print("ok")
