from app.cache.redis_client import r
QUEUE="priority_jobs"
def get_job():
    result=r.brpop(QUEUE,timeout=5)
    return result[1] if result else None
def wait_job():
    return get_job()
