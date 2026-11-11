"""Hivon UI components rebuilt in HTML from the two Hivon SVGs (exact tokens),
plus Meta-style WhatsApp utility template parts (quick replies, list button, Flow form).
All data is SAMPLE data."""

# ---- Reel palette P3 Sage Calm (locked) ----
P = dict(ground="#E6EEE7", text="#13201B", accent="#2F7D57", problem="#B5483F",
         pending="#9A6A12", solved="#2F7D57", card="#F8FBF8", dark="#13201B",
         cta="#5EC26A", navy="#101729")

# ---- Hivon chat tokens (from hivon-whatsapp-chat.svg) ----
WA = dict(ink="#101729", muted="#6B7280", screen="#F6F6F6", chat="#EAE6DF",
          inb="#FFFFFF", outb="#E2FBCB", link="#1D8FF5", notice="#FFF3C4")
# ---- Hivon dashboard tokens (from hivon-erp-dashboard.svg) ----
DB = dict(ink="#101729", muted="#5B6475", line="#E6E9F0", canvas="#F9FAFC", card="#FFFFFF",
          mint="#EFFDF6", green="#55B685", deep="#43946C", amber="#E9A23B",
          coral="#DD524C", purple="#845EEE")

FONT = "Inter, 'Noto Color Emoji', sans-serif"

