"""Round 2 storyboards (all fresh): D = Comic Panel Pop, E = Type Architecture, F = Isometric Mini Factory.
Palette P3 Sage Calm (locked). All data is SAMPLE data."""
import sys, os, math, random
sys.path.insert(0, os.path.dirname(__file__))
from comp import *

OUT = os.path.join(os.path.dirname(__file__), "frames2")
os.makedirs(OUT, exist_ok=True)
G, T, A, PR, PE, C, D = P['ground'], P['text'], P['accent'], P['problem'], P['pending'], P['card'], P['dark']
CTA, NAVY = P['cta'], P['navy']
PINK, MINT, AMB = "#F1DEDA", "#DDEDE1", "#E9C46A"


def save(name, html):
    open(f"{OUT}/{name}.html", "w").write(html)


def svg(inner, w=1080, h=1920, x=0, y=0, z=1, extra=""):
    return f'<svg class="hz-abs" style="left:{x}px;top:{y}px;z-index:{z};{extra}" width="{w}" height="{h}" viewBox="0 0 {w} {h}">{svg_defs()}{inner}</svg>'


def div(x, y, style, inner="", w=None, h=None, z=None):
    s = f"left:{x}px;top:{y}px;" + (f"width:{w}px;" if w else "") + (f"height:{h}px;" if h else "") + (f"z-index:{z};" if z else "")
    return f'<div class="hz-abs" style="{s}{style}">{inner}</div>'


SAMPLE = lambda x, y, c="rgba(19,32,27,.6)": f'<div class="hz-sample" style="left:{x}px;top:{y}px;color:{c};z-index:9">SAMPLE DATA</div>'
WORDMARK = lambda x, y, c=T, s=54: f'<div class="hz-abs" style="left:{x}px;top:{y}px;font:800 {s}px Inter;letter-spacing:-1px;color:{c};z-index:9">hivon<span style="color:{CTA}">.</span></div>'


def zig(seed, x=540, amp=46, step=96, y0=-20, y1=1960):
    r = random.Random(seed); pts = []; y = y0; sgn = 1
    while y <= y1:
        pts.append((x + sgn * r.uniform(amp * .55, amp), y)); sgn = -sgn; y += r.uniform(step * .7, step * 1.2)
    return pts


def halves(pts, gap):
    L = "0px 0px," + ",".join(f"{x-gap:.0f}px {y:.0f}px" for x, y in pts) + ",0px 1920px"
    R = ",".join(f"{x+gap:.0f}px {y:.0f}px" for x, y in pts) + ",1080px 1920px,1080px 0px"
    return L, R


def burst(cx, cy, r1, r2, n, fill, stroke=T, sw=8, rot=0):
    pts = []
    for i in range(n * 2):
        a = math.pi * i / n + rot; r = r1 if i % 2 == 0 else r2
        pts.append(f"{cx + r*math.cos(a):.0f},{cy + r*math.sin(a):.0f}")
    return f'<polygon points="{" ".join(pts)}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" stroke-linejoin="round"/>'


# =====================================================================
# D  COMIC PANEL POP   (madpencil-753990 comic style, pankajkumar-dev-718609 frame break)
# =====================================================================
def dots(c, a=.16, sz=20):
    return f"background-image:radial-gradient(rgba({c},{a}) 3px,transparent 3.6px);background-size:{sz}px {sz}px"


D_CSS = f"""
.cp{{position:absolute;border:8px solid {T};background:{C};box-shadow:14px 14px 0 {T};overflow:hidden}}
.cap{{position:absolute;background:{AMB};border:6px solid {T};padding:10px 22px;font:900 40px Inter;color:{T};letter-spacing:.01em;box-shadow:7px 7px 0 {T};z-index:8}}
.bub{{position:absolute;background:#fff;border:7px solid {T};border-radius:60px;padding:22px 32px;font:800 40px Inter;line-height:1.12;color:{T};z-index:8;text-align:center}}
.bub:after{{content:'';position:absolute;width:44px;height:44px;background:#fff;border-right:7px solid {T};border-bottom:7px solid {T};bottom:-29px;left:var(--tl,70px);transform:skewX(22deg) rotate(45deg)}}
.sfx{{position:absolute;font:italic 900 96px Inter;color:{PR};-webkit-text-stroke:5px {T};paint-order:stroke fill;letter-spacing:-2px;z-index:8;text-shadow:7px 7px 0 {T}}}
"""


def speed(cx, cy, n=28, r0=260, r1=1500, col="rgba(19,32,27,.14)", seed=2):
    r = random.Random(seed); o = []
    for i in range(n):
        a = 2 * math.pi * i / n + r.uniform(-.05, .05); w = r.uniform(.02, .05)
        o.append(f'<polygon points="{cx+r0*math.cos(a):.0f},{cy+r0*math.sin(a):.0f} {cx+r1*math.cos(a-w):.0f},{cy+r1*math.sin(a-w):.0f} {cx+r1*math.cos(a+w):.0f},{cy+r1*math.sin(a+w):.0f}" fill="{col}"/>')
    return "".join(o)


