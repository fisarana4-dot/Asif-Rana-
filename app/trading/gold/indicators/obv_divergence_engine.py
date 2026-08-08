class OBVDivergenceEngine:
    def detect(self,prices,obv):
        if len(prices)<2 or len(obv)<2: return []
        if prices[-1]<prices[-2] and obv[-1]>obv[-2]: return [{"type":"BULLISH_OBV_DIVERGENCE","trend":"BULLISH"}]
        if prices[-1]>prices[-2] and obv[-1]<obv[-2]: return [{"type":"BEARISH_OBV_DIVERGENCE","trend":"BEARISH"}]
        return []
obv_divergence_engine=OBVDivergenceEngine()