BASE_CSS = f"""
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{width:1080px;height:1920px;overflow:hidden}}
body{{font-family:{FONT};position:relative}}
.hz-abs{{position:absolute}}
/* ---------- phone (Hivon chat SVG geometry, 448x900 body, 420x872 screen) ---------- */
.hz-phone{{position:absolute;width:448px;height:900px;border-radius:64px;background:#0D0D0D;
  box-shadow:0 30px 60px rgba(16,23,41,.28),0 6px 14px rgba(16,23,41,.18);transform-origin:top left}}
.hz-phone:before{{content:'';position:absolute;left:-4px;top:50px;width:4px;height:46px;background:#2A2A2A;border-radius:2px}}
.hz-scr{{position:absolute;left:14px;top:14px;width:420px;height:872px;border-radius:52px;overflow:hidden;background:{WA['screen']}}}
.hz-notch{{position:absolute;left:202px;top:12px;width:16px;height:16px;border-radius:50%;background:#0D0D0D;z-index:5}}
.hz-status{{height:52px;display:flex;align-items:flex-end;justify-content:space-between;padding:0 30px 4px 36px;font-weight:700;font-size:16px;color:#111}}
.hz-head{{height:60px;display:flex;align-items:center;gap:12px;padding:0 18px;font-size:17px;font-weight:600;color:{WA['ink']};border-bottom:1px solid #e4e4e4}}
.hz-av{{width:40px;height:40px;border-radius:50%;background:#0D0D0D;color:#fff;font-weight:800;font-size:15px;display:flex;align-items:center;justify-content:center}}
.hz-chat{{position:absolute;top:112px;left:0;right:0;bottom:70px;background:{WA['chat']};padding:16px 14px;display:flex;flex-direction:column;gap:10px;overflow:hidden}}
.hz-input{{position:absolute;bottom:0;left:0;right:0;height:70px;background:{WA['screen']};display:flex;align-items:flex-start;padding:10px 16px;gap:10px}}
.hz-input i{{flex:1;height:34px;border-radius:17px;background:#fff;border:1px solid #D9D9D9;display:block}}
.hz-input b{{position:absolute;left:130px;bottom:10px;width:160px;height:5px;border-radius:3px;background:#0D0D0D}}
.hz-date{{align-self:center;background:#fff;border-radius:8px;padding:4px 14px;font-size:13px;color:{WA['ink']};box-shadow:0 1px 1.5px rgba(0,0,0,.18)}}
.hz-in,.hz-out{{max-width:330px;border-radius:14px;padding:10px 14px 8px;font-size:14.5px;line-height:1.42;color:{WA['ink']};box-shadow:0 1px 1.5px rgba(0,0,0,.18);position:relative}}
.hz-in{{background:{WA['inb']};align-self:flex-start;width:330px}}
.hz-out{{background:{WA['outb']};align-self:flex-end}}
.hz-in .hz-t{{font-weight:700;border-bottom:1.5px solid #9aa0a6;padding-bottom:5px;margin-bottom:6px}}
.hz-foot{{font-size:12.5px;color:{WA['muted']};border-top:1.5px solid #9aa0a6;margin-top:7px;padding-top:5px;display:flex;justify-content:space-between}}
.hz-foot span{{font-size:11px}}
.hz-tm{{font-size:11px;color:{WA['muted']};text-align:right;margin-top:2px}}
.hz-tick{{color:{WA['link']};font-weight:700;letter-spacing:-3px;margin-left:4px}}
.hz-qr{{width:330px;align-self:flex-start;margin-top:-8px;display:flex;flex-direction:column;gap:2px}}
.hz-qr div{{background:#fff;border-radius:0;padding:9px;text-align:center;color:{WA['link']};font-weight:600;font-size:14.5px;box-shadow:0 1px 1.5px rgba(0,0,0,.14)}}
.hz-qr div:first-child{{border-top:1px solid #eee}}
.hz-qr div:last-child{{border-radius:0 0 14px 14px}}
.hz-qr div.hz-on{{background:#EAF4FF}}
/* Flow bottom sheet */
.hz-sheet{{position:absolute;left:0;right:0;bottom:0;background:#fff;border-radius:22px 22px 0 0;padding:14px 22px 22px;box-shadow:0 -10px 30px rgba(0,0,0,.18);z-index:8}}
.hz-grab{{width:44px;height:5px;border-radius:3px;background:#cfd3d8;margin:0 auto 12px}}
.hz-sh-h{{display:flex;justify-content:space-between;align-items:center;font-weight:700;font-size:18px;color:{WA['ink']};margin-bottom:14px}}
.hz-sh-h small{{font-weight:500;color:{WA['muted']};font-size:13px}}
.hz-fl{{font-size:12.5px;color:{WA['muted']};margin:10px 0 5px;font-weight:600}}
.hz-fi{{border:1.5px solid #D9DEE5;border-radius:10px;padding:11px 12px;font-size:15px;color:{WA['ink']};display:flex;justify-content:space-between}}
.hz-fi.hz-act{{border-color:#1DAA61}}
.hz-btn{{margin-top:18px;background:#1DAA61;color:#fff;font-weight:700;text-align:center;border-radius:24px;padding:13px;font-size:16px}}
.hz-dim{{position:absolute;inset:0;background:rgba(0,0,0,.35);z-index:7}}
/* ---------- dashboard parts (Hivon ERP SVG look) ---------- */
.hd-card{{background:{DB['card']};border:1.5px solid {DB['line']};border-radius:18px;box-shadow:0 2px 8px rgba(16,23,41,.06);font-family:Inter;color:{DB['ink']}}}
.hd-kpi{{padding:24px 26px;position:relative}}
.hd-kpi h4{{font-size:19px;font-weight:600;color:#3B4457}}
.hd-kpi .hd-n{{font-size:62px;font-weight:800;letter-spacing:-1px;margin:4px 0 0}}
.hd-kpi p{{font-size:16px;color:{DB['muted']}}}
.hd-ic{{position:absolute;right:22px;top:20px;width:46px;height:46px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:22px}}
.hd-al{{padding:24px 26px}}
.hd-al h3{{font-size:27px;font-weight:800}}
.hd-al .hd-s{{font-size:16px;color:{DB['muted']};margin-bottom:10px}}
.hd-row{{display:flex;justify-content:space-between;align-items:center;padding:14px 0;border-bottom:1.5px solid {DB['line']}}}
.hd-row:last-child{{border-bottom:0}}
.hd-row b{{font-size:19px;font-weight:600;display:block}}
.hd-row span{{font-size:15px;color:{DB['muted']}}}
.hd-badge{{font-size:13px;font-weight:800;padding:6px 13px;border-radius:14px;letter-spacing:.04em}}
.hd-URGENT{{background:{DB['coral']};color:#fff}} .hd-PENDING{{background:{DB['amber']};color:{DB['ink']}}}
.hd-DONE{{background:{DB['green']};color:{DB['ink']}}} .hd-NEW{{background:{DB['ink']};color:#fff}}
.hd-hl{{background:{DB['mint']};margin:0 -14px;padding:14px;border-radius:12px;box-shadow:0 0 0 3px {DB['green']} inset}}
.hd-side{{background:#fff;border-right:1.5px solid {DB['line']}}}
.hz-sample{{position:absolute;font:600 22px Inter;color:rgba(19,32,27,.55);letter-spacing:.06em}}
"""


