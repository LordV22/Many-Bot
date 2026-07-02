"""
🤖 Many Bot
Configuration Engine

Centraliza todas as configurações do sistema.

Nunca utilize:
    os.getenv()

Utilize sempre:

from app.core.settings import settings
"""

from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore",
    )

    # =====================================================
    # APP
    # =====================================================

    APP_NAME: str = "🤖 Many Bot"

    APP_ENV: str = "development"

    APP_VERSION: str = "1.0.0"

    DEBUG: bool = True

    HOST: str = "0.0.0.0"

    PORT: int = 8000

    TIMEZONE: str = "America/Sao_Paulo"

    LOG_LEVEL: str = "INFO"

    # =====================================================
    # SECURITY
    # =====================================================

    SECRET_KEY: str = Field(...)

    JWT_SECRET: str = Field(...)

    JWT_EXPIRE_MINUTES: int = 1440

    # =====================================================
    # DATABASE
    # =====================================================

    DATABASE_URL: str

    POSTGRES_HOST: str

    POSTGRES_PORT: int

    POSTGRES_DB: str

    POSTGRES_USER: str

    POSTGRES_PASSWORD: str

    # =====================================================
    # REDIS
    # =====================================================

    REDIS_URL: str

    REDIS_HOST: str

    REDIS_PORT: int

    REDIS_DB: int = 0

    REDIS_PASSWORD: str | None = None

    # =====================================================
    # CACHE
    # =====================================================

    CACHE_ENABLED: bool = True

    CACHE_TTL: int = 3600

    # =====================================================
    # FEATURES
    # =====================================================

    ENABLE_RATE_LIMIT: bool = True

    ENABLE_GHOST_ENGINE: bool = True

    ENABLE_RISK_ENGINE: bool = True

    ENABLE_AUDIT_LOG: bool = True

    ENABLE_AUTO_BACKUP: bool = True

    ENABLE_AUTO_RECOVERY: bool = True

    ENABLE_HEALTHCHECK: bool = True

    # =====================================================
    # LOG
    # =====================================================

    LOG_JSON: bool = True

    LOG_FILE: str = "logs/manybot.log"

    # =====================================================
    # DASHBOARD
    # =====================================================

    DASHBOARD_ENABLED: bool = True

    DASHBOARD_USERNAME: str = "admin"

    DASHBOARD_PASSWORD: str = "admin"

    # =====================================================
    # API
    # =====================================================

    API_PREFIX: str = "/api/v1"

    API_DOCS: bool = True

    # =====================================================
    # AI
    # =====================================================

    OPENAI_API_KEY: str | None = None

    GEMINI_API_KEY: str | None = None

    GROQ_API_KEY: str | None = None

    # =====================================================
    # WEATHER
    # =====================================================

    OPENWEATHER_API_KEY: str | None = None

    # =====================================================
    # WHATSAPP
    # =====================================================

    WHATSAPP_ENGINE: str = "baileys"

    SESSION_NAME: str = "manybot"

    AUTO_RECONNECT: bool = True

    HEARTBEAT_SECONDS: int = 30


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
