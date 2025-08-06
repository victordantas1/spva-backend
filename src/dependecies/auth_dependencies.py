from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, SecurityScopes
from starlette import status

from src.model import UserApp
from src.repository import UserAppRepository
from src.services import AuthService
from src.dependecies import get_user_repository

def get_auth_service(user_repo: UserAppRepository = Depends(get_user_repository)) -> AuthService:
    return AuthService(user_repo)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login",
                                     scopes={
                                        "candidate": "Read information's about jobs, edit your data and apply to jobs",
                                        "admin": "CRUD Jobs and see jobs candidates",
                                        "master": "Can create admins and has all permissions",
                                     })

async def get_current_user(
    security_scopes: SecurityScopes,
    token: str = Depends(oauth2_scheme),
    auth_service: AuthService = Depends(get_auth_service)
) -> UserApp:
    if security_scopes.scopes:
        authenticate_value = f'Bearer scope="{security_scopes.scope_str}"'
        credentials_exception = None
    else:
        authenticate_value = "Bearer"
        credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": authenticate_value},
    )
    return await auth_service.get_current_user(token, security_scopes, authenticate_value, credentials_exception)