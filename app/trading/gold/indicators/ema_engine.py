class EMAEngine:
    def ema(self,prices,period=200):
        if len(prices)<period: return None
        k=2/(period+1)
        value=sum(prices[:period])/period
        for price in prices[period:]: value=price*k+value*(1-k)
        return value
ema_engine=EMAEngine()
