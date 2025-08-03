from typing import List

from fastapi import APIRouter, Depends, status

from dependecies import get_job_service, get_current_user
from model import UserApp, Candidate
from schemas import UserAppOut
from schemas import JobOut, JobIn
from services import JobService

router = APIRouter(prefix="/jobs", tags=["jobs"])

@router.get("", response_model=List[JobOut])
async def get_jobs(service: JobService = Depends(get_job_service), user: UserApp = Depends(get_current_user)):
    jobs = service.get_jobs()
    return jobs

@router.get("/{job_id}", response_model=JobOut)
async def get_job(job_id: int, service: JobService = Depends(get_job_service)):
    job = service.get_job_by_id(job_id)
    return job

@router.post("", response_model=JobOut, status_code=status.HTTP_201_CREATED)
async def create_job(job: JobIn, service: JobService = Depends(get_job_service)):
    job = service.create_job(job)
    return job

@router.delete("/{job_id}", response_model=JobOut)
async def delete_job(job_id: int, service: JobService = Depends(get_job_service)):
    job = service.delete_job_by_id(job_id)
    return job

@router.put("/{job_id}", response_model=JobOut)
async def update_job(job: JobIn, job_id: int, service: JobService = Depends(get_job_service)):
    job = service.update_job_by_id(job_id, job)
    return job

@router.get("/{job_id}/candidates", response_model=List[UserAppOut])
async def get_candidates(job_id: int, service: JobService = Depends(get_job_service)):
    candidates = service.get_candidates(job_id)
    return candidates
