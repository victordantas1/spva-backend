from datetime import date
from typing import Optional

from pydantic import BaseModel

from model.enums.category_enum import CategoryEnum


class JobBase(BaseModel):
    user_id: int
    title: str
    description: str
    position: str
    category: CategoryEnum
    create_date: date = date.today()
    responsibilities: Optional[str] = None
    requirements: Optional[str] = None
    level: Optional[str] = None
    contract_type: Optional[str] = None
    schedule: Optional[str] = None
    salary_range: Optional[str] = None
    company: Optional[str] = None

class JobIn(JobBase):
    pass

class JobOut(JobBase):
    job_id: int