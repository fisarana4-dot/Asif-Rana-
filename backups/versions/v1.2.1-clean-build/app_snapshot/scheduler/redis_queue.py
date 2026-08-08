from app.cache.redis_client import r
QUEUE = "priority_jobs"
def push(job):
    r.lpush(QUEUE, job)
def pop():
    return r.rpop(QUEUE)
from app.cache.redis_client import r