def phone(x, y, scale, chat_html, sheet_html="", rot=0, extra=""):
    return f"""<div class="hz-phone" style="left:{x}px;top:{y}px;transform:scale({scale}) rotate({rot}deg);{extra}">
<div class="hz-scr"><div class="hz-notch"></div>
<div class="hz-status"><span>9:30</span><svg width="72" height="14" viewBox="0 0 72 14"><g fill="#111"><rect x="0" y="9" width="4" height="4" rx="1"/><rect x="6" y="6" width="4" height="7" rx="1"/><rect x="12" y="3" width="4" height="10" rx="1"/><rect x="18" y="0" width="4" height="13" rx="1"/></g><path d="M30 6 a9 9 0 0 1 14 0 M33 9 a5 5 0 0 1 8 0" stroke="#111" stroke-width="2" fill="none"/><circle cx="37" cy="12" r="1.6" fill="#111"/><rect x="48" y="1.5" width="20" height="11" rx="3" fill="none" stroke="#111" stroke-width="1.5"/><rect x="50" y="3.5" width="16" height="7" rx="1.5" fill="#111"/></svg></div>
<div class="hz-head"><span style="font-size:22px">←</span><div class="hz-av">HI</div>Hivon Automations
<svg style="margin-left:auto" width="76" height="24" viewBox="0 0 76 24"><g fill="none" stroke="{WA['link']}" stroke-width="2"><rect x="1" y="5" width="22" height="16" rx="4"/><path d="M23 11 l11 -6 v16 l-11 -6"/><path d="M52 4 c2 0 4 4 4 6 c0 2 -3 2 -3 4 c1 3 4 6 7 7 c2 0 2 -3 4 -3 c2 0 6 2 6 4 c0 3 -3 4 -6 4 c-8 -1 -17 -10 -18 -18 c0 -3 1 -6 6 -6z"/></g></svg></div>
<div class="hz-chat">{chat_html}</div>
<div class="hz-input"><span style="color:{WA['link']};font-size:24px;line-height:30px">+</span><i></i><b></b></div>
{sheet_html}</div></div>"""


def tin(title, body, time="10:42", footer=True):
    f = f'<div class="hz-foot">Hivon Automations | WhatsApp ERP<span>{time}</span></div>' if footer else f'<div class="hz-tm">{time}</div>'
    return f'<div class="hz-in"><div class="hz-t">{title}</div>{body}{f}</div>'


def qr(*labels, on=None):
    return '<div class="hz-qr">' + ''.join(
        f'<div class="{"hz-on" if l == on else ""}">{l}</div>' for l in labels) + '</div>'


def tout(text, time="10:43"):
    return f'<div class="hz-out">{text}<div class="hz-tm">{time}<span class="hz-tick">✓✓</span></div></div>'


def flow(title, sub, fields, btn="Submit"):
    fs = ''.join(f'<div class="hz-fl">{l}</div><div class="hz-fi {"hz-act" if a else ""}">{v}<span style="color:#9aa0a6">{"▾" if d else ""}</span></div>'
                 for l, v, d, a in fields)
    return f'''<div class="hz-dim"></div><div class="hz-sheet"><div class="hz-grab"></div>
<div class="hz-sh-h"><span>{title}</span><small>✕</small></div><div style="font-size:13px;color:{WA['muted']}">{sub}</div>
{fs}<div class="hz-btn">{btn}</div></div>'''


# the one event shown in chat AND dashboard (principle 8)
def chat_production(stage="flow"):
    """Supervisor production update: template -> flow form -> confirmation."""
    msg1 = tin("🏭 Production Update", "Shift A ki production entry karein.<br>Machine aur quantity select karein.", "10:41")
    q = qr("📝 Entry karein", "📋 Aaj ka target", on="📝 Entry karein" if stage != "start" else None)
    done = tin("✅ Production Logged!", "⚙️ Machine: <b>M-4</b><br>📦 Item: <b>Flange 40mm</b><br>🔢 Qty: <b>120 pcs</b>", "10:42")
    if stage == "flow":
        sheet = flow("Production Entry", "Hivon Automations · sample", [
            ("Machine", "M-4  (CNC Lathe)", True, False),
            ("Item", "Flange 40mm", True, False),
            ("Quantity (pcs)", "120", False, True)])
        return '<div class="hz-date">Today</div>' + msg1 + q, sheet
    return '<div class="hz-date">Today</div>' + msg1 + q + done, ""


