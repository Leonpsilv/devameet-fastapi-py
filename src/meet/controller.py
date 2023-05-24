from fastapi import APIRouter, Depends
from src.auth.handler import get_current_user

from src.meet.schema import CreateMeet
from src.meet.service import MeetService


router = APIRouter()


@router.post("/")
async def create_meet(
    dto: CreateMeet,
    service: MeetService = Depends(MeetService),
    username: str = Depends(get_current_user),
):
    return service.create_meet(dto)


@router.get("/")
async def get_all_meets(
    service: MeetService = Depends(MeetService),
    username: str = Depends(get_current_user),
):
    return service.get_all_meets()
