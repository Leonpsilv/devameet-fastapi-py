from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError
from src.room.gateway import WebSocketServer
from src.core.config import get_settings
from src.core.middlewares.error import ErrorConverterMiddleware, ErrorHandlerMiddleware, handle_http_exception, handle_validation_error
from src.core.middlewares.database_session_middleware import DatabaseSessionMiddleware
from src.core.router import router


def build_api() -> FastAPI:
    application = FastAPI()
    application.add_middleware(DatabaseSessionMiddleware)

    application.add_exception_handler(RequestValidationError, handle_validation_error)
    application.add_exception_handler(HTTPException, handle_http_exception)

    application.add_middleware(ErrorConverterMiddleware)
    application.add_middleware(ErrorHandlerMiddleware)

    application.include_router(router, prefix="/api")

    origins = get_settings().origins.split(', ')
    WebSocketServer(app=application, origins=origins)

    return application


app = build_api()
