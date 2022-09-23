from pydantic import BaseModel, confloat


class ProducerResponse(BaseModel):
    topic: str
    message_id: str = ""
    timestamp: str = ""


class ProducerMessage(BaseModel):

    lat: confloat(lt=90, gt=-90)
    lon: confloat(lt=180, gt=-180)
    ele: float
    name: str
