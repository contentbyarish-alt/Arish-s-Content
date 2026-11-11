import json, sys
sc=json.load(open('scenes3/scenes.json'))
names={"s01":"01 VS opening","s02":"02 Face 1 - teen reason","s03":"03 Reason 1 - koi system nahi","s04":"04 Reason 2 - skilled manpower","s05":"05 Reason 3 - implementation","s06":"06 Hivon WhatsApp ERP","s07":"07 Business seekhte hain","s08":"08 SOPs","s09":"09 Face 2 - staff objection","s10":"10 Sab WhatsApp par","s11":"11 Attendance","s12":"12 Inward","s13":"13 Production entry","s14":"14 Dashboard","s15":"15 Price","s16":"16 Face 3 - CTA"}
T=sc[-1][2]
r=lambda f:f"{f}/25s"
o=['<?xml version="1.0" encoding="UTF-8"?>','<!DOCTYPE fcpxml>','<fcpxml version="1.9">',' <resources>',
'  <format id="r1" name="FFVideoFormat1080x1920p25" frameDuration="1/25s" width="1080" height="1920" colorSpace="1-1-1 (Rec. 709)"/>']
for i,(n,a,b) in enumerate(sc):
    o.append(f'  <asset id="a{i+1}" name="{names[n]}" start="0s" duration="{r(b-a)}" hasVideo="1" format="r1" videoSources="1"><media-rep kind="original-media" src="./media/{n}.mp4"/></asset>')
for k,(f,nm) in enumerate([("vo.wav","Voiceover"),("sfx.wav","SFX"),("bgm.wav","BGM")]):
    o.append(f'  <asset id="au{k+1}" name="{nm}" start="0s" duration="{r(T)}" hasAudio="1" audioSources="1" audioChannels="2" audioRate="48000"><media-rep kind="original-media" src="./media/{f}"/></asset>')
o+=[' </resources>',' <library>','  <event name="WhatsApp ERP vs Other ERP">','   <project name="WhatsApp ERP vs Other ERP - Reel">',
f'    <sequence format="r1" duration="{r(T)}" tcStart="0s" tcFormat="NDF" audioLayout="stereo" audioRate="48k">','     <spine>']
for i,(n,a,b) in enumerate(sc):
    o.append(f'      <asset-clip ref="a{i+1}" name="{names[n]}" offset="{r(a)}" start="0s" duration="{r(b-a)}" format="r1" tcFormat="NDF">')
    if i==0:
        o.append(f'       <asset-clip ref="au1" name="Voiceover" lane="-1" offset="0s" start="0s" duration="{r(T)}" audioRole="dialogue"/>')
        o.append(f'       <asset-clip ref="au2" name="SFX" lane="-2" offset="0s" start="0s" duration="{r(T)}" audioRole="effects"/>')
        o.append(f'       <asset-clip ref="au3" name="BGM" lane="-3" offset="0s" start="0s" duration="{r(T)}" audioRole="music"/>')
    o.append('      </asset-clip>')
o+=['     </spine>','    </sequence>','   </project>','  </event>',' </library>','</fcpxml>']
open(sys.argv[1],'w').write('\n'.join(o))
