import sys
from PIL import Image
d=sys.argv[1]
for s,o in zip("DEF","ABC"):
    W=Image.new("RGB",(540*3+40*4,960*2+40*3),"#1b1b1b")
    for i in range(6):
        im=Image.open(f"{d}/frames2/{s}{i+1}.png").convert("RGB").resize((540,960),Image.LANCZOS)
        r,c=divmod(i,3); W.paste(im,(40+c*580,40+r*1000))
    W.save(f"{d}/v2_sheet_{o}.png")
