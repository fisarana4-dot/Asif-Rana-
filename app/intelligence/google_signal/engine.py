class GoogleSignalEngine:
    def score(self,s): return sum(s.values())
    def classify(self,s): return "HIGH" if self.score(s)>=70 else "LOW"
    def opportunity(self,s): return min(100,self.score(s))
