class AmazonMVP:
    def analyze(self,p): return {"product":p,"status":"READY"}

    def score(self,p): return min(100,p.get("demand",0)+p.get("margin",0)-p.get("competition",0))
