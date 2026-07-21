import time
from app.workers.engine.redis_worker import process
RUNNING=True
def start():
    while RUNNING:
        process()
