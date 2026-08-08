from app.cache.redis_client import r
def ping(): return r.ping()
