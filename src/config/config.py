import os
from dotenv import load_dotenv

load_dotenv()

config = {
    'db_url': os.environ.get('DATABASE_URL'),
    'db_username': os.environ.get('DATABASE_USER'),
    'db_password': os.environ.get('DATABASE_USER_PASSWORD'),
}