from lib import *
H=[];J=[]
def el(i,style,html="",cls=""): return f'<div id="{i}" class="{cls}" style="{style}">{html}</div>'
def scene(i,a,b,html,dark=False,rings=True):
    r=''.join(f'<div style="left:{540-q}px;top:{980-q}px;width:{2*q}px;height:{2*q}px;border-radius:50%;border:3px solid rgba({"248,247,243" if dark else "17,20,24"},{0.05+0.012*k:.3f})"></div>' for k,q in enumerate(range(1100,100,-110)))
    H.append(f'<div class="scene" id="{i}" data-a="{a}" data-b="{b}" style="background:{T if dark else G}"><div class="rings" id="{i}_rings">{r if rings else ""}</div><div class="cam" id="{i}_cam">{html}</div></div>')
D='font-family:\'Inter Display\',Inter;font-weight:900;letter-spacing:-.035em;line-height:.95;'
def pill(i,x,y,txt,bg=T,fg=CARD,fs=30,extra=""): return el(i,f"left:{x}px;top:{y}px;background:{bg};color:{fg};font:800 {fs}px Inter;border-radius:999px;padding:{fs*0.4:.0f}px {fs*0.85:.0f}px;white-space:nowrap;{extra}",txt)
def pcard(i,src,x,y,w,h,rot,pos):
    return el(i,f"left:{x}px;top:{y}px;width:{w}px;height:{h}px;overflow:hidden;border-radius:34px;border:7px solid {T};background:#bbb;box-shadow:0 14px 0 {T}",f'<img src="{src}" style="width:100%;height:100%;object-fit:cover;object-position:{pos};filter:grayscale(1) contrast(1.12)">',cls=f"rot{rot}")
def face(i,x,y,w,h,rad=34):
    return el(i,f"left:{x}px;top:{y}px;width:{w}px;height:{h}px;border-radius:{rad}px;border:7px solid {T};box-shadow:0 14px 0 {T};overflow:hidden;background:#d9d6ce",f'<img class="facevid" data-seg="{i}" style="width:100%;height:100%;object-fit:cover;object-position:55% 48%;display:none"><div class="faceph" style="width:100%;height:100%;display:flex;align-items:center;justify-content:center;text-align:center;font:700 40px/1.3 Inter;color:{PUR};background:repeating-linear-gradient(45deg,rgba(91,75,138,.12) 0 26px,rgba(91,75,138,.04) 26px 52px)">FACE<br>HeyGen clip<br>yahan aayega</div>')
strip=lambda sid,act: el(sid+"_st","left:100px;top:262px;width:880px;height:70px","".join(f'<div id="{sid}_st{k}" style="left:{[0,344,592][k]}px;top:0;font:800 30px Inter;border-radius:999px;padding:14px 24px;white-space:nowrap;{"background:"+c+";color:"+CARD if k==act else "border:4px solid "+c+";color:"+c+";padding:10px 20px"};{"filter:blur(7px);opacity:.55" if k>act else ""}{"opacity:.6" if k<act else ""}">{n}{" ✓" if k<act else ""}</div>' for k,(n,c) in enumerate([("01 Shareholders",NAVY),("02 Board",PUR),("03 CEO",OCH)])))
# ---------- S1 hook 0-5.80
h=el("h_co","left:100px;top:300px;width:880px;height:300px","".join(el(f"h_co{k}",f"left:0;top:0;{D}font-size:{s}px;color:{T};white-space:nowrap",n) for k,(n,s) in enumerate([("NVIDIA",190),("APPLE",190),("BHARATPE",150)])))
h+=el("h_t1",f"left:100px;top:270px;{D}font-size:128px","Company<br>banayi.")+el("h_t2",f"left:100px;top:528px;{D}font-size:128px;color:{RED}","Chali gayi.")
for k,(n,src,x,y,w,hh,rot,pos,nm) in enumerate([("j","jensen.jpg",92,800,290,430,-5,"50% 0%","Jensen Huang"),("s","steve.jpg",380,860,320,470,0,"50% 30%","Steve Jobs"),("a","ashneer.jpg",698,800,290,430,5,"47% 30%","Ashneer Grover")]):
    h+=pcard(f"h_p{n}",src,x,y,w,hh,rot,pos)+pill(f"h_n{n}",x+w/2-150,y+hh+26,nm,CARD,T,30,f"width:300px;text-align:center;border:5px solid {T}")+pill(f"h_o{n}",x+w-120,y-24,"OUT",RED,CARD,30)
scene("S1",0,5.80,h)
t0=[0.40,1.28,2.14]
for k,n in enumerate("jsa"):
    J.append(f"pop('h_p{n}',{t0[k]},.45);tw('h_p{n}','y',{t0[k]},.45,260,0,'back');pop('h_n{n}',{t0[k]+.18},.3);hid('h_o{n}');slam('h_o{n}',{[4.62,4.98,5.30][k]});")
    J.append(f"hid('h_co{k}');tw('h_co{k}','o',{t0[k]},.08,0,1);tw('h_co{k}','x',{t0[k]},.35,-120,0,'exp');"+(f"tw('h_co{k}','o',{t0[k+1]-.02},.06,1,0);" if k<2 else "tw('h_co2','o',3.34,.08,1,0);"))