def kpi(title, num, cap, color, icon, icbg, extra=""):
    return f'''<div class="hd-card hd-kpi" style="{extra}"><h4>{title}</h4><div class="hd-n" style="color:{color}">{num}</div><p>{cap}</p>
<div class="hd-ic" style="background:{icbg}">{icon}</div></div>'''


def alerts(rows, hl=0, title="Live Alerts", extra=""):
    r = ''.join(f'<div class="hd-row {"hd-hl" if i == hl else ""}"><div><b>{a}</b><span>{b}</span></div><span class="hd-badge hd-{c}">{c}</span></div>'
                for i, (a, b, c) in enumerate(rows))
    return f'<div class="hd-card hd-al" style="{extra}"><h3>{title}</h3><div class="hd-s">Latest from WhatsApp ERP</div>{r}</div>'


ALERT_ROWS = [("Machine M-4: 120 pcs logged", "Shift A • Flange 40mm • 10:42", "NEW"),
              ("Inward: Steel rod 500 kg", "Gate entry • 10:15", "DONE"),
              ("Low stock: Flange blanks", "40 left • 09:58", "URGENT"),
              ("Attendance: 94 present", "Shift A • 09:30", "DONE")]


def bars(vals, w=560, h=260, color=DB['green'], hl=None, labels=None):
    n = len(vals); bw = w / n * 0.56; gap = w / n
    out = []
    for i, v in enumerate(vals):
        bh = v / 100 * (h - 40); x = i * gap + (gap - bw) / 2; y = h - 30 - bh
        c = DB['deep'] if i == hl else color
        out.append(f'<rect x="{x:.0f}" y="{y:.0f}" width="{bw:.0f}" height="{bh:.0f}" rx="8" fill="{c}"/>')
        if labels: out.append(f'<text x="{x+bw/2:.0f}" y="{h-6}" text-anchor="middle" font-family="Inter" font-size="16" fill="{DB["muted"]}">{labels[i]}</text>')
    return f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}">{"".join(out)}</svg>'


# ---------- 2D cast ----------
SKIN = ["#C98B5B", "#B57A4C", "#D7A273"]


