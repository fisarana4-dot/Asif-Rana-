
import csv
f="data/gold/full/xauusd-m15-bid-2026-01-01-2026-08-08.csv"
rows=list(csv.DictReader(open(f)))
c=[float(x["close"]) for x in rows]
h=[float(x["high"]) for x in rows]
l=[float(x["low"]) for x in rows]
v=[float(x["volume"]) for x in rows]; print("DATA",len(c))

def ema(a,n):
 k=2/(n+1); e=a[0]; r=[]
 for x in a:r.append(e:=x*k+e*(1-k))
 return r

e50=ema(c,50)
e200=ema(c,200)
print("EMA",round(e50[-1],2),round(e200[-1],2))
def rsi14(i):
 g=d=0
 for j in range(i-13,i+1):
  ch=c[j]-c[j-1]
  g+=max(ch,0); d+=max(-ch,0)
 return 100 if d==0 else 100-100/(1+(g/d))

def vwma20(i):
 sv=sum(v[i-19:i+1])
 return sum(c[j]*v[j] for
j in range(i-19,i+1))/sv if sv else c[i]

def atr14(i):
 return sum(max(h[j]-l[j],abs(h[j]-c[j-1]),abs(l[j]-c[j-1])) for j in range(i-13,i+1))/14

i=len(c)-1
rsi=rsi14(i)
vw=vwma20(i)
at=atr14(i)
print("RSI",round(rsi,2),"VWMA",round(vw,3),"ATR",round(at,3))

trades=[]
pos=None
entry=sl=0
wins=losses=0
R=0

for i in range(200,len(c)):
 r=rsi14(i); vw=vwma20(i); a=atr14(i)
 buy=(e50[i]>e200[i])+(r>50)+(c[i]>vw)
 sell=(e50[i]<e200[i])+(r<50)+(c[i]<vw)
 sig="
BUY" if buy>=2 else "SELL" if sell>=2 else "NO_TRADE"
 if pos is None and sig!="NO_TRADE":
  pos=sig; entry=c[i]; sl=entry-a*1.5
  sl=entry-a*1.5 if pos=="BUY" else entry+a*1.5
 elif pos=="BUY" and l[
