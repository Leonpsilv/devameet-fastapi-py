from .model import User
from sqlalchemy.orm import Session
from .schema import Login, Register
from passlib.context import CryptContext
from src.core.database import get_db
from fastapi import Depends


class AuthService:
    def __init__(self, db: Session = Depends(get_db)):
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        self.db = db

    def login(self, dto: Login):
        return {"message": "login success"}

    def register(self, register_dto: Register):
        hashed_password = self.pwd_context.hash(secret=register_dto.password)
        user = User(
            name=register_dto.name,
            avatar=register_dto.avatar,
            username=register_dto.email,
            hashed_password=hashed_password,
        )
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user
