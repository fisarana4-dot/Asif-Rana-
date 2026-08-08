import redis.asyncio as redis
from app.core.config import settings

redis_client = redis.from_url(settings.REDIS_URL, decode_responses=True)

async def get_redis():
    return redis_client

async def redis_health_check():
    try:
        await redis_client.ping()
        return True
    except Exception:
        return False
