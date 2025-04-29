from pydantic import BaseModel


class RoleUserBase(BaseModel):
    name: str

class RoleUserOut(RoleUserBase):
    role_id: int

class RoleUserIn(RoleUserBase):
    pass