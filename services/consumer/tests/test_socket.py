from app.main import app
from fastapi import TestClient


def test_websocket_connection():
    client = TestClient(app)
    with client.websocket_connect("/consumer/stream") as websocket:
        data = websocket.receive_json()

        assert data == {"type": "message", "data": {"text": "Connected!"}}
