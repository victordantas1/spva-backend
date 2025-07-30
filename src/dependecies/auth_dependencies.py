from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from model import UserApp
from repository import UserAppRepository
from services import AuthService
from dependecies import get_user_repository

"""def get_auth_service() -> AuthService:
    session = next(get_session())
    user_repo = UserAppRepository(session)
    return AuthService(user_repo)
"""

def get_auth_service(user_repo: UserAppRepository = Depends(get_user_repository)) -> AuthService:
    return AuthService(user_repo)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

async def get_current_user(
    token: str = Depends(oauth2_scheme),
    auth_service: AuthService = Depends(get_auth_service)
) -> UserApp:
    return await auth_service.get_current_user(token)





"""async def get_current_user(auth_service: AuthService = Depends(get_auth_service)) -> UserApp:
    return await auth_service.get_current_user()"""