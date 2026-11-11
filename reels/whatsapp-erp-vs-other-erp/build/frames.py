import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from comp import *

OUT = os.path.join(os.path.dirname(__file__), "frames")
os.makedirs(OUT, exist_ok=True)
G, T, A, PR, PE, C, D = P['ground'], P['text'], P['accent'], P['problem'], P['pending'], P['card'], P['dark']


def save(name, html):
    open(f"{OUT}/{name}.html", "w").write(html)


def svg(inner, w=1080, h=1920, x=0, y=0, z=1):
    return f'<svg class="hz-abs" style="left:{x}px;top:{y}px;z-index:{z}" width="{w}" height="{h}" viewBox="0 0 {w} {h}">{svg_defs()}{inner}</svg>'


def tag(text, x, y, color=T, size=26, extra=""):
    return f'<div class="hz-abs" style="left:{x}px;top:{y}px;font:800 {size}px Inter;letter-spacing:.16em;color:{color};{extra}">{text}</div>'


SAMPLE = lambda x, y, c="rgba(19,32,27,.55)": f'<div class="hz-sample" style="left:{x}px;top:{y}px;color:{c}">SAMPLE DATA</div>'
WORDMARK = lambda x, y, c=T, s=54: f'<div class="hz-abs" style="left:{x}px;top:{y}px;font:800 {s}px Inter;letter-spacing:-1px;color:{c}">hivon<span style="color:{P["cta"]}">.</span></div>'

# =====================================================================
# A  BLUEPRINT LINE  (heyiamnick-119558: one pencil line, drafting table)
# =====================================================================
GRID = f"background-color:{G};background-image:linear-gradient(rgba(47,125,87,.13) 2px,transparent 2px),linear-gradient(90deg,rgba(47,125,87,.13) 2px,transparent 2px),linear-gradient(rgba(47,125,87,.06) 1px,transparent 1px),linear-gradient(90deg,rgba(47,125,87,.06) 1px,transparent 1px);background-size:300px 300px,300px 300px,60px 60px,60px 60px"
GRID_D = "background-color:#13201B;background-image:linear-gradient(rgba(159,211,181,.14) 2px,transparent 2px),linear-gradient(90deg,rgba(159,211,181,.14) 2px,transparent 2px),linear-gradient(rgba(159,211,181,.06) 1px,transparent 1px),linear-gradient(90deg,rgba(159,211,181,.06) 1px,transparent 1px);background-size:300px 300px,300px 300px,60px 60px,60px 60px"
INK = f'stroke="{T}" stroke-width="5" fill="none" stroke-linecap="round" stroke-linejoin="round"'
CRACK = "M540 120 L552 260 L528 380 L560 520 L532 660 L556 800 L524 940 L560 1080 L530 1220 L554 1360 L526 1500 L548 1640 L536 1800"


def A1():
    # left half: Other ERP (dense desktop), right: WhatsApp ERP (one phone)
    menus = ''.join(f'<rect x="{78+ (i%2)*0}" y="{560+i*26}" width="{90 if i%3 else 120}" height="12" rx="3" fill="{PR}" opacity=".55"/>' for i in range(12))
    grid_cells = ''.join(f'<rect x="{200+c*70}" y="{560+r*44}" width="58" height="30" rx="4" fill="url(#hatchc)" stroke="{PR}" stroke-width="2"/>' for r in range(7) for c in range(4))
    wires = f'<path d="M120 900 C 200 1000, 60 1040, 160 1080 S 330 1020, 280 1120 S 120 1160, 220 1200" stroke="{PR}" stroke-width="4" fill="none"/>'
    left = f'''
<rect x="60" y="500" width="430" height="340" rx="14" {INK}/><rect x="60" y="500" width="430" height="40" rx="14" fill="url(#hatchc)" stroke="{T}" stroke-width="5"/>
{menus}{grid_cells}<path d="M240 840 L310 840 L330 890 L220 890 Z" {INK}/>{wires}
<g transform="translate(70,1280)"><rect width="150" height="200" rx="8" fill="url(#hatchc)" stroke="{T}" stroke-width="5"/><text x="75" y="105" text-anchor="middle" font="" font-family="Inter" font-weight="800" font-size="22" fill="{T}">USER</text><text x="75" y="132" text-anchor="middle" font-family="Inter" font-weight="800" font-size="22" fill="{T}">MANUAL</text></g>
{person("worker","line",240,1240,1.0,pose="head")}'''
    right = f'''
<g transform="translate(700,470)"><rect width="250" height="470" rx="40" {INK}/><rect x="18" y="40" width="214" height="400" rx="14" fill="#F8FBF8" stroke="{T}" stroke-width="3"/>
<rect x="34" y="70" width="150" height="58" rx="12" fill="#fff" stroke="{T}" stroke-width="3"/><rect x="48" y="86" width="100" height="9" rx="4" fill="{T}"/><rect x="48" y="104" width="70" height="9" rx="4" fill="#9aa0a6"/>
<rect x="34" y="138" width="150" height="34" rx="0 0 12 12" fill="#EAF4FF" stroke="{T}" stroke-width="3"/><text x="109" y="161" text-anchor="middle" font-family="Inter" font-weight="700" font-size="16" fill="#1D8FF5">Entry karein</text>
<rect x="66" y="196" width="150" height="46" rx="12" fill="#E2FBCB" stroke="{T}" stroke-width="3"/><rect x="80" y="214" width="90" height="9" rx="4" fill="{T}"/>
<rect x="34" y="262" width="160" height="82" rx="12" fill="#fff" stroke="{T}" stroke-width="3"/><text x="50" y="292" font-family="Inter" font-weight="800" font-size="17" fill="{A}">✓ Logged</text><rect x="50" y="306" width="110" height="9" rx="4" fill="#9aa0a6"/><rect x="50" y="322" width="80" height="9" rx="4" fill="#9aa0a6"/></g>
{person("supervisor","line",720,1240,1.0,pose="wave")}'''
    crack = f'<path d="{CRACK}" stroke="{T}" stroke-width="7" fill="none" stroke-linejoin="bevel"/><path d="{CRACK}" transform="translate(9,4)" stroke="rgba(19,32,27,.25)" stroke-width="3" fill="none"/>'
    body = f'''<div class="hz-abs" style="left:0;top:0;width:540px;height:1920px;background:rgba(181,72,63,.07)"></div>
{svg(left + right + crack)}
{tag("OTHER ERP", 70, 300, PR, 56, "letter-spacing:.04em")}
{tag("WHATSAPP<br>ERP", 680, 270, A, 56, "letter-spacing:.04em;line-height:1.02")}
<div class="hz-abs" style="left:420px;top:780px;width:240px;height:240px;border-radius:50%;background:{C};border:6px solid {T};display:flex;align-items:center;justify-content:center;font:italic 700 118px 'DejaVu Serif';color:{T};box-shadow:10px 10px 0 rgba(19,32,27,.18);z-index:3">vs</div>
<div class="hz-abs" style="left:0;right:0;top:1620px;text-align:center;font:800 70px Inter;color:{T};z-index:3">for <span style="font:italic 700 74px 'DejaVu Serif';color:{A}">Manufacturing</span></div>'''
    save("A1", page(body, G, f"body{{{GRID}}}"))


