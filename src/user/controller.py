from fastapi import APIRouter, Body, Depends

from src.auth.handler import get_current_user
from .service import UserService
from .schema import UpdateUser

router = APIRouter()


@router.get("/")
async def read_user_me(
    username: str = Depends(get_current_user),
    service: UserService = Depends(UserService),
):
    return service.get_user_by_username(username)


@router.put("/{id}")
async def update_user_me(
    id: str,
    dto: UpdateUser = Body(embed=False),
    service: UserService = Depends(UserService),
    username: str = Depends(get_current_user),
):
    return service.update_user(id, username, dto)
