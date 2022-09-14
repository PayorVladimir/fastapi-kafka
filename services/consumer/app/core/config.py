from pydantic import BaseSettings, Field


class Config(BaseSettings):
    PROJECT_NAME: str = Field()
    KAFKA_URL: str = Field()
    KAFKA_PORT: str = Field()


config = Config()
