import numpy as np, wave
from scipy.signal import butter, sosfilt
SR=48000; DUR=78.66; N=int(SR*DUR); BPM=105.0; PH=0.055; E=60/BPM/2
rng=np.random.default_rng(3)
tr={k:np.zeros(N+SR*2) for k in ("kick","snare","hat","bass","lead","stab","fx")}
def add(name,t,sig,g=1.0):
    i=int(t*SR)
    if i<0: sig=sig[-i:]; i=0
    if i>=N: return
    tr[name][i:i+len(sig)]+=sig*g
def env(n,a=0.003,d=8.0):
    t=np.arange(n)/SR; return np.minimum(1,t/a)*np.exp(-t*d)
def kick():
    n=int(.32*SR); t=np.arange(n)/SR; f=48+110*np.exp(-t*34); ph=2*np.pi*np.cumsum(f)/SR
    return np.sin(ph)*np.exp(-t*10)+0.25*rng.standard_normal(n)*np.exp(-t*220)
def snare():
    n=int(.22*SR); t=np.arange(n)/SR; nz=sosfilt(butter(2,[900,7000],'bp',fs=SR,output='sos'),rng.standard_normal(n))
    return 0.9*nz*np.exp(-t*24)+0.5*np.sin(2*np.pi*185*t)*np.exp(-t*34)
def hat(op=False):
    n=int((.16 if op else .05)*SR); t=np.arange(n)/SR; nz=sosfilt(butter(2,6500,'hp',fs=SR,output='sos'),rng.standard_normal(n))
    return nz*np.exp(-t*(22 if op else 95))
def pluck(f,dur=.26,bright=1.0):
    n=int(dur*SR); t=np.arange(n)/SR; s=np.zeros(n)
    for k in (1,2,3,4,5,7):
        s+=np.sin(2*np.pi*k*f*t)/(k**1.15)*np.exp(-t*(7+3.2*k/bright))
    return (s+0.12*rng.standard_normal(n)*np.exp(-t*400))*np.minimum(1,t/0.002)*np.minimum(1,(dur-t)/0.02)
def bass(f,dur=.24):
    n=int(dur*SR); t=np.arange(n)/SR
    s=np.sin(2*np.pi*f*t)+0.45*np.sin(4*np.pi*f*t)+0.2*np.sin(6*np.pi*f*t)
    return np.tanh(1.4*s)*np.minimum(1,t/0.004)*np.exp(-t*3.5)*np.minimum(1,(dur-t)/0.03)
def stab(fs,dur=.14):
    n=int(dur*SR); t=np.arange(n)/SR; s=sum(np.sin(2*np.pi*f*t)+0.3*np.sin(4*np.pi*f*t) for f in fs)
    return s/len(fs)*np.minimum(1,t/0.003)*np.exp(-t*16)
def glide(f0,f1,dur):
    n=int(dur*SR); t=np.arange(n)/SR; f=f0+(f1-f0)*(t/dur)**1.5; ph=2*np.pi*np.cumsum(f)/SR
    s=sum(np.sin(k*ph)/k for k in (1,2,3,4,5,6)); wah=0.6+0.4*np.sin(2*np.pi*5.5*t)
    return s*wah*np.minimum(1,t/0.03)*np.minimum(1,(dur-t)/0.08)
m=lambda n:440*2**((n-69)/12)
# original 2-bar riff in D minor (8th-note steps; 0 = rest), midi notes
RA=[74,0,77,74, 69,0,74,0, 77,76,74,0, 72,0,69,0,   70,0,74,70, 67,0,70,0, 69,73,76,0, 69,0,0,0]
RB=[74,77,0,81, 79,0,77,0, 76,0,74,72, 74,0,0,69,   70,74,0,77, 76,0,74,0, 73,0,76,73, 69,0,0,0]
BS=[38,0,0,38, 0,0,38,0, 38,0,0,41, 0,0,36,0,   34,0,0,34, 0,0,34,0, 33,0,0,33, 0,37,33,0]
CH=[[62,65,69],[62,65,69],[58,62,65],[57,61,64]]   # Dm Dm Bb A per half-bar pairs (2 bars -> 4 slots of 8 steps... index by step//8)
def sec(t):
    if t<5.80: return "hook"
    if t<10.07: return "face"
    if t<21.76: return "story"
    if t<23.86: return "break"
    if t<37.55: return "sh"
    if t<51.50: return "bd"
    if t<59.16: return "ceo"
    if t<66.60: return "face"
    if t<70.56: return "jen"
    if t<73.50: return "stop"
    if t<76.05: return "back"
    return "out"
