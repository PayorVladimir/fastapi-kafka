import json

import pytest

pytestmark = pytest.mark.asyncio


async def test_producer(test_app, kafka):
    test_data = {"lat": 30.1, "lon": 30.1, "ele": 101.1, "name": "user"}
    response = await test_app.post("api/producer/test", json=test_data)

    assert response.status_code == 200
    msg = await kafka.getone()
    kafka_message_json = json.loads(msg.value.decode())
    assert response.json()["message_id"] == kafka_message_json["message_id"]
