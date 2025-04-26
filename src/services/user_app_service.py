from model import UserApp
from repository.user_app_repository import UserAppRepository
from db import get_session

class UserAppService:
    def __init__(self, config):
        self.repository = UserAppRepository(get_session(config["db_url"], config["db_username"], config["db_password"]))
