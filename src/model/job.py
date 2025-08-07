from typing import List

from sqlalchemy import ForeignKey, String, Text, Enum, Date, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.model.base_model import Base
from .enums import CategoryEnum
from src.model.user_app import Administrator, Candidate

from datetime import date, datetime

from src.schemas.job import JobIn


class Job(Base):
    __tablename__ = 'job'
    job_id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user_app.user_id'), nullable=False)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    position: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[CategoryEnum] = mapped_column(Enum('remote', 'on-site', 'hybrid', name='category_enum'), nullable=False)
    create_date: Mapped[date] = mapped_column(Date, nullable=False)
    responsibilities: Mapped[str] = mapped_column(Text, nullable=True)
    requirements: Mapped[str] = mapped_column(Text, nullable=True)
    level: Mapped[str] = mapped_column(String(50), nullable=True)
    contract_type: Mapped[str] = mapped_column(String(50), nullable=True)
    schedule: Mapped[str] = mapped_column(String(50), nullable=True)
    salary_range: Mapped[str] = mapped_column(String(50), nullable=True)
    company: Mapped[str] = mapped_column(String(255), nullable=True)
    update_date: Mapped[datetime] = mapped_column(DateTime, nullable=True)

    administrator: Mapped["Administrator"] = relationship("Administrator", back_populates="created_jobs")
    applicants: Mapped[List["UserJob"]] = relationship(back_populates="job")

    def update_attributes(self, other_job: JobIn):
        self.title = other_job.title
        self.description = other_job.description
        self.position = other_job.position
        self.category = other_job.category
        self.create_date = other_job.create_date
        self.responsibilities = other_job.responsibilities
        self.requirements = other_job.requirements
        self.level = other_job.level
        self.contract_type = other_job.contract_type
        self.schedule = other_job.schedule
        self.salary_range = other_job.salary_range
        self.company = other_job.company
        self.update_date = datetime.now()