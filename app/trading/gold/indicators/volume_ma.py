class VolumeMA:
    def value(self,volume,period=20):
        if len(volume)<period: return None
        return sum(volume[-period:])/period
volume_ma=VolumeMA()
