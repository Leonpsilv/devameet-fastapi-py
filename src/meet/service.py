from fastapi import Depends
from src.auth.model import User
from src.meet.model import Meet, ObjectMeet
from src.core.middlewares.error import ApiError
from src.core.database import SessionLocal, get_db
from src.meet.schema import CreateMeet, UpdateMeet


class MeetService:
    def __init__(self, db: SessionLocal = Depends(get_db)):
        self.db = db

    def create_meet(self, create_meet_dto: CreateMeet, username: str):
        user = self.db.query(User).filter(User.username == username).first()
        meet = Meet(name=create_meet_dto.name, color=create_meet_dto.color, user_id=user.id)
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

        self.db.query(ObjectMeet).filter(ObjectMeet.meet_id == id).delete(synchronize_session=False)
        objects = [
            ObjectMeet(
                name=object_meet.name,
                x=object_meet.x,
                y=object_meet.y,
                z_index=object_meet.zindex,
                orientation=object_meet.orientation,
                meet_id=id
            ) for object_meet in dto.objects
        ]

        self.db.add_all(objects)
        self.db.commit()
        self.db.refresh(meet)
        return {
            **meet.__dict__,
            'objects': [object_meet.__dict__ for object_meet in meet.object_meets]
        }

    def delete_meet(self, id: str):
        meet = self.db.query(Meet).filter(Meet.id == id).first()
        if not meet:
            raise ApiError(
                message="Cannot delete this meet", error="Bad Request", status_code=404
            )
        self.db.delete(meet)
        self.db.commit()

        return meet

    def get_objects(self, id):
        meet = self.db.query(Meet).filter(Meet.id == id).first()
        if not meet:
            raise ApiError(
                message="Cannot find this meet", error="Bad Request", status_code=404
            )
        return meet.object_meets