def D1():
    pts = zig(11, amp=58, step=150)
    L, R = halves(pts, 13)
    # LEFT: heavy desktop ERP with error popups, manuals, sweating owner
    cells = ''.join(f'<rect x="{96+c*62}" y="{618+r*36}" width="52" height="24" fill="{PR}" opacity="{.25+((r*3+c)%4)*.14}"/>' for r in range(6) for c in range(5))
    mon = f'''<g stroke="{T}" stroke-width="7" stroke-linejoin="round"><rect x="70" y="540" width="370" height="330" rx="12" fill="#fff"/><rect x="70" y="540" width="370" height="50" fill="{PR}"/>
<path d="M210 870 L300 870 L326 940 L184 940 Z" fill="#CDD8CF"/></g>{cells}
<g stroke="{T}" stroke-width="6"><rect x="150" y="690" width="250" height="120" fill="#fff" transform="rotate(-5 275 750)"/><rect x="60" y="770" width="230" height="100" fill="#fff" transform="rotate(4 175 820)"/></g>
<text x="276" y="768" text-anchor="middle" transform="rotate(-5 275 750)" font-family="Inter" font-weight="900" font-size="46" fill="{PR}">ERROR!</text>
<text x="176" y="836" text-anchor="middle" transform="rotate(4 175 820)" font-family="Inter" font-weight="800" font-size="30" fill="{T}">Step 14 of 32</text>'''
    books = ''.join(f'<rect x="{60+ (i%2)*14}" y="{1470 - i*46}" width="{200 - (i%3)*18}" height="46" rx="4" fill="{["#B5483F","#D9A79E","#C96D62","#E4C2BB"][i%4]}" stroke="{T}" stroke-width="6"/>' for i in range(5))
    sweat = f'<path d="M352 1130 q-14 22 0 30 q14 -8 0 -30z M440 1100 q-12 20 0 27 q12 -7 0 -27z" fill="#8EC5E8" stroke="{T}" stroke-width="4"/>'
    left = mon + books + f'<text x="160" y="1560" text-anchor="middle" font-family="Inter" font-weight="900" font-size="26" fill="{T}">MANUALS</text>' + person("owner", "comic", 250, 1130, 1.25, pose="head") + sweat
    # RIGHT: one phone, happy supervisor
    ph = f'''<g transform="translate(690,520) rotate(5)"><rect width="300" height="560" rx="46" fill="{T}"/><rect x="16" y="16" width="268" height="528" rx="32" fill="#EAE6DF"/>
<rect x="16" y="16" width="268" height="62" fill="#F6F6F6"/><circle cx="52" cy="48" r="17" fill="#0D0D0D"/><rect x="80" y="40" width="120" height="14" rx="7" fill="#101729"/>
<rect x="32" y="100" width="206" height="78" rx="12" fill="#fff"/><text x="46" y="130" font-family="Inter" font-weight="800" font-size="17" fill="#101729">🏭 Production Update</text><rect x="46" y="146" width="130" height="10" rx="5" fill="#9aa0a6"/>
<rect x="32" y="181" width="206" height="40" rx="0" fill="#EAF4FF"/><text x="135" y="208" text-anchor="middle" font-family="Inter" font-weight="700" font-size="18" fill="#1D8FF5">📝 Entry karein</text>
<rect x="110" y="246" width="160" height="50" rx="12" fill="#E2FBCB"/><text x="126" y="278" font-family="Inter" font-weight="600" font-size="18" fill="#101729">M-4 · 120 pcs</text>
<rect x="32" y="320" width="220" height="92" rx="12" fill="#fff"/><text x="46" y="354" font-family="Inter" font-weight="800" font-size="19" fill="{A}">✅ Logged!</text><rect x="46" y="372" width="150" height="10" rx="5" fill="#9aa0a6"/><rect x="46" y="390" width="100" height="10" rx="5" fill="#9aa0a6"/></g>'''
    right = ph + person("supervisor", "comic", 650, 1150, 1.25, pose="wave") + burst(930, 1240, 70, 40, 9, CTA, T, 6) + f'<path d="M900 1240 l22 22 l40 -46" stroke="{T}" stroke-width="12" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'
    body = f'''<div class="hz-abs" style="inset:0;background:{T}"></div>
<div class="hz-abs" style="inset:0;clip-path:polygon({L});background-color:{PINK};{dots('181,72,63',.2)}">{svg(left)}</div>
<div class="hz-abs" style="inset:0;clip-path:polygon({R});background-color:{MINT};{dots('47,125,87',.2)}">{svg(speed(830, 800, 22, 330, 1500, 'rgba(47,125,87,.12)') + right)}</div>
<div class="cap" style="left:60px;top:270px;transform:rotate(-3deg);background:#fff;color:{PR};font-size:54px">OTHER ERP</div>
<div class="cap" style="left:572px;top:270px;transform:rotate(2deg);background:#fff;color:{A};font-size:44px;white-space:nowrap">WHATSAPP ERP</div>
<div class="bub" style="left:60px;top:1000px;font-size:32px;--tl:150px">Yeh kaise<br>chalega?!</div>
<div class="bub" style="left:820px;top:1040px;font-size:32px;--tl:30px;padding:16px 26px">Ho gaya!</div>
{svg(burst(540, 930, 215, 140, 14, AMB, T, 9, .1) + burst(552, 942, 215, 140, 14, "none", "rgba(0,0,0,0)", 0), z=6)}
<div class="hz-abs" style="left:390px;top:850px;width:300px;text-align:center;font:italic 900 150px Inter;color:#fff;-webkit-text-stroke:8px {T};paint-order:stroke fill;text-shadow:9px 9px 0 {T};z-index:7;letter-spacing:-6px;transform:rotate(-6deg)">VS</div>
<div class="cap" style="left:215px;top:1650px;font-size:58px;transform:rotate(-1.5deg);background:{T};color:#fff;box-shadow:8px 8px 0 {A}">for MANUFACTURING</div>'''
    save("D1", page(body, G, D_CSS))


def D2():
    papers = ''.join(f'<g transform="translate({x},{y}) rotate({r})" stroke="{T}" stroke-width="6"><rect width="150" height="190" fill="#fff"/>{"".join(f"<line x1=\"22\" y1=\"{38+k*28}\" x2=\"{120-(k%2)*36}\" y2=\"{38+k*28}\" stroke-width=\"5\" opacity=\".45\"/>" for k in range(5))}</g>'
                     for x, y, r in [(90, 560, -20), (820, 520, 16), (150, 1010, 14), (800, 980, -12), (470, 470, 5)])
    reg = f'<g transform="translate(610,1290) rotate(7)" stroke="{T}" stroke-width="7"><rect width="340" height="200" rx="6" fill="{PINK}"/><line x1="170" y1="0" x2="170" y2="200"/>{"".join(f"<line x1=\"24\" y1=\"{40+k*34}\" x2=\"146\" y2=\"{40+k*34}\" stroke-width=\"4\" opacity=\".5\"/><line x1=\"194\" y1=\"{40+k*34}\" x2=\"316\" y2=\"{40+k*34}\" stroke-width=\"4\" opacity=\".5\"/>" for k in range(5))}</g>'
    phone_r = f'<g transform="translate(150,810) rotate(-16)"><rect width="120" height="200" rx="20" fill="{T}"/><rect x="10" y="12" width="100" height="176" rx="12" fill="#CFE9D6"/></g>'
    body = f'''<div class="cp" style="left:50px;top:230px;width:980px;height:1320px;background-color:{PINK};{dots('181,72,63',.18)}">
{svg(speed(540, 780, 30, 380, 1500, 'rgba(181,72,63,.13)') + papers + phone_r + reg + person("owner", "comic", 330, 640, 1.9, pose="head"), w=980, h=1320)}</div>
<div class="cap" style="left:30px;top:190px;transform:rotate(-2deg);font-size:46px">REASON 1</div>
<div class="hz-abs" style="left:110px;top:300px;font:900 104px Inter;letter-spacing:-3.5px;line-height:.98;color:{T};z-index:7;-webkit-text-stroke:0">Koi system<br><span style="background:{T};color:#fff;padding:0 18px">hi nahi</span></div>
<div class="sfx" style="left:60px;top:960px;font-size:84px;transform:rotate(-14deg)">TRING!</div>
<div class="bub" style="left:560px;top:690px;--tl:60px;font-size:38px">Register<br>kahan hai?!</div>
<div class="cap" style="left:70px;top:1500px;font-size:38px;background:#fff;transform:rotate(1deg);white-space:nowrap">Software laga bhi doge… <span style="color:{PR}">phir bhi FAIL</span></div>'''
    save("D2", page(body, G + ";" + dots('19,32,27', .07, 22), D_CSS))


