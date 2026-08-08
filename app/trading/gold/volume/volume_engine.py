class VolumeEngine:
    def analyze(self,d): return [int(x['volume']) for x in d]
volume_engine=VolumeEngine()
