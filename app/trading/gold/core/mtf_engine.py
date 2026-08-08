TIMEFRAMES=("D1","H4","H1","M15","M5","M1")
class MTFEngine:
    def bias(self,d): return {tf:d.get(tf,"UNKNOWN") for tf in TIMEFRAMES}
mtf_engine=MTFEngine()
