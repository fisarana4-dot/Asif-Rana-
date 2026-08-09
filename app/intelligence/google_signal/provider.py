import os
class GoogleDataProvider:
    def key(self): return os.getenv("GOOGLE_MAPS_API_KEY")