def headline_wall(active, x=90, y=200, dim=.28, color=T, acc=PR, size=78):
    rows = [("01", "Koi system hi nahi"), ("02", "Skilled manpower kam"), ("03", "Implementation lamba")]
    h = ""
    for i, (n, t) in enumerate(rows):
        on = i == active
        h += f'<div style="display:flex;gap:26px;align-items:baseline;opacity:{1 if on else dim};margin-bottom:18px;transform:translateY({-12 if on else 0}px)"><span style="font:700 40px \'JetBrains Mono\';color:{acc if on else color}">{n}</span><span style="font:800 {size}px Inter;color:{color};letter-spacing:-1.5px;line-height:1.05;{"text-decoration:underline;text-decoration-color:"+acc+";text-decoration-thickness:8px;text-underline-offset:12px" if on else ""}">{t}</span></div>'
    return f'<div class="hz-abs" style="left:{x}px;top:{y}px;width:930px;z-index:3">{h}</div>'


def A2():
    papers = ''.join(f'<g transform="translate({x},{y}) rotate({r})"><rect width="130" height="160" rx="6" fill="#F8FBF8" stroke="{T}" stroke-width="4"/>{"".join(f"<line x1=\"18\" y1=\"{30+k*24}\" x2=\"{100 - (k%2)*30}\" y2=\"{30+k*24}\" stroke=\"{T}\" stroke-width=\"3\" opacity=\".5\"/>" for k in range(5))}</g>'
                     for x, y, r in [(90, 900, -18), (800, 860, 14), (130, 1300, 10), (790, 1280, -12), (700, 1070, 24)])
    phone_ring = f'<g transform="translate(250,1040) rotate(-14)"><rect width="90" height="150" rx="16" fill="#F8FBF8" stroke="{T}" stroke-width="5"/><path d="M-20 30 q-14 30 0 60 M-40 18 q-22 42 0 84 M110 30 q14 30 0 60 M130 18 q22 42 0 84" stroke="{PR}" stroke-width="4" fill="none" stroke-linecap="round"/></g>'
    reg = f'<g transform="translate(560,1480) rotate(6)"><rect width="300" height="190" rx="8" fill="url(#hatchc)" stroke="{T}" stroke-width="5"/><line x1="150" y1="0" x2="150" y2="190" stroke="{T}" stroke-width="4"/><text x="150" y="-14" text-anchor="middle" font-family="Inter" font-weight="800" font-size="24" fill="{T}">REGISTER</text></g>'
    q = ''.join(f'<text x="{x}" y="{y}" font-family="DejaVu Serif" font-style="italic" font-weight="700" font-size="{s}" fill="{PR}">?</text>' for x, y, s in [(330, 940, 90), (690, 1000, 70), (600, 860, 56)])
    body = f'''{headline_wall(0)}
{svg(papers + phone_ring + reg + q + person("owner", "line", 380, 1000, 1.45, pose="head"))}
<div class="hz-abs" style="left:90px;top:1720px;right:90px;font:700 40px Inter;color:{T};z-index:3">Software laga bhi doge, <span style="background:{PR};color:#fff;padding:2px 12px;border-radius:8px">phir bhi fail</span></div>'''
    save("A2", page(body, G, f"body{{{GRID}}}"))


