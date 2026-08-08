class EvidenceScore:
    def calculate(self,market,buyer,product,memory): return {'confidence':market+buyer+product+memory}
score_engine=EvidenceScore()
