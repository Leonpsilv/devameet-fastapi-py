from datetime import datetime, timedelta
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from jose import JWTError, jwt
from src.core.middlewares.error import ApiError
from src.core.config import get_settings

config = get_settings()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="Authorization")


class TokenHandler:
    @staticmethod
    def create_access_token(username: str):
        expiration = datetime.utcnow() + timedelta(seconds=config.jwt_expiration)
        data = {"sub": username, "exp": expiration}
        encoded_jwt = jwt.encode(
            data, config.jwt_secret, algorithm=config.jwt_algorithm
        )
        return encoded_jwt

    @staticmethod
    def read_token(token: str):
        try:
            payload = jwt.decode(
                token, config.jwt_secret, algorithms=[config.jwt_algorithm]
            )
            username = payload.get("sub")
            if not username:
                raise ApiError(message="Invalid token", error="TokenError", status_code=401)
            return username
        except JWTError:
            raise ApiError(message="Invalid token", error="TokenError", status_code=401)


def get_current_user(token: str = Depends(oauth2_scheme)):
    return TokenHandler.read_token(token)