def D3():
    ticks = ''.join(f'<div class="cap" style="left:{x}px;top:{y}px;background:#fff;font-size:36px;transform:rotate({r}deg)"><span style="color:{A}">✔</span> {t}</div>'
                    for x, y, r, t in [(70, 1290, -3, "System"), (390, 1330, 2, "Manpower"), (760, 1290, -2, "Time")])
    ph = f'''<g transform="translate(360,520) rotate(-7)"><rect x="14" y="14" width="360" height="680" rx="56" fill="{T}"/><rect width="360" height="680" rx="56" fill="#0D0D0D" stroke="{T}" stroke-width="8"/><rect x="20" y="20" width="320" height="640" rx="38" fill="#EAE6DF"/>
<rect x="20" y="20" width="320" height="76" fill="#F6F6F6"/><circle cx="66" cy="60" r="22" fill="#0D0D0D"/><text x="66" y="67" text-anchor="middle" font-family="Inter" font-weight="800" font-size="17" fill="#fff">HI</text><text x="100" y="67" font-family="Inter" font-weight="700" font-size="21" fill="#101729">Hivon Automations</text>
<rect x="40" y="124" width="250" height="100" rx="14" fill="#fff"/><text x="58" y="162" font-family="Inter" font-weight="800" font-size="22" fill="#101729">🏭 Production Update</text><rect x="58" y="182" width="170" height="12" rx="6" fill="#9aa0a6"/>
<rect x="40" y="227" width="250" height="48" fill="#EAF4FF"/><text x="165" y="259" text-anchor="middle" font-family="Inter" font-weight="700" font-size="21" fill="#1D8FF5">📝 Entry karein</text>
<rect x="130" y="304" width="190" height="60" rx="14" fill="#E2FBCB"/><text x="148" y="342" font-family="Inter" font-weight="600" font-size="21" fill="#101729">M-4 · 120 pcs</text>
<rect x="40" y="392" width="260" height="110" rx="14" fill="#fff"/><text x="58" y="434" font-family="Inter" font-weight="800" font-size="24" fill="{A}">✅ Logged!</text><rect x="58" y="454" width="180" height="12" rx="6" fill="#9aa0a6"/><rect x="58" y="474" width="120" height="12" rx="6" fill="#9aa0a6"/></g>'''
    body = f'''<div class="cp" style="left:50px;top:420px;width:980px;height:820px;background-color:{MINT};{dots('47,125,87',.2)}">{svg(speed(490, 400, 34, 300, 1400, 'rgba(47,125,87,.16)'), w=980, h=820)}</div>
{svg(ph, z=6)}
<div class="cap" style="left:60px;top:200px;transform:rotate(-2deg);font-size:40px;background:#fff">HIVON AUTOMATION</div>
<div class="hz-abs" style="left:60px;top:290px;font:italic 900 112px Inter;letter-spacing:-4px;color:{A};-webkit-text-stroke:7px {T};paint-order:stroke fill;text-shadow:8px 8px 0 {T};z-index:7">WhatsApp ERP</div>
<div class="sfx" style="left:700px;top:560px;color:{AMB};font-size:104px;transform:rotate(10deg)">POP!</div>
{ticks}
<div class="hz-abs" style="left:70px;top:1470px;right:70px;font:800 50px Inter;line-height:1.15;color:{T}">Yahi teeno cheezein<br><span style="background:{A};color:#fff;padding:0 14px">solve</span> karta hai</div>'''
    save("D3", page(body, G + ";" + dots('19,32,27', .07, 22), D_CSS))


def D4():
    ch, sh = chat_production("flow")
    mach = f'''<g transform="translate(40,560)" stroke="{T}" stroke-width="7" stroke-linejoin="round"><rect width="330" height="260" rx="14" fill="#B9CCBE"/><rect x="28" y="30" width="130" height="90" rx="8" fill="#fff"/>
<circle cx="240" cy="120" r="62" fill="#fff"/><circle cx="240" cy="120" r="18" fill="{T}"/><rect x="60" y="260" width="210" height="60" fill="#8FA596"/><rect x="270" y="28" width="36" height="26" rx="6" fill="{CTA}"/></g>
<text x="72" y="792" font-family="Inter" font-weight="900" font-size="44" fill="{T}">M-4</text>'''
    body = f'''<div class="cp" style="left:50px;top:230px;width:980px;height:1400px;background-color:{MINT};{dots('47,125,87',.18)}">{svg(mach + person("supervisor", "comic", 70, 860, 1.25, pose="phone"), w=980, h=1400)}</div>
{phone(420, 330, 1.34, ch, sh, extra=f"box-shadow:14px 14px 0 {T};z-index:6")}
<div class="cap" style="left:30px;top:190px;transform:rotate(-2deg);font-size:46px">Supervisor · machine se</div>
<div class="bub" style="left:60px;top:390px;--tl:120px;font-size:36px;padding:18px 26px">Aaj ki<br>production?</div>
<div class="sfx" style="left:70px;top:1500px;color:{CTA};font-size:84px;transform:rotate(-8deg)">EK INPUT!</div>
{SAMPLE(90, 1660)}'''
    save("D4", page(body, G + ";" + dots('19,32,27', .07, 22), D_CSS))


