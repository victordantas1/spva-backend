from typing import List

from model import PhoneNumber
from repository import PhoneNumberRepository
from schemas import PhoneNumberBase


class PhoneNumberService:
    def __init__(self, repository: PhoneNumberRepository):
        self.repository = repository

    def get_phone_number_by_id(self, phone_number_id: int) -> PhoneNumber:
        phone_number = self.repository.get_phone_number_by_id(phone_number_id)
        return phone_number

    def get_phone_numbers(self) -> List[PhoneNumber]:
        phone_numbers = self.repository.get_phone_numbers()
        return phone_numbers

    def create_phone_number(self, phone_number: PhoneNumberBase) -> PhoneNumber:
        phone_number = self.repository.save_phone_number(PhoneNumber(**phone_number.dict()))
        return phone_number

    def delete_phone_number_by_id(self, phone_number_id: int) -> PhoneNumber:
        phone_number = self.repository.delete_phone_number_by_id(phone_number_id)
        return phone_number

    def update_phone_number_by_id(self, phone_number_id: int, phone_number: PhoneNumberBase) -> PhoneNumber:
        phone_number = self.repository.update_phone_number_by_id(phone_number_id, phone_number.number)
        return phone_number