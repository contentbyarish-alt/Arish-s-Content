import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import scenes4 as s4
from scenes4 import *
s4.START['ff'] = 0.0; s4.DUR['ff'] = 2.48
L = ROOT + "/assets2/logos"

def logo_card(name, x, y, t, w=186, h=118, pad=18):
    return (f'<div class="hz-abs" {an(t, "pop", .3)} style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;border-radius:20px;background:#fff;'
            f'box-shadow:0 10px 24px rgba(19,32,27,.10);display:flex;align-items:center;justify-content:center;z-index:5">'
            f'<img src="file://{L}/{name}.png" style="max-width:{w-2*pad}px;max-height:{h-2*pad}px"></div>')

logos = ''.join(logo_card(n, 90 + (i % 2) * 200, 580 + (i // 2) * 134, -.5 + i * .02) for i, n in enumerate(["odoo", "sap", "tally", "zoho"]))
body = f'''<div class="c-h" {an(-.5, "l", .3)} style="top:300px;font-size:104px;letter-spacing:-5px;color:{PR}">Other ERP</div>
<div class="hz-abs" id="strike" style="left:90px;top:360px;width:560px;height:9px;background:{T};transform:rotate(-4deg) scaleX(0);transform-origin:0 50%;z-index:9"></div>
<div class="c-h" {an(.62, "r", .3)} style="top:410px;font-size:104px;letter-spacing:-5px;text-align:right">WhatsApp <span style="color:{A}">ERP</span></div>
{logos}
<div class="hz-abs" {an(-.5, "fade", .3)} style="left:90px;top:870px;width:390px;display:flex;flex-wrap:wrap;gap:10px;z-index:6">
<span style="background:#F6E4E1;color:{PR};border-radius:999px;padding:8px 18px;font:700 24px Inter">40+ modules</span><span style="background:#F6E4E1;color:{PR};border-radius:999px;padding:8px 18px;font:700 24px Inter">Training · consultants</span></div>
<div {an(.85, "r", .36)} class="hz-abs" style="left:0;top:0;width:1080px;height:1920px;z-index:3">{laptop(570, 590, 420)}</div>
{phone_anim(at(0, tm("✅ Production Logged", "⚙️ Machine <b>M-4</b> · Flange 40mm<br>✔️ OK: <b>120 pcs</b> · ✖️ Reject: <b>3</b><br>🎯 Target 150 · <b>80%</b>", "5:57 PM", doc="DPR-M4.pdf")), x=770, y=700, s=.5, t=.75)}
<svg class="hz-abs" {an(1.25, "fade", .3)} style="left:0;top:0;z-index:8" width="1080" height="1920">{sync_line(770, 930, 700, 860, "#2F7D57")}</svg>
<div class="hz-abs" {an(.95, "pop", .3)} style="left:420px;top:900px;width:130px;height:130px;border-radius:50%;background:{T};display:flex;align-items:center;justify-content:center;font:italic 700 62px 'DejaVu Serif';color:#fff;z-index:9">vs</div>
<div class="hz-abs" {an(1.4, "fade", .3)} style="left:90px;top:1085px;font:700 28px Inter;letter-spacing:.18em;color:{T}">FOR MANUFACTURING</div>'''
scene("ff", body, "const p=E.out(E.cl((t-0.38)/0.25));document.getElementById('strike').style.transform=`rotate(-4deg) scaleX(${p})`;")
print("ok")
