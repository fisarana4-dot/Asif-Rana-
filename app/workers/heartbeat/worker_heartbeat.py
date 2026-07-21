import time
HEARTBEATS={}
def beat(worker):
    HEARTBEATS[worker]=time.time()
def last(worker): return HEARTBEATS.get(worker)
