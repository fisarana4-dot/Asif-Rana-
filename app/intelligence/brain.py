from app.providers.registry.provider_registry import ProviderRegistry
from app.core.ai_fusion.router.ai_router import AIRouter
from app.intelligence.providers.gemini import GeminiProvider
class NexraBrain:
    router = AIRouter()
    registry = ProviderRegistry
    providers = ProviderRegistry.providers
    def status(self): return {"status":"READY","providers":self.registry.providers}
    def ask(self, text): return {"provider":"gemini","request":text}
    def gemini(self, text): return self.router.route('reasoning', text).get('r')
    def intent(self, text): return self.gemini("Classify intent: "+text)
    def decide(self, text): return {"intent":self.intent(text),"action":"RESEARCH"}
    def route(self, text): return {"action":"RESEARCH","provider":"gemini"}
    def providers_list(self): return self.registry.providers
    def add_provider(self, name): self.registry.providers.append(name)
    def capability(self, name): return self.registry.capabilities[name]
    def best(self, need): return next((p for p in self.registry.providers if self.capability(p)==need),None)
    def fallback(self, need): return [p for p in self.registry.providers if self.capability(p)==need]
    def available(self, name): return name in self.registry.providers
    def provider_info(self, name): return {"name":name,"available":self.available(name),"capability":self.capability(name)}
    def select(self, need): return self.best(need)
    def execute(self, text, need="reasoning"): r=self.router.route(need,text); return {"provider":r.get("p"),"response":r.get("r",r),"status":r.get("s")}
    def ask_gemini(self, text): return self.router.route('reasoning', text).get('r')
