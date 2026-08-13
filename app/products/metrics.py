import json
from app.autonomy.research.providers import ask
def metrics(product):
 r=ask("JSON metrics 0-100: "+product)
 return r["text"]
def parse(text):
 a=text.find("{"); b=text.rfind("}")
 return json.loads(text[a:b+1])
def safe(text):
 try:return parse(text)
 except:return {"demand":50,"margin":50,"competition":50,"risk":50}
def business(m):
 return {k:m[k] for k in ("demand","margin","competition","risk")} if all(k in m for k in ("demand","margin","competition","risk")) else None
