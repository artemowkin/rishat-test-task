from pathlib import Path

from pydantic import BaseSettings


CONFIG_DIR = Path(__file__).resolve().parent.parent


class Config(BaseSettings):
    database_name: str
    database_user: str
    database_password: str
    database_host: str = '127.0.0.1'
    database_port: str = '5432'
    secret_key: str
    debug: bool = True
    stripe_key: str

    class Config:
        env_file = CONFIG_DIR / '.env'


config = Config()
