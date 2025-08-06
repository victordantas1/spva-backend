from datetime import timedelta
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from starlette import status

from dependecies import get_auth_service
from services import AuthService
from src.auth import Token
from config import auth_config

ACCESS_TOKEN_EXPIRE_MINUTES = auth_config['access_token_expires_minutes']

auth_router = APIRouter(prefix='/auth', tags=['auth'])

@auth_router.post("/login")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], auth_service: AuthService = Depends(get_auth_service)) -> Token:
    user = auth_service.authenticate_user(form_data.username, form_data.password)
    scopes = auth_service.get_roles(user)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = auth_service.create_token(
        data={"sub": user.email, "scopes": scopes},
        expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")