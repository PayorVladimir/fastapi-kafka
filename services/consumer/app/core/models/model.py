from pydantic import BaseModel, confloat



class WebSocketMessage(BaseModel):
    type: str
    data: dict

class ConsumerResponse(BaseModel):
    topic: str
    message_id: str
    timestamp: str
    lat: confloat(lt=90, gt=-90)
    lon: confloat(lt=180, gt=-180)
    ele: float
