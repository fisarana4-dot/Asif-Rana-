def run(chain,call):
    for p in chain:
        try: return p,call(p)
        except Exception: continue
