from sqlalchemy import ForeignKey, String, Text, Enum, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship

from model.base_model import Base
from enums import CategoryEnum
from model.user_app import Administrator, Candidate

from datetime import date

from schemas.job import JobIn


class Job(Base):
    __tablename__ = 'job'
    job_id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user_app.user_id'), nullable=False)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    position: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[CategoryEnum] = mapped_column(Enum('remote', 'on-site', 'hybrid', name='category_enum'), nullable=False)
    create_date: Mapped[date] = mapped_column(Date, nullable=False)

    administrator: Mapped["Administrator"] = relationship("Administrator", back_populates="created_jobs")
    candidates: Mapped["Candidate"] = relationship("Candidate", back_populates="applied_jobs")

    def update_attributes(self, other_job: JobIn):
        self.title = other_job.title
        self.description = other_job.description
        self.position = other_job.position
        self.category = other_job.category
        self.create_date = other_job.create_date