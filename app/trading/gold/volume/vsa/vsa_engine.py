class VSAEngine:
    def analyze(self,d): return ["BULL"] if d.get("clv",0)>=.7 else ["BEAR"] if d.get("clv",0)<=.3 else []
    def no_demand(self,d): return []
    def no_supply(self,d): return []
    def stopping_volume(self,d): return []
    def climactic_volume(self,d): return []
    def volume_confirmation(self,d): return []
    def volume_divergence(self,d): return []
    def effort_result(self,d): return []
    def upthrust(self,d): return []
    def volume_confirmation(self,d): return []
vsa_engine=VSAEngine()
