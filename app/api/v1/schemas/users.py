from typing import List
from pydantic import BaseModel, EmailStr


class User(BaseModel):
    username: str
    email: EmailStr


class UserCreate(User):
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class ShowUser(User):
    id: int
    is_active: bool

    class Config:
        orm_mode = True


class UserLoginResponse(User):
    access_token: str
    token_type: str

    class Config:
        orm_mode = True