def D5():
    k = (kpi("Today Production", "1,240", "pcs · Shift A", DB['deep'], "⚙️", DB['mint'], "position:absolute;left:40px;top:140px;width:435px;border:5px solid " + T) +
         kpi("Inventory", "312", "SKUs in stock", DB['ink'], "📦", "#F1F2F5", "position:absolute;left:495px;top:140px;width:435px;border:5px solid " + T) +
         kpi("Today Present", "94", "checked in", DB['green'], "🗓️", DB['mint'], "position:absolute;left:40px;top:365px;width:435px;border:5px solid " + T) +
         kpi("Pending Inward", "3", "gate entries", DB['amber'], "🚚", "#FDF1DD", "position:absolute;left:495px;top:365px;width:435px;border:5px solid " + T))
    body = f'''<div class="cp" style="left:50px;top:230px;width:980px;height:1090px;background:{DB['canvas']}">
<div style="position:absolute;left:40px;top:50px;font:800 42px Inter;color:{T}">Hivon ERP <span style="font-weight:500;color:{DB['muted']};font-size:30px">· Management Overview</span></div>
{k}{alerts(ALERT_ROWS[:3], 0, extra="position:absolute;left:40px;top:595px;width:890px;border:5px solid " + T)}</div>
{svg(burst(900, 800, 90, 58, 11, AMB, T, 7, .2), z=7)}
<div class="hz-abs" style="left:848px;top:774px;font:italic 900 44px Inter;color:{T};z-index:8;transform:rotate(-10deg)">NEW!</div>
<div class="cap" style="left:30px;top:170px;transform:rotate(-2deg);font-size:46px">Live status · ek dashboard</div>
{svg(person("owner", "comic", 90, 1290, 1.35, pose="wave"), z=6)}
<div class="bub" style="left:400px;top:1380px;--tl:40px;font-size:40px;border-radius:50px">Sab kuch <span style="color:{A}">live</span><br>dikh raha hai!</div>
{SAMPLE(420, 1640)}'''
    save("D5", page(body, G + ";" + dots('19,32,27', .07, 22), D_CSS))


def D6():
    body = f'''<div class="cp" style="left:50px;top:230px;width:980px;height:900px;background:{MINT}">{face_placeholder(0, 0, 964, 884, "HEYGEN FACE · placeholder", radius=0, bg="#CFDCD1")}</div>
<div class="cap" style="left:30px;top:150px;transform:rotate(-2deg);font-size:42px;background:#fff">hivon<span style="color:{CTA}">.</span> WhatsApp ERP</div>
<div class="bub" style="left:70px;top:1120px;width:940px;border-radius:70px;padding:44px 50px;text-align:left;--tl:200px;transform:none">
<div style="font:900 66px Inter;letter-spacing:-2px;line-height:1.02">Apni factory ka<br><span style="color:{A}">custom WhatsApp ERP?</span></div>
<div style="font:700 34px Inter;margin-top:16px;opacity:.75">₹15,000/mahine se shuru</div></div>
<div class="hz-abs" style="left:190px;top:1500px;background:{CTA};border:7px solid {NAVY};box-shadow:10px 10px 0 {T};padding:26px 44px;font:900 54px Inter;color:{NAVY};transform:rotate(-2deg);z-index:9">WhatsApp pe DM karo ↓</div>'''
    save("D6", page(body, G + ";" + dots('19,32,27', .07, 22), D_CSS))


# =====================================================================
# E  TYPE ARCHITECTURE  (gdgtify-929495: words are load-bearing structure)
# =====================================================================
E_CSS = f""".tb{{position:absolute;font:900 120px Inter;letter-spacing:-4px;line-height:.86;white-space:nowrap}}
.mono{{position:absolute;font:600 26px 'JetBrains Mono';letter-spacing:.08em}}
.serif{{font-family:'DejaVu Serif';font-style:italic;font-weight:700;letter-spacing:-1px}}"""
flat = lambda role, x, y, s, pose="stand", flip=False: person(role, "pill", x, y, s, pose=pose, flip=flip)


def E1():
    pts = zig(5, amp=30, step=120)
    L, R = halves(pts, 9)
    words = [("MODULES", -3, 0), ("MANUALS", 4, 22), ("TRAINING", -2, -10), ("CONSULTANT", 3, 14), ("LICENCE", -5, -6), ("SOFTWARE", 2, 8)]
    pile = ''.join(f'<div class="tb" style="left:{28+dx}px;top:{560+i*128}px;font-size:{80 if len(w)<9 else 54}px;color:{"#E8A69E" if i%2 else "#fff"};transform:rotate({r}deg);-webkit-text-stroke:0">{w}</div>' for i, (w, r, dx) in enumerate(words))
    left = f'''<div class="mono" style="left:60px;top:250px;color:#E8A69E">01 — OTHER ERP</div>
<div class="tb" style="left:54px;top:300px;font-size:128px;color:#fff">OTHER<br><span style="color:#E8A69E">ERP</span></div>{pile}
{svg(f'<g opacity=".95">{flat("owner", 190, 1330, 1.25, "head")}</g><path d="M60 1740 h440" stroke="#E8A69E" stroke-width="6"/>')}
<div class="mono" style="left:60px;top:1760px;color:#E8A69E;font-size:24px">SEEKHNA PADTA HAI</div>'''
    right = f'''<div class="mono" style="left:600px;top:250px;color:{A}">02 — WHATSAPP ERP</div>
<div class="tb" style="left:596px;top:300px;font-size:104px;color:{T}">WHATS<br>APP <span style="color:{A}">ERP</span></div>
<div class="hz-abs" style="left:700px;top:780px;width:330px;height:520px;border-radius:60px 60px 60px 12px;background:{A};box-shadow:0 30px 50px rgba(47,125,87,.3)"></div>
<div class="tb" style="left:730px;top:840px;font-size:190px;color:#fff;line-height:.8">EK<br><span style="font-size:92px;letter-spacing:-4px">CLICK</span></div>
<div class="hz-abs" style="left:734px;top:1200px;font:700 34px Inter;color:#DFF3E6">✓✓ 10:42</div>
{svg(flat("worker", 700, 1330, 1.25, "phone") + f'<path d="M600 1740 h420" stroke="{A}" stroke-width="6"/>')}
<div class="mono" style="left:600px;top:1760px;color:{A};font-size:24px">SAB JAANTE HAIN</div>'''
    crack = "M" + " L".join(f"{x:.0f} {y:.0f}" for x, y in pts)
    body = f'''<div class="hz-abs" style="inset:0;background:#0A120F"></div>
<div class="hz-abs" style="inset:0;clip-path:polygon({L});background:{D}">{left}</div>
<div class="hz-abs" style="inset:0;clip-path:polygon({R});background:{G}">{right}</div>
{svg(f'<path d="{crack}" stroke="{AMB}" stroke-width="4" fill="none" opacity=".9"/>', z=5)}
<div class="hz-abs" style="left:400px;top:960px;width:270px;height:190px;background:{AMB};display:flex;align-items:center;justify-content:center;font:900 150px Inter;letter-spacing:-8px;color:{T};z-index:6;transform:rotate(-4deg);box-shadow:0 24px 50px rgba(0,0,0,.35)">VS</div>
<div class="hz-abs" style="left:0;right:0;top:150px;text-align:center;z-index:6"><span style="background:{C};color:{T};padding:10px 30px;font:800 54px Inter;letter-spacing:-1px">for <span class="serif" style="color:{A};font-size:58px">Manufacturing</span></span></div>'''
    save("E1", page(body, D, E_CSS))


