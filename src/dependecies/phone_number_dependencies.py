from fastapi.params import Depends
from sqlalchemy.orm import Session

from db import get_session
from repository import PhoneNumberRepository
from services import PhoneNumberService


def get_phone_number_repository(session: Session = Depends(get_session)):
    return PhoneNumberRepository(session)

def get_phone_number_service(repository: PhoneNumberRepository = Depends(get_phone_number_repository)):
    return PhoneNumberService(repository)