def A3():
    lg = "#9FD3B5"
    # the pencil line promoted into a phone outline (pull-back)
    line = f'''<path d="M60 1180 C 260 1180, 300 1180, 360 1180 L360 640 Q360 600 400 600 L680 600 Q720 600 720 640 L720 1320 Q720 1360 680 1360 L400 1360 Q360 1360 360 1320 L360 1180" stroke="{lg}" stroke-width="7" fill="none" stroke-linecap="round"/>
<circle cx="60" cy="1180" r="12" fill="{lg}"/>
<rect x="390" y="680" width="300" height="80" rx="14" fill="none" stroke="#55B685" stroke-width="4"/><rect x="390" y="772" width="300" height="44" rx="10" fill="none" stroke="#55B685" stroke-width="4"/>
<rect x="470" y="842" width="220" height="64" rx="14" fill="none" stroke="#55B685" stroke-width="4"/>
<rect x="390" y="930" width="300" height="120" rx="14" fill="rgba(85,182,133,.12)" stroke="#55B685" stroke-width="4"/>
<path d="M412 990 l20 20 l36 -40" stroke="#55B685" stroke-width="7" fill="none" stroke-linecap="round"/>
<g font-family="Inter" font-weight="700" font-size="30" fill="{lg}" letter-spacing="3">
<text x="760" y="720">SYSTEM ✓</text><text x="760" y="900">MANPOWER ✓</text><text x="760" y="1080">TIME ✓</text></g>
<path d="M724 708 h28 M724 888 h28 M724 1068 h28" stroke="{lg}" stroke-width="3" stroke-dasharray="6 6"/>'''
    body = f'''{svg(line)}
<div class="hz-abs" style="left:90px;top:230px;font:700 30px Inter;letter-spacing:.3em;color:{lg}">HIVON AUTOMATION</div>
<div class="hz-abs" style="left:86px;top:290px;font:900 124px Inter;letter-spacing:-3px;line-height:.95;color:#F2F6F3">WhatsApp<br><span style="color:#55B685">ERP</span></div>
<div class="hz-abs" style="left:90px;top:1480px;right:90px;font:600 44px Inter;line-height:1.25;color:#F2F6F3">Yahi <span style="font:italic 700 50px 'DejaVu Serif';color:#55B685">teeno</span> cheezon ko solve karta hai</div>'''
    save("A3", page(body, D, f"body{{{GRID_D}}}"))


def A4():
    ch, sh = chat_production("flow")
    machine = f'''<g transform="translate(40,860)"><rect width="330" height="210" rx="16" fill="url(#hatch)" stroke="{T}" stroke-width="5"/><rect x="30" y="34" width="120" height="80" rx="8" fill="#F8FBF8" stroke="{T}" stroke-width="4"/>
<circle cx="245" cy="105" r="52" fill="#F8FBF8" stroke="{T}" stroke-width="5"/><circle cx="245" cy="105" r="16" fill="{T}"/><text x="40" y="180" font-family="Inter" font-weight="800" font-size="34" fill="{T}">M-4</text>
<rect x="70" y="210" width="190" height="40" fill="none" stroke="{T}" stroke-width="5"/></g>'''
    body = f'''<div class="hz-abs" style="left:90px;top:170px;font:800 64px Inter;letter-spacing:-1.5px;line-height:1.05;color:{T};z-index:3">Machine pe baithe<br><span style="font:italic 700 68px 'DejaVu Serif';color:{A}">ek input</span></div>
{svg(machine + person("supervisor","line",60,1300,1.2,pose="phone"))}
{phone(420,420,1.38,ch,sh)}
<svg class="hz-abs" style="left:300px;top:1180px;z-index:4" width="200" height="120"><path d="M10 100 C 60 20, 120 10, 180 40" stroke="{T}" stroke-width="5" fill="none" stroke-dasharray="10 10"/><path d="M168 24 l16 18 -22 8" stroke="{T}" stroke-width="5" fill="none"/></svg>
{SAMPLE(90, 1790)}'''
    save("A4", page(body, G, f"body{{{GRID}}}"))


def A5():
    k = (kpi("Today Production", "1,240", "pcs · Shift A", DB['deep'], "⚙️", DB['mint'], "position:absolute;left:70px;top:420px;width:460px") +
         kpi("Inventory", "312", "SKUs in stock", DB['ink'], "📦", "#F1F2F5", "position:absolute;left:550px;top:420px;width:460px") +
         kpi("Today Present", "94", "checked in", DB['green'], "🗓️", DB['mint'], "position:absolute;left:70px;top:640px;width:460px") +
         kpi("Pending Inward", "3", "gate entries", DB['amber'], "🚚", "#FDF1DD", "position:absolute;left:550px;top:640px;width:460px"))
    chart = f'''<div class="hd-card" style="position:absolute;left:70px;top:870px;width:940px;padding:24px 28px"><div style="font:800 27px Inter">Production by machine</div><div style="font:16px Inter;color:{DB['muted']};margin-bottom:8px">Today · pcs</div>
{bars([62,78,55,92,70,48],880,250,hl=3,labels=["M-1","M-2","M-3","M-4","M-5","M-6"])}</div>'''
    body = f'''<div class="hz-abs" style="left:70px;top:170px;font:800 66px Inter;letter-spacing:-1.5px;color:{T}">Live status, <span style="font:italic 700 70px 'DejaVu Serif';color:{A}">ek dashboard</span></div>
<div class="hz-abs" style="left:72px;top:262px;font:600 30px Inter;color:{T};opacity:.7">Hivon ERP · Management Overview</div>
{k}{chart}{alerts(ALERT_ROWS[:3],0,extra="position:absolute;left:70px;top:1260px;width:940px")}{SAMPLE(72, 1820)}'''
    save("A5", page(body, G, f"body{{{GRID}}}"))


