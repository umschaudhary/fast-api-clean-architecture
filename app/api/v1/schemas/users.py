from typing import List
from pydantic import BaseModel, EmailStr


class User(BaseModel):
    username: str
    email: EmailStr


class UserCreate(User):
    password: str


class ShowUser(User):
    id: int
    is_active: bool

    class Config():
        orm_mode = True