def person(role, style, x, y, s=1.0, pose="stand", flip=False, rot=0):
    """Original flat 2D cast. role: owner|supervisor|worker|store. style: line|paper|pill."""
    skin = {"owner": SKIN[0], "supervisor": SKIN[1], "worker": SKIN[2], "store": SKIN[1]}[role]
    shirt = {"owner": "#F3EBDD", "supervisor": "#3E6FA8", "worker": "#2F7D57", "store": "#9A6A12"}[role]
    pants = {"owner": "#F3EBDD", "supervisor": "#2B3445", "worker": "#33404F", "store": "#3B3B3B"}[role]
    ink = P['text']
    import math
    # angles from straight down, positive = away from body; bend = extra angle for forearm
    la, ra, lb, rb = {"stand": (12, 12, 0, 0), "wave": (14, 150, 0, 20), "phone": (12, 40, 0, 95),
                      "shrug": (55, 55, 75, 75), "head": (140, 140, 75, 75), "point": (12, 88, 0, 0),
                      "carry": (25, 25, 70, 70)}[pose]
    def arm(sx, sy, side, a, b, L=78):
        ra_, rb_ = math.radians(a), math.radians(a + b)
        ex, ey = sx + side * L * 0.55 * math.sin(ra_), sy + L * 0.55 * math.cos(ra_)
        hx, hy = ex + side * L * 0.5 * math.sin(rb_), ey + L * 0.5 * math.cos(rb_)
        return (ex, ey, hx, hy)
    L = arm(68, 150, -1, la, lb); R = arm(132, 150, 1, ra, rb)
    if style == "line":
        sw = 5; st = f'stroke="{ink}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round"'
        fillc = lambda c: "url(#hatch)" if c not in ("#F3EBDD",) else "#F8FBF8"
        sk = "#F8FBF8"; sh = fillc(shirt); pa = "#F8FBF8"
    elif style == "paper":
        st = 'stroke="none"'; sk = skin; sh = shirt; pa = pants
    elif style == "comic":
        st = f'stroke="{ink}" stroke-width="6" stroke-linejoin="round"'; sk = skin; sh = shirt; pa = pants
    else:
        st = 'stroke="none"'; sk = skin; sh = shirt; pa = pants
    g = []
    # legs
    if style == "pill":
        g.append(f'<rect x="76" y="225" width="20" height="95" rx="10" fill="{pa}"/><rect x="104" y="225" width="20" height="95" rx="10" fill="{pa}"/>')
    else:
        if style == "comic": g.append(f'<path d="M84 230 L78 318 M116 230 L122 318" stroke="{ink}" stroke-width="33" stroke-linecap="round" fill="none"/>')
        g.append(f'<path d="M84 230 L78 318 M116 230 L122 318" {st if style=="line" else f"stroke=\"{pa}\" stroke-width=\"22\" stroke-linecap=\"round\""} fill="none"/>')
        g.append(f'<path d="M66 322 h24 M110 322 h24" stroke="{ink if style=="line" else "#1d1d1d"}" stroke-width="{8 if style!="line" else 6}" stroke-linecap="round"/>')
    # body
    if role == "owner":
        body = '<path d="M62 140 Q100 122 138 140 L146 262 Q100 272 54 262 Z"/>'  # kurta
    else:
        body = '<path d="M64 140 Q100 124 136 140 L140 236 Q100 244 60 236 Z"/>'
    if style == "pill":
        body = f'<rect x="58" y="126" width="84" height="{140 if role=="owner" else 116}" rx="40"/>'
    g.append(body.replace('/>', f' fill="{sh}" {st}/>').replace('<rect ', f'<rect fill="{sh}" ', 1) if style == "pill" else body.replace('/>', f' fill="{sh}" {st}/>'))
    if role == "supervisor" and style != "pill":
        g.append(f'<rect x="88" y="150" width="24" height="70" fill="#F4C542" opacity=".9" {st}/>')  # hi-vis stripe
    # arms
    acol = sh if style != "line" else "none"
    for (sx, sy), (ex, ey, hx, hy) in (((68, 150), L), ((132, 150), R)):
        if style == "line":
            g.append(f'<path d="M{sx} {sy} L{ex:.0f} {ey:.0f} L{hx:.0f} {hy:.0f}" fill="none" {st}/>')
            g.append(f'<circle cx="{hx:.0f}" cy="{hy:.0f}" r="8" fill="#F8FBF8" {st}/>')
        else:
            if style == "comic": g.append(f'<path d="M{sx} {sy} L{ex:.0f} {ey:.0f} L{hx:.0f} {hy:.0f}" fill="none" stroke="{ink}" stroke-width="31" stroke-linecap="round" stroke-linejoin="round"/><circle cx="{hx:.0f}" cy="{hy:.0f}" r="15" fill="{ink}"/>')
            g.append(f'<path d="M{sx} {sy} L{ex:.0f} {ey:.0f} L{hx:.0f} {hy:.0f}" fill="none" stroke="{shirt}" stroke-width="20" stroke-linecap="round" stroke-linejoin="round"/>')
            g.append(f'<circle cx="{hx:.0f}" cy="{hy:.0f}" r="10" fill="{skin}"/>')
            if style == "paper":
                g.append(f'<circle cx="{ex:.0f}" cy="{ey:.0f}" r="3.5" fill="#C9A646"/>')  # split pin
    if pose == "phone":
        hx, hy = R[2], R[3]
        g.append(f'<rect x="{hx-14:.0f}" y="{hy-30:.0f}" width="26" height="44" rx="5" fill="#0D0D0D"/><rect x="{hx-10:.0f}" y="{hy-25:.0f}" width="18" height="32" rx="2" fill="#5EC26A"/>')
    # head
    g.append(f'<rect x="90" y="108" width="20" height="22" fill="{sk}" {st}/>')
    g.append(f'<circle cx="100" cy="80" r="36" fill="{sk}" {st}/>')
    if style != "pill":
        g.append(f'<circle cx="88" cy="80" r="4" fill="{ink}"/><circle cx="112" cy="80" r="4" fill="{ink}"/>')
        g.append(f'<path d="M90 99 Q100 105 110 99" stroke="{ink}" stroke-width="3.5" fill="none" stroke-linecap="round"/>')
    else:
        g.append(f'<circle cx="89" cy="80" r="4.5" fill="{ink}"/><circle cx="111" cy="80" r="4.5" fill="{ink}"/>')
    # headwear / hair
    if role == "owner":
        g.append(f'<path d="M64 74 Q66 38 100 40 Q134 38 136 74 Q120 54 100 56 Q80 54 64 74Z" fill="{"#2b2b2b" if style!="line" else ink}"/>')
        if style != "pill":
            g.append(f'<path d="M86 93 Q100 88 114 93" stroke="{"#2b2b2b" if style!="line" else ink}" stroke-width="6" fill="none" stroke-linecap="round"/>')
            g.append(f'<rect x="78" y="72" width="18" height="13" rx="4" fill="none" stroke="{ink}" stroke-width="3"/><rect x="104" y="72" width="18" height="13" rx="4" fill="none" stroke="{ink}" stroke-width="3"/>')
    elif role == "supervisor":
        g.append(f'<path d="M60 70 Q62 34 100 34 Q138 34 140 70 Z" fill="#F4C542" {st}/><rect x="56" y="66" width="88" height="9" rx="4" fill="#E0AE2A" {st}/>')
    elif role == "worker":
        g.append(f'<path d="M64 66 Q66 40 100 40 Q134 40 136 66 Z" fill="#2F7D57" {st}/><path d="M130 64 h26" stroke="#2F7D57" stroke-width="9" stroke-linecap="round"/>')
    else:
        g.append(f'<path d="M64 70 Q66 40 100 42 Q134 40 136 70 Q118 56 100 58 Q82 56 64 70Z" fill="#3a2a1f"/>')
    tr = f'translate({x},{y}) scale({-s if flip else s},{s}) rotate({rot},100,180)'
    if flip: tr = f'translate({x + 200*s},{y}) scale({-s},{s}) rotate({rot},100,180)'
    shadow = ' filter="url(#paperdrop)"' if style == "paper" else ''
    return f'<g transform="{tr}"{shadow}>{"".join(g)}</g>'


