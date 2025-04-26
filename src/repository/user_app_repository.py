from typing import Type, List

from sqlalchemy.orm import Session
from model import UserApp


class UserAppRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_user_by_id(self, user_id: int) -> Type[UserApp] | None:
        return self.session.get(UserApp, user_id)

    def get_users(self) -> List[Type[UserApp]]:
        return self.session.query(UserApp).all()
