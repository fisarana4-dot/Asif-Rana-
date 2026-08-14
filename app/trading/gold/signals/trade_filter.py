class TradeFilter:
    def evaluate(self,d): return "WAIT" if d.get("loss_streak",0)>=2 or d.get("inducement",False) or d.get("spread_risk",False) or d.get("slippage_risk",False) or d.get("volatility_risk",False) or d.get("friday_close",False) or d.get("news",False) or d.get("black_swan",False) or d.get("war",False) else "PASS"
trade_filter=TradeFilter()
