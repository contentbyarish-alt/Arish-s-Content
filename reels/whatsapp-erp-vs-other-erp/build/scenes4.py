"""Final Reel v4: Storyboard C (Keynote Chapters), ad-safe layout (x 65-1015, y 270-1250), complete WhatsApp flows
animated step by step, dashboard updates, running captions. Rendered via file://. SAMPLE data."""
import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from flows import (CSS as FCSS, R, DASH, ROOT, REPLY, LISTI, LINKI, MENU_ROWS, INK, MUT, GRN, DATE, wloc, laptop)
from comp import BASE_CSS, phone, P, svg_defs, person
from scenes import ENGINE, ANIM_CSS, an, SCENES
from scenes3 import GLOBAL_JS, CAPS
from boards import monitor_old, sync_line, C_CSS, C_BG, CH

OUT = ROOT + "/final/scenes4"; os.makedirs(OUT, exist_ok=True)
HG = ROOT + "/final/hg"
G, T, A, PR, C, CTA, NAVY = P['ground'], P['text'], P['accent'], P['problem'], P['card'], P['cta'], P['navy']
SC = [list(x) for x in SCENES]; SC[-1][2] = 1494
START = {n: a / 25 for n, a, b in SC}; DUR = {n: (b - a) / 25 for n, a, b in SC}

CSS = BASE_CSS + ANIM_CSS + FCSS + C_CSS + f"""
body{{background:{C_BG}}}
#stage{{position:absolute;inset:0;transform-origin:0 0}}
.rail{{left:90px;right:90px;top:290px}} .c-h{{left:90px;right:90px}}
#capt{{position:absolute;left:0;right:0;top:1166px;text-align:center;z-index:50}}
#capt span{{display:inline-block;background:{T};color:#fff;font:800 44px Inter;letter-spacing:-.5px;padding:12px 30px;border-radius:20px;box-shadow:0 12px 26px rgba(19,32,27,.22)}}
#cur{{position:absolute;width:60px;height:60px;border-radius:50%;background:rgba(19,32,27,.3);border:4px solid #fff;z-index:40;opacity:0;box-shadow:0 6px 16px rgba(0,0,0,.25)}}
#rp{{position:absolute;width:150px;height:150px;border-radius:50%;border:8px solid {A};z-index:39;opacity:0}}
.ring{{position:absolute;border:5px solid #55B685;border-radius:18px;box-shadow:0 0 0 7px rgba(85,182,133,.22);z-index:12}}
.up{{position:absolute;background:{A};color:#fff;font:800 30px Inter;padding:8px 20px;border-radius:999px;z-index:13;white-space:nowrap}}
.chip{{position:absolute;background:#fff;border-radius:999px;padding:12px 26px;font:700 30px Inter;color:{T};box-shadow:0 8px 20px rgba(19,32,27,.1);white-space:nowrap;z-index:9}}
.w-btn.on{{background:#E4F5EA}}
"""


def deco():
    return (f'<div class="hz-abs" style="left:-60px;top:1300px;width:1200px;height:700px;overflow:hidden;opacity:.22;filter:blur(3px);transform:rotate(-4deg)"><img src="file://{DASH}" style="width:1200px"></div>'
            f'<div class="hz-abs" style="left:0;top:1260px;width:1080px;height:200px;background:linear-gradient(#EEF2EC,rgba(238,242,236,0))"></div>'
            f'<div class="hz-abs" style="left:0;top:0;width:1080px;height:250px;background:linear-gradient(90deg,#E3ECE5,#F3EFE7)"></div>')


MSGJS = """
function msgs(t){document.querySelectorAll('[data-at]').forEach(e=>{const a=+e.dataset.at;e.style.display=t>=a?'flex':'none';const p=E.cl((t-a)/0.25);
 e.style.transform=`translateY(${(1-E.out(p))*24}px) scale(${0.94+0.06*E.out(p)})`;e.style.opacity=Math.min(1,p*2.5);});}
function onAt(id,tt,t,cls){const e=document.getElementById(id);if(e)e.classList.toggle(cls||'on',t>=tt);}
function press(id,tt,t){const e=document.getElementById(id);if(!e)return;const k=t>tt&&t<tt+0.16;e.style.filter=k?'brightness(.85)':'';e.style.transform=k?'scale(.96)':'';}
function faceAt(t,hg0,mx){const i=document.getElementById('hg');if(!i)return;const n=Math.min(Math.round(mx*25),Math.max(0,Math.round((hg0+t)*25)))+1;
 const s='file://"""+HG+"""/'+String(Math.min(291,n)).padStart(4,'0')+'.jpg';if(i.getAttribute('src')!==s)i.setAttribute('src',s);i.style.transform=`scale(${1+0.025*t})`;}
"""