def E2():
    letters = [("S", 60, 720, -4, 1), ("Y", 250, 700, 6, 1), ("S", 420, 760, -9, .5), ("T", 590, 690, 3, 1), ("E", 730, 900, 38, 1), ("M", 820, 1250, -62, 1)]
    ls = ''.join(f'<div class="tb" style="left:{x}px;top:{y}px;font-size:300px;color:{"#fff" if o==1 else "transparent"};{"-webkit-text-stroke:5px #E8A69E;" if o!=1 else ""}transform:rotate({r}deg)">{c}</div>' for c, x, y, r, o in letters)
    body = f'''<div class="mono" style="left:90px;top:250px;color:#E8A69E">REASON 01 / 03</div>
<div class="tb" style="left:84px;top:300px;font-size:150px;color:#fff">KOI</div>
{ls}
<div class="tb" style="left:84px;top:1090px;font-size:150px;color:#E8A69E">HI NAHI</div>
{svg(flat("owner", 380, 1250, 1.5, "shrug") + f'<path d="M90 1736 h900" stroke="#fff" stroke-width="6"/><path d="M700 1000 q40 60 20 130 M780 980 q60 80 60 200" stroke="#E8A69E" stroke-width="4" fill="none" stroke-dasharray="10 12"/>')}
<div class="hz-abs" style="left:90px;top:1756px;font:600 36px Inter;color:#fff;opacity:.85">Software laga bhi doge, <span class="serif" style="color:#E8A69E">phir bhi fail</span></div>'''
    save("E2", page(body, D, E_CSS))


def E3():
    ticks = ''.join(f'<line x1="{60+i*40}" y1="1000" x2="{60+i*40}" y2="{1040 if i%5 else 1070}" stroke="{T}" stroke-width="4"/>' for i in range(26))
    months = ''.join(f'<text x="{60+i*200}" y="1120" font-family="JetBrains Mono" font-weight="600" font-size="28" fill="{T}">M{i+1}</text>' for i in range(6))
    body = f'''<div class="mono" style="left:90px;top:250px;color:{PR}">REASON 03 / 03</div>
<div class="tb" style="left:84px;top:300px;font-size:110px;color:{T}">Implementation<br><span style="color:{PR}">time</span></div>
<div class="tb" style="left:60px;top:700px;font-size:250px;color:{PR};letter-spacing:-10px;line-height:.8">LAMBAAAAAA</div>
{svg(f'<rect x="60" y="990" width="1020" height="10" fill="{T}"/>' + ticks + months + flat("worker", 30, 1210, 1.4, "point") + f'<path d="M250 1400 L1080 1400" stroke="{T}" stroke-width="7" stroke-dasharray="2 18" stroke-linecap="round"/><path d="M1000 1370 l60 30 l-60 30" stroke="{T}" stroke-width="7" fill="none"/>')}
<div class="hz-abs" style="left:330px;top:1230px;font:800 54px Inter;letter-spacing:-1px;color:{T}">kheechta hi<br>jaata hai<span style="color:{PR}">…</span></div>
<div class="mono" style="left:90px;top:1700px;color:{T};opacity:.6">→ SCREEN SE BAHAR</div>'''
    save("E3", page(body, G, E_CSS))


def E4():
    ch, sh = chat_production("flow")
    body = f'''<div class="tb" style="left:-20px;top:420px;font-size:560px;color:{A};opacity:.16;letter-spacing:-30px">EK</div>
<div class="tb" style="left:40px;top:1180px;font-size:300px;color:{A};opacity:.16;letter-spacing:-16px">INPUT</div>
<div class="mono" style="left:90px;top:250px;color:{A}">SUPERVISOR · MACHINE M-4</div>
<div class="tb" style="left:84px;top:300px;font-size:104px;color:{T}">Machine se<br><span class="serif" style="color:{A};font-size:110px">ek input</span></div>
{phone(330, 560, 1.42, ch, sh)}
{svg(flat("supervisor", 40, 1300, 1.45, "phone"), z=5)}
{SAMPLE(90, 1800)}'''
    save("E4", page(body, G, E_CSS))


def E5():
    body = f'''<div class="mono" style="left:90px;top:250px;color:{A}">HIVON ERP · LIVE</div>
<div class="tb" style="left:76px;top:290px;font-size:330px;color:{T};letter-spacing:-16px">1,240</div>
<div class="hz-abs" style="left:90px;top:640px;font:800 54px Inter;letter-spacing:-1px;color:{T}">pcs aaj ki <span class="serif" style="color:{A};font-size:58px">production</span></div>
<div class="hz-abs" style="left:90px;top:770px;width:900px;display:flex;gap:24px">
<div style="flex:1;border-top:8px solid {T};padding-top:14px"><div style="font:900 120px Inter;letter-spacing:-5px;color:{T}">312</div><div class="mono" style="position:static;color:{T};opacity:.65">INVENTORY · SKUs</div></div>
<div style="flex:1;border-top:8px solid {T};padding-top:14px"><div style="font:900 120px Inter;letter-spacing:-5px;color:{A}">94</div><div class="mono" style="position:static;color:{T};opacity:.65">LOG PRESENT</div></div></div>
{alerts(ALERT_ROWS, 0, extra="position:absolute;left:70px;top:1050px;width:940px;box-shadow:0 24px 50px rgba(19,32,27,.14)")}
<div class="hz-abs" style="left:90px;top:1590px;font:800 58px Inter;letter-spacing:-1.5px;color:{T}">Ek single dashboard,<br><span style="color:{A}">woh bhi WhatsApp se</span></div>
{SAMPLE(90, 1790)}'''
    save("E5", page(body, G, E_CSS))


def E6():
    body = f'''{face_placeholder(70, 230, 940, 800, "HEYGEN FACE · placeholder", radius=0, bg="#2A3B33", ink="#DDEDE1")}
<div class="tb" style="left:60px;top:1010px;font-size:400px;color:{CTA};letter-spacing:-20px;z-index:4">DM</div>
<div class="tb" style="left:730px;top:1100px;font-size:108px;color:#fff;z-index:4">kar<br>do <span style="color:{CTA}">↓</span></div>
<div class="hz-abs" style="left:76px;top:1400px;font:800 56px Inter;letter-spacing:-1.5px;line-height:1.08;color:#fff">Apni factory ka<br>custom <span class="serif" style="color:{CTA};font-size:60px">WhatsApp ERP</span></div>
<div class="hz-abs" style="left:76px;top:1570px;display:flex;gap:22px;align-items:center"><span style="background:{CTA};color:{NAVY};font:800 36px Inter;padding:20px 32px">WhatsApp number neeche</span><span class="mono" style="position:static;color:#fff;opacity:.8;font-size:28px">₹15,000/MAHINE SE</span></div>
{WORDMARK(800, 1740, "#fff")}'''
    save("E6", page(body, D, E_CSS))


