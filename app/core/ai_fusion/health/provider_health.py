PROVIDERS=["gemini","grok","deepseek","openai","claude","perplexity","copilot","meta"]
def status(name,available=False): return {"provider":name,"status":"AVAILABLE" if available else "UNAVAILABLE"}
import os
def available(name): return bool(os.getenv(name))
KEYS={"gemini":"GOOGLE_API_KEY","grok":"XAI_API_KEY","deepseek":"DEEPSEEK_API_KEY","openai":"OPENAI_API_KEY"}
def choose(order): return next((p for p in order if available(KEYS.get(p,""))),None)
def chain(): return ["grok","deepseek","openai","gemini"]
KEYS.update({"claude":"ANTHROPIC_API_KEY","perplexity":"PERPLEXITY_API_KEY","copilot":"COPILOT_API_KEY","meta":"META_API_KEY"})
