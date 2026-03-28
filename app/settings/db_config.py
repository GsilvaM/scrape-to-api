from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env', env_file_encoding='utf-8', extra='ignore'
    )

    DB_HOST: str = ''
    DB_PORT: str = ''
    DB_USER: str = ''
    DB_PASSWORD: str = ''
    DB_NAME: str = ''

    @property
    def database_url(self) -> str:

        return f'mysql+pymysql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'


settings = Settings()
