class ATREngine:
    def value(self,high,low,close,period=14):
        if len(close)<=period: return None
        tr=[]
        for i in range(1,len(close)): tr.append(max(high[i]-low[i],abs(high[i]-close[i-1]),abs(low[i]-close[i-1])))
        atr=sum(tr[:period])/period
        for x in tr[period:]: atr=(atr*(period-1)+x)/period
        return atr
atr_engine=ATREngine()
