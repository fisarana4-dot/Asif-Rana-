import json
from app.scheduler.redis_queue import pop,push
from app.workers.retry.retry_manager import should_retry
from app.workers.retry.dead_letter_queue import add
from app.workers.retry.job_status import set_status

def process():
    job=pop()
    if not job: return None
    set_status(job,"RUNNING")
