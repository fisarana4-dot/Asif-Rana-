class GeminiProvider:
    def __init__(self): self.name="gemini"
    def ask(self,text):
        import subprocess,json
        k=open("/data/data/com.termux/files/home/.gemini_key").read().strip()
        u="https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent"
        h="x-goog-api-key: "+k
        d=json.dumps({"contents":[{"parts":[{"text":text}]}]})
        r=subprocess.run(["curl","-s","-H",h,"-H","Content-Type: application/json","-d",d,u],capture_output=True,text=True)
        j=json.loads(r.stdout);return j["candidates"][0]["content"]["parts"][0]["text"]
