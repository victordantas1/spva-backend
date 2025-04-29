from pydantic import BaseModel


class PhoneNumberBase(BaseModel):
    phone_number_id: int | None = None
    user_id: int
    number: str | None = None