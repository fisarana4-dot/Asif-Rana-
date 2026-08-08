import time
from app.workers.engine.redis_worker import process
RUNNING=True
def start():
    while RUNNING:
        process()
from app.workers.heartbeat.worker_heartbeat import beat
        beat("worker-1")
