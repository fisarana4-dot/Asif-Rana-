def regime_score(d):
 return d.get("trend",0)-d.get("range",0)-d.get("volatility_risk",0)
