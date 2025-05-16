from typing import Annotated

from fastapi import HTTPException, Depends
from jwt import InvalidTokenError
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
        print(user)
        return user

    def create_token(self, data: dict, expires_delta: timedelta) -> str:
        token = create_access_token(data, expires_delta)
        return token

    async def get_current_user(self, token: str) -> UserApp:
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        try:
            payload = decode_token(token)
            username = payload.get("sub")
            if username is None:
                raise credentials_exception
            token_data = TokenData(username=username)
        except InvalidTokenError:
            raise credentials_exception
        user = self.user_repository.get_user_by_email(token_data.username)
        if user is None:
            raise credentials_exception
        return user

