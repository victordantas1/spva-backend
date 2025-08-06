from fastapi.params import Depends
from sqlalchemy.orm import Session

from src.db import get_session
from src.repository import JobRepository
from src.services import JobService


def get_job_repository(session: Session = Depends(get_session)):
    return JobRepository(session)

def get_job_service(repository: JobRepository = Depends(get_job_repository)):
    return JobService(repository)