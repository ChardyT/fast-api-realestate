from pydantic import BaseSettings

from .enums import BestBetEnvironment


class AppSettings(BaseSettings):
    ENVIRONMENT: BestBetEnvironment



AppConfig = AppSettings()
