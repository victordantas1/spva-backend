from typing import List, Annotated

from fastapi import APIRouter, Depends, status, UploadFile, Security

from dependecies import get_user_service, get_auth_service, get_current_user
from dependecies.resume_dependencies import get_minio_service
from model import UserApp
from schemas import UserAppOut, UserAppBase
from schemas import UserAppIn
from services import UserAppService, MinioService

router = APIRouter(prefix="/users", tags=["users"])

@router.get("", response_model=List[UserAppOut])
async def get_users(
        service: Annotated[UserAppService, Depends(get_user_service)],
        user: Annotated[UserApp, Security(get_current_user, scopes=["admin"])]
):
    users = service.get_users()
    return users

@router.get('/me', response_model=UserAppOut)
async def get_me(
        service: Annotated[UserAppService, Depends(get_user_service)],
        user: Annotated[UserApp, Security(get_current_user, scopes=["candidate"])]
):
    user = service.get_user_by_id(user.user_id)
    return user

@router.get("/{user_id}", response_model=UserAppOut)
async def get_user(
        user_id: int,
        service: Annotated[UserAppService, Depends(get_user_service)],
        user: Annotated[UserApp, Security(get_current_user, scopes=["admin"])]
):
    user = service.get_user_by_id(user_id)
    return user

@router.post("", response_model=UserAppOut, status_code=status.HTTP_201_CREATED)
async def create_user(
        user: UserAppIn,
        service: Annotated[UserAppService, Depends(get_user_service)],
):
    user = service.create_user(user)
    return user

@router.delete("", response_model=UserAppOut)
async def delete_user(
        service: Annotated[UserAppService, Depends(get_user_service)],
        user: Annotated[UserApp, Security(get_current_user, scopes=["candidate"])]
):
    user = service.delete_user_by_id(user.user_id)
    return user

@router.put("", response_model=UserAppOut)
async def update_user(
        user_in: UserAppIn,
        service: Annotated[UserAppService, Depends(get_user_service)],
        user: Annotated[UserApp, Security(get_current_user, scopes=["candidate"])]
):
    user = service.update_user_by_id(user.user_id, user_in)
    return user

@router.post("/upload_resume", response_model=UserAppOut)
async def upload_resume(
        resume: UploadFile,
        service: Annotated[UserAppService, Depends(get_user_service)],
        minio_service: Annotated[MinioService, Depends(get_minio_service)],
        user: Annotated[UserApp, Security(get_current_user, scopes=["candidate"])]
):
    user_id = user.user_id
    user.resume_path = f'{user.user_id}/{resume.filename}'
    await minio_service.upload_resume(resume, user_id)
    user = service.update_user_by_id(user_id, UserAppIn(user_id=user.user_id,
                                                 first_name=user.first_name,
                                                 last_name=user.last_name,
                                                 email=user.email,
                                                 password=user.password,
                                                 role_id=user.role_id,
                                                 birthdate=user.birthdate,
                                                 resume_path=str(user.resume_path)))
    return user
