class VWMAEngine:
    def value(self,prices,volume,period=20):
        if len(prices)<period or len(volume)<period: return None
        p=prices[-period:];v=volume[-period:]
        return sum(x*y for x,y in zip(p,v))/sum(v) if sum(v) else None
vwma_engine=VWMAEngine()
