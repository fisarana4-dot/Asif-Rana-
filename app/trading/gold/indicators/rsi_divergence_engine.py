class RSIDivergenceEngine:
    def detect(self,prices,rsi):
        if len(prices)<2 or len(rsi)<2: return []
        if prices[-1]<prices[-2] and rsi[-1]>rsi[-2]: return [{"type":"BULLISH_DIVERGENCE"}]
        if prices[-1]>prices[-2] and rsi[-1]<rsi[-2]: return [{"type":"BEARISH_DIVERGENCE"}]
        return []
rsi_divergence_engine=RSIDivergenceEngine()
