from datetime import date
from typing import List, Optional, Tuple

from sqlalchemy import select
from sqlalchemy.orm import Session

from src.model.enums import StatusEnum
from src.model import Job, Candidate
from src.schemas import JobIn


class JobRepository:
    def __init__(self, session: Session):
        self.session = session
        
    def get_jobs(self) -> List[Job]:
        stmt = select(Job)
        result = self.session.execute(stmt)
        jobs = result.scalars().all()
        return list(jobs)
    
    def get_job_by_id(self, job_id: int) -> Optional[Job]:
        return self.session.get(Job, job_id)

    def save_job(self, job: Job) -> Job:
        try:
            self.session.add(job)
            self.session.commit()
            return job
        except:
            self.session.rollback()
            raise

    def delete_job_by_id(self, job_id: int) -> Optional[Job]:
        try:
            job = self.get_job_by_id(job_id)
            self.session.delete(job)
            self.session.commit()
            return job
        except:
            self.session.rollback()
            raise

    def update_job_by_id(self, job_id: int, job: JobIn) -> Job:
        try:
            job_to_update = self.get_job_by_id(job_id)
            job_to_update.update_attributes(job)
            self.session.commit()
        except:
            self.session.rollback()
            raise
        return job_to_update

    def get_candidates(self, job_id: int) -> List[Tuple[Candidate, date, StatusEnum]]:
        job = self.session.get(Job, job_id)
        candidates = []
        for application in job.applicants:
            candidates.append((application.candidate, application.application_date, application.status))
        return candidates