def A6():
    corner = ''.join(f'<path d="{d}" stroke="{T}" stroke-width="6" fill="none"/>' for d in ["M70 170 v-50 h50", "M1010 170 v-50 h-50", "M70 1090 v50 h50", "M1010 1090 v50 h-50"])
    body = f'''{face_placeholder(90, 140, 900, 980, "HEYGEN FACE · placeholder")}{svg(corner)}
<div class="hz-abs" style="left:70px;top:1180px;width:940px;padding:40px 44px;border-radius:28px;background:rgba(248,251,248,.82);backdrop-filter:blur(18px);border:2px solid #fff;box-shadow:0 20px 40px rgba(19,32,27,.12);z-index:3">
<div style="font:700 28px Inter;letter-spacing:.14em;color:{A}">CUSTOM SOFTWARE</div>
<div style="font:800 62px Inter;letter-spacing:-1.5px;line-height:1.05;color:{T};margin:10px 0 18px">Apni factory ka<br>WhatsApp ERP</div>
<div style="display:flex;gap:18px;align-items:center"><span style="background:{P['cta']};color:{P['navy']};font:800 34px Inter;padding:20px 30px;border-radius:18px;border:3px solid {P['navy']}">WhatsApp pe DM karo ↓</span>
<span style="font:700 28px Inter;color:{T};opacity:.75">₹15,000/mahine se</span></div></div>
{WORDMARK(70, 1700)}'''
    save("A6", page(body, G, f"body{{{GRID}}}"))


# =====================================================================
# B  PAPER THEATRE  (x4b47x-034026 shadow theatre + tomandrieu96707-875264 collage)
# =====================================================================
NOISE = '%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%22300%22 height=%22300%22%3E%3Cfilter id=%22n%22%3E%3CfeTurbulence type=%22fractalNoise%22 baseFrequency=%22.8%22 numOctaves=%223%22/%3E%3CfeColorMatrix values=%220 0 0 0 0.07 0 0 0 0 0.12 0 0 0 0 0.1 0 0 0 .07 0%22/%3E%3C/filter%3E%3Crect width=%22300%22 height=%22300%22 filter=%22url(%23n)%22/%3E%3C/svg%3E'
PAPER_BG = f"background-color:{G};background-image:url('data:image/svg+xml;utf8,{NOISE}')"
B_CSS = f"""body{{{PAPER_BG}}}
.pc-sheet{{position:absolute;background:{C};box-shadow:0 10px 0 rgba(19,32,27,.10),0 18px 30px rgba(19,32,27,.16)}}
.pc-tape{{position:absolute;width:150px;height:46px;background:rgba(214,226,206,.75);border:1px solid rgba(19,32,27,.08);z-index:6}}
.pc-label{{position:absolute;background:{C};padding:14px 26px;font:800 44px Inter;color:{T};box-shadow:0 6px 0 rgba(19,32,27,.12);z-index:5}}"""


def torn(points_side, x0, x1, y0=0, y1=1920, seed=1, amp=26, step=60):
    import random
    rnd = random.Random(seed); pts = []
    y = y0
    while y <= y1:
        pts.append((x1 + rnd.uniform(-amp, amp), y)); y += step
    return pts


def B1():
    import random
    rnd = random.Random(3)
    edge = [(540 + rnd.uniform(-34, 34), y) for y in range(0, 1981, 55)]
    left_poly = "0px 0px," + ",".join(f"{x-14:.0f}px {y}px" for x, y in edge) + ",0px 1920px"
    right_poly = ",".join(f"{x+14:.0f}px {y}px" for x, y in edge) + ",1080px 1920px,1080px 0px"
    binders = ''.join(f'<rect x="{80+i*58}" y="{720 - (i%2)*16}" width="52" height="{250 + (i%2)*16}" rx="6" fill="{["#B5483F","#C7705F","#9E3E37","#B5483F","#D08A72"][i]}"/><rect x="{92+i*58}" y="{760- (i%2)*16}" width="28" height="40" fill="#F8FBF8" opacity=".7"/>' for i in range(5))
    tangle = f'<path d="M90 1080 C 200 980, 330 1180, 220 1120 S 80 1240, 260 1260 S 420 1150, 330 1300 S 140 1330, 200 1400" stroke="{PR}" stroke-width="7" fill="none" stroke-linecap="round"/>'
    mon = f'<g filter="url(#paperdrop)"><rect x="80" y="480" width="380" height="210" rx="14" fill="#5A6B62"/><rect x="96" y="496" width="348" height="170" rx="6" fill="#DCE5DE"/>' + ''.join(f'<rect x="{110+c*84}" y="{510+r*30}" width="72" height="18" rx="3" fill="{PR}" opacity="{.3 + (r+c)%3*.15}"/>' for r in range(5) for c in range(4)) + '</g>'
    left_art = f'<g filter="url(#paperdrop)">{binders}</g>{mon}<g filter="url(#paperdrop)">{tangle}</g>{person("owner","paper",250,1380,1.05,pose="head")}'
    ph = f'''<g transform="translate(660,560) rotate(4)" filter="url(#paperdrop)"><rect width="300" height="560" rx="44" fill="#0D0D0D"/><rect x="16" y="16" width="268" height="528" rx="32" fill="#EAE6DF"/>
<rect x="34" y="70" width="200" height="74" rx="12" fill="#fff"/><rect x="50" y="88" width="130" height="10" rx="5" fill="#101729"/><rect x="50" y="110" width="90" height="10" rx="5" fill="#9aa0a6"/>
<rect x="34" y="148" width="200" height="38" fill="#EAF4FF"/><text x="134" y="173" text-anchor="middle" font-family="Inter" font-weight="700" font-size="17" fill="#1D8FF5">Entry karein</text>
<rect x="90" y="214" width="176" height="52" rx="12" fill="#E2FBCB"/><rect x="106" y="234" width="110" height="10" rx="5" fill="#101729"/>
<rect x="34" y="292" width="210" height="96" rx="12" fill="#fff"/><text x="50" y="326" font-family="Inter" font-weight="800" font-size="20" fill="{A}">✅ Logged!</text><rect x="50" y="344" width="140" height="10" rx="5" fill="#9aa0a6"/></g>'''
    right_art = ph + person("worker", "paper", 650, 1340, 1.05, pose="phone")
    body = f'''<div class="hz-abs" style="inset:0;background:{D}"></div>
<div class="hz-abs" style="inset:0;clip-path:polygon({left_poly});background:#F3E4E0;{PAPER_BG.replace(G,'#F3E4E0')}">{svg(left_art)}</div>
<div class="hz-abs" style="inset:0;clip-path:polygon({right_poly});background:#EAF4EC;{PAPER_BG.replace(G,'#EAF4EC')}">{svg(right_art)}</div>
<div class="pc-label" style="left:60px;top:250px;transform:rotate(-3deg);color:{PR}">OTHER ERP</div>
<div class="pc-label" style="left:610px;top:250px;transform:rotate(2deg);color:{A}">WHATSAPP ERP</div>
<div class="hz-abs" style="left:395px;top:820px;width:290px;height:200px;border:9px solid {T};border-radius:22px;display:flex;align-items:center;justify-content:center;font:900 130px Inter;color:{T};transform:rotate(-8deg);background:rgba(248,251,248,.88);z-index:7;letter-spacing:-4px">VS</div>
<div class="pc-label" style="left:250px;top:1730px;font-size:52px;transform:rotate(-1.5deg)">for Manufacturing</div>
<div class="pc-tape" style="left:220px;top:1715px;transform:rotate(-30deg)"></div><div class="pc-tape" style="left:740px;top:1712px;transform:rotate(26deg)"></div>'''
    save("B1", page(body, G, B_CSS))


