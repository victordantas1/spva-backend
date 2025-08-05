from typing import Annotated

from fastapi import HTTPException, Depends
from fastapi.security import SecurityScopes
from jwt import InvalidTokenError
from pydantic import ValidationError
from starlette import status
from auth import *
from model import UserApp
from repository import UserAppRepository

class AuthService:
    def __init__(self, user_repository: UserAppRepository):
        self.user_repository = user_repository

    def authenticate_user(self, username: str, password: str):
        user = self.user_repository.get_user_by_email(username)
        if not user:
            return False
        if not verify_password(password, user.password):
            return False
        return user

    def create_token(self, data: dict, expires_delta: timedelta) -> str:
        token = create_access_token(data, expires_delta)
        return token

    async def get_current_user(self, token: str, security_scopes: SecurityScopes, authenticate_value, credentials_exception) -> UserApp:
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            username = payload.get("sub")
            if username is None:
                raise credentials_exception
            token_scopes = payload.get("scopes", [])
            token_data = TokenData(scopes=token_scopes, username=username)
        except (InvalidTokenError, ValidationError):
            raise credentials_exception
        user = self.user_repository.get_user_by_email(token_data.username)
        if user is None:
            raise credentials_exception
        for scope in security_scopes.scopes:
            if scope not in token_data.scopes:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Not enough permissions",
                    headers={"WWW-Authenticate": authenticate_value},
                )
        return user

