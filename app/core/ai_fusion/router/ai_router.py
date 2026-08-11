from app.intelligence.providers.gemini import GeminiProvider
from app.providers.registry.provider_registry import ProviderRegistry
class AIRouter:
 def __init__(self):self.g=GeminiProvider();self.registry=ProviderRegistry
 def route(self,n,t): return self.g.ask(t) if n=="reasoning" else {"s":"NOT_CONNECTED"} if n in self.registry.capabilities else {"s":"NO"}
