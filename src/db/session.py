from sqlalchemy.orm import Session
from sqlalchemy import create_engine

def get_session(db_url: str, db_username: str, db_password: str):
    engine = create_engine(f"mysql+pymysql://{db_username}:{db_password}@{db_url}")
    session = Session(bind=engine)
    return session