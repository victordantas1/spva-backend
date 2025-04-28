from fastapi.params import Depends
from sqlalchemy.orm import Session

from db import get_session
from repository import UserJobRepository, UserAppRepository
from services import UserJobService
from .user_app_dependecies import get_user_repository

def get_user_job_repository(session: Session = Depends(get_session)):
    return UserJobRepository(session)

def get_user_job_service(user_job_repository: UserJobRepository = Depends(get_user_job_repository), user_app_repository: UserAppRepository = Depends(get_user_repository)):
    return UserJobService(user_job_repository, user_app_repository)