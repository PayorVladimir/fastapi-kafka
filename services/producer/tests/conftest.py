import pytest
from aiokafka import AIOKafkaConsumer
from app.core.config import config
from app.main import app
from asgi_lifespan import LifespanManager
from httpx import AsyncClient


@pytest.fixture
async def test_app():
    async with AsyncClient(app=app, base_url="http://test") as client, LifespanManager(
        app
    ):
        yield client


@pytest.fixture
async def kafka():
    kafka_consumer = AIOKafkaConsumer(
        "test",
        client_id="test",
        bootstrap_servers=f"{config.KAFKA_URL}:{config.KAFKA_PORT}",
        enable_auto_commit=False,
    )
    await kafka_consumer.start()
    yield kafka_consumer
    await kafka_consumer.stop()
