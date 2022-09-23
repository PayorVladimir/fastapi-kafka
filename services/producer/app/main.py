from aiokafka import AIOKafkaProducer
from app.api import producer
from app.core import dependencies
from app.core.config import config
from fastapi import FastAPI

app = FastAPI(title=config.PROJECT_NAME)


@app.on_event("startup")
async def on_startup():
    kafka_producer = AIOKafkaProducer(
        bootstrap_servers=f"{config.KAFKA_URL}:{config.KAFKA_PORT}",
        client_id=config.PROJECT_NAME,
    )
    dependencies.kafka = kafka_producer
    await dependencies.kafka.start()


@app.on_event("shutdown")
async def on_shutdown():
    await dependencies.kafka.stop()


app.include_router(producer.router, prefix="/api", tags=["movies_ugc"])
