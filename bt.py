import csv
rows=list(csv.DictReader(open("data/gold/xauusd-m15-bid-2026-01-01-2026-01-31.csv")))





print("ROWS:",len(rows))
closes=[float(x["close"]) for x in rows]
print("CLOSES:",len(closes))
ema=[]; k=2/51; e=closes[0]
[ema.append((e:=closes[i]*k+e*(1-k))) for i in range(len(closes))]; print("EMA:",len(ema),round(ema[-1],2))
ema200=[]; k2=2/201; e2=closes[0]
[ema200.append((e2:=closes[i]*k2+e2*(1-k2))) for i in range(len(closes))]; print("EMA200:",len(ema200),round(ema200[-1],2))
