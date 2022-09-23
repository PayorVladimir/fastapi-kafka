import uuid
from datetime import datetime

from pydantic import BaseModel, validator


class KafkaMessage(BaseModel):
    message_id: str = ""
    timestamp: str = ""
    data: dict

    @validator("message_id", always=True, pre=True)
    def set_message_id(cls, v):
        return str(uuid.uuid4())

    @validator("timestamp", always=True, pre=True)
    def set_message_timestamp(cls, v):
        return str(datetime.utcnow())
