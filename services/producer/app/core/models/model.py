import uuid
from datetime import datetime

from pydantic import BaseModel, confloat, validator


class ProducerMessage(BaseModel):

    lat: confloat(lt=90, gt=-90)
    lon: confloat(lt=180, gt=-180)
    ele: float
    name: str


class KafkaMessage(ProducerMessage):
    message_id: str = ""
    timestamp: str = ""

    @validator("message_id", always=True, pre=True)
    def set_message_id(cls, v):
        return str(uuid.uuid4())

    @validator("timestamp", always=True, pre=True)
    def set_message_timestamp(cls, v):
        return str(datetime.utcnow())


class ProducerResponse(BaseModel):
    topic: str
    message_id: str = ""
    timestamp: str = ""