def B2():
    # shadow theatre: dark stage, glowing sage light, silhouettes
    sil = "#07100C"
    stage = f'''<defs><radialGradient id="spot" cx="50%" cy="48%" r="55%"><stop offset="0" stop-color="#7FB08F"/><stop offset=".55" stop-color="#3F6B54"/><stop offset="1" stop-color="#13201B"/></radialGradient></defs>
<rect width="1080" height="1920" fill="url(#spot)"/>
<g fill="{sil}">{"".join(f'<rect x="{x}" y="{y}" width="110" height="140" rx="4" transform="rotate({r} {x+55} {y+70})"/>' for x,y,r in [(120,640,-20),(820,600,16),(180,1000,12),(780,980,-14),(470,560,6)])}
<rect x="240" y="820" width="70" height="120" rx="12" transform="rotate(-16 275 880)"/>
<path d="M0 1560 Q540 1500 1080 1560 L1080 1920 L0 1920Z"/></g>
<g style="filter:brightness(0)">{person("owner","paper",360,980,1.7,pose="head")}</g>
<path d="M200 800 q-20 40 0 80 M330 790 q22 42 0 84" stroke="{sil}" stroke-width="7" fill="none" stroke-linecap="round"/>'''
    body = f'''{svg(stage)}
<div class="pc-label" style="left:90px;top:220px;font-size:36px;transform:rotate(-2deg);color:{PR}">REASON 01</div>
<div class="hz-abs" style="left:90px;top:300px;font:900 96px Inter;letter-spacing:-2.5px;line-height:1;color:#F2F6F3;z-index:4">Koi system<br>hi nahi</div>
<svg class="hz-abs" style="left:50px;top:400px;z-index:5" width="560" height="160"><path d="M14 90 C 10 30, 200 6, 380 18 S 560 70, 520 112 S 200 160, 60 130 S 20 100, 40 70" stroke="#F0B3A9" stroke-width="7" fill="none" stroke-linecap="round" filter="url(#rough)"/>{svg_defs()}</svg>
<div class="pc-sheet" style="left:110px;top:1630px;width:860px;padding:22px 30px;transform:rotate(-1deg);font:700 38px Inter;color:{T};z-index:5">Software laga bhi doge, phir bhi <span style="color:{PR}">fail</span></div>'''
    save("B2", page(body, D, B_CSS))


def B3():
    items = [("Pehle aapka business seekhte hain", True), ("Phir aapke SOPs banaate hain", True), ("SME factory mein implement", False)]
    rows = ''.join(f'''<div style="display:flex;gap:26px;align-items:center;margin:26px 0"><div style="width:70px;height:70px;border:6px solid {T};border-radius:12px;flex:none;display:flex;align-items:center;justify-content:center;background:#fff">
{"<svg width='54' height='54'><path d='M8 28 l14 14 l26 -32' stroke='"+A+"' stroke-width='9' fill='none' stroke-linecap='round'/></svg>" if done else ""}</div>
<div style="font:800 48px Inter;letter-spacing:-1px;color:{T};line-height:1.1;{"" if done else "opacity:.45"}">{t}</div></div>''' for t, done in items)
    body = f'''<div class="pc-sheet" style="left:70px;top:230px;width:940px;height:760px;padding:56px 60px;transform:rotate(-1.2deg)">
<div style="font:700 30px Inter;letter-spacing:.16em;color:{A}">HIVON KA TAREEKA</div>{rows}</div>
<div class="pc-tape" style="left:110px;top:200px;transform:rotate(-14deg)"></div><div class="pc-tape" style="left:820px;top:205px;transform:rotate(12deg)"></div>
{svg(person("owner","paper",160,1130,1.5,pose="point") + person("store","paper",640,1130,1.5,pose="carry",flip=True) +
 f'<g transform="translate(470,1280) rotate(-8)" filter="url(#paperdrop)"><rect width="150" height="190" rx="6" fill="#F8FBF8"/><text x="75" y="58" text-anchor="middle" font-family="Inter" font-weight="900" font-size="38" fill="{A}">SOP</text>' + ''.join(f'<rect x="24" y="{84+k*24}" width="{100-k%2*30}" height="8" rx="4" fill="{T}" opacity=".45"/>' for k in range(4)) + '</g>')}
<div class="hz-abs" style="left:90px;top:1770px;font:700 34px Inter;color:{T};opacity:.75">Aapko hamara software na seekhna pade</div>'''
    save("B3", page(body, G, B_CSS))


