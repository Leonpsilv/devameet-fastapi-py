from fastapi import Depends
from src.meet.model import Meet
from src.core.middlewares.error import ApiError
from src.auth.model import User
from src.core.database import SessionLocal, get_db
from src.meet.schema import CreateMeet, UpdateMeet


class MeetService:
    def __init__(self, db: SessionLocal = Depends(get_db)):
        self.db = db

    def create_meet(self, create_meet_dto: CreateMeet):
        meet = Meet(name=create_meet_dto.name, color=create_meet_dto.color)
        self.db.add(meet)
        self.db.commit()
        self.db.refresh(meet)
        return meet
