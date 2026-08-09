class GoogleSignalEngine:
    def score(self,s): return sum(s.values())
    def classify(self,s): return "HIGH" if self.score(s)>=70 else "LOW"
