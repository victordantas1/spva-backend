from datetime import date

from pydantic import BaseModel

from model.enums.category_enum import CategoryEnum


class JobBase(BaseModel):
    user_id: int
    title: str
    description: str
    position: str
    category: CategoryEnum
    create_date: date | None = date.today()

class JobIn(JobBase):
    pass

class JobOut(JobBase):
    job_id: int