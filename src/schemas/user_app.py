from datetime import date

from pydantic import BaseModel, EmailStr

class UserAppBase(BaseModel):
    user_id: int | None = None
    first_name: str
    last_name: str
    email: EmailStr

    class Config:
        orm_mode = True

class UserAppOut(UserAppBase):
    resume_path: str

class UserAppIn(UserAppBase):
    password: str
    birthdate: date
    resume_path: str
    role_id: int
