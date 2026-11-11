import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from flows import *
from comp import P
OUT = os.path.join(ROOT, "boards"); os.makedirs(OUT, exist_ok=True)
T, A = P['text'], P['accent']
rows = [("1 · Labour attendance (34.4–37.1 s)", ATTENDANCE, ("present", "a3"), "Today Total Present 94 + check-in alert"),
        ("2 · Store: maal inward (37.1–39.9 s)", INWARD, ("inv", "a2"), "Inventory + GRN-101 alert"),
        ("3 · Supervisor: production (39.9–44.2 s)", PRODUCTION, ("prod", "a4"), "Today Production 1,240 + M-4 alert")]
body = f'<div class="hz-abs" style="left:60px;top:40px;font:800 56px Inter;color:{T};letter-spacing:-1.5px">Complete WhatsApp flows + dashboard result (sample data)</div>'
for r, (title, steps, (k1, k2), cap) in enumerate(rows):
    y = 150 + r * 860
    body += f'<div class="hz-abs" style="left:60px;top:{y}px;font:700 36px Inter;color:{A}">{title}</div>'
    for i, (lab, msgs, sh) in enumerate(steps):
        x = 60 + i * 470
        body += f'<div class="hz-abs" style="left:{x}px;top:{y+50}px;font:600 26px Inter;color:{T}">{i+1}. {lab}</div>'
        body += ph(x - 10, y + 95, .72, msgs, sh)
    x = 60 + 4 * 470
    body += f'<div class="hz-abs" style="left:{x}px;top:{y+50}px;font:600 26px Inter;color:{T}">5. Dashboard updates</div>'
    body += dcrop(k1, 1.05, x, y + 110, ring=k1) + dcrop(R["alerts"], .98, x, y + 300, ring=k2)
    body += f'<div class="hz-abs" style="left:{x}px;top:{y+640}px;width:440px;font:500 24px Inter;color:{T};opacity:.75">{cap}</div>'
html = f'<!doctype html><html><head><meta charset="utf-8"><style>{BASE_CSS}{CSS}html,body{{width:2420px!important;height:2760px!important}}</style></head><body style="background:{P["ground"]}">{body}</body></html>'
open(f"{OUT}/flows.html", "w").write(html); print("ok")
