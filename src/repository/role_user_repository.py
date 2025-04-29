from typing import List, Optional

from sqlalchemy import select
from sqlalchemy.orm import Session

from model import RoleUser
from schemas import RoleUserIn


class RoleUserRepository:
    def __init__(self, session: Session):
        self.session = session
        
    def get_role_users(self) -> List[RoleUser]:
        stmt = select(RoleUser)
        result = self.session.execute(stmt)
        role_users = result.scalars().all()
        return list(role_users)
    
    def get_role_user_by_id(self, role_user_id: int) -> Optional[RoleUser]:
        return self.session.get(RoleUser, role_user_id)

    def save_role_user(self, role_user: RoleUser) -> RoleUser:
        try:
            self.session.add(role_user)
            self.session.commit()
            return role_user
        except:
            self.session.rollback()
            raise

    def delete_role_user_by_id(self, role_user_id: int) -> Optional[RoleUser]:
        try:
            role_user = self.get_role_user_by_id(role_user_id)
            self.session.delete(role_user)
            self.session.commit()
            return role_user
        except:
            self.session.rollback()
            raise

    def update_role_user_by_id(self, role_user_id: int, role_name: str) -> RoleUser:
        try:
            role_user_to_update = self.get_role_user_by_id(role_user_id)
            role_user_to_update.update_role_name(role_name)
            self.session.commit()
        except:
            self.session.rollback()
            raise
        return role_user_to_update