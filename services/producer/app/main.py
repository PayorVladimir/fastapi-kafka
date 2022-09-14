import asyncio

from aiokafka import AIOKafkaProducer
from app.core.config import config
from app.core.models.model import (KafkaMessage, ProducerMessage,
                                   ProducerResponse)
from fastapi import FastAPI

app = FastAPI(title=config.PROJECT_NAME)
event_loop = asyncio.get_event_loop()
kafka_producer = AIOKafkaProducer(
    loop=event_loop,
    bootstrap_servers=f"{config.KAFKA_URL}:{config.KAFKA_PORT}",
    client_id=config.PROJECT_NAME,
)


@app.on_event("startup")
async def on_startup():
    await kafka_producer.start()


@app.post("/producer/{topic}", response_model=ProducerResponse)
async def produce(topic: str, message: ProducerMessage):
    kafka_message = KafkaMessage(**message.dict())
    await kafka_producer.send(topic=topic, value=kafka_message.json().encode("utf-8"))
    response = ProducerResponse(**kafka_message.dict(), topic=topic)

    return response
