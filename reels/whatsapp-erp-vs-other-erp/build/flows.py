"""Complete WhatsApp ERP flows (Meta utility/interactive style) + dashboard crops, used together. SAMPLE data."""
import os, re
from comp import phone, BASE_CSS

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
AS = ROOT + "/assets2"
INK, MUT, LINK, GRN = "#101729", "#6B7280", "#1D8FF5", "#1DA35E"

# ---------- dashboard final state (all sample events applied) ----------
def make_dash():
    s = open(f"{AS}/dashboard_reel_static.svg").read()
    s = s.replace('<rect x="1457" y="703" width="79" height="26" rx="13" fill="#E9A23B"/>', '<rect x="1489" y="703" width="47" height="26" rx="13" fill="#55B685"/>')
    s = s.replace('<text class="badge" x="1496" y="720" text-anchor="middle" style="fill:#101729">PENDING</text>', '<text class="badge" x="1512" y="720" text-anchor="middle" style="fill:#101729">DONE</text>')
    s = s.replace('>Attendance: 94 present<', '>Check-in: Suresh · Plant 1<').replace('>Shift A • 09:30<', '>Inside radius • 09:01<')
    open(f"{AS}/dash_final.svg", "w").write(s)
    return f"{AS}/dash_final.svg"


DASH = make_dash()
# svg-space regions
R = dict(present=(1164, 204, 396, 148), prod=(320, 372, 396, 148), inv=(742, 372, 396, 148), inward=(1164, 372, 396, 148),
         headcount=(320, 204, 396, 148), chart=(320, 548, 760, 330), alerts=(1104, 548, 456, 330),
         a1=(1114, 636, 436, 56), a2=(1114, 694, 436, 56), a3=(1114, 752, 436, 56), a4=(1114, 810, 436, 56))

CSS = f"""
.w-msg{{width:330px;align-self:flex-start;background:#fff;border-radius:14px;box-shadow:0 1px 1.5px rgba(0,0,0,.18);color:{INK};overflow:hidden;flex:none}}
.w-b{{padding:10px 14px 7px}} .w-t{{font:700 16px Inter;margin-bottom:6px}} .w-x{{font:400 14px/1.42 Inter}}
.w-f{{display:flex;justify-content:space-between;align-items:flex-end;margin-top:7px;font:400 12px Inter;color:{MUT}}} .w-f span{{font-size:11px}}
.w-btn{{border-top:1px solid #E7E7E7;text-align:center;padding:10px;font:600 15px Inter;color:{GRN}}} .w-btn.on{{background:#E4F5EA}}
.w-out{{align-self:flex-end;background:#E2FBCB;border-radius:14px;padding:8px 13px 5px;font:400 14.5px Inter;color:{INK};box-shadow:0 1px 1.5px rgba(0,0,0,.18);flex:none;max-width:290px}}
.w-out small{{display:block;text-align:right;font-size:11px;color:{MUT};margin-top:2px}}
.w-doc{{display:flex;gap:10px;align-items:center;background:#F3F4F6;margin:-10px -14px 8px;padding:10px 14px}}
.w-pdf{{width:24px;height:30px;border-radius:4px;background:#D6203E;color:#fff;font:700 8px Inter;display:flex;align-items:center;justify-content:center}}
.w-list{{position:absolute;left:0;right:0;bottom:0;background:#fff;border-radius:22px 22px 0 0;padding:14px 0 18px;box-shadow:0 -10px 30px rgba(0,0,0,.18);z-index:8}}
.w-list h5{{font:700 17px Inter;color:{INK};text-align:center;margin:6px 0 10px}}
.w-li{{display:flex;justify-content:space-between;align-items:center;padding:13px 24px;border-top:1px solid #EFEFEF;font:500 15.5px Inter;color:{INK}}}
.w-li small{{display:block;font:400 12.5px Inter;color:{MUT};margin-top:2px}}
.w-rad{{width:20px;height:20px;border-radius:50%;border:2px solid #C4C7CC;flex:none}} .w-rad.on{{border:6px solid {GRN}}}
.w-send{{margin:14px 24px 0;background:{GRN};color:#fff;font:700 15px Inter;text-align:center;border-radius:22px;padding:11px}}
.hd-ring{{position:absolute;border:5px solid #55B685;border-radius:18px;box-shadow:0 0 0 6px rgba(85,182,133,.22)}}
"""
REPLY = f'<svg width="18" height="15" viewBox="0 0 20 16" style="vertical-align:-2px;margin-right:6px"><path d="M8 1 L1 7.500 L8 14 V10 C13 10 16 11.500 18.500 15 C18 9 14.500 5 8 5 Z" fill="none" stroke="{GRN}" stroke-width="1.8" stroke-linejoin="round"/></svg>'
LISTI = f'<svg width="18" height="14" style="vertical-align:-2px;margin-right:6px"><path d="M1 2h16M1 7h16M1 12h16" stroke="{GRN}" stroke-width="2"/></svg>'
LINKI = f'<svg width="16" height="16" style="vertical-align:-2px;margin-right:6px"><rect x="1" y="1" width="14" height="14" rx="3" fill="none" stroke="{GRN}" stroke-width="1.8"/><path d="M6 10l4-4M6.500 6h3.500v3.500" stroke="{GRN}" stroke-width="1.8" fill="none"/></svg>'


