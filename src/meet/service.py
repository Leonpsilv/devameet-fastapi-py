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

    def get_all(self):
        return self.db.query(Meet).all()

    def get_meet_by_id(self, id):
        meet = self.db.query(Meet).filter(Meet.id == id).first()
        if not meet:
            raise ApiError(
                message="Cannot find this meet", error="Bad Request", status_code=404
            )
        return meet

    def update_meet(self, id: str, dto: UpdateMeet):
        meet = self.db.query(Meet).filter(Meet.id == id).first()
        if not meet:
            raise ApiError(
                message="Cannot update this meet", error="Bad Request", status_code=404
            )
        meet.name = dto.name
        meet.color = dto.color

        self.db.commit()
        self.db.refresh(meet)
        return meet

    def delete_meet(self, id: str):
        meet = self.db.query(Meet).filter(Meet.id == id).first()
        if not meet:
            raise ApiError(
                message="Cannot delete this meet", error="Bad Request", status_code=404
            )
        self.db.delete(meet)
        self.db.commit()

        return meet
