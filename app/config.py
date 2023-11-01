import os

from pydantic import PostgresDsn, RedisDsn
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # asyncpg_url: PostgresDsn = os.getenv("SQL_URL")
    # redis_url: RedisDsn = os.getenv("REDIS_URL")
    # jwt_algorithm: str = os.getenv("JWT_ALGORITHM")
    # jwt_expire: int = os.getenv("JWT_EXPIRE")
    
    asyncpg_url: PostgresDsn = "postgresql+asyncpg://postgres:postgres@192.168.166.51:5432/fast_async_db"
    # redis_url: RedisDsn = os.getenv("REDIS_URL")
    # jwt_algorithm: str = os.getenv("JWT_ALGORITHM")
    # jwt_expire: int = os.getenv("JWT_EXPIRE")


settings = Settings()