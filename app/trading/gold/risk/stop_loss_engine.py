class StopLossEngine:
    def calculate(self,entry,sl): return abs(entry-sl)
    def atr_sl(self,atr,mult=1.5): return atr*mult
    def swing_sl(self,entry,swing,buf=0.5): return abs(entry-swing)-buf
    def candle_sl(self,entry,direction,d): return entry-d["low"] if direction=="BUY" else d["high"]-entry
    def sl_price(self,entry,direction,risk): return entry-risk if direction=="BUY" else entry+risk
stop_loss_engine=StopLossEngine()
