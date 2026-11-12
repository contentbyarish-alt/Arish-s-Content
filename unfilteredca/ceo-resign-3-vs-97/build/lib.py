import random
G="#ECEAE4";T="#111418";RED="#B3261E";NAVY="#1D3557";PUR="#5B4B8A";OCH="#8A6A12";CARD="#F8F7F3";SKIN="#D8B48A"
BASE='''*{box-sizing:border-box;margin:0;padding:0}body{background:#222;font-family:Inter,sans-serif}
.fr{width:1080px;height:1920px;position:relative;overflow:hidden;background:#ECEAE4;color:#111418}
.fr>*{position:absolute}.fr>* .ab{position:absolute}
.ph{object-fit:cover}
.facebox{border:5px dashed #5B4B8A;background:repeating-linear-gradient(45deg,rgba(91,75,138,.10) 0 22px,rgba(91,75,138,.03) 22px 44px);display:flex;align-items:center;justify-content:center;text-align:center;font:700 34px/1.3 Inter;color:#5B4B8A}

'''
def tok(c,s=40,hand=False,extra=""):
    h=f'<path d="M34 30 L40 6" stroke="{c}" stroke-width="6" stroke-linecap="round"/>' if hand else ""
    return f'<svg width="{s}" height="{s*1.15:.0f}" viewBox="0 0 40 46" style="{extra}">{h}<circle cx="20" cy="13" r="10" fill="{c}"/><path d="M2 46c0-12 8-19 18-19s18 7 18 19z" fill="{c}"/></svg>'
def ramesh(w=220,pose="stand",shirt=RED,style="",face=True,flip=False,legs=T):
    arms={"stand":f'<path d="M66 150 L44 236" stroke="{shirt}" stroke-width="26" stroke-linecap="round"/><path d="M154 150 L176 236" stroke="{shirt}" stroke-width="26" stroke-linecap="round"/><circle cx="42" cy="244" r="13" fill="{SKIN}"/><circle cx="178" cy="244" r="13" fill="{SKIN}"/>',
          "up":f'<path d="M66 150 L44 236" stroke="{shirt}" stroke-width="26" stroke-linecap="round"/><path d="M154 152 L196 74" stroke="{shirt}" stroke-width="26" stroke-linecap="round"/><circle cx="42" cy="244" r="13" fill="{SKIN}"/><circle cx="200" cy="64" r="14" fill="{SKIN}"/>',
          "box":f'<path d="M66 150 L84 222" stroke="{shirt}" stroke-width="26" stroke-linecap="round"/><path d="M154 150 L140 222" stroke="{shirt}" stroke-width="26" stroke-linecap="round"/><rect x="58" y="196" width="108" height="76" rx="6" fill="#CDB892" stroke="{T}" stroke-width="5"/><path d="M58 220h108" stroke="{T}" stroke-width="4"/><circle cx="70" cy="232" r="12" fill="{SKIN}"/><circle cx="154" cy="232" r="12" fill="{SKIN}"/>',
          "point":f'<path d="M66 150 L44 236" stroke="{shirt}" stroke-width="26" stroke-linecap="round"/><path d="M154 156 L214 150" stroke="{shirt}" stroke-width="26" stroke-linecap="round"/><circle cx="42" cy="244" r="13" fill="{SKIN}"/><circle cx="224" cy="150" r="13" fill="{SKIN}"/>'}[pose]
    fc=f'<circle cx="96" cy="80" r="4.5" fill="{T}"/><circle cx="126" cy="80" r="4.5" fill="{T}"/><path d="M90 98c8-9 34-9 42 0c-8 6-34 6-42 0z" fill="{T}"/>' if face else ""
    tr='transform="translate(240,0) scale(-1,1)"' if flip else ""
    return f'''<svg width="{w}" height="{w*420/240:.0f}" viewBox="0 0 240 420" style="{style}"><g {tr}>
<rect x="76" y="250" width="30" height="140" rx="10" fill="{legs}"/><rect x="116" y="250" width="30" height="140" rx="10" fill="{legs}"/>
<rect x="64" y="384" width="46" height="18" rx="9" fill="{legs}"/><rect x="112" y="384" width="46" height="18" rx="9" fill="{legs}"/>
<rect x="58" y="128" width="106" height="142" rx="30" fill="{shirt}"/>{arms}
<rect x="100" y="112" width="22" height="26" fill="{SKIN}"/><circle cx="111" cy="78" r="44" fill="{SKIN}"/>
<path d="M67 76c-4-34 20-50 46-50s48 16 42 50c-8-18-22-26-44-26s-36 8-44 26z" fill="{T}"/>{fc}</g></svg>'''
def chair(w=200,c=CARD,o=T,style=""):
    return f'''<svg width="{w}" height="{w*1.5:.0f}" viewBox="0 0 200 300" style="{style}"><rect x="52" y="10" width="96" height="128" rx="22" fill="{c}" stroke="{o}" stroke-width="7"/><rect x="92" y="136" width="16" height="22" fill="{o}"/>
<rect x="34" y="154" width="132" height="34" rx="14" fill="{c}" stroke="{o}" stroke-width="7"/><rect x="93" y="188" width="14" height="62" fill="{o}"/>
<path d="M100 250 L36 276 M100 250 L164 276 M100 250 L100 282" stroke="{o}" stroke-width="9" stroke-linecap="round"/><circle cx="34" cy="282" r="9" fill="{o}"/><circle cx="166" cy="282" r="9" fill="{o}"/><circle cx="100" cy="288" r="9" fill="{o}"/></svg>'''
def page(css,frames):
    return f'<!doctype html><meta charset="utf-8"><style>{BASE}{css}</style>'+"".join(f'<div class="fr" id="f{i+1}" {a}>{h}</div>' for i,(a,h) in enumerate(frames))
