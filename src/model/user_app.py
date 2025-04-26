from sqlalchemy import String, Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import date
from model.base_model import Base


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
    birthdate: Mapped[date] = mapped_column()
    email: Mapped[str] = mapped_column(String(255), nullable=False)
    resume_path: Mapped[str] = mapped_column(String(255), nullable=False)
    role_id: Mapped[int] = mapped_column(ForeignKey('role_user.role_id'), nullable=False)

    role: Mapped["RoleUser"] = relationship("RoleUser", back_populates="users")
    phone_numbers: Mapped[list["PhoneNumber"]] = relationship("PhoneNumber", back_populates="user")


class Candidate(UserApp):
    __mapper_args__ = {
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