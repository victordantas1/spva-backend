from typing import List, Optional

from sqlalchemy.orm import Session
from sqlalchemy import select
from model import UserApp
from schemas import UserAppIn


class UserAppRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_user_by_id(self, user_id: int) -> Optional[UserApp]:
        return self.session.get(UserApp, user_id)

    def get_users(self) -> List[UserApp]:
        stmt = select(UserApp)
        result = self.session.execute(stmt)
        users = result.scalars().all()
        return list(users)

    def get_user_by_email(self, email: str) -> Optional[UserApp]:
        stmt = select(UserApp).where(UserApp.email == email)
        result = self.session.execute(stmt)
        user = result.scalar()
        return user

    def save_user(self, user: UserApp) -> UserApp:
        try:
            self.session.add(user)
            self.session.commit()
            return user
        except:
            self.session.rollback()
            raise

    def delete_user_by_id(self, user_id: int) -> Optional[UserApp]:
        try:
            user = self.get_user_by_id(user_id)
            self.session.delete(user)
            self.session.commit()
            return user
        except:
            self.session.rollback()
            raise

    def update_user_by_id(self, user_id: int, user: UserAppIn) -> UserApp:
        try:
            user_to_update = self.get_user_by_id(user_id)
            user_to_update.update_attributes(user)
            self.session.commit()
        except:
            self.session.rollback()
            raise
        return user_to_update