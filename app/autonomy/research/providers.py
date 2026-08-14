from app.intelligence.providers.gemini import GeminiProvider
def ask(q): return {"provider":"gemini","text":GeminiProvider().ask(q),"query":q}