def scene(name, body, js="", nodrift=True):
    html = f'''<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{deco()}
<div id="stage">{body}<div id="cur"></div><div id="rp"></div></div><div id="capt"></div>
<script>window.SCSTART={START[name]};window.SCDUR={DUR[name]};window.NODRIFT={"true" if nodrift else "false"};const CAPS={json.dumps(CAPS, ensure_ascii=False)};
{ENGINE}{GLOBAL_JS}{MSGJS}function sc(t){{if(window.msgs)msgs(t);{js}}}
seek(0);</script></body></html>'''
    open(f"{OUT}/{name}.html", "w").write(html)


def rail(i, t=0):
    return f'<div class="rail" {an(t, "fade", .25)}>' + ''.join(f'<div class="{"on" if k == i else ("done" if k < i else "")}">{"0" + str(k)} {c}</div>' for k, c in enumerate(CH)) + '</div>'


def head(l1, l2, t=.05, top=362, fs=58, col=A):
    return f'<div class="c-h" {an(t, "u", .32)} style="top:{top}px;font-size:{fs}px;letter-spacing:-2px">{l1}<br><span style="color:{col}">{l2}</span></div>'


# ---------- animated WhatsApp messages ----------
def at(t, html):
    return f'<div data-at="{t}" style="display:none;flex:none;align-self:stretch;display:flex;flex-direction:column">{html}</div>'


def tm(title, body, time, btns=(), doc=None):
    b = ''.join(f'<div class="w-btn" id="{bid}">{ic}{l}</div>' for bid, ic, l in btns)
    d = f'<div class="w-doc"><div class="w-pdf">PDF</div><div style="font:500 13.5px Inter">{doc}<div style="font:400 10.5px Inter;color:{MUT}">1 page · pdf</div></div></div>' if doc else ''
    return f'<div class="w-msg"><div class="w-b">{d}<div class="w-t">{title}</div><div class="w-x">{body}</div><div class="w-f">Powered by Hivon Automations<span>{time}</span></div></div>{b}</div>'


def wo(text, time):
    return f'<div class="w-out">{text}<small>{time} <span style="color:#1D8FF5;letter-spacing:-3px">✓✓</span></small></div>'


def listsheet(t_in, t_out, sel_t, send_t, sel="Material Inward"):
    rows = ''.join(f'<div class="w-li"><div>{a}<small>{b}</small></div><div class="w-rad" id="{"rsel" if a == sel else ""}"></div></div>' for a, b in [("Attendance", "Check-in / leave")] + MENU_ROWS[:3])
    return (f'<div class="hz-dim" {an(t_in, "fade", .2, out=t_out, od=.2)}></div><div class="w-list" {an(t_in, "u", .3, out=t_out, od=.2)}><div class="hz-grab"></div><h5>View Options</h5>{rows}<div class="w-send" id="lsend">Send</div></div>',
            f"onAt('rsel',{sel_t},t);press('lsend',{send_t},t);")


def flowsheet(fid, title, fields, t_in, t_out, btn="Submit"):
    fs = ''.join(f'<div class="hz-fl">{l}</div><div class="hz-fi">{v}<span style="color:#9aa0a6">{"▾" if d else ""}</span></div>' for l, v, d in fields)
    return (f'<div class="hz-dim" {an(t_in, "fade", .2, out=t_out, od=.2)}></div><div class="hz-sheet" id="{fid}" {an(t_in, "u", .32, out=t_out, od=.2)}><div class="hz-grab"></div><div class="hz-sh-h"><span>{title}</span><small>✕</small></div>'
            f'<div style="font-size:13px;color:{MUT}">Hivon Automations · sample</div>{fs}<div class="hz-btn" id="{fid}_b" style="background:{GRN}">{btn}</div></div>')


