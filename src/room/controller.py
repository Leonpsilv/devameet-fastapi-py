from fastapi import APIRouter, Body, Depends
from src.auth.handler import get_current_user

from src.room.service import RoomService

router = APIRouter()


@router.get("/{link}")
def get_room(
    link: str,
    service: RoomService = Depends(RoomService),
    username: str = Depends(get_current_user),
):
    return service.get_room(link)


