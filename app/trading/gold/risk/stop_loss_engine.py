class StopLossEngine:
    def calculate(self,entry,sl): return abs(entry-sl)
    def atr_sl(self,atr,mult=1.5): return atr*mult
    def swing_sl(self,entry,swing,buf=0.5): return abs(entry-swing)-buf
stop_loss_engine=StopLossEngine()
