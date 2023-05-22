from fastapi import FastAPI
from src.core.config import get_settings
from src.core.logger import ApiLogger

app = FastAPI()


@app.get("/")
async def root():
    settings = get_settings()
    api_logger = ApiLogger()

    api_logger.debug('this is a debug line')
    return {"message": "hello world"}