def tmsg(title, body, time, btns=(), on=None, doc=None):
    b = ''.join(f'<div class="w-btn {"on" if l == on else ""}">{ic}{l}</div>' for ic, l in btns)
    d = f'<div class="w-doc"><div class="w-pdf">PDF</div><div style="font:500 13.5px Inter">{doc}<div style="font:400 10.5px Inter;color:{MUT}">1 page · pdf</div></div></div>' if doc else ''
    return f'<div class="w-msg"><div class="w-b">{d}<div class="w-t">{title}</div><div class="w-x">{body}</div><div class="w-f">Powered by Hivon Automations<span>{time}</span></div></div>{b}</div>'


def wout(text, time):
    return f'<div class="w-out">{text}<small>{time} <span style="color:{LINK};letter-spacing:-3px">✓✓</span></small></div>'


def wloc(time):
    m = ('<svg width="250" height="130" viewBox="0 0 250 130"><rect width="250" height="130" fill="#E8EEF1"/><path d="M0 40 H250 M0 95 H250 M70 0 V130 M180 0 V130" stroke="#fff" stroke-width="9"/>'
         '<path d="M0 20 L250 120" stroke="#F5D98B" stroke-width="7"/><circle cx="125" cy="62" r="34" fill="rgba(29,163,94,.15)" stroke="#1DA35E" stroke-dasharray="4 4"/>'
         '<path d="M125 70 c-10 -14 -16 -20 -16 -30 a16 16 0 0 1 32 0 c0 10 -6 16 -16 30z" fill="#DD524C"/><circle cx="125" cy="40" r="6" fill="#fff"/></svg>')
    return f'<div class="w-out" style="padding:5px 5px 4px">{m}<div style="font:600 13.5px Inter;padding:5px 6px 0">📍 Plant 1 · live location</div><small style="padding-right:6px">{time} <span style="color:{LINK};letter-spacing:-3px">✓✓</span></small></div>'


def wlist(title, rows, sel):
    r = ''.join(f'<div class="w-li"><div>{a}<small>{b}</small></div><div class="w-rad {"on" if a == sel else ""}"></div></div>' for a, b in rows)
    return f'<div class="hz-dim"></div><div class="w-list"><div class="hz-grab"></div><h5>{title}</h5>{r}<div class="w-send">Send</div></div>'


def wflow(title, fields, btn="Submit"):
    fs = ''.join(f'<div class="hz-fl">{l}</div><div class="hz-fi {"hz-act" if a else ""}">{v}<span style="color:#9aa0a6">{"▾" if d else ""}</span></div>' for l, v, d, a in fields)
    return f'''<div class="hz-dim"></div><div class="hz-sheet"><div class="hz-grab"></div><div class="hz-sh-h"><span>{title}</span><small>✕</small></div>
<div style="font-size:13px;color:{MUT}">Hivon Automations · sample</div>{fs}<div class="hz-btn" style="background:{GRN}">{btn}</div></div>'''


DATE = '<div class="hz-date" style="flex:none">Today</div>'


def ph(x, y, s, msgs, sheet="", rot=0, extra=""):
    h = phone(x, y, s, DATE + msgs, sheet, rot, extra)
    return h.replace('<div class="hz-chat">', '<div class="hz-chat" style="justify-content:flex-end">', 1)


