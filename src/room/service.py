from fastapi import Depends
from src.auth.model import User
from src.meet.model import Meet
from src.room.model import Position
from src.core.middlewares.error import ApiError
from src.core.database import SessionLocal, get_db
from src.room.schema import UpdatePosition, ToggleMute


class RoomService:
    def __init__(self, db: SessionLocal = Depends(get_db)):
        self.db = db

    def _get_meet(self, link: str):
        meet = self.db.query(Meet).filter(Meet.link == link).one()
        if not meet:
            raise ApiError(
                message="Cannot find this meet", error="Bad Request", status_code=404
            )
        return meet

    def get_room(self, link: str):
        meet = self._get_meet(link)
        return {
            "link": meet.link,
            "name": meet.name,
            "color": meet.color,
            "objects": meet.object_meets,
        }

    def list_users_position(self, link: str):
        meet = self._get_meet(link)
        return self.db.query(Position).filter(meet.id == Position.meet_id).all()

    def delete_users_position(self, client_id: str):
        self.db.query(Position).filter(Position.client_id == client_id).delete()
        self.db.commit()

    def update_user_position(
        self, user_id: str, link: str, client_id: str, dto: UpdatePosition
    ):
        meet = self._get_meet(link)
        user = self.db.query(User).filter(User.id == user_id).first()
        position = Position(
            x=dto.x,
            y=dto.y,
            orientation=dto.orientation,
            user_id=user.id,
            meet_id=meet.id,
            client_id=client_id,
            name=user.name,
            avatar=user.avatar,
        )
        users_in_room = (
            self.db.query(Position).filter(Position.meet_id == meet.id).all()
        )
        if len(users_in_room) > 20:
            raise ApiError(
                message="Meet is full", error="UpdateMeetError", status_code=400
            )
        if any(
            user
            for user in users_in_room
            if user.user_id == user.id or user.client_id == client_id
        ):
            position = (
                self.db.query(Position).filter(Position.client_id == client_id).one()
            )
            position.x = dto.x
            position.y = dto.y
            position.orientation = dto.orientation
        else:
            self.db.add(position)
        self.db.commit()

    def update_user_mute(self, dto: ToggleMute):
        meet = self._get_meet(dto.link)
        user = self.db.query(User).filter(User.id == dto.user_id).first()
        self.db.query(Position)\
            .filter(Position.meet_id == meet.id)\
            .filter(Position.user_id == user.id)\
            .update({"muted": dto.muted})
        self.db.commit()

    
