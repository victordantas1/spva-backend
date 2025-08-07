from typing import List

from src.schemas import CandidateOut
from src.model import Job, UserApp, Candidate
from src.repository import JobRepository
from src.schemas import JobIn


class JobService:
    def __init__(self, repository: JobRepository):
        self.repository = repository

    def get_job_by_id(self, job_id: int) -> Job:
        job = self.repository.get_job_by_id(job_id)
        return job

    def get_jobs(self) -> List[Job]:
        jobs = self.repository.get_jobs()
        return jobs

    def create_job(self, job: JobIn) -> Job:
        job = self.repository.save_job(Job(**job.dict()))
        return job

    def delete_job_by_id(self, job_id: int) -> Job:
        job = self.repository.delete_job_by_id(job_id)
        return job

    def update_job_by_id(self, job_id: int, job: JobIn) -> Job:
        job = self.repository.update_job_by_id(job_id, job)
        return job

    def get_candidates(self, job_id: int) -> List[CandidateOut]:
        candidates = self.repository.get_candidates(job_id)
        candidates_out = []
        for candidate, application_date, status in candidates:
            candidates_out.append(
                CandidateOut(
                    **candidate.__dict__,
                    application_date=application_date,
                    status=status
                )
            )
        return candidates_out