def phone_anim(chat, sheets="", x=70, y=478, s=.72, t=0):
    h = phone(x, y, s, DATE + chat, sheets)
    h = h.replace('<div class="hz-chat">', '<div class="hz-chat" style="justify-content:flex-end">', 1)
    return f'<div {an(t, "u", .38)} class="hz-abs" style="left:0;top:0;width:1080px;height:1920px;z-index:4">{h}</div>'


# ---------- dashboard crops with timed rings ----------
def dc(region, scale, left, top, t=0, ring_t=None, up=None, z=5, fx="pop"):
    x, y, w, h = R[region] if isinstance(region, str) else region
    o = f'''<div {an(t, fx, .3)} class="hz-abs" style="left:{left}px;top:{top}px;width:{w*scale:.0f}px;height:{h*scale:.0f}px;overflow:hidden;border-radius:22px;background:#F9FAFC;z-index:{z};box-shadow:0 10px 26px rgba(19,32,27,.08)">
<img src="file://{DASH}" style="position:absolute;left:{-x*scale:.0f}px;top:{-y*scale:.0f}px;width:{1600*scale:.0f}px;height:{900*scale:.0f}px"></div>'''
    return o


def ring(region, crop, scale, left, top, t, up=None, upx=0, upy=0):
    x, y = (R[crop] if isinstance(crop, str) else crop)[:2]
    rx, ry, rw, rh = R[region] if isinstance(region, str) else region
    o = f'<div class="ring" {an(t, "pop", .3)} style="left:{left+(rx-x)*scale-6:.0f}px;top:{top+(ry-y)*scale-6:.0f}px;width:{rw*scale+12:.0f}px;height:{rh*scale+12:.0f}px"></div>'
    if up: o += f'<div class="up" {an(t+.1, "pop", .3)} style="left:{left+(rx-x)*scale+rw*scale-180+upx:.0f}px;top:{top+(ry-y)*scale-28+upy:.0f}px">{up}</div>'
    return o


CAM_PH = (231, 812, 1.22)   # phone centre (x 70-392, y 478-1126) zoom


def cam(kf):
    return f"cam({json.dumps(kf)},t);"


def zoomkf(t_in, t_out, cx=CAM_PH[0], cy=CAM_PH[1], s=CAM_PH[2]):
    return [[0, 540, 860, 1], [t_in, 540, 860, 1], [t_in + .3, cx, cy, s], [t_out, cx, cy, s], [t_out + .3, 540, 860, 1], [99, 540, 860, 1]]


def cur_svg():
    return ""


# ====================================================================== scenes
def s01():
    body = f'''<div class="c-h" {an(-.5, "l", .3)} style="top:300px;font-size:104px;letter-spacing:-5px;color:{PR}">Other ERP</div>
<div class="hz-abs" id="strike" style="left:90px;top:360px;width:560px;height:9px;background:{T};transform:rotate(-4deg) scaleX(0);transform-origin:0 50%;z-index:9"></div>
<div class="c-h" {an(.62, "r", .3)} style="top:410px;font-size:104px;letter-spacing:-5px;text-align:right">WhatsApp <span style="color:{A}">ERP</span></div>
<svg class="hz-abs" {an(-.5, "l", .34)} style="left:0;top:0;z-index:2" width="1080" height="1920">{svg_defs()}{monitor_old(85, 640, .78)}</svg>
<div class="hz-abs" {an(-.5, "fade", .3)} style="left:85px;top:1010px;font:600 28px Inter;color:{PR};z-index:9">40+ modules · training</div>
{phone_anim(at(0, tm("✅ GRN-101 Created", "📦 Steel Rod 12mm · <b>500 kg</b><br>🏢 Vendor A · Challan #4471<br>📊 Stock updated: <b>1,250 kg</b>", "10:15 AM", doc="GRN-101.pdf")), x=560, y=548, s=.62, t=.8)}
{dc("inv", .9, 600, 920, t=1.2)}{ring("inv", "inv", .9, 600, 920, 1.35)}
<div class="hz-abs" {an(.95, "pop", .3)} style="left:420px;top:740px;width:150px;height:150px;border-radius:50%;background:{T};display:flex;align-items:center;justify-content:center;font:italic 700 70px 'DejaVu Serif';color:#fff;z-index:9">vs</div>
<div class="hz-abs" {an(1.4, "fade", .3)} style="left:90px;top:1085px;font:700 28px Inter;letter-spacing:.18em;color:{T}">FOR MANUFACTURING</div>'''
    scene("s01", body, "const p=E.out(E.cl((t-0.38)/0.25));document.getElementById('strike').style.transform=`rotate(-4deg) scaleX(${p})`;")


