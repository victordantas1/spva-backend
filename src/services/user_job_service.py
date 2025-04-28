from typing import List

import model
from model import UserJob

from repository import UserAppRepository, UserJobRepository
from schemas import UserJob


class UserJobService:
    def __init__(self, user_job_repository: UserJobRepository, user_repository: UserAppRepository):
        self.user_repository = user_repository
        self.user_job_repository = user_job_repository

    def get_user_job_by_id(self, user_id: int, job_id: int) -> UserJob:
        user_job = self.user_job_repository.get_user_job_by_id(user_id, job_id)
        return user_job

    def get_user_jobs(self) -> List[UserJob]:
        user_jobs = self.user_job_repository.get_user_jobs()
        return user_jobs

    def create_user_job(self, user_job: UserJob) -> UserJob:
        candidate = self.user_repository.get_user_by_id(user_job.user_id)
        user_job.resume_path = str(candidate.resume_path)
        user_job = self.user_job_repository.save_user_job(model.UserJob(**user_job.dict()))
        return user_job

    def delete_user_job_by_id(self, user_id: int, job_id: int) -> UserJob:
        user_job = self.user_job_repository.delete_user_job_by_id(user_id, job_id)
        return user_job

    def update_user_job_by_id(self, user_id: int, job_id: int, user_job: UserJob) -> UserJob:
        user_job = self.user_job_repository.update_user_job_by_id(user_id, job_id, user_job)
        return user_job