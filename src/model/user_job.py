from sqlalchemy import Date, Enum, String, ForeignKey
from datetime import date
from sqlalchemy.orm import mapped_column, Mapped, relationship

import src.schemas as schemas
from src.model.base_model import Base
from .enums import StatusEnum


class UserJob(Base):
    __tablename__ = 'user_job'

    user_id: Mapped[int] = mapped_column(ForeignKey('user_app.user_id'), primary_key=True)
    job_id: Mapped[int] = mapped_column(ForeignKey('job.job_id'), primary_key=True)
    application_date: Mapped[date] = mapped_column(Date, nullable=False, default=date.today())
    status: Mapped[StatusEnum] = mapped_column(Enum('sent', 'analyse', 'rejected', 'accepted'), nullable=False, default='sent')
    resume_path: Mapped[str] = mapped_column(String(255), nullable=False)

    def update_user_job(self, user_job: schemas.UserJob) -> None:
        if user_job.resume_path:
            self.resume_path = user_job.resume_path
        if user_job.status:
            self.status = user_job.status
        if user_job.application_date:
            self.application_date = user_job.application_date

    job: Mapped["Job"] = relationship(back_populates="applicants")
    candidate: Mapped["Candidate"] = relationship(back_populates="applications")