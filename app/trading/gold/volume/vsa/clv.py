def clv(d):
    h,l,c=d["High"],d["Low"],d["Close"]
    return ((c-l)-(h-c))/(h-l) if h!=l else 0.0
