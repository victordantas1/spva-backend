from typing import List

from pydantic import EmailStr
from sqlalchemy import String, Date, ForeignKey, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import date

from src.model.base_model import Base
from src.schemas.user_app import UserAppIn


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
    email: Mapped[EmailStr] = mapped_column(String(255), nullable=False)
    resume_path: Mapped[str] = mapped_column(String(255))
    role_id: Mapped[int] = mapped_column(ForeignKey('role_user.role_id'), nullable=False)

    github_url: Mapped[str] = mapped_column(String(255), nullable=True)
    linkedin_url: Mapped[str] = mapped_column(String(255), nullable=True)
    portfolio_url: Mapped[str] = mapped_column(String(255), nullable=True)
    city: Mapped[str] = mapped_column(String(100), nullable=True)
    state: Mapped[str] = mapped_column(String(100), nullable=True)
    country: Mapped[str] = mapped_column(String(100), nullable=True)
    work_preference: Mapped[str] = mapped_column(Enum('remote', 'on-site', 'hybrid', name='work_preference_enum'), nullable=True)
    interest_area: Mapped[str] = mapped_column(String(255), nullable=True)

    role: Mapped["RoleUser"] = relationship("RoleUser", back_populates="users")
    phone_numbers: Mapped[list["PhoneNumber"]] = relationship("PhoneNumber", back_populates="user")


    def update_attributes(self, other_user: UserAppIn):
        self.first_name = other_user.first_name
        self.last_name = other_user.last_name
        self.email = other_user.email

        if other_user.birthdate:
            self.birthdate = other_user.birthdate
        if other_user.resume_path:
            self.resume_path = other_user.resume_path
        if other_user.role_id:
            self.role_id = other_user.role_id
        if other_user.github_url:
            self.github_url = other_user.github_url
        if other_user.linkedin_url:
            self.linkedin_url = other_user.linkedin_url
        if other_user.portfolio_url:
            self.portfolio_url = other_user.portfolio_url
        if other_user.city:
            self.city = other_user.city
        if other_user.state:
            self.state = other_user.state
        if other_user.country:
            self.country = other_user.country
        if other_user.work_preference:
            self.work_preference = other_user.work_preference
        if other_user.interest_area:
            self.interest_area = other_user.interest_area

class Administrator(UserApp):
    __mapper_args__ = {
        "polymorphic_identity": 1
    }

    created_jobs: Mapped[list["Job"]] = relationship(
        "Job",
        back_populates="administrator"
    )
    def __repr__(self):
        return f'<UserApp {self.user_id}>, {self.first_name} {self.last_name}, {self.email}, {self.resume_path}'

class Master(Administrator):
    __mapper_args__ = {
        "polymorphic_identity": 2
    }

class Candidate(UserApp):
    __mapper_args__ = {
        "polymorphic_identity": 3
    }

    applications: Mapped[List["UserJob"]] = relationship(back_populates="candidate")