def B4():
    ch, sh = chat_production("flow")
    body = f'''<div class="pc-sheet" style="left:110px;top:300px;width:860px;height:1420px;transform:rotate(1.5deg);background:#EAF4EC"></div>
<div class="pc-label" style="left:90px;top:170px;transform:rotate(-2deg)">Supervisor: <span style="color:{A}">ek input</span></div>
{phone(250,380,1.3,ch,sh,rot=-2)}
<div class="pc-tape" style="left:250px;top:360px;transform:rotate(-38deg)"></div><div class="pc-tape" style="left:700px;top:1530px;transform:rotate(-38deg)"></div>
{svg(person("supervisor","paper",20,1400,1.15,pose="point"))}
<svg class="hz-abs" style="left:300px;top:1305px;z-index:9" width="580" height="150">{svg_defs()}<ellipse cx="290" cy="75" rx="275" ry="62" stroke="{PR}" stroke-width="7" fill="none" filter="url(#rough)"/></svg>
{SAMPLE(130, 1790)}'''
    save("B4", page(body, G, B_CSS))


def B5():
    body = f'''<div class="pc-label" style="left:80px;top:170px;transform:rotate(-1.5deg)">Live status · <span style="color:{A}">dashboard</span></div>
<div class="pc-sheet" style="left:60px;top:300px;width:960px;height:1080px;transform:rotate(-1deg);background:{DB['canvas']}">
<div style="display:flex;gap:20px;padding:40px 40px 0">{kpi("Production","1,240","pcs today",DB['deep'],"⚙️",DB['mint'],"flex:1")}{kpi("Present","94","Shift A",DB['green'],"🗓️",DB['mint'],"flex:1")}</div>
<div style="padding:20px 40px 0">{kpi("Inventory","312","SKUs in stock",DB['ink'],"📦","#F1F2F5")}</div>
<div style="padding:20px 40px">{alerts(ALERT_ROWS[:3],0)}</div></div>
<div class="pc-tape" style="left:70px;top:285px;transform:rotate(-24deg)"></div><div class="pc-tape" style="left:870px;top:280px;transform:rotate(22deg)"></div>
<svg class="hz-abs" style="left:70px;top:760px;z-index:9" width="960" height="170">{svg_defs()}<path d="M30 90 C 20 14, 500 4, 905 20 S 960 140, 820 158 S 120 172, 40 128" stroke="{PR}" stroke-width="7" fill="none" filter="url(#rough)"/></svg>
<div class="hz-abs" style="left:560px;top:1450px;font:italic 700 50px 'DejaVu Serif';color:{PR};transform:rotate(-4deg)">← same entry!</div>{SAMPLE(80, 1760)}'''
    save("B5", page(body, G, B_CSS))


def B6():
    body = f'''<div class="pc-sheet" style="left:50px;top:90px;width:980px;height:1720px;background:{C}"></div>
<div class="hz-abs" style="left:90px;top:120px;font:900 150px Inter;letter-spacing:-6px;color:{T};z-index:3">hivon<span style="color:{P['cta']}">.</span></div>
<div class="hz-abs" style="left:96px;top:300px;font:700 24px Inter;letter-spacing:.2em;color:{T};opacity:.6;z-index:3">ISSUE: WHATSAPP ERP · FOR MANUFACTURING</div>
{face_placeholder(90, 350, 900, 1000, "HEYGEN FACE · placeholder", radius=6)}
<div class="hz-abs" style="left:90px;top:1380px;width:900px;z-index:3">
<div style="font:900 74px Inter;letter-spacing:-2px;line-height:1;color:{T}">Custom WhatsApp ERP<br><span style="color:{A}">aapki factory ke liye</span></div>
<div style="font:700 34px Inter;color:{T};margin-top:20px;opacity:.75">₹15,000/mahine se shuru</div></div>
<div class="hz-abs" style="left:700px;top:330px;width:270px;height:270px;border-radius:50%;background:{P['cta']};border:5px solid {P['navy']};display:flex;align-items:center;justify-content:center;text-align:center;font:900 40px Inter;line-height:1.05;color:{P['navy']};transform:rotate(-10deg);z-index:6">DM karo<br><span style="font-size:30px">WhatsApp ↓</span></div>'''
    save("B6", page(body, G, B_CSS))


# =====================================================================
# C  ONE SHAPE, FROSTED GLASS  (sanjeevn72-457691 morph + twoclipping-000267 minimal)
# =====================================================================
C_CSS = f"""body{{background:radial-gradient(120% 70% at 50% 35%,#F4F8F5 0%,{G} 55%,#D3E1D6 100%)}}
.gl{{position:absolute;background:rgba(248,251,248,.62);backdrop-filter:blur(22px);border:2px solid rgba(255,255,255,.9);border-radius:40px;box-shadow:0 30px 60px rgba(19,32,27,.14),inset 0 1px 0 #fff}}
.gl-chip{{position:absolute;background:rgba(248,251,248,.8);backdrop-filter:blur(14px);border:2px solid #fff;border-radius:999px;padding:16px 28px;font:700 30px Inter;color:{T};box-shadow:0 14px 30px rgba(19,32,27,.12);z-index:6}}
.blob{{position:absolute;border-radius:50%;filter:blur(60px);opacity:.55}}"""


