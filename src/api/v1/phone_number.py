from typing import List

from fastapi import APIRouter, Depends, status

from dependecies import get_phone_number_service
from schemas import PhoneNumberBase
from services import PhoneNumberService

router = APIRouter(prefix="/phone_numbers", tags=["phone_numbers"])

@router.get("", response_model=List[PhoneNumberBase])
async def get_phone_numbers(service: PhoneNumberService = Depends(get_phone_number_service)):
    phone_numbers = service.get_phone_numbers()
    return phone_numbers

@router.get("/{phone_number_id}", response_model=PhoneNumberBase)
async def get_phone_number(phone_number_id: int, service: PhoneNumberService = Depends(get_phone_number_service)):
    phone_number = service.get_phone_number_by_id(phone_number_id)
    return phone_number

@router.post("", response_model=PhoneNumberBase, status_code=status.HTTP_201_CREATED)
async def create_phone_number(phone_number: PhoneNumberBase, service: PhoneNumberService = Depends(get_phone_number_service)):
    phone_number = service.create_phone_number(phone_number)
    return phone_number

@router.delete("/{phone_number_id}", response_model=PhoneNumberBase)
async def delete_phone_number(phone_number_id: int, service: PhoneNumberService = Depends(get_phone_number_service)):
    phone_number = service.delete_phone_number_by_id(phone_number_id)
    return phone_number

@router.put("/{phone_number_id}", response_model=PhoneNumberBase)
async def update_phone_number(phone_number: PhoneNumberBase, phone_number_id: int, service: PhoneNumberService = Depends(get_phone_number_service)):
    phone_number = service.update_phone_number_by_id(phone_number_id, phone_number)
    return phone_number