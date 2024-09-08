from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_title: str
    database_url: str

    class Config:
        env_file = '.env'
        extra = 'ignore'


settings = Settings()
