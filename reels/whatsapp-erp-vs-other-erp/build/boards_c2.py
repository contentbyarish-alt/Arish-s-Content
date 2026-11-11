"""Storyboard C (Keynote Chapters) re-laid for the Reels-ad safe zone: x 65-1015, y 270-1250.
Captions band y 1160-1240. SAMPLE data."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from boards import *

SX0, SX1, SY0, SY1 = 65, 1015, 270, 1250
CS = C_CSS + f"""
.rail{{left:90px;right:90px;top:290px}}
.c-h{{left:90px;right:90px}}
.cap{{position:absolute;left:0;right:0;top:1168px;text-align:center;z-index:30}}
.cap span{{display:inline-block;background:{T};color:#fff;font:800 44px Inter;letter-spacing:-.5px;padding:12px 30px;border-radius:20px}}
.amb{{position:absolute;left:0;width:1080px;font:800 230px Inter;letter-spacing:-10px;color:{T};opacity:.045;white-space:nowrap}}
"""


def cap(t):
    return f'<div class="cap"><span>{t}</span></div>'


def amb():  # decorative only, lives outside the safe zone (safe to be covered by ad UI)
    deco = f'<div class="hz-abs" style="left:-60px;top:1300px;width:1200px;height:700px;overflow:hidden;opacity:.22;filter:blur(3px);transform:rotate(-4deg)"><img src="file://{DASH}" style="width:1200px"></div>'
    deco += f'<div class="hz-abs" style="left:0;top:1260px;width:1080px;height:200px;background:linear-gradient(#EEF2EC,rgba(238,242,236,0))"></div>'
    deco += f'<div class="hz-abs" style="left:0;top:0;width:1080px;height:250px;background:linear-gradient(90deg,#E3ECE5,#F3EFE7)"></div>'
    return deco


def save_c(n, body):
    save(n, amb() + body, C_BG, CS)


def C1():
    body = f'''<div class="c-h" style="top:300px;font-size:104px;letter-spacing:-5px;color:{PR}">Other ERP</div>
<div class="hz-abs" style="left:90px;top:360px;width:560px;height:9px;background:{T};transform:rotate(-4deg);z-index:9"></div>
<div class="c-h" style="top:410px;font-size:104px;letter-spacing:-5px;text-align:right">WhatsApp <span style="color:{A}">ERP</span></div>
{svg(monitor_old(85, 640, .78), z=2)}
<div class="hz-abs" style="left:85px;top:1010px;font:600 28px Inter;color:{PR};z-index:9">40+ modules · training</div>
{ph(560, 548, .62, INWARD[3][1], "")}{dcrop("inv", .9, 600, 920, ring="inv", radius=18, z=7)}
<div class="hz-abs" style="left:420px;top:740px;width:150px;height:150px;border-radius:50%;background:{T};display:flex;align-items:center;justify-content:center;font:italic 700 70px 'DejaVu Serif';color:#fff;z-index:9">vs</div>
<div class="hz-abs" style="left:90px;top:1085px;font:700 28px Inter;letter-spacing:.18em;color:{T}">FOR MANUFACTURING</div>{cap("WhatsApp ERP vs other ERP")}'''
    save_c("C1", body)


def C2():
    face_ = face(90, 290, 900, 640, 60, 40, vy=-0.24)
    nums = ''.join(f'<div class="hz-abs" style="left:{90+i*310}px;top:960px;width:280px;height:170px;border-radius:32px;background:#fff;box-shadow:0 12px 30px rgba(19,32,27,.1);display:flex;align-items:center;justify-content:center;font:900 100px Inter;letter-spacing:-4px;color:{PR}">0{i+1}</div>' for i in range(3))
    save_c("C2", face_ + nums + cap("Iske teen bade reason hain"))


def C3():
    cards = ''.join(f'''<div class="hz-abs" style="left:90px;top:{560+i*196}px;width:900px;height:176px;border-radius:34px;background:#fff;box-shadow:{"0 26px 50px rgba(19,32,27,.16)" if i==1 else "0 8px 20px rgba(19,32,27,.06)"};transform:scale({1.03 if i==1 else .97});opacity:{1 if i==1 else .5};display:flex;align-items:center;gap:34px;padding:0 44px">
<div style="font:800 86px Inter;letter-spacing:-4px;color:{PR}">0{i+1}</div><div><div style="font:800 46px Inter;letter-spacing:-1.2px;color:{T}">{t}</div><div style="font:500 27px Inter;color:#6B7A71;margin-top:4px">{s}</div></div></div>''' for i, (t, s) in enumerate([("Koi system nahi", "Registers, Excel, calls"), ("Skilled manpower kam", "Software chalayega kaun?"), ("Implementation lamba", "Mahine nikal jaate hain")]))
    save_c("C3", f'{rail(0)}<div class="c-h" style="top:370px;font-size:70px">ERP fail <span style="color:{PR}">kyun hota hai?</span></div>{cards}{cap("skilled manpower bahut kam")}')


def C4():
    body = f'''<div class="c-h" style="top:300px;font-size:44px;color:{A}">Hivon Automation</div><div class="c-h" style="top:350px;font-size:96px;letter-spacing:-4px">WhatsApp ERP</div>
{laptop(370, 540, 600, ring="alerts")}{ph(86, 470, .66, INWARD[1][1], INWARD[1][2])}
{svg(sync_line(385, 820, 450, 760, "#2F7D57"), z=8)}
<div class="hz-abs" style="left:410px;top:940px;font:700 30px Inter;color:{T};z-index:9">Input <span style="color:{A}">WhatsApp</span> → Output <span style="color:{A}">Dashboard</span></div>
<div class="hz-abs" style="left:410px;top:1000px;display:flex;gap:12px;z-index:9">{"".join(f'<span style="background:#fff;border-radius:999px;padding:10px 22px;font:700 26px Inter;color:{T};box-shadow:0 6px 16px rgba(19,32,27,.08)"><b style="color:{A}">✓</b> {t}</span>' for t in ["System", "Manpower", "Time"])}</div>
{cap("Hivon Automation with its WhatsApp ERP")}'''
    save_c("C4", body)


def chapter(n, i, l1, l2, msgs, sheet, k1, k2, capt, cursor=None):
    cur = f'<svg class="hz-abs" style="left:{cursor[0]}px;top:{cursor[1]}px;z-index:20" width="80" height="100"><path d="M8 8 L8 84 L28 66 L42 94 L56 87 L42 58 L70 58 Z" fill="#13201B" stroke="#fff" stroke-width="5" stroke-linejoin="round"/></svg>' if cursor else ""
    body = f'''{rail(i)}<div class="c-h" style="top:362px;font-size:58px;letter-spacing:-2px">{l1}<br><span style="color:{A}">{l2}</span></div>
{ph(70, 478, .72, msgs, sheet)}{cur}
{dcrop(k1, 1.28, 440, 500, ring=k1, radius=22)}{dcrop(R["alerts"], 1.18, 440, 720, ring=k2, radius=22)}
{svg(sync_line(410, 760, 440, 600, "#2F7D57") + sync_line(410, 980, 440, 900, "#2F7D57"), z=8)}
<div class="hz-abs" style="left:440px;top:1120px;font:600 20px Inter;letter-spacing:.1em;color:rgba(19,32,27,.5)">SAMPLE DATA</div>{cap(capt)}'''
    save_c(n, body)


def C5():
    chapter("C5", 1, "Labour ki attendance,", "ek click + location", ATTENDANCE[3][1], "", "present", "a3", "ek click mein attendance", (300, 1040))


def C6():
    chapter("C6", 3, "Supervisor: machine se", "ek input, production live", PRODUCTION[1][1], PRODUCTION[1][2], "prod", "a4", "aaj maine itni production ki")


def C7():
    body = f'''{rail(4)}<div class="c-h" style="top:362px;font-size:62px;letter-spacing:-2px">Poori factory,<br><span style="color:{A}">ek dashboard</span></div>
{dcrop("prod", 1.08, 90, 520, ring="prod", radius=24)}{dcrop("present", 1.08, 90, 700, radius=24)}{dcrop("inv", 1.08, 90, 880, radius=24)}
{dcrop(R["alerts"], 1.0, 540, 520, ring="a4", radius=24)}{dcrop((320, 548, 760, 330), .62, 540, 880, radius=24)}
{cap("woh bhi WhatsApp ke through")}'''
    save_c("C7", body)


def C8():
    body = f'''{face(90, 290, 900, 560, 230, 40, vy=-0.27)}
<div class="hz-abs" style="left:90px;top:870px;width:900px;padding:30px 40px;border-radius:34px;background:rgba(255,255,255,.8);backdrop-filter:blur(24px);border:2px solid #fff;box-shadow:0 24px 50px rgba(19,32,27,.12);z-index:5;display:flex;gap:30px;align-items:center">
{ph(0, 0, 0, "", "").replace('class="hz-phone"', 'class="hz-phone" style="display:none"')}
<div style="flex:1"><div style="font:800 48px Inter;letter-spacing:-1.5px;line-height:1.05;color:{T}">Apni factory ka<br><span style="color:{A}">custom WhatsApp ERP</span></div>
<div style="font:600 28px Inter;color:#55665C;margin:12px 0 18px">₹15,000/mahine se shuru</div>
<span style="background:{CTA};color:{NAVY};border-radius:999px;padding:16px 32px;font:800 34px Inter">WhatsApp pe DM karo ↓</span></div></div>
{WM(860, 300, "#fff", 40)}{cap("WhatsApp number par DM kar do")}'''
    save_c("C8", body)


SAFE_OVERLAY = f'''<div class="hz-abs" style="left:0;top:0;width:1080px;height:{SY0}px;background:rgba(221,82,76,.22);z-index:99"></div>
<div class="hz-abs" style="left:0;top:{SY1}px;width:1080px;height:{1920-SY1}px;background:rgba(221,82,76,.22);z-index:99"></div>
<div class="hz-abs" style="left:0;top:{SY0}px;width:{SX0}px;height:{SY1-SY0}px;background:rgba(221,82,76,.22);z-index:99"></div>
<div class="hz-abs" style="left:{SX1}px;top:{SY0}px;width:{1080-SX1}px;height:{SY1-SY0}px;background:rgba(221,82,76,.22);z-index:99"></div>
<div class="hz-abs" style="left:{SX0}px;top:{SY0}px;width:{SX1-SX0}px;height:{SY1-SY0}px;border:4px dashed #DD524C;z-index:99"></div>
<div class="hz-abs" style="left:0;right:0;top:{SY1+40}px;text-align:center;font:800 40px Inter;color:#B5483F;z-index:99">AD UI ZONE (caption · CTA button)</div>
<div class="hz-abs" style="left:0;right:0;top:110px;text-align:center;font:800 40px Inter;color:#B5483F;z-index:99">AD UI ZONE (profile · Sponsored)</div>'''

if __name__ == "__main__":
    for f in [C1, C2, C3, C4, C5, C6, C7, C8]:
        f()
    for i in range(1, 9):
        s = open(f"{OUT}/C{i}.html").read()
        open(f"{OUT}/C{i}_safe.html", "w").write(s.replace("</body>", SAFE_OVERLAY + "</body>"))
    print("ok")
