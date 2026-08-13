from app.autonomy.research.providers import ask

def research(product):
    return ask("Global product research: "+product)
from app.products.scoring import score

def opportunity(demand,margin,competition,risk):
    return score(demand,margin,competition,risk)
