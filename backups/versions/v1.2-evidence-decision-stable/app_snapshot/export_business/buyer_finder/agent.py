
class BuyerFinderAgent:
    def __init__(self):
        self.name = "Buyer Agent"

    def score_buyer(self, buyer):
        score = 0
        if buyer.get("country"):
            score += 20
        
