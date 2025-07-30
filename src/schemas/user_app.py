from datetime import date
from typing import Optional

from fastapi import UploadFile
from pydantic import BaseModel, EmailStr

from model.enums import CategoryEnum


class UserAppBase(BaseModel):
    user_id: Optional[int] = None
    first_name: str
    last_name: str
    email: EmailStr

    class Config:
        from_attributes = True

class UserAppIn(UserAppBase):
    password: Optional[str] = None
    birthdate: Optional[date] = None
    resume_path: Optional[str] = None
    role_id: Optional[int] = None
    phone: Optional[str] = None
    github_url: Optional[str] = None
    linkedin_url: Optional[str] = None
    portfolio_url: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    country: Optional[str] = None
    work_preference: Optional[CategoryEnum] = None
    interest_area: Optional[str] = None

class UserAppOut(UserAppIn):
    pass
