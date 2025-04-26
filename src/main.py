from fastapi import FastAPI

from db import get_session
from repository.user_app_repository import UserAppRepository
from config import config

app = FastAPI()

