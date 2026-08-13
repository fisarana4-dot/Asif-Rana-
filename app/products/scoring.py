def score(demand,margin,competition,risk):
    return round((demand+margin+(100-competition)+(100-risk))/4,1)
