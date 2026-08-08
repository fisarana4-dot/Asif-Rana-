import time
from app.workers.engine.redis_worker import process
from app.workers.heartbeat.worker_heartbeat import beat
RUNNING=True
def start():
    while RUNNING:
        process()
        beat('worker-1')