# =====================================================================
# F  ISOMETRIC MINI FACTORY  (niegramotny-197521 low-poly from code, thegrootdev-966114 UI chips)
# =====================================================================
def iso(x, y, z=0, ox=540, oy=900, s=1.0):
    return (ox + (x - y) * 0.866 * s, oy + (x + y) * 0.5 * s - z * s)


def shade(hexc, f):
    h = hexc.lstrip('#'); r, g, b = [int(h[i:i+2], 16) for i in (0, 2, 4)]
    if f < 1: r, g, b = [int(v * f) for v in (r, g, b)]
    else: r, g, b = [int(v + (255 - v) * (f - 1)) for v in (r, g, b)]
    return f"#{r:02x}{g:02x}{b:02x}"


class Iso:
    def __init__(self, ox, oy, s=1.0):
        self.ox, self.oy, self.s, self.items = ox, oy, s, []

    def p(self, x, y, z):
        a, b = iso(x, y, z, self.ox, self.oy, self.s); return f"{a:.1f},{b:.1f}"

    def box(self, x, y, z, w, d, h, col, key=None, op=1, stroke=None):
        st = f' stroke="{stroke}" stroke-width="2" stroke-linejoin="round"' if stroke else ''
        top = f'<polygon points="{self.p(x,y,z+h)} {self.p(x+w,y,z+h)} {self.p(x+w,y+d,z+h)} {self.p(x,y+d,z+h)}" fill="{shade(col,1.18)}"{st}/>'
        lf = f'<polygon points="{self.p(x,y+d,z+h)} {self.p(x+w,y+d,z+h)} {self.p(x+w,y+d,z)} {self.p(x,y+d,z)}" fill="{col}"{st}/>'
        rt = f'<polygon points="{self.p(x+w,y,z+h)} {self.p(x+w,y+d,z+h)} {self.p(x+w,y+d,z)} {self.p(x+w,y,z)}" fill="{shade(col,.8)}"{st}/>'
        self.items.append((key if key is not None else x + y + w / 2 + d / 2 + z * .01, f'<g opacity="{op}">{top}{lf}{rt}</g>'))

    def raw(self, key, s):
        self.items.append((key, s))

    def pt(self, x, y, z=0):
        return iso(x, y, z, self.ox, self.oy, self.s)

    def machine(self, x, y, col="#8FB39C", lamp=CTA, op=1):
        self.box(x, y, 0, 90, 70, 46, col, op=op)
        self.box(x + 8, y + 8, 46, 40, 54, 44, shade(col, .9), key=x + y + 80.2, op=op)
        self.box(x + 58, y + 20, 46, 22, 30, 18, "#F8FBF8", key=x + y + 80.4, op=op)
        cx, cy = self.pt(x + 28, y + 35, 108)
        self.raw(x + y + 80.6, f'<circle cx="{cx:.0f}" cy="{cy:.0f}" r="{9*self.s:.0f}" fill="{lamp}" opacity="{op}"/>')

    def desk(self, x, y):
        self.box(x, y, 0, 80, 50, 30, "#C9B6A6")
        self.box(x + 22, y + 14, 30, 36, 8, 34, "#5A6B62", key=x + y + 65.2)
        cx, cy = self.pt(x + 40, y + 22, 50)
        self.raw(x + y + 65.4, f'<rect x="{cx-4:.0f}" y="{cy-14:.0f}" width="{26*self.s:.0f}" height="{14*self.s:.0f}" fill="{PR}" transform="skewY(30)" opacity="0"/>')

    def stack(self, x, y, n, cols=("#B5483F", "#D9A79E", "#C96D62", "#E4C2BB")):
        for i in range(n):
            self.box(x + (i % 2) * 4, y - (i % 3) * 3, i * 13, 46, 34, 12, cols[i % 4], key=x + y + 40 + i * .01)

    def person(self, x, y, shirt=A, hat=None, op=1, z=0):
        cx, cy = self.pt(x, y, z); s = self.s
        o = f'<g opacity="{op}"><ellipse cx="{cx:.0f}" cy="{cy:.0f}" rx="{17*s:.0f}" ry="{8*s:.0f}" fill="rgba(19,32,27,.22)"/>'
        o += f'<rect x="{cx-12*s:.0f}" y="{cy-52*s:.0f}" width="{24*s:.0f}" height="{50*s:.0f}" rx="{12*s:.0f}" fill="{shirt}"/>'
        o += f'<circle cx="{cx:.0f}" cy="{cy-64*s:.0f}" r="{13*s:.0f}" fill="#C98B5B"/>'
        if hat: o += f'<path d="M{cx-14*s:.0f} {cy-66*s:.0f} a{14*s:.0f} {14*s:.0f} 0 0 1 {28*s:.0f} 0z" fill="{hat}"/><rect x="{cx-17*s:.0f}" y="{cy-68*s:.0f}" width="{34*s:.0f}" height="{5*s:.0f}" rx="2" fill="{hat}"/>'
        self.raw(x + y + 6, o + '</g>')

    def chip(self, x, y, z, text, bg="#fff", fg=T, key=9999, fs=24):
        cx, cy = self.pt(x, y, z); w = len(text) * fs * .58 + 34
        self.raw(key, f'<g><path d="M{cx:.0f} {cy+26:.0f} l-10 -14 h20z" fill="{bg}"/><rect x="{cx-w/2:.0f}" y="{cy-34:.0f}" width="{w:.0f}" height="48" rx="24" fill="{bg}" stroke="rgba(19,32,27,.15)" stroke-width="2"/><text x="{cx:.0f}" y="{cy-2:.0f}" text-anchor="middle" font-family="Inter" font-weight="800" font-size="{fs}" fill="{fg}">{text}</text></g>')

    def out(self):
        return "".join(s for _, s in sorted(self.items, key=lambda t: t[0]))


F_CSS = f"""body{{background:radial-gradient(110% 60% at 50% 50%,#F2F7F3 0%,{G} 60%,#D5E2D8 100%)}}
.ft{{position:absolute;font:900 92px Inter;letter-spacing:-3px;line-height:.98;color:{T}}}
.fl{{position:absolute;font:700 28px Inter;letter-spacing:.18em}}
.fchip{{position:absolute;background:#fff;border-radius:999px;padding:14px 26px;font:800 30px Inter;color:{T};box-shadow:0 12px 26px rgba(19,32,27,.14);z-index:7}}"""


