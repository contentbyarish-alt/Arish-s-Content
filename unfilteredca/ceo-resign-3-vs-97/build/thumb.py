from lib import *
D="font-family:'Inter Display',Inter;font-weight:900;letter-spacing:-.04em;line-height:.92;"
rings="".join(f'<div style="position:absolute;left:{540-r}px;top:{1060-r}px;width:{2*r}px;height:{2*r}px;border-radius:50%;border:3px solid rgba(17,20,24,{0.05+0.012*i:.3f})"></div>' for i,r in enumerate(range(1100,100,-110)))
def pc(src,x,y,w,h,rot,pos): return f'<div style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{h}px;overflow:hidden;border-radius:38px;border:8px solid {T};box-shadow:0 16px 0 {T};transform:rotate({rot}deg)"><img src="{src}" style="width:100%;height:100%;object-fit:cover;object-position:{pos};filter:grayscale(1) contrast(1.12)"></div>'
def out(x,y,r): return f'<div style="position:absolute;left:{x}px;top:{y}px;background:{RED};color:{CARD};font:900 44px Inter;border-radius:999px;padding:12px 30px;transform:rotate({r}deg);border:5px solid {CARD}">OUT</div>'
html=f'''<!doctype html><meta charset="utf-8"><style>*{{box-sizing:border-box;margin:0}}body{{width:1080px;height:1920px;background:{G};overflow:hidden;position:relative;font-family:Inter;color:{T}}}</style>{rings}
<div style="position:absolute;left:100px;top:380px;font:800 34px Inter;letter-spacing:.1em">@UNFILTEREDCA_</div>
<div style="position:absolute;left:92px;top:440px;{D}font-size:178px">Malik bhi</div>
<div style="position:absolute;left:92px;top:610px;{D}font-size:216px;color:{RED}">OUT?</div>
{pc("jensen.jpg",96,930,300,430,-6,"50% 0%")}{pc("ashneer.jpg",684,930,300,430,6,"47% 30%")}{pc("steve.jpg",372,980,336,470,0,"50% 30%")}
{out(290,900,-10)}{out(596,950,6)}{out(880,900,12)}
<div style="position:absolute;left:690px;top:630px;background:{T};color:{CARD};border-radius:30px;padding:18px 30px;transform:rotate(4deg);{D}font-size:84px;letter-spacing:-.03em"><span style="color:#F0A89F">3</span> vs <span style="color:#9DB7E8">97</span></div>
<div style="position:absolute;left:716px;top:790px;font:800 40px Inter;transform:rotate(4deg)">ka rule</div>'''
open("thumb.html","w").write(html)
