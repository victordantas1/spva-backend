from sqlalchemy.orm import Mapped, mapped_column, relationship

from model.base_model import Base


class RoleUser(Base):
    __tablename__ = "role_user"
    role_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)

    users: Mapped[list["UserApp"]] = relationship("UserApp", back_populates="role")

    def update_role_name(self, role_name: str) -> None:
        self.name = role_name