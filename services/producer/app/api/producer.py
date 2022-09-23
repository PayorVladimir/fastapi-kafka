from app.api.schemas import ProducerMessage, ProducerResponse
from app.core.dependencies import get_queue
from app.core.models.model import KafkaMessage
from fastapi import APIRouter, Depends

router = APIRouter()


@router.post("/producer/{topic}", response_model=ProducerResponse)
async def produce(topic: str, message: ProducerMessage, kafa=Depends(get_queue)):
    kafka_message = KafkaMessage(data=message.dict())
    await kafa.send(topic=topic, value=kafka_message.json().encode("utf-8"))
    response = ProducerResponse(**kafka_message.dict(), topic=topic)

    return response
