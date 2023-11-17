import redis.asyncio as redis
from app.config import settings as global_settings


async def get_redis():
    return await redis.from_url(
        global_settings.REDIS_URL.unicode_string(),
        encoding="utf-8",
        decode_responses=True,
    )