def face_scene(name, hg0, mx, top, h, vy, extra):
    sc_ = 900 / 1080
    body = f'''<div class="hz-abs" {an(0, "fade", .2)} style="left:90px;top:{top}px;width:900px;height:{h}px;border-radius:40px;overflow:hidden;z-index:2;background:#cfdcd1">
<img id="hg" src="file://{HG}/0001.jpg" style="position:absolute;left:0;top:{int(vy*1920*sc_)}px;width:900px;transform-origin:50% 35%"></div>{extra}'''
    scene(name, body, f"faceAt(t,{hg0},{mx});")


def s02():
    nums = ''.join(f'<div class="hz-abs" {an(2.68 + i*.14, "pop", .3)} style="left:{90+i*310}px;top:960px;width:280px;height:170px;border-radius:32px;background:#fff;box-shadow:0 12px 30px rgba(19,32,27,.1);display:flex;align-items:center;justify-content:center;font:900 100px Inter;letter-spacing:-4px;color:{PR};z-index:5">0{i+1}</div>' for i in range(3))
    q = f'<div class="c-h" {an(.25, "u", .3, out=2.5, od=.15)} style="top:960px;font-size:62px;letter-spacing:-2px">Factory mein ERP<br><span style="color:{PR}">fail kyun hota hai?</span></div>'
    face_scene("s02", .02, 3.70, 290, 640, -.24, q + nums)


def problem(name, active, extra="", js=""):
    cards = ''.join(f'''<div class="hz-abs" id="pc{i}" style="left:90px;top:{560+i*196}px;width:900px;height:176px;border-radius:34px;background:#fff;display:flex;align-items:center;gap:34px;padding:0 44px;z-index:3;transition:none">
<div style="font:800 86px Inter;letter-spacing:-4px;color:{PR}">0{i+1}</div><div><div style="font:800 46px Inter;letter-spacing:-1.2px;color:{T}">{t}</div><div style="font:500 27px Inter;color:#6B7A71;margin-top:4px">{s}</div></div></div>''' for i, (t, s) in enumerate([("Koi system nahi", "Registers, Excel, calls"), ("Skilled manpower kam", "Software chalayega kaun?"), ("Implementation lamba", "Mahine nikal jaate hain")]))
    pj = f"""for(let i=0;i<3;i++){{const e=document.getElementById('pc'+i),on=i=={active},p=E.out(E.cl(t/0.35));const k=on?0.97+0.06*p:1.0-0.03*p;
e.style.transform=`scale(${{on?k:(i<{active}?0.97:0.97)}})`;e.style.opacity=on?1:({1 if active == 0 else .5}+(0.5-{1 if active == 0 else .5})*p);e.style.boxShadow=on?`0 ${{8+18*p}}px ${{20+30*p}}px rgba(19,32,27,${{.06+.1*p}})`:'0 8px 20px rgba(19,32,27,.06)';}}"""
    body = f'{rail(0)}<div class="c-h" style="top:370px;font-size:70px">ERP fail <span style="color:{PR}">kyun hota hai?</span></div>{cards}{extra}'
    scene(name, body, pj + js)


def s03():
    stamp = f'<div class="hz-abs" {an(2.25, "stamp", .25, base="rotate(-6deg)")} style="left:660px;top:585px;border:6px solid {PR};color:{PR};font:900 40px Inter;padding:6px 18px;border-radius:12px;background:#fff;z-index:6">PHIR BHI FAIL</div>'
    chips = ''.join(f'<div class="chip" {an(.5 + i*.18, "pop", .25, out=2.1, od=.2)} style="left:{560+i*0}px;top:{548+i*0}px;display:none"></div>' for i in range(0))
    problem("s03", 0, stamp + chips)


