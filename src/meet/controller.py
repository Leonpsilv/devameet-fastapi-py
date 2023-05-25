from fastapi import APIRouter, Body, Depends
from src.auth.handler import get_current_user

from src.meet.schema import CreateMeet, UpdateMeet
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
    return service.get_all()


@router.get("/{id}")
async def get_meet_by_id(
    id: str,
    service: MeetService = Depends(MeetService),
    username: str = Depends(get_current_user),
):
    return service.get_meet_by_id(id)


@router.put("/{id}")
async def update_meet(
    id: str,
    dto: UpdateMeet = Body(embed=False),
    service: MeetService = Depends(MeetService),
    username: str = Depends(get_current_user),
):
    return service.update_meet(id, dto)


@router.delete("/{id}")
async def delete_meet(
    id: str,
    service: MeetService = Depends(MeetService),
    username: str = Depends(get_current_user),
):
    return service.delete_meet(id)

@router.get("/{id}/object")
async def get_objects(
    id: str,
    service: MeetService = Depends(MeetService),
    username: str = Depends(get_current_user),
):
    return service.get_objects(id)
