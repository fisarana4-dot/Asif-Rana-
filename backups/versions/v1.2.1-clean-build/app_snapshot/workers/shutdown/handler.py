import signal
RUNNING=True

def stop(sig,frame):
    global RUNNING
    RUNNING=False