def s04():
    ppl = ''.join(f'<g {an(2.0 + i*.07, "pop", .25)} opacity="{1 if i == 2 else .3}">{person("supervisor" if i == 2 else "worker", "pill", 712 + i*56, 22, .3)}</g>' for i in range(5))
    body = f'<svg class="hz-abs" style="left:0;top:780px;z-index:6" width="1080" height="160">{svg_defs()}{ppl}</svg>'
    problem("s04", 1, body)


def s05():
    ms = ''.join(f'<div class="chip" {an(.6 + i*.28, "pop", .25)} style="left:{790+i*56}px;top:1040px;font-size:20px;padding:6px 10px;color:{PR}">M{i+1}</div>' for i in range(4))
    problem("s05", 2, ms)


def s06():
    lst, lj = listsheet(.0, 99, 1.4, 99)
    body = f'''<div class="c-h" {an(0, "fade", .25)} style="top:300px;font-size:44px;color:{A}">Hivon Automation</div><div class="c-h" {an(.08, "u", .3)} style="top:350px;font-size:96px;letter-spacing:-4px">WhatsApp ERP</div>
{laptop(370, 540, 600).replace('class="hz-abs"', f'class="hz-abs" {an(.55, "r", .36)}', 2)}
{phone_anim(at(0, wo("Hi", "10:12 AM")) + at(0, tm("Main Menu", "Namaste Ramesh 👋<br>Kya karna hai? Option chunein.", "10:12 AM", [("bm", LISTI, "View Options")])), lst, x=86, y=470, s=.66, t=.3)}
<svg class="hz-abs" {an(1.0, "fade", .3)} style="left:0;top:0;z-index:8" width="1080" height="1920">{sync_line(385, 820, 450, 760, "#2F7D57")}</svg>
<div class="hz-abs" {an(1.05, "fade", .3)} style="left:410px;top:940px;font:700 30px Inter;color:{T};z-index:9">Input <span style="color:{A}">WhatsApp</span> → Output <span style="color:{A}">Dashboard</span></div>
{"".join(f'<div class="chip" {an(1.45 + i*.2, "pop", .25)} style="left:{410+i*190}px;top:1000px;font-size:26px;padding:10px 22px"><b style="color:{A}">✓</b> {t}</div>' for i, t in enumerate(["System", "Manpower", "Time"]))}'''
    body = body.replace('<div class="hz-dim" data-in="0.0"', '<div class="hz-dim" data-in="0.75"').replace('<div class="w-list" data-in="0.0"', '<div class="w-list" data-in="0.75"')
    scene("s06", body, lj)


def s07():
    notes = ''.join(f'<div class="chip" {an(.4 + i*.3, "pop", .3)} style="left:{x}px;top:{y}px;font-size:34px;background:#FFF6D8">{t}</div>' for i, (x, y, t) in enumerate([(110, 620, "Purchase"), (420, 560, "Production"), (720, 650, "Dispatch"), (260, 800, "Store"), (600, 820, "Quality")]))
    lines = '<path d="M250 650 L460 600 M640 600 L780 680 M300 830 L460 600 M660 850 L780 690" stroke="#9BB3A2" stroke-width="5" stroke-dasharray="3 12" stroke-linecap="round" fill="none"/>'
    body = f'''<div class="c-h" {an(.05, "u", .3)} style="top:330px;font-size:62px;letter-spacing:-2px">Hum pehle aapka<br><span style="color:{A}">business seekhte hain</span></div>
<svg class="hz-abs" {an(1.1, "fade", .5)} style="left:0;top:0;z-index:2" width="1080" height="1920">{lines}</svg>{notes}
<svg class="hz-abs" style="left:0;top:0;z-index:3" width="1080" height="1920">{svg_defs()}<g {an(.2, "pop", .3)}>{person("owner", "pill", 120, 880, .8, pose="point")}</g><g {an(.3, "pop", .3)}>{person("store", "pill", 820, 880, .8, pose="carry", flip=True)}</g></svg>
<div class="chip" {an(1.78, "u", .3)} style="left:270px;top:1040px;background:{A};color:#fff;font-size:34px">Software seekhna nahi padega</div>'''
    scene("s07", body)


