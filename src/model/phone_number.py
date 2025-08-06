from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import mapped_column, Mapped, relationship
from src.model.base_model import Base


class PhoneNumber(Base):
    __tablename__ = 'phone_number'
    phone_number_id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user_app.user_id'), nullable=False)
    number: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)

    user: Mapped["UserApp"] = relationship("UserApp", back_populates="phone_numbers")

    def update_number(self, number: str) -> None:
        self.number = number