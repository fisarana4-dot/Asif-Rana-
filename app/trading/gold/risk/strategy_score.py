def strategy_score(d):
 s=0
 s+=d.get("mtf",0)+d.get("vsa",0)+d.get("candle",0)
 return s
