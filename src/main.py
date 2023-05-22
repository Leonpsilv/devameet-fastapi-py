from fastapi import FastAPI
from src.core.router import router


def build_api() -> FastAPI:
    application = FastAPI()
    application.include_router(router, prefix="/api")

    return application


app = build_api()