# ---------------- the three complete flows (each = list of (label, msgs, sheet)) ----------------
ATT1 = tmsg("Please Mark Your Attendance", "Hi, <b>Suresh (Operator)</b><br>Shift A shuru hone wali hai. Check-in karein.", "8:58 AM", [(REPLY, "Check-in"), (REPLY, "Apply Leave")])
ATT1on = ATT1.replace('<div class="w-btn ">' + REPLY + 'Check-in', '<div class="w-btn on">' + REPLY + 'Check-in', 1)
ATT2 = tmsg("Location Required", "Apni current location share karein,<br>taaki check-in verify ho sake.", "9:00 AM", [(REPLY, "📍 Send location")])
ATT3 = tmsg("✅ Check-in Successful", "👤 <b>Suresh (Operator)</b><br>🕘 In time: <b>9:01 AM</b><br>📍 Plant 1 · <b>inside radius</b><br>🏭 Shift A", "9:01 AM")
ATTENDANCE = [
    ("Reminder template", ATT1, ""),
    ("Check-in tap → location ask", ATT1on + wout("Check-in", "9:00 AM") + ATT2, ""),
    ("Live location shared", wout("Check-in", "9:00 AM") + ATT2 + wloc("9:01 AM"), ""),
    ("Check-in confirmed", ATT2 + wloc("9:01 AM") + ATT3, ""),
]
MENU = tmsg("Main Menu", "Namaste Ramesh 👋<br>Kya karna hai? Option chunein.", "10:12 AM", [(LISTI, "View Options")])
MENU_ROWS = [("Material Inward", "Gate par aaya maal"), ("Material Issue", "Production ko maal dena"), ("Stock Check", "Item ka live stock"), ("Purchase Request", "Naya maal mangwana")]
INW3 = tmsg("✅ GRN-101 Created", "📦 Steel Rod 12mm · <b>500 kg</b><br>🏢 Vendor A · Challan #4471<br>📊 Stock updated: <b>1,250 kg</b>", "10:15 AM", doc="GRN-101.pdf")
INWARD = [
    ("Hi → Main Menu", wout("Hi", "10:12 AM") + MENU, ""),
    ("Option select", wout("Hi", "10:12 AM") + MENU, wlist("View Options", MENU_ROWS, "Material Inward")),
    ("Inward form", wout("Hi", "10:12 AM") + MENU + wout("Material Inward", "10:13 AM"),
     wflow("Material Inward", [("Vendor", "Vendor A", True, False), ("Item", "Steel Rod 12mm", True, False), ("Quantity", "500 kg", False, True), ("Challan photo", "📎 challan_4471.jpg", False, False)])),
    ("GRN confirmed", MENU + wout("Material Inward", "10:13 AM") + INW3, ""),
]
PRD1 = tmsg("Production Update · Shift A", "Hi <b>Vikas (Supervisor)</b><br>Aaj ki production entry karein.", "5:55 PM", [(LINKI, "Update Production"), (REPLY, "Aaj ka target")])
PRD1on = PRD1.replace('<div class="w-btn ">' + LINKI, '<div class="w-btn on">' + LINKI, 1)
PRD3 = tmsg("✅ Production Logged", "⚙️ Machine <b>M-4</b> · Flange 40mm<br>✔️ OK: <b>120 pcs</b> · ✖️ Reject: <b>3</b><br>🎯 Target 150 · <b>80%</b>", "5:57 PM", doc="DPR-M4.pdf")
PRODUCTION = [
    ("6 PM reminder", PRD1, ""),
    ("Production form", PRD1on, wflow("Production Entry", [("Machine", "M-4 (CNC Lathe)", True, False), ("Item", "Flange 40mm", True, False), ("OK quantity (pcs)", "120", False, True), ("Rejection (pcs)", "3", False, False)])),
    ("Submit", PRD1on, wflow("Production Entry", [("Machine", "M-4 (CNC Lathe)", True, False), ("Item", "Flange 40mm", True, False), ("OK quantity (pcs)", "120", False, False), ("Rejection (pcs)", "3", False, False)], "Submitting…")),
    ("Logged + report", PRD1on + wout("Submitted", "5:57 PM") + PRD3, ""),
]


# ---------------- dashboard helpers ----------------
def dcrop(region, scale, left, top, ring=None, radius=24, extra="", pad=0, z=5):
    """Show a crop of the real dashboard. region=(x,y,w,h) in svg units or a key of R."""
    x, y, w, h = R[region] if isinstance(region, str) else region
    x -= pad; y -= pad; w += 2 * pad; h += 2 * pad
    rg = ""
    if ring:
        rx, ry, rw, rh = R[ring] if isinstance(ring, str) else ring
        rg = f'<div class="hd-ring" style="left:{(rx-x)*scale-6:.0f}px;top:{(ry-y)*scale-6:.0f}px;width:{rw*scale+12:.0f}px;height:{rh*scale+12:.0f}px"></div>'
    return f'''<div class="hz-abs" style="left:{left}px;top:{top}px;width:{w*scale:.0f}px;height:{h*scale:.0f}px;overflow:hidden;border-radius:{radius}px;background:#F9FAFC;z-index:{z};{extra}">
<img src="file://{DASH}" style="position:absolute;left:{-x*scale:.0f}px;top:{-y*scale:.0f}px;width:{1600*scale:.0f}px;height:{900*scale:.0f}px">{rg}</div>'''


def laptop(left, top, width, ring=None, z=4, dark=False):
    sc = width / 1600; h = 900 * sc
    rg = ""
    if ring:
        rx, ry, rw, rh = R[ring] if isinstance(ring, str) else ring
        rg = f'<div class="hd-ring" style="left:{rx*sc-5:.0f}px;top:{ry*sc-5:.0f}px;width:{rw*sc+10:.0f}px;height:{rh*sc+10:.0f}px;border-width:4px"></div>'
    return f'''<div class="hz-abs" style="left:{left-22}px;top:{top-22}px;width:{width+44}px;height:{h+44}px;border-radius:26px;background:{"#2A2F33" if dark else "#1E2326"};box-shadow:0 30px 60px rgba(0,0,0,.28);z-index:{z}">
<div style="position:absolute;left:22px;top:22px;width:{width}px;height:{h:.0f}px;overflow:hidden;border-radius:6px"><img src="file://{DASH}" style="width:{width}px;height:{h:.0f}px;display:block">{rg}</div></div>
<div class="hz-abs" style="left:{left-80}px;top:{top+h+22:.0f}px;width:{width+160}px;height:26px;border-radius:0 0 30px 30px;background:linear-gradient(#C9CFD3,#9DA5AB);z-index:{z}"></div>'''
