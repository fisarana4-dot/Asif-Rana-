class TradeManager:
 def manage(self,d):
  e=d["entry"];r=abs(e-d["sl"]);p=d["price"]
  return {"sl":e} if abs(p-e)>=r else d
 def trail(self,d): return d["price"]-d["atr"] if d["price"]>d["entry"] else d["sl"] if d["direction"]=="BUY" else (d["price"]+d["atr"] if d["price"]<d["entry"] else d["sl"])
trade_manager=TradeManager()
