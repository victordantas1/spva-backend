from typing import List

from model import UserApp
from repository import UserAppRepository
from schemas.user_app import UserAppIn


class UserAppService:
    def __init__(self, repository: UserAppRepository):
        self.repository = repository

    def get_user_by_id(self, user_id: int) -> UserApp:
        user = self.repository.get_user_by_id(user_id)
        return user

    def get_users(self) -> List[UserApp]:
        users = self.repository.get_users()
        return users

    def create_user(self, user: UserAppIn) -> UserApp:
        user = self.repository.save_user(UserApp(**user.dict()))
        return user

    def delete_user_by_id(self, user_id: int) -> UserApp:
        user = self.repository.delete_user_by_id(user_id)
        return user

    def update_user_by_id(self, user_id: int, user: UserAppIn) -> UserApp:
        user = self.repository.update_user_by_id(user_id, user)
        return user