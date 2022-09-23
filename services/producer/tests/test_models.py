import pytest
from app.api.schemas import ProducerMessage, ProducerResponse
from app.core.models.model import KafkaMessage


def test_producer_message():
    test_msg = ProducerMessage(
        name="test_1",
        lat=32.1,
        lon=82.2,
        ele=100,
    )

    assert all([k in test_msg.dict() for k in ["name", "lat", "lon", "ele"]])
    assert isinstance(test_msg.name, str)
    assert isinstance(test_msg.lat, float)
    assert isinstance(test_msg.lon, float)
    assert isinstance(test_msg.ele, float)


def test_producer_response():
    test_msg = ProducerResponse(
        topic="test_1", message_id="test", timestamp="21-09-2022T10:00"
    )

    assert all([k in test_msg.dict() for k in ["topic", "message_id", "timestamp"]])
    assert isinstance(test_msg.topic, str)
    assert isinstance(test_msg.message_id, str)
    assert isinstance(test_msg.timestamp, str)


def test_kafka_message():

    test_msg = KafkaMessage(data={})

    assert all([k in test_msg.dict() for k in ["data", "message_id", "timestamp"]])
    assert isinstance(test_msg.data, dict)
    assert isinstance(test_msg.message_id, str)
    assert isinstance(test_msg.timestamp, str)