def s08():
    lines = ''.join(f'<div class="ln" style="height:13px;border-radius:7px;background:#CBD5CE;margin:18px 0;width:{[92,70,84,60,88,52][k]}%;transform:scaleX(0);transform-origin:0 50%"></div>' for k in range(6))
    rows = ''.join(f'''<div {an(.7 + i*.45, "l", .3)} style="display:flex;gap:20px;align-items:center;margin:22px 0"><svg width="62" height="62"><rect width="62" height="62" rx="18" fill="{A}"/><path d="M16 33 l11 11 l21 -24" stroke="#fff" stroke-width="8" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg><div style="font:700 38px Inter;letter-spacing:-1px;color:{T}">{t}</div></div>''' for i, t in enumerate(["Process samjha", "SOP banaya", "Aapne approve kiya"]))
    mach = ''.join(f'<div class="chip" {an(2.7 + i*.3, "pop", .3)} style="left:{110+i*300}px;top:960px;font-size:30px"><b style="color:{A}">✓</b> Plant {i+1}</div>' for i in range(3))
    body = f'''<div class="c-h" {an(.05, "u", .3)} style="top:330px;font-size:62px;letter-spacing:-2px">Phir aapke<br><span style="color:{A}">SOPs banaate hain</span></div>
<div {an(.15, "pop", .3)} class="hz-abs" style="left:90px;top:520px;width:330px;height:410px;border-radius:24px;background:#fff;box-shadow:0 14px 34px rgba(19,32,27,.12);padding:30px;z-index:3"><div style="font:900 56px Inter;color:{A};letter-spacing:-2px">SOP</div>{lines}</div>
<div class="hz-abs" style="left:460px;top:540px;width:540px;z-index:3">{rows}</div>{mach}
<div class="chip" {an(2.64, "u", .3)} style="left:150px;top:1060px;background:{A};color:#fff;font-size:30px;display:none">x</div>'''
    scene("s08", body, "document.querySelectorAll('.ln').forEach((l,i)=>{l.style.transform=`scaleX(${E.out(E.cl((t-0.3-i*0.12)/0.3))})`});")


def s09():
    q = f'<div class="c-h" {an(.74, "u", .3)} style="top:960px;font-size:60px;letter-spacing:-2px">"Mera staff software<br><span style="color:{PR}">seekhega nahi"</span></div>'
    face_scene("s09", 3.77, 6.66, 290, 640, -.24, q)


def chapter_frame(i, l1, l2, k1, ring_k1, ring_alert, up, t_dash):
    return (f'{rail(i)}{head(l1, l2)}'
            f'{dc(k1, 1.28, 440, 500, t=.1, fx="r")}{dc(R["alerts"], 1.18, 440, 720, t=.18, fx="r")}'
            f'{ring(k1, k1, 1.28, 440, 500, t_dash, up)}{ring(ring_alert, R["alerts"], 1.18, 440, 720, t_dash + .12)}'
            f'<svg class="hz-abs" {an(t_dash - .25, "fade", .2)} style="left:0;top:0;z-index:8" width="1080" height="1920">{sync_line(395, 760, 440, 600, "#2F7D57")}{sync_line(395, 980, 440, 900, "#2F7D57")}</svg>'
            f'<div class="hz-abs" style="left:440px;top:1122px;font:600 20px Inter;letter-spacing:.1em;color:rgba(19,32,27,.5);z-index:9">SAMPLE DATA</div>')


def s10():
    lst, lj = listsheet(1.0, 99, 1.5, 99, sel="Attendance")
    chat = at(.1, wo("Hi", "8:58 AM")) + at(.35, tm("Main Menu", "Namaste 👋 Kya karna hai?<br>Option chunein.", "8:58 AM", [("bm", LISTI, "View Options")]))
    body = (f'{rail(0)}{head("Kuch seekhne ki zaroorat nahi,", "sab kuch WhatsApp par")}{phone_anim(chat, lst)}'
            f'{dc("headcount", 1.28, 440, 500, t=.2, fx="r")}{dc(R["alerts"], 1.18, 440, 720, t=.3, fx="r")}'
            f'<div class="hz-abs" style="left:440px;top:1122px;font:600 20px Inter;letter-spacing:.1em;color:rgba(19,32,27,.5);z-index:9">SAMPLE DATA</div>')
    scene("s10", body, lj + "tapAt('bm',0.85,t);" + cam(zoomkf(.45, 1.95)))