def C1():
    desk = ''.join(f'<div style="height:16px;width:{60+ (i*37)%90}%;background:{PR};opacity:{.18+(i%4)*.08};border-radius:6px;margin:10px 0"></div>' for i in range(14))
    tabs = ''.join(f'<span style="display:inline-block;padding:6px 10px;margin:3px;border-radius:6px;background:rgba(181,72,63,.14);font:600 15px Inter;color:{PR}">Module {i+1}</span>' for i in range(12))
    cracks = f'''<path d="M540 0 L548 300 L530 560 L556 760 L540 900 L522 1100 L552 1340 L536 1600 L546 1920" stroke="#fff" stroke-width="6" fill="none"/>
<path d="M540 900 L430 840 M540 900 L650 820 M540 900 L620 1010 M540 900 L450 990 M548 300 L620 250 M522 1100 L440 1160" stroke="#fff" stroke-width="3" fill="none" opacity=".9"/>'''
    body = f'''<div class="blob" style="left:-100px;top:300px;width:600px;height:600px;background:#E8B8B0"></div><div class="blob" style="left:600px;top:900px;width:600px;height:600px;background:#9FD3B5"></div>
<div style="position:absolute;inset:0;perspective:1400px">
<div class="gl" style="left:40px;top:330px;width:470px;height:1240px;transform:rotateY(14deg);padding:40px 34px;filter:saturate(.75)">
<div style="font:800 46px Inter;color:{PR};letter-spacing:-1px">Other ERP</div><div style="margin:14px 0">{tabs}</div>{desk}</div>
<div class="gl" style="left:570px;top:330px;width:470px;height:1240px;transform:rotateY(-14deg);padding:40px 34px">
<div style="font:800 46px Inter;color:{A};letter-spacing:-1px">WhatsApp ERP</div>
<div style="margin:60px auto 0;width:300px;height:560px;border-radius:44px;background:#0D0D0D;padding:12px"><div style="height:100%;border-radius:34px;background:#EAE6DF;padding:70px 16px">
<div style="background:#fff;border-radius:12px;padding:12px;font:700 16px Inter;color:#101729">🏭 Production Update<div style="font:400 14px Inter;margin-top:6px">Entry karein</div></div>
<div style="background:#fff;margin-top:2px;padding:9px;text-align:center;font:600 15px Inter;color:#1D8FF5;border-radius:0 0 12px 12px">📝 Entry karein</div>
<div style="background:#fff;border-radius:12px;padding:12px;font:800 16px Inter;color:{A};margin-top:14px">✅ Logged!</div></div></div></div></div>
{svg(cracks, z=4)}
<div class="gl-chip" style="left:430px;top:815px;width:220px;height:170px;border-radius:40px;display:flex;align-items:center;justify-content:center;font:900 96px Inter;letter-spacing:-3px;padding:0">VS</div>
<div class="hz-abs" style="left:0;right:0;top:150px;text-align:center;font:600 34px Inter;letter-spacing:.24em;color:{T};opacity:.7">FOR MANUFACTURING</div>
<div class="hz-abs" style="left:0;right:0;top:1650px;text-align:center;font:800 64px Inter;letter-spacing:-1.5px;color:{T}">Kaunsa <span style="color:{A}">chalega?</span></div>'''
    save("C1", page(body, G, C_CSS))


def C2():
    ppl = ''
    for i in range(12):
        r, c = divmod(i, 4); hl = i in (5,)
        ppl += f'<g opacity="{1 if hl else .28}">{person("worker" if not hl else "supervisor","pill",120+c*215,620+r*360,0.95)}</g>'
    body = f'''<div class="gl" style="left:60px;top:470px;width:960px;height:1180px"></div>
{svg(ppl, z=2)}
<div class="hz-abs" style="left:320px;top:950px;width:225px;height:350px;border-radius:40px;border:5px solid {A};box-shadow:0 0 0 2000px rgba(230,238,231,.0);z-index:3"></div>
<div class="hz-abs" style="left:90px;top:190px;font:700 30px Inter;letter-spacing:.2em;color:{PR}">REASON 02</div>
<div class="hz-abs" style="left:86px;top:240px;font:900 90px Inter;letter-spacing:-2.5px;line-height:1;color:{T}">Skilled manpower<br><span style="color:{PR}">bahut kam</span></div>
<div class="gl-chip" style="left:470px;top:1320px">skilled ✓</div>
<div class="hz-abs" style="left:90px;top:1720px;font:600 36px Inter;color:{T};opacity:.75">SME manufacturing ki asli problem</div>'''
    save("C2", page(body, G, C_CSS))