J.append("hid('h_t1');hid('h_t2');pop('h_t1',3.42,.3);tw('h_t1','y',3.42,.3,60,0,'exp');pop('h_t2',4.50,.3);tw('h_t2','x',4.50,.3,-80,0,'exp');tw('S1_rings','s',0,5.8,1,1.45,'lin');")
# ---------- S2 face 5.80-10.07
h=face("F1",90,270,900,1060)+el("f1_q",f"left:130px;top:1150px;{D}font-size:92px;color:{CARD};background:{T};padding:18px 30px;border-radius:26px","Malik bhi <span style='color:#F0A89F'>out?</span>",cls="rot-3")
h+=el("f1_3",f"left:150px;top:1130px;{D}font-size:300px;color:{RED};-webkit-text-stroke:10px {CARD};paint-order:stroke fill","3")+el("f1_vs",f"left:360px;top:1270px;font:italic 700 96px 'Liberation Serif',serif;background:{CARD};border:5px solid {T};border-radius:20px;padding:0 22px","vs")+el("f1_97",f"left:540px;top:1130px;{D}font-size:300px;color:{NAVY};-webkit-text-stroke:10px {CARD};paint-order:stroke fill","97")
scene("S2",5.80,10.07,h)
J.append("hid('f1_q');pop('f1_q',6.12,.3);tw('f1_q','o',8.30,.12,1,0);hid('f1_3');hid('f1_vs');hid('f1_97');slam('f1_3',8.44);pop('f1_vs',8.60,.2);slam('f1_97',8.94);")
# ---------- S3 Ramesh story 10.07-21.76
FL=1100
crowd="".join(el(f"c{i}",f"left:{104+(i%14)*63+(8 if (i//14)%2 else 0)}px;top:{FL+14+(i//14)*47}px",tok(NAVY,50)) for i in range(97))
C=628.3
pie=f'''<svg width="520" height="520" viewBox="-130 -130 260 260"><circle r="100" fill="none" stroke="#D5D2CA" stroke-width="56"/><circle id="pie_red" r="100" fill="none" stroke="{RED}" stroke-width="56" stroke-dasharray="0 {C}" transform="rotate(-90)"/><circle id="pie_navy" r="100" fill="none" stroke="{NAVY}" stroke-width="56" stroke-dasharray="0 {C}" transform="rotate(-79.2)"/></svg>'''
bld=lambda w,c=T:f'<svg width="{w}" height="{w}" viewBox="0 0 100 100"><rect x="18" y="22" width="64" height="74" rx="5" fill="{CARD}" stroke="{c}" stroke-width="5"/>'+"".join(f'<rect x="{30+a*17}" y="{34+b*17}" width="9" height="9" fill="{c}"/>' for a in range(3) for b in range(2))+f'<rect x="43" y="72" width="14" height="24" fill="{c}"/><path d="M12 22h76" stroke="{c}" stroke-width="6" stroke-linecap="round"/></svg>'
coin=lambda s,txt="₹":f'<div style="width:{s}px;height:{s}px;border-radius:50%;background:#E0B94A;border:{max(3,s//14)}px solid {T};display:flex;align-items:center;justify-content:center;font:900 {s*0.5:.0f}px Inter;color:{T}">{txt}</div>'
h=el("r_h100",f"left:100px;top:262px;{D}font-size:170px","<span id='r_cnt'>100</span>%")+el("r_strike",f"left:96px;top:330px;width:440px;height:16px;background:{T};border-radius:8px",cls="rot-5")+el("r_h100l",f"left:104px;top:432px;font:800 34px Inter;letter-spacing:.04em","COMPANY RAMESH KI")
h+=el("r_ti",f"left:100px;top:270px;{D}font-size:120px","Maan lo…<br><span style='color:"+RED+"'>Ramesh.</span>")+el("r_h3",f"left:100px;top:262px;{D}font-size:230px;color:{RED}","3%")+el("r_h3l",f"left:104px;top:486px;font:800 34px Inter;letter-spacing:.04em;color:{RED}","AB RAMESH KA HISSA")
h+=el("r_pie","left:480px;top:480px;width:520px;height:520px",pie)+el("r_bld","left:650px;top:650px",bld(180))+el("r_sliver","left:480px;top:480px;width:520px;height:520px",f'<svg width="520" height="520" viewBox="-130 -130 260 260"><circle r="100" fill="none" stroke="{RED}" stroke-width="56" stroke-dasharray="{0.03*C:.1f} {C}" transform="rotate(-90)"/></svg>')
h+=pill("r_sl",610,440,"Ramesh · 3 hisse",RED,CARD,32)+pill("r_97",330,FL-44,"<span id='r_c97'>0</span> log · 97 hisse",NAVY,CARD,34,f"border:5px solid {G}")
h+=el("r_ram","left:110px;top:628px",ramesh(270,"point"))+pill("r_nm",150,556,"Ramesh",T,CARD,34)+el("r_coin","left:300px;top:680px",coin(96,"₹"))+pill("r_100",270,620,"₹100 lagaye",CARD,T,28,f"border:4px solid {T}")
h+=el("r_th","left:70px;top:462px;width:330px;height:170px;background:"+CARD+";border:6px solid "+T+";border-radius:50% / 46%;display:flex;align-items:center;justify-content:center",f'<div style="position:static;display:flex;align-items:flex-end;gap:10px"><div style="position:static">{bld(56)}</div><span style="font:900 50px Inter;color:{RED}">→</span><div style="position:static">{bld(110)}</div></div>')+el("r_thd","left:330px;top:612px;width:36px;height:36px;border-radius:50%;background:"+CARD+";border:5px solid "+T)
h+=el("r_fl",f"left:0;top:{FL}px;width:1080px;height:8px;background:{T}")+crowd
scene("S3",10.07,21.76,h)
J.append("""tw('r_ram','x',10.10,.8,-460,0,'out3');pop('r_ti',10.14,.3);tw('r_ti','o',13.5,.12,1,0);bob('r_ram',10.10,.8,5,14);hid('r_nm');pop('r_nm',11.14,.3);
hid('r_100');hid('r_coin');pop('r_coin',11.52,.25);pop('r_100',11.74,.25);tw('r_100','o',12.5,.15,1,0);tw('r_coin','x',12.45,.5,0,400,'io');tw('r_coin','y',12.45,.5,0,40,'in3');tw('r_coin','o',12.92,.06,1,0);
hid('r_bld');pop('r_bld',12.92,.4);hid('r_pie');tw('r_pie','o',13.50,.15,0,1);tw('r_pie','s',13.50,.4,.7,1,'back');
hid('r_h100');hid('r_h100l');pop('r_h100',13.64,.25);pop('r_h100l',14.36,.25);hid('r_strike');
fx.push(t=>{const p=cl((t-13.64)/.9);const q=cl((t-18.10)/2.1);txt('r_cnt',Math.round(100*eo(p)));dash('pie_red',eo(p));dash('pie_navy',.97*q);txt('r_c97',Math.round(97*q));});
hid('r_th');hid('r_thd');tw('r_nm','o',15.5,.1,1,0);pop('r_thd',15.56,.2);pop('r_th',15.70,.35);tw('r_th','o',17.80,.15,1,0);tw('r_thd','o',17.80,.15,1,0);
hid('r_97');pop('r_97',18.10,.3);tw('r_strike','o',18.24,.01,0,1);tw('r_strike','sx',18.24,.3,0,1,'exp');tw('r_h100','o',18.3,.3,1,.25);tw('r_h100l','o',18.3,.2,1,0);
tw('r_h100','o',20.30,.1,.25,0);tw('r_strike','o',20.30,.1,1,0);hid('r_h3');hid('r_h3l');slam('r_h3',20.36);pop('r_h3l',20.9,.25);
hid('r_sliver');hid('r_sl');tw('r_sliver','o',20.36,.05,0,1);tw('r_sliver','x',20.96,.3,0,-26,'back');tw('r_sliver','y',20.96,.3,0,-30,'back');pop('r_sl',21.06,.3);
""")
for i in range(97): J.append(f"hid('c{i}');pop('c{i}',{18.10+i*2.05/97:.3f},.22);")
# ---------- S4 three kinds 21.76-23.86
def tier(i,y,col,k,title,blur=True):
    return el(i,f"left:100px;top:{y}px;width:880px;height:240px;border-radius:30px;background:{CARD};border:6px solid {T}",f'<div style="left:34px;top:30px;font:800 28px Inter;letter-spacing:.06em;color:{col}">{k}</div><div style="left:34px;top:76px;{D}font-size:84px;color:{col};filter:blur(16px)">{title}</div><div style="left:36px;top:176px;width:520px;height:22px;border-radius:11px;background:{col};opacity:.35;filter:blur(8px)"></div><div style="left:700px;top:40px;{D}font-size:170px;color:{col};opacity:.5">?</div>')
