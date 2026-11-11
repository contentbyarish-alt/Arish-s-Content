import re,sys
SRC=sys.argv[1]
chat=open(SRC+'/hivon-whatsapp-chat.svg').read()
db=open(SRC+'/hivon-erp-dashboard.svg').read()
def txt(s,old,new,n=1):
    assert old in s, old
    return s.replace(old,new,n)
def nth(s,pat,new,k):
    ms=list(re.finditer(pat,s)); assert len(ms)>k,(pat,len(ms)); m=ms[k]
    return s[:m.start()]+new+s[m.end():]
I=r'Item: <tspan class="b">[^<]*</tspan>'
def chat_variant(title,l1,l2,q1,q2,r1,r2,done=None,fname=None,hide3=False):
    s=chat
    if not hide3: s=nth(s,r'>[^<>]*Item: <tspan class="b">[^<]*</tspan><',f'>@@ITEM3@@<',1)
    s=re.sub(r'>[^<>]*Inventory Stock Alert!<',f'>{title}<',s,count=1)
    s=nth(s,r'>[^<>]*Item: <tspan class="b">[^<]*</tspan><',f'>{l1}<',0)
    s=re.sub(r'>[^<>]*Available Stock: <tspan class="b">[^<]*</tspan><',f'>{l2}<',s,count=1)
    s=txt(s,'Would you like me to place a new',q1); s=txt(s,'>order?<',f'>{q2}<')
    s=txt(s,'Yes, please order 100 units',r1); s=txt(s,'from Ram Enterprises.',r2)
    if hide3: s=txt(s,'<g id="msg-3"','<g id="msg-3" display="none"'); s=txt(s,'<g id="typing"','<g id="typing" display="none"')
    else:
        t,a,b,c,d=done
        s=re.sub(r'>[^<>]*Purchase Order Created!<',f'>{t}<',s,count=1)
        s=txt(s,'@@ITEM3@@',a)
        s=re.sub(r'>[^<>]*Quantity: <tspan class="b">[^<]*</tspan><',f'>{b}<',s,count=1)
        s=re.sub(r'>[^<>]*Vendor: <tspan class="b">[^<]*</tspan><',f'>{c}<',s,count=1)
        s=re.sub(r'>[^<>]*Attachment: <tspan class="b">[^<]*</tspan><',f'>{d}<',s,count=1)
        s=txt(s,'>PO-101.pdf<',f'>{fname}<')
    return s
B=lambda k,v:f'{k}: <tspan class="b">{v}</tspan>'
V={
'chat_attendance':chat_variant('🕘 Please Mark Your Attendance',B('👤 Name','Worker 12'),B('🏭 Shift','A · Plant 1'),'Check-in karne ke liye reply','karein.','Check-in','09:01 · Plant 1',hide3=True),
'chat_inward':chat_variant('🚚 Material Inward',B('📦 Item','Steel Rod 12mm'),B('🏢 Vendor','Vendor A'),'Kitna maal andar aaya hai?','','500 kg aaya hai,','gate entry kar do.',('✅ Inward Entry Created!',B('📦 Item','Steel Rod 12mm'),B('🔢 Quantity','500 kg'),B('🏢 Vendor','Vendor A'),B('🔗 Attachment','GRN_101.pdf')),'GRN-101.pdf'),
'chat_production':chat_variant('⚙️ Production Update',B('🏭 Machine','M-4'),B('🕘 Shift','A'),'Aaj kitni production hui?','','Aaj 120 pcs bane,','Flange 40mm.',('✅ Production Logged!',B('📦 Item','Flange 40mm'),B('🔢 Quantity','120 pcs'),B('🏭 Machine','M-4 · Shift A'),B('🔗 Attachment','Daily_Report_M4.pdf')),'DPR-M4.pdf'),
}
for k,s in V.items(): open(k+'.svg','w').write(s)
d=db
for a,b in [('Real-time stats across employees, leads and production.','Real-time stats across employees, inventory and production.'),
 ('>Absent &amp; Checked-Out<','>Today Production<'),('style="fill:#E9A23B">26<','style="fill:#43946C">1,240<'),('>Absent + checked out<','>pcs · all machines<'),
 ('>On Leave<','>Inventory<'),('style="fill:#845EEE">6<','style="fill:#101729">312<'),('>Approved leave today<','>SKUs in stock<'),
 ('>Defaulters<','>Pending Inward<'),('style="fill:#DD524C">14<','style="fill:#E9A23B">3<'),('>No check-in recorded<','>Gate entries today<'),
 ('>Weekly Presence Trend<','>Weekly Production Trend<'),('>Historical presence (last 7 days, % of workforce)<','>Last 7 days, % of daily target<'),
 ('>Low stock: 3x3 Boxes<','>Low stock: Flange blanks<'),('>10 units left • 14:37<','>40 left • 09:58<'),
 ('>Payment due: INV001<','>Inward: Steel Rod 500 kg<'),('>₹50,000 • Ram Enterprises<','>GRN-101 • Vendor A • 10:15<'),
 ('>PO-101 created<','>Attendance: 94 present<'),('>Ram Enterprises • 100 units<','>Shift A • 09:30<'),
 ('>Attendance outside radius<','>Machine M-4: 120 pcs logged<'),('>Site B • 09:42<','>Shift A • Flange 40mm • 10:42<')]:
    d=txt(d,a,b)
open('dashboard_reel.svg','w').write(d)
for k in list(V)+['dashboard_reel']:
    s=open(k+'.svg').read(); open(k+'_static.svg','w').write(s.replace('<svg ','<svg class="static" ',1))
print('ok')
