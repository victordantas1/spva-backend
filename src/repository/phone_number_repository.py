from typing import List, Optional

from sqlalchemy import select
from sqlalchemy.orm import Session

from model import PhoneNumber


class PhoneNumberRepository:
    def __init__(self, session: Session):
        self.session = session
        
    def get_phone_numbers(self) -> List[PhoneNumber]:
        stmt = select(PhoneNumber)
        result = self.session.execute(stmt)
        phone_numbers = result.scalars().all()
        return list(phone_numbers)
    
    def get_phone_number_by_id(self, phone_number_id: int) -> Optional[PhoneNumber]:
        return self.session.get(PhoneNumber, phone_number_id)

    def save_phone_number(self, phone_number: PhoneNumber) -> PhoneNumber:
        try:
            self.session.add(phone_number)
            self.session.commit()
            return phone_number
        except:
            self.session.rollback()
            raise

    def delete_phone_number_by_id(self, phone_number_id: int) -> Optional[PhoneNumber]:
        try:
            phone_number = self.get_phone_number_by_id(phone_number_id)
            self.session.delete(phone_number)
            self.session.commit()
            return phone_number
        except:
            self.session.rollback()
            raise

    def update_phone_number_by_id(self, phone_number_id: int, number: str) -> PhoneNumber:
        try:
            phone_number_to_update = self.get_phone_number_by_id(phone_number_id)
            phone_number_to_update.update_number(number)
            self.session.commit()
        except:
            self.session.rollback()
            raise
        return phone_number_to_update