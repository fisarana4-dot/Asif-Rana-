class TrendLineEngine:
    def detect(self,prices):
        if len(prices)<2: return []
        x1,x2=0,len(prices)-1;y1,y2=prices[0],prices[-1]
        slope=(y2-y1)/(x2-x1)
        return [{"type":"UPTREND" if slope>0 else "DOWNTREND" if slope<0 else "FLAT","slope":slope,"start":y1,"end":y2}]
trendline_engine=TrendLineEngine()
