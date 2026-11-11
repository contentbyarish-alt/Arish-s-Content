"""Round 4 storyboards (redesigned): A Live Sync, B Floor & Screen, C Keynote Chapters. Phone + dashboard together. SAMPLE data."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from flows import *
from comp import P, person, svg_defs
OUT = os.path.join(ROOT, "boards"); os.makedirs(OUT, exist_ok=True)
G, T, A, PR, C, CTA, NAVY = P['ground'], P['text'], P['accent'], P['problem'], P['card'], P['cta'], P['navy']
HG = ROOT + "/final/hg"


def save(n, body, bg, css=""):
    open(f"{OUT}/{n}.html", "w").write(f'<!doctype html><html><head><meta charset="utf-8"><style>{BASE_CSS}{CSS}{css}</style></head><body style="background:{bg}">{body}</body></html>')


def svg(inner, w=1080, h=1920, x=0, y=0, z=1):
    return f'<svg class="hz-abs" style="left:{x}px;top:{y}px;z-index:{z}" width="{w}" height="{h}" viewBox="0 0 {w} {h}">{svg_defs()}{inner}</svg>'


def face(x, y, w, h, frame, radius=36, vy=-0.08, z=2):
    sc = w / 1080
    return f'<div class="hz-abs" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;border-radius:{radius}px;overflow:hidden;z-index:{z}"><img src="file://{HG}/{frame:04d}.jpg" style="position:absolute;left:0;top:{int(vy*1920*sc)}px;width:{w}px"></div>'


def monitor_old(x, y, s=1, dim=False):
    tabs = ''.join(f'<rect x="{18+i*58}" y="52" width="52" height="18" rx="4" fill="#C9B9B6"/>' for i in range(6))
    side = ''.join(f'<rect x="18" y="{84+i*22}" width="70" height="12" rx="3" fill="#D8C9C6"/>' for i in range(11))
    grid = ''.join(f'<rect x="{100+c*62}" y="{84+r*30}" width="54" height="20" rx="3" fill="#B5483F" opacity="{.12+((r+c)%4)*.08}"/>' for r in range(8) for c in range(4))
    pop = '<rect x="150" y="140" width="210" height="96" rx="10" fill="#fff" stroke="#B5483F" stroke-width="3"/><text x="255" y="182" text-anchor="middle" font-family="Inter" font-weight="800" font-size="22" fill="#B5483F">Error 403</text><text x="255" y="210" text-anchor="middle" font-family="Inter" font-size="15" fill="#555">Contact administrator</text>'
    return f'''<g transform="translate({x},{y}) scale({s})" opacity="{.75 if dim else 1}"><rect width="380" height="350" rx="16" fill="#2B2F33"/><rect x="10" y="10" width="360" height="318" rx="8" fill="#F4EEEC"/>
<rect x="10" y="10" width="360" height="32" rx="8" fill="#E3D5D2"/>{tabs}{side}{grid}{pop}<path d="M150 350 h80 l14 50 h-108 z" fill="#3A3F44"/><rect x="110" y="398" width="160" height="10" rx="5" fill="#3A3F44"/></g>'''


def sync_line(x1, y1, x2, y2, col="#55B685", w=5):
    mx = (x1 + x2) / 2
    return f'<path d="M{x1} {y1} C {mx} {y1}, {mx} {y2}, {x2} {y2}" stroke="{col}" stroke-width="{w}" fill="none" stroke-dasharray="2 14" stroke-linecap="round"/><circle cx="{x2}" cy="{y2}" r="9" fill="{col}"/><circle cx="{x1}" cy="{y1}" r="9" fill="{col}"/>'


SAMPLE = lambda x, y, c="rgba(255,255,255,.5)": f'<div class="hz-abs" style="left:{x}px;top:{y}px;font:600 20px Inter;letter-spacing:.1em;color:{c};z-index:9">SAMPLE DATA</div>'
WM = lambda x, y, c=T, s=50: f'<div class="hz-abs" style="left:{x}px;top:{y}px;font:800 {s}px Inter;letter-spacing:-1px;color:{c};z-index:9">hivon<span style="color:{CTA}">.</span></div>'

# =====================================================================
# A  LIVE SYNC — premium dark stage, phone + dashboard always side by side
#    refs: brainextends-606193 (near-black rounded stage, green atmosphere), jake11moran-414633 (slow camera)
# =====================================================================
A_BG = "radial-gradient(90% 60% at 15% 5%,#3E8E66 0%,#1B3A2B 45%,#0B1410 100%)"
A_CSS = f"""
.st{{position:absolute;left:36px;top:120px;width:1008px;height:1680px;border-radius:56px;background:#0E1512;box-shadow:inset 0 0 0 1px rgba(255,255,255,.06),0 40px 80px rgba(0,0,0,.45);overflow:hidden}}
.a-k{{position:absolute;font:600 26px Inter;letter-spacing:.2em;color:#7FC79F;text-transform:uppercase}}
.a-h{{position:absolute;font:700 76px Inter;letter-spacing:-2.5px;line-height:1.04;color:#F2F6F3}}
.a-s{{position:absolute;font:500 34px Inter;color:#9DB3A6;line-height:1.3}}
.a-pill{{position:absolute;border-radius:999px;padding:12px 26px;font:600 28px Inter;background:rgba(255,255,255,.08);color:#DDE9E1;border:1px solid rgba(255,255,255,.12)}}
"""


def A1():
    left = monitor_old(70, 760, .95, dim=True)
    body = f'''<div class="st">
<div class="hz-abs" style="left:0;top:0;width:500px;height:1680px;background:linear-gradient(180deg,#1A1514,#120F0E)"></div>
{svg(left, 1008, 1680)}
<div class="a-k" style="left:60px;top:150px;color:#E39A92">Other ERP</div><div class="a-h" style="left:56px;top:196px;font-size:64px;color:#E8D8D5">Software<br>seekho pehle</div>
<div class="a-pill" style="left:60px;top:1270px;color:#E39A92">40+ modules</div><div class="a-pill" style="left:60px;top:1350px;color:#E39A92">Training · manuals</div>
<div class="a-k" style="left:560px;top:150px">WhatsApp ERP</div><div class="a-h" style="left:556px;top:196px;font-size:64px">Bas WhatsApp<br>chalao</div>
{ph(560, 520, .62, ATTENDANCE[3][1], "")}
{dcrop("present", .95, 600, 1130, ring="present", radius=18, z=6)}
{svg(sync_line(800, 1080, 790, 1140), 1008, 1680, z=7)}
<div class="hz-abs" style="left:502px;top:0;width:4px;height:1680px;background:linear-gradient(#55B685,rgba(85,182,133,.1));z-index:8"></div>
<div class="hz-abs" style="left:414px;top:640px;width:180px;height:180px;border-radius:50%;background:rgba(14,21,18,.85);backdrop-filter:blur(12px);border:2px solid rgba(255,255,255,.18);display:flex;align-items:center;justify-content:center;font:300 italic 84px 'DejaVu Serif';color:#fff;z-index:9">vs</div>
<div class="hz-abs" style="left:0;right:0;top:1500px;text-align:center;font:600 40px Inter;letter-spacing:.3em;color:#9DB3A6;z-index:9">FOR MANUFACTURING</div></div>'''
    save("A1", body, A_BG, A_CSS)


def A2():
    body = f'''<div class="st">{face(0, 0, 1008, 1200, 60, 0)}
<div class="hz-abs" style="left:0;top:900px;width:1008px;height:300px;background:linear-gradient(transparent,#0E1512)"></div>
<div class="a-h" style="left:60px;top:1230px;font-size:64px">Factory mein ERP<br><span style="color:#E39A92">fail kyun</span> hota hai?</div>
{"".join(f'<div class="a-pill" style="left:{60+i*190}px;top:1460px;font-size:40px;font-weight:800">0{i+1}</div>' for i in range(3))}</div>'''
    save("A2", body, A_BG, A_CSS)


def A3():
    rows = [("01", "Koi system hi nahi", 1), ("02", "Skilled manpower kam", .3), ("03", "Implementation lamba", .3)]
    hw = ''.join(f'<div style="display:flex;gap:28px;align-items:baseline;margin:26px 0;opacity:{o}"><span style="font:600 32px JetBrains Mono;color:#E39A92">{n}</span><span style="font:700 70px Inter;letter-spacing:-2px;color:#F2F6F3">{t}</span></div>' for n, t, o in rows)
    papers = ''.join(f'<g transform="translate({x},{y}) rotate({r})"><rect width="120" height="150" rx="8" fill="#2A332F"/>{"".join(f"<rect x=\"16\" y=\"{24+k*24}\" width=\"{88-(k%2)*28}\" height=\"7\" rx=\"3\" fill=\"#46524C\"/>" for k in range(5))}</g>' for x, y, r in [(80, 1060, -14), (300, 1180, 9), (600, 1040, -6), (780, 1200, 12)])
    body = f'''<div class="st"><div class="a-k" style="left:60px;top:150px;color:#E39A92">Teen reason</div><div class="hz-abs" style="left:60px;top:210px">{hw}</div>
{svg(papers + f'<g opacity=".9">{person("owner","pill",380,1010,1.35,pose="head")}</g>', 1008, 1680)}
<div class="a-s" style="left:60px;top:1500px">Registers, Excel, phone calls…<br><span style="color:#E39A92">software laga bhi doge, phir bhi fail</span></div></div>'''
    save("A3", body, A_BG, A_CSS)


def A4():
    body = f'''<div class="st"><div class="a-k" style="left:60px;top:130px">Hivon Automation</div><div class="a-h" style="left:56px;top:176px;font-size:96px">WhatsApp <span style="color:#55B685">ERP</span></div>
<div class="a-s" style="left:60px;top:300px">Input WhatsApp par · output dashboard par</div>
{ph(40, 440, .86, MENU, wlist("View Options", MENU_ROWS, "Material Inward"))}
{dcrop("inv", .95, 560, 560, radius=18, z=6)}{dcrop(R["alerts"], 1.0, 520, 760, ring="a2", radius=18, z=6)}
{svg(sync_line(420, 820, 560, 640) + sync_line(420, 1000, 520, 930), 1008, 1680, z=7)}
<div class="a-pill" style="left:60px;top:1350px">✓ System</div><div class="a-pill" style="left:290px;top:1350px">✓ Manpower</div><div class="a-pill" style="left:560px;top:1350px">✓ Time</div>
{SAMPLE(60, 1600)}</div>'''
    save("A4", body, A_BG, A_CSS)


def A5():
    steps = ''.join(f'<div class="a-pill" style="left:{60+i*300}px;top:150px;font-size:26px;{"background:#2F7D57;color:#fff" if i==2 else ""}">{t}</div>' for i, t in enumerate(["✓ Attendance", "✓ Inward", "● Production"]))
    body = f'''<div class="st">{steps}<div class="a-h" style="left:56px;top:230px;font-size:62px">Supervisor ka ek input,<br><span style="color:#55B685">dashboard live</span></div>
{ph(30, 470, .9, PRODUCTION[3][1], "")}
{dcrop("prod", 1.08, 550, 560, ring="prod", radius=18, z=6)}{dcrop(R["alerts"], 1.0, 520, 800, ring="a4", radius=18, z=6)}
{svg(sync_line(440, 1180, 520, 1140) + sync_line(440, 1060, 550, 700), 1008, 1680, z=7)}
<div class="a-pill" style="left:560px;top:1180px;background:#2F7D57;color:#fff">+120 pcs · M-4</div>
{SAMPLE(60, 1600)}</div>'''
    save("A5", body, A_BG, A_CSS)


def A6():
    body = f'''<div class="st">{face(0, 0, 1008, 900, 230, 0)}
<div class="hz-abs" style="left:0;top:700px;width:1008px;height:200px;background:linear-gradient(transparent,#0E1512)"></div>
<div class="a-h" style="left:60px;top:920px;font-size:62px">Apni factory ka<br><span style="color:#55B685">custom WhatsApp ERP</span></div>
{ph(60, 1110, .44, PRODUCTION[3][1], "")}{dcrop("present", .62, 300, 1150, radius=14, z=6)}{dcrop("prod", .62, 300, 1260, radius=14, z=6)}
<div class="hz-abs" style="left:300px;top:1400px;background:{CTA};color:{NAVY};border-radius:999px;padding:22px 40px;font:800 40px Inter;z-index:9">WhatsApp pe DM karo ↓</div>
<div class="a-s" style="left:300px;top:1510px;font-size:30px">₹15,000/mahine se shuru</div>{WM(820, 1580, "#F2F6F3", 44)}</div>'''
    save("A6", body, A_BG, A_CSS)


# =====================================================================
# B  FLOOR & SCREEN — top: the factory moment (illustrated); bottom: the system (phone + dashboard)
#    refs: astrothewizard-618782 (storybook explainer, characters with personality, sound synced)
# =====================================================================
B_CSS = f"""
.fl{{position:absolute;left:0;top:0;width:1080px;height:900px;overflow:hidden;background:linear-gradient(#F4EFE6,#E9E1D3)}}
.sc{{position:absolute;left:0;top:900px;width:1080px;height:1020px;background:{G}}}
.b-tag{{position:absolute;background:{T};color:#fff;border-radius:14px;padding:12px 24px;font:700 30px Inter;z-index:9}}
.b-h{{position:absolute;font:800 64px Inter;letter-spacing:-2px;line-height:1.05;color:{T};z-index:9}}
.b-div{{position:absolute;left:0;top:888px;width:1080px;height:24px;background:{G};border-radius:24px 24px 0 0;z-index:3}}
"""


def floor(inner, bg="linear-gradient(#F4EFE6,#E9E1D3)"):
    flr = '<rect x="0" y="700" width="1080" height="200" fill="#D9CDB8"/><path d="M0 700 H1080" stroke="#C7B89F" stroke-width="4"/>'
    win = ''.join(f'<rect x="{80+i*250}" y="110" width="170" height="120" rx="8" fill="#FFFFFF" opacity=".55"/>' for i in range(4))
    return f'<div class="fl" style="background:{bg}">{svg(win + flr + inner, 1080, 900)}</div><div class="b-div"></div>'


def machine(x, y, s=1, lamp="#5EC26A", label=""):
    t = f'<text x="30" y="200" font-family="Inter" font-weight="800" font-size="34" fill="#13201B">{label}</text>' if label else ""
    return f'''<g transform="translate({x},{y}) scale({s})"><rect width="300" height="230" rx="18" fill="#9FB8A7"/><rect x="0" y="0" width="300" height="40" rx="18" fill="#8AA594"/><rect x="24" y="56" width="120" height="80" rx="10" fill="#F8FBF8"/>
<circle cx="222" cy="120" r="52" fill="#F8FBF8"/><circle cx="222" cy="120" r="16" fill="#6E8A77"/><rect x="40" y="230" width="220" height="40" rx="6" fill="#7E9786"/><circle cx="270" cy="22" r="10" fill="{lamp}"/>{t}</g>'''


def truck(x, y, s=1):
    return f'''<g transform="translate({x},{y}) scale({s})"><rect width="360" height="190" rx="12" fill="#C9D6CC"/><text x="180" y="110" text-anchor="middle" font-family="Inter" font-weight="800" font-size="34" fill="#13201B">STEEL ROD</text>
<path d="M360 50 h110 l60 70 v70 h-170z" fill="#2F7D57"/><rect x="384" y="70" width="80" height="50" rx="6" fill="#E9F3EC"/>
<circle cx="90" cy="200" r="40" fill="#2B3036"/><circle cx="90" cy="200" r="14" fill="#C8CDD1"/><circle cx="440" cy="200" r="40" fill="#2B3036"/><circle cx="440" cy="200" r="14" fill="#C8CDD1"/></g>'''


def bubble_over(x, y, text, col="#1DA35E"):
    return f'<g transform="translate({x},{y})"><rect x="0" y="0" width="{len(text)*15+60}" height="56" rx="28" fill="#fff" stroke="{col}" stroke-width="3"/><circle cx="30" cy="28" r="14" fill="{col}"/><path d="M23 28 l5 5 l9 -10" stroke="#fff" stroke-width="3" fill="none"/><text x="52" y="37" font-family="Inter" font-weight="700" font-size="24" fill="#13201B">{text}</text></g>'


def B1():
    left = monitor_old(40, 300, .9) + person("owner", "paper", 300, 420, 1.0, pose="head")
    right = machine(600, 430, .7) + person("worker", "paper", 820, 400, 1.0, pose="phone") + bubble_over(660, 300, "Check-in ✓")
    body = f'''{floor(f'<rect x="0" y="0" width="540" height="900" fill="#F1E2DE" opacity=".7"/>' + left + right + '<path d="M540 0 L556 150 L528 300 L560 450 L532 600 L552 750 L540 900" stroke="#13201B" stroke-width="6" fill="none"/>')}
<div class="b-tag" style="left:60px;top:80px;background:#B5483F">Other ERP</div><div class="b-tag" style="left:680px;top:80px;background:#2F7D57">WhatsApp ERP</div>
<div class="hz-abs" style="left:440px;top:380px;width:200px;height:200px;border-radius:50%;background:#fff;box-shadow:0 14px 40px rgba(0,0,0,.2);display:flex;align-items:center;justify-content:center;font:italic 700 96px 'DejaVu Serif';color:{T};z-index:9">vs</div>
<div class="sc"></div>{ph(70, 960, .74, ATTENDANCE[3][1], "")}{dcrop("present", 1.05, 470, 1010, ring="present", radius=20)}{dcrop(R["a3"], 1.18, 470, 1220, radius=16)}
<div class="b-h" style="left:470px;top:1340px;font-size:58px">for<br><span style="color:{A}">Manufacturing</span></div>'''
    save("B1", body, G, B_CSS)


def B2():
    ms = ''.join(machine(40 + i * 340, 420, .78, "#5EC26A" if i == 1 else "#D9A79E") for i in range(3))
    ppl = person("supervisor", "paper", 380, 400, 1.0, pose="point") + person("worker", "paper", 80, 420, .95, pose="shrug") + person("worker", "paper", 760, 420, .95, pose="head")
    q = ''.join(f'<text x="{x}" y="{y}" font-family="DejaVu Serif" font-style="italic" font-weight="700" font-size="64" fill="#B5483F">?</text>' for x, y in [(180, 390), (860, 380)])
    body = f'''{floor(ms + ppl + q + bubble_over(400, 300, "Sirf ek skilled operator", "#2F7D57"))}
<div class="b-tag" style="left:60px;top:80px;background:#B5483F">Reason 02</div>
<div class="sc"></div><div class="b-h" style="left:70px;top:980px">Skilled manpower<br><span style="color:{PR}">bahut kam</span></div>
<div class="hz-abs" style="left:70px;top:1240px;width:940px;display:flex;gap:20px;transform:scale(1.0)">{"".join(f'<div style="flex:1;background:#fff;border-radius:28px;padding:30px 26px;box-shadow:0 10px 26px rgba(19,32,27,.08)"><div style="font:800 52px Inter;color:{c}">{n}</div><div style="font:600 28px Inter;color:{T};margin-top:8px">{t}</div></div>' for n, t, c in [("01", "Koi system nahi", PR), ("02", "Manpower kam", PR), ("03", "Lamba implementation", "#B9C4BC")])}</div>
<div class="hz-abs" style="left:70px;top:1520px;font:700 48px Inter;letter-spacing:-1px;color:{T}">Complex software<br><span style="color:{PR}">chalayega kaun?</span></div>'''
    save("B2", body, G, B_CSS)


def B3():
    ms = ''.join(machine(40 + i * 340, 440, .74) for i in range(3))
    ppl = ''.join(person(r, "paper", x, 410, .95, pose="phone") for r, x in [("worker", 150), ("supervisor", 490), ("store", 830)])
    bub = bubble_over(90, 300, "Attendance") + bubble_over(420, 270, "Production") + bubble_over(760, 300, "Inward")
    body = f'''{floor(ms + ppl + bub, "linear-gradient(#EEF5EF,#DDE9DF)")}
<div class="b-tag" style="left:60px;top:80px;background:#2F7D57">Hivon Automation</div>
<div class="sc"></div><div class="b-h" style="left:70px;top:950px;font-size:76px">WhatsApp <span style="color:{A}">ERP</span></div>
{ph(70, 1060, .72, MENU, wlist("View Options", MENU_ROWS, "Material Inward"))}
{laptop(480, 1110, 480)}
{svg(sync_line(400, 1350, 470, 1300, "#2F7D57"), z=6)}
<div class="hz-abs" style="left:470px;top:1460px;font:600 32px Inter;color:{T};opacity:.75">Input phone par → report dashboard par</div>'''
    save("B3", body, G, B_CSS)


def B4():
    fl = truck(60, 470, .95) + person("store", "paper", 700, 410, 1.0, pose="phone") + bubble_over(620, 300, "500 kg inward")
    body = f'''{floor(fl)}<div class="b-tag" style="left:60px;top:80px">Store · maal inward</div>
<div class="sc"></div>{ph(60, 950, .8, INWARD[2][1], INWARD[2][2])}
{dcrop("inv", 1.12, 480, 990, ring="inv", radius=20)}{dcrop(R["alerts"], 1.15, 470, 1190, ring="a2", radius=20)}
{svg(sync_line(420, 1400, 470, 1330, "#2F7D57"), z=6)}{SAMPLE(480, 1590, "rgba(19,32,27,.5)")}'''
    save("B4", body, G, B_CSS)


def B5():
    fl = machine(100, 400, 1.0, label="M-4") + person("supervisor", "paper", 560, 400, 1.05, pose="phone") + bubble_over(560, 290, "120 pcs bane")
    body = f'''{floor(fl)}<div class="b-tag" style="left:60px;top:80px">Supervisor · machine M-4</div>
<div class="sc"></div>{ph(60, 950, .8, PRODUCTION[3][1], "")}
{dcrop("prod", 1.12, 480, 990, ring="prod", radius=20)}{dcrop(R["chart"], .74, 470, 1190, radius=20)}
<div class="hz-abs" style="left:480px;top:1450px;background:{A};color:#fff;border-radius:999px;padding:12px 26px;font:700 30px Inter">+120 pcs · M-4</div>{SAMPLE(480, 1560, "rgba(19,32,27,.5)")}'''
    save("B5", body, G, B_CSS)


def B6():
    body = f'''{face(0, 0, 1080, 900, 230, 0)}<div class="b-div"></div>
<div class="sc"></div><div class="b-h" style="left:70px;top:950px;font-size:66px">Apni factory ka<br><span style="color:{A}">custom WhatsApp ERP?</span></div>
{ph(70, 1150, .5, PRODUCTION[3][1], "")}{dcrop("prod", .8, 380, 1180, radius=16)}{dcrop("present", .8, 380, 1320, radius=16)}
<div class="hz-abs" style="left:380px;top:1470px;background:{CTA};color:{NAVY};border-radius:999px;padding:22px 40px;font:800 42px Inter">WhatsApp pe DM karo ↓</div>
<div class="hz-abs" style="left:380px;top:1580px;font:600 30px Inter;color:{T};opacity:.75">₹15,000/mahine se shuru</div>{WM(820, 1640)}'''
    save("B6", body, G, B_CSS)


# =====================================================================
# C  KEYNOTE CHAPTERS — warm canvas, one continuous take, phone above laptop, chapter rail
#    refs: twoclipping-496100 (Apple-keynote film, cursor-driven, screen-studio zoom), howdevelop-733090 (precise launch film)
# =====================================================================
C_CSS = f"""
.rail{{position:absolute;left:60px;right:60px;top:110px;display:flex;gap:10px;z-index:9}}
.rail div{{flex:1;padding-top:14px;border-top:5px solid #C9D6CC;font:600 22px Inter;color:#7D8C83}}
.rail div.on{{border-color:{A};color:{T}}} .rail div.done{{border-color:{A};color:#7D8C83}}
.c-h{{position:absolute;left:70px;right:70px;font:800 80px Inter;letter-spacing:-3px;line-height:1;color:{T};z-index:9}}
.c-n{{position:absolute;font:800 300px Inter;letter-spacing:-14px;color:{T};opacity:.06;z-index:0}}
"""
CH = ["Problem", "Attendance", "Inward", "Production", "Dashboard"]


def rail(i):
    return '<div class="rail">' + ''.join(f'<div class="{"on" if k == i else ("done" if k < i else "")}">{"0" + str(k)} {c}</div>' for k, c in enumerate(CH)) + '</div>'


C_BG = "linear-gradient(180deg,#F6F4EF 0%,#EEF2EC 100%)"


def C1():
    body = f'''<div class="c-h" style="top:200px;font-size:150px;letter-spacing:-7px;color:{PR};opacity:.9">Other<br>ERP</div>
<div class="hz-abs" style="left:60px;top:440px;width:960px;height:10px;background:{T};transform:rotate(-8deg);z-index:9"></div>
<div class="c-h" style="top:520px;font-size:150px;letter-spacing:-7px;text-align:right">WhatsApp<br><span style="color:{A}">ERP</span></div>
{svg(monitor_old(40, 920, .78), z=2)}{ph(560, 820, .68, INWARD[3][1], "")}{laptop(600, 1420, 360)}
<div class="hz-abs" style="left:440px;top:1060px;width:150px;height:150px;border-radius:50%;background:{T};display:flex;align-items:center;justify-content:center;font:italic 700 70px 'DejaVu Serif';color:#fff;z-index:9">vs</div>
<div class="hz-abs" style="left:60px;top:1740px;font:700 44px Inter;letter-spacing:.24em;color:{T}">FOR MANUFACTURING</div>'''
    save("C1", body, C_BG, C_CSS)


def C2():
    cards = ''.join(f'''<div class="hz-abs" style="left:70px;top:{560+i*300}px;width:940px;height:260px;border-radius:40px;background:#fff;box-shadow:{"0 30px 60px rgba(19,32,27,.16)" if i==1 else "0 10px 24px rgba(19,32,27,.06)"};transform:scale({1.04 if i==1 else .96});opacity:{1 if i==1 else .55};display:flex;align-items:center;gap:40px;padding:0 50px">
<div style="font:800 110px Inter;letter-spacing:-5px;color:{PR}">0{i+1}</div><div><div style="font:800 54px Inter;letter-spacing:-1.5px;color:{T}">{t}</div><div style="font:500 30px Inter;color:#6B7A71;margin-top:6px">{s}</div></div></div>''' for i, (t, s) in enumerate([("Koi system nahi", "Registers, Excel, calls"), ("Skilled manpower kam", "Software chalayega kaun?"), ("Implementation lamba", "Mahine nikal jaate hain")]))
    body = f'''{rail(0)}<div class="c-h" style="top:250px">ERP fail<br><span style="color:{PR}">kyun hota hai?</span></div>{cards}'''
    save("C2", body, C_BG, C_CSS)


def C3():
    body = f'''<div class="c-h" style="top:180px;font-size:64px;color:{A}">Hivon Automation</div><div class="c-h" style="top:250px;font-size:120px;letter-spacing:-5px">WhatsApp ERP</div>
{ph(316, 450, .86, INWARD[1][1], INWARD[1][2])}{laptop(140, 1290, 800, ring="alerts")}
<div class="hz-abs" style="left:70px;top:1000px;font:700 34px Inter;color:{T};z-index:9">Input<br><span style="color:{A}">WhatsApp</span></div>
<div class="hz-abs" style="left:820px;top:1000px;text-align:right;font:700 34px Inter;color:{T};z-index:9">Output<br><span style="color:{A}">Dashboard</span></div>'''
    save("C3", body, C_BG, C_CSS)


def C4():
    cur = '<svg class="hz-abs" style="left:560px;top:860px;z-index:20" width="90" height="110"><path d="M8 8 L8 92 L30 72 L46 104 L62 96 L46 64 L78 64 Z" fill="#13201B" stroke="#fff" stroke-width="5" stroke-linejoin="round"/></svg>'
    body = f'''{rail(1)}<div class="c-n" style="left:40px;top:150px">01</div><div class="c-h" style="top:220px;font-size:70px">Labour ki attendance,<br><span style="color:{A}">ek click + location</span></div>
{ph(250, 430, 1.0, ATTENDANCE[2][1], "")}{cur}{laptop(170, 1430, 740, ring="present")}{SAMPLE(70, 1390, "rgba(19,32,27,.5)")}'''
    save("C4", body, C_BG, C_CSS)


def C5():
    body = f'''{rail(4)}<div class="c-n" style="left:40px;top:150px">04</div><div class="c-h" style="top:220px;font-size:76px">Poori factory,<br><span style="color:{A}">ek dashboard</span></div>
{dcrop("prod", 1.3, 70, 470, ring="prod", radius=28)}{dcrop("present", 1.3, 70, 690, radius=28)}
{dcrop(R["alerts"], 1.0, 600, 470, ring="a4", radius=28)}
{dcrop(R["chart"], 1.2, 70, 930, radius=28)}
<div class="hz-abs" style="left:70px;top:1360px;font:600 40px Inter;color:{T}">Production · inventory · kitne log —<br><span style="color:{A}">woh bhi WhatsApp ke through</span></div>{SAMPLE(70, 1520, "rgba(19,32,27,.5)")}'''
    save("C5", body, C_BG, C_CSS)


def C6():
    body = f'''{face(70, 160, 940, 940, 230, 48)}
<div class="hz-abs" style="left:110px;top:900px;width:860px;padding:44px 50px;border-radius:40px;background:rgba(255,255,255,.72);backdrop-filter:blur(24px);border:2px solid #fff;box-shadow:0 30px 60px rgba(19,32,27,.14);z-index:5">
<div style="font:800 60px Inter;letter-spacing:-2px;line-height:1.05;color:{T}">Apni factory ka<br><span style="color:{A}">custom WhatsApp ERP</span></div>
<div style="font:600 32px Inter;color:#55665C;margin:16px 0 26px">₹15,000/mahine se shuru</div>
<span style="background:{CTA};color:{NAVY};border-radius:999px;padding:20px 38px;font:800 40px Inter">WhatsApp pe DM karo ↓</span></div>
{ph(90, 1390, .42, PRODUCTION[3][1], "")}{laptop(380, 1460, 600)}{WM(860, 100)}'''
    save("C6", body, C_BG, C_CSS)


if __name__ == "__main__":
    for f in [A1, A2, A3, A4, A5, A6, B1, B2, B3, B4, B5, B6, C1, C2, C3, C4, C5, C6]:
        f()
    print("ok")
