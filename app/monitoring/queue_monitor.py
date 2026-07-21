from app.scheduler.redis_queue import r,QUEUE
def size(): return r.llen(QUEUE)
