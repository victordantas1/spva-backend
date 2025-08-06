from typing import List

from src.model import RoleUser
from src.repository import RoleUserRepository
from src.schemas import RoleUserIn


class RoleUserService:
    def __init__(self, repository: RoleUserRepository):
        self.repository = repository

    def get_role_user_by_id(self, role_user_id: int) -> RoleUser:
        role_user = self.repository.get_role_user_by_id(role_user_id)
        return role_user

    def get_role_users(self) -> List[RoleUser]:
        role_users = self.repository.get_role_users()
        return role_users

    def create_role_user(self, role_user: RoleUserIn) -> RoleUser:
        role_user = self.repository.save_role_user(RoleUser(**role_user.dict()))
        return role_user

    def delete_role_user_by_id(self, role_user_id: int) -> RoleUser:
        role_user = self.repository.delete_role_user_by_id(role_user_id)
        return role_user

    def update_role_user_by_id(self, role_user_id: int, role_user: RoleUserIn) -> RoleUser:
        role_user = self.repository.update_role_user_by_id(role_user_id, role_user.name)
        return role_user