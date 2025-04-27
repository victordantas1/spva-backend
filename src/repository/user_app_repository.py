from typing import Type, List, Optional

from fastapi import Depends
from sqlalchemy.orm import Session
from sqlalchemy import select

from db import get_session
from model import UserApp


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

    def save_user(self, user: UserApp) -> UserApp:
        try:
            self.session.add(user)
            self.session.commit()
            return user
        except:
            self.session.rollback()
            raise

    def delete_user_by_id(self, user_id: int) -> Optional[UserApp]:
        user = self.get_user_by_id(user_id)
        try:
            self.session.delete(user)
            self.session.commit()
            return user
        except:
            self.session.rollback()
            raise
