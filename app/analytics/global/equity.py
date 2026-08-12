REQUIRED=["ticker","country","exchange","price","eps","book_value","roe","pe","pb"]
META=["source","timestamp","currency"]
def valid(x): return x is not None and x != ""
def fresh(ts): return bool(ts)
import time
def age(ts): return int(time.time()-ts)
MAX_AGE=300
def live(ts): return age(ts)<=MAX_AGE
def ratio(p,x): return round(p/x,2) if x else None
def valuation_ok(e,b): return e>0 and b>0
def roe_ok(r): return isinstance(r,(int,float))
def usable(r): return roe_ok(r) and r==r
def sourced(s): return isinstance(s,str) and bool(s.strip())
def trusted(x): return all(x.get(k) is not None for k in REQUIRED) and sourced(x.get("source",""))
OPTIONAL=["market_cap","sector","dividend_yield"]
def rankable(x): return trusted(x) and numeric_ok(x) and timestamp_ok(x.get("timestamp")) and live(x.get("timestamp"))
def timestamp_ok(ts): return isinstance(ts,(int,float)) and ts>0
NUMERIC=["price","eps","book_value","roe","pe","pb"]
def numeric_ok(x): return all(isinstance(x.get(k),(int,float)) for k in NUMERIC)
def positive_valuation(x): return x.get("pe",0)>0 and x.get("pb",0)>0
def score(x): return round(x["roe"]/(x["pe"]*x["pb"]),2)
def score(x): return round(x["roe"]/(x["pe"]*x["pb"]),2)
def quality_score(x): return score(x) if positive_valuation(x) and usable(x["roe"]) else None
def quality_score(x): return score(x) if positive_valuation(x) and usable(x["roe"]) else None
