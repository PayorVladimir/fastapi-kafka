from app.core.config import config
from fastapi import FastAPI

app = FastAPI(title=config.PROJECT_NAME)


@app.get("/ping")
def ping():
    return {"ping": "pong!"}
