class ProviderRegistry: pass
provider_registry = ProviderRegistry()
ProviderRegistry.providers = ["gemini"]
ProviderRegistry.capabilities = {"gemini":"reasoning","openai":"general"}
