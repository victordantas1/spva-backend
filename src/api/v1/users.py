from typing import List

from fastapi import APIRouter, Depends
from starlette import status

from dependecies import get_user_service
from schemas import UserAppOut
from schemas.user_app import UserAppIn
from services import UserAppService

router = APIRouter(prefix="/users", tags=["users"])

@router.get("", response_model=List[UserAppOut])
async def get_users(service: UserAppService = Depends(get_user_service)):
    users = service.get_users()
    return users

@router.get("/{user_id}", response_model=UserAppOut)
async def get_user(user_id: int, service: UserAppService = Depends(get_user_service)):
    user = service.get_user_by_id(user_id)
    return user

@router.post("", response_model=UserAppOut, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserAppIn, service: UserAppService = Depends(get_user_service)):
    user = service.create_user(user)
    return user

@router.delete("/{user_id}", response_model=UserAppOut)
async def delete_user(user_id: int, service: UserAppService = Depends(get_user_service)):
    user = service.delete_user_by_id(user_id)
    return user

@router.put("/{user_id}", response_model=UserAppOut)
async def update_user(user: UserAppIn, user_id: int, service: UserAppService = Depends(get_user_service)):
    user = service.update_user_by_id(user_id, user)
    return user
