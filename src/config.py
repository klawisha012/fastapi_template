# src/config.py

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import PostgresDsn
class Database(BaseSettings):
    DB_USER: str
    DB_HOST: str
    DB_PORT: str
    DB_NAME: str
    DB_PASS: str

    @property
    def ALEMBIC_DATABASE_URL(self) -> str:
        return (
            f"postgresql://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )
    
    @property
    def DATABASE_URL(self) -> str:
        return (
            f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )

    class Config:
        env_file = ".env.example"


database_settings = Database()