def s11():
    chat = (at(0, tm("Please Mark Your Attendance", "Hi, <b>Suresh (Operator)</b><br>Shift A shuru hone wali hai. Check-in karein.", "8:58 AM", [("bci", REPLY, "Check-in"), ("blv", REPLY, "Apply Leave")]))
            + at(.82, wo("Check-in", "9:00 AM"))
            + at(.98, tm("Location Required", "Apni current location share karein,<br>taaki check-in verify ho sake.", "9:00 AM", [("bloc", REPLY, "📍 Send location")]))
            + at(1.42, wloc("9:01 AM"))
            + at(1.72, tm("✅ Check-in Successful", "👤 <b>Suresh (Operator)</b><br>🕘 In time: <b>9:01 AM</b><br>📍 Plant 1 · <b>inside radius</b>", "9:01 AM")))
    body = chapter_frame(1, "Labour ki attendance,", "ek click + location", "present", "present", "a3", "+1 present", 2.22) + phone_anim(chat)
    scene("s11", body, "tapAt('bci',0.68,t);tapAt('bloc',1.3,t);" + cam(zoomkf(.15, 1.9)))


def s12():
    sh = flowsheet("fs_inw", "Material Inward", [("Vendor", "Vendor A", True), ("Item", "Steel Rod 12mm", True), ("Quantity", "500 kg", False), ("Challan photo", "📎 challan_4471.jpg", False)], .15, 1.62)
    chat = (at(0, tm("Main Menu", "Namaste Ramesh 👋<br>Kya karna hai? Option chunein.", "10:12 AM", [("bm", LISTI, "View Options")])) + at(0, wo("Material Inward", "10:13 AM"))
            + at(1.7, tm("✅ GRN-101 Created", "📦 Steel Rod 12mm · <b>500 kg</b><br>🏢 Vendor A · Challan #4471<br>📊 Stock updated: <b>1,250 kg</b>", "10:15 AM", doc="GRN-101.pdf")))
    body = chapter_frame(2, "Maal kitna aaya,", "ek form, ek click", "inv", "inv", "a2", "+500 kg", 2.35) + phone_anim(chat, sh)
    scene("s12", body, "fillFields('#fs_inw .hz-fi',[0.42,0.66,0.9,1.14],t);press('fs_inw_b',1.45,t);" + cam(zoomkf(.0, 2.0)))


def s13():
    sh = flowsheet("fs_prd", "Production Entry", [("Machine", "M-4 (CNC Lathe)", True), ("Item", "Flange 40mm", True), ("OK quantity (pcs)", "120", False), ("Rejection (pcs)", "3", False)], .85, 2.95)
    chat = (at(0, tm("Production Update · Shift A", "Hi <b>Vikas (Supervisor)</b><br>Aaj ki production entry karein.", "5:55 PM", [("bup", LINKI, "Update Production"), ("btg", REPLY, "Aaj ka target")]))
            + at(3.05, wo("Submitted", "5:57 PM"))
            + at(3.22, tm("✅ Production Logged", "⚙️ Machine <b>M-4</b> · Flange 40mm<br>✔️ OK: <b>120 pcs</b> · ✖️ Reject: <b>3</b><br>🎯 Target 150 · <b>80%</b>", "5:57 PM", doc="DPR-M4.pdf")))
    body = chapter_frame(3, "Supervisor: machine se", "ek input, production live", "prod", "prod", "a4", "+120 pcs", 3.75) + phone_anim(chat, sh)
    scene("s13", body, "tapAt('bup',0.68,t);fillFields('#fs_prd .hz-fi',[1.25,1.65,2.05,2.4],t);press('fs_prd_b',2.75,t);" + cam(zoomkf(.2, 3.42)))


