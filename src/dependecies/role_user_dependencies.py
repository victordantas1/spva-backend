from fastapi.params import Depends
from sqlalchemy.orm import Session

from db import get_session
from repository import RoleUserRepository
from services import RoleUserService


def get_role_user_repository(session: Session = Depends(get_session)):
    return RoleUserRepository(session)

def get_role_user_service(repository: RoleUserRepository = Depends(get_role_user_repository)):
    return RoleUserService(repository)