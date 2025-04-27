from fastapi.params import Depends
from sqlalchemy.orm import Session

from db import get_session
from repository import UserAppRepository
from services import UserAppService


def get_user_repository(session: Session = Depends(get_session)):
    return UserAppRepository(session)

def get_user_service(repository: UserAppRepository = Depends(get_user_repository)):
    return UserAppService(repository)