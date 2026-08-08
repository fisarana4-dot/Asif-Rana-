class TradeDecision:
    def decide(self,d):
        if d.get("blocked"): return "NO_TRADE"
        return d.get("signal","NO_TRADE")
trade_decision=TradeDecision()
