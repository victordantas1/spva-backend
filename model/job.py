from sqlalchemy import ForeignKey, String, Text, Enum, Date
from sqlalchemy.orm import Mapped, mapped_column

from model.base_model import Base


class Job(Base):
    __tablename__ = 'job'
    job_id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user_app.user_id'), nullable=False)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[Text] = mapped_column(nullable=False)
    position: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[Enum] = mapped_column(Enum('remote', 'on-site', 'hybrid', name='category_enum'), nullable=False)
    create_date: Mapped[Date] = mapped_column(Date, nullable=False)