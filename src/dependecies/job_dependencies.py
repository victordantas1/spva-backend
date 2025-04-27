from fastapi.params import Depends
from sqlalchemy.orm import Session

from db import get_session
from repository import JobRepository
from services import JobService


def get_job_repository(session: Session = Depends(get_session)):
    return JobRepository(session)

def get_job_service(repository: JobRepository = Depends(get_job_repository)):
    return JobService(repository)