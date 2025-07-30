import io
from typing import List, Annotated

from fastapi import APIRouter, Depends, status, UploadFile, File
from fastapi.params import Header
from minio import Minio

from model import UserApp
from src.auth import TokenData
from dependecies import get_user_job_service, get_current_user
from schemas import UserJob
from services import UserJobService

router = APIRouter(prefix="/user_jobs", tags=["user_job_jobs"])

@router.get("", response_model=List[UserJob])
async def get_user_job_job(service: UserJobService = Depends(get_user_job_service)):
    user_job_job = service.get_user_jobs()
    return user_job_job

@router.get("/{user_id}/{job_id}", response_model=UserJob)
async def get_user_job(user_id: int, job_id: int, service: UserJobService = Depends(get_user_job_service)):
    user_job = service.get_user_job_by_id(user_id, job_id)
    return user_job

@router.post("", response_model=UserJob, status_code=status.HTTP_201_CREATED)
async def create_user_job(user_job: UserJob, service: UserJobService = Depends(get_user_job_service), user: UserApp = Depends(get_current_user)):
    user_job = service.create_user_job(user_job, user)
    return user_job

@router.delete("/{user_id}/{job_id}", response_model=UserJob)
async def delete_user_job(user_id: int, job_id, service: UserJobService = Depends(get_user_job_service)):
    user_job = service.delete_user_job_by_id(user_id, job_id)
    return user_job

@router.put("/{user_id}/{job_id}", response_model=UserJob)
async def update_user_job(user_job: UserJob, user_id: int, job_id: int, service: UserJobService = Depends(get_user_job_service)):
    user_job = service.update_user_job_by_id(user_id, job_id, user_job)
    return user_job