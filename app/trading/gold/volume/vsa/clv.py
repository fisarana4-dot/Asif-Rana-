def clv(d): return (d["close"]-d["low"])/(d["high"]-d["low"]) if d["high"]!=d["low"] else 0
