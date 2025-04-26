from sqlalchemy.orm import Mapped, mapped_column

from base_model import Base

class RoleUser(Base):
    __tablename__ = "role_user"
    role_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)