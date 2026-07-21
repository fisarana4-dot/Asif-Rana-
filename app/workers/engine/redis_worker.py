import json
from app.scheduler.redis_queue import pop,push
from app.workers.retry.retry_manager import should_retry
from app.workers.retry.dead_letter_queue import add
from app.workers.retry.job_status import set_status

def process():
    job=pop()
    if not job: return None
    set_status(job,"RUNNING")
    try:
        data=json.loads(job)
        set_status(job,"SUCCESS")
        return data
    except Exception:
        add(job)
        set_status(job,"FAILED")
        if should_retry(1):
            push(job)
        return None
