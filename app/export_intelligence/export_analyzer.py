class ExportAnalyzer:
    def analyze(self,product,country): return {'product':product,'country':country}
    def market_score(self,demand,competition): return demand-competition
    def buyer_score(self,buyers,demand): return buyers*demand
export_engine=ExportAnalyzer()
