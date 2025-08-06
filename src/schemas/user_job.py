from datetime import date

from pydantic import BaseModel

from src.model.enums import StatusEnum


class UserJob(BaseModel):
    user_id: int | None = None
    job_id: int | None = None
    application_date: date | None = date.today()
    status: StatusEnum | None = 'sent'
    resume_path: str | None = None