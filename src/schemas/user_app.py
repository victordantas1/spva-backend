from datetime import date

from fastapi import UploadFile
from pydantic import BaseModel, EmailStr

class UserAppBase(BaseModel):
    user_id: int | None = None
    first_name: str
    last_name: str
    email: EmailStr

    class Config:
        orm_mode = True

class UserAppOut(UserAppBase):
    resume_path: str | None = None

class UserAppIn(UserAppBase):
    password: str
    birthdate: date | None = None
    resume_path: str | None = None
    role_id: int | None = 1