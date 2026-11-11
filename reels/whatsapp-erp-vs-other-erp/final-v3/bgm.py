import numpy as np, wave
SR=48000; DUR=60.0; N=int(SR*DUR); t=np.arange(N)/SR; rng=np.random.default_rng(7)
beat=0.6; out=np.zeros(N)
def note(freq,start,dur,amp,kind="pluck"):
    i0=int(start*SR); n=int(dur*SR)
    if i0>=N: return
    n=min(n,N-i0); tt=np.arange(n)/SR
    if kind=="pluck": w=(np.sin(2*np.pi*freq*tt)+0.35*np.sin(2*np.pi*2*freq*tt)+0.12*np.sin(2*np.pi*3*freq*tt))*np.exp(-tt*6.5)*np.minimum(1,tt/0.004)
    elif kind=="pad": w=(np.sin(2*np.pi*freq*tt)+0.3*np.sin(2*np.pi*2.001*freq*tt))*np.minimum(1,tt/0.5)*np.minimum(1,(dur-tt)/0.5)
    elif kind=="bass": w=np.sin(2*np.pi*freq*tt)*np.exp(-tt*2.2)*np.minimum(1,tt/0.01)
    out[i0:i0+n]+=amp*w
def kick(start,amp):
    i0=int(start*SR); n=int(0.22*SR)
    if i0+n>=N: return
    tt=np.arange(n)/SR; out[i0:i0+n]+=amp*np.sin(2*np.pi*(48+70*np.exp(-tt*28))*tt)*np.exp(-tt*16)
def hat(start,amp):
    i0=int(start*SR); n=int(0.05*SR)
    if i0+n>=N: return
    x=rng.standard_normal(n); x=x-np.convolve(x,np.ones(6)/6,'same'); out[i0:i0+n]+=amp*x*np.exp(-np.arange(n)/SR*90)
F=lambda m:440*2**((m-69)/12)
A=[[57,60,64,67],[53,57,60,64],[48,52,55,59],[55,59,62,64]]   # Am7 F C G6  (problem)
B=[[48,52,55,59],[55,59,62,66],[57,60,64,67],[53,57,60,64]]   # Cmaj7 G Am7 Fmaj7 (solution)
bar=4*beat; nb=int(DUR/bar)+1
for b in range(nb):
    s=b*bar; prog=A if s<17.2 else B; ch=prog[b%4]
    for m in ch: note(F(m),s,bar+0.3,0.05,"pad")
    if s>=2.0: note(F(ch[0]-12),s,1.2,0.22,"bass"); note(F(ch[0]-12),s+2*beat,1.0,0.16,"bass")
    for k in range(8):
        st=s+k*beat/2
        if st<2.0 and k%2: continue
        m=ch[[0,2,1,3,2,3,1,2][k]]+12; note(F(m),st,0.5,0.085 if st>=17.2 else 0.065,"pluck")
    if s>=5.9:
        for k in (0,2): kick(s+k*beat,0.3)
    if s>=17.2:
        for k in range(4): hat(s+k*beat+beat/2,0.035)
k=np.ones(24)/24; out=np.convolve(out,k,'same')
env=np.minimum(1,t/0.8)*np.minimum(1,(DUR-0.25-t).clip(0)/2.0); out*=env
out=out/np.abs(out).max()*0.5
R=np.roll(out,int(0.011*SR)); st=np.stack([out,0.85*out+0.15*R],1)
w=wave.open('bgm_synth.wav','wb'); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((st*32767).astype(np.int16).tobytes()); w.close(); print('bgm ok')
