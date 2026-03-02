from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', extra='ignore')

    DB_HOST: str = 'localhost'
    DB_PORT: str = ''
    DB_USER: str = 'root'
    DB_PASSWORD: str = '1914'
    DB_NAME: str = 'books_db'

    @property
    def database_url(self) -> str:
        return f'mysql+pymysql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'


settings = Settings()