K=int((DUR-PH)/E)+1
for k in range(K):
    t=PH+k*E; s=sec(t); st=k%16; sb=k%32; sw=0.035 if k%2 else 0   # swing offbeats
    tt=t+sw
    if s=="stop": continue
    drums = s not in ("break",)
    if drums:
        if st in (0,3,8,11) or (st==14 and s in("sh","bd","back","hook")): add("kick",tt,kick(),1.0 if st in(0,8) else .8)
        if st in (4,12): add("snare",tt,snare(),.9 if s not in("face","ceo") else .55)
        add("hat",tt,hat(op=(st==15 and s!="face")),.5 if k%2==0 else .32)
    else:
        if st%4==0: add("kick",tt,kick(),.9)
    if BS[sb]: add("bass",tt,bass(m(BS[sb])),.9 if s!="ceo" else .7)
    riff=RB if s in("bd","back","out") else RA
    if s in("hook","story","sh","bd","ceo","jen","back","out") and riff[sb]:
        n=riff[sb]+(12 if s=="ceo" else 0)
        add("lead",tt,pluck(m(n),bright=0.6 if s=="jen" else 1.0),.8 if s!="story" else .65)
    if s in("bd","sh","back","hook","out") and st in (2,6,10,14) and s!="sh" or (s=="sh" and st in (6,14)):
        add("stab",tt,stab([m(x+12) for x in CH[(sb//8)%4]]),.5)
# break hits on tier pops, punch hit, sad wah-wah, final stab
for t0 in (22.66,22.90,23.14): add("kick",t0,kick(),1.0); add("stab",t0,stab([m(74),m(77),m(81)]),.6)
add("kick",70.56,kick(),1.2)
add("fx",72.50,glide(m(58),m(55),.42),.5); add("fx",72.96,glide(m(55),m(49),.62),.5)
add("stab",78.14,stab([m(62),m(69),m(74),m(77)],.5),.9); add("kick",78.14,kick(),1.0)
# riser into punch
n=int(1.2*SR); t=np.arange(n)/SR; add("fx",69.36,sosfilt(butter(2,[600,5000],'bp',fs=SR,output='sos'),rng.standard_normal(n))*(t/1.2)**2.5,.35)
g=dict(kick=.9,snare=.5,hat=.22,bass=.55,lead=.42,stab=.28,fx=.5)
mix=sum(tr[k][:N]*g[k] for k in tr)
# jensen section lowpass (tension)
a,b=int(66.60*SR),int(70.56*SR); mix[a:b]=sosfilt(butter(2,1400,'lp',fs=SR,output='sos'),mix[a:b])
mix=np.tanh(mix*1.1); mix=mix/np.abs(mix).max()*0.7
# short tail fade
f=int(.25*SR); mix[-f:]*=np.linspace(1,0,f)
st=np.stack([mix,mix],1); w=wave.open("bgm_original_105bpm.wav","wb"); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((st*32767).astype(np.int16).tobytes()); w.close()
print("bgm ok",len(mix)/SR)
# --- SFX
def save(name,x):
    x=x/np.abs(x).max()*0.8; w=wave.open(name,"wb"); w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes((x*32767).astype(np.int16).tobytes()); w.close()
def T(d): return np.arange(int(d*SR))/SR
t=T(.18); save("sfx_pop.wav",np.sin(2*np.pi*np.cumsum(440+440*np.exp(-t*40))/SR)*np.exp(-t*28))
t=T(.16); save("sfx_pop_hi.wav",np.sin(2*np.pi*np.cumsum(700+600*np.exp(-t*45))/SR)*np.exp(-t*30))
t=T(.05); save("sfx_click.wav",0.7*np.sin(2*np.pi*2200*t)*np.exp(-t*300)+0.3*rng.standard_normal(len(t))*np.exp(-t*600))
t=T(.9); save("sfx_chime.wav",(np.sin(2*np.pi*1046.5*t)+0.5*np.sin(2*np.pi*1568*t)+0.2*np.sin(2*np.pi*2093*t))*np.exp(-t*5)*np.minimum(1,t/.005))
t=T(.55); save("sfx_whoosh.wav",sosfilt(butter(2,[300,2600],'bp',fs=SR,output='sos'),rng.standard_normal(len(t)))*np.sin(np.pi*t/.55)**2)
t=T(.5); save("sfx_hit.wav",np.sin(2*np.pi*np.cumsum(110+260*np.exp(-t*30))/SR)*np.exp(-t*10)+0.5*sosfilt(butter(2,[350,3000],'bp',fs=SR,output='sos'),rng.standard_normal(len(t)))*np.exp(-t*35))
def roll(d,rate0,rate1,f=1500):
    x=np.zeros(int(d*SR)); tt=0.0
    while tt<d-0.05:
        c=T(.03); s=np.sin(2*np.pi*f*(1+0.3*tt/d)*c)*np.exp(-c*260); i=int(tt*SR); x[i:i+len(s)]+=s
        tt+=1/(rate0+(rate1-rate0)*tt/d)
    return x
save("sfx_tickroll.wav",roll(2.0,14,30)); save("sfx_coins.wav",roll(0.95,12,14,2400))
x=np.zeros(int(1.0*SR))
for i in range(5):
    t=T(.14); s=np.sin(2*np.pi*np.cumsum(520+60*i+420*np.exp(-t*40))/SR)*np.exp(-t*30); j=int(i*.2*SR); x[j:j+len(s)]+=s
save("sfx_5pops.wav",x)
x=np.zeros(int(1.3*SR))
for i,tt in enumerate((0,.31,.62,.93)):
    t=T(.12); s=np.sin(2*np.pi*np.cumsum(1500-500*np.exp(-t*60)+0*t)/SR)*np.exp(-t*38); j=int(tt*SR); x[j:j+len(s)]+=s
save("sfx_drips.wav",x); print("sfx ok")
