from .fetcher import fetch
from .verifier import trust
from .providers import ask
def run(url):
 t=fetch(url);return {"ai":ask(t),"trust":trust(t)}
from .memory import save
from .memory import save
