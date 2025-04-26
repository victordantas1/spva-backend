from datetime import date

from sqlalchemy import String, Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from model.base_model import Base
from model.job import Job
from model.phone_number import PhoneNumber
from model.role_user import RoleUser


class UserApp(Base):
    __tablename__ = "user_app"
    __mapper_args__ = {
        "polymorphic_on": "role_id",
        "polymorphic_identity": "user"  # identidade base
    }

    user_id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(255), nullable=False)
    last_name: Mapped[str] = mapped_column(String(255),nullable=False)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    birthdate: Mapped[Date] = mapped_column()
    email: Mapped[str] = mapped_column(String(255), nullable=False)
    resume_path: Mapped[str] = mapped_column(String(255), nullable=False)
    role_id: Mapped[int] = mapped_column(ForeignKey('role_user.role_id'), nullable=False)

    role: Mapped["RoleUser"] = relationship("Role", back_populates="users")
    phone_numbers: Mapped[list["PhoneNumber"]] = relationship("Phone Number", back_populates="user")


class Candidate(UserApp):
    __maped_args__ = {
        "polymorphic_identity": 1
    }

    applied_jobs: Mapped[list["Job"]] = relationship(
        "Job",
        secondary="user_job",
        primaryjoin="Candidate.user_id == UserJob.user_id",
        secondaryjoin="Job.job_id == UserJob.job_id",
        back_populates="candidates"
    )

class Administrator(UserApp):
    __mapper_args__ = {
        "polymorphic_identity": 2
    }

    created_jobs: Mapped[list["Job"]] = relationship(
        "Job",
        back_populates="administrator"
    )