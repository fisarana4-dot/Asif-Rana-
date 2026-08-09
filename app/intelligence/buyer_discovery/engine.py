class BuyerDiscovery: 
    def find(self,query): return {"query":query,"status":"READY"}

    def score(self,b): return min(100,b.get("relevance",0)+b.get("market",0)+b.get("activity",0))

    def grade(self,score): return "A" if score>=80 else "B" if score>=60 else "C"

    def evaluate(self,b): s=self.score(b); return {"score":s,"grade":self.grade(s)}

    def evaluate(self,b): s=self.score(b); return {"score":s,"grade":self.grade(s)}