h=el("t_t",f"left:100px;top:270px;{D}font-size:112px","Company mein<br><span style='color:"+RED+"'>3 tarah</span> ke log")+tier("t_1",620,NAVY,"01","Shareholders")+tier("t_2",890,PUR,"02","Board")+tier("t_3",1160,OCH,"03","CEO")
scene("S4",21.76,23.86,h)
J.append("pop('t_t',21.80,.3);hid('t_1');hid('t_2');hid('t_3');pop('t_1',22.66,.3);tw('t_1','x',22.66,.3,-200,0,'exp');pop('t_2',22.90,.3);tw('t_2','x',22.90,.3,200,0,'exp');pop('t_3',23.14,.3);tw('t_3','x',23.14,.3,-200,0,'exp');tw('S4_cam','s',23.60,.26,1,1.5,'in3');tw('S4_cam','o',23.72,.14,1,0);")
# ---------- S5 shareholders 23.86-37.55
sh="".join(el(f"s_k{i}",f"left:{150+(i%6)*135}px;top:{640+(i//6)*130}px",tok(NAVY,96)) for i in range(12))
co="".join(el(f"s_c{i}",f"left:{176+(i%6)*135}px;top:{760+(i//6)*130}px",coin(44)) for i in range(12))
hands="".join(el(f"s_b{i}",f"left:{20+(i%6)*62}px;top:{34+(i//6)*56}px",tok(CARD,50,hand=(i%3==0))) for i in range(54))
h=strip("s5",0)+el("s_t",f"left:100px;top:370px;{D}font-size:124px;color:{NAVY}","Shareholders")+pill("s_sub",104,520,"jinhone paisa lagaya",CARD,NAVY,34,f"border:5px solid {NAVY}")
h+=sh+co+el("s_box","left:400px;top:960px",bld(280,NAVY))+el("s_st",f"left:250px;top:1270px;{D}font-size:100px;color:{CARD};background:{NAVY};padding:16px 40px;border-radius:26px;border:7px solid {T}","ASLI MALIK",cls="rot-5")
h+=el("s_q",f"left:100px;top:370px;font:800 44px Inter;color:{NAVY}","Inki taakat?")+el("s_v1",f"left:100px;top:430px;{D}font-size:150px","1 hissa")+el("s_v2",f"left:100px;top:580px;{D}font-size:150px;color:{NAVY}","= 1 vote")
h+=el("s_bn","left:540px;top:560px;width:410px;height:720px;background:"+NAVY+";border-radius:30px 30px 0 0;border:6px solid "+T+";border-bottom:0;transform-origin:50% 100%",hands+f'<div style="left:0;top:560px;width:398px;text-align:center;{D}font-size:130px;color:{CARD}"><span id="s_n97">0</span></div>')
h+=el("s_br","left:150px;top:1196px;width:250px;height:84px;background:"+RED+";border-radius:22px 22px 0 0;border:6px solid "+T+";border-bottom:0;transform-origin:50% 100%",f'<div style="left:0;top:2px;width:238px;text-align:center;{D}font-size:74px;color:{CARD}">3</div>')
h+=el("s_ram","left:176px;top:846px",ramesh(200,"up"))+el("s_fl","left:0;top:1280px;width:1080px;height:8px;background:"+T)+el("s_l1",f"left:150px;top:1304px;font:800 28px Inter;letter-spacing:.06em;color:{RED}","RAMESH · 3 VOTE")+el("s_l2",f"left:540px;top:1304px;font:800 28px Inter;letter-spacing:.06em;color:{NAVY}","BAAKI · 97 VOTE")
h+=pill("s_mj",100,500,"Majority jeetegi ✓",T,CARD,44)+pill("s_vp",100,372,"1 hissa = 1 vote",CARD,NAVY,50,f"border:6px solid {NAVY}")
h+=el("s_cx",f"left:100px;top:380px;{D}font-size:110px","Ye log <span style='color:"+PUR+"'>board</span><br>ko chunte hain")+"".join(el(f"s_e{i}",f"left:{180+i*150}px;top:700px",tok(NAVY,110)) for i in range(5))
h+=el("s_ar","left:515px;top:850px;width:50px;height:230px",f'<div id="s_arl" style="left:19px;top:0;width:12px;height:190px;background:{T};transform-origin:50% 0"></div><div id="s_arh" style="left:-5px;top:180px;width:0;height:0;border-left:30px solid transparent;border-right:30px solid transparent;border-top:44px solid {T}"></div>')
h+=el("s_bc",f"left:140px;top:1100px;width:800px;height:230px;border-radius:30px;background:{CARD};border:6px solid {PUR}",f'<div style="left:34px;top:30px;font:800 28px Inter;color:{PUR}">02</div><div style="left:34px;top:76px;{D}font-size:100px;color:{PUR}">Board</div>')
scene("S5",23.86,37.55,h)
J.append("""tw('S5_cam','s',23.86,.3,.8,1,'exp');hid('s_t');hid('s_sub');slam('s_t',24.24);pop('s_sub',26.26,.3);
hid('s_box');pop('s_box',26.62,.35);hid('s_st');slam('s_st',27.98);
for(const i of ['s_t','s_sub','s_box','s_st']){tw(i,'o',28.92,.12,1,0);}
hid('s_q');hid('s_v1');hid('s_v2');pop('s_q',29.06,.25);slam('s_v1',29.96);slam('s_v2',30.42);tw('s_q','o',30.85,.1,1,0);tw('s_v1','o',30.86,.1,1,0);tw('s_v2','o',30.86,.1,1,0);hid('s_vp');pop('s_vp',30.92,.25);
hid('s_fl');tw('s_fl','o',30.9,.1,0,1);hid('s_ram');pop('s_ram',30.94,.3);hid('s_br');tw('s_br','o',31.5,.01,0,1);tw('s_br','sy',31.5,.3,0,1,'back');hid('s_l1');pop('s_l1',31.6,.2);
hid('s_bn');tw('s_bn','o',32.2,.01,0,1);tw('s_bn','sy',32.2,1.3,0,1,'out3');hid('s_l2');pop('s_l2',33.3,.2);fx.push(t=>txt('s_n97',Math.round(97*eo(cl((t-32.2)/1.3)))));
hid('s_mj');slam('s_mj',34.05);tw('s_bn','sx',34.71,.15,1,1.05,'io');tw('s_bn','sx',34.90,.2,1.05,1,'io');
for(const i of ['s_vp','s_fl','s_ram','s_br','s_bn','s_l1','s_l2','s_mj']){tw(i,'o',35.50,.1,1,0);}
hid('s_cx');pop('s_cx',35.62,.3);hid('s_ar');hid('s_bc');tw('s_ar','o',36.6,.05,0,1);tw('s_arl','sy',36.6,.35,0,1,'out3');hid('s_arh');tw('s_arh','o',36.9,.08,0,1);
tw('s_bc','o',36.3,.3,0,.75);tw('s_bc','blur',36.3,.01,14,14);tw('s_bc','blur',37.0,.4,14,0,'io');tw('s_bc','o',37.0,.3,.75,1);tw('S5_cam','s',37.30,.25,1,1.35,'in3');tw('S5_cam','y',37.30,.25,0,-420,'in3');
""")
for i in range(12): J.append(f"hid('s_k{i}');pop('s_k{i}',{25.50+i*.06:.2f},.25);hid('s_c{i}');tw('s_c{i}','o',{26.70+i*.07:.2f},.05,0,1);tw('s_c{i}','x',{26.70+i*.07:.2f},.45,0,{540-22-(176+(i%6)*135)},'io');tw('s_c{i}','y',{26.70+i*.07:.2f},.45,0,{1040-(760+(i//6)*130)},'in3');tw('s_c{i}','o',{27.13+i*.07:.2f},.05,1,0);tw('s_k{i}','o',28.92,.12,1,0);")
for i in range(5): J.append(f"hid('s_e{i}');pop('s_e{i}',{35.70+i*.07:.2f},.25);")
# ---------- S6 board 37.55-51.50
mem="".join(el(f"b_m{i}",f"left:{224+i*130}px;top:640px",tok(PUR,120)) for i in range(5))
def crow(i,y,txt,hi=False): return el(i,f"left:100px;top:{y}px;width:880px;height:{130 if hi else 108}px;border-radius:26px;background:{PUR if hi else CARD};color:{CARD if hi else T};border:6px solid {T};font:800 {54 if hi else 46}px Inter;display:flex;align-items:center;padding-left:34px",f'<span style="color:{CARD if hi else PUR};margin-right:22px;font-weight:900">✓</span>{txt}')
h=strip("s6",1)+el("b_t",f"left:100px;top:370px;{D}font-size:118px;color:{PUR}","Board of<br>Directors")+el("b_tb",f"left:190px;top:770px;width:700px;height:96px;border-radius:48px;background:{PUR};border:6px solid {T}")+mem
h+=el("b_5",f"left:806px;top:372px;{D}font-size:230px;color:{PUR}","5")+pill("b_ch",250,900,"↑ shareholders ne chuna",NAVY,CARD,38)
h+=el("b_no","left:160px;top:1040px;width:760px;height:170px;border-radius:30px;background:"+CARD+";border:6px solid "+T,f'<div style="left:28px;top:30px">{coin(104)}</div><div style="left:14px;top:74px;width:134px;height:14px;background:{RED};border-radius:7px;transform:rotate(-38deg)"></div><div style="left:170px;top:28px;font:800 44px/1.2 Inter">Khud ka paisa?<br><span style="color:{RED}">Zaroori nahi.</span></div>')
h+=el("b_k",f"left:100px;top:660px;{D}font-size:96px","Kaam: <span style='color:"+PUR+"'>bade faisle</span>")+crow("b_r1",800,"Naya loan lena ya nahi")+crow("b_r2",926,"Company ki direction")+crow("b_r3",1052,"CEO kaun rahega",True)
h+=el("b_chair","left:420px;top:900px",chair(240,CARD,T))+el("b_ceo","left:455px;top:800px",ramesh(170,"stand",shirt=OCH))+pill("b_rk",130,820,"Rakh sakte hain ✓",T,CARD,44)+pill("b_ht",470,1290,"Hata bhi sakte hain",RED,CARD,52)
scene("S6",37.55,51.50,h)
J.append("""tw('S6_cam','s',37.55,.3,.82,1,'exp');hid('b_t');slam('b_t',37.97);hid('b_tb');pop('b_tb',38.93,.3);hid('b_5');slam('b_5',39.21);hid('b_ch');pop('b_ch',40.55,.3);hid('b_no');pop('b_no',41.73,.3);tw('b_no','r',42.94,.12,0,-3,'io');tw('b_no','r',43.06,.12,-3,0,'io');
for(const i of ['b_t','b_5','b_ch','b_no']){tw(i,'o',43.5,.1,1,0);} tw('b_tb','y',43.5,.35,0,-330,'io');tw('b_tb','s',43.5,.35,1,.8,'io');
hid('b_k');pop('b_k',43.84,.3);hid('b_r1');hid('b_r2');hid('b_r3');pop('b_r1',44.96,.3);tw('b_r1','x',44.96,.3,-160,0,'exp');pop('b_r2',46.16,.3);tw('b_r2','x',46.16,.3,-160,0,'exp');slam('b_r3',47.94);
for(const i of ['b_k','b_r1','b_r2']){tw(i,'o',49.2,.12,1,0);} tw('b_r3','y',49.2,.35,0,-392,'io');
hid('b_chair');pop('b_chair',49.30,.3);hid('b_ceo');tw('b_ceo','o',49.90,.05,0,1);tw('b_ceo','y',49.90,.3,-300,0,'back');hid('b_rk');pop('b_rk',49.94,.25);
tw('b_ceo','x',50.80,.5,0,760,'in3');tw('b_ceo','y',50.80,.5,0,-260,'out3');tw('b_ceo','r',50.80,.5,0,200,'lin');tw('b_rk','o',50.78,.08,1,0);hid('b_ht');slam('b_ht',50.84);tw('b_chair','r',50.82,.1,0,-7,'io');tw('b_chair','r',50.92,.2,-7,0,'io');
""")
for i in range(5): J.append(f"hid('b_m{i}');pop('b_m{i}',{39.21+i*.2:.2f},.25);tw('b_m{i}','y',43.5,.35,0,-330,'io');tw('b_m{i}','x',43.5,.35,0,{(2-i)*26},'io');tw('b_m{i}','s',43.5,.35,1,.8,'io');")
# ---------- S7 CEO 51.50-59.16
chips=[("c_1","Roz ka kaam",120,1150,54.66,T),("c_2","Staff",130,820,55.36,OCH),("c_3","Sales",730,800,55.82,OCH),("c_4","Maal",760,1010,56.20,OCH),("c_5","Sab kuch sambhalna",470,1150,56.90,T)]
h=strip("s7",2)+el("e_t",f"left:100px;top:360px;{D}font-size:300px;color:{OCH}","CEO")+pill("e_b",610,640,"↓ Board ne rakha",PUR,CARD,40)
h+=el("e_desk",f"left:330px;top:1040px;width:420px;height:26px;border-radius:13px;background:{T}")+el("e_dl","left:370px;top:1066px;width:18px;height:90px;background:"+T)+el("e_dr","left:692px;top:1066px;width:18px;height:90px;background:"+T)+el("e_ch","left:440px;top:830px",chair(200,CARD,T))+el("e_ram","left:432px;top:700px",ramesh(216,"stand",shirt=OCH))
h+="".join(pill(i,x,y,txt,CARD if c==OCH else T,T if c==OCH else CARD,44,f"border:6px solid {T}") for i,txt,x,y,_,c in chips)
h+=el("e_no",f"left:150px;top:1258px;{D}font-size:104px;color:{RED}","Bade faisle ✕")+pill("e_bd",250,1376,"wo Board ka kaam hai",PUR,CARD,46)
scene("S7",51.50,59.16,h)
J.append("""tw('S7_cam','s',51.50,.3,.82,1,'exp');hid('e_t');slam('e_t',52.30);hid('e_b');pop('e_b',53.10,.3);tw('e_b','y',53.10,.3,-80,0,'back');
for(const i of ['e_desk','e_dl','e_dr','e_ch','e_ram']){hid(i);pop(i,53.90,.3);} bob('e_ram',54.5,2.8,2.5,7);
hid('e_no');slam('e_no',57.46);hid('e_bd');pop('e_bd',58.30,.3);""")
for i,txt,x,y,t,c in chips: J.append(f"hid('{i}');pop('{i}',{t},.28);tw('{i}','o',57.36,.1,1,{.25});")
# ---------- S8 face 59.16-66.60
def lad(i,y,col,txt,sub): return el(i,f"left:150px;top:{y}px;width:780px;height:150px;border-radius:30px;background:{col};border:6px solid {T};color:{CARD}",f'<div style="left:36px;top:22px;{D}font-size:86px">{txt}</div><div style="right:34px;top:54px;font:800 30px Inter;opacity:.9">{sub}</div>')
arr=lambda i,y:el(i,f"left:500px;top:{y}px;width:80px;height:70px",f'<div style="left:32px;top:0;width:16px;height:36px;background:{T}"></div><div style="left:10px;top:30px;width:0;height:0;border-left:30px solid transparent;border-right:30px solid transparent;border-top:38px solid {T}"></div>')
h=face("F2",90,270,900,1060)+pill("f2_a",130,1180,"Ramesh CEO bhi hai",T,CARD,56)+el("f2_b",f"left:560px;top:1050px;{D}font-size:150px;color:{RED};-webkit-text-stroke:10px {CARD};paint-order:stroke fill","Kyun?",cls="rot-5")+pill("f2_c",130,1180,"Kyunki board ne rakha",PUR,CARD,56)
h+=lad("l_1",860,NAVY,"Malik","shareholders")+arr("l_a1",1012)+lad("l_2",1086,PUR,"Board","bade faisle")+arr("l_a2",1238)+lad("l_3",1312,OCH,"CEO","roz ka kaam")
scene("S8",59.16,66.60,h)
J.append("""hid('f2_a');pop('f2_a',59.62,.3);tw('f2_a','o',60.72,.1,1,0);hid('f2_b');slam('f2_b',61.20);tw('f2_b','o',61.86,.1,1,0);hid('f2_c');pop('f2_c',61.90,.3);tw('f2_c','o',62.56,.1,1,0);
tw('F2','s',62.56,.4,1,.5,'io');tw('F2','y',62.56,.4,0,-268,'io');
for(const [i,t] of [['l_1',63.18],['l_a1',63.84],['l_2',63.58],['l_a2',64.92],['l_3',64.46]]){hid(i);pop(i,t,.3);}
for(const [i,t] of [['l_1',65.34],['l_a1',65.5],['l_2',65.66],['l_a2',65.84],['l_3',66.0]]){tw(i,'s',t,.14,1,1.1,'io');tw(i,'s',t+.14,.2,1.1,1,'io');}
""")
# ---------- S9 Jensen 66.60-70.56
h=el("j_k",f"left:100px;top:270px;font:800 36px Inter;letter-spacing:.08em","NVIDIA · JENSEN HUANG")+el("j_n",f"left:92px;top:320px;{D}font-size:300px;color:{RED}","<span id='j_cnt'>0.0</span>%")+el("j_s",f"left:106px;top:610px;font:800 54px Inter","share the. Phir bhi…")
h+=pcard("j_p","jensen.jpg",250,740,560,620,-3,"50% 6%")+pill("j_o",560,700,"OUT",RED,CARD,60)+el("j_f",f"left:100px;top:1400px;width:880px;text-align:center;font:700 30px/1.35 Inter;background:{CARD};border:4px solid {T};border-radius:20px;padding:14px 10px","Board investigation ke baad resign · 12 Nov 2026")
scene("S9",66.60,70.56,h)
J.append("""tw('S9_cam','s',66.60,.3,1.25,1,'exp');pop('j_k',66.66,.2);tw('j_p','y',66.66,.4,400,0,'back');hid('j_n');slam('j_n',68.30);fx.push(t=>txt('j_cnt',(3.5*eo(cl((t-68.30)/.6))).toFixed(1)));hid('j_s');pop('j_s',69.14,.25);hid('j_o');slam('j_o',69.90);hid('j_f');pop('j_f',69.6,.3);tw('S9_rings','s',66.6,4,1,1.3,'lin');""")
# ---------- S10 punch 70.56-73.50 (dark)
SC=1.132
drop=lambda i,x,y,s=1:el(i,f"left:{x}px;top:{y}px",f'<svg width="{30*s:.0f}" height="{42*s:.0f}" viewBox="0 0 30 42"><path d="M15 2 C15 2 3 20 3 28 a12 12 0 0 0 24 0 C27 20 15 2 15 2z" fill="#7CC4F2" stroke="{T}" stroke-width="3"/><path d="M9 28 a6 6 0 0 0 5 6" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/></svg>')
drops="".join(drop(f"d{i}",(183 if i%2==0 else 256)-15+(-6 if i%2==0 else 6),176,1.35) for i in range(10))
jc=el("p_j","left:560px;top:880px;width:430px;height:475px;border-radius:34px;border:7px solid "+CARD+";box-shadow:0 14px 0 "+CARD+";overflow:hidden;background:#000",f'<img src="jensen.jpg" style="left:{-180*SC:.0f}px;top:{-60*SC:.0f}px;width:{736*SC:.0f}px;filter:grayscale(1) contrast(1.12)">'+drops,cls="rot4")
bm="".join(el(f"p_m{i}",f"left:{250+i*118}px;top:330px",tok(PUR,104)) for i in range(5))
h=el("p_sp","left:0;top:0;width:1080px;height:1920px;background:radial-gradient(ellipse 380px 520px at 300px 1150px,rgba(248,247,243,.20),rgba(248,247,243,0) 72%)")+bm+el("p_tb",f"left:190px;top:428px;width:700px;height:90px;border-radius:45px;background:{PUR};border:6px solid {CARD}")
h+=el("p_bub",f"left:120px;top:578px;width:840px;height:250px;background:{CARD};border-radius:40px",f'<div style="left:390px;top:-30px;width:0;height:0;border-left:28px solid transparent;border-right:28px solid transparent;border-bottom:38px solid {CARD}"></div><div id="p_w1" style="left:40px;top:26px;font:800 44px Inter;color:{T}">“Ramesh,</div><div id="p_w2" style="left:36px;top:92px;{D}font-size:104px;color:{T};white-space:nowrap">kal se</div><div id="p_w3" style="left:338px;top:92px;{D}font-size:104px;color:{RED};white-space:nowrap">mat aana.”</div>')
h+=el("p_ch","left:170px;top:900px",chair(270,CARD,T))+pill("p_kk",130,1320,"Kursi khaali",RED,CARD,50)+jc+el("p_fl",f"left:0;top:1420px;width:1080px;height:8px;background:{CARD}")
scene("S10",70.56,73.50,h,dark=True)
J.append("""tw('S10_cam','s',70.56,.25,1.2,1,'exp');for(let i=0;i<5;i++){hid('p_m'+i);pop('p_m'+i,70.62+i*.05,.2);} hid('p_bub');pop('p_bub',71.36,.3);
hid('p_w1');hid('p_w2');hid('p_w3');pop('p_w1',71.70,.15);slam('p_w2',72.12);slam('p_w3',72.46);tw('p_j','x',70.9,.45,560,0,'back');hid('p_kk');slam('p_kk',72.96);tw('p_ch','r',72.96,.12,0,-8,'io');tw('p_ch','r',73.08,.25,-8,0,'io');
tw('p_j','r',72.46,.08,0,2,'io');tw('p_j','r',72.54,.08,2,-2,'io');tw('p_j','r',72.62,.1,-2,0,'io');
fx.push(t=>{for(let i=0;i<10;i++){const e=document.getElementById('d'+i);const ph=((t-71.3)/0.62+i/10*1.0)%1;const on=t>71.3+ (i/10)*0.62;const p=ph<0?0:ph;e.style.opacity=on?(p<.08?p/.08:(p>.85?(1-p)/.15:1)):0;const side=i%2==0?-1:1;e.style.transform=`translate(${side*(8+34*p)}px,${p*p*270+p*30}px) scale(${.55+.7*Math.min(1,p*3)})`;}});
""")
# ---------- S11 3% still his 73.50-76.05
h=el("k_s0",f"left:100px;top:270px;{D}font-size:128px","Kursi gayi.<br>Par…")+el("k_t",f"left:100px;top:270px;{D}font-size:330px;color:{RED}","3%")+el("k_s",f"left:106px;top:590px;{D}font-size:92px","share abhi bhi<br>Ramesh ke.")
h+=el("k_pie","left:520px;top:780px;width:440px;height:440px",f'<svg width="440" height="440" viewBox="-130 -130 260 260"><circle r="100" fill="none" stroke="{NAVY}" stroke-width="56" stroke-dasharray="{0.97*C:.1f} {C}" transform="rotate(-79.2)" opacity=".35"/><g id="k_sl" transform="translate(-10,-12)"><circle r="100" fill="none" stroke="{RED}" stroke-width="64" stroke-dasharray="{0.03*C:.1f} {C}" transform="rotate(-90)"/></g></svg>')
h+=el("k_ram","left:150px;top:842px",ramesh(260,"box"))+el("k_fl","left:0;top:1290px;width:1080px;height:8px;background:"+T)+pill("k_p",330,1330,"Shareholder abhi bhi ✓",T,CARD,48)
scene("S11",73.50,76.05,h)
J.append("""tw('S11_cam','s',73.50,.3,.85,1,'exp');pop('k_s0',73.66,.25);tw('k_s0','o',74.80,.08,1,0);hid('k_t');slam('k_t',74.86);hid('k_s');pop('k_s',75.20,.25);tw('k_ram','x',73.5,2.55,-60,60,'lin');bob('k_ram',73.5,2.55,5,10);hid('k_p');pop('k_p',75.50,.25);
fx.push(t=>{const g=document.getElementById('k_sl');const p=.5+.5*Math.sin((t-73.5)*9);g.setAttribute('transform',`translate(${-10-4*p},${-12-5*p})`);});""")
# ---------- S12 CTA face 76.05-78.65
h=el("z_card","left:120px;top:280px;width:840px;height:1190px;border-radius:56px;background:rgba(248,247,243,.82);border:3px solid #fff;box-shadow:0 30px 80px rgba(17,20,24,.18)")+face("F3",280,330,520,520,260)
h+=el("z_t",f"left:120px;top:900px;width:840px;text-align:center;{D}font-size:100px","Kuch naya<br>seekha?")+el("z_l",f"left:180px;top:1140px;width:330px;text-align:center;font:800 54px Inter;border:6px solid {T};border-radius:999px;padding:20px;background:{CARD}","<span style='color:"+RED+"'>♥</span> Like")+el("z_f",f"left:540px;top:1140px;width:360px;text-align:center;font:800 54px Inter;background:{T};color:{CARD};border-radius:999px;padding:26px 20px","+ Follow")
h+=el("z_h","left:120px;top:1310px;width:840px;text-align:center;font:800 40px Inter","@unfilteredca_<br><span style='font-weight:600;font-size:30px;opacity:.7'>Facebook: Tax Khabari</span>")
scene("S12",76.05,78.66,h)
J.append("""tw('S12_cam','s',76.05,.3,.85,1,'exp');hid('z_t');pop('z_t',76.40,.3);hid('z_l');slam('z_l',77.60);hid('z_f');slam('z_f',78.10);tw('z_l','s',77.9,.1,1,1.08,'io');tw('z_l','s',78.0,.15,1.08,1,'io');pop('z_h',76.9,.3);tw('S12_rings','s',76.05,2.6,1,1.2,'lin');""")
# ---------- captions
CAPS=[(0.40,"Nvidia ke *Jensen Huang*"),(1.30,"*Steve Jobs*"),(2.16,"*Ashneer Grover*"),(3.42,"Teeno ne apni company banayi"),(4.50,"aur teeno ki company *chali gayi*"),
(5.92,"But malik ko company se"),(7.04,"kaise *nikala* ja sakta hai?"),(8.12,"Iske liye *3 versus 97* ka rule"),(9.60,"sun lo"),
(10.10,"Maan lo ek aadmi hai *Ramesh*"),(11.50,"usne *100 rupay* lagaye"),(12.50,"aur apni company shuru kari"),(13.64,"Abhi *100%* company Ramesh ki hai"),
(15.48,"Ab Ramesh ne socha"),(16.18,"mujhe company *badi* karni hai"),(17.18,"akele nahi chalegi"),(18.00,"To usne *97 logon* ko"),(19.26,"97 hisse bech diye"),(20.34,"Ab Ramesh ke paas bache *3 hisse*"),
(21.80,"Uske baad company mein"),(22.66,"*teen tarike* ke log hain"),(23.90,"Pehla: *shareholder*"),(24.72,"yaani promoter"),(25.50,"Ye wo log hain jinhone"),(26.62,"company mein *paisa lagaya* hai"),(27.76,"yaani *asli malik* yahi hain"),
(29.06,"Inki taakat kya hoti hai?"),(29.96,"*Ek hissa, ek vote*"),(30.94,"Ramesh ke paas *teen vote*"),(31.96,"baaki 97 logon ke paas *97 vote*"),(34.05,"*Majority* jo bolegi, wahi hoga"),(35.59,"Aur sabse badi baat"),(36.39,"ye log *board* ko chunte hain"),
(37.59,"Doosra: *board of directors*"),(38.93,"Maan lo *paanch log* board mein chune gaye"),(40.55,"jinhe shareholders ne chuna"),(41.73,"Inka khud ka paisa lagna"),(42.94,"*zaroori nahi* hai"),(43.60,"Inka kaam hai *bade faisle* lena"),(44.96,"naya loan lena ya nahi lena"),(46.16,"company kis direction mein jayegi"),(47.32,"aur sabse zaroori kaam"),(48.18,"*CEO kaun rahega*"),(49.30,"Aur jo CEO rakh sakte hain"),(50.48,"wo CEO *hata bhi sakte hain*"),
(51.54,"Teesra role hota hai *CEO* ka"),(53.04,"ise board ne rakha"),(53.98,"Iska kaam: *roz ka kaam*"),(55.36,"staff, sales, maal"),(56.56,"aur sab kuch sambhalna"),(57.46,"*Bade faisle nahi*"),(58.32,"wo board ka kaam hai"),
(59.22,"Ramesh yahan *CEO bhi* hai"),(60.44,"par wo CEO *kyun* hai?"),(61.66,"Kyunki *board ne rakha*"),(62.60,"Yaad rakho"),(63.20,"malik *board* ko chunta hai"),(64.22,"board *CEO* ko chunta hai"),(65.34,"*upar se neeche* cheezein chalti hain"),
(66.62,"Aur Nvidia mein Jensen Huang ke paas"),(68.32,"*3.5% share* the"),(69.72,"unke saath aise hi hua"),(70.62,"Ek din board ne bola"),(71.72,"Ramesh, *kal se mat aana*"),(72.96,"*kursi khaali*"),
(73.64,"But abhi bhi Ramesh ke paas"),(74.66,"uske *3% share* to hain"),(76.12,"To agar aapne kuch naya seekha hai"),(77.24,"to video ko *like* kar do"),(78.04,"aur *follow* kar lo")]
import json,re
caps=[[t,re.sub(r"\*(.+?)\*",r"<b>\1</b>",s)] for t,s in CAPS]
CSS=f'''*{{box-sizing:border-box;margin:0;padding:0}}html,body{{width:1080px;height:1920px;overflow:hidden;background:{G};font-family:Inter,sans-serif;color:{T}}}
.scene{{position:absolute;left:0;top:0;width:1080px;height:1920px;overflow:hidden;display:none}}
.scene div,.scene img{{position:absolute}} .scene svg{{display:block}}
.rings,.cam{{left:0;top:0;width:1080px;height:1920px;transform-origin:540px 980px}}
#cap{{position:absolute;left:60px;width:960px;top:1500px;text-align:center;z-index:50}}
#capi{{display:inline-block;background:{T};color:{CARD};font:800 44px/1.2 Inter;border-radius:22px;padding:16px 30px;box-shadow:0 0 0 4px {CARD}}}
#capi b{{color:#F0A89F}}
#flash{{position:absolute;inset:0;background:{CARD};opacity:0;z-index:60;pointer-events:none}}
'''
JS='''const E={},fx=[];const cl=x=>Math.max(0,Math.min(1,x));const eo=x=>1-Math.pow(1-x,3);
const ease={out3:eo,lin:x=>x,in3:x=>x*x*x,io:x=>x<.5?2*x*x:1-Math.pow(-2*x+2,2)/2,exp:x=>x>=1?1:1-Math.pow(2,-10*x),back:x=>{const c=1.9,c3=c+1;return 1+c3*Math.pow(x-1,3)+c*Math.pow(x-1,2)}};
function tw(id,p,t0,d,f,to,e='out3'){((E[id]??={})[p]??=[]).push([t0,d,f,to,e]);}
function hid(id){tw(id,'o',-1,.001,0,0);}
function pop(id,t,d=.3){tw(id,'o',t,Math.min(.1,d),0,1,'lin');tw(id,'s',t,d,.4,1,'back');}
function slam(id,t){tw(id,'o',t,.05,0,1,'lin');tw(id,'s',t,.22,2.2,1,'exp');}
function bob(id,t,d,hz,amp){fx.push(tt=>{if(tt>=t&&tt<=t+d){const e=document.getElementById(id);e.style.transform+=` translateY(${-Math.abs(Math.sin((tt-t)*Math.PI*hz))*amp}px)`;}});}
function txt(id,v){const e=document.getElementById(id);if(e.textContent!=String(v))e.textContent=v;}
function dash(id,fr){document.getElementById(id).setAttribute('stroke-dasharray',`${(fr*628.3).toFixed(1)} 628.3`);}
function val(l,t){let c=l[0][2];for(const [t0,d,f,to,e] of l){if(t<t0)break;c=f+(to-f)*ease[e](cl((t-t0)/d));}return c;}
const CUTS=[];const BASE={};
function init(){document.querySelectorAll('.scene').forEach(s=>CUTS.push([+s.dataset.a,+s.dataset.b,s]));
 for(const id in E){const e=document.getElementById(id);if(!e){console.error('missing',id);continue;}const m=(e.className||'').match&&(e.className.match(/rot(-?\\d+)/));BASE[id]=m?+m[1]:0;for(const p in E[id])E[id][p].sort((a,b)=>a[0]-b[0]);}
 document.querySelectorAll('[class*=rot]').forEach(e=>{if(!E[e.id]){const m=e.className.match(/rot(-?\\d+)/);e.style.transform=`rotate(${m[1]}deg)`;}});}
window.FACE={};
function seek(t){for(const [a,b,s] of CUTS){s.style.display=(t>=a&&t<b)?'block':'none';}
 for(const id in E){const e=document.getElementById(id);if(!e)continue;const w=E[id];const g=(p,d)=>w[p]?val(w[p],t):d;
  const x=g('x',0),y=g('y',0),s=g('s',1),sx=g('sx',1),sy=g('sy',1),r=g('r',0)+BASE[id];
  e.style.transform=`translate(${x.toFixed(2)}px,${y.toFixed(2)}px) rotate(${r.toFixed(2)}deg) scale(${(s*sx).toFixed(4)},${(s*sy).toFixed(4)})`;
  if(w.o)e.style.opacity=val(w.o,t).toFixed(3);if(w.blur){const b=val(w.blur,t);e.style.filter=b>0.05?`blur(${b.toFixed(1)}px)`:'none';}}
 for(const f of fx)f(t);
 let c='';for(const [ct,s] of CAPS){if(t>=ct)c=s;else break;}const ci=document.getElementById('capi');if(ci.innerHTML!==c)ci.innerHTML=c;
 let lt=0;for(const [ct] of CAPS){if(t>=ct)lt=ct;}const cp=cl((t-lt)/.14);ci.style.transform=`scale(${(.86+.14*ease.back(cp)).toFixed(3)})`;ci.style.opacity=t<CAPS[0][0]?0:1;
 for(const k in window.FACE){const F=window.FACE[k];const im=document.querySelector(`.facevid[data-seg=${k}]`);const n=Math.max(0,Math.min(F.n-1,Math.round((t-F.t0)*25)));if(t>=F.t0-0.05&&t<F.t1+0.05){im.style.display='block';im.nextElementSibling.style.display='none';const src=F.dir+String(F.f0+n+1).padStart(4,'0')+'.jpg';if(im.dataset.s!==src){im.dataset.s=src;im.src=src;}}}
 const fl=document.getElementById('flash');const ft=[70.56,73.50];let fo=0;for(const q of ft){if(t>=q&&t<q+.16)fo=Math.max(fo,.55*(1-(t-q)/.16));}fl.style.opacity=fo;
}
'''
html=f'<!doctype html><meta charset="utf-8"><style>{CSS}</style><body>{"".join(H)}<div id="cap"><span id="capi"></span></div><div id="flash"></div><script>const CAPS={json.dumps(caps)};{JS}{"".join(J)}init();seek(0);</script></body>'
open("reel.html","w").write(html); print("ok",len(html))