def s14():
    cards = (dc("prod", 1.08, 90, 520, t=.1) + dc("present", 1.08, 90, 700, t=.2) + dc("inv", 1.08, 90, 880, t=.3)
             + dc(R["alerts"], 1.0, 540, 520, t=.25, fx="r") + dc((320, 548, 760, 330), .62, 540, 880, t=.35, fx="r"))
    rings = (ring("prod", "prod", 1.08, 90, 520, 1.98, "Production") + ring("inv", "inv", 1.08, 90, 880, 3.66, "Inventory")
             + ring("present", "present", 1.08, 90, 700, 4.9, "Kitne log") + ring("a4", R["alerts"], 1.0, 540, 520, 5.6))
    body = (f'{rail(4)}{head("Poori factory,", "ek single dashboard", fs=62)}{cards}{rings}'
            f'<div class="chip" {an(6.95, "u", .3)} style="left:300px;top:1090px;background:{A};color:#fff;font-size:30px">WhatsApp → Dashboard · live</div>')
    js = "const z=E.out(E.cl((t-0.2)/7.6));document.getElementById('stage').style.transformOrigin='540px 820px';document.getElementById('stage').style.transform=`scale(${1+0.03*z})`;"
    scene("s14", body, js)


def s15():
    tiles = ''.join(f'<div class="chip" {an(.1 + i*.16, "pop", .3)} style="left:{90+(i%2)*460}px;top:{340+(i//2)*120}px;width:430px;font-size:38px;padding:22px 30px">{e}  {t}</div>' for i, (e, t) in enumerate([("🕘", "Attendance"), ("🚚", "Inward"), ("⚙️", "Production"), ("📊", "Dashboard")]))
    body = (f'{tiles}<div class="hz-abs" {an(1.35, "pop", .32)} style="left:80px;top:640px;font:900 220px Inter;letter-spacing:-11px;color:{T}">₹<span id="pr">0</span></div>'
            f'<div class="hz-abs" {an(1.9, "u", .3)} style="left:92px;top:900px;font:700 68px Inter;letter-spacing:-2px;color:{A}">ke mahine se shuru</div>')
    scene("s15", body, "document.getElementById('pr').textContent=Math.round(15000*E.out(E.cl((t-1.35)/0.5))).toLocaleString('en-IN');")


def s16():
    panel = f'''<div class="hz-abs" {an(.5, "u", .34)} style="left:90px;top:870px;width:900px;padding:30px 40px;border-radius:34px;background:rgba(255,255,255,.85);backdrop-filter:blur(24px);border:2px solid #fff;box-shadow:0 24px 50px rgba(19,32,27,.12);z-index:5">
<div style="font:800 48px Inter;letter-spacing:-1.5px;line-height:1.05;color:{T}">Apni factory ka<br><span style="color:{A}">custom WhatsApp ERP</span></div>
<div style="font:600 28px Inter;color:#55665C;margin:12px 0 18px">₹15,000/mahine se shuru</div>
<span id="ctab" style="display:inline-block;background:{CTA};color:{NAVY};border-radius:999px;padding:16px 32px;font:800 34px Inter;opacity:0">WhatsApp pe DM karo ↓</span></div>
<div class="hz-abs" style="left:860px;top:300px;font:800 40px Inter;color:#fff;z-index:6">hivon<span style="color:{CTA}">.</span></div>'''
    sc_ = 900 / 1080
    body = f'''<div class="hz-abs" {an(0, "fade", .2)} style="left:90px;top:290px;width:900px;height:560px;border-radius:40px;overflow:hidden;z-index:2;background:#cfdcd1">
<img id="hg" src="file://{HG}/0001.jpg" style="position:absolute;left:0;top:{int(-.27*1920*sc_)}px;width:900px;transform-origin:50% 35%"></div>{panel}'''
    scene("s16", body, "faceAt(t,6.72,11.6);const p=E.out(E.cl((t-3.0)/0.35));const b=document.getElementById('ctab');b.style.opacity=p;b.style.transform=`translateY(${(1-p)*30}px) scale(${1+0.04*Math.sin(Math.max(0,t-3.4)*6)})`;")


if __name__ == "__main__":
    fs = [s01, s02, s03, s04, s05, s06, s07, s08, s09, s10, s11, s12, s13, s14, s15, s16]
    only = sys.argv[1:]
    for f in fs:
        if not only or f.__name__ in only: f()
    json.dump(SC, open(f"{OUT}/scenes.json", "w"))
    print("ok")