def island(I, size, col, edge):
    I.box(0, 0, -44, size, size, 44, col, key=-1000)
    # jagged broken inner edge blocks
    return I


def F1():
    # left island: chaos
    Lf = Iso(270, 960, 1.0); Lf.box(0, 0, -50, 300, 300, 50, "#E7CFCA", key=-1e4)
    for (x, y) in [(20, 30), (150, 20), (30, 170)]: Lf.desk(x, y)
    Lf.stack(210, 150, 9); Lf.stack(120, 230, 6); Lf.stack(236, 236, 4); Lf.stack(150, 110, 5)
    Lf.person(120, 175, "#F3EBDD"); Lf.person(250, 80, "#9A6A12", op=.9)
    Lf.chip(60, 50, 120, "ERROR", PR, "#fff"); Lf.chip(190, 40, 120, "Step 14/32", "#fff", PR, fs=22); Lf.chip(230, 170, 150, "manual?", "#fff", T, fs=22)
    # right island: tidy
    Rt = Iso(810, 960, 1.0); Rt.box(0, 0, -50, 300, 300, 50, "#CFE3D4", key=-1e4)
    for (x, y) in [(30, 30), (170, 30), (30, 180), (170, 180)]: Rt.machine(x, y)
    Rt.person(140, 120, "#3E6FA8", "#F4C542"); Rt.person(280, 260, A, A)
    Rt.chip(75, 65, 150, "✓ 120 pcs", CTA, NAVY); Rt.chip(215, 215, 150, "✓ Present", CTA, NAVY, fs=22); Rt.chip(215, 65, 150, "✓ Inward", "#fff", A, fs=22)
    pts = zig(21, amp=40, step=110, y0=330, y1=1490)
    crack = "M" + " L".join(f"{x:.0f} {y:.0f}" for x, y in pts)
    shards = ''.join(f'<polygon points="{x},{y} {x+w},{y-h*.5} {x+w*.4},{y+h}" fill="{c}" opacity=".9"/>' for x, y, w, h, c in [(500, 1130, 34, 30, "#E7CFCA"), (560, 1180, 28, 26, "#CFE3D4"), (520, 1240, 20, 22, "#E7CFCA"), (575, 1100, 18, 18, "#CFE3D4"), (535, 1320, 16, 16, "#CFE3D4")])
    body = f'''<div class="hz-abs" style="left:0;top:0;width:540px;height:1920px;background:linear-gradient(90deg,rgba(181,72,63,.13),rgba(181,72,63,.03))"></div>
{svg(f'<path d="{crack}" stroke="{T}" stroke-width="9" fill="none" stroke-linejoin="bevel"/><path d="{crack}" stroke="#fff" stroke-width="3" fill="none" transform="translate(6,0)"/>' + Lf.out() + Rt.out() + shards)}
<div class="fl" style="left:70px;top:260px;color:{PR}">PURANA TAREEKA</div>
<div class="ft" style="left:64px;top:300px;font-size:84px;color:{PR}">Other<br>ERP</div>
<div class="fl" style="left:600px;top:260px;color:{A}">NAYA TAREEKA</div>
<div class="ft" style="left:594px;top:300px;font-size:84px;color:{A}">WhatsApp<br>ERP</div>
<div class="hz-abs" style="left:410px;top:540px;width:260px;height:260px;z-index:6">
<div style="position:absolute;left:12px;top:14px;width:240px;height:240px;border-radius:56px;background:{T};transform:rotate(45deg) scale(.82)"></div>
<div style="position:absolute;left:0;top:0;width:240px;height:240px;border-radius:56px;background:#fff;border:6px solid {T};transform:rotate(45deg) scale(.82);margin:6px"></div>
<div style="position:absolute;left:0;right:0;top:66px;text-align:center;font:900 112px Inter;letter-spacing:-5px;color:{T}">VS</div></div>
<div class="fchip" style="left:50px;top:1400px;font-size:27px;color:{PR}">Software seekhna padta hai</div>
<div class="fchip" style="left:580px;top:1400px;font-size:27px;color:{A}">WhatsApp par chalta hai</div>
<div class="hz-abs" style="left:0;right:0;top:1520px;text-align:center;font:900 84px Inter;letter-spacing:-3px;color:{T}">for <span style="color:{A}">Manufacturing</span></div>
<div class="hz-abs" style="left:0;right:0;top:1630px;text-align:center;font:600 36px Inter;color:{T};opacity:.7">ERP fail kyun hota hai?</div>'''
    save("F1", page(body, G, F_CSS))


def factory(I, staffed=(3,), n=6, lamp_on=None):
    I.box(0, 0, -44, 520, 520, 44, "#D3E3D7", key=-1e4)
    I.box(0, 0, 0, 520, 14, 90, "#BFD3C4", key=-9e3); I.box(0, 14, 0, 14, 506, 90, "#C7D9CC", key=-9e3 + 1)
    pos = [(70, 70), (250, 70), (400, 70), (70, 260), (250, 260), (400, 260)][:n]
    for i, (x, y) in enumerate(pos):
        on = i in staffed
        I.machine(x, y, "#8FB39C" if on else "#B9C7BD", CTA if on else PR, op=1)
        if on: I.person(x + 45, y + 110, "#3E6FA8", "#F4C542")
    return pos


def F2():
    I = Iso(540, 760, .98)
    pos = factory(I, staffed=(4,))
    for i, (x, y) in enumerate(pos):
        if i != 4: I.chip(x + 40, y + 30, 140, "khaali", "#fff", PR, fs=22)
    I.chip(295, 300, 150, "skilled ✓", CTA, NAVY)
    I.stack(60, 430, 5, ("#C9B6A6", "#E2D5C9", "#B9A493", "#E2D5C9")); I.stack(130, 440, 3, ("#C9B6A6", "#E2D5C9", "#B9A493", "#E2D5C9"))
    body = f'''{svg(I.out())}
<div class="fl" style="left:90px;top:250px;color:{PR}">REASON 02</div>
<div class="ft" style="left:84px;top:296px">Skilled manpower<br><span style="color:{PR}">bahut kam</span></div>
<div class="hz-abs" style="left:90px;top:1420px;display:flex;gap:26px;align-items:flex-end">
<div style="font:900 190px Inter;letter-spacing:-8px;color:{PR};line-height:.8">1<span style="color:{T};opacity:.3">/6</span></div>
<div style="font:700 40px Inter;line-height:1.2;color:{T};padding-bottom:6px">machine par hi<br>skilled operator</div></div>
<div class="hz-abs" style="left:90px;top:1640px;font:600 34px Inter;color:{T};opacity:.7">SME manufacturing ki asli dikkat · illustration</div>'''
    save("F2", page(body, G, F_CSS))


