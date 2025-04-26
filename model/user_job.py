from sqlalchemy import Date, Enum, String
from datetime import date
from sqlalchemy.orm import mapped_column, Mapped

from model.base_model import Base


class UserJob(Base):
    __tablename__ = 'user_job'
    user_id: Mapped[int] = mapped_column(primary_key=True)
    job_id: Mapped[int] = mapped_column(primary_key=True)
    application_date: Mapped[date] = mapped_column(Date, nullable=False, default=date.today())
    status: Mapped[Enum] = mapped_column(Enum('sent', 'analyse', 'rejected', 'accepted'), nullable=False, default='sent')
    resume_path: Mapped[str] = mapped_column(String(255), nullable=False)