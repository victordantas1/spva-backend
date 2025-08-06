from fastapi.params import Depends
from sqlalchemy.orm import Session

from src.db import get_session
from src.repository import RoleUserRepository
from src.services import RoleUserService


def get_role_user_repository(session: Session = Depends(get_session)):
    return RoleUserRepository(session)

def get_role_user_service(repository: RoleUserRepository = Depends(get_role_user_repository)):
    return RoleUserService(repository)