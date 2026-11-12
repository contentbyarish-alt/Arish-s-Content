import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import scenes4 as s4
from scenes4 import *
from firstframe import logo_card, L
s4.START['ff'] = 0.0; s4.DUR['ff'] = 2.48

logos = ''.join(logo_card(n, 600 + (i % 2) * 200, 580 + (i // 2) * 134, .7 + i * .08) for i, n in enumerate(["odoo", "sap", "tally", "zoho"]))
body = f'''<div class="c-h" {an(-.5, "l", .3)} style="top:300px;font-size:104px;letter-spacing:-5px">WhatsApp <span style="color:{A}">ERP</span></div>
<div class="c-h" {an(.55, "r", .3)} style="top:410px;font-size:104px;letter-spacing:-5px;text-align:right;color:{PR}">Other ERP</div>
<div class="hz-abs" id="strike" style="left:520px;top:470px;width:500px;height:9px;background:{T};transform:rotate(-4deg) scaleX(0);transform-origin:0 50%;z-index:9"></div>
<div {an(-.5, "l", .36)} class="hz-abs" style="left:0;top:0;width:1080px;height:1920px;z-index:3">{laptop(90, 590, 420)}</div>
{phone_anim(at(-.5, tm("✅ Production Logged", "⚙️ Machine <b>M-4</b> · Flange 40mm<br>✔️ OK: <b>120 pcs</b> · ✖️ Reject: <b>3</b><br>🎯 Target 150 · <b>80%</b>", "5:57 PM", doc="DPR-M4.pdf")), x=300, y=700, s=.5, t=-.5)}
<svg class="hz-abs" {an(-.5, "fade", .3)} style="left:0;top:0;z-index:8" width="1080" height="1920">{sync_line(300, 930, 230, 860, "#2F7D57")}</svg>
{logos}
<div class="hz-abs" {an(1.0, "fade", .3)} style="left:600px;top:870px;width:400px;display:flex;flex-wrap:wrap;gap:10px;z-index:6">
<span style="background:#F6E4E1;color:{PR};border-radius:999px;padding:8px 18px;font:700 24px Inter">40+ modules</span><span style="background:#F6E4E1;color:{PR};border-radius:999px;padding:8px 18px;font:700 24px Inter">Training · consultants</span></div>
<div class="hz-abs" {an(.95, "pop", .3)} style="left:500px;top:1000px;width:120px;height:120px;border-radius:50%;background:{T};display:flex;align-items:center;justify-content:center;font:italic 700 58px 'DejaVu Serif';color:#fff;z-index:9">vs</div>
<div class="hz-abs" {an(1.4, "fade", .3)} style="left:640px;top:1046px;font:700 24px Inter;letter-spacing:.16em;color:{T}">FOR MANUFACTURING</div>'''
scene("ff", body, "const p=E.out(E.cl((t-1.0)/0.25));document.getElementById('strike').style.transform=`rotate(-4deg) scaleX(${p})`;")
print("ok")
