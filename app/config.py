from pydantic import PostgresDsn, RedisDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    ASYNCPG_URL: PostgresDsn
    REDIS_URL: RedisDsn
    JWT_ALGORITHM: str
    JWT_EXPIRE: str


settings = Settings()
