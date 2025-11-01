from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str
    secret_key: str
    debug: bool = False
    # Access token lifetime in minutes
    access_token_expire_minutes: int = 15
    # Refresh token lifetime in days
    refresh_token_expire_days: int = 7

    class Config:
        env_file = ".env"


settings = Settings()