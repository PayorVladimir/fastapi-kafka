import asyncio
import json
import typing

from aiokafka import AIOKafkaConsumer
from app.core.config import config
from app.core.models.model import ConsumerResponse, WebSocketMessage
from fastapi import FastAPI
from starlette.endpoints import WebSocket, WebSocketEndpoint
from starlette.middleware.cors import CORSMiddleware

app = FastAPI(title=config.PROJECT_NAME)
app.add_middleware(CORSMiddleware, allow_origins=["*"])


@app.websocket_route("/consumer/{topic}")
class ConsumerTopicWebscoket(WebSocketEndpoint):
    async def consume(self, consumer: AIOKafkaConsumer) -> str:
        async for message in consumer:
            return message.value.decode()

    async def on_connect(self, websocket: WebSocket) -> None:
        topic = websocket.path_params["topic"]

        await websocket.accept()
        msg = "Connected!"
        await websocket.send_json(
            WebSocketMessage(type="message", data={"text": msg}).dict()
        )

        loop = asyncio.get_event_loop()

        self.kafka_consumer = AIOKafkaConsumer(
            topic,
            loop=loop,
            client_id=config.PROJECT_NAME,
            bootstrap_servers=f"{config.KAFKA_URL}:{config.KAFKA_PORT}",
            enable_auto_commit=False,
        )
        await self.kafka_consumer.start()

        self.consumer_task = asyncio.create_task(
            self.send_message_to_websocket(topic=topic, websocket=websocket)
        )
        await self.consumer_task

    async def on_receive(self, websocket: WebSocket, data: typing.Any) -> None:
        msg = "Ping!"
        await websocket.send_json(
            WebSocketMessage(type="message", data={"text": msg}).dict()
        )

    async def on_disconnect(self, websocket: WebSocket, close_code: int) -> None:
        self.consumer_task.cancel()
        await self.kafka_consumer.stop()

    async def send_message_to_websocket(self, websocket: WebSocket, topic: str):
        while True:
            consumer_data = await self.consume(self.kafka_consumer)
            response = ConsumerResponse(**json.loads(consumer_data), topic=topic)

            await websocket.send_json(
                WebSocketMessage(type="location", data=response.dict()).dict()
            )
