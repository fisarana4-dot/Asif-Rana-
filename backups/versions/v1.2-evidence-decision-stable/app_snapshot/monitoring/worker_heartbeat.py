HEARTBEAT={}
def beat(worker): HEARTBEAT[worker]="ALIVE"
def status(worker): return HEARTBEAT.get(worker,"OFFLINE")
