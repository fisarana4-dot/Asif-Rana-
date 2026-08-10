import httpx
def fetch(url): return httpx.get(url,timeout=10).text
