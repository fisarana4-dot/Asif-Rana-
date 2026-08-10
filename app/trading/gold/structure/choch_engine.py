class CHoCHEngine:
    def detect(self,d): return "CHoCH_UP" if d.get("Close",0)>d.get("swing_high",0) else "CHoCH_DOWN" if d.get("Close",0)<d.get("swing_low",0) else ""
choch_engine=CHoCHEngine()