def svg_defs():
    return f'''<defs>
<pattern id="hatch" width="10" height="10" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="10" height="10" fill="#F8FBF8"/><line x1="0" y1="0" x2="0" y2="10" stroke="{P['accent']}" stroke-width="2.4" opacity=".55"/></pattern>
<pattern id="hatchc" width="10" height="10" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="10" height="10" fill="#F6E9E7"/><line x1="0" y1="0" x2="0" y2="10" stroke="{P['problem']}" stroke-width="2.4" opacity=".6"/></pattern>
<filter id="paperdrop" x="-20%" y="-20%" width="140%" height="140%"><feDropShadow dx="0" dy="7" stdDeviation="2" flood-color="#13201B" flood-opacity=".22"/></filter>
<filter id="rough"><feTurbulence type="fractalNoise" baseFrequency="0.035" numOctaves="2" seed="4"/><feDisplacementMap in="SourceGraphic" scale="4"/></filter>
</defs>'''


def page(body, bg, extra_css=""):
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{BASE_CSS}{extra_css}</style></head><body style="background:{bg}">{body}</body></html>'


def face_placeholder(x, y, w, h, label="HEYGEN FACE · placeholder", radius=36, bg="#CFDCD1", ink=None):
    ink = ink or P['text']
    return f'''<div class="hz-abs" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;border-radius:{radius}px;background:{bg};overflow:hidden;
border:3px dashed rgba(19,32,27,.35)">
<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}"><circle cx="{w/2}" cy="{h*0.42}" r="{min(w,h)*0.17}" fill="rgba(19,32,27,.22)"/>
<path d="M{w*0.18} {h} Q{w*0.2} {h*0.66} {w/2} {h*0.64} Q{w*0.8} {h*0.66} {w*0.82} {h} Z" fill="rgba(19,32,27,.22)"/></svg>
<div style="position:absolute;left:0;right:0;top:22px;text-align:center;font:700 24px Inter;letter-spacing:.12em;color:{ink};opacity:.7">{label}</div></div>'''
