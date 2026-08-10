def clv(d): return (d["Close"]-d["Low"])/(d["High"]-d["Low"]) if d["High"]!=d["Low"] else 0
