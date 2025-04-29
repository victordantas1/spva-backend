from typing import List

from fastapi import APIRouter, Depends, status

from dependecies import get_role_user_service
from schemas import RoleUserOut, RoleUserIn
from services import RoleUserService

router = APIRouter(prefix="/role_users", tags=["role_users"])

@router.get("", response_model=List[RoleUserOut])
async def get_role_users(service: RoleUserService = Depends(get_role_user_service)):
    role_users = service.get_role_users()
    return role_users

@router.get("/{role_user_id}", response_model=RoleUserOut)
async def get_role_user(role_user_id: int, service: RoleUserService = Depends(get_role_user_service)):
    role_user = service.get_role_user_by_id(role_user_id)
    return role_user

@router.post("", response_model=RoleUserOut, status_code=status.HTTP_201_CREATED)
async def create_role_user(role_user: RoleUserIn, service: RoleUserService = Depends(get_role_user_service)):
    role_user = service.create_role_user(role_user)
    return role_user

@router.delete("/{role_user_id}", response_model=RoleUserOut)
async def delete_role_user(role_user_id: int, service: RoleUserService = Depends(get_role_user_service)):
    role_user = service.delete_role_user_by_id(role_user_id)
    return role_user

@router.put("/{role_user_id}", response_model=RoleUserOut)
async def update_role_user(role_user: RoleUserIn, role_user_id: int, service: RoleUserService = Depends(get_role_user_service)):
    role_user = service.update_role_user_by_id(role_user_id, role_user)
    return role_user