def F3():
    I = Iso(540, 800, .98)
    I.box(0, 0, -44, 520, 520, 44, "#D3E3D7", key=-1e4)
    I.machine(60, 60); I.machine(380, 80); I.machine(80, 380)
    I.box(230, 220, 0, 90, 90, 12, "#F8FBF8", key=450); I.box(380, 380, 0, 90, 90, 12, "#F8FBF8", key=770)
    # path
    path_pts = [I.pt(110, 170, 2), I.pt(275, 265, 14), I.pt(425, 425, 14)]
    pth = "M" + " L".join(f"{a:.0f} {b:.0f}" for a, b in path_pts)
    I.raw(300, f'<path d="{pth}" stroke="{A}" stroke-width="9" fill="none" stroke-dasharray="4 20" stroke-linecap="round"/>')
    I.person(110, 170, "#F3EBDD"); I.person(150, 190, A, None)
    I.person(275, 265, A, None, z=12); I.person(425, 425, "#3E6FA8", "#F4C542", z=12)
    I.chip(110, 150, 190, "1 · Business seekhna", "#fff", T, fs=24)
    I.chip(275, 245, 150, "2 · SOPs", CTA, NAVY, fs=26)
    I.chip(425, 405, 120, "3 · Implement", "#fff", T, fs=24)
    body = f'''{svg(I.out())}
<div class="fl" style="left:90px;top:250px;color:{A}">HIVON KA TAREEKA</div>
<div class="ft" style="left:84px;top:296px;font-size:86px">Pehle aapka<br>business <span style="color:{A}">seekhte hain</span></div>
<div class="hz-abs" style="left:90px;top:1440px;width:900px;font:800 54px Inter;letter-spacing:-1px;line-height:1.15;color:{T}">Phir SOPs, jo <span style="color:{A}">small-medium</span><br>factory mein chal sakein</div>
<div class="hz-abs" style="left:90px;top:1630px;font:600 34px Inter;color:{T};opacity:.7">Aapko hamara software na seekhna pade</div>'''
    save("F3", page(body, G, F_CSS))


def F4():
    ch, sh = chat_production("flow")
    I = Iso(230, 1500, 1.3)
    I.box(0, 0, -30, 220, 190, 30, "#D3E3D7", key=-1e4)
    I.machine(40, 40); I.person(150, 150, "#3E6FA8", "#F4C542")
    I.chip(85, 75, 150, "M-4", "#fff", T, fs=30)
    a = I.pt(150, 150, 70)
    body = f'''{svg(I.out() + f'<path d="M{a[0]+20:.0f} {a[1]:.0f} C {a[0]+90:.0f} {a[1]-120:.0f}, 430 1150, 470 1090" stroke="{A}" stroke-width="7" fill="none" stroke-dasharray="4 18" stroke-linecap="round"/>', z=1)}
<div class="fl" style="left:90px;top:250px;color:{A}">SUPERVISOR · KISI BHI MACHINE SE</div>
<div class="ft" style="left:84px;top:296px;font-size:88px">Ek input,<br><span style="color:{A}">production update</span></div>
{phone(440, 520, 1.3, ch, sh)}
{SAMPLE(90, 1760)}'''
    save("F4", page(body, G, F_CSS))


def F5():
    I = Iso(540, 520, .62)
    pos = factory(I, staffed=(0, 1, 2, 3, 4, 5))
    I.chip(295, 300, 150, "M-4 · 120 pcs", CTA, NAVY, fs=22)
    I.chip(110, 110, 150, "Present 94", "#fff", T, fs=20); I.chip(440, 110, 150, "Stock 312", "#fff", T, fs=20)
    lines = ''.join(f'<path d="M{x} 800 C {x} 860, {x2} 860, {x2} 930" stroke="{A}" stroke-width="6" fill="none" stroke-dasharray="3 14" stroke-linecap="round"/>' for x, x2 in [(380, 290), (540, 540), (700, 790)])
    k = (kpi("Production", "1,240", "pcs today", DB['deep'], "⚙️", DB['mint'], "position:absolute;left:60px;top:940px;width:310px;padding:20px 22px") +
         kpi("Inventory", "312", "SKUs", DB['ink'], "📦", "#F1F2F5", "position:absolute;left:385px;top:940px;width:310px;padding:20px 22px") +
         kpi("Present", "94", "log aaj", DB['green'], "🗓️", DB['mint'], "position:absolute;left:710px;top:940px;width:310px;padding:20px 22px"))
    body = f'''{svg(I.out() + lines)}
<div class="fl" style="left:90px;top:230px;color:{A}">LIVE STATUS</div>
<div class="ft" style="left:84px;top:270px;font-size:80px">Poori factory, <span style="color:{A}">ek dashboard</span></div>
{k}{alerts(ALERT_ROWS[:3], 0, extra="position:absolute;left:60px;top:1180px;width:960px;box-shadow:0 24px 50px rgba(19,32,27,.14)")}
<div class="hz-abs" style="left:90px;top:1640px;font:800 44px Inter;color:{T}">Woh bhi <span style="color:{A}">WhatsApp ke through</span></div>
{SAMPLE(90, 1730)}'''
    save("F5", page(body, G, F_CSS))


def F6():
    I = Iso(840, 1560, .5)
    factory(I, staffed=(0, 2, 4))
    body = f'''{face_placeholder(70, 230, 940, 860, "HEYGEN FACE · placeholder", radius=48)}
{svg(I.out(), z=4)}
<div class="fl" style="left:90px;top:1150px;color:{A}">CUSTOM SOFTWARE</div>
<div class="ft" style="left:84px;top:1196px;font-size:84px">Apni factory ka<br><span style="color:{A}">WhatsApp ERP</span></div>
<div class="hz-abs" style="left:90px;top:1410px;font:700 36px Inter;color:{T};opacity:.75">₹15,000/mahine se shuru</div>
<div class="hz-abs" style="left:90px;top:1500px;background:{CTA};color:{NAVY};font:800 40px Inter;padding:24px 36px;border-radius:999px;border:3px solid {NAVY};z-index:6">WhatsApp pe DM karo ↓</div>
{WORDMARK(90, 1660)}'''
    save("F6", page(body, G, F_CSS))


if __name__ == "__main__":
    fs = [D1, D2, D3, D4, D5, D6, E1, E2, E3, E4, E5, E6, F1, F2, F3, F4, F5, F6]
    only = sys.argv[1:]
    for f in fs:
        if not only or f.__name__ in only: f()
    print("ok")
