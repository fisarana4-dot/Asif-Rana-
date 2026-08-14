class CandlePatternEngine:
 def detect(self,d):
  o,h,l,c=d["open"],d["high"],d["low"],d["close"]
  p=d.get("prev",{});r=h-l;b=abs(c-o);x=[]
  if p and h<p.get("high",0) and l>p.get("low",0): x+=["INSIDE_BAR"]
  if r and (h-max(o,c)>2*b or min(o,c)-l>2*b): x+=["PIN_BAR"]
  return x or (["BULL"] if c>o else ["BEAR"])
candle_pattern_engine=CandlePatternEngine()
