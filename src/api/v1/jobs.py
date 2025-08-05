from typing import List, Annotated

from fastapi import APIRouter, Depends, status, Security

from dependecies import get_job_service, get_current_user
from model import UserApp
from schemas import UserAppOut
from schemas import JobOut, JobIn
from services import JobService

router = APIRouter(prefix="/jobs", tags=["jobs"])

@router.get("", response_model=List[JobOut])
async def get_jobs(
        service: Annotated[JobService, Depends(get_job_service)],
        user: Annotated[UserApp, Security(get_current_user, scopes=["candidate"])]
):
    jobs = service.get_jobs()
    return jobs

@router.get("/{job_id}", response_model=JobOut)
async def get_job(
        job_id: int,
        service: Annotated[JobService, Depends(get_job_service)],
        user: Annotated[UserApp, Security(get_current_user, scopes=["candidate"])]
):
    job = service.get_job_by_id(job_id)
    return job

@router.post("", response_model=JobOut, status_code=status.HTTP_201_CREATED)
async def create_job(
        job: JobIn,
        service: Annotated[JobService, Depends(get_job_service)],
        user: Annotated[UserApp, Security(get_current_user, scopes=["admin"])]
):
    job = service.create_job(job)
    return job

@router.delete("/{job_id}", response_model=JobOut)
async def delete_job(
        job_id: int,
        service: Annotated[JobService, Depends(get_job_service)],
        user: Annotated[UserApp, Security(get_current_user, scopes=["admin"])]
):
    job = service.delete_job_by_id(job_id)
    return job

@router.put("/{job_id}", response_model=JobOut)
async def update_job(
        job: JobIn,
        job_id: int,
        service: Annotated[JobService, Depends(get_job_service)],
        user: Annotated[UserApp, Security(get_current_user, scopes=["admin"])]
):
    job = service.update_job_by_id(job_id, job)
    return job

@router.get("/{job_id}/candidates", response_model=List[UserAppOut])
async def get_candidates(
        job_id: int,
        service: Annotated[JobService, Depends(get_job_service)],
        user: Annotated[UserApp, Security(get_current_user, scopes=["admin"])]
):
    candidates = service.get_candidates(job_id)
    return candidates