def C3():
    steps = [("01", "Business seekhna", "🧭"), ("02", "SOPs banana", "📋"), ("03", "Implement", "⚙️")]
    st = ''.join(f'''<div class="gl" style="left:{90 + i*40}px;top:{520 + i*330}px;width:{760}px;height:260px;padding:40px 46px;display:flex;align-items:center;gap:34px;{"box-shadow:0 0 0 5px "+A+",0 30px 60px rgba(19,32,27,.18)" if i==1 else ""}">
<div style="width:150px;height:150px;border-radius:{40 if i!=1 else 75}px;background:{A if i<=1 else "rgba(47,125,87,.2)"};display:flex;align-items:center;justify-content:center;font-size:70px;flex:none">{e}</div>
<div><div style="font:700 28px 'JetBrains Mono';color:{A}">{n}</div><div style="font:800 58px Inter;letter-spacing:-1.5px;color:{T}">{t}</div></div></div>''' for i, (n, t, e) in enumerate(steps))
    cursor = f'<svg class="hz-abs" style="left:880px;top:880px;z-index:9" width="140" height="170"><path d="M10 10 L10 140 L44 108 L70 160 L96 148 L70 98 L118 98 Z" fill="{T}" stroke="#fff" stroke-width="6" stroke-linejoin="round"/></svg>'
    body = f'''<div class="hz-abs" style="left:90px;top:200px;font:900 82px Inter;letter-spacing:-2.5px;line-height:1;color:{T}">Hum aapka business<br><span style="color:{A}">seekhte hain</span></div>
{st}{cursor}
<div class="hz-abs" style="left:90px;top:1600px;width:900px;font:600 38px Inter;line-height:1.3;color:{T};opacity:.8">Taaki aapko hamara software <b>na seekhna pade</b></div>'''
    save("C3", page(body, G, C_CSS))


def C4():
    ch, sh = chat_production("flow")
    body = f'''<div class="blob" style="left:200px;top:500px;width:700px;height:700px;background:#9FD3B5"></div>
<div style="position:absolute;inset:0;perspective:1600px;z-index:2"><div style="position:absolute;left:250px;top:330px;width:620px;height:1250px;transform:rotateY(-16deg) rotateX(4deg);transform-style:preserve-3d">
{phone(0,0,1.36,ch,sh)}</div></div>
<div class="hz-abs" style="left:300px;top:1590px;width:520px;height:50px;border-radius:50%;background:rgba(19,32,27,.18);filter:blur(16px)"></div>
<div class="gl-chip" style="left:40px;top:470px">🕘 Attendance · 1 click</div>
<div class="gl-chip" style="left:640px;top:760px">🚚 Inward entry</div>
<div class="gl-chip" style="left:40px;top:1240px;box-shadow:0 0 0 4px {A},0 14px 30px rgba(19,32,27,.12)">⚙️ Production · M-4</div>
<div class="hz-abs" style="left:90px;top:180px;font:900 76px Inter;letter-spacing:-2px;line-height:1;color:{T}">Sab kuch<br><span style="color:{A}">WhatsApp par</span></div>
{SAMPLE(90, 1800)}'''
    save("C4", page(body, G, C_CSS))


def C5():
    wall = ''
    for i in range(9):
        r, c = divmod(i, 3)
        wall += kpi(["Production","Inventory","Present","Inward","Dispatch","Absent","Job orders","Leave","Defaulters"][i], ["1,240","312","94","3","18","26","7","6","14"][i], "sample", [DB['deep'],DB['ink'],DB['green'],DB['amber'],DB['ink'],DB['amber'],DB['purple'],DB['purple'],DB['coral']][i], "•", "#F1F2F5",
                    f"position:absolute;left:{-60+c*400}px;top:{380+r*260}px;width:370px;transform:scale(.92);opacity:.55;filter:blur(2.5px)")
    body = f'''{wall}
<div class="hz-abs" style="left:0;top:0;width:1080px;height:1920px;background:linear-gradient(180deg,rgba(230,238,231,.0) 30%,rgba(230,238,231,.75) 60%)"></div>
{kpi("Today Production","1,240","pcs · all machines",DB['deep'],"⚙️",DB['mint'],"position:absolute;left:110px;top:600px;width:860px;transform:rotate(-1.5deg);box-shadow:0 30px 60px rgba(19,32,27,.18)")}
{alerts(ALERT_ROWS,0,extra="position:absolute;left:80px;top:900px;width:920px;box-shadow:0 30px 60px rgba(19,32,27,.2)")}
<div class="hz-abs" style="left:90px;top:170px;font:900 80px Inter;letter-spacing:-2.5px;line-height:1;color:{T}">Ek single<br><span style="color:{A}">dashboard</span></div>
{SAMPLE(90, 1800)}'''
    save("C5", page(body, G, C_CSS))


def C6():
    body = f'''{face_placeholder(0, 0, 1080, 1920, "HEYGEN FACE · placeholder (full frame)", radius=0, bg="#C7D6CA")}
<div class="gl" style="left:70px;top:1150px;width:940px;height:600px;padding:46px 50px;z-index:3;background:rgba(248,251,248,.7)">
<div style="font:700 28px Inter;letter-spacing:.18em;color:{A}">CUSTOM · WHATSAPP ERP</div>
<div style="font:900 70px Inter;letter-spacing:-2px;line-height:1.02;color:{T};margin:14px 0 10px">Apni factory mein<br>lagwana hai?</div>
<div style="font:700 32px Inter;color:{T};opacity:.75;margin-bottom:28px">₹15,000/mahine se shuru</div>
<span style="background:{P['cta']};color:{P['navy']};font:800 36px Inter;padding:22px 34px;border-radius:999px;border:3px solid {P['navy']}">DM karo · WhatsApp ↓</span></div>
{WORDMARK(800, 120)}'''
    save("C6", page(body, G, C_CSS))


if __name__ == "__main__":
    for f in [A1, A2, A3, A4, A5, A6, B1, B2, B3, B4, B5, B6, C1, C2, C3, C4, C5, C6]:
        f()
    print("ok")
