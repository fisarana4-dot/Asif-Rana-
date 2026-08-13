from app.intelligence.providers.gemini import GeminiProvider
def call(name,text):
    if name=="gemini": return GeminiProvider().ask(text)
    raise RuntimeError("PROVIDER_NOT_CONNECTED")
