"""Thumbnail + GBP carousel for Storyboard A (Comic Panel Pop). SAMPLE data only."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from comp import *
from frames2 import D_CSS, dots, burst, speed, zig, halves, svg, PINK, MINT, AMB, G, T, A, PR, C, CTA, NAVY

OUT = os.path.join(os.path.dirname(__file__), "extras")
os.makedirs(OUT, exist_ok=True)
BG = G + ";" + dots('19,32,27', .07, 22)


def save(n, html):
    open(f"{OUT}/{n}.html", "w").write(html)


def mini_phone(x, y, s=1, rot=5):
    return f'''<g transform="translate({x},{y}) rotate({rot}) scale({s})"><rect width="300" height="560" rx="46" fill="{T}"/><rect x="16" y="16" width="268" height="528" rx="32" fill="#EAE6DF"/>
<rect x="16" y="16" width="268" height="62" fill="#F6F6F6"/><circle cx="52" cy="48" r="17" fill="#0D0D0D"/><rect x="80" y="40" width="120" height="14" rx="7" fill="#101729"/>
<rect x="32" y="100" width="206" height="78" rx="12" fill="#fff"/><text x="46" y="130" font-family="Inter" font-weight="800" font-size="17" fill="#101729">🏭 Production Update</text><rect x="46" y="146" width="130" height="10" rx="5" fill="#9aa0a6"/>
<rect x="32" y="181" width="206" height="40" fill="#EAF4FF"/><text x="135" y="208" text-anchor="middle" font-family="Inter" font-weight="700" font-size="18" fill="#1D8FF5">📝 Entry karein</text>
<rect x="110" y="246" width="160" height="50" rx="12" fill="#E2FBCB"/><text x="126" y="278" font-family="Inter" font-weight="600" font-size="18" fill="#101729">M-4 · 120 pcs</text>
<rect x="32" y="320" width="220" height="92" rx="12" fill="#fff"/><text x="46" y="354" font-family="Inter" font-weight="800" font-size="19" fill="{A}">✅ Logged!</text><rect x="46" y="372" width="150" height="10" rx="5" fill="#9aa0a6"/></g>'''


def monitor(x, y, s=1):
    cells = ''.join(f'<rect x="{26+c*62}" y="{78+r*36}" width="52" height="24" fill="{PR}" opacity="{.25+((r*3+c)%4)*.14}"/>' for r in range(6) for c in range(5))
    return f'''<g transform="translate({x},{y}) scale({s})"><g stroke="{T}" stroke-width="7" stroke-linejoin="round"><rect width="370" height="330" rx="12" fill="#fff"/><rect width="370" height="50" fill="{PR}"/><path d="M140 330 L230 330 L256 400 L114 400 Z" fill="#CDD8CF"/></g>{cells}
<g stroke="{T}" stroke-width="6"><rect x="80" y="150" width="250" height="120" fill="#fff" transform="rotate(-5 205 210)"/></g>
<text x="206" y="228" text-anchor="middle" transform="rotate(-5 205 210)" font-family="Inter" font-weight="900" font-size="46" fill="{PR}">ERROR!</text></g>'''


# ---------------- thumbnail ----------------
def thumb():
    pts = zig(11, amp=58, step=150); L, R = halves(pts, 13)
    left = monitor(70, 880, .95) + person("owner", "comic", 200, 1180, 1.05, pose="head")
    right = mini_phone(700, 850, .82) + person("supervisor", "comic", 690, 1180, 1.05, pose="wave")
    body = f'''<div class="hz-abs" style="inset:0;background:{T}"></div>
<div class="hz-abs" style="inset:0;clip-path:polygon({L});background-color:{PINK};{dots('181,72,63',.2)}">{svg(left)}</div>
<div class="hz-abs" style="inset:0;clip-path:polygon({R});background-color:{MINT};{dots('47,125,87',.2)}">{svg(speed(830, 1100, 22, 330, 1500, 'rgba(47,125,87,.12)') + right)}</div>
<div class="hz-abs" style="left:100px;top:372px;font:900 62px Inter;letter-spacing:-2px;color:{T};background:#fff;border:6px solid {T};padding:2px 22px;box-shadow:7px 7px 0 {T};z-index:9">hivon<span style="color:{CTA}">.</span></div>
<div class="hz-abs" style="left:90px;top:490px;width:900px;z-index:8;transform:rotate(-2deg)">
<div style="display:inline-block;background:{AMB};border:8px solid {T};box-shadow:12px 12px 0 {T};padding:6px 30px;font:italic 900 168px Inter;letter-spacing:-7px;line-height:1;color:{T}">ERP FAIL</div><br>
<div style="display:inline-block;margin-top:6px;margin-left:150px;background:{T};border:8px solid {T};box-shadow:12px 12px 0 {PR};padding:0 30px;font:italic 900 168px Inter;letter-spacing:-7px;line-height:1.02;color:#fff">KYUN?</div></div>
{svg(burst(540, 1130, 170, 108, 14, "#fff", T, 9, .1), z=6)}
<div class="hz-abs" style="left:420px;top:1060px;width:240px;text-align:center;font:italic 900 124px Inter;color:{PR};-webkit-text-stroke:7px {T};paint-order:stroke fill;z-index:7;letter-spacing:-5px;transform:rotate(-6deg)">VS</div>
<div class="cap" style="left:100px;top:1440px;background:#fff;color:{PR};font-size:44px;transform:rotate(-2deg)">OTHER ERP</div>
<div class="cap" style="left:590px;top:1440px;background:#fff;color:{A};font-size:44px;transform:rotate(2deg);white-space:nowrap">WHATSAPP ERP</div>'''
    save("thumb", page(body, G, D_CSS))


# ---------------- carousel (1080x1350) ----------------
CAR = D_CSS + f"""html,body{{height:1350px!important}}
.ch{{position:absolute;left:80px;right:80px;font:900 92px Inter;letter-spacing:-3.5px;line-height:1;color:{T}}}
.ck{{position:absolute;left:80px;font:700 30px Inter;color:{T};opacity:.7}}
.cpn{{position:absolute;border:8px solid {T};box-shadow:12px 12px 0 {T};overflow:hidden}}"""
N = 9


def slide(n, inner, bg=BG):
    foot = f'''<div class="hz-abs" style="left:80px;top:1262px;font:900 44px Inter;letter-spacing:-1px;color:{T};z-index:9">hivon<span style="color:{CTA}">.</span></div>
<div class="hz-abs" style="right:80px;top:1268px;font:800 30px 'JetBrains Mono';color:{T};z-index:9">{n:02d} / {N:02d}</div>
<div class="hz-abs" style="left:250px;right:230px;top:1286px;height:8px;background:rgba(19,32,27,.15);z-index:9"><div style="width:{n/N*100:.0f}%;height:100%;background:{A}"></div></div>'''
    save(f"c{n}", page(inner + foot, bg, CAR))


def reason(n, num, title, hl, art, cap, sn):
    slide(n, f'''<div class="cap" style="left:60px;top:70px;transform:rotate(-2deg);font-size:44px">REASON {num}</div>
<div class="ch" style="top:170px">{title}<br><span style="background:{T};color:#fff;padding:0 16px">{hl}</span></div>
<div class="cpn" style="left:60px;top:430px;width:960px;height:640px;background-color:{PINK};{dots('181,72,63',.18)}">{svg(speed(480, 330, 28, 300, 1400, 'rgba(181,72,63,.12)') + art, w=960, h=640)}</div>
<div class="cap" style="left:90px;top:1090px;background:#fff;font-size:38px;transform:rotate(1deg);white-space:nowrap">{cap}</div>{sn}''')


def carousel():
    # 1 hook
    slide(1, f'''<div class="cap" style="left:60px;top:80px;transform:rotate(-2deg);font-size:40px;background:#fff">WHATSAPP ERP <span style="color:{PR}">vs</span> OTHER ERP</div>
<div class="ch" style="top:200px;font-size:128px;letter-spacing:-5px">Factory mein ERP <span style="background:{PR};color:#fff;padding:0 16px">fail</span> kyun hota hai?</div>
{svg(burst(800, 960, 190, 125, 14, AMB, T, 9, .1) + person("owner", "comic", 110, 760, 1.4, pose="head"), h=1350)}
<div class="hz-abs" style="left:690px;top:890px;width:220px;text-align:center;font:italic 900 64px Inter;line-height:.95;color:{T};transform:rotate(-8deg);z-index:5">3 bade<br>reason</div>
<div class="hz-abs" style="left:430px;top:1150px;font:800 34px Inter;color:{T}">swipe →</div>''')
    # 2-4 reasons
    papers = ''.join(f'<g transform="translate({x},{y}) rotate({r})" stroke="{T}" stroke-width="6"><rect width="120" height="150" fill="#fff"/>{"".join(f"<line x1=\"18\" y1=\"{30+k*24}\" x2=\"{96-(k%2)*30}\" y2=\"{30+k*24}\" stroke-width=\"4\" opacity=\".45\"/>" for k in range(5))}</g>' for x, y, r in [(70, 90, -18), (760, 70, 14), (110, 400, 12), (770, 380, -12)])
    reason(2, 1, "Koi system", "hi nahi", papers + person("owner", "comic", 350, 130, 1.45, pose="head"), f'Software laga bhi doge… <span style="color:{PR}">phir bhi fail</span>', "")
    crew = ''.join(f'<g opacity="{1 if i==2 else .3}">{person("supervisor" if i==2 else "worker", "comic", 30+i*180, 190, .95)}</g>' for i in range(5))
    reason(3, 2, "Skilled manpower", "bahut kam", crew + burst(480, 110, 96, 66, 12, AMB, T, 6) + f'<text x="480" y="124" text-anchor="middle" font-family="Inter" font-weight="900" font-size="28" fill="{T}">skilled</text>', "SME manufacturing ki asli dikkat", "")
    cal = ''.join(f'<g transform="translate({60+i*150},{150+ (i%2)*50}) rotate({-8+i*4})" stroke="{T}" stroke-width="6"><rect width="130" height="150" fill="#fff"/><rect width="130" height="38" fill="{PR}"/><text x="65" y="112" text-anchor="middle" font-family="Inter" font-weight="900" font-size="48" fill="{T}" stroke="none">M{i+1}</text></g>' for i in range(6))
    reason(4, 3, "Implementation", "lamba kheechta hai", cal + person("worker", "comic", 380, 300, 1.0, pose="shrug"), "Mahine nikalte jaate hain", "")
    # 5 hivon way
    steps = [("1", "Pehle aapka business seekhte hain"), ("2", "Phir aapke SOPs banaate hain"), ("3", "SOPs jo small-medium factory mein implement ho sakein")]
    st = ''.join(f'''<div class="hz-abs" style="left:{80+i*24}px;top:{420+i*200}px;width:860px;background:#fff;border:7px solid {T};box-shadow:10px 10px 0 {T};padding:24px 30px;display:flex;gap:26px;align-items:center;transform:rotate({[-1,1,-.6][i]}deg)">
<div style="width:92px;height:92px;flex:none;background:{A};border:6px solid {T};display:flex;align-items:center;justify-content:center;font:900 60px Inter;color:#fff">{n}</div><div style="font:800 44px Inter;letter-spacing:-1px;line-height:1.1;color:{T}">{t}</div></div>''' for i, (n, t) in enumerate(steps))
    slide(5, f'''<div class="cap" style="left:60px;top:70px;transform:rotate(-2deg);font-size:40px;background:#fff">HIVON KA TAREEKA</div>
<div class="ch" style="top:170px;font-size:84px">Software se pehle,<br><span style="color:{A}">aapka business</span></div>{st}
<div class="ck" style="top:1100px;font-size:36px;opacity:1;font-weight:800">Taaki aapko hamara software na seekhna pade</div>''')
    # 6 whatsapp
    ch, sh = chat_production("flow")
    chips = ''.join(f'<div class="cap" style="left:60px;top:{560+i*150}px;background:#fff;font-size:38px;transform:rotate({[-2,1.5,-1][i]}deg)">{t}</div>' for i, t in enumerate(["🕘 Attendance · ek click", "🚚 Maal inward · input", "⚙️ Production update"]))
    slide(6, f'''<div class="cap" style="left:60px;top:70px;transform:rotate(-2deg);font-size:40px">STAFF KO KUCH SEEKHNA NAHI</div>
<div class="ch" style="top:170px;font-size:92px">Sab kuch<br><span style="color:{A}">WhatsApp par</span></div>
{chips}{phone(590, 400, .92, ch, sh, rot=3, extra=f"box-shadow:12px 12px 0 {T};z-index:6")}
<div class="hz-sample" style="left:80px;top:1130px">SAMPLE DATA</div>''')
    # 7 dashboard
    k = (kpi("Today Production", "1,240", "pcs · Shift A", DB['deep'], "⚙️", DB['mint'], "position:absolute;left:30px;top:30px;width:280px;padding:18px 20px;border:5px solid " + T) +
         kpi("Inventory", "312", "SKUs", DB['ink'], "📦", "#F1F2F5", "position:absolute;left:330px;top:30px;width:280px;padding:18px 20px;border:5px solid " + T) +
         kpi("Present", "94", "log aaj", DB['green'], "🗓️", DB['mint'], "position:absolute;left:630px;top:30px;width:280px;padding:18px 20px;border:5px solid " + T))
    slide(7, f'''<div class="cap" style="left:60px;top:70px;transform:rotate(-2deg);font-size:40px">LIVE STATUS</div>
<div class="ch" style="top:170px;font-size:92px">Poori factory,<br><span style="color:{A}">ek dashboard</span></div>
<div class="cpn" style="left:60px;top:420px;width:960px;height:660px;background:{DB['canvas']}">{k}{alerts(ALERT_ROWS[:3], 0, extra="position:absolute;left:30px;top:240px;width:880px;border:5px solid " + T)}</div>
<div class="ck" style="top:1110px;font-size:34px">Production · inventory · kitne log · woh bhi WhatsApp se</div>
<div class="hz-sample" style="left:80px;top:1170px">SAMPLE DATA</div>''')
    # 8 save-worthy
    rows = [("Koi system hi nahi", "Pehle business seekhte hain, phir SOPs"), ("Skilled manpower kam", "Staff ke liye sirf WhatsApp"), ("Implementation lamba", "SOPs jo SME mein implement ho sakein")]
    rw = ''.join(f'''<div style="display:flex;border-top:6px solid {T}"><div style="flex:1;padding:44px 26px;background:{PINK};font:800 44px Inter;letter-spacing:-.5px;line-height:1.12;color:{PR};border-right:6px solid {T}">✗ {a}</div><div style="flex:1.25;padding:44px 26px;background:{MINT};font:800 44px Inter;letter-spacing:-.5px;line-height:1.12;color:{T}"><span style="color:{A}">✓</span> {b}</div></div>''' for a, b in rows)
    slide(8, f'''<div class="cap" style="left:60px;top:70px;transform:rotate(-2deg);font-size:40px">SAVE KAR LO</div>
<div class="ch" style="top:170px;font-size:84px">3 reason,<br><span style="color:{A}">3 jawab</span></div>
<div class="cpn" style="left:60px;top:410px;width:960px;background:#fff">
<div style="display:flex"><div style="flex:1;padding:18px 24px;font:900 34px Inter;color:#fff;background:{PR};border-right:6px solid {T}">ERP fail kyun</div><div style="flex:1.25;padding:18px 24px;font:900 34px Inter;color:#fff;background:{A}">Hivon WhatsApp ERP</div></div>{rw}</div>''')
    # 9 CTA
    slide(9, f'''<div class="cap" style="left:60px;top:80px;transform:rotate(-2deg);font-size:40px;background:#fff">CUSTOM SOFTWARE</div>
<div class="ch" style="top:190px;font-size:112px;letter-spacing:-4px">Apni factory ka <span style="color:{A}">WhatsApp ERP?</span></div>
<div class="hz-abs" style="left:80px;top:540px;font:800 54px Inter;letter-spacing:-1px;color:{T}">₹15,000/mahine se shuru</div>
<div class="hz-abs" style="left:80px;top:670px;background:{CTA};border:7px solid {NAVY};box-shadow:10px 10px 0 {T};padding:26px 44px;font:900 58px Inter;color:{NAVY};transform:rotate(-2deg);z-index:9">WhatsApp pe DM karo</div>
<div class="hz-abs" style="left:80px;top:870px;font:700 40px Inter;color:{T}">ya dekho: <b>hivon.in</b></div>
{svg(person("supervisor", "comic", 740, 800, 1.25, pose="wave"), h=1350)}''')


# ---------------- GBP 4:3 (1200x900) ----------------
def gbp():
    rows = [("Koi system hi nahi", "Pehle business seekhte hain, phir SOPs"), ("Skilled manpower kam", "Staff ke liye sirf WhatsApp"), ("Implementation lamba", "SOPs jo SME mein implement ho sakein")]
    rw = ''.join(f'''<div style="display:flex;border-top:5px solid {T}"><div style="flex:1;padding:16px 20px;background:{PINK};font:800 32px Inter;line-height:1.12;color:{PR};border-right:5px solid {T}">✗ {a}</div><div style="flex:1.3;padding:16px 20px;background:{MINT};font:800 32px Inter;line-height:1.12;color:{T}"><span style="color:{A}">✓</span> {b}</div></div>''' for a, b in rows)
    body = f'''<div class="hz-abs" style="left:70px;top:150px;font:900 48px Inter;letter-spacing:-1.5px;color:{T}">hivon<span style="color:{CTA}">.</span></div>
<div class="hz-abs" style="left:250px;top:156px;font:700 30px Inter;color:{T};opacity:.7">WhatsApp ERP for Manufacturing</div>
<div class="hz-abs" style="left:70px;top:226px;width:1060px;font:900 76px Inter;letter-spacing:-3px;line-height:1;color:{T}">Factory mein ERP <span style="background:{PR};color:#fff;padding:0 12px">fail</span> kyun hota hai?</div>
<div class="hz-abs" style="left:70px;top:420px;width:1060px;border:7px solid {T};box-shadow:10px 10px 0 {T};background:#fff">
<div style="display:flex"><div style="flex:1;padding:12px 20px;font:900 32px Inter;color:#fff;background:{PR};border-right:5px solid {T}">3 reason</div><div style="flex:1.3;padding:12px 20px;font:900 32px Inter;color:#fff;background:{A}">Hivon WhatsApp ERP</div></div>{rw}</div>'''
    save("gbp", page(body, BG, D_CSS + "html,body{width:1200px!important;height:900px!important}"))


if __name__ == "__main__":
    thumb(); carousel(); gbp(); print("ok")
