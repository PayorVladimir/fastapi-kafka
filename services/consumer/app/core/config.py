from pydantic import BaseSettings, Field


class Config(BaseSettings):
    PROJECT_NAME: str = Field('auth_service')


config = Config()
