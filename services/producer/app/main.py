from fastapi import FastAPI
from app.core.config import config


app = FastAPI(title=config.PROJECT_NAME)


@app.get("/ping")
def ping():
    return {"ping": "pong!"}

