def clv(d):
    h,l,c=d["high"],d["low"],d["close"]
    return ((c-l)-(h-c))/(h-l) if h!=l else 0.0
