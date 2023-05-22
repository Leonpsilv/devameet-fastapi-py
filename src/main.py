from fastapi import FastAPI
from src.core.middlewares.database_session_middleware import DatabaseSessionMiddleware
from src.core.router import router


def build_api() -> FastAPI:
    application = FastAPI()
    application.add_middleware(DatabaseSessionMiddleware)
    application.include_router(router, prefix="/api")

    return application


app = build_api()
