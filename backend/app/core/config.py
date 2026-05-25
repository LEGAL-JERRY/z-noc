
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql+asyncpg://znoc:znoc@postgres:5432/znoc"
    REDIS_URL: str = "redis://redis:6379"

settings = Settings